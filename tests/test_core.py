"""Hattın dayandığı varsayımların testleri."""

import numpy as np
import pandas as pd
import pytest

from voynich_lab.abc import analyze_view
from voynich_lab.checks import (
    degradation_experiment,
    evaize,
    homogeneity_experiment,
    homophonic,
    lexicon_stats,
    markov_surrogate,
    order_stats,
    spelling_noise,
    word_families,
)
from voynich_lab.manuscripts import (
    GROWTH_B,
    MEAN_A,
    MEAN_B,
    SD_A,
    SD_B,
    growth_profile,
    simulate_manuscript,
    t_statistic,
    voynich_reference,
)
from voynich_lab.manuscripts import analyze_view as analyze_manuscripts
from voynich_lab.probe import profile, summarize
from voynich_lab.probe import run as run_probe
from voynich_lab.search import perturb, prior_for, run_search

from voynich_lab.corpus import load_period, normalize
from voynich_lab.fetch import _html_to_text
from voynich_lab.dataset import _truncate
from voynich_lab.features import FEATURE_NAMES, _is_ed1, extract_features
from voynich_lab.generators import (
    LAYOUT_PRIOR,
    PROCESS_PRIOR,
    Allographs,
    GIBBERISH_PROCESSES,
    LANGUAGE_PROCESSES,
    Forms,
    Layout,
    Mark,
    _slot_alphabets,
    layout_from_params,
    layout_params,
    lay_out,
    sample_layout,
)
from voynich_lab.transliteration import (
    _merge_eva_ligatures,
    ivtff_page_variables,
    load_ivtff,
    load_takahashi,
    load_v101,
    to_windows,
)

TEXT = (
    "in principio creavit deus caelum et terram terra autem erat inanis et vacua "
    "et tenebrae super faciem abyssi et spiritus dei ferebatur super aquas"
).split() * 40


def _lines(seed=0):
    return lay_out(list(TEXT), np.random.default_rng(seed), Layout())


def test_features_are_finite_and_complete():
    f = extract_features(_lines())
    assert list(f) == FEATURE_NAMES
    assert all(np.isfinite(v) for v in f.values())


def test_monoalphabetic_substitution_is_invisible():
    """İkame şifresi feature'ları değiştirmemeli: 'plain' sınıfının gerekçesi."""
    lines = _lines()
    alphabet = sorted({ch for ln in lines for w in ln for ch in w})
    perm = np.random.default_rng(1).permutation(len(alphabet))
    table = {a: chr(0x4E00 + int(p)) for a, p in zip(alphabet, perm)}
    enc = [["".join(table[c] for c in w) for w in ln] for ln in lines]
    a, b = extract_features(lines), extract_features(enc)
    for k in FEATURE_NAMES:
        assert a[k] == pytest.approx(b[k], abs=1e-9), k


def test_entropy_of_uniform_symbols():
    rng = np.random.default_rng(0)
    words = ["".join(rng.choice(list("abcdefgh"), size=4)) for _ in range(4000)]
    f = extract_features(lay_out(words, rng, Layout()))
    assert f["n_symbols"] == 8
    assert f["eff_symbols"] == pytest.approx(8, rel=0.01)


def test_edit_distance_one():
    assert _is_ed1("daiin", "dain")
    assert _is_ed1("daiin", "saiin")
    assert not _is_ed1("daiin", "daiin")
    assert not _is_ed1("daiin", "okain")


@pytest.mark.parametrize("name", list(LANGUAGE_PROCESSES))
def test_language_processes(name):
    lines = LANGUAGE_PROCESSES[name](list(TEXT), np.random.default_rng(3))
    words = [w for ln in lines for w in ln]
    assert len(words) >= len(TEXT)
    assert all(words)


@pytest.mark.parametrize("name", list(GIBBERISH_PROCESSES))
def test_gibberish_processes_are_deterministic(name):
    a = GIBBERISH_PROCESSES[name](500, np.random.default_rng(5))
    b = GIBBERISH_PROCESSES[name](500, np.random.default_rng(5))
    assert a == b
    assert sum(len(ln) for ln in a) >= 500
    assert all(w for ln in a for w in ln)


def test_layout_without_marks_only_breaks_lines():
    """İşaretsiz düzen kelimeleri değiştirmez, yalnız satıra böler."""
    lines = lay_out(list(TEXT), np.random.default_rng(0), Layout(para_lines=5, width_jitter=0.3))
    assert [w for ln in lines for w in ln] == TEXT
    assert all(lines)


