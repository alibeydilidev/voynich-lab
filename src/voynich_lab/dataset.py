"""Sentetik korpus fabrikası: (dil penceresi x süreç) -> feature satırı."""

from __future__ import annotations

import numpy as np
import pandas as pd

from . import Lines
from .corpus import ABJAD_CAPABLE_SCRIPTS, dominant_script
from .features import extract_features
from .generators import GIBBERISH_PROCESSES, LANGUAGE_PROCESSES

META_COLUMNS = ["label", "group", "source"]


def _truncate(lines: Lines, n_words: int) -> Lines:
    """Pencereyi tam n_words kelimeye keser (feature'lar boyuta duyarlı)."""
    out, total = [], 0
    for ln in lines:
        if total + len(ln) >= n_words:
            out.append(ln[: n_words - total])
            break
        out.append(ln)
        total += len(ln)
    return [ln for ln in out if ln]


def _window_starts(n_total: int, window: int, count: int) -> list[int]:
    """Metne eşit aralıkla yayılmış, örtüşmeyen pencere başlangıçları."""
    count = min(count, n_total // window)
    return [int(x) for x in np.linspace(0, n_total - window, count)]


def build_dataset(
    corpora: dict[str, list[str]],
    window_words: int = 2000,
    windows_per_language: int = 24,
    seed: int = 7,
) -> pd.DataFrame:
    """Etiketli feature tablosu üretir.

    group sütunu çapraz doğrulama içindir: dil tabanlı örneklerde dil adı,
    anlamsız üreteçlerde yapay aile numarası. Böylece model hiç görmediği bir
    dilde sınanır, "Latinceyi ezberledi" sonucu çıkmaz.
    """
    rng = np.random.default_rng(seed)
    rows: list[dict] = []

    for lang, words in corpora.items():
        can_abjad = dominant_script(words) in ABJAD_CAPABLE_SCRIPTS
        for start in _window_starts(len(words), window_words * 2, windows_per_language):
            # Verbose şifre kelime bölebildiği için iki katı ham metin ayrılır,
            # çıktı sonra window_words'e kesilir.
            base = words[start : start + window_words * 2]
            for name, proc in LANGUAGE_PROCESSES.items():
                if name == "abjad" and not can_abjad:
                    continue
                src = base if name == "verbose" else base[:window_words]
                lines = _truncate(proc(src, rng), window_words)
                rows.append(
                    extract_features(lines) | {"label": name, "group": lang, "source": lang}
                )

    for name, proc in GIBBERISH_PROCESSES.items():
        for family in range(len(corpora)):
            for _ in range(windows_per_language):
                lines = _truncate(proc(window_words + 50, rng), window_words)
                rows.append(
                    extract_features(lines)
                    | {"label": name, "group": f"{name}_{family}", "source": "synthetic"}
                )

    return pd.DataFrame(rows)
