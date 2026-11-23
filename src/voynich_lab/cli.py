"""Komut satırı: python -m voynich_lab.cli {fetch,build,report,all}

  fetch  : ham veriyi data/raw altına indirir
  build  : sentetik feature tablosunu üretir (results/synthetic.csv)
  report : modeli doğrular, eğitir, Voynich'i analiz eder, results/report.md yazar
  all    : üçünü sırayla çalıştırır
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


def main() -> None:
    p = argparse.ArgumentParser(prog="voynich_lab")
    p.add_argument("command", choices=["fetch", "build", "report", "all"])
    p.add_argument("--raw", default="data/raw")
    p.add_argument("--results", default="results")
    p.add_argument("--window", type=int, default=2000, help="pencere boyutu (kelime)")
    p.add_argument("--per-language", type=int, default=24, help="dil başına pencere")
    p.add_argument("--seed", type=int, default=7)
    args = p.parse_args()
    steps = {"fetch": [cmd_fetch], "build": [cmd_build], "report": [cmd_report]}
    for step in steps.get(args.command, [cmd_fetch, cmd_build, cmd_report]):
        step(args)


if __name__ == "__main__":
    main()