def test_width_wrapping_lengthens_line_initial_words():
    """Genişliğe göre doldurma tek başına satır başı kelimelerini uzun yapar.

    Sığmayan kelime alt satıra iner ve sığmayan çoğunlukla uzun kelimedir. Bu
    yüzden len_ratio_line_initial > 1 kendi başına bulgu değildir. Satır sonunda
    aynı kayma yoktur: orada 1'den sapma doldurmayla açıklanamaz.
    """
    first, last = [], []
    for seed in range(10):
        rng = np.random.default_rng(seed)
        words = [TEXT[i] for i in rng.permutation(len(TEXT))]
        f = extract_features(lay_out(words, rng, Layout(width_jitter=0.2)))
        first.append(f["len_ratio_line_initial"])
        last.append(f["len_ratio_line_final"])
    assert min(first) > 1.05
    assert abs(np.mean(last) - 1) < 0.03


def test_line_marks_land_on_line_edges():
    new_glyph = Mark(p=1.0, mode="add", glyphs=(1.0,), weights=(1.0,))
    plain_lines = _lines()
    marked = lay_out(
        list(TEXT),
        np.random.default_rng(0),
        Layout(line_initial=new_glyph, line_final=Mark(1.0, "abbreviate", (2.0,), (1.0,))),
    )
    assert len({ln[0][0] for ln in marked}) == 1  # her satır aynı yeni glifle başlar
    assert len({ln[-1][-1] for ln in marked}) == 1
    assert {ln[0][0] for ln in marked} != {ln[-1][-1] for ln in marked}
    inner = {ch for ln in marked for w in ln[1:-1] for ch in w}
    assert marked[0][0][0] not in inner and marked[0][-1][-1] not in inner
    a, b = extract_features(plain_lines), extract_features(marked)
    assert b["jsd_line_initial"] > a["jsd_line_initial"] + 0.3
    assert b["jsd_line_final"] > a["jsd_line_final"] + 0.3


def test_final_forms_separate_last_glyph_completely():
    """Her glifin ayrı son biçimi varsa kelime sonu glifleri başka yerde hiç görünmez."""
    plain_lines = _lines()
    formed = lay_out(list(TEXT), np.random.default_rng(0), Layout(final_forms=Forms(1.0)))
    assert [[len(w) for w in ln] for ln in formed] == [[len(w) for w in ln] for ln in plain_lines]
    a, b = extract_features(plain_lines), extract_features(formed)
    assert b["jsd_last"] == pytest.approx(1.0)
    assert b["n_symbols"] > a["n_symbols"]
    assert b["wlen_mean"] == a["wlen_mean"] and b["ttr"] == a["ttr"]  # bilgi kaybı yok


def test_shared_final_forms_lose_information():
    """Glifler tek ortak son biçime düşerse (kısaltma işareti) kelime türleri birleşir."""
    a = extract_features(_lines())
    merged = lay_out(list(TEXT), np.random.default_rng(0), Layout(final_forms=Forms(1.0, k=1)))
    b = extract_features(merged)
    assert len({w[-1] for ln in merged for w in ln}) == 1
    assert b["ttr"] <= a["ttr"] and b["last_entropy_ratio"] == 0.0


def test_allographs_add_rare_symbols_only():
    a = extract_features(_lines())
    lines = lay_out(list(TEXT), np.random.default_rng(0), Layout(allographs=Allographs(2.0, 0.05)))
    b = extract_features(lines)
    assert [w for ln in lines for w in ln] != TEXT
    assert b["n_symbols"] > a["n_symbols"] + 10
    # Eklenenler nadir: sembol sayısı çok artar, etkin sembol sayısı az artar.
    assert b["eff_symbols"] - a["eff_symbols"] < 0.25 * (b["n_symbols"] - a["n_symbols"])
    assert b["wlen_mean"] == a["wlen_mean"]


def test_slot_alphabets_overlap_extremes():
    alphabet = list("abcdefghijklmnop")
    apart = _slot_alphabets(alphabet, 3, 0.0, np.random.default_rng(0))
    assert sorted(g for slot in apart for g in slot) == alphabet  # ayrık ve eksiksiz
    assert all(apart)
    shared = _slot_alphabets(alphabet, 3, 1.0, np.random.default_rng(0))
    assert all(sorted(slot) == alphabet for slot in shared)


