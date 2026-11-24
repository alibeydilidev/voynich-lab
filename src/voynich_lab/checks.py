"""Hattın kendi sonuçlarını sınayan deneyler.

evaize deneyi: sınıflandırıcı düz EVA görünümlerinde `verbose`, birleşik glif
görünümlerinde `grille` diyor. Soru: bu fark Voynich'ten mi, yoksa EVA'nın tek
glifi birkaç harfle yazma alışkanlığından mı geliyor? Sınama: bilinen anlamsız
metinleri (grille, selfcite) EVA'nın yaptığı gibi yeniden yaz ve sınıflandırıcıya
sor. Cevap değişiyorsa düz EVA görünümleri "şifre mi, anlamsız mı" ayrımında
kullanılamaz.

homojenlik deneyi: ABC ve arama, her sentetik örneği ayrı bir "el yazması"
gibi baştan üretir (yeni tablo, yeni alfabe). Voynich pencereleri ise tek bir
el yazmasının parçalarıdır. Soru: sentetik örnekler arası farkın ne kadarı
ayarlardan ve tablodan, ne kadarı aynı tablonun farklı metninden geliyor; ve
tek bir tablo, Voynich'in kendi içindeki kadar değişken metin üretiyor mu?

sözlük deneyi: bir metnin kelimeleri sınırlı bir sözlükten mi geliyor, yoksa
kelime içi harf dizilişi kurallarının izin verdiği her şey mi yazılıyor? Ölçüm
hiçbir üretece ya da önsele dayanmaz. Metnin ilk yarısından k. dereceden bir
glif zinciri öğrenilir (kelime başı ve sonu dahil) ve aynı sayıda kelime
bağımsız çekilir: bu "vekil" metindir. İki sayı:

  tür oranı : vekildeki farklı kelime sayısı / gerçek metindeki farklı kelime
              sayısı. Sözlüğü olan dilde vekil, dilde olmayan pek çok "kelime"
              uydurur ve oran 1'in çok üstüne çıkar. Sözlük yoksa oran 1'dir.
  yeni kelime oranı : vekildeki, ilk yarıda hiç görülmemiş kelimelerin payı /
              gerçek ikinci yarıdaki aynı pay. Aynı sorunun görülmemiş veriyle
              sorulmuş hâli: gerçek metin, vekil kadar sık yeni kelime üretiyor mu?

sıra deneyi: kelimelerin sırası, hangi kelimelerin bir arada geçtiğinin ötesinde
bilgi taşıyor mu? İlk yarıdan kelime ikilisi modeli öğrenilir ve görülmemiş
ikinci yarıda, tek kelime sıklığı modeline göre kelime başına kaç bit
kazandırdığı ölçülür. Aynı ölçüm, her satırın kelimeleri kendi içinde
karıştırılmış metinde tekrarlanır; fark sıranın taşıdığı bilgidir. Bire bir
kelime kodlaması (kod defteri) kelime kimliklerini koruduğu için kaynak dille
aynı sayıyı verir.

bozulma taraması: iki sınama ve büyüme profili birlikte, gerçek bir dil metni
hangi bozulma altında Voynich gibi görünür sorusuna uygulanır (yazım
çeşitlemesi, eşsesli yazım; sesli ve seslisiz). Üç ölçütü birden tutturan
düzenlerde, kelime türleri "bir harf farklı" ailelerine toplandıktan sonra
sıra bilgisinin geri gelip gelmediğine de bakılır.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from math import log2

import numpy as np
import pandas as pd

from . import Lines
from .dataset import _truncate
from .features import FEATURE_NAMES, extract_features
from .generators import GIBBERISH_PROCESSES
from .model import fit

_STROKE_C, _STROKE_H = chr(0xF000), chr(0xF001)


def evaize(lines: Lines) -> Lines | None:
    """Altı glifi EVA'daki kalıpla çok harfli diziye açar.

    EVA'da `ch` ve `sh` sık, `cth ckh cph cfh` seyrek gliflerdir ve hepsi `c`,
    `h` çizgilerini paylaşır. Aynı kalıp: iki sık glif C+H ve S+H olur, dört
    seyrek glif C+T+H olur (S ve T metinde zaten bulunan gliflerdir).
    Alfabe 17 gliften küçükse None döner.
    """
    counts = Counter(ch for ln in lines for w in ln for ch in w)
    ranked = [g for g, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))]
    if len(ranked) < 17:
        return None
    table = {ranked[1]: _STROKE_C + _STROKE_H, ranked[6]: ranked[8] + _STROKE_H}
    for src, mid in zip(ranked[11:15], (ranked[7], ranked[9], ranked[10], ranked[15])):
        table[src] = _STROKE_C + mid + _STROKE_H
    return [["".join(table.get(ch, ch) for ch in w) for w in ln] for ln in lines]


def evaize_experiment(
    df: pd.DataFrame, window_words: int = 2000, n: int = 300, seed: int = 123, model_seed: int = 7
) -> dict:
    """Anlamsız metin örneklerinin özgün ve EVA'laştırılmış hâllerini sınıflandırır."""
    model, classes = fit(df, seed=model_seed)
    rng = np.random.default_rng(seed)
    out: dict = {"n": n, "classes": classes, "processes": {}}
    for name, proc in GIBBERISH_PROCESSES.items():
        plain_rows, eva_rows = [], []
        while len(plain_rows) < n:
            lines = _truncate(proc(window_words + 50, rng), window_words)
            split = evaize(lines)
            if split is None:
                continue
            plain_rows.append(extract_features(lines))
            eva_rows.append(extract_features(split))
        res = {}
        for tag, rows in (("original", plain_rows), ("evaized", eva_rows)):
            proba = model.predict_proba(pd.DataFrame(rows)[FEATURE_NAMES].to_numpy(dtype=float))
            votes = Counter(classes[i] for i in proba.argmax(1))
            res[tag] = {
                "votes": {c: int(votes.get(c, 0)) for c in classes},
                "mean_proba": {c: float(p) for c, p in zip(classes, proba.mean(0))},
            }
        out["processes"][name] = res
    return out


