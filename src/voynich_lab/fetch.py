"""Ham veriyi indirir. Veri depoya girmez (lisansları üçüncü taraflara ait)."""

from __future__ import annotations

import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

_RAW = "https://raw.githubusercontent.com"

TRANSLITERATIONS = {
    "takahashi_eva.txt": f"{_RAW}/alephmembeth/voynich/HEAD/analysis/takahashi_original.txt",
    "claston_v101.txt": f"{_RAW}/musyoku/voynich-transcription/HEAD/voynich.txt",
    # Zandbergen ve Landini, IVTFF 2.0. Dosya adı sürümü taşır (3b, 13/05/2025).
    "zl_ivtff.txt": "https://www.voynich.nu/data/ZL3b-n.txt",
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
    # voynich.nu, Python'un varsayılan istemci adını 406 ile reddediyor; genel bir ad verilir.
    req = urllib.request.Request(url, headers={"User-Agent": "fetch/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        dest.write_bytes(r.read())


# 15. yüzyıl dönem metinleri (İncil çevirileri modern olduğu için karşılaştırma tabanı).
# Dosya adı: dil_eser_yaklaşık-yıl. Kaynak ya Latin Library sayfa listesi ya da
# Wikisource alt sayfa öneki (isteğe bağlı başlık süzgeciyle).
PERIOD_TEXTS: dict[str, dict] = {
    "latin_kempis_1420": {
        "latin_library": [f"kempis/kempis{i}.shtml" for i in range(1, 5)],
    },
    "italian_alberti_1440": {"wikisource": ("it", "I libri della famiglia/", None)},
    "spanish_celestina_1499": {"wikisource": ("es", "La Celestina (1913)/", "aucto")},
}
_UA = {"User-Agent": "fetch/1.0"}
_TAG_BLOCK = re.compile(r"<(style|script)[^>]*>.*?</\1>", re.S)
_NOTE = re.compile(r'<sup[^>]*>.*?</sup>|<ol class="references">.*?</ol>', re.S)
_TAG = re.compile(r"<[^>]+>")


def _html_to_text(page: str) -> str:
    """İndirilen sayfa güvenilmez veri: yalnız regex ile etiketler atılır, hiçbir şey çalıştırılmaz."""
    page = _NOTE.sub(" ", _TAG_BLOCK.sub(" ", page))
    return re.sub(r"\s+", " ", html.unescape(_TAG.sub(" ", page))).strip()


def _get(url: str, pause: float) -> bytes:
    """Kaynağın hız sınırına uyar: her istekten önce bekler, 429 gelirse söylenen kadar bekleyip yeniden dener."""
    for _ in range(6):
        time.sleep(pause)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=_UA), timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
            time.sleep(min(int(e.headers.get("Retry-After") or 30), 120))
    raise RuntimeError(f"hız sınırı aşılamadı: {url}")


def _wikisource(site: str, **params: str | int) -> dict:
    query = urllib.parse.urlencode(params | {"format": "json", "formatversion": 2})
    return json.loads(_get(f"https://{site}.wikisource.org/w/api.php?{query}", pause=4.0))


def _period_text(spec: dict) -> str:
    if "latin_library" in spec:
        pages = [
            _get("https://www.thelatinlibrary.com/" + path, pause=2.0).decode("latin-1")
            for path in spec["latin_library"]
        ]
        return "\n\n".join(_html_to_text(p) for p in pages)
    site, prefix, must = spec["wikisource"]
    titles: list[str] = []
    cont: dict = {}
    while True:
        d = _wikisource(site, action="query", list="allpages", apprefix=prefix, aplimit=200, apnamespace=0, **cont)
        titles += [p["title"] for p in d["query"]["allpages"]]
        if "continue" not in d:
            break
        cont = {"apcontinue": d["continue"]["apcontinue"]}
    parts = []
    for title in titles:
        if must is not None and must not in title.lower():
            continue
        d = _wikisource(site, action="parse", page=title, prop="text", disablelimitreport=1, disableeditsection=1)
        parts.append(_html_to_text(d["parse"]["text"]))
    return "\n\n".join(parts)


def fetch_period(raw_dir: str | Path) -> None:
    out = Path(raw_dir) / "period"
    out.mkdir(parents=True, exist_ok=True)
    for name, spec in PERIOD_TEXTS.items():
        dest = out / f"{name}.txt"
        if dest.exists() and dest.stat().st_size > 1000:
            print(f"  var: {dest.name}")
            continue
        print(f"  indiriliyor: {dest.name} (hız sınırı nedeniyle yavaş)")
        dest.write_text(_period_text(spec), encoding="utf-8")


def fetch_all(raw_dir: str | Path) -> None:
    raw_dir = Path(raw_dir)
    (raw_dir / "bible").mkdir(parents=True, exist_ok=True)
    for name, url in TRANSLITERATIONS.items():
        _download(url, raw_dir / name)
    for lang in BIBLE_LANGUAGES:
        _download(_BIBLE_URL.format(lang=lang), raw_dir / "bible" / f"{lang}.xml")
    fetch_period(raw_dir)
