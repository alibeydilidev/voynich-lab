"""Voynich pencerelerini eğitilmiş modele sokar ve üç soruyu yanıtlar:

  1. Hangi süreç sınıfına benziyor? (sınıf olasılıkları)
  2. Neden? (XGBoost'un kendi SHAP katkıları, pred_contribs)
  3. Bu soruyu sormaya hakkımız var mı? (dağılım dışı kontrolü)

Üçüncüsü kritik: sınıflandırıcı, hiçbir sınıfa benzemeyen bir girdiye de
yüksek olasılık verir. Voynich sentetik evrenin dışındaysa 1 ve 2 anlamsızdır.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.covariance import LedoitWolf

from .features import FEATURE_NAMES, extract_features
from .transliteration import FolioLine, to_windows


class OODReference:
    """Sınıf başına Mahalanobis mesafesi ve feature aralıkları."""

    def __init__(self, df: pd.DataFrame):
        X = df[FEATURE_NAMES].to_numpy(dtype=float)
        self.mean, self.std = X.mean(0), X.std(0) + 1e-9
        self.lo, self.hi = X.min(0), X.max(0)
        Z = (X - self.mean) / self.std
        self.classes: dict[str, tuple[np.ndarray, np.ndarray, np.ndarray]] = {}
        for label in sorted(df["label"].unique()):
            Zc = Z[(df["label"] == label).to_numpy()]
            lw = LedoitWolf().fit(Zc)
            own = self._dist(Zc, lw.location_, lw.precision_)
            self.classes[label] = (lw.location_, lw.precision_, np.sort(own))

    @staticmethod
    def _dist(Z: np.ndarray, mu: np.ndarray, prec: np.ndarray) -> np.ndarray:
        d = Z - mu
        return np.sqrt(np.einsum("ij,jk,ik->i", d, prec, d))

    def score(self, X: np.ndarray) -> list[dict]:
        """Her satır için: en yakın sınıf, mesafe, o sınıfın kendi
        örneklerine göre yüzdelik (100 = sınıfın bütün örneklerinden uzak)."""
        Z = (X - self.mean) / self.std
        out = []
        for i in range(len(Z)):
            best = None
            for label, (mu, prec, own) in self.classes.items():
                d = float(self._dist(Z[i : i + 1], mu, prec)[0])
                pct = 100.0 * float(np.searchsorted(own, d)) / len(own)
                if best is None or d / np.median(own) < best["ratio"]:
                    best = {
                        "nearest": label,
                        "distance": d,
                        "percentile": pct,
                        "ratio": d / float(np.median(own)),
                    }
            out.append(best)
        return out

    def out_of_range(self, X: np.ndarray) -> dict[str, float]:
        """Feature başına: sentetik evrenin [min, max] aralığı dışında kalan
        pencere oranı. Sıfırdan büyükse üreteçler o özelliği hiç üretemiyor."""
        outside = (X < self.lo) | (X > self.hi)
        frac = outside.mean(0)
        return {n: float(v) for n, v in zip(FEATURE_NAMES, frac) if v > 0}


def analyze_view(
    lines: list[FolioLine],
    model: xgb.XGBClassifier,
    classes: list[str],
    ood: OODReference,
    window_words: int,
    top_k: int = 6,
) -> dict:
    windows = to_windows(lines, window_words)
    feats = pd.DataFrame([extract_features(w) for _, w in windows])[FEATURE_NAMES]
    X = feats.to_numpy(dtype=float)

    proba = model.predict_proba(X)
    contribs = model.get_booster().predict(
        xgb.DMatrix(X, feature_names=None), pred_contribs=True
    )  # (pencere, sınıf, feature + bias)
    winner = int(np.argmax(proba.mean(0)))
    mean_contrib = contribs[:, winner, :-1].mean(0)
    order = np.argsort(-np.abs(mean_contrib))[:top_k]

    ood_rows = ood.score(X)
    z_vs_all = (X.mean(0) - ood.mean) / ood.std

    return {
        "n_windows": len(windows),
        "n_words": int(sum(len(w) for _, ws in windows for w in ws)),
        "mean_proba": {c: float(p) for c, p in zip(classes, proba.mean(0))},
        "window_votes": {
            c: int((proba.argmax(1) == i).sum()) for i, c in enumerate(classes)
        },
        "predicted": classes[winner],
        "top_contributions": [
            {
                "feature": FEATURE_NAMES[j],
                "contribution": float(mean_contrib[j]),
                "voynich_mean": float(X[:, j].mean()),
                "z_vs_synthetic": float(z_vs_all[j]),
            }
            for j in order
        ],
        "ood": {
            "median_percentile": float(np.median([r["percentile"] for r in ood_rows])),
            "median_ratio": float(np.median([r["ratio"] for r in ood_rows])),
            "nearest_by_distance": pd.Series([r["nearest"] for r in ood_rows])
            .value_counts()
            .to_dict(),
            "features_out_of_range": ood.out_of_range(X),
        },
        "feature_means": {n: float(v) for n, v in zip(FEATURE_NAMES, X.mean(0))},
        "windows": [
            {"folios": label, "proba": {c: float(p) for c, p in zip(classes, row)}}
            for (label, _), row in zip(windows, proba)
        ],
    }


def render_markdown(cv: dict, views: dict[str, dict], window_words: int) -> str:
    """Raporu insan okuyacak biçime çevirir."""
    cls = cv["classes"]
    md = ["# Voynich süreç sınıflandırma raporu", ""]
    md += [f"Pencere boyutu: {window_words} kelime.", ""]
    md += ["## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)", ""]
    md += [f"Doğruluk: **{cv['accuracy']:.3f}**", ""]
    md += ["| gerçek \\ tahmin | " + " | ".join(cls) + " |", "|---|" + "---|" * len(cls)]
    for c, row in zip(cls, cv["confusion_matrix"]):
        md.append(f"| {c} | " + " | ".join(str(v) for v in row) + " |")
    md += ["", "## 2. Voynich hangi sürece benziyor", ""]
    md += ["| görünüm | pencere | " + " | ".join(cls) + " |", "|---|---|" + "---|" * len(cls)]
    for name, v in views.items():
        md.append(
            f"| {name} | {v['n_windows']} | "
            + " | ".join(f"{v['mean_proba'][c]:.2f}" for c in cls)
            + " |"
        )
    md += ["", "## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)", ""]
    md += [
        "Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin "
        "tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "
        "\"en az kötü eşleşme\"dir, bulgu değil.",
        "",
        "| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |",
        "|---|---|---|---|",
    ]
    for name, v in views.items():
        o = v["ood"]
        near = ", ".join(f"{k}: {n}" for k, n in o["nearest_by_distance"].items())
        md.append(
            f"| {name} | {near} | {o['median_percentile']:.0f} | {o['median_ratio']:.1f}x |"
        )
    for name, v in views.items():
        md += ["", f"### {name}: tahmin `{v['predicted']}`, en etkili feature'lar", ""]
        md += ["| feature | katkı | Voynich ort. | sentetik evrene göre z |", "|---|---|---|---|"]
        for t in v["top_contributions"]:
            md.append(
                f"| {t['feature']} | {t['contribution']:+.2f} | "
                f"{t['voynich_mean']:.3f} | {t['z_vs_synthetic']:+.1f} |"
            )
        oor = v["ood"]["features_out_of_range"]
        if oor:
            items = ", ".join(f"{k} (%{100 * f:.0f})" for k, f in sorted(oor.items(), key=lambda x: -x[1]))
            md += ["", f"Sentetik aralığın dışına taşan feature'lar (pencere oranı): {items}"]
    return "\n".join(md) + "\n"
