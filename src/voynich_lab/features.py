"""Bir metin penceresinden sembol adından bağımsız istatistikler çıkarır.

Temel ilke: hiçbir feature "hangi harf" olduğuna bakmaz, yalnızca dağılımın
şekline bakar. Böylece Latince, İbranice, EVA ve v101 aynı uzayda kıyaslanır.
Sonuç: tek alfabeli ikame şifresi feature vektörünü değiştirmez (testi var).

Feature'lar pencere boyutuna duyarlıdır (entropi tahminleri, TTR). Sentetik
veri ile Voynich pencereleri bu yüzden aynı kelime sayısıyla kesilmelidir.
"""

from __future__ import annotations

from collections import Counter
from math import log2

import numpy as np

from . import Lines


def _entropy(counter: Counter) -> float:
    total = sum(counter.values())
    if total == 0:
        return 0.0
    return -sum((c / total) * log2(c / total) for c in counter.values())


def _jsd(a: Counter, b: Counter) -> float:
    """Jensen-Shannon ıraksaması (bit, 0..1)."""
    ta, tb = sum(a.values()), sum(b.values())
    if ta == 0 or tb == 0:
        return 0.0
    mix = Counter()
    for k, v in a.items():
        mix[k] += 0.5 * v / ta
    for k, v in b.items():
        mix[k] += 0.5 * v / tb
    h_mix = -sum(p * log2(p) for p in mix.values() if p > 0)
    return max(0.0, h_mix - 0.5 * _entropy(a) - 0.5 * _entropy(b))


def _ngram_counts(seq: str, n: int) -> Counter:
    return Counter(seq[i : i + n] for i in range(len(seq) - n + 1))


def _is_ed1(a: str, b: str) -> bool:
    """Düzenleme mesafesi tam 1 mi (tek ekleme, silme ya da değiştirme)."""
    la, lb = len(a), len(b)
    if abs(la - lb) > 1 or a == b:
        return False
    if la == lb:
        return sum(x != y for x, y in zip(a, b)) == 1
    if la > lb:
        a, b = b, a
    i = 0
    while i < len(a) and a[i] == b[i]:
        i += 1
    return a[i:] == b[i + 1 :]


def _ed1_density(types: list[str]) -> float:
    """En az bir "tek harf farklı" komşusu olan kelime türlerinin oranı.

    Voynich'in ayırt edici özelliği: kelime dağarcığı çok sıkı bir ağ kurar
    (daiin, dain, aiin, saiin ...). Doğal dillerde bu oran belirgin düşüktür.
    """
    vocab = set(types)
    patterns: Counter = Counter()
    for w in vocab:
        for i in range(len(w)):
            patterns[w[:i] + "\0" + w[i + 1 :]] += 1
    linked: set[str] = set()
    for w in vocab:
        for i in range(len(w)):
            if patterns[w[:i] + "\0" + w[i + 1 :]] > 1:  # tek harf değişik komşu
                linked.add(w)
            shorter = w[:i] + w[i + 1 :]
            if shorter in vocab:  # tek harf eksik komşu, ilişki iki yönlü
                linked.add(w)
                linked.add(shorter)
    return len(linked) / max(1, len(vocab))


