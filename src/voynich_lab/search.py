"""Yönlendirilmiş arama: her hipotez, önselinin içinde Voynich'e en fazla ne kadar yaklaşabilir?

Rejection ABC (abc.py) ayarları rastgele dener; 32 feature'ı aynı anda tutturan
örnek seyrek olduğu için hipotezleri olduğundan kötü gösterir. Bu adım aramayı
yönlendirir:

  1. Başlangıç nüfusu: ABC tablosunda o sınıfın Voynich'e en yakın örneklerinin ayarları.
  2. Her turda nüfustaki ayarlar biraz oynatılır (önsel sınırları içinde), her
     yeni ayarla bir örnek üretilir, en yakınları yeni nüfus olur.
  3. Son nüfusun her ayarıyla TAZE örnekler üretilir; rapor edilen mesafe budur.

Üçüncü adım şart: turlar boyunca "şanslı çıkan" örnekler seçildiği için tur içi
mesafeler iyimserdir. Bir ayarın gerçekten iyi olup olmadığı, aynı ayarla
yeniden üretilen örneğin de yakın çıkmasıyla anlaşılır.

Bu, ağırlıklı ABC-SMC değildir, sonsal dağılım vermez. Yanıtladığı soru daha
dar: "bu hipotezin önseli içinde Voynich'ten ayırt edilemeyen örnek üreten bir
ayar bölgesi var mı?" Ölçüt abc.py ile aynıdır (Voynich öz mesafesi).
"""

from __future__ import annotations

from functools import lru_cache
from math import isnan
from pathlib import Path

import numpy as np
import pandas as pd

from .dataset import _truncate
from .features import FEATURE_NAMES, extract_features
from .generators import (
    GIBBERISH_PROCESSES,
    LANGUAGE_PROCESSES,
    LAYOUT_PRIOR,
    PROCESS_PRIOR,
    layout_from_params,
)

LANGUAGE_KEY = "language"


def prior_for(label: str) -> dict[str, tuple[float, float, str]]:
    return LAYOUT_PRIOR | PROCESS_PRIOR[label]


def _num(value) -> float:
    return 0.0 if value is None or (isinstance(value, float) and isnan(value)) else float(value)


def perturb(
    theta: dict,
    spread: dict[str, float],
    prior: dict[str, tuple[float, float, str]],
    languages: list[str],
    rng: np.random.Generator,
) -> dict:
    """Bir ayar kümesini önsel sınırları içinde biraz oynatır.

    spread: ayar başına adım büyüklüğü (nüfustaki yayılımdan gelir).
    """
    out = dict(theta)
    for name, (lo, hi, kind) in prior.items():
        v = _num(theta.get(name))
        step = spread.get(name, 0.0)
        if kind == "b":
            out[name] = float(1 - v) if rng.random() < 0.1 else float(v)
        elif kind == "f":
            out[name] = float(np.clip(v + rng.normal(0, max(step, 0.02 * (hi - lo))), lo, hi))
        elif kind == "i":
            out[name] = float(np.clip(round(v + rng.normal(0, max(step, 0.5))), lo, hi))
        elif kind == "log":
            x = np.log(max(v, lo)) + rng.normal(0, max(step, 0.05))
            out[name] = float(np.clip(round(np.exp(x)), lo, hi))
        else:  # "m": 0 (kapalı) ya da [lo, hi]
            if rng.random() < 0.05:  # aç ya da kapat
                v = float(rng.uniform(lo, hi)) if v <= 0 else 0.0
            elif v > 0:
                v = v + rng.normal(0, max(step, 0.02 * (hi - lo)))
            out[name] = 0.0 if v < lo / 2 else float(np.clip(v, lo, hi))
    if languages and (LANGUAGE_KEY not in out or rng.random() < 0.15):
        out[LANGUAGE_KEY] = str(rng.choice(languages))
    return out


def _spread(pop: list[dict], prior: dict[str, tuple[float, float, str]], factor: float = 0.5) -> dict:
    out = {}
    for name, (lo, _, kind) in prior.items():
        vals = np.array([_num(t.get(name)) for t in pop])
        if kind == "log":
            vals = np.log(np.maximum(vals, lo))
        elif kind == "m":
            vals = vals[vals > 0]
        out[name] = factor * float(vals.std()) if len(vals) > 1 else 0.0
    return out


