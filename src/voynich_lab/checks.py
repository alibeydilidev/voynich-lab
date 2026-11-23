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
"""

from __future__ import annotations

from collections import Counter

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
                books[name].append(
                    np.array([[extract_features(w)[f] for f in FEATURE_NAMES] for w in wins])
                )

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
