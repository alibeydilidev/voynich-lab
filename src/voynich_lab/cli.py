"""Komut satırı: python -m voynich_lab.cli {fetch,build,report,all,abc,search,checks}

  fetch  : ham veriyi data/raw altına indirir
  build  : sentetik feature tablosunu üretir (results/synthetic.csv)
  report : modeli doğrular, eğitir, Voynich'i analiz eder, results/report.md yazar
  all    : ilk üçünü sırayla çalıştırır
  abc    : büyük sentetik tablo üretir (results/abc_synthetic.csv), her hipotezin
           Voynich'e en fazla ne kadar yaklaştığını ölçer, results/abc.md yazar
  search : abc tablosundan başlayıp her hipotez için ayarları yönlendirerek arar,
           ulaşılan en iyi noktayı taze örneklerle ölçer, results/search.md yazar
  checks : hattın kendi sonuçlarını sınayan deneyler, results/checks.md yazar
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


def cmd_fetch(args: argparse.Namespace) -> None:
    from .fetch import fetch_all

    fetch_all(args.raw)


def cmd_build(args: argparse.Namespace) -> None:
    from .corpus import load_all
    from .dataset import build_dataset

    corpora = load_all(Path(args.raw) / "bible")
    print(f"{len(corpora)} dil yüklendi: {', '.join(corpora)}")
    df = build_dataset(corpora, args.window, args.per_language, args.seed)
    out = Path(args.results)
    out.mkdir(parents=True, exist_ok=True)
    df.to_csv(out / "synthetic.csv", index=False)
    print(f"{len(df)} örnek yazıldı -> {out / 'synthetic.csv'}")
    print(df["label"].value_counts().to_string())


def cmd_report(args: argparse.Namespace) -> None:
    from .analyze import OODReference, analyze_view, render_markdown
    from .model import cross_validate, fit
    from .transliteration import load_views

    out = Path(args.results)
    df = pd.read_csv(out / "synthetic.csv")
    cv = cross_validate(df, seed=args.seed)
    print(f"Gruplu CV doğruluğu: {cv['accuracy']:.3f}")
    model, classes = fit(df, seed=args.seed)
    ood = OODReference(df)
    views = {
        name: analyze_view(lines, model, classes, ood, args.window)
        for name, lines in load_views(args.raw).items()
    }
    (out / "report.json").write_text(
        json.dumps({"cv": cv, "views": views}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    md = render_markdown(cv, views, args.window)
    (out / "report.md").write_text(md, encoding="utf-8")
    model.save_model(out / "model.json")
    print(md)


def _abc_chunk(job: tuple[str, int, int, int]) -> pd.DataFrame:
    """Tek bir tohumla sentetik tablo parçası üretir (ayrı süreçte çalışır)."""
    from .corpus import load_all
    from .dataset import build_dataset

    raw, window, per_language, seed = job
    df = build_dataset(load_all(Path(raw) / "bible"), window, per_language, seed)
    df["seed"] = seed
    return df


def cmd_abc(args: argparse.Namespace) -> None:
    from concurrent.futures import ProcessPoolExecutor

    from .abc import analyze_view, render_markdown, voynich_features
    from .transliteration import load_views

    out = Path(args.results)
    out.mkdir(parents=True, exist_ok=True)
    table = out / "abc_synthetic.csv"
    seeds = [args.seed + 1000 * (i + 1) for i in range(args.abc_seeds)]
    if table.exists() and not args.rebuild:
        df = pd.read_csv(table)
        print(f"var olan tablo okundu: {len(df)} örnek ({table}); yeniden üretmek için --rebuild")
    else:
        jobs = [(args.raw, args.window, args.abc_per_language, s) for s in seeds]
        with ProcessPoolExecutor(max_workers=min(args.jobs, len(jobs))) as pool:
            df = pd.concat(list(pool.map(_abc_chunk, jobs)), ignore_index=True)
        df.to_csv(table, index=False)
        print(f"{len(df)} örnek yazıldı -> {table}")
    print(df["label"].value_counts().to_string())
    views = {
        name: analyze_view(df, voynich_features(lines, args.window), args.accept)
        for name, lines in load_views(args.raw).items()
    }
    (out / "abc.json").write_text(
        json.dumps({"n_samples": len(df), "accept": args.accept, "views": views}, indent=2),
        encoding="utf-8",
    )
    md = render_markdown(views, len(df), args.accept)
    (out / "abc.md").write_text(md, encoding="utf-8")
    print(md)


def cmd_search(args: argparse.Namespace) -> None:
    from concurrent.futures import ProcessPoolExecutor

    import numpy as np

    from .abc import SCALE_FLOOR, voynich_features
    from .features import FEATURE_NAMES
    from .generators import LANGUAGE_PROCESSES
    from .search import initial_population, render_markdown, run_search
    from .transliteration import load_views

    out = Path(args.results)
    df = pd.read_csv(out / "abc_synthetic.csv")
    abc = json.loads((out / "abc.json").read_text(encoding="utf-8"))
    universe_sd = df[FEATURE_NAMES].to_numpy(dtype=float).std(0)
    labels = sorted(df["label"].unique())
    jobs, meta = [], {}
    for vi, (view, lines) in enumerate(load_views(args.raw).items()):
        V = voynich_features(lines, args.window).to_numpy(dtype=float)
        center = V.mean(0)
        scale = np.maximum(V.std(0, ddof=1), SCALE_FLOOR * universe_sd) + 1e-12
        n = len(V)
        self_d = np.sqrt(((((V - (center * n - V) / (n - 1)) / scale) ** 2).mean(1)))
        meta[view] = {"median": float(np.median(self_d)), "max": float(self_d.max())}
        for li, label in enumerate(labels):
            languages = (
                sorted(df.loc[df["label"] == label, "group"].unique())
                if label in LANGUAGE_PROCESSES
                else []
            )
            jobs.append(
                {
                    "label": label,
                    "view": view,
                    "raw": args.raw,
                    "window": args.window,
                    "center": center.tolist(),
                    "scale": scale.tolist(),
                    "self_max": meta[view]["max"],
                    "languages": languages,
                    "init": initial_population(df, label, center, scale, args.keep),
                    "keep": args.keep,
                    "children": args.children,
                    "rounds": args.rounds,
                    "fresh": args.fresh,
                    "seed": [args.seed, vi, li],
                }
            )
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        results = list(pool.map(run_search, jobs))
    views: dict = {v: {"self_distance": m, "classes": {}} for v, m in meta.items()}
    for r in results:
        r["abc_median_distance"] = abc["views"][r["view"]]["classes"][r["label"]][
            "accepted_median_distance"
        ]
        views[r["view"]]["classes"][r["label"]] = r
    settings = {"rounds": args.rounds, "keep": args.keep, "children": args.children, "fresh": args.fresh}
    (out / "search.json").write_text(
        json.dumps({"settings": settings, "views": views}, indent=2), encoding="utf-8"
    )
    md = render_markdown(views, settings)
    (out / "search.md").write_text(md, encoding="utf-8")
    print(md)


def cmd_checks(args: argparse.Namespace) -> None:
    from .abc import voynich_features
    from .checks import (
        evaize_experiment,
        homogeneity_experiment,
        render_homogeneity,
        render_markdown,
    )
    from .transliteration import load_views

    out = Path(args.results)
    df = pd.read_csv(out / "synthetic.csv")
    evaized = evaize_experiment(df, args.window, model_seed=args.seed)
    voynich = {
        name: voynich_features(lines, args.window) for name, lines in load_views(args.raw).items()
    }
    homogeneity = homogeneity_experiment(df, voynich, args.window)
    (out / "checks.json").write_text(
        json.dumps({"evaize": evaized, "homogeneity": homogeneity}, indent=2), encoding="utf-8"
    )
    md = render_markdown(evaized) + "\n" + render_homogeneity(homogeneity)
    (out / "checks.md").write_text(md, encoding="utf-8")
    print(md)


def main() -> None:
    p = argparse.ArgumentParser(prog="voynich_lab")
    p.add_argument("command", choices=["fetch", "build", "report", "all", "abc", "search", "checks"])
    p.add_argument("--raw", default="data/raw")
    p.add_argument("--results", default="results")
    p.add_argument("--window", type=int, default=2000, help="pencere boyutu (kelime)")
    p.add_argument("--per-language", type=int, default=24, help="dil başına pencere")
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--abc-per-language", type=int, default=100, help="abc: dil başına pencere")
    p.add_argument("--abc-seeds", type=int, default=4, help="abc: kaç ayrı tohumla üretilecek")
    p.add_argument("--accept", type=float, default=0.01, help="abc: kabul oranı")
    p.add_argument("--jobs", type=int, default=4, help="abc: paralel süreç sayısı")
    p.add_argument("--rebuild", action="store_true", help="abc: tabloyu baştan üret")
    p.add_argument("--rounds", type=int, default=5, help="search: tur sayısı")
    p.add_argument("--keep", type=int, default=100, help="search: her turda tutulan ayar sayısı")
    p.add_argument("--children", type=int, default=6, help="search: tutulan ayar başına deneme")
    p.add_argument("--fresh", type=int, default=2, help="search: son ayar başına taze örnek")
    args = p.parse_args()
    steps = {
        "fetch": [cmd_fetch],
        "build": [cmd_build],
        "report": [cmd_report],
        "abc": [cmd_abc],
        "search": [cmd_search],
        "checks": [cmd_checks],
    }
    for step in steps.get(args.command, [cmd_fetch, cmd_build, cmd_report]):
        step(args)


if __name__ == "__main__":
    main()