def extract_features(lines: Lines) -> dict[str, float]:
    """Bir pencere için feature sözlüğü döndürür."""
    lines = [ln for ln in lines if ln]
    words = [w for ln in lines for w in ln]
    n = len(words)
    if n < 50:
        raise ValueError("pencere çok kısa (en az 50 kelime gerekir)")
    f: dict[str, float] = {}

    # ---- karakter düzeyi entropi
    stream = " ".join(words)  # boşluk da bir sembol (klasik h1/h2 tanımı)
    u1, u2, u3 = (_ngram_counts(stream, k) for k in (1, 2, 3))
    h1 = _entropy(u1)
    f["h1"] = h1
    f["h2"] = _entropy(u2) - h1  # H(c_n | c_{n-1})
    f["h3"] = _entropy(u3) - _entropy(u2)
    f["h2_over_h1"] = f["h2"] / h1 if h1 else 0.0
    inner = Counter(ch for w in words for ch in w)
    h1_inner = _entropy(inner)
    f["n_symbols"] = float(len(inner))
    f["eff_symbols"] = 2.0**h1_inner
    inner_bi = Counter(w[i : i + 2] for w in words for i in range(len(w) - 1))
    n_bi = sum(inner_bi.values())
    f["char_double_rate"] = (
        sum(c for bg, c in inner_bi.items() if bg[0] == bg[1]) / n_bi if n_bi else 0.0
    )

    # ---- kelime uzunluğu
    lens = np.array([len(w) for w in words], dtype=float)
    mu, sd = lens.mean(), lens.std()
    f["wlen_mean"] = mu
    f["wlen_std"] = sd
    f["wlen_skew"] = float(((lens - mu) ** 3).mean() / sd**3) if sd > 0 else 0.0
    f["wlen_frac1"] = float((lens == 1).mean())
    f["wlen_frac_le2"] = float((lens <= 2).mean())
    if n > 2 and sd > 0:
        f["wlen_autocorr1"] = float(np.corrcoef(lens[:-1], lens[1:])[0, 1])
    else:
        f["wlen_autocorr1"] = 0.0

    # ---- dağarcık
    wc = Counter(words)
    types = list(wc)
    freqs = np.array(sorted(wc.values(), reverse=True), dtype=float)
    f["ttr"] = len(types) / n
    f["hapax_ratio"] = float((freqs == 1).sum()) / len(types)
    f["word_entropy_norm"] = _entropy(wc) / log2(n)
    f["top1_freq"] = freqs[0] / n
    f["top10_coverage"] = freqs[:10].sum() / n
    k = min(len(freqs), 200)
    if k >= 5:
        slope = np.polyfit(np.log(np.arange(1, k + 1)), np.log(freqs[:k]), 1)[0]
        f["zipf_slope"] = float(slope)
    else:
        f["zipf_slope"] = 0.0
    f["type_len_mean"] = float(np.mean([len(t) for t in types]))
    f["vocab_ed1_density"] = _ed1_density(types)

    # ---- tekrar yapısı
    pairs = list(zip(words[:-1], words[1:]))
    f["rep_adjacent_exact"] = sum(a == b for a, b in pairs) / len(pairs)
    f["rep_adjacent_ed1"] = sum(_is_ed1(a, b) for a, b in pairs) / len(pairs)
    f["rep_within3"] = sum(words[i] in words[max(0, i - 3) : i] for i in range(1, n)) / (n - 1)

    # ---- kelime içi konum kısıtları
    first = Counter(w[0] for w in words)
    last = Counter(w[-1] for w in words)
    non_first = Counter(ch for w in words for ch in w[1:])
    non_last = Counter(ch for w in words for ch in w[:-1])
    f["jsd_first"] = _jsd(first, non_first)
    f["jsd_last"] = _jsd(last, non_last)
    f["first_entropy_ratio"] = _entropy(first) / h1_inner if h1_inner else 0.0
    f["last_entropy_ratio"] = _entropy(last) / h1_inner if h1_inner else 0.0

    # ---- satır konumu etkileri (doğal dilde satır kırılımı rastgeledir)
    li_first = Counter(ln[0][0] for ln in lines)
    other_first = Counter(w[0] for ln in lines for w in ln[1:])
    lf_last = Counter(ln[-1][-1] for ln in lines)
    other_last = Counter(w[-1] for ln in lines for w in ln[:-1])
    f["jsd_line_initial"] = _jsd(li_first, other_first)
    f["jsd_line_final"] = _jsd(lf_last, other_last)
    f["len_ratio_line_initial"] = float(np.mean([len(ln[0]) for ln in lines]) / mu)
    f["len_ratio_line_final"] = float(np.mean([len(ln[-1]) for ln in lines]) / mu)

    return f


FEATURE_NAMES: list[str] = list(
    extract_features([["ab", "ba", "abc"] * 4 for _ in range(6)]).keys()
)