def test_layout_prior_is_deterministic_and_includes_no_effect_case():
    layouts = [sample_layout(np.random.default_rng(i)) for i in range(200)]
    assert layouts[3] == sample_layout(np.random.default_rng(3))
    bare = [
        lo
        for lo in layouts
        if not (
            lo.line_initial or lo.line_final or lo.para_initial
            or lo.final_forms or lo.initial_forms or lo.allographs
        )
    ]
    assert bare  # "hiç satır etkisi yok" durumu evrenin içinde
    assert any(lo.line_initial for lo in layouts) and any(lo.line_final for lo in layouts)


def test_truncate_gives_exact_window():
    assert sum(len(ln) for ln in _truncate(_lines(), 500)) == 500


def test_normalize_scripts():
    assert normalize("Dixitque Deus: fiat lux!") == ["dixitque", "deus", "fiat", "lux"]
    assert normalize("Başlangıçta, Tanrı göğü") == ["başlangıçta", "tanrı", "göğü"]
    # İbranice nikud atılır, harfler kalır.
    assert normalize("בְּרֵאשִׁית") == ["בראשית"]


def test_takahashi_parser(tmp_path):
    p = tmp_path / "t.txt"
    p.write_text(
        "<f1r.P1.1;H>       fachys.ykal.ar.cTh!res.Shol-\n"
        "<f1r.L1.2;H>       otol=\n"
        "<f1r.P1.3;H>       *.odar.cTh*ar.daiin=\n"
        "<f1v.P.1;H>        kchsy.ol-oltchey.am-\n",
        encoding="utf-8",
    )
    lines = load_takahashi(p, "basic")
    assert [ln.words for ln in lines] == [
        ["fachys", "ykal", "ar", "cthres", "shol"],
        ["odar", "daiin"],
        ["kchsy", "ol", "oltchey", "am"],  # satır içi "-" çizim boşluğu: kelime sınırı
    ]
    glyph = load_takahashi(p, "glyph")
    assert len(glyph[0].words[3]) == len("cthres") - 2  # cth tek sembol
    assert len(_merge_eva_ligatures("chckhy")) == 3


def test_ivtff_parser(tmp_path):
    p = tmp_path / "zl.txt"
    p.write_text(
        "#=IVTFF Eva- 2.0 M 5\n"
        "<f1r>      <! $Q=A $P=A>\n"
        "# page 1\n"
        "<f1r.1,@P0>       <%>fachys.ykal.[cth:oto]res.y<!@254;>\n"
        "<f1r.2,+P0>       sory.or,y.d?n.{c'y}.sh{c'y}<$>\n"
        "<f1r.6,=Pt>       ydaraishy<$>\n"
        "<f1v.1,@P0>       <%>kchsy.ol<->o,l.dam@175;\n",
        encoding="latin-1",
    )
    lines = load_ivtff(p)
    assert [ln.folio for ln in lines] == ["1r", "1r", "1v"]
    assert lines[0].words == ["fachys", "ykal", "cthres", "y"]
    # d?n okunamadığı için atılır; {c'y} tek nadir glif olur ve her yerde aynı semboldür
    assert lines[1].words[:3] == ["sory", "or", "y"]
    rare = lines[1].words[3]
    assert len(rare) == 1 and lines[1].words[4] == "sh" + rare
    assert lines[2].words[:4] == ["kchsy", "ol", "o", "l"] and len(lines[2].words[4]) == 4
    assert load_ivtff(p, comma_is_space=False)[1].words[1] == "ory"
    assert len(load_ivtff(p, "glyph")[0].words[2]) == len("cthres") - 2
    assert ivtff_page_variables(p) == {"1r": {"Q": "A", "P": "A"}}


def test_v101_parser(tmp_path):
    p = tmp_path / "v.txt"
    p.write_text("<1r.1>fa19s.9,hae.ay-\n<67r1.labels_2>oy9=\n", encoding="utf-8")
    assert [ln.words for ln in load_v101(p)] == [["fa19s", "9", "hae", "ay"]]
    assert [ln.words for ln in load_v101(p, comma_is_space=False)] == [["fa19s", "9hae", "ay"]]


def test_windows_drop_incomplete_tail(tmp_path):
    p = tmp_path / "t.txt"
    p.write_text("".join(f"<f{i}r.P.1;H> a.b.c.d.e=\n" for i in range(1, 8)), encoding="utf-8")
    wins = to_windows(load_takahashi(p), 10)
    assert len(wins) == 3
    assert wins[0][0] == "1r..2r"


