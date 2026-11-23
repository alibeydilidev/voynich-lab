"""El yazması düzeyinde karşılaştırma.

abc.py ve search.py her sentetik örneği baştan üretir: yeni tablo, yeni alfabe,
yeni kod tablosu. Voynich pencereleri ise tek bir el yazmasının parçalarıdır.
Bu yüzden orada ölçülen şey büyük ölçüde "tablo şansı"dır (checks: homojenlik).

Burada birim el yazmasıdır: bir aday = ayarlar + tohum. Aday tek seferde uzun
bir metin üretir (tek tablo, tek kod tablosu), metin Voynich gibi pencerelere
bölünür ve iki yarıya ayrılır:

  seçim yarısı    : adaylar Voynich'e yakınlığa göre bununla sıralanır
  doğrulama yarısı: seçilen adayın AYNI tablodan ürettiği, seçimde hiç
                    kullanılmamış metin. Rapor edilen sayı budur.

İstatistik T: aday yarısının pencere ortalaması ile Voynich'in pencere
ortalaması arasındaki fark, feature başına standart hataya bölünür, feature'lar
üzerinden karekök ortalaması alınır. Aday pencereleri Voynich pencereleriyle
aynı kaynaktan geliyorsa T yaklaşık 1 olur. Referans: Voynich'in kendi
yarılarının birbirine karşı T değeri (rastgele bölmeler ve ardışık bölme).

T yalnız ortalamaya bakar. İç değişkenlik ayrı raporlanır (yayılım oranı):
adayın pencereleri arası standart sapmanın Voynich'inkine oranı, feature'lar
üzerinden medyan. 1 ise aday Voynich kadar değişken.
"""

from __future__ import annotations

from math import isnan

import numpy as np
import pandas as pd

from .abc import SCALE_FLOOR
from .features import FEATURE_NAMES, extract_features
from .generators import GIBBERISH_PROCESSES, LANGUAGE_PROCESSES, layout_from_params
from .search import LANGUAGE_KEY, _corpora, prior_for

MEAN_A = [f"ma_{f}" for f in FEATURE_NAMES]
MEAN_B = [f"mb_{f}" for f in FEATURE_NAMES]
SD_A = [f"sa_{f}" for f in FEATURE_NAMES]
SD_B = [f"sb_{f}" for f in FEATURE_NAMES]


def windows(lines: list[list[str]], window_words: int) -> list[list[list[str]]]:
    """Voynich'teki pencereleme ile aynı kural: satır sonunda, sayı dolunca keser."""
    out, cur, count = [], [], 0
    for ln in lines:
        cur.append(ln)
        count += len(ln)
        if count >= window_words:
            out.append(cur)
            cur, count = [], 0
    return out


def simulate_manuscript(
    label: str,
    theta: dict,
    raw: str,
    window_words: int,
    n_windows: int,
    seed: list[int],
) -> tuple[np.ndarray, dict] | None:
    """Tek tablo ve tek ayar kümesiyle n_windows pencerelik bir el yazması üretir.

    theta boşsa bütün ayarlar önselden çekilir. Dönen değer: (pencere x feature
    matrisi, kullanılan ayarlar). Aynı (theta, seed) hep aynı metni verir.
    Metin yeterince uzun çıkmazsa None döner.
    """
    rng = np.random.default_rng(seed)
    layout = layout_from_params(theta, rng)
    rec: dict = {}
    need = (n_windows + 1) * window_words
    if label in LANGUAGE_PROCESSES:
        corpora = _corpora(raw)
        language = theta.get(LANGUAGE_KEY) or str(rng.choice(sorted(_languages(label, raw))))
        words = corpora[language]
        start = int(rng.integers(0, len(words) - need))
        lines = LANGUAGE_PROCESSES[label](
            words[start : start + need], rng, layout=layout, rec=rec, fixed=theta
        )
        rec[LANGUAGE_KEY] = language
    else:
        lines = GIBBERISH_PROCESSES[label](need, rng, layout=layout, rec=rec, fixed=theta)
    wins = windows(lines, window_words)[:n_windows]
    if len(wins) < n_windows:
        return None
    feats = [extract_features(w) for w in wins]
    F = np.array([[f[name] for name in FEATURE_NAMES] for f in feats], dtype=float)
    return F, rec


def _languages(label: str, raw: str) -> list[str]:
    from .corpus import ABJAD_CAPABLE_SCRIPTS, dominant_script

    corpora = _corpora(raw)
    if label != "abjad":
        return list(corpora)
    return [k for k, w in corpora.items() if dominant_script(w) in ABJAD_CAPABLE_SCRIPTS]