def _windows(lines: Lines, window_words: int) -> list[Lines]:
    out, cur, count = [], [], 0
    for ln in lines:
        cur.append(ln)
        count += len(ln)
        if count >= window_words:
            out.append(cur)
            cur, count = [], 0
    return out


def homogeneity_experiment(
    df: pd.DataFrame,
    voynich: dict[str, pd.DataFrame],
    window_words: int = 2000,
    n_manuscripts: int = 12,
    n_windows: int = 8,
    seed: int = 5,
) -> dict:
    """Aynı tablodan uzun metin üretir, pencerelerin iç değişkenliğini Voynich'inkiyle kıyaslar.

    Birim abc.py ile aynıdır (Voynich pencereleri arası standart sapma). "İç":
    bir el yazmasının pencerelerinin kendi ortalamalarına ortalama uzaklığı.
    "Arası": farklı el yazmalarının ortalamalarının genel ortalamaya uzaklığı.
    """
    from .abc import SCALE_FLOOR

    rng = np.random.default_rng(seed)
    universe_sd = df[FEATURE_NAMES].to_numpy(dtype=float).std(0)
    books: dict[str, list[np.ndarray]] = {}
    for name, proc in GIBBERISH_PROCESSES.items():
        books[name] = []
        while len(books[name]) < n_manuscripts:
            wins = _windows(proc((n_windows + 1) * window_words, rng), window_words)[:n_windows]
            if len(wins) == n_windows:
                feats = [extract_features(w) for w in wins]
                books[name].append(np.array([[f[n] for n in FEATURE_NAMES] for f in feats]))

    def rms(z: np.ndarray) -> np.ndarray:
        return np.sqrt((z**2).mean(-1))

    out: dict = {"n_manuscripts": n_manuscripts, "n_windows": n_windows, "views": {}}
    for view, vf in voynich.items():
        V = vf[FEATURE_NAMES].to_numpy(dtype=float)
        scale = np.maximum(V.std(0, ddof=1), SCALE_FLOOR * universe_sd) + 1e-12
        res = {"voynich_within": float(rms((V - V.mean(0)) / scale).mean())}
        for name, mss in books.items():
            means = np.array([F.mean(0) for F in mss])
            res[name] = {
                "within": float(np.mean([rms((F - F.mean(0)) / scale).mean() for F in mss])),
                "between": float(rms((means - means.mean(0)) / scale).mean()),
            }
        out["views"][view] = res
    return out


def render_homogeneity(result: dict) -> str:
    procs = [k for k in next(iter(result["views"].values())) if k != "voynich_within"]
    md = [
        "# Sınama: tek bir tablo Voynich kadar değişken metin üretiyor mu",
        "",
        f"Her süreçten {result['n_manuscripts']} el yazması üretildi; her biri tek tablo ve tek "
        f"ayar kümesiyle {result['n_windows']} pencere. Birim Voynich pencereleri arası değişkenlik. "
        "\"İç\": pencerelerin kendi el yazmasının ortalamasına uzaklığı. \"Arası\": farklı el "
        "yazmalarının ortalamaları arasındaki uzaklık.",
        "",
        "| görünüm | Voynich iç | " + " | ".join(f"{p} iç | {p} arası" for p in procs) + " |",
        "|---|---|" + "---|---|" * len(procs),
    ]
    for view, r in result["views"].items():
        md.append(
            f"| {view} | {r['voynich_within']:.2f} | "
            + " | ".join(f"{r[p]['within']:.2f} | {r[p]['between']:.2f}" for p in procs)
            + " |"
        )
    return "\n".join(md) + "\n"