def test_params_are_recorded_without_changing_output():
    """Ayar kaydı (ABC için) üretilen metni değiştirmemeli."""
    for name, proc in GIBBERISH_PROCESSES.items():
        rec: dict = {}
        assert proc(300, np.random.default_rng(5), rec=rec) == proc(300, np.random.default_rng(5))
        assert any(k.startswith("p_") for k in rec), name
        assert "l_words_per_line" in rec and "l_final_forms_share" in rec, name
    for name, proc in LANGUAGE_PROCESSES.items():
        rec = {}
        a = proc(list(TEXT), np.random.default_rng(3), rec=rec)
        assert a == proc(list(TEXT), np.random.default_rng(3))
        assert "l_line_final_p" in rec, name
    rec = {}
    LANGUAGE_PROCESSES["verbose"](list(TEXT), np.random.default_rng(3), rec=rec)
    assert "p_split" in rec


def test_abc_finds_matching_class_and_its_parameters():
    """ABC: hedefe uyan sınıf öz mesafe aralığına girer, uymayan girmez;
    yalnız belli ayarda uyan sınıfta o ayar önselden kayar."""
    rng = np.random.default_rng(0)
    k = len(FEATURE_NAMES)

    def table(mean, label, n=600):
        knob = rng.uniform(0, 1, n)
        X = rng.normal(0, 1, (n, k)) + np.outer(mean(knob), np.ones(k))
        return pd.DataFrame(X, columns=FEATURE_NAMES).assign(label=label, p_knob=knob)

    voy = pd.DataFrame(rng.normal(0, 1, (16, k)), columns=FEATURE_NAMES)
    df = pd.concat(
        [
            table(lambda u: 0 * u, "matches"),
            table(lambda u: 0 * u + 4, "never"),
            table(lambda u: 6 * (1 - u), "tuned"),  # yalnız knob 1'e yakınken uyar
        ],
        ignore_index=True,
    )
    r = analyze_view(df, voy, accept=0.05)
    limit = r["self_distance"]["max"]
    c = r["classes"]
    assert c["matches"]["accepted_median_distance"] < limit
    assert c["never"]["best_distance"] > limit and c["never"]["share_within_self_max"] == 0
    assert c["matches"]["share_within_self_max"] > 0.5
    knob = c["tuned"]["param_shifts"][0]
    assert knob["param"] == "p_knob" and knob["quantile_in_prior"] > 0.9
    assert abs(c["matches"]["param_shifts"][0]["quantile_in_prior"] - 0.5) < 0.25


def test_evaize_splits_six_glyphs_into_shared_strokes():
    lines = GIBBERISH_PROCESSES["grille"](600, np.random.default_rng(2), Layout())
    split = evaize(lines)
    a, b = extract_features(lines), extract_features(split)
    assert [len(ln) for ln in split] == [len(ln) for ln in lines]  # kelime sayısı aynı
    assert b["wlen_mean"] > a["wlen_mean"]
    # Altı glif gider, iki ortak çizgi gelir.
    assert b["n_symbols"] == a["n_symbols"] - 6 + 2
    assert evaize([["ab", "ba"] * 30]) is None  # alfabe çok küçük



def test_priors_cover_what_is_drawn():
    """Arama sınırları (PRIOR tabloları) ile üreteçlerin gerçekte çektiği aralık aynı olmalı."""
    seen: dict[str, dict[str, list[float]]] = {}
    for i in range(150):
        for name, proc in GIBBERISH_PROCESSES.items():
            rec: dict = {}
            proc(120, np.random.default_rng(i), rec=rec)
            for key, v in rec.items():
                seen.setdefault(name, {}).setdefault(key, []).append(float(v))
        for name in ("verbose", "codebook"):
            rec = {}
            LANGUAGE_PROCESSES[name](TEXT[:300], np.random.default_rng(i), rec=rec)
            for key, v in rec.items():
                seen.setdefault(name, {}).setdefault(key, []).append(float(v))
    for name, cols in seen.items():
        prior = prior_for(name)
        drawn = {k for k in cols if k != "p_code_len_mean"}
        assert drawn == set(prior), (name, drawn ^ set(prior))
        for key, (lo, hi, kind) in prior.items():
            vals = np.array([v for v in cols[key] if not np.isnan(v)])
            on = vals[vals > 0] if kind == "m" else vals
            assert on.min() >= lo - 1e-9 and on.max() <= hi + 1e-9, (name, key, on.min(), on.max())
    assert set(PROCESS_PRIOR) == set(LANGUAGE_PROCESSES) | set(GIBBERISH_PROCESSES)


