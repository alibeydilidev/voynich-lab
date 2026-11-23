"""Hattın dayandığı varsayımların testleri."""

import numpy as np
import pandas as pd
import pytest

from voynich_lab.abc import analyze_view

from voynich_lab.corpus import normalize
from voynich_lab.dataset import _truncate
from voynich_lab.features import FEATURE_NAMES, _is_ed1, extract_features
from voynich_lab.generators import (
    Allographs,
    GIBBERISH_PROCESSES,
    LANGUAGE_PROCESSES,
    Forms,
    Layout,
    Mark,
    _slot_alphabets,
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
