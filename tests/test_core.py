"""Hattın dayandığı varsayımların testleri."""

import numpy as np
import pandas as pd
import pytest

from voynich_lab.abc import analyze_view
from voynich_lab.checks import evaize, homogeneity_experiment
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
from voynich_lab.search import perturb, prior_for, run_search

from voynich_lab.corpus import normalize
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
    assert "p_split" in rec  # son süreç verbose


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
        rec = {}
        LANGUAGE_PROCESSES["verbose"](TEXT[:300], np.random.default_rng(i), rec=rec)
        for key, v in rec.items():
            seen.setdefault("verbose", {}).setdefault(key, []).append(float(v))
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