def test_fixed_params_are_honoured():
    fixed = {"p_rows": 77, "p_len_mid": 5, "p_slot_overlap": 0.0, "p_alphabet": 20}
    rec: dict = {}
    lines = GIBBERISH_PROCESSES["grille"](400, np.random.default_rng(1), Layout(), rec, fixed)
    assert all(rec[k] == v for k, v in fixed.items())
    assert extract_features(lines)["n_symbols"] <= 20
    rec = {}
    GIBBERISH_PROCESSES["selfcite"](200, np.random.default_rng(1), Layout(), rec, {"p_reach": 30, "p_copy": 0.9})
    assert rec["p_reach"] == 30 and rec["p_copy"] == 0.9


def test_layout_params_round_trip():
    for i in range(50):
        rng = np.random.default_rng(i)
        params = layout_params(sample_layout(rng))
        back = layout_params(layout_from_params(params, rng))
        for key in LAYOUT_PRIOR:
            a, b = params[key], back[key]
            assert (np.isnan(a) and np.isnan(b)) or a == pytest.approx(b), (i, key, a, b)
    off = layout_from_params({k: 0.0 for k in LAYOUT_PRIOR} | {"l_words_per_line": 8.0}, np.random.default_rng(0))
    assert off == Layout(words_per_line=8.0)


def test_perturb_stays_inside_prior():
    rng = np.random.default_rng(0)
    prior = prior_for("grille")
    theta = {k: (lo if kind != "m" else 0.0) for k, (lo, hi, kind) in prior.items()}
    for _ in range(300):
        theta = perturb(theta, {k: 10.0 for k in prior}, prior, [], rng)
        for key, (lo, hi, kind) in prior.items():
            v = theta[key]
            assert (kind == "m" and v == 0) or lo <= v <= hi, (key, v)
            assert kind not in ("i", "log", "b") or v == round(v), (key, v)


def test_search_runs_and_is_deterministic():
    k = len(FEATURE_NAMES)
    job = {
        "label": "grille", "view": "t", "raw": "unused", "window": 200,
        "center": [0.0] * k, "scale": [1.0] * k, "self_max": 1.0, "languages": [],
        "init": [{} for _ in range(4)], "keep": 4, "children": 2, "rounds": 2, "fresh": 1,
        "seed": [1, 2, 3],
    }  # fmt: skip
    a, b = run_search(job), run_search(job)
    assert a == b
    assert len(a["round_medians"]) == 2 and a["n_fresh"] == 4
    assert np.isfinite(a["fresh_median_distance"])


def test_homogeneity_experiment_reports_within_and_between():
    rng = np.random.default_rng(0)
    k = len(FEATURE_NAMES)
    df = pd.DataFrame(rng.normal(0, 1, (50, k)), columns=FEATURE_NAMES)
    voy = {"v": pd.DataFrame(rng.normal(0, 1, (6, k)), columns=FEATURE_NAMES)}
    r = homogeneity_experiment(df, voy, window_words=200, n_manuscripts=2, n_windows=2)
    res = r["views"]["v"]
    assert set(res) == {"voynich_within"} | set(GIBBERISH_PROCESSES)
    assert all(res[p]["within"] >= 0 and res[p]["between"] >= 0 for p in GIBBERISH_PROCESSES)
    assert 0 < res["voynich_within"] < 2


def test_manuscript_is_reproducible_and_has_one_table():
    a = simulate_manuscript("grille", {}, "unused", 300, 4, [1, 2, 3])
    b = simulate_manuscript("grille", {}, "unused", 300, 4, [1, 2, 3])
    assert a is not None and np.array_equal(a[0], b[0]) and a[1] == b[1] and a[2] == b[2]
    assert len(a[2]) == 2 and all(0 < x <= 1 for half in a[2] for x in half)
    assert a[0].shape == (4, len(FEATURE_NAMES))
    # Ayarlar sabitlenince kayıt aynı ayarları gösterir, tohum değişince metin değişir.
    theta = {k: v for k, v in a[1].items() if k in prior_for("grille")}
    c = simulate_manuscript("grille", theta, "unused", 300, 4, [9, 9, 9])
    assert c[1]["p_rows"] == a[1]["p_rows"] and not np.array_equal(c[0], a[0])


def test_t_statistic_is_about_one_for_exchangeable_halves():
    rng = np.random.default_rng(0)
    V = rng.normal(0, 1, (400, len(FEATURE_NAMES)))
    scale = V.std(0, ddof=1)
    ref = voynich_reference(V[:16], V[:16].std(0, ddof=1), 8, n_splits=300)
    assert 0.6 < ref["random_median"] < 1.4
    a, b = V[:200], V[200:]
    assert 0.6 < float(t_statistic(a.mean(0), 200, b.mean(0), 200, scale)) < 1.4
    assert float(t_statistic(a.mean(0) + 1, 200, b.mean(0), 200, scale)) > 5


