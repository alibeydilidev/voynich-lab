"""Üretim süreçleri: her biri bir "Voynich nasıl yazıldı" hipotezinin simülasyonu.

Dil tabanlı süreçler gerçek bir metni dönüştürür:
  plain    : düz doğal dil. Tek alfabeli ikame şifresi istatistiksel olarak
             bununla aynıdır (feature'lar sembol adına bakmaz), ayrı sınıf değil.
  abjad    : sesli harfler atılmış yazım
  verbose  : her harf 1-3 sembollük bir gruba açılır (verbose şifre)
  codebook : kelime kelime kodlama. Her kelime türü, sıra numarasının yuvalara
             basamak olarak yazılmasıyla kurulan bir kod kelimesine eşlenir

Anlamsız metin üreteçleri gerçek metne ihtiyaç duymaz:
  grille   : Rugg tarzı tablo + ızgara (önek/orta/sonek hücreleri)
  selfcite : Timm ve Schinner tarzı kendinden kopyalama (önceki kelimeyi al, boz)
  slotcite : melez. Kelimeler grille gibi önek + gövde + sonek hecelerinden
             kurulur, metin selfcite gibi önceki kelimeleri kopyalayıp bir
             hecesini değiştirerek ilerler
  slotgram : çok yuvalı kelime grameri. Kelime 3 ila 8 sıralı, seçmeli yuvadan
             kurulur; isteğe bağlı olarak yerel kopyalama da yapar
  automaton: rastgele kurulmuş katmanlı glif otomatı. Her kelime, gliften glife
             bağımsız bir yürüyüştür; sözlük yoktur

Bunlar bilinçli olarak basit v0 sürümleri. Hattın bilimsel değeri bu
üreteçlerin aslına sadakatine bağlı, asıl geliştirme alanı burası.

Her sürecin üstünde ortak bir "yazıcı" katmanı durur (Layout): harflere kelime
başı ve kelime sonu için özel biçimler verebilir, metni sayfa genişliğine göre
satırlara böler, paragraf açar ve satır başı, satır sonu, paragraf başı
alışkanlıklarını uygular. Bu katmanın parametreleri bütün sınıflar için AYNI
önselden çekilir. Böylece satır konumu etkileri tek başına
hiçbir sınıfı işaret edemez; sınıflandırıcı onları kestirme yol yapamaz.

Yeni süreç eklemek: fonksiyonu yaz, sonunda lay_out(...) çağır, LANGUAGE_PROCESSES
ya da GIBBERISH_PROCESSES sözlüğüne ekle. Gerisi kendiliğinden akar.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from math import isnan, nan
from typing import Callable, Iterator

import numpy as np

from . import Lines
from .corpus import is_vowel

# Sentetik semboller için özel kullanım alanı (gerçek alfabelerle karışmasın).
_SYM_BASE = 0xE100


def _symbols(n: int) -> list[str]:
    return [chr(_SYM_BASE + i) for i in range(n)]


# Yazıcı katmanının eklediği yeni semboller (üreteç alfabeleriyle karışmasın).
_MARK_BASE = 0xE200
_FINAL_FORM_BASE = 0xE300
_INITIAL_FORM_BASE = 0xE400
_ALLOGRAPH_BASE = 0xE500


# -------------------------------------------------------------- yazıcı katmanı


@dataclass(frozen=True)
class Mark:
    """Belirli bir konumdaki kelimeye uygulanan yazıcı alışkanlığı.

    glyphs: her değer bir glif seçer. [0, 1) aralığındaysa metnin kendi
    alfabesinde sıklık sırasına göre bir konumdur (0 = en sık glif); 1 ve
    üstüyse metinde olmayan yeni bir semboldür.
    mode  : "add" (glif ekle), "replace" (uçtaki glifi değiştir) ya da yalnız
            satır sonu için "abbreviate" (kelimeyi kısalt, işaret koy).
    """

    p: float
    mode: str
    glyphs: tuple[float, ...]
    weights: tuple[float, ...]


@dataclass(frozen=True)
class Forms:
    """Konuma özgü harf biçimleri (kelime başı ya da kelime sonu).

    Gerçek yazılarda yaygın: Arapça ve İbranice son biçimleri, Yunanca son
    sigma, ortaçağ Latincesinde kelime sonu kısaltma işaretleri.

    share: o konumda özel biçimle yazılan glif türlerinin oranı.
    k    : kaç farklı özel biçim olduğu. 0 ise her glifin kendi özel biçimi
           vardır (bilgi kaybı yok). k > 0 ise seçilen glifler k ortak biçime
           düşer (kısaltma işareti gibi, bilgi kaybeder).
    """

    share: float
    k: int = 0


@dataclass(frozen=True)
class Allographs:
    """Nadir harf çeşitlemeleri: aynı glifin arada bir farklı çizilmesi.

    Transliterasyonların ayrıştığı yer tam burası: v101 her çeşitlemeyi ayrı
    sembol sayar (pencerede ~70 sembol), EVA birleştirir (~20). Bu katman
    sayesinde sentetik evren iki tercihi de kapsar.

    per_glyph: glif başına ortalama çeşitleme sayısı (Poisson).
    rate     : bir glifin çeşitlemeyle yazılma olasılığı.
    """

    per_glyph: float
    rate: float


@dataclass(frozen=True)
class Layout:
    """Yazı ve sayfa düzeni alışkanlıkları.

    words_per_line: satır genişliği, ortalama kelime cinsinden. Satırlar kelime
                    sayısına göre değil genişliğe göre dolar; uzun kelime
                    sığmazsa alt satıra iner (gerçek yazıcı gibi).
    width_jitter  : genişliğin satırdan satıra daralma payı (çizimler, kenar).
    para_lines    : ortalama paragraf uzunluğu (satır). 0 ise paragraf yok.
    """

    words_per_line: float = 9.0
    width_jitter: float = 0.0
    para_lines: float = 0.0
    allographs: Allographs | None = None
    final_forms: Forms | None = None
    initial_forms: Forms | None = None
    line_initial: Mark | None = None
    line_final: Mark | None = None
    para_initial: Mark | None = None

    def budgets(self, unit: float, rng: np.random.Generator) -> Iterator[tuple[float, bool]]:
        """Sonsuz (satır genişliği, paragraf ilk satırı mı) akışı.

        unit: bir kelimenin ortalama kapladığı yer (ortalama uzunluk + boşluk).
        Paragrafın son satırı yarım kalır.
        """
        para_start = True
        while True:
            width = self.words_per_line * unit * (1.0 - self.width_jitter * rng.random())
            ends = self.para_lines > 0 and rng.random() < 1.0 / self.para_lines
            if ends:
                width *= rng.uniform(0.1, 1.0)
            yield width, para_start
            para_start = ends


def _note(rec: dict | None, **values: float) -> None:
    """Örnek için çekilen parametreleri kaydeder (ABC adımı bunları okur)."""
    if rec is not None:
        rec.update(values)


class Knobs:
    """Bir sürecin ayarlarını verir: dışarıdan sabitlenmişse onu, değilse önselden
    çekileni. Her ayar kaydedilir. Hiçbir şey sabitlenmemişse rastgele sayı
    akışı, ayarlar doğrudan çekilseydi nasıl olacaksa öyledir."""

    def __init__(self, fixed: dict | None = None, rec: dict | None = None):
        self.fixed = fixed or {}
        self.rec = rec

    def get(self, name: str, draw: Callable[[], float]) -> float:
        value = self.fixed.get(name)
        if value is None or (isinstance(value, float) and isnan(value)):
            value = draw()
        if self.rec is not None:
            self.rec[name] = value
        return value


# Ayarların önsel sınırları: (alt, üst, tür). Yönlendirilmiş arama bu sınırların
# dışına çıkmaz. Tür: "f" sürekli, "i" tam sayı, "log" logaritmik ölçekte tam sayı,
# "b" 0 ya da 1, "m" ya 0 (kapalı) ya da [alt, üst] aralığında.
# Çekim kodundaki aralıklarla aynı olmalı (testi: test_priors_cover_what_is_drawn).
LAYOUT_PRIOR: dict[str, tuple[float, float, str]] = {
    "l_words_per_line": (5, 13, "f"),
    "l_width_jitter": (0, 0.35, "f"),
    "l_para_lines": (3, 15, "m"),
    "l_allo_per_glyph": (0.2, 3.0, "m"),
    "l_allo_rate": (0.01, 0.15, "m"),
    "l_final_forms_share": (0.1, 1.0, "m"),
    "l_final_forms_k": (0, 4, "i"),
    "l_initial_forms_share": (0.1, 1.0, "m"),
    "l_initial_forms_k": (0, 4, "i"),
    "l_line_initial_p": (0.1, 0.9, "m"),
    "l_line_final_p": (0.1, 0.9, "m"),
    "l_para_initial_p": (0.3, 1.0, "m"),
}
PROCESS_PRIOR: dict[str, dict[str, tuple[float, float, str]]] = {
    "automaton": {
        "p_alphabet": (15, 25, "i"),
        "p_levels": (3, 8, "i"),
        "p_out_degree": (2, 8, "i"),
        "p_concentration": (0.2, 3.0, "f"),
        "p_stay": (0, 1, "f"),
        "p_end_from": (1, 3, "i"),
    },
    "plain": {},
    "abjad": {},
    "verbose": {
        "p_alphabet": (12, 22, "i"),
        "p_drop_vowels": (0, 1, "b"),
        "p_short": (0.3, 1.0, "f"),
        "p_by_syllable": (0, 1, "b"),
        "p_split": (0.05, 0.7, "m"),
    },
    "codebook": {
        "p_alphabet": (15, 25, "i"),
        "p_n_slots": (3, 6, "i"),
        "p_slot_overlap": (0, 1, "f"),
        "p_len_max": (1, 2, "i"),
        "p_zero_empty": (0, 1, "b"),
        "p_order": (0, 2, "i"),
    },
    "grille": {
        "p_alphabet": (15, 25, "i"),
        "p_rows": (60, 3000, "log"),
        "p_slot_overlap": (0, 1, "f"),
        "p_n_edge": (5, 40, "log"),
        "p_n_mid": (10, 120, "log"),
        "p_empty": (0, 0.6, "f"),
        "p_len_edge": (1, 3, "i"),
        "p_len_mid": (2, 5, "i"),
        "p_n_grilles": (3, 8, "i"),
    },
    "selfcite": {
        "p_alphabet": (15, 25, "i"),
        "p_glyph_classes": (4, 7, "i"),
        "p_copy": (0.85, 0.97, "f"),
        "p_exact": (0.2, 0.8, "f"),
        "p_reach": (1, 30, "log"),
        "p_same_line": (0, 0.3, "f"),
        "p_slot_overlap": (0, 1, "f"),
        "p_affix": (0.3, 0.9, "f"),
        "p_mut_substitute": (0, 1, "f"),
        "p_mut_prefix": (0, 1, "f"),
        "p_mut_delete": (0, 1, "f"),
        "p_mut_double": (0, 1, "f"),
    },
    "slotcite": {
        "p_alphabet": (15, 25, "i"),
        "p_slot_overlap": (0, 1, "f"),
        "p_n_edge": (5, 40, "log"),
        "p_n_mid": (10, 120, "log"),
        "p_empty": (0, 0.6, "f"),
        "p_len_edge": (1, 3, "i"),
        "p_len_mid": (2, 5, "i"),
        "p_copy": (0.5, 0.97, "f"),
        "p_exact": (0.1, 0.7, "f"),
        "p_reach": (1, 30, "log"),
        "p_same_line": (0, 0.5, "f"),
        "p_mut_prefix": (0, 1, "f"),
        "p_mut_mid": (0, 1, "f"),
        "p_mut_suffix": (0, 1, "f"),
    },
    "slotgram": {
        "p_alphabet": (15, 25, "i"),
        "p_n_slots": (3, 8, "i"),
        "p_slot_overlap": (0, 1, "f"),
        "p_n_inv": (2, 30, "log"),
        "p_len_max": (1, 2, "i"),
        "p_empty": (0.1, 0.8, "f"),
        "p_copy": (0.3, 0.95, "m"),
        "p_exact": (0, 0.5, "f"),
        "p_reach": (1, 30, "log"),
        "p_same_line": (0, 0.5, "f"),
    },
}


def layout_params(layout: Layout) -> dict[str, float]:
    """Yazıcı katmanı ayarlarını düz sayısal sözlüğe çevirir. Kapalı alışkanlığın
    olasılığı ya da oranı 0 yazılır, böylece "yok" ile "az" aynı eksende durur."""
    out = {
        "words_per_line": layout.words_per_line,
        "width_jitter": layout.width_jitter,
        "para_lines": layout.para_lines,
        "allo_per_glyph": layout.allographs.per_glyph if layout.allographs else 0.0,
        "allo_rate": layout.allographs.rate if layout.allographs else 0.0,
    }
    for name, forms in (("final", layout.final_forms), ("initial", layout.initial_forms)):
        out[f"{name}_forms_share"] = forms.share if forms else 0.0
        out[f"{name}_forms_k"] = float(forms.k) if forms else nan
    for name, mark in (
        ("line_initial", layout.line_initial),
        ("line_final", layout.line_final),
        ("para_initial", layout.para_initial),
    ):
        out[f"{name}_p"] = mark.p if mark else 0.0
    return {f"l_{k}": float(v) for k, v in out.items()}


def _sample_mark(rng: np.random.Generator, p_range: tuple[float, float], modes: list[str]) -> Mark:
    k = int(rng.integers(1, 4))
    glyphs = tuple(
        float(1 + i) if rng.random() < 0.25 else float(rng.random()) for i in range(k)
    )
    w = rng.dirichlet(np.ones(k))
    return Mark(float(rng.uniform(*p_range)), str(rng.choice(modes)), glyphs, tuple(map(float, w)))


def sample_layout(rng: np.random.Generator) -> Layout:
    """Yazıcı katmanının önseli. Bilinçli olarak geniş ve sınıftan bağımsız.

    Her alışkanlık belli bir olasılıkla hiç yoktur; "hiçbir satır etkisi yok"
    durumu da evrenin içindedir. Aralıklar Voynich'e göre ayarlanmadı; hangi
    bölgenin Voynich'e yakın olduğunu bulmak ABC adımının işi (yol haritası 2).
    """
    has_para = rng.random() < 0.7

    def forms(p_active: float) -> Forms | None:
        if rng.random() >= p_active:
            return None
        k = 0 if rng.random() < 0.5 else int(rng.integers(1, 5))
        return Forms(float(rng.uniform(0.1, 1.0)), k)

    return Layout(
        words_per_line=float(rng.uniform(5, 13)),
        width_jitter=float(rng.uniform(0, 0.35)),
        para_lines=float(rng.uniform(3, 15)) if has_para else 0.0,
        allographs=Allographs(float(rng.uniform(0.2, 3.0)), float(rng.uniform(0.01, 0.15)))
        if rng.random() < 0.5
        else None,
        final_forms=forms(0.5),
        initial_forms=forms(0.4),
        line_initial=_sample_mark(rng, (0.1, 0.9), ["add", "replace"])
        if rng.random() < 0.6
        else None,
        line_final=_sample_mark(rng, (0.1, 0.9), ["add", "replace", "abbreviate"])
        if rng.random() < 0.6
        else None,
        para_initial=_sample_mark(rng, (0.3, 1.0), ["add", "replace"])
        if has_para and rng.random() < 0.6
        else None,
    )


def layout_from_params(params: dict, rng: np.random.Generator) -> Layout:
    """`l_` önekli ayarlardan Layout kurar (layout_params'ın tersi).

    Sayısal olmayan seçimler (işaret türü, hangi glifler) önselden çekilir.
    Verilmeyen ayar da önselden gelir. 0 değeri "bu alışkanlık yok" demektir.
    """
    base = sample_layout(rng)
    given = layout_params(base)
    for key, value in params.items():
        if key in given and value is not None and not (isinstance(value, float) and isnan(value)):
            given[key] = float(value)
    v = {k[2:]: x for k, x in given.items()}

    def forms(name: str) -> Forms | None:
        if v[f"{name}_forms_share"] <= 0:
            return None
        k = v[f"{name}_forms_k"]
        return Forms(v[f"{name}_forms_share"], 0 if isnan(k) else int(round(k)))

    def mark(name: str, template: Mark | None, p_range: tuple[float, float], modes: list[str]) -> Mark | None:
        if v[f"{name}_p"] <= 0:
            return None
        m = template or _sample_mark(rng, p_range, modes)
        return Mark(v[f"{name}_p"], m.mode, m.glyphs, m.weights)

    has_allo = v["allo_per_glyph"] > 0 and v["allo_rate"] > 0
    return Layout(
        words_per_line=v["words_per_line"],
        width_jitter=v["width_jitter"],
        para_lines=v["para_lines"],
        allographs=Allographs(v["allo_per_glyph"], v["allo_rate"]) if has_allo else None,
        final_forms=forms("final"),
        initial_forms=forms("initial"),
        line_initial=mark("line_initial", base.line_initial, (0.1, 0.9), ["add", "replace"]),
        line_final=mark("line_final", base.line_final, (0.1, 0.9), ["add", "replace", "abbreviate"]),
        para_initial=mark("para_initial", base.para_initial, (0.3, 1.0), ["add", "replace"])
        if v["para_lines"] > 0
        else None,
    )


def _apply_mark(word: str, mark: Mark, at_end: bool, ranked: list[str], rng: np.random.Generator) -> str:
    u = mark.glyphs[int(rng.choice(len(mark.glyphs), p=mark.weights))]
    g = chr(_MARK_BASE + int(u) - 1) if u >= 1 else ranked[int(u * len(ranked))]
    if not at_end:
        return g + (word[1:] if mark.mode == "replace" else word)
    if mark.mode == "replace":
        return word[:-1] + g
    if mark.mode == "abbreviate":
        return word[: max(1, len(word) - int(rng.integers(1, 4)))] + g
    return word + g


def _ranked_alphabet(lines: Lines) -> list[str]:
    counts = Counter(ch for ln in lines for w in ln for ch in w)
    return [g for g, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))]


def _form_table(
    ranked: list[str], forms: Forms | None, base: int, rng: np.random.Generator
) -> dict[str, str]:
    """Hangi glif o konumda hangi özel biçimle yazılır."""
    if forms is None:
        return {}
    chosen = [g for g in ranked if rng.random() < forms.share]
    if forms.k == 0:
        return {g: chr(base + i) for i, g in enumerate(chosen)}
    return {g: chr(base + int(rng.integers(0, forms.k))) for g in chosen}


def apply_allographs(lines: Lines, layout: Layout, rng: np.random.Generator) -> Lines:
    """Glifleri küçük bir olasılıkla nadir çeşitlemeleriyle değiştirir."""
    spec = layout.allographs
    if spec is None:
        return lines
    ranked = _ranked_alphabet(lines)
    variants: dict[str, list[str]] = {}
    nxt = _ALLOGRAPH_BASE
    for g in ranked:
        n = int(rng.poisson(spec.per_glyph))
        variants[g] = [chr(nxt + i) for i in range(n)]
        nxt += n
    out: Lines = []
    for ln in lines:
        new_ln = []
        for w in ln:
            hits = np.flatnonzero(rng.random(len(w)) < spec.rate)
            if len(hits):
                chars = list(w)
                for i in hits:
                    v = variants[chars[i]]
                    if v:
                        chars[i] = v[int(rng.integers(0, len(v)))]
                w = "".join(chars)
            new_ln.append(w)
        out.append(new_ln)
    return out


def apply_forms(lines: Lines, layout: Layout, rng: np.random.Generator) -> Lines:
    """Kelime başı ve kelime sonu gliflerini özel biçimleriyle değiştirir.

    Kelime sayısı ve uzunlukları değişmez. Tek glifli kelimede son biçim önceliklidir.
    """
    if not (layout.final_forms or layout.initial_forms):
        return lines
    ranked = _ranked_alphabet(lines)
    fin = _form_table(ranked, layout.final_forms, _FINAL_FORM_BASE, rng)
    ini = _form_table(ranked, layout.initial_forms, _INITIAL_FORM_BASE, rng)

    def conv(w: str) -> str:
        if w[-1] in fin:
            w = w[:-1] + fin[w[-1]]
            if len(w) == 1:
                return w
        if w[0] in ini:
            w = ini[w[0]] + w[1:]
        return w

    return [[conv(w) for w in ln] for ln in lines]


def finish(
    lines: Lines, para_starts: list[bool], layout: Layout, rng: np.random.Generator
) -> Lines:
    """Yazıcı katmanının son adımı: nadir harf çeşitlemeleri, konuma özgü harf
    biçimleri, sonra satır başı, satır sonu ve paragraf başı alışkanlıkları."""
    lines = apply_forms(apply_allographs(lines, layout, rng), layout, rng)
    if not (layout.line_initial or layout.line_final or layout.para_initial):
        return lines
    ranked = _ranked_alphabet(lines)
    out: Lines = []
    for ln, starts in zip(lines, para_starts):
        ln = list(ln)
        head = layout.para_initial if starts and layout.para_initial else layout.line_initial
        if head and rng.random() < head.p:
            ln[0] = _apply_mark(ln[0], head, False, ranked, rng)
        if layout.line_final and rng.random() < layout.line_final.p:
            ln[-1] = _apply_mark(ln[-1], layout.line_final, True, ranked, rng)
        out.append(ln)
    return out


def lay_out(
    words: list[str],
    rng: np.random.Generator,
    layout: Layout | None = None,
    rec: dict | None = None,
) -> Lines:
    """Kelime akışını yazıcı katmanından geçirip satırlara döker.

    layout verilmezse önselden çekilir. Satırlar genişliğe göre dolar: sığmayan
    kelime alt satırın başına iner. Bunun ölçülmüş yan etkisi, hiçbir özel kural
    olmadan da satır başı kelimelerinin ortalamadan uzun çıkmasıdır (sığmayan
    kelime çoğunlukla uzun kelimedir). Satır sonu kelimelerinde böyle bir kayma
    oluşmaz (testi: test_width_wrapping_lengthens_line_initial_words).
    """
    if layout is None:
        layout = sample_layout(rng)
    _note(rec, **layout_params(layout))
    if not words:
        return []
    unit = float(np.mean([len(w) for w in words])) + 1.0
    budgets = layout.budgets(unit, rng)
    lines: Lines = []
    para_starts: list[bool] = []
    i = 0
    while i < len(words):
        width, starts = next(budgets)
        line, used = [words[i]], len(words[i]) + 1
        i += 1
        while i < len(words) and used + len(words[i]) + 1 <= width:
            line.append(words[i])
            used += len(words[i]) + 1
            i += 1
        lines.append(line)
        para_starts.append(starts)
    return finish(lines, para_starts, layout, rng)


# ---------------------------------------------------------------- dil tabanlı


def plain(
    words: list[str],
    rng: np.random.Generator,
    layout: Layout | None = None,
    rec: dict | None = None,
    fixed: dict | None = None,
) -> Lines:
    return lay_out(list(words), rng, layout, rec)


def abjad(
    words: list[str],
    rng: np.random.Generator,
    layout: Layout | None = None,
    rec: dict | None = None,
    fixed: dict | None = None,
) -> Lines:
    """Sesli harfleri atar. Tamamen sesliden oluşan kelimenin ilk harfi kalır."""
    out = []
    for w in words:
        c = "".join(ch for ch in w if not is_vowel(ch))
        out.append(c or w[0])
    return lay_out(out, rng, layout, rec)


def verbose(
    words: list[str],
    rng: np.random.Generator,
    layout: Layout | None = None,
    rec: dict | None = None,
    fixed: dict | None = None,
) -> Lines:
    """Verbose şifre: sık harfler kısa, seyrek harfler uzun sembol grubu alır.

    Örnek başına rastgele: şifre alfabesi boyutu, kod tablosu ve kelime
    sınırlarının nasıl kurulduğu. Üç seçenek var: düz metnin kelime sınırları
    korunur; kelime içine rastgele boşluk eklenir; ya da her hece ayrı kelime
    yazılır (hece = ünsüzler + ünlü grubu). Son ikisi "Voynich kelimesi düz
    metnin kelimesi değil, bir parçasıdır" hipotezinin karşılığıdır.

    İki ayar daha: şifrelemeden önce seslilerin atılması (abjad + verbose
    bileşimi; sesliler atılınca hece modu boşa düşer, çünkü hece sınırı ünlüye
    bakar) ve kodların ne kadar kısa olduğu (1'e yakınsa sık harfler tek glif
    alır, şifre düz ikameye yaklaşır).
    """
    k = Knobs(fixed, rec)
    alphabet = _symbols(int(k.get("p_alphabet", lambda: int(rng.integers(12, 23)))))
    if bool(k.get("p_drop_vowels", lambda: float(rng.random() < 0.3))):
        words = [("".join(ch for ch in w if not is_vowel(ch)) or w[0]) for w in words]
    short_base = float(k.get("p_short", lambda: float(rng.uniform(0.3, 1.0))))
    letters, counts = np.unique([ch for w in words for ch in w], return_counts=True)
    order = letters[np.argsort(-counts)]

    codes: dict[str, str] = {}
    used: set[str] = set()
    for rank, letter in enumerate(order):
        # Sık harfler için kısa kod olasılığı daha yüksek.
        p_short = max(0.1, short_base - 0.04 * rank)
        while True:
            length = 1 if rng.random() < p_short else int(rng.integers(2, 4))
            code = "".join(rng.choice(alphabet, size=length))
            if code not in used:
                used.add(code)
                codes[letter] = code
                break

    r = rng.random()
    by_syllable = bool(k.get("p_by_syllable", lambda: float(r < 0.25)))
    # Rastgele boşluk ekleme olasılığı (hece modunda kullanılmaz).
    split_p = float(k.get("p_split", lambda: 0.0 if r < 0.55 else float(rng.uniform(0.05, 0.7))))
    _note(rec, p_code_len_mean=float(np.mean([len(c) for c in codes.values()])))
    out: list[str] = []
    for w in words:
        cur = ""
        for i, ch in enumerate(w):
            cur += codes[ch]
            if by_syllable:
                # Hece sonu: ünlüden sonra ünsüz geliyorsa.
                cut = i + 1 < len(w) and is_vowel(ch) and not is_vowel(w[i + 1])
            else:
                cut = split_p > 0 and rng.random() < split_p
            if cut:
                out.append(cur)
                cur = ""
        if cur:
            out.append(cur)
    return lay_out(out, rng, layout, rec)


def codebook(
    words: list[str],
    rng: np.random.Generator,
    layout: Layout | None = None,
    rec: dict | None = None,
    fixed: dict | None = None,
) -> Lines:
    """Kelime kelime kodlama (kod defteri): her kelime türü tek bir kod kelimesi olur.

    v0.9'dan doğan hipotez. Kod, kelimenin sıra numarasının karışık tabanlı bir
    sayı gibi yuvalara yazılmasıdır: her yuvanın kendi hece envanteri vardır,
    numaranın her basamağı o yuvadan bir hece seçer, kod kelimesi hecelerin
    yuva sırasıyla yan yana gelmesidir. Böylece dağarcık düz metninkiyle bire
    bir aynıdır, her kod yuva yapısına uyar ve kod uzayı sık dolu olduğu için
    türler arasında "bir hece farklı" komşu çoktur.

    Örnek başına rastgele: yuva sayısı, yuva alfabelerinin örtüşmesi, hecelerin
    en çok kaç glif olduğu, 0 basamağının boş yuva sayılıp sayılmadığı (sayılırsa
    küçük numaralı kelimeler kısa olur) ve numaranın neye göre verildiği:
    sıklık sırası (sık kelimeler küçük numara alır), ilk geçiş sırası (yakında
    ilk kez geçen kelimeler ardışık numara alır) ya da rastgele.
    """
    k = Knobs(fixed, rec)
    alphabet = _symbols(int(k.get("p_alphabet", lambda: int(rng.integers(15, 26)))))
    n_slots = int(k.get("p_n_slots", lambda: int(rng.integers(3, 7))))
    overlap = float(k.get("p_slot_overlap", lambda: float(rng.uniform(0, 1))))
    slot_alphabets = _slot_alphabets(alphabet, n_slots, overlap, rng)
    len_max = int(k.get("p_len_max", lambda: int(rng.integers(1, 3))))
    zero_empty = bool(k.get("p_zero_empty", lambda: float(rng.random() < 0.5)))
    order = int(k.get("p_order", lambda: int(rng.integers(0, 3))))

    counts = Counter(words)
    if order == 0:
        ranked = [w for w, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))]
    elif order == 1:
        ranked = list(dict.fromkeys(words))
    else:
        pool = sorted(counts)
        ranked = [pool[int(i)] for i in rng.permutation(len(pool))]

    # Yuva envanterleri: kısa heceler önce. Kod uzayı dağarcığa yetmezse heceler uzar.
    length = len_max
    while True:
        invs: list[list[str]] = []
        for A in slot_alphabets:
            syl: list[str] = []
            cur = [""]
            for _ in range(length):
                cur = [x + a for x in cur for a in A][:400]
                syl += [cur[int(i)] for i in rng.permutation(len(cur))]
            invs.append(syl[:400])
        radices = [len(v) + (1 if zero_empty else 0) for v in invs]
        if float(np.prod([float(r) for r in radices])) >= 2 * len(ranked) + 2 or length >= 4:
            break
        length += 1
    significance = [int(j) for j in rng.permutation(n_slots)]  # hangi yuva en hızlı değişir

    def spell(number: int) -> str:
        parts = [""] * n_slots
        for j in significance:
            number, digit = divmod(number, radices[j])
            if zero_empty:
                parts[j] = "" if digit == 0 else invs[j][digit - 1]
            else:
                parts[j] = invs[j][digit]
        return "".join(parts)

    code: dict[str, str] = {}
    used: set[str] = set()
    number = 0
    for w in ranked:
        while True:
            c = spell(number)
            number += 1
            if c and c not in used:
                break
        used.add(c)
        code[w] = c
    return lay_out([code[w] for w in words], rng, layout, rec)


# ------------------------------------------------------------------- anlamsız


def _log_int(lo: int, hi: int, rng: np.random.Generator) -> int:
    """[lo, hi] aralığında logaritmik ölçekte düzgün tam sayı."""
    return int(round(np.exp(rng.uniform(np.log(lo), np.log(hi)))))


def _zipf_weights(n: int, rng: np.random.Generator) -> np.ndarray:
    w = 1.0 / np.arange(1, n + 1) ** rng.uniform(0.6, 1.2)
    return w / w.sum()


def _slot_alphabets(
    alphabet: list[str], n_slots: int, overlap: float, rng: np.random.Generator
) -> list[list[str]]:
    """Alfabeyi kelime içi yuvalara (önek, gövde, sonek ...) paylaştırır.

    overlap 0 ise her yuvanın glif kümesi ayrıdır (glifin kelimedeki yeri
    sabittir); 1 ise bütün yuvalar bütün alfabeyi kullanır (konum yapısı yok).
    """
    owner = rng.integers(0, n_slots, size=len(alphabet))
    owner[rng.permutation(len(alphabet))[:n_slots]] = np.arange(n_slots)  # boş yuva kalmasın
    slots = []
    for j in range(n_slots):
        own = [g for g, o in zip(alphabet, owner) if o == j]
        extra = [g for g, o in zip(alphabet, owner) if o != j and rng.random() < overlap]
        slots.append([str(g) for g in rng.permutation(own + extra)])
    return slots


def _syllables(
    alphabet: list[str], n: int, max_len: int, p_empty: float, rng: np.random.Generator
) -> list[str]:
    sym_w = _zipf_weights(len(alphabet), rng)
    out = []
    for _ in range(n):
        if rng.random() < p_empty:
            out.append("")
        else:
            k = int(rng.integers(1, max_len + 1))
            out.append("".join(rng.choice(alphabet, size=k, p=sym_w)))
    return out


def grille(
    n_words: int,
    rng: np.random.Generator,
    layout: Layout | None = None,
    rec: dict | None = None,
    fixed: dict | None = None,
) -> Lines:
    """Rugg (2004) tarzı: üç sütunlu hece tablosu, üzerinde gezen delikli ızgara.

    Her ızgara üç sütun için birer satır kayması tanımlar. Izgara tabloyu
    baştan sona tarar, sonra sıradaki ızgaraya geçilir.

    Örnek başına rastgele: tablo boyutu (küçük tablo kendini tekrar eder, büyük
    tablo her kelimeyi neredeyse bağımsız çeker), üç sütunun glif kümelerinin
    ne kadar örtüştüğü (Rugg'ın tablosunda önek, gövde ve sonek heceleri ayrıdır),
    hecelerin en çok kaç glif olduğu ve önek ile sonek hücrelerinin boş kalma payı.
    """
    k = Knobs(fixed, rec)
    alphabet = _symbols(int(k.get("p_alphabet", lambda: int(rng.integers(15, 26)))))
    rows = int(k.get("p_rows", lambda: _log_int(60, 3000, rng)))
    overlap = float(k.get("p_slot_overlap", lambda: float(rng.uniform(0, 1))))
    alpha_p, alpha_m, alpha_s = _slot_alphabets(alphabet, 3, overlap, rng)
    n_edge = int(k.get("p_n_edge", lambda: _log_int(5, 40, rng)))
    n_mid = int(k.get("p_n_mid", lambda: _log_int(10, 120, rng)))
    p_empty = float(k.get("p_empty", lambda: float(rng.uniform(0.0, 0.6))))
    len_edge = int(k.get("p_len_edge", lambda: int(rng.integers(1, 4))))
    len_mid = int(k.get("p_len_mid", lambda: int(rng.integers(2, 6))))
    inv_p = _syllables(alpha_p, n_edge, len_edge, p_empty, rng)
    inv_m = _syllables(alpha_m, n_mid, len_mid, 0.0, rng)
    inv_s = _syllables(alpha_s, n_edge, len_edge, p_empty, rng)
    col_p = rng.choice(inv_p, size=rows, p=_zipf_weights(len(inv_p), rng))
    col_m = rng.choice(inv_m, size=rows, p=_zipf_weights(len(inv_m), rng))
    col_s = rng.choice(inv_s, size=rows, p=_zipf_weights(len(inv_s), rng))
    n_grilles = int(k.get("p_n_grilles", lambda: int(rng.integers(3, 9))))
    grilles = rng.integers(0, rows, size=(n_grilles, 3))

    words: list[str] = []
    j = 0
    while len(words) < n_words:
        a, b, c = grilles[(j // rows) % len(grilles)]
        r = j % rows
        w = col_p[(r + a) % rows] + col_m[(r + b) % rows] + col_s[(r + c) % rows]
        if w:
            words.append(str(w))
        j += 1
    return lay_out(words, rng, layout, rec)


def selfcite(
    n_words: int,
    rng: np.random.Generator,
    layout: Layout | None = None,
    rec: dict | None = None,
    fixed: dict | None = None,
) -> Lines:
    """Timm ve Schinner (2019) tarzı: yazıcı önceki satırlardan kelime kopyalar,
    küçük değişikliklerle yeniden yazar. Benzer kelimelerin yakın durması ve
    yoğun "bir harf farklı" kelime ağı bu sürecin doğal sonucudur.

    Örnek başına rastgele: kopyanın değişmeden kalma olasılığı, yazıcının kaç
    satır geriye baktığı, yeni kelimelerin yuva (önek, gövde, sonek) yapısının
    sıkılığı. Değerler Timm ve Schinner'ın makalesinden alınmadı, geniş bir
    aralıktan çekilir (bkz. CLAUDE.md yol haritası).

    Kopyalama satır konumuna bağlı olduğu için bu süreç satırlarını kendisi
    kurar, ama genişlik ve paragraf kararını ortak yazıcı katmanından alır.
    Yazıcı katmanı en sonda uygulanır, kopyalanan kaynak işaretsizdir.
    """
    if layout is None:
        layout = sample_layout(rng)
    _note(rec, **layout_params(layout))
    k = Knobs(fixed, rec)
    alphabet = _symbols(int(k.get("p_alphabet", lambda: int(rng.integers(15, 26)))))
    sym_w = _zipf_weights(len(alphabet), rng)
    # Benzer görünen glif sınıfları: değişiklikler çoğunlukla sınıf içinde olur.
    classes = np.array_split(
        rng.permutation(len(alphabet)),
        int(k.get("p_glyph_classes", lambda: int(rng.integers(4, 8)))),
    )
    class_of = {alphabet[i]: [alphabet[k] for k in cls] for cls in classes for i in cls}
    prefixes = [str(s) for s in rng.choice(alphabet, size=3, p=sym_w)]
    p_copy = k.get("p_copy", lambda: rng.uniform(0.85, 0.97))
    p_exact = k.get("p_exact", lambda: rng.uniform(0.2, 0.8))  # kopyanın hiç değişmeme olasılığı
    reach = int(k.get("p_reach", lambda: _log_int(1, 30, rng)))  # kaç satır geriye bakılır
    # Kaynağın aynı satırdan seçilme olasılığı.
    p_same_line = k.get("p_same_line", lambda: rng.uniform(0.0, 0.3))
    # Değişiklik türlerinin payı: değiştir, önek, sil, ikile (ortalama 0.43, 0.21, 0.17, 0.19).
    drawn = rng.dirichlet(4 * np.array([0.43, 0.21, 0.17, 0.19]))
    names = ("p_mut_substitute", "p_mut_prefix", "p_mut_delete", "p_mut_double")
    mix = np.array([float(k.get(n, lambda v=v: float(v))) for n, v in zip(names, drawn)])
    cut = np.cumsum(mix / max(mix.sum(), 1e-9))
    # Yeni kelimeler önek + gövde + sonek yuvalarından kurulur.
    overlap = float(k.get("p_slot_overlap", lambda: float(rng.uniform(0, 1))))
    slot_p, slot_m, slot_s = (
        (a, _zipf_weights(len(a), rng)) for a in _slot_alphabets(alphabet, 3, overlap, rng)
    )
    p_affix = k.get("p_affix", lambda: rng.uniform(0.3, 0.9))

    def fresh() -> str:
        w = "".join(rng.choice(slot_m[0], size=int(rng.integers(1, 5)), p=slot_m[1]))
        if rng.random() < p_affix:
            w = str(rng.choice(slot_p[0], p=slot_p[1])) + w
        if rng.random() < p_affix:
            w = w + str(rng.choice(slot_s[0], p=slot_s[1]))
        return w

    def mutate(w: str) -> str:
        if rng.random() < p_exact or not w:
            return w
        r = rng.random()
        i = int(rng.integers(0, len(w)))
        if r < cut[0]:  # benzer glifle değiştir
            return w[:i] + str(rng.choice(class_of[w[i]])) + w[i + 1 :]
        if r < cut[1]:  # önek ekle ya da at
            if w[0] in prefixes and len(w) > 1:
                return w[1:]
            return str(rng.choice(prefixes)) + w
        if r < cut[2] and len(w) > 1:  # glif sil
            return w[:i] + w[i + 1 :]
        return w[:i] + w[i] + w[i:]  # glifi ikile

    def next_word(lines: Lines, line: list[str]) -> str:
        if lines and rng.random() < p_copy:
            # Kaynak: son `reach` satırda benzer konum ya da aynı satırın başı.
            src_line = lines[-int(rng.integers(1, min(reach, len(lines)) + 1))]
            if line and rng.random() < p_same_line:
                src = line[int(rng.integers(0, len(line)))]
            else:
                k = min(len(src_line) - 1, max(0, len(line) + int(rng.integers(-1, 2))))
                src = src_line[k]
            return mutate(src)[:10] or fresh()
        return fresh()

    budgets = layout.budgets(4.0 + 1.0, rng)  # kelimeler ortalama 4 glif civarı
    lines: Lines = []
    para_starts: list[bool] = []
    total = 0
    carry: str | None = None  # satıra sığmayan kelime alt satırın başına iner
    while total < n_words:
        width, starts = next(budgets)
        line: list[str] = []
        used = 0
        while True:
            w = carry if carry is not None else next_word(lines, line)
            carry = None
            if line and used + len(w) + 1 > width:
                carry = w
                break
            line.append(w)
            used += len(w) + 1
        lines.append(line)
        para_starts.append(starts)
        total += len(line)
    return finish(lines, para_starts, layout, rng)


def slotcite(
    n_words: int,
    rng: np.random.Generator,
    layout: Layout | None = None,
    rec: dict | None = None,
    fixed: dict | None = None,
) -> Lines:
    """Melez: yuva yapılı kelime + yerel kopyalayıp değiştirme.

    v0.5 bulgusundan doğan hipotez: grille kelime yapısını tutturuyor ama komşu
    kelimeleri birbirine benzetemiyor ve yeterince tek geçen kelime üretmiyor;
    selfcite komşu benzerliğini tutturuyor ama kelime yapısı gevşek. Burada her
    kelime (önek, gövde, sonek) hece üçlüsüdür. Yazıcı çoğu kelimeyi üst
    satırlardaki benzer konumdan ya da aynı satırdan kopyalar; kopyada ya hiçbir
    şeyi değiştirmez ya da üç heceden birini envanterden yenisiyle değiştirir.
    Böylece her kelime yuva yapısına uyar, komşular birbirine benzer ve
    çeşitlemeler birikir.
    """
    if layout is None:
        layout = sample_layout(rng)
    _note(rec, **layout_params(layout))
    k = Knobs(fixed, rec)
    alphabet = _symbols(int(k.get("p_alphabet", lambda: int(rng.integers(15, 26)))))
    overlap = float(k.get("p_slot_overlap", lambda: float(rng.uniform(0, 1))))
    slot_alphabets = _slot_alphabets(alphabet, 3, overlap, rng)
    n_edge = int(k.get("p_n_edge", lambda: _log_int(5, 40, rng)))
    n_mid = int(k.get("p_n_mid", lambda: _log_int(10, 120, rng)))
    p_empty = float(k.get("p_empty", lambda: float(rng.uniform(0.0, 0.6))))
    len_edge = int(k.get("p_len_edge", lambda: int(rng.integers(1, 4))))
    len_mid = int(k.get("p_len_mid", lambda: int(rng.integers(2, 6))))
    inv = [
        _syllables(slot_alphabets[0], n_edge, len_edge, p_empty, rng),
        _syllables(slot_alphabets[1], n_mid, len_mid, 0.0, rng),
        _syllables(slot_alphabets[2], n_edge, len_edge, p_empty, rng),
    ]
    weights = [_zipf_weights(len(v), rng) for v in inv]
    p_copy = float(k.get("p_copy", lambda: float(rng.uniform(0.5, 0.97))))
    p_exact = float(k.get("p_exact", lambda: float(rng.uniform(0.1, 0.7))))
    reach = int(k.get("p_reach", lambda: _log_int(1, 30, rng)))
    p_same_line = float(k.get("p_same_line", lambda: float(rng.uniform(0.0, 0.5))))
    drawn = rng.dirichlet(2 * np.ones(3))
    names = ("p_mut_prefix", "p_mut_mid", "p_mut_suffix")
    mix = np.array([float(k.get(n, lambda v=v: float(v))) for n, v in zip(names, drawn)])
    cut = np.cumsum(mix / max(mix.sum(), 1e-9))

    mean_len = sum(float(np.dot(weights[j], [len(x) for x in inv[j]])) for j in range(3))
    return _cite_text(inv, weights, p_copy, p_exact, reach, p_same_line, cut, mean_len, n_words, layout, rng)


def _cite_text(
    inv: list[list[str]],
    weights: list[np.ndarray],
    p_copy: float,
    p_exact: float,
    reach: int,
    p_same_line: float,
    cut: np.ndarray,
    mean_len: float,
    n_words: int,
    layout: Layout,
    rng: np.random.Generator,
) -> Lines:
    """Yuva yapılı kelimelerle metin kurar; isteğe bağlı yerel kopyalama yapar.

    Her kelime, yuva başına bir hece indeksinden oluşan bir demettir. Yeni
    kelime her yuvadan bağımsız çekilir. Kopyalanan kelime ya aynen alınır ya da
    tek bir yuvası yeniden çekilir; hangi yuvanın değişeceğini `cut` (birikimli
    olasılık) belirler. Boş çıkan kelime yeniden çekilir.
    """
    n_slots = len(inv)
    # Tek tek çekmek yavaş: hece ve olasılık çekimleri bloklar hâlinde hazırlanır.
    block = 4096
    pools = [iter(()) for _ in range(n_slots)]
    uniforms = iter(())

    def syllable(j: int) -> int:
        nonlocal pools
        v = next(pools[j], None)
        if v is None:
            pools[j] = iter(rng.choice(len(inv[j]), size=block, p=weights[j]).tolist())
            v = next(pools[j])
        return v

    def u() -> float:
        nonlocal uniforms
        v = next(uniforms, None)
        if v is None:
            uniforms = iter(rng.random(block).tolist())
            v = next(uniforms)
        return v

    Word = tuple[int, ...]

    def spell(w: Word) -> str:
        return "".join(inv[j][i] for j, i in enumerate(w))

    def fresh() -> Word:
        while True:
            w = tuple(syllable(j) for j in range(n_slots))
            if spell(w):
                return w

    def next_word(lines: list[list[Word]], line: list[Word]) -> Word:
        if not lines or u() >= p_copy:
            return fresh()
        if line and u() < p_same_line:
            src = line[int(u() * len(line))]
        else:
            src_line = lines[-(1 + int(u() * min(reach, len(lines))))]
            pos = min(len(src_line) - 1, max(0, len(line) + int(u() * 3) - 1))
            src = src_line[pos]
        if u() < p_exact:
            return src
        j = int(np.searchsorted(cut, u(), side="right").clip(0, n_slots - 1))
        w = list(src)
        w[j] = syllable(j)
        if not spell(tuple(w)):
            return src
        return tuple(w)

    budgets = layout.budgets(mean_len + 1.0, rng)
    lines: list[list[Word]] = []
    para_starts: list[bool] = []
    total = 0
    carry: Word | None = None
    while total < n_words:
        width, starts = next(budgets)
        line: list[Word] = []
        used = 0
        while True:
            w = carry if carry is not None else next_word(lines, line)
            carry = None
            size = len(spell(w)) + 1
            if line and used + size > width:
                carry = w
                break
            line.append(w)
            used += size
        lines.append(line)
        para_starts.append(starts)
        total += len(line)
    return finish([[spell(w) for w in ln] for ln in lines], para_starts, layout, rng)


def slotgram(
    n_words: int,
    rng: np.random.Generator,
    layout: Layout | None = None,
    rec: dict | None = None,
    fixed: dict | None = None,
) -> Lines:
    """Çok yuvalı kelime grameri: kelime 3 ila 8 sıralı, seçmeli yuvadan kurulur.

    v0.6 bulgusundan doğan hipotez: üç yuvalı üreteçlerin dağarcığı kapalı
    kalıyor (tek geçen kelime az, "bir harf farklı" komşu fazla). Voynich
    kelime grameri literatürü kelimeyi çok sayıda kısa, seçmeli yuvaya böler.
    Burada her yuvanın küçük bir hece envanteri vardır ve yuva boş geçilebilir;
    kelime, yuvaların sırayla yan yana gelmesidir. Yuva sayısı arttıkça olası
    kelime sayısı çarpımsal büyür.

    Yerel kopyalama isteğe bağlıdır (p_copy 0 olabilir): kopyalanan kelimenin
    tek bir yuvası yeniden çekilir, yani bir hece eklenir, silinir ya da değişir.
    """
    if layout is None:
        layout = sample_layout(rng)
    _note(rec, **layout_params(layout))
    k = Knobs(fixed, rec)
    alphabet = _symbols(int(k.get("p_alphabet", lambda: int(rng.integers(15, 26)))))
    n_slots = int(k.get("p_n_slots", lambda: int(rng.integers(3, 9))))
    overlap = float(k.get("p_slot_overlap", lambda: float(rng.uniform(0, 1))))
    slot_alphabets = _slot_alphabets(alphabet, n_slots, overlap, rng)
    n_inv = int(k.get("p_n_inv", lambda: _log_int(2, 30, rng)))
    len_max = int(k.get("p_len_max", lambda: int(rng.integers(1, 3))))
    p_empty = float(k.get("p_empty", lambda: float(rng.uniform(0.1, 0.8))))
    inv: list[list[str]] = []
    weights: list[np.ndarray] = []
    for j in range(n_slots):
        # Yuvalar birbirinin aynısı değildir: boyut ve boş geçme payı yuvadan yuvaya oynar.
        size = max(1, int(round(n_inv * float(np.exp(rng.normal(0, 0.5))))))
        empty = float(np.clip(p_empty + rng.normal(0, 0.15), 0.0, 0.95))
        syl = [x for x in dict.fromkeys(_syllables(slot_alphabets[j], size, len_max, 0.0, rng))]
        inv.append([""] + syl)
        weights.append(np.concatenate([[empty], (1 - empty) * _zipf_weights(len(syl), rng)]))
    p_copy = float(k.get("p_copy", lambda: 0.0 if rng.random() < 0.5 else float(rng.uniform(0.3, 0.95))))
    p_exact = float(k.get("p_exact", lambda: float(rng.uniform(0.0, 0.5))))
    reach = int(k.get("p_reach", lambda: _log_int(1, 30, rng)))
    p_same_line = float(k.get("p_same_line", lambda: float(rng.uniform(0.0, 0.5))))
    cut = np.arange(1, n_slots + 1) / n_slots  # değişecek yuva eşit olasılıkla seçilir
    mean_len = sum(float(np.dot(weights[j], [len(x) for x in inv[j]])) for j in range(n_slots))
    return _cite_text(inv, weights, p_copy, p_exact, reach, p_same_line, cut, mean_len, n_words, layout, rng)


def automaton(
    n_words: int,
    rng: np.random.Generator,
    layout: Layout | None = None,
    rec: dict | None = None,
    fixed: dict | None = None,
) -> Lines:
    """Rastgele kurulmuş katmanlı glif otomatı: her kelime bağımsız bir yürüyüş.

    v0.11 sözlük sınamasından doğan hipotez: Voynich'in dağarcığı, kelime içi
    glif geçişlerinden serbestçe üretilen kelimelerle aynı büyüklükte. Burada
    geçiş yapısı Voynich'ten öğrenilmez, önselden çekilir: glifler katmanlara
    dağıtılır (kelimenin başından sonuna doğru sıralı konum sınıfları), her
    glif aynı ya da sonraki iki katmandaki birkaç glife gidebilir, belli bir
    katmandan sonra kelime bitebilir. Tablo ya da sözlük yoktur; olası kelime
    kümesi sınırsız değil ama çok büyüktür ve seyrek kullanılır.

    Örnek başına rastgele: glif ve katman sayısı, glif başına çıkış sayısı,
    geçiş ağırlıklarının yoğunlaşması (küçükse birkaç geçiş baskın), aynı
    katmanda kalmaya izin verilen kenar payı, kelimenin bitebildiği ilk katman.
    Komşu kelimeler arasında bağ yoktur.
    """
    k = Knobs(fixed, rec)
    n_glyphs = int(k.get("p_alphabet", lambda: int(rng.integers(15, 26))))
    n_levels = int(k.get("p_levels", lambda: int(rng.integers(3, 9))))
    out_deg = int(k.get("p_out_degree", lambda: int(rng.integers(2, 9))))
    conc = float(k.get("p_concentration", lambda: float(np.exp(rng.uniform(np.log(0.2), np.log(3.0))))))
    p_stay = float(k.get("p_stay", lambda: float(rng.uniform(0, 1))))
    end_from = min(
        int(k.get("p_end_from", lambda: int(rng.integers(1, 4)))), n_levels - 1
    )

    glyphs = _symbols(n_glyphs)
    level = rng.integers(0, n_levels, n_glyphs)
    level[:n_levels] = np.arange(n_levels)  # boş katman kalmasın
    level = np.sort(level)
    by_level = [[i for i in range(n_glyphs) if level[i] == lv] for lv in range(n_levels)]
    starts = [i for i in range(n_glyphs) if level[i] <= 1]
    start_cum = np.cumsum(rng.dirichlet(np.full(len(starts), conc)))
    trans: list[tuple[list[int], np.ndarray]] = []
    for i in range(n_glyphs):
        cand: list[int] = []
        for lv in range(int(level[i]), min(n_levels, int(level[i]) + 3)):
            for j in by_level[lv]:
                if lv == level[i] and (j == i or rng.random() > p_stay):
                    continue
                cand.append(j)
        cand = [int(j) for j in rng.permutation(cand)][:out_deg] if cand else []
        opts = cand + ([-1] if level[i] >= end_from or not cand else [])  # -1: kelime biter
        trans.append((opts, np.cumsum(rng.dirichlet(np.full(len(opts), conc)))))

    block = 8192
    uniforms = iter(())

    def u() -> float:
        nonlocal uniforms
        v = next(uniforms, None)
        if v is None:
            uniforms = iter(rng.random(block).tolist())
            v = next(uniforms)
        return v

    words: list[str] = []
    while len(words) < n_words:
        i = starts[min(int(np.searchsorted(start_cum, u(), side="right")), len(starts) - 1)]
        w = glyphs[i]
        while len(w) < 12:
            opts, cum = trans[i]
            i = opts[min(int(np.searchsorted(cum, u(), side="right")), len(opts) - 1)]
            if i < 0:
                break
            w += glyphs[i]
        words.append(w)
    return lay_out(words, rng, layout, rec)


LANGUAGE_PROCESSES: dict[str, Callable[..., Lines]] = {
    "plain": plain,
    "abjad": abjad,
    "verbose": verbose,
    "codebook": codebook,
}
GIBBERISH_PROCESSES: dict[str, Callable[..., Lines]] = {
    "grille": grille,
    "selfcite": selfcite,
    "slotcite": slotcite,
    "slotgram": slotgram,
    "automaton": automaton,
}