def markov_surrogate(words: list[str], k: int, n: int, rng: np.random.Generator) -> list[str]:
    """`words` içindeki kelime içi glif dizilişinden (k. derece) n kelime bağımsız çeker."""
    trans: dict[str, Counter] = defaultdict(Counter)
    for w in words:
        s = "\x02" * k + w + "\x03"
        for i in range(k, len(s)):
            trans[s[i - k : i]][s[i]] += 1
    table = {
        ctx: (list(c), np.cumsum(list(c.values())) / sum(c.values())) for ctx, c in trans.items()
    }
    out: list[str] = []
    while len(out) < n:
        ctx, w = "\x02" * k, ""
        while True:
            syms, cum = table[ctx]
            ch = syms[min(int(np.searchsorted(cum, rng.random(), side="right")), len(syms) - 1)]
            if ch == "\x03":
                break
            w += ch
            ctx = (ctx + ch)[-k:]
        if w:
            out.append(w)
    return out


def lexicon_stats(
    words: list[str], rng: np.random.Generator, half: int = 16000, orders: tuple[int, ...] = (1, 2)
) -> dict[str, float] | None:
    """Bir metin için sözlük ölçüleri. Metin 2 * half kelimeden kısaysa None."""
    if len(words) < 2 * half:
        return None
    train, test = words[:half], words[half : 2 * half]
    vocab = set(train)
    real_new = sum(w not in vocab for w in test) / half
    out = {
        "types": float(len(vocab)),
        "mean_len": float(np.mean([len(w) for w in train])),
        "real_new": real_new,
    }
    for k in orders:
        sur = markov_surrogate(train, k, half, rng)
        out[f"type_ratio_k{k}"] = len(set(sur)) / len(vocab)
        out[f"new_ratio_k{k}"] = (sum(w not in vocab for w in sur) / half) / max(real_new, 1e-9)
    return out


def lexicon_experiment(
    voynich: dict[str, list[str]],
    corpora: dict[str, list[str]],
    n_per_class: int = 30,
    seed: int = 11,
    half: int = 16000,
    period: dict[str, list[str]] | None = None,
    sections: dict[str, list[str]] | None = None,
    section_half: int = 5000,
) -> dict:
    """Voynich, doğal diller (düz ve seslisiz), dönem metinleri ve üreteç sınıfları için sözlük ölçüleri.

    period  : 15. yüzyıl metinleri (modern İncil çevirilerine karşı denetim).
    sections: Voynich'in bölümleri (Currier dili, çizim türü). Bölümler kısa
              olduğu için ayrı ve daha küçük bir yarı boyuyla (section_half)
              ölçülür; karşılaştırma tabanı aynı boyda yeniden hesaplanır.
    """
    from .corpus import ABJAD_CAPABLE_SCRIPTS, dominant_script, is_vowel
    from .generators import LANGUAGE_PROCESSES

    rng = np.random.default_rng(seed)
    need = 2 * half + 2000
    out: dict = {"half": half, "voynich": {}, "groups": {}}
    for view, words in voynich.items():
        out["voynich"][view] = lexicon_stats(words, rng, half)
    plain_rows, abjad_rows = {}, {}
    for lang in sorted(corpora):
        words = corpora[lang][20000 : 20000 + need]
        plain_rows[lang] = lexicon_stats(words, rng, half)
        if dominant_script(words) in ABJAD_CAPABLE_SCRIPTS:
            bare = [("".join(ch for ch in w if not is_vowel(ch)) or w[0]) for w in words]
            abjad_rows[lang] = lexicon_stats(bare, rng, half)
    out["groups"]["doğal dil, düz"] = plain_rows
    out["groups"]["doğal dil, seslisiz"] = abjad_rows
    if period:
        rows, bare_rows = {}, {}
        for name, words in period.items():
            body = words[500:]  # baştaki sayfa başlığı ve gezinme metni
            rows[name] = lexicon_stats(body, rng, half)
            bare = [("".join(ch for ch in w if not is_vowel(ch)) or w[0]) for w in body]
            bare_rows[name] = lexicon_stats(bare, rng, half)
        out["groups"]["dönem metni (15. yy), düz"] = rows
        out["groups"]["dönem metni (15. yy), seslisiz"] = bare_rows
    if sections:
        out["section_half"] = section_half
        out["sections"] = {
            name: lexicon_stats(words, rng, section_half) for name, words in sections.items()
        }
        need_s = 2 * section_half
        out["section_reference"] = {
            lang: lexicon_stats(corpora[lang][20000 : 20000 + need_s], rng, section_half)
            for lang in sorted(corpora)
        }
    languages = sorted(corpora)
    for name in ("verbose", "codebook"):
        rows = {}
        for i in range(n_per_class):
            lang = languages[int(rng.integers(len(languages)))]
            start = int(rng.integers(0, len(corpora[lang]) - need))
            lines = LANGUAGE_PROCESSES[name](corpora[lang][start : start + need], rng)
            r = lexicon_stats([w for ln in lines for w in ln], rng, half)
            if r is not None:
                rows[f"{name} {i} ({lang})"] = r
        out["groups"][name] = rows
    for name, proc in GIBBERISH_PROCESSES.items():
        rows = {}
        for i in range(n_per_class):
            r = lexicon_stats([w for ln in proc(need, rng) for w in ln], rng, half)
            if r is not None:
                rows[f"{name} {i}"] = r
        out["groups"][name] = rows
    return out