@lru_cache(maxsize=1)
def _corpora(raw: str) -> dict[str, list[str]]:
    from .corpus import load_all

    return load_all(Path(raw) / "bible")


def simulate(
    label: str, theta: dict, raw: str, window_words: int, rng: np.random.Generator
) -> np.ndarray:
    """Verilen ayarlarla tek bir örnek üretir, feature vektörünü döndürür."""
    layout = layout_from_params(theta, rng)
    if label in LANGUAGE_PROCESSES:
        words = _corpora(raw)[theta[LANGUAGE_KEY]]
        start = int(rng.integers(0, len(words) - 2 * window_words))
        base = words[start : start + 2 * window_words]
        src = base if label == "verbose" else base[:window_words]
        lines = LANGUAGE_PROCESSES[label](src, rng, layout=layout, fixed=theta)
    else:
        lines = GIBBERISH_PROCESSES[label](window_words + 50, rng, layout=layout, fixed=theta)
    f = extract_features(_truncate(lines, window_words))
    return np.array([f[n] for n in FEATURE_NAMES], dtype=float)


def distance(x: np.ndarray, center: np.ndarray, scale: np.ndarray) -> float:
    return float(np.sqrt((((x - center) / scale) ** 2).mean()))


def initial_population(df: pd.DataFrame, label: str, center, scale, keep: int) -> list[dict]:
    """ABC tablosundan o sınıfın Voynich'e en yakın `keep` örneğinin ayarları."""
    g = df[df["label"] == label]
    X = g[FEATURE_NAMES].to_numpy(dtype=float)
    d = np.sqrt((((X - center) / scale) ** 2).mean(1))
    prior = prior_for(label)
    pop = []
    for i in np.argsort(d)[:keep]:
        row = g.iloc[int(i)]
        theta = {name: _num(row.get(name)) for name in prior}
        if label in LANGUAGE_PROCESSES:
            theta[LANGUAGE_KEY] = str(row["group"])
        pop.append(theta)
    return pop


def run_search(job: dict) -> dict:
    """Tek bir (sınıf, görünüm) için arama. Ayrı süreçte çalışacak şekilde yazıldı."""
    label, raw, window = job["label"], job["raw"], job["window"]
    center, scale = np.array(job["center"]), np.array(job["scale"])
    keep, children, rounds, fresh = job["keep"], job["children"], job["rounds"], job["fresh"]
    rng = np.random.default_rng(job["seed"])
    prior = prior_for(label)
    languages = job["languages"]
    pop: list[dict] = job["init"]
    history = []
    for _ in range(rounds):
        spread = _spread(pop, prior)
        proposals = [
            perturb(pop[int(rng.integers(len(pop)))], spread, prior, languages, rng)
            for _ in range(keep * children)
        ]
        d = np.array([distance(simulate(label, t, raw, window, rng), center, scale) for t in proposals])
        order = np.argsort(d)[:keep]
        pop = [proposals[int(i)] for i in order]
        history.append(float(np.median(d[order])))

    # Taze örnekler: seçilmiş ayarlar yeniden üretildiğinde de yakın mı?
    X = np.array([simulate(label, t, raw, window, rng) for t in pop for _ in range(fresh)])
    Z = (X - center) / scale
    d = np.sqrt((Z**2).mean(1))
    z_med = np.median(Z, axis=0)
    order = np.argsort(-np.abs(z_med))
    params = {}
    for name in prior:
        vals = np.array([_num(t.get(name)) for t in pop])
        params[name] = {
            "median": float(np.median(vals)),
            "iqr": [float(np.percentile(vals, 25)), float(np.percentile(vals, 75))],
            "prior": [float(prior[name][0]), float(prior[name][1])],
        }
    if languages:
        counts = pd.Series([t[LANGUAGE_KEY] for t in pop]).value_counts()
        params[LANGUAGE_KEY] = {str(k): int(v) for k, v in counts.head(5).items()}
    return {
        "label": label,
        "view": job["view"],
        "round_medians": history,
        "fresh_median_distance": float(np.median(d)),
        "fresh_best_distance": float(d.min()),
        "fresh_share_within_self_max": float((d <= job["self_max"]).mean()),
        "n_fresh": int(len(d)),
        "n_features_off_by_2": int((np.abs(z_med) > 2).sum()),
        "misfit": [
            {
                "feature": FEATURE_NAMES[j],
                "z": float(z_med[j]),
                "voynich": float(center[j]),
                "fresh_median": float(np.median(X[:, j])),
            }
            for j in order[:8]
        ],
        "params": params,
    }


