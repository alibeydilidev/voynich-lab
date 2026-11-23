"""ABC (approximate Bayesian computation): her hipotez Voynich'e en fazla ne kadar yaklaşabiliyor?

Sınıflandırıcı "hangisi daha olası" der ama hepsi kötüyse de birini seçer. Bu
adım soruyu ters çevirir: her süreç için çok sayıda örnek üret, Voynich'e en
yakın küçük dilimi kabul et (rejection ABC), sonra üç şeye bak:

  1. Kabul edilen örnekler Voynich'e ne kadar yakın?
  2. Hangi feature'ları hâlâ tutturamıyorlar?
  3. Hangi ayarlarla yaklaştılar (önsele göre nereye kaydılar)?

Mesafe birimi Voynich'in kendi iç değişkenliğidir: her feature, Voynich
pencereleri arasındaki standart sapmaya bölünür. Böylece "mesafe 1" kabaca
"bir Voynich penceresinin öbür pencerelere benzediği kadar benziyor" demektir.
Asıl ölçüt, aynı birimle hesaplanan Voynich öz mesafesidir (her pencerenin,
kalan pencerelerin ortalamasına uzaklığı). Bir hipotezin kabul edilen örnekleri
bu aralığa giriyorsa, o hipotez bu feature kümesinde Voynich'ten ayırt edilemez.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .features import FEATURE_NAMES, extract_features
from .transliteration import FolioLine, to_windows

# Voynich'te neredeyse sabit olan bir feature mesafeyi tek başına ele geçirmesin:
# ölçek, sentetik evrendeki yayılımın bu oranından küçük olamaz.
SCALE_FLOOR = 0.05


def voynich_features(lines: list[FolioLine], window_words: int) -> pd.DataFrame:
    wins = to_windows(lines, window_words)
    return pd.DataFrame([extract_features(w) for _, w in wins])[FEATURE_NAMES]


def _rms(z: np.ndarray) -> np.ndarray:
    return np.sqrt((z**2).mean(axis=-1))


def analyze_view(
    df: pd.DataFrame, voy: pd.DataFrame, accept: float = 0.01, min_accept: int = 30
) -> dict:
    """Bir görünüm için sınıf başına ABC özeti.

    df : sentetik tablo (feature'lar, `label`, `p_*` ve `l_*` parametre sütunları)
    voy: Voynich pencere feature'ları
    """
    V = voy[FEATURE_NAMES].to_numpy(dtype=float)
    center = V.mean(0)
    universe_sd = df[FEATURE_NAMES].to_numpy(dtype=float).std(0)
    scale = np.maximum(V.std(0, ddof=1), SCALE_FLOOR * universe_sd) + 1e-12

    # Öz mesafe: her pencere, kendisi hariç pencerelerin ortalamasına ne kadar uzak.
    n = len(V)
    loo_center = (center * n - V) / (n - 1)
    self_d = _rms((V - loo_center) / scale)

    param_cols = [c for c in df.columns if c.startswith(("p_", "l_"))]
    classes = {}
    for label, g in df.groupby("label"):
        X = g[FEATURE_NAMES].to_numpy(dtype=float)
        Z = (X - center) / scale
        d = _rms(Z)
        k = min(len(g), max(min_accept, int(round(accept * len(g)))))
        idx = np.argsort(d)[:k]
        acc_z = np.median(Z[idx], axis=0)
        order = np.argsort(-np.abs(acc_z))
        shifts = []
        for col in param_cols:
            prior = g[col].to_numpy(dtype=float)
            post = prior[idx]
            prior, post = prior[~np.isnan(prior)], post[~np.isnan(post)]
            if len(prior) < 50 or len(post) < 10 or prior.std() == 0:
                continue
            # Kabul edilenlerin medyanı önsel dağılımın hangi yüzdeliğinde.
            q = float((prior < np.median(post)).mean() + 0.5 * (prior == np.median(post)).mean())
            shifts.append(
                {
                    "param": col,
                    "prior_median": float(np.median(prior)),
                    "accepted_median": float(np.median(post)),
                    "accepted_iqr": [float(np.percentile(post, 25)), float(np.percentile(post, 75))],
                    "quantile_in_prior": q,
                }
            )
        shifts.sort(key=lambda r: -abs(r["quantile_in_prior"] - 0.5))
        classes[label] = {
            "n_samples": int(len(g)),
            "n_accepted": int(k),
            "best_distance": float(d[idx[0]]),
            "accepted_median_distance": float(np.median(d[idx])),
            "accepted_max_distance": float(d[idx[-1]]),
            "share_within_self_max": float((d <= self_d.max()).mean()),
            "share_within_self_median": float((d <= np.median(self_d)).mean()),
            "misfit": [
                {
                    "feature": FEATURE_NAMES[j],
                    "z": float(acc_z[j]),
                    "voynich": float(center[j]),
                    "accepted_median": float(np.median(X[idx, j])),
                }
                for j in order[:8]
            ],
            "n_features_off_by_2": int((np.abs(acc_z) > 2).sum()),
            "param_shifts": shifts,
        }
    return {
        "n_windows": int(n),
        "self_distance": {
            "median": float(np.median(self_d)),
            "max": float(self_d.max()),
        },
        "classes": classes,
    }


def render_markdown(views: dict[str, dict], n_total: int, accept: float) -> str:
    labels = sorted(next(iter(views.values()))["classes"])
    md = ["# ABC raporu: her hipotez Voynich'e ne kadar yaklaşabiliyor", ""]
    md += [
        f"Sentetik örnek: {n_total}. Her sınıfta Voynich'e en yakın %{100 * accept:g} kabul edildi.",
        "",
        "Mesafe birimi Voynich'in kendi pencereleri arasındaki değişkenliktir. "
        "\"Voynich öz mesafesi\" bir Voynich penceresinin diğerlerinin ortalamasına "
        "uzaklığıdır; bir hipotezin mesafesi bu aralığa girmiyorsa o hipotez "
        "Voynich'i (bu feature kümesinde) üretemiyor demektir.",
        "",
        "## 1. Kabul edilen örneklerin medyan mesafesi",
        "",
        "| görünüm | Voynich öz mesafesi (medyan, en çok) | " + " | ".join(labels) + " |",
        "|---|---|" + "---|" * len(labels),
    ]
    for name, v in views.items():
        s = v["self_distance"]
        md.append(
            f"| {name} | {s['median']:.2f}, {s['max']:.2f} | "
            + " | ".join(f"{v['classes'][c]['accepted_median_distance']:.2f}" for c in labels)
            + " |"
        )
    md += ["", "## 2. En iyi tek örneğin mesafesi", ""]
    md += ["| görünüm | " + " | ".join(labels) + " |", "|---|" + "---|" * len(labels)]
    for name, v in views.items():
        md.append(
            f"| {name} | "
            + " | ".join(f"{v['classes'][c]['best_distance']:.2f}" for c in labels)
            + " |"
        )
    md += ["", "## 3. Voynich'in en uç penceresi kadar yakın olan örneklerin oranı", ""]
    md += ["| görünüm | " + " | ".join(labels) + " |", "|---|" + "---|" * len(labels)]
    for name, v in views.items():
        md.append(
            f"| {name} | "
            + " | ".join(f"%{100 * v['classes'][c]['share_within_self_max']:.2f}" for c in labels)
            + " |"
        )
    for name, v in views.items():
        md += ["", f"## {name}: sınıf sınıf", ""]
        ranked = sorted(labels, key=lambda c: v["classes"][c]["accepted_median_distance"])
        for c in ranked:
            r = v["classes"][c]
            md += [
                f"### {c}: medyan mesafe {r['accepted_median_distance']:.2f} "
                f"({r['n_accepted']} / {r['n_samples']} örnek kabul)",
                "",
                f"Voynich'ten 2 birimden fazla sapan feature sayısı: {r['n_features_off_by_2']}",
                "",
                "| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |",
                "|---|---|---|---|",
            ]
            for m in r["misfit"][:6]:
                md.append(
                    f"| {m['feature']} | {m['z']:+.1f} | {m['voynich']:.3f} | {m['accepted_median']:.3f} |"
                )
            moved = [s for s in r["param_shifts"] if abs(s["quantile_in_prior"] - 0.5) >= 0.25]
            if moved:
                md += [
                    "",
                    "| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |",
                    "|---|---|---|---|",
                ]
                for s in moved[:8]:
                    lo, hi = s["accepted_iqr"]
                    md.append(
                        f"| {s['param']} | {s['prior_median']:.3g} | "
                        f"{s['accepted_median']:.3g} [{lo:.3g}, {hi:.3g}] | "
                        f"{100 * s['quantile_in_prior']:.0f} |"
                    )
            md.append("")
    return "\n".join(md).rstrip() + "\n"