# ------------------------------------------------------------------ sıra deneyi

_MIX_WEIGHTS = (0.0, 0.02, 0.05, 0.1, 0.2, 0.3, 0.45, 0.6, 0.75)


def order_gain(train: list[str], test: list[str]) -> tuple[float, float, float]:
    """Kelime ikilisi modelinin görülmemiş metinde tekli modele göre kazancı.

    Dönüş: (tekli model kelime başına bit, kazanç bit, seçilen karışım ağırlığı).
    İkili ve tekli model doğrusal karıştırılır; ağırlık eğitim metninin son
    beşte birinde seçilir, sınama metnine hiç bakılmaz. Sıra bilgi taşımıyorsa
    ağırlık sıfıra yakın seçilir ve kazanç sıfır çıkar.
    """

    def tables(words: list[str]):
        uni = Counter(words)
        big: dict[str, Counter] = defaultdict(Counter)
        for a, b in zip(words[:-1], words[1:]):
            big[a][b] += 1
        return uni, big, {a: sum(c.values()) for a, c in big.items()}, len(words)

    def cost(model, words: list[str], lam: float) -> tuple[float, float]:
        uni, big, ctx, n = model
        v = len(uni) + 1
        h_uni = h_mix = 0.0
        for a, b in zip(words[:-1], words[1:]):
            pu = (uni.get(b, 0) + 1) / (n + v)
            pb = big[a].get(b, 0) / ctx[a] if a in ctx else pu
            h_uni -= log2(pu)
            h_mix -= log2((1 - lam) * pu + lam * pb)
        m = max(len(words) - 1, 1)
        return h_uni / m, h_mix / m

    cut = int(len(train) * 0.8)
    small = tables(train[:cut])
    lam = min((cost(small, train[cut:], w)[1], w) for w in _MIX_WEIGHTS)[1]
    h_uni, h_mix = cost(tables(train), test, lam)
    return h_uni, h_uni - h_mix, lam


def order_stats(
    lines: Lines, half: int, rng: np.random.Generator, n_shuffles: int = 3
) -> dict[str, float] | None:
    """Bir metnin kelime sırası bilgisi. Metin 2 * half kelimeden kısaysa None.

    order: gerçek metindeki kazanç eksi satır içi karıştırılmış metindeki kazanç.
    """
    if sum(len(ln) for ln in lines) < 2 * half:
        return None

    def split(ls: Lines) -> tuple[list[str], list[str]]:
        train: list[str] = []
        test: list[str] = []
        count = 0
        for ln in ls:
            (train if count < half else test).extend(ln)
            count += len(ln)
        return train[:half], test[:half]

    h_uni, real, lam = order_gain(*split(lines))
    shuffled = float(
        np.mean(
            [
                order_gain(*split([[ln[int(i)] for i in rng.permutation(len(ln))] for ln in lines]))[1]
                for _ in range(n_shuffles)
            ]
        )
    )
    return {"unigram_bits": h_uni, "real": real, "shuffled": shuffled, "order": real - shuffled, "weight": lam}


