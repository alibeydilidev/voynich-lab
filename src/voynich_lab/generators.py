"""Üretim süreçleri: her biri bir "Voynich nasıl yazıldı" hipotezinin simülasyonu.

Dil tabanlı süreçler gerçek bir metni dönüştürür:
  plain    : düz doğal dil. Tek alfabeli ikame şifresi istatistiksel olarak
             bununla aynıdır (feature'lar sembol adına bakmaz), ayrı sınıf değil.
  abjad    : sesli harfler atılmış yazım
  verbose  : her harf 1-3 sembollük bir gruba açılır (verbose şifre)

Anlamsız metin üreteçleri gerçek metne ihtiyaç duymaz:
  grille   : Rugg tarzı tablo + ızgara (önek/orta/sonek hücreleri)
  selfcite : Timm ve Schinner tarzı kendinden kopyalama (önceki kelimeyi al, boz)

Bunlar bilinçli olarak basit v0 sürümleri. Hattın bilimsel değeri bu
üreteçlerin aslına sadakatine bağlı, asıl geliştirme alanı burası.

Her sürecin üstünde ortak bir "yazıcı" katmanı durur (Layout): metni sayfa
genişliğine göre satırlara böler, paragraf açar ve satır başı, satır sonu,
paragraf başı alışkanlıklarını uygular. Bu katmanın parametreleri bütün
sınıflar için AYNI önselden çekilir. Böylece satır konumu etkileri tek başına
hiçbir sınıfı işaret edemez; sınıflandırıcı onları kestirme yol yapamaz.

Yeni süreç eklemek: fonksiyonu yaz, sonunda lay_out(...) çağır, LANGUAGE_PROCESSES
ya da GIBBERISH_PROCESSES sözlüğüne ekle. Gerisi kendiliğinden akar.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
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
class Layout:
    """Sayfa düzeni ve satır konumu alışkanlıkları.

    words_per_line: satır genişliği, ortalama kelime cinsinden. Satırlar kelime
                    sayısına göre değil genişliğe göre dolar; uzun kelime
                    sığmazsa alt satıra iner (gerçek yazıcı gibi).
    width_jitter  : genişliğin satırdan satıra daralma payı (çizimler, kenar).
    para_lines    : ortalama paragraf uzunluğu (satır). 0 ise paragraf yok.
    """

    words_per_line: float = 9.0
    width_jitter: float = 0.0
    para_lines: float = 0.0
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
    return Layout(
        words_per_line=float(rng.uniform(5, 13)),
        width_jitter=float(rng.uniform(0, 0.35)),
        para_lines=float(rng.uniform(3, 15)) if has_para else 0.0,
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


def decorate(
    lines: Lines, para_starts: list[bool], layout: Layout, rng: np.random.Generator
) -> Lines:
    """Satır başı, satır sonu ve paragraf başı alışkanlıklarını uygular."""
    if not (layout.line_initial or layout.line_final or layout.para_initial):
        return lines
    counts = Counter(ch for ln in lines for w in ln for ch in w)
    ranked = [g for g, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))]
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


def lay_out(words: list[str], rng: np.random.Generator, layout: Layout | None = None) -> Lines:
    """Kelime akışını yazıcı katmanından geçirip satırlara döker.

    layout verilmezse önselden çekilir. Satırlar genişliğe göre dolar: sığmayan
    kelime alt satırın başına iner. Bunun ölçülmüş yan etkisi, hiçbir özel kural
    olmadan da satır başı kelimelerinin ortalamadan uzun çıkmasıdır (sığmayan
    kelime çoğunlukla uzun kelimedir). Satır sonu kelimelerinde böyle bir kayma
    oluşmaz (testi: test_width_wrapping_lengthens_line_initial_words).
    """
    if layout is None:
        layout = sample_layout(rng)
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
    return decorate(lines, para_starts, layout, rng)


# ---------------------------------------------------------------- dil tabanlı


def plain(words: list[str], rng: np.random.Generator, layout: Layout | None = None) -> Lines:
    return lay_out(list(words), rng, layout)


def abjad(words: list[str], rng: np.random.Generator, layout: Layout | None = None) -> Lines:
    """Sesli harfleri atar. Tamamen sesliden oluşan kelimenin ilk harfi kalır."""
    out = []
    for w in words:
        c = "".join(ch for ch in w if not is_vowel(ch))
        out.append(c or w[0])
    return lay_out(out, rng, layout)


def verbose(words: list[str], rng: np.random.Generator, layout: Layout | None = None) -> Lines:
    """Verbose şifre: sık harfler kısa, seyrek harfler uzun sembol grubu alır.

    Örnek başına rastgele: şifre alfabesi boyutu, kod tablosu ve kelime
    sınırlarının korunup korunmayacağı (kelime içi bölme olasılığı).
    """
    alphabet = _symbols(int(rng.integers(12, 23)))
    letters, counts = np.unique([ch for w in words for ch in w], return_counts=True)
    order = letters[np.argsort(-counts)]

    codes: dict[str, str] = {}
    used: set[str] = set()
    for rank, letter in enumerate(order):
        # Sık harfler için kısa kod olasılığı daha yüksek.
        p_short = max(0.1, 0.6 - 0.04 * rank)
        while True:
            length = 1 if rng.random() < p_short else int(rng.integers(2, 4))
            code = "".join(rng.choice(alphabet, size=length))
            if code not in used:
                used.add(code)
                codes[letter] = code
                break

    split_p = float(rng.choice([0.0, 0.0, 0.15, 0.3]))  # kelime içi boşluk ekleme
    out: list[str] = []
    for w in words:
        cur = ""
        for ch in w:
            cur += codes[ch]
            if split_p and rng.random() < split_p:
                out.append(cur)
                cur = ""
        if cur:
            out.append(cur)
    return lay_out(out, rng, layout)


# ------------------------------------------------------------------- anlamsız


def _zipf_weights(n: int, rng: np.random.Generator) -> np.ndarray:
    w = 1.0 / np.arange(1, n + 1) ** rng.uniform(0.6, 1.2)
    return w / w.sum()


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


def grille(n_words: int, rng: np.random.Generator, layout: Layout | None = None) -> Lines:
    """Rugg (2004) tarzı: üç sütunlu hece tablosu, üzerinde gezen delikli ızgara.

    Her ızgara üç sütun için birer satır kayması tanımlar. Izgara tabloyu
    baştan sona tarar, sonra sıradaki ızgaraya geçilir.
    """
    alphabet = _symbols(int(rng.integers(15, 26)))
    rows = int(rng.integers(60, 201))
    inv_p = _syllables(alphabet, int(rng.integers(8, 21)), 2, 0.3, rng)
    inv_m = _syllables(alphabet, int(rng.integers(15, 41)), 3, 0.0, rng)
    inv_s = _syllables(alphabet, int(rng.integers(8, 21)), 2, 0.3, rng)
    col_p = rng.choice(inv_p, size=rows, p=_zipf_weights(len(inv_p), rng))
    col_m = rng.choice(inv_m, size=rows, p=_zipf_weights(len(inv_m), rng))
    col_s = rng.choice(inv_s, size=rows, p=_zipf_weights(len(inv_s), rng))
    grilles = rng.integers(0, rows, size=(int(rng.integers(3, 9)), 3))

    words: list[str] = []
    j = 0
    while len(words) < n_words:
        a, b, c = grilles[(j // rows) % len(grilles)]
        r = j % rows
        w = col_p[(r + a) % rows] + col_m[(r + b) % rows] + col_s[(r + c) % rows]
        if w:
            words.append(str(w))
        j += 1
    return lay_out(words, rng, layout)


def selfcite(n_words: int, rng: np.random.Generator, layout: Layout | None = None) -> Lines:
    """Timm ve Schinner (2019) tarzı: yazıcı önceki satırlardan kelime kopyalar,
    küçük değişikliklerle yeniden yazar. Benzer kelimelerin yakın durması ve
    yoğun "bir harf farklı" kelime ağı bu sürecin doğal sonucudur.

    Kopyalama satır konumuna bağlı olduğu için bu süreç satırlarını kendisi
    kurar, ama genişlik ve paragraf kararını ortak yazıcı katmanından alır.
    Satır konumu işaretleri en sonda uygulanır, kopyalanan kaynak işaretsizdir.
    """
    if layout is None:
        layout = sample_layout(rng)
    alphabet = _symbols(int(rng.integers(15, 26)))
    sym_w = _zipf_weights(len(alphabet), rng)
    # Benzer görünen glif sınıfları: değişiklikler çoğunlukla sınıf içinde olur.
    classes = np.array_split(rng.permutation(len(alphabet)), int(rng.integers(4, 8)))
    class_of = {alphabet[i]: [alphabet[k] for k in cls] for cls in classes for i in cls}
    prefixes = [str(s) for s in rng.choice(alphabet, size=3, p=sym_w)]
    p_copy = rng.uniform(0.85, 0.97)

    def fresh() -> str:
        return "".join(rng.choice(alphabet, size=int(rng.integers(2, 7)), p=sym_w))

    def mutate(w: str) -> str:
        r = rng.random()
        if r < 0.30 or not w:
            return w
        i = int(rng.integers(0, len(w)))
        if r < 0.60:  # benzer glifle değiştir
            return w[:i] + str(rng.choice(class_of[w[i]])) + w[i + 1 :]
        if r < 0.75:  # önek ekle ya da at
            if w[0] in prefixes and len(w) > 2:
                return w[1:]
            return str(rng.choice(prefixes)) + w
        if r < 0.87 and len(w) > 2:  # glif sil
            return w[:i] + w[i + 1 :]
        return w[:i] + w[i] + w[i:]  # glifi ikile

    def next_word(lines: Lines, line: list[str]) -> str:
        if lines and rng.random() < p_copy:
            # Kaynak: son üç satırda benzer konum ya da aynı satırın başı.
            src_line = lines[-int(rng.integers(1, min(3, len(lines)) + 1))]
            if line and rng.random() < 0.25:
                src = line[int(rng.integers(0, len(line)))]
            else:
                k = min(len(src_line) - 1, max(0, len(line) + int(rng.integers(-1, 2))))
                src = src_line[k]
            return mutate(src)[:10] or fresh()
        return fresh()

    budgets = layout.budgets(4.0 + 1.0, rng)  # fresh() ortalama 4 glif üretir
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
    return decorate(lines, para_starts, layout, rng)


LANGUAGE_PROCESSES: dict[str, Callable[..., Lines]] = {
    "plain": plain,
    "abjad": abjad,
    "verbose": verbose,
}
GIBBERISH_PROCESSES: dict[str, Callable[..., Lines]] = {
    "grille": grille,
    "selfcite": selfcite,
}