def test_manuscript_analysis_validates_on_the_other_half():
    """Seçim yarısında şansla yakın çıkan aday doğrulama yarısında yakalanır."""
    rng = np.random.default_rng(1)
    k = len(FEATURE_NAMES)
    V = rng.normal(0, 1, (16, k))

    def table(label, mean_a, mean_b, n=200):
        d = {"label": label, "index": np.arange(n)}
        d |= dict(zip(MEAN_A, (rng.normal(mean_a, 0.35, (n, k))).T))
        d |= dict(zip(MEAN_B, (rng.normal(mean_b, 0.35, (n, k))).T))
        d |= dict(zip(SD_A, np.ones((k, n)))) | dict(zip(SD_B, np.ones((k, n))))
        return pd.DataFrame(d)

    df = pd.concat([table("grille", 0, 0), table("selfcite", 0, 3)], ignore_index=True)
    r = analyze_manuscripts(df, V, np.ones(k), half=8, top=20)
    c = r["classes"]
    assert c["grille"]["validation_median"] < 2 and c["selfcite"]["validation_median"] > 5
    assert c["selfcite"]["selection_median"] < 2  # seçim yarısında iyi görünüyordu
    assert c["grille"]["validation_share_within_p95"] > 0.3


def test_growth_profile_separates_closed_and_open_vocabularies():
    """Kapalı dağarcık uzun metinde doyar (hapax azalır), açık dağarcık doymaz."""
    rng = np.random.default_rng(0)
    closed = [f"w{i}" for i in rng.integers(0, 300, 8000)]
    opened = [f"w{i}" for i in (rng.pareto(1.0, 8000) * 50).astype(int)]
    c, o = growth_profile(closed), growth_profile(opened)
    assert c[0] < 0.05 and c[1] < 0.01  # 300 türün hepsi çok kez geçer
    assert o[0] > 2 * c[0] and o[1] > 0.3
    assert growth_profile(["daiin", "dain", "aiin", "okeey"])[2] == 0.75