def word_families(words: list[str]) -> dict[str, str]:
    """Kelime türlerini "bir harf farklı" ailelerine toplar.

    Türler sıklık sırasıyla işlenir: her tür, daha sık bir "bir harf farklı"
    komşusu (değiştirme, ekleme ya da silme) varsa onun ailesine katılır,
    yoksa kendi ailesini kurar. Dönüş: {tür: aile temsilcisi}.
    """
    counts = Counter(words)
    family: dict[str, str] = {}
    by_pattern: dict[str, list[str]] = defaultdict(list)
    for w, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        cands: set[str] = set()
        for i in range(len(w)):
            cands.update(by_pattern.get(w[:i] + "\0" + w[i + 1 :], ()))
            shorter = w[:i] + w[i + 1 :]
            if shorter in family:
                cands.add(shorter)
        for i in range(len(w) + 1):
            cands.update(by_pattern.get(w[:i] + "\0" + w[i:], ()))
        cands.discard(w)
        family[w] = family[max(cands, key=lambda c: (counts[c], c))] if cands else w
        for i in range(len(w)):
            by_pattern[w[:i] + "\0" + w[i + 1 :]].append(w)
    return family


def spelling_noise(words: list[str], p: float, rng: np.random.Generator) -> list[str]:
    """Kelimelerin p kadarını bir harfi değişmiş, silinmiş ya da eklenmiş yazar."""
    letters = sorted({c for w in words[:5000] for c in w})
    out = []
    for w in words:
        if rng.random() < p:
            i = int(rng.integers(0, len(w)))
            r = rng.random()
            if r < 0.5:
                w = w[:i] + letters[int(rng.integers(len(letters)))] + w[i + 1 :]
            elif r < 0.75 and len(w) > 1:
                w = w[:i] + w[i + 1 :]
            else:
                w = w[:i] + letters[int(rng.integers(len(letters)))] + w[i:]
        out.append(w)
    return out


def homophonic(words: list[str], share: float, k: int, rng: np.random.Generator) -> list[str]:
    """Eşsesli yazım: harflerin `share` kadarının k ayrı yazılışı vardır, her geçişte biri rastgele seçilir."""
    letters = sorted({c for w in words[:8000] for c in w})
    table = {
        c: [chr(0xF200 + 8 * i + j) for j in range(k if rng.random() < share else 1)]
        for i, c in enumerate(letters)
    }
    return [
        "".join(table[c][int(rng.integers(len(table[c])))] if c in table else c for c in w)
        for w in words
    ]


def _chunk(words: list[str], size: int = 9) -> Lines:
    """Satır yapısı olmayan metni Voynich'e yakın uzunlukta (9 kelime) satırlara böler."""
    return [words[i : i + size] for i in range(0, len(words), size)]


def order_experiment(
    voynich: dict[str, Lines],
    corpora: dict[str, list[str]],
    period: dict[str, list[str]] | None = None,
    sections: dict[str, Lines] | None = None,
    n_per_class: int = 20,
    seed: int = 13,
    half: int = 16000,
    small_half: int = 3500,
) -> dict:
    """Voynich, doğal diller, dönem ve tür metinleri ve üreteç sınıfları için kelime sırası bilgisi.

    Uzun metinler `half`, kısa olanlar (tür metinleri, Voynich bölümleri)
    `small_half` ile ölçülür; her boy için doğal dil tabanı ayrıca hesaplanır.
    Voynich için aile düzeyindeki değer de verilir.
    """
    from .generators import LANGUAGE_PROCESSES

    rng = np.random.default_rng(seed)
    out: dict = {"half": half, "small_half": small_half, "voynich": {}, "groups": {}, "small": {}}
    for view, lines in voynich.items():
        r = order_stats(lines, half, rng)
        if r is not None:
            fam = word_families([w for ln in lines for w in ln][: 2 * half])
            f = order_stats([[fam.get(w, w) for w in ln] for ln in lines], half, rng)
            r["family_order"] = f["order"]
            r["n_families"] = float(len(set(fam.values())))
        out["voynich"][view] = r
    need = 2 * half + 200
    out["groups"]["doğal dil, düz"] = {
        lang: order_stats(_chunk(corpora[lang][20000 : 20000 + need]), half, rng) for lang in sorted(corpora)
    }
    if period:
        out["groups"]["dönem ve tür metinleri"] = {
            name: order_stats(_chunk(words[500 : 500 + need]), half, rng) for name, words in period.items()
        }
    languages = sorted(corpora)
    for name in ("verbose", "codebook"):
        rows = {}
        for i in range(n_per_class):
            lang = languages[int(rng.integers(len(languages)))]
            start = int(rng.integers(0, len(corpora[lang]) - need - 2000))
            lines = LANGUAGE_PROCESSES[name](corpora[lang][start : start + need + 2000], rng)
            rows[f"{name} {i} ({lang})"] = order_stats(lines, half, rng, 1)
        out["groups"][name] = rows
    for name, proc in GIBBERISH_PROCESSES.items():
        out["groups"][name] = {
            f"{name} {i}": order_stats(proc(need + 2000, rng), half, rng, 1) for i in range(n_per_class)
        }
    # Küçük yarı boyu: kısa metinler ve Voynich bölümleri, aynı boyda dil tabanıyla.
    need_s = 2 * small_half + 200
    small: dict = {"voynich": {}, "texts": {}}
    for view, lines in voynich.items():
        small["voynich"][view] = order_stats(lines, small_half, rng)
    for name, lines in (sections or {}).items():
        small["voynich"][name] = order_stats(lines, small_half, rng)
    small["languages"] = {
        lang: order_stats(_chunk(corpora[lang][20000 : 20000 + need_s]), small_half, rng)
        for lang in sorted(corpora)
    }
    for name, words in (period or {}).items():
        small["texts"][name] = order_stats(_chunk(words[300 : 300 + need_s]), small_half, rng)
    out["small"] = small
    return out


