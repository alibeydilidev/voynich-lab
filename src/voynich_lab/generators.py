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

Yeni süreç eklemek: fonksiyonu yaz, LANGUAGE_PROCESSES ya da
GIBBERISH_PROCESSES sözlüğüne ekle. Gerisi kendiliğinden akar.
"""

from __future__ import annotations

from typing import Callable

import numpy as np

from . import Lines
from .corpus import is_vowel

# Sentetik semboller için özel kullanım alanı (gerçek alfabelerle karışmasın).
_SYM_BASE = 0xE100


def _symbols(n: int) -> list[str]:
    return [chr(_SYM_BASE + i) for i in range(n)]


def wrap(words: list[str], rng: np.random.Generator) -> Lines:
    """Kelime akışını Voynich'e benzer uzunlukta (6-12 kelime) satırlara böler."""
    lines, i = [], 0
    while i < len(words):
        n = int(rng.integers(6, 13))
        lines.append(words[i : i + n])
        i += n
    return lines


# ---------------------------------------------------------------- dil tabanlı


def plain(words: list[str], rng: np.random.Generator) -> Lines:
    return wrap(list(words), rng)


def abjad(words: list[str], rng: np.random.Generator) -> Lines:
    """Sesli harfleri atar. Tamamen sesliden oluşan kelimenin ilk harfi kalır."""
    out = []
    for w in words:
        c = "".join(ch for ch in w if not is_vowel(ch))
        out.append(c or w[0])
    return wrap(out, rng)


def verbose(words: list[str], rng: np.random.Generator) -> Lines:
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
    return wrap(out, rng)


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


def grille(n_words: int, rng: np.random.Generator) -> Lines:
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
    return wrap(words, rng)


def selfcite(n_words: int, rng: np.random.Generator) -> Lines:
    """Timm ve Schinner (2019) tarzı: yazıcı önceki satırlardan kelime kopyalar,
    küçük değişikliklerle yeniden yazar. Benzer kelimelerin yakın durması ve
    yoğun "bir harf farklı" kelime ağı bu sürecin doğal sonucudur.
    """
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

    lines: Lines = [[fresh() for _ in range(8)]]
    total = 8
    while total < n_words:
        n = int(rng.integers(6, 13))
        line: list[str] = []
        for pos in range(n):
            if rng.random() < p_copy:
                # Kaynak: son üç satırda benzer konum ya da aynı satırın başı.
                src_line = lines[-int(rng.integers(1, min(3, len(lines)) + 1))]
                if line and rng.random() < 0.25:
                    src = line[int(rng.integers(0, len(line)))]
                else:
                    k = min(len(src_line) - 1, max(0, pos + int(rng.integers(-1, 2))))
                    src = src_line[k]
                w = mutate(src)[:10]
            else:
                w = fresh()
            line.append(w or fresh())
        lines.append(line)
        total += n
    return lines


LANGUAGE_PROCESSES: dict[str, Callable[[list[str], np.random.Generator], Lines]] = {
    "plain": plain,
    "abjad": abjad,
    "verbose": verbose,
}
GIBBERISH_PROCESSES: dict[str, Callable[[int, np.random.Generator], Lines]] = {
    "grille": grille,
    "selfcite": selfcite,
}