def build_chunk(job: dict) -> pd.DataFrame:
    """Bir sınıf için bir dilim el yazması üretir (ayrı süreçte çalışır)."""
    rows = []
    half = job["n_windows"] // 2
    for i in range(job["start"], job["stop"]):
        seed = [job["seed"], job["label_index"], i]
        res = simulate_manuscript(
            job["label"], {}, job["raw"], job["window"], job["n_windows"], seed
        )
        if res is None:
            continue
        F, rec = res
        a, b = F[:half], F[half:]
        row = {"label": job["label"], "index": i} | rec
        row |= dict(zip(MEAN_A, a.mean(0))) | dict(zip(MEAN_B, b.mean(0)))
        row |= dict(zip(SD_A, a.std(0, ddof=1))) | dict(zip(SD_B, b.std(0, ddof=1)))
        rows.append(row)
    return pd.DataFrame(rows)


def t_statistic(mean: np.ndarray, n: int, v_mean: np.ndarray, v_n: int, scale: np.ndarray) -> np.ndarray:
    """Feature başına standart hataya bölünmüş ortalama farkının karekök ortalaması."""
    se = scale * np.sqrt(1.0 / n + 1.0 / v_n)
    return np.sqrt((((mean - v_mean) / se) ** 2).mean(-1))


def voynich_reference(V: np.ndarray, scale: np.ndarray, half: int, n_splits: int = 2000) -> dict:
    """Voynich'in kendi yarılarının birbirine karşı T değeri."""
    rng = np.random.default_rng(0)
    n = len(V)
    vals = []
    for _ in range(n_splits):
        idx = rng.permutation(n)
        a, b = V[idx[:half]], V[idx[half:]]
        vals.append(float(t_statistic(a.mean(0), len(a), b.mean(0), len(b), scale)))
    a, b = V[:half], V[half:]
    return {
        "random_median": float(np.median(vals)),
        "random_p95": float(np.percentile(vals, 95)),
        "contiguous": float(t_statistic(a.mean(0), len(a), b.mean(0), len(b), scale)),
    }


def scale_for(V: np.ndarray, universe_sd: np.ndarray) -> np.ndarray:
    return np.maximum(V.std(0, ddof=1), SCALE_FLOOR * universe_sd) + 1e-12


def analyze_view(df: pd.DataFrame, V: np.ndarray, universe_sd: np.ndarray, half: int, top: int) -> dict:
    """Bir görünüm için: her sınıfta seçim yarısına göre en yakın `top` aday ve doğrulamaları."""
    scale = scale_for(V, universe_sd)
    v_mean, v_n = V.mean(0), len(V)
    v_sd = V.std(0, ddof=1)
    out = {"reference": voynich_reference(V, scale, half), "n_windows": int(v_n), "classes": {}}
    for label, g in df.groupby("label"):
        t_sel = t_statistic(g[MEAN_A].to_numpy(float), half, v_mean, v_n, scale)
        t_val = t_statistic(g[MEAN_B].to_numpy(float), half, v_mean, v_n, scale)
        order = np.argsort(t_sel)[:top]
        z = (g[MEAN_B].to_numpy(float)[order] - v_mean) / (scale * np.sqrt(1 / half + 1 / v_n))
        z_med = np.median(z, axis=0)
        feat_order = np.argsort(-np.abs(z_med))
        spread = g[SD_B].to_numpy(float)[order] / np.maximum(v_sd, 1e-12)
        params = {}
        for name in prior_for(label):
            if name not in g:
                continue
            prior_vals = g[name].to_numpy(float)
            vals = prior_vals[order]
            vals, prior_vals = vals[~np.isnan(vals)], prior_vals[~np.isnan(prior_vals)]
            if len(vals) == 0:
                continue
            params[name] = {
                "prior_median": float(np.median(prior_vals)),
                "selected_median": float(np.median(vals)),
                "selected_iqr": [float(np.percentile(vals, 25)), float(np.percentile(vals, 75))],
            }
        out["classes"][label] = {
            "n_manuscripts": int(len(g)),
            "n_selected": int(len(order)),
            "selection_median": float(np.median(t_sel[order])),
            "validation_median": float(np.median(t_val[order])),
            "validation_best": float(t_val[order].min()),
            "validation_share_within_p95": float(
                (t_val[order] <= out["reference"]["random_p95"]).mean()
            ),
            "all_validation_best": float(t_val.min()),
            "spread_ratio_median": float(np.median(spread)),
            "n_features_off_by_2": int((np.abs(z_med) > 2).sum()),
            "misfit": [
                {
                    "feature": FEATURE_NAMES[j],
                    "z": float(z_med[j]),
                    "voynich": float(v_mean[j]),
                    "selected_median": float(np.median(g[MEAN_B].to_numpy(float)[order][:, j])),
                }
                for j in feat_order[:8]
            ],
            "params": params,
            "selected_index": [int(i) for i in g["index"].to_numpy()[order]],
        }
    return out