def degradation_experiment(
    corpora: dict[str, list[str]],
    bands: dict[str, tuple[float, float]],
    seed: int = 17,
    half: int = 16000,
) -> dict:
    """Gerçek dil metni hangi bozulma altında üç ölçütte birden Voynich gibi görünür?

    bands: Voynich'in ölçülen aralıkları (küçük payla): type_ratio, order (üst
    sınır), ttr, hapax, ed1. Her dil, sesli ve seslisiz, yazım çeşitlemesi (üç
    düzey) ve eşsesli yazım (dört düzen) altında ölçülür. Üçünü birden
    tutturan düzenlerde aile düzeyinde sıra bilgisi de ölçülür.
    """
    from .corpus import ABJAD_CAPABLE_SCRIPTS, dominant_script, is_vowel
    from .manuscripts import growth_profile

    rng = np.random.default_rng(seed)
    configs = [("yazım çeşitlemesi", p, 0) for p in (0.3, 0.6, 0.9)]
    configs += [("eşsesli yazım", s, k) for s, k in ((0.3, 2), (0.6, 2), (1.0, 2), (0.6, 3))]
    rows = []
    for lang in sorted(corpora):
        plain_words = corpora[lang][20000 : 20000 + 2 * half + 400]
        variants = [(False, plain_words)]
        if dominant_script(plain_words) in ABJAD_CAPABLE_SCRIPTS:
            variants.append(
                (True, [("".join(c for c in w if not is_vowel(c)) or w[0]) for w in plain_words])
            )
        for bare, base in variants:
            for kind, level, k in configs:
                w = spelling_noise(base, level, rng) if k == 0 else homophonic(base, level, k, rng)
                o = order_stats(_chunk(w), half, rng, 1)
                lx = lexicon_stats(w, rng, half, orders=(2,))
                g = growth_profile(w[:half])
                row = {
                    "language": lang, "vowelless": bare, "kind": kind, "level": level, "k": k,
                    "order": o["order"], "type_ratio": lx["type_ratio_k2"],
                    "ttr": g[0], "hapax": g[1], "ed1": g[2],
                    "mean_len": float(np.mean([len(x) for x in w[:half]])),
                }  # fmt: skip
                row["fits_lexicon"] = bands["type_ratio"][0] <= row["type_ratio"] <= bands["type_ratio"][1]
                row["fits_order"] = row["order"] <= bands["order"][1]
                row["fits_growth"] = all(bands[m][0] <= row[m] <= bands[m][1] for m in ("ttr", "hapax", "ed1"))
                if row["fits_lexicon"] and row["fits_order"] and row["fits_growth"]:
                    fam = word_families(w[: 2 * half])
                    f = order_stats(_chunk([fam.get(x, x) for x in w]), half, rng, 1)
                    row["family_order"] = f["order"]
                rows.append(row)
    return {"bands": {k: list(v) for k, v in bands.items()}, "rows": rows}


