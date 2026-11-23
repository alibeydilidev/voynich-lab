"""Hattın dayandığı varsayımların testleri."""

import numpy as np
import pytest

from voynich_lab.corpus import normalize
from voynich_lab.dataset import _truncate
from voynich_lab.features import FEATURE_NAMES, _is_ed1, extract_features
from voynich_lab.generators import (
    GIBBERISH_PROCESSES,
    LANGUAGE_PROCESSES,
    Layout,
    Mark,
    lay_out,
    sample_layout,
)
from voynich_lab.transliteration import _merge_eva_ligatures, load_takahashi, load_v101, to_windows

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


def test_layout_prior_is_deterministic_and_includes_no_effect_case():
    layouts = [sample_layout(np.random.default_rng(i)) for i in range(200)]
    assert layouts[3] == sample_layout(np.random.default_rng(3))
    bare = [lo for lo in layouts if not (lo.line_initial or lo.line_final or lo.para_initial)]
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