def test_manuscript_analysis_reports_growth_fit():
    rng = np.random.default_rng(2)
    k = len(FEATURE_NAMES)
    V = rng.normal(0, 1, (16, k))
    n = 100
    d = {"label": "grille", "index": np.arange(n)}
    d |= dict(zip(MEAN_A, rng.normal(0, 0.35, (k, n)))) | dict(zip(MEAN_B, rng.normal(0, 0.35, (k, n))))
    d |= dict(zip(SD_A, np.ones((k, n)))) | dict(zip(SD_B, np.ones((k, n))))
    G = np.tile([0.2, 0.6, 0.9], (n, 1))
    G[: n // 2, 1] = 0.3  # yarısı hapax'ta uymuyor
    d |= dict(zip(GROWTH_B, G.T))
    r = analyze_manuscripts(pd.DataFrame(d), V, np.ones(k), 8, 10, [[0.21, 0.61, 0.9], [0.19, 0.6, 0.89]])
    g = r["classes"]["grille"]["growth"]
    assert g["n_fitting"] == n // 2 and g["best_t_among_fitting"] is not None
    assert r["growth_reference"]["first_half"]["hapax"] == 0.61


def test_codebook_is_one_to_one_on_word_types():
    """Kod defteri kelime türlerini bire bir eşler: dağarcık ölçüleri düz metinle aynı kalır."""
    for seed in range(8):
        lines = LANGUAGE_PROCESSES["codebook"](list(TEXT), np.random.default_rng(seed), Layout())
        coded = [w for ln in lines for w in ln]
        assert len(coded) == len(TEXT)
        mapping: dict[str, str] = {}
        for plain_word, code in zip(TEXT, coded):
            assert mapping.setdefault(plain_word, code) == code  # aynı kelime hep aynı kod
        assert len(set(mapping.values())) == len(mapping)  # farklı kelime farklı kod
        a, b = extract_features(_lines()), extract_features(lines)
        assert b["ttr"] == a["ttr"] and b["hapax_ratio"] == a["hapax_ratio"]


def test_probe_flags_closed_vocabulary_before_any_chain_run():
    """Ön sınama: doyan dağarcık büyüme bandına giremez, açık dağarcık girebilir."""
    def closed(rng):
        return GIBBERISH_PROCESSES["grille"](1500, rng, Layout(), fixed={"p_rows": 60, "p_n_grilles": 3})

    df = run_probe(closed, n=3, window_words=300, n_windows=4)
    assert len(df) == 3 and {"ttr", "hapax", "ed1", "h2"} <= set(df.columns)
    assert df["ttr"].max() < 0.2  # 180 kelimelik döngü kendini tekrar eder
    target = {"ttr": 0.27, "hapax": 0.7, "ed1": 0.88}
    target |= {k: 0.0 for k in df.columns if k not in target}
    s = summarize(df, {"v": target})
    assert s["views"]["v"]["n_fitting_growth"] == 0 and not s["passes"]
    near = df.copy()
    near[["ttr", "hapax", "ed1"]] = [0.26, 0.69, 0.9]
    assert summarize(near, {"v": target})["passes"]
    assert profile([["ab", "ba"]] * 5, 300, 4) is None  # metin kısa


def test_lexicon_test_separates_a_word_list_from_free_generation():
    """Sözlük sınaması: sabit sözlükten gelen metinde vekil çok daha fazla tür üretir;
    kelimeleri harf zincirinden serbestçe üretilen metinde vekil ile metin aynıdır."""
    rng = np.random.default_rng(0)
    letters = list("abcdefghijklmnop")
    lexicon = ["".join(rng.choice(letters, size=int(rng.integers(3, 8)))) for _ in range(400)]
    weights = 1 / np.arange(1, 401)
    listed = [lexicon[int(i)] for i in rng.choice(400, size=2000, p=weights / weights.sum())]
    a = lexicon_stats(listed, rng, half=1000)
    assert a["type_ratio_k1"] > 2.5 and a["new_ratio_k1"] > 2.5

    seed_words = ["".join(rng.choice(letters[:6], size=int(rng.integers(2, 6)))) for _ in range(300)]
    free = markov_surrogate(seed_words, 1, 2000, rng)
    b = lexicon_stats(free, rng, half=1000)
    assert 0.8 < b["type_ratio_k1"] < 1.25 and 0.7 < b["new_ratio_k1"] < 1.4
    assert lexicon_stats(free[:500], rng, half=1000) is None
    assert all(set(w) <= set(letters[:6]) for w in free)


def test_period_text_loading_and_html_cleanup(tmp_path):
    page = (
        "<html><style>p {color: red}</style><body><p>Qui sequitur me<sup>[1]</sup> non ambulat"
        " in tenebris&nbsp;dicit Dominus.</p><ol class=\"references\"><li>nota editoris</li></ol>"
        "<script>alert(1)</script></body></html>"
    )
    text = _html_to_text(page)
    assert text == "Qui sequitur me non ambulat in tenebris dicit Dominus."
    (tmp_path / "latin_test_1420.txt").write_text((text + " ") * 6000, encoding="utf-8")
    (tmp_path / "short.txt").write_text(text, encoding="utf-8")
    period = load_period(tmp_path)
    assert list(period) == ["latin_test_1420"]  # kısa metin alınmaz
    assert period["latin_test_1420"][:4] == ["qui", "sequitur", "me", "non"]
    # Çok sayfalı Wikisource metni: her sayfanın üst bilgisi ve sayfa işaretleri atılır.
    page = "Questo testo è riletto <dc:title>X</dc:title> ◄ Capitolo I Capitolo III ► [p. 7 modifica ] colla di spicchi "
    (tmp_path / "italian_test_1400.txt").write_text("\n\n".join([page * 1] * 3000), encoding="utf-8")
    words = load_period(tmp_path)["italian_test_1400"]
    assert words[:6] == ["colla", "di", "spicchi", "colla", "di", "spicchi"] and len(words) == 9000


def _ordered_text(rng, n=6000):
    """Sırası bilgi taşıyan yapay metin: her kelime bir öncekine bağlı (kelime zinciri)."""
    vocab = [f"w{i}" for i in range(60)]
    nxt = {w: [vocab[int(j)] for j in rng.choice(60, size=3, replace=False)] for w in vocab}
    words, cur = [], vocab[0]
    for _ in range(n):
        words.append(cur)
        cur = nxt[cur][int(rng.integers(3))]
    return words


def test_order_test_finds_order_and_ignores_its_absence():
    """Sıra sınaması: zincirle üretilen metinde sıra bilgisi büyük, aynı kelimeler
    karıştırılınca sıfır. Bire bir kelime kodlaması sonucu değiştirmez."""
    rng = np.random.default_rng(0)
    words = _ordered_text(rng)
    lines = [words[i : i + 9] for i in range(0, len(words), 9)]
    a = order_stats(lines, 2500, np.random.default_rng(1))
    assert a["order"] > 1.0 and a["weight"] >= 0.45
    shuffled = [words[int(i)] for i in rng.permutation(len(words))]
    b = order_stats([shuffled[i : i + 9] for i in range(0, len(shuffled), 9)], 2500, np.random.default_rng(1))
    assert abs(b["order"]) < 0.05
    code = {w: f"x{i:03d}q" for i, w in enumerate(sorted(set(words)))}
    recoded = order_stats([[code[w] for w in ln] for ln in lines], 2500, np.random.default_rng(1))
    assert recoded["order"] == pytest.approx(a["order"])  # kod defteri sırayı korur
    assert order_stats(lines[:10], 2500, rng) is None


def test_word_families_and_noise_helpers():
    fam = word_families(["daiin"] * 5 + ["dain"] * 3 + ["aiin"] * 2 + ["saiin", "chol", "chol", "okeey"])
    assert fam["dain"] == fam["aiin"] == fam["saiin"] == fam["daiin"] == "daiin"
    assert fam["chol"] == "chol" and fam["okeey"] == "okeey"
    rng = np.random.default_rng(0)
    assert spelling_noise(TEXT[:200], 0.0, rng) == TEXT[:200]
    noisy = spelling_noise(TEXT[:2000], 1.0, rng)
    assert sum(a != b for a, b in zip(noisy, TEXT)) > 0.9 * len(TEXT)  # hemen hepsi değişir
    same = homophonic(TEXT[:2000], 0.0, 2, rng)  # eşsesli yok: bire bir ikame
    assert len(set(same)) == len(set(TEXT[:2000])) and [len(w) for w in same] == [len(w) for w in TEXT[:2000]]
    assert len(set(homophonic(TEXT[:2000], 1.0, 3, rng))) > 3 * len(set(TEXT[:2000]))


def test_degradation_scan_reports_joint_fit():
    rng = np.random.default_rng(0)
    words = _ordered_text(rng, 20000 + 2 * 400 + 400)
    bands = {
        "type_ratio": (0.0, 99.0), "order": (float("-inf"), 99.0),
        "ttr": (0.0, 1.0), "hapax": (0.0, 1.0), "ed1": (0.0, 1.0),
    }  # fmt: skip
    r = degradation_experiment({"Yapay": words}, bands, half=400)
    assert len(r["rows"]) == 14  # sesli ve seslisiz, yedişer bozulma düzeni
    assert all(row["fits_lexicon"] and row["fits_order"] and row["fits_growth"] for row in r["rows"])
    assert all("family_order" in row for row in r["rows"])
    tight = degradation_experiment({"Yapay": words}, bands | {"ttr": (0.9, 1.0)}, half=400)
    assert not any(row["fits_growth"] for row in tight["rows"])



def test_load_eva_plain(tmp_path):
    from voynich_lab.transliteration import load_eva_plain

    path = tmp_path / "control.txt"
    path.write_text("chedy  qokeedy\n\n\nsh3 daiin\n", encoding="utf-8")
    assert load_eva_plain(path) == [["chedy", "qokeedy"], ["daiin"]]
    glyph = load_eva_plain(path, "glyph")
    assert len(glyph[0][0]) == 4  # "ch" tek glif
    assert load_eva_plain(path, "raw") == [["chedy", "qokeedy"], ["sh3", "daiin"]]
    with pytest.raises(ValueError):
        load_eva_plain(path, "v101")


def test_control_experiment_reports_each_text_and_skips_short_halves():
    from voynich_lab.checks import control_experiment

    rng = np.random.default_rng(3)
    lexicon = ["".join(rng.choice(list("abcdefgh"), size=rng.integers(3, 7))) for _ in range(300)]
    weights = 1.0 / np.arange(1, len(lexicon) + 1)
    words = list(rng.choice(lexicon, size=3300, p=weights / weights.sum()))
    lines = [words[i : i + 10] for i in range(0, len(words), 10)]
    a = control_experiment({"bağımsız çekim": lines}, halves=(1500, 5000))
    b = control_experiment({"bağımsız çekim": lines}, halves=(1500, 5000))
    assert a == b  # tohum sabit
    row = a["texts"]["bağımsız çekim"]
    assert list(row) == ["1500"]  # 5000'lik yarı için metin kısa
    r = row["1500"]
    assert abs(r["order"]) < 0.05  # bağımsız çekilen kelimelerde sıra bilgisi yok
    assert r["type_ratio_k2"] > 1.5  # 300 kelimelik kapalı sözlük: vekil çok daha fazla tür üretir
    assert 0 < r["ttr"] < 1 and 0 <= r["hapax"] <= 1 and 0 <= r["ed1"] <= 1