def render_order(result: dict) -> str:
    md = [
        "# Sınama: kelimelerin sırası bilgi taşıyor mu",
        "",
        f"Her metnin ilk {result['half']} kelimesinden kelime ikilisi modeli öğrenildi; görülmemiş sonraki "
        f"{result['half']} kelimede, tek kelime sıklığı modeline göre kelime başına kaç bit kazandırdığı "
        "ölçüldü. Aynı ölçüm her satırın kelimeleri kendi içinde karıştırılarak tekrarlandı. \"Sıra\" "
        "sütunu ikisinin farkıdır: sıranın, birlikte geçmenin ötesinde taşıdığı bilgi (bit/kelime). "
        "Bire bir kelime kodlaması kaynak dille aynı değeri verir.",
        "",
        "| metin | n | sıra (bit/kelime) | gerçek kazanç | karıştırılmış kazanç |",
        "|---|---|---|---|---|",
    ]
    for view, r in result["voynich"].items():
        if r is None:
            continue
        md.append(
            f"| Voynich {view} (aile düzeyinde: {r['family_order']:+.3f}) | 1 | {r['order']:+.3f} | "
            f"{r['real']:+.3f} | {r['shuffled']:+.3f} |"
        )
    for group, rows in result["groups"].items():
        vals = [r for r in rows.values() if r is not None]
        if not vals:
            continue
        cells = []
        for c in ("order", "real", "shuffled"):
            x = np.array([r[c] for r in vals])
            cells.append(f"{np.median(x):+.3f} [{x.min():+.3f}, {x.max():+.3f}]")
        md.append(f"| {group} (medyan [en az, en çok]) | {len(vals)} | " + " | ".join(cells) + " |")
    period = result["groups"].get("dönem ve tür metinleri", {})
    for name, r in period.items():
        if r is not None:
            md.append(f"| {name} | 1 | {r['order']:+.3f} | {r['real']:+.3f} | {r['shuffled']:+.3f} |")
    small = result["small"]
    md += [
        "",
        f"## Kısa metinler ve Voynich bölümleri (yarı boyu {result['small_half']} kelime)",
        "",
        "| metin | sıra (bit/kelime) |",
        "|---|---|",
    ]
    for name, r in small["voynich"].items():
        md.append(f"| Voynich {name} | " + ("metin kısa" if r is None else f"{r['order']:+.3f}") + " |")
    x = np.array([r["order"] for r in small["languages"].values() if r is not None])
    md.append(f"| doğal dil, düz, {len(x)} dil (medyan [en az, en çok]) | {np.median(x):+.3f} [{x.min():+.3f}, {x.max():+.3f}] |")
    for name, r in small["texts"].items():
        md.append(f"| {name} | " + ("metin kısa" if r is None else f"{r['order']:+.3f}") + " |")
    return "\n".join(md) + "\n"


def render_degradation(result: dict) -> str:
    rows = result["rows"]
    b = result["bands"]

    def count(*keys: str) -> int:
        return sum(all(r[k] for k in keys) for r in rows)

    all3 = [r for r in rows if r["fits_lexicon"] and r["fits_order"] and r["fits_growth"]]
    md = [
        "# Tarama: gerçek dil hangi bozulma altında Voynich gibi görünür",
        "",
        f"{len(rows)} düzen: her dil, sesli ve seslisiz; yazım çeşitlemesi (kelimelerin 0.3, 0.6, 0.9'u bir "
        "harf farklı yazılır) ve eşsesli yazım (harflerin bir bölümünün 2 ya da 3 ayrı yazılışı vardır). "
        f"Voynich bantları: tür oranı {b['type_ratio'][0]:.2f} ila {b['type_ratio'][1]:.2f}; sıra en çok "
        f"{b['order'][1]:.3f}; tür/kelime {b['ttr'][0]:.2f} ila {b['ttr'][1]:.2f}; hapax {b['hapax'][0]:.2f} ila "
        f"{b['hapax'][1]:.2f}; ed1 {b['ed1'][0]:.2f} ila {b['ed1'][1]:.2f}.",
        "",
        "| ölçüt | uyan düzen |",
        "|---|---|",
        f"| sözlük | {count('fits_lexicon')} |",
        f"| sıra | {count('fits_order')} |",
        f"| büyüme | {count('fits_growth')} |",
        f"| sözlük ve sıra | {count('fits_lexicon', 'fits_order')} |",
        f"| sözlük ve büyüme | {count('fits_lexicon', 'fits_growth')} |",
        f"| sıra ve büyüme | {count('fits_order', 'fits_growth')} |",
        f"| üçü birden | {len(all3)} |",
    ]
    if all3:
        md += [
            "",
            "## Üç ölçütü birden tutturan düzenler",
            "",
            "| dil | seslisiz | bozulma | düzey | tür oranı | sıra | aile düzeyinde sıra | tür/kelime | hapax | ed1 | ort. kelime uzunluğu |",
            "|---|---|---|---|---|---|---|---|---|---|---|",
        ]
        for r in sorted(all3, key=lambda r: (r["language"], r["level"])):
            level = f"{r['level']}" + (f" x{r['k']}" if r["k"] else "")
            md.append(
                f"| {r['language']} | {'evet' if r['vowelless'] else 'hayır'} | {r['kind']} | {level} | "
                f"{r['type_ratio']:.2f} | {r['order']:+.3f} | {r['family_order']:+.3f} | {r['ttr']:.2f} | "
                f"{r['hapax']:.2f} | {r['ed1']:.2f} | {r['mean_len']:.1f} |"
            )
    return "\n".join(md) + "\n"