def reseed_job(job: dict) -> dict:
    """Seçilmiş bir adayın ayarlarını sabit tutup yeni tohumlarla (yeni tablo) yeniden üretir."""
    theta = {k: v for k, v in job["theta"].items() if not (isinstance(v, float) and isnan(v))}
    center, scale = np.array(job["center"]), np.array(job["scale"])
    vals = []
    for r in range(job["n_reseeds"]):
        res = simulate_manuscript(
            job["label"], theta, job["raw"], job["window"], job["half"],
            [job["seed"], 999, job["label_index"], job["index"], r],
        )  # fmt: skip
        if res is not None:
            vals.append(float(t_statistic(res[0].mean(0), job["half"], center, job["v_n"], scale)))
    return {"label": job["label"], "view": job["view"], "values": vals}


def render_markdown(views: dict[str, dict], settings: dict) -> str:
    labels = sorted(next(iter(views.values()))["classes"])
    half = settings["n_windows"] // 2
    md = ["# El yazması düzeyinde karşılaştırma", ""]
    md += [
        f"Her sınıftan önselden {settings['per_class']} el yazması üretildi; her biri tek tablo ve "
        f"tek ayar kümesiyle {settings['n_windows']} pencere ({half} seçim + {half} doğrulama). "
        f"Her sınıfta seçim yarısına göre Voynich'e en yakın {settings['top']} aday seçildi; "
        "tablolar bu adayların DOĞRULAMA yarısındaki değerlerini verir.",
        "",
        "T yaklaşık 1 ise adayın ortalama profili Voynich'ten ayırt edilemez. Referans, "
        "Voynich'in kendi yarılarının birbirine karşı T değeridir: rastgele bölmelerde "
        "beklenen düzey ve ardışık bölmede (ilk yarı ile son yarı) gerçekte olan.",
        "",
        "## 1. Seçilen adayların doğrulama yarısında medyan T (parantezde seçim yarısındaki değer)",
        "",
        "| görünüm | Voynich: rastgele medyan, %95, ardışık | " + " | ".join(labels) + " |",
        "|---|---|" + "---|" * len(labels),
    ]
    for name, v in views.items():
        r = v["reference"]
        cells = [
            f"{v['classes'][c]['validation_median']:.1f} ({v['classes'][c]['selection_median']:.1f})"
            for c in labels
        ]
        md.append(
            f"| {name} | {r['random_median']:.2f}, {r['random_p95']:.2f}, {r['contiguous']:.2f} | "
            + " | ".join(cells) + " |"
        )
    md += ["", "## 2. Doğrulama yarısında en iyi tek aday (T)", ""]
    md += ["| görünüm | " + " | ".join(labels) + " |", "|---|" + "---|" * len(labels)]
    for name, v in views.items():
        md.append(
            f"| {name} | "
            + " | ".join(f"{v['classes'][c]['validation_best']:.1f}" for c in labels) + " |"
        )
    md += ["", "## 3. Aynı ayar, yeni tablo: seçilen ayarlar yeni tohumla yeniden üretilince medyan T", ""]
    md += ["| görünüm | " + " | ".join(labels) + " |", "|---|" + "---|" * len(labels)]
    for name, v in views.items():
        md.append(
            f"| {name} | "
            + " | ".join(f"{v['classes'][c]['reseed_median']:.1f}" for c in labels) + " |"
        )
    md += ["", "## 4. İç değişkenlik: seçilen adayların yayılım oranı (Voynich = 1)", ""]
    md += ["| görünüm | " + " | ".join(labels) + " |", "|---|" + "---|" * len(labels)]
    for name, v in views.items():
        md.append(
            f"| {name} | "
            + " | ".join(f"{v['classes'][c]['spread_ratio_median']:.2f}" for c in labels) + " |"
        )
    for name, v in views.items():
        md += ["", f"## {name}: sınıf sınıf", ""]
        for c in sorted(labels, key=lambda c: v["classes"][c]["validation_median"]):
            r = v["classes"][c]
            md += [
                f"### {c}: doğrulama medyan T {r['validation_median']:.1f}, en iyi {r['validation_best']:.1f}",
                "",
                f"Standart hatanın 2 katından fazla sapan feature sayısı: {r['n_features_off_by_2']} / {len(FEATURE_NAMES)}",
                "",
                "| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |",
                "|---|---|---|---|",
            ]
            for m in r["misfit"][:6]:
                md.append(
                    f"| {m['feature']} | {m['z']:+.1f} | {m['voynich']:.3f} | {m['selected_median']:.3f} |"
                )
            md.append("")
    return "\n".join(md).rstrip() + "\n"
