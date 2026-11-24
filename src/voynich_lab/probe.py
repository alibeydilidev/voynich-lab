"""Ön sınama: yeni bir mekanizma zincire girmeden önce saniyeler içinde ölçülür.

2026-11-24'te dört hipotez üreteç sınıfı olarak yazıldı, her biri tam zincirle
(yaklaşık 30 dakika) sınandı ve dördü de tutmadı. Dördünde de sonucu tek bir
büyüme ölçüsü belirledi; o ölçü tek bir el yazmasında görülebilirdi. Bu modül
o bekçidir.

Kural: ön sınamada büyüme bandına hiçbir el yazması girmiyorsa mekanizma için
sınıf yazılmaz ve zincir koşulmaz. Giriyorsa, pencere feature'larının Voynich'e
göre nerede durduğuna bakılır ve öngörü ön sınama sonucuyla birlikte yazılır.

Ön sınama bir eleme aracıdır, hüküm aracı değildir: geçmek "hipotez tutuyor"
demek değil, "tam sınamaya değer" demektir. Hüküm `cli manuscripts`'ten verilir.
"""

from __future__ import annotations

from typing import Callable

import numpy as np
import pandas as pd

from . import Lines
from .features import extract_features
from .manuscripts import GROWTH_NAMES, GROWTH_TOLERANCE, growth_profile, windows
from .transliteration import FolioLine

# Pencere düzeyinde bakılan ölçüler: şimdiye kadarki hipotezleri en çok ayıranlar.
PROBE_FEATURES = [
    "h2",
    "wlen_mean",
    "wlen_std",
    "jsd_last",
    "wlen_autocorr1",
    "rep_adjacent_ed1",
    "hapax_ratio",
    "vocab_ed1_density",
    "edge_mi",
]


def profile(lines: Lines, window_words: int = 2000, n_windows: int = 8) -> dict[str, float] | None:
    """Bir metnin ön sınama profili: büyüme ölçüleri ve pencere ortalamaları.

    Metin n_windows pencereden kısaysa None döner.
    """
    wins = windows(lines, window_words)[:n_windows]
    if len(wins) < n_windows:
        return None
    words = [w for win in wins for ln in win for w in ln][: n_windows * window_words]
    out = dict(zip(GROWTH_NAMES, growth_profile(words)))
    feats = [extract_features(w) for w in wins]
    for name in PROBE_FEATURES:
        out[name] = float(np.mean([f[name] for f in feats]))
    return out


def voynich_target(
    lines: list[FolioLine], window_words: int = 2000, n_windows: int = 8
) -> dict[str, float]:
    """Voynich'in aynı ölçülerdeki değeri: ardışık iki yarının ortalaması."""
    rows = [[ln.words for ln in lines]]
    halves = []
    all_windows = windows(rows[0], window_words)
    for part in (all_windows[:n_windows], all_windows[n_windows : 2 * n_windows]):
        if len(part) == n_windows:
            halves.append(profile([ln for win in part for ln in win], window_words, n_windows))
    keys = halves[0].keys()
    return {k: float(np.mean([h[k] for h in halves])) for k in keys}


def run(
    make: Callable[[np.random.Generator], Lines],
    n: int = 12,
    seed: int = 7,
    window_words: int = 2000,
    n_windows: int = 8,
) -> pd.DataFrame:
    """`make(rng)` ile n el yazması üretir, her birinin profilini döndürür.

    make, en az (n_windows + 1) * window_words kelimelik metin üretmelidir.
    """
    rows = []
    for i in range(n):
        p = profile(make(np.random.default_rng([seed, 4242, i])), window_words, n_windows)
        if p is not None:
            rows.append(p)
    return pd.DataFrame(rows)


def summarize(df: pd.DataFrame, targets: dict[str, dict[str, float]]) -> dict:
    """Görünüm başına: büyüme bandına giren el yazması sayısı ve ölçülerin medyanı."""
    out = {"n": int(len(df)), "median": {k: float(df[k].median()) for k in df.columns}, "views": {}}
    for view, t in targets.items():
        fits = np.ones(len(df), dtype=bool)
        for g in GROWTH_NAMES:
            fits &= (df[g] - t[g]).abs().to_numpy() <= GROWTH_TOLERANCE
        out["views"][view] = {"n_fitting_growth": int(fits.sum()), "target": t}
    out["passes"] = any(v["n_fitting_growth"] > 0 for v in out["views"].values())
    return out


def render(summary: dict) -> str:
    cols = list(summary["median"])
    lines = [
        f"El yazması: {summary['n']}. Büyüme bandı: üç ölçünün her birinde Voynich'ten fark en çok {GROWTH_TOLERANCE}.",
        "",
        "| | " + " | ".join(cols) + " | büyümeye uyan |",
        "|---|" + "---|" * (len(cols) + 1),
        "| aday (medyan) | " + " | ".join(f"{summary['median'][c]:.3f}" for c in cols) + " | |",
    ]
    for view, v in summary["views"].items():
        lines.append(
            f"| Voynich {view} | " + " | ".join(f"{v['target'][c]:.3f}" for c in cols)
            + f" | {v['n_fitting_growth']} / {summary['n']} |"
        )
    lines += [
        "",
        "Sonuç: "
        + (
            "büyüme bandına giren el yazması var; tam sınamaya değer."
            if summary["passes"]
            else "büyüme bandına giren el yazması yok; bu haliyle zincir koşulmaz."
        ),
    ]
    return "\n".join(lines) + "\n"