def render_lexicon(result: dict) -> str:
    cols = ["type_ratio_k1", "type_ratio_k2", "new_ratio_k1", "new_ratio_k2"]
    md = [
        "# Sınama: kelimeler bir sözlükten mi geliyor",
        "",
        f"Her metnin ilk {result['half']} kelimesinden kelime içi glif zinciri öğrenildi (k = 1 ve 2) "
        "ve aynı sayıda kelime bağımsız çekildi (vekil). Tür oranı: vekildeki farklı kelime sayısı / "
        "gerçek metindeki. Yeni kelime oranı: vekilde, ilk yarıda görülmemiş kelimelerin payı / gerçek "
        "ikinci yarıda aynı pay. İkisi de 1'e yakınsa metin, harf dizilişi kurallarının izin verdiği "
        "her kelimeyi kullanıyor demektir (sözlük kısıtı görünmüyor); 1'in belirgin üstündeyse "
        "kelimeler bu kuralların izin verdiğinden çok daha dar bir kümeden geliyor demektir.",
        "",
        "| metin | n | ort. kelime uzunluğu | tür oranı k=1 | tür oranı k=2 | yeni kelime oranı k=1 | yeni kelime oranı k=2 |",
        "|---|---|---|---|---|---|---|",
    ]
    for view, r in result["voynich"].items():
        if r is None:  # bu boy için kısa; bölüm tablosunda küçük boyla ölçülür
            continue
        md.append(
            f"| Voynich {view} | 1 | {r['mean_len']:.1f} | "
            + " | ".join(f"{r[c]:.2f}" for c in cols) + " |"
        )
    for group, rows in result["groups"].items():
        vals = [r for r in rows.values() if r is not None]
        if not vals:
            continue
        cells = []
        for c in cols:
            x = np.array([r[c] for r in vals])
            cells.append(f"{np.median(x):.2f} [{x.min():.2f}, {x.max():.2f}]")
        md.append(
            f"| {group} (medyan [en az, en çok]) | {len(vals)} | "
            f"{np.median([r['mean_len'] for r in vals]):.1f} | " + " | ".join(cells) + " |"
        )
    if result.get("sections"):
        md += [
            "",
            f"## Voynich bölüm bölüm (yarı boyu {result['section_half']} kelime)",
            "",
            "Bölümler kısa olduğu için daha küçük yarı boyuyla ölçüldü; doğal dil tabanı aynı boyda "
            "yeniden hesaplandı. Yeterince uzun olmayan bölümler ölçülemedi.",
            "",
            "| metin | ort. kelime uzunluğu | tür oranı k=1 | tür oranı k=2 | yeni kelime oranı k=1 | yeni kelime oranı k=2 |",
            "|---|---|---|---|---|---|",
        ]
        for name, r in result["sections"].items():
            if r is None:
                md.append(f"| Voynich {name} | metin kısa | | | | |")
            else:
                md.append(
                    f"| Voynich {name} | {r['mean_len']:.1f} | " + " | ".join(f"{r[c]:.2f}" for c in cols) + " |"
                )
        vals = [r for r in result["section_reference"].values() if r is not None]
        cells = []
        for c in cols:
            x = np.array([r[c] for r in vals])
            cells.append(f"{np.median(x):.2f} [{x.min():.2f}, {x.max():.2f}]")
        md.append(
            f"| doğal dil, düz, {len(vals)} dil (medyan [en az, en çok]) | "
            f"{np.median([r['mean_len'] for r in vals]):.1f} | " + " | ".join(cells) + " |"
        )
    return "\n".join(md) + "\n"


def render_markdown(result: dict) -> str:
    cls = result["classes"]
    md = [
        "# Sınama: EVA'laştırma sınıflandırıcının kararını değiştiriyor mu",
        "",
        f"Her süreçten {result['n']} anlamsız metin örneği üretildi. Her örnek iki kez "
        "sınıflandırıldı: özgün hâliyle ve altı glifi EVA'daki gibi çok harfli diziye "
        "açılmış hâliyle. Tablo oy sayısını verir.",
        "",
        "| süreç | yazım | " + " | ".join(cls) + " |",
        "|---|---|" + "---|" * len(cls),
    ]
    for name, res in result["processes"].items():
        for tag, label in (("original", "özgün"), ("evaized", "EVA'laştırılmış")):
            md.append(
                f"| {name} | {label} | " + " | ".join(str(res[tag]["votes"][c]) for c in cls) + " |"
            )
    return "\n".join(md) + "\n"