def render_markdown(views: dict[str, dict], settings: dict) -> str:
    labels = sorted(next(iter(views.values()))["classes"])
    md = ["# Yönlendirilmiş arama raporu: her hipotezin ulaşabildiği en iyi nokta", ""]
    md += [
        f"Her (sınıf, görünüm) için {settings['rounds']} tur, tur başına "
        f"{settings['keep'] * settings['children']} deneme, en yakın {settings['keep']} ayar tutuldu. "
        f"Tablolardaki mesafeler, son turda kalan ayarların her biriyle yeniden üretilen "
        f"{settings['fresh']} taze örnekten hesaplandı (toplam {settings['keep'] * settings['fresh']}).",
        "",
        "Mesafe birimi ve ölçüt `abc.md` ile aynı: bir hipotezin taze örnekleri Voynich öz "
        "mesafesinin içine giriyorsa, o hipotez bu feature kümesinde Voynich'ten ayırt edilemez.",
        "",
        "## 1. Taze örneklerin medyan mesafesi (parantezde rejection ABC'deki değer)",
        "",
        "| görünüm | Voynich öz mesafesi (medyan, en çok) | " + " | ".join(labels) + " |",
        "|---|---|" + "---|" * len(labels),
    ]
    for name, v in views.items():
        s = v["self_distance"]
        cells = [
            f"{v['classes'][c]['fresh_median_distance']:.2f} ({v['classes'][c]['abc_median_distance']:.2f})"
            for c in labels
        ]
        md.append(f"| {name} | {s['median']:.2f}, {s['max']:.2f} | " + " | ".join(cells) + " |")
    md += ["", "## 2. Voynich'in en uç penceresi kadar yakın olan taze örneklerin oranı", ""]
    md += ["| görünüm | " + " | ".join(labels) + " |", "|---|" + "---|" * len(labels)]
    for name, v in views.items():
        md.append(
            f"| {name} | "
            + " | ".join(f"%{100 * v['classes'][c]['fresh_share_within_self_max']:.0f}" for c in labels)
            + " |"
        )
    md += ["", "## 3. Arama yakınsadı mı (tur tur, tutulan ayarların medyan mesafesi)", ""]
    md += ["| görünüm | sınıf | turlar |", "|---|---|---|"]
    for name, v in views.items():
        for c in labels:
            hist = " -> ".join(f"{x:.2f}" for x in v["classes"][c]["round_medians"])
            md.append(f"| {name} | {c} | {hist} |")
    for name, v in views.items():
        md += ["", f"## {name}: sınıf sınıf", ""]
        for c in sorted(labels, key=lambda c: v["classes"][c]["fresh_median_distance"]):
            r = v["classes"][c]
            md += [
                f"### {c}: taze medyan mesafe {r['fresh_median_distance']:.2f}, "
                f"en iyi {r['fresh_best_distance']:.2f}",
                "",
                f"Voynich'ten 2 birimden fazla sapan feature sayısı: {r['n_features_off_by_2']}",
                "",
                "| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |",
                "|---|---|---|---|",
            ]
            for m in r["misfit"][:6]:
                md.append(
                    f"| {m['feature']} | {m['z']:+.1f} | {m['voynich']:.3f} | {m['fresh_median']:.3f} |"
                )
            md += ["", "| ayar | bulunan medyan [çeyrekler] | önsel aralığı |", "|---|---|---|"]
            for pname, p in r["params"].items():
                if pname == LANGUAGE_KEY:
                    continue
                lo, hi = p["iqr"]
                md.append(
                    f"| {pname} | {p['median']:.3g} [{lo:.3g}, {hi:.3g}] | "
                    f"{p['prior'][0]:g} .. {p['prior'][1]:g} |"
                )
            if LANGUAGE_KEY in r["params"]:
                langs = ", ".join(f"{k} {n}" for k, n in r["params"][LANGUAGE_KEY].items())
                md += ["", f"Kaynak dil (son nüfusta en sık): {langs}"]
            md.append("")
    return "\n".join(md).rstrip() + "\n"
