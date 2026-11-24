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
"""

from __future__ import annotations

from collections import Counter, defaultdict

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
    n_per_class: int = 6,
    seed: int = 11,
    half: int = 16000,
) -> dict:
    """Voynich, doğal diller (düz ve seslisiz) ve üreteç sınıfları için sözlük ölçüleri."""
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
