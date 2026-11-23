"""Ham veriyi indirir. Veri depoya girmez (lisansları üçüncü taraflara ait)."""

from __future__ import annotations

import urllib.request
from pathlib import Path

_RAW = "https://raw.githubusercontent.com"

TRANSLITERATIONS = {
    "takahashi_eva.txt": f"{_RAW}/alephmembeth/voynich/HEAD/analysis/takahashi_original.txt",
    "claston_v101.txt": f"{_RAW}/musyoku/voynich-transcription/HEAD/voynich.txt",
}

BIBLE_LANGUAGES = [
    "Latin", "Italian", "Spanish", "French", "Portuguese", "Romanian",
    "German", "English", "Dutch", "Swedish",
    "Czech", "Polish", "Croatian", "Russian",
    "Greek", "Albanian", "Hungarian", "Finnish", "Turkish",
    "Hebrew", "Arabic", "Farsi",
]  # fmt: skip
_BIBLE_URL = _RAW + "/christos-c/bible-corpus/master/bibles/{lang}.xml"


def _download(url: str, dest: Path) -> None:
    if dest.exists() and dest.stat().st_size > 1000:
        print(f"  var: {dest.name}")
        return
    print(f"  indiriliyor: {dest.name}")
    with urllib.request.urlopen(url, timeout=120) as r:
        dest.write_bytes(r.read())


def fetch_all(raw_dir: str | Path) -> None:
    raw_dir = Path(raw_dir)
    (raw_dir / "bible").mkdir(parents=True, exist_ok=True)
    for name, url in TRANSLITERATIONS.items():
        _download(url, raw_dir / name)
    for lang in BIBLE_LANGUAGES:
        _download(_BIBLE_URL.format(lang=lang), raw_dir / "bible" / f"{lang}.xml")
