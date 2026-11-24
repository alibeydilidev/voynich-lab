"""Voynich transliterasyon dosyalarını ortak `Lines` biçimine çevirir.

Beş görünüm üretilir, çünkü hem "hangi çizgi tek harf" kararı hem de okuyan
kişi istatistikleri değiştirir:
  eva_basic : Takahashi EVA, her EVA harfi bir sembol
  eva_glyph : Takahashi EVA, ch/sh ve sehpalı gallows'lar tek sembol
  v101      : Glen Claston v101, bambaşka (daha ince taneli) bir alfabe
  zl_basic  : Zandbergen ve Landini (IVTFF), EVA, her harf bir sembol
  zl_glyph  : Zandbergen ve Landini, ch/sh ve sehpalı gallows'lar tek sembol
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

# EVA'da birden fazla harfle yazılan ama el yazmasında tek glif olan birimler.
# Sıra önemli: uzun olanlar önce eşleşmeli.
_EVA_LIGATURES = ["cth", "ckh", "cph", "cfh", "sh", "ch"]
_PRIVATE_BASE = 0xE000  # Unicode özel kullanım alanı, gerçek harflerle çakışmaz

_TAKAHASHI_TAG = re.compile(r"^<f(\w+?)\.([A-Za-z])\w*\.\d+;\w>\s*(.*)$")
_V101_TAG = re.compile(r"^<(\d+[rv]\d*(?:-[rv]?\d*)?)\.(\d+)>(.*)$")
_IVTFF_LOCUS = re.compile(r"^<f(\w+)\.\d+\w*,[^\w>]?(\w+)>\s*(.*)$")
_IVTFF_COMMENT = re.compile(r"<![^>]*>")
_IVTFF_TAG = re.compile(r"<[^>]*>")
_IVTFF_ALTERNATIVE = re.compile(r"\[([^:\]]*):[^\]]*\]")
_IVTFF_RARE = re.compile(r"\{[^}]*\}|@\d+;")
_RARE_BASE = _PRIVATE_BASE + 0x40  # IVTFF'teki nadir ve bileşik glifler


@dataclass(frozen=True)
class FolioLine:
    folio: str
    words: list[str]


def _merge_eva_ligatures(word: str) -> str:
    for i, lig in enumerate(_EVA_LIGATURES):
        word = word.replace(lig, chr(_PRIVATE_BASE + i))
    return word


def load_takahashi(
    path: str | Path,
    glyph_mode: str = "basic",
    locus_types: tuple[str, ...] = ("P",),
) -> list[FolioLine]:
    """Takahashi EVA dosyasını okur.

    locus_types: varsayılan yalnızca paragraf metni (P). Etiketler, halka
    yazıları vb. akan metin istatistiklerini bozduğu için dışarıda bırakılır.
    Okunamayan glif (*) içeren kelimeler atılır.

    Satır ortasındaki "-" bir çizimin metni böldüğü yerdir; glif değil, kelime
    sınırı sayılır (satır sonu sayılmaz, bkz. CLAUDE.md "Bilinen tuzaklar").
    """
    if glyph_mode not in ("basic", "glyph"):
        raise ValueError(f"glyph_mode 'basic' ya da 'glyph' olmalı: {glyph_mode}")
    out: list[FolioLine] = []
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        m = _TAKAHASHI_TAG.match(raw)
        if not m:
            continue
        folio, locus, body = m.groups()
        if locus not in locus_types:
            continue
        body = body.replace("!", "").replace("%", "").rstrip("-=").lower()
        body = body.replace("-", ".")  # çizim boşluğu: kelime sınırı
        words = [w for w in body.split(".") if w and "*" not in w]
        if glyph_mode == "glyph":
            words = [_merge_eva_ligatures(w) for w in words]
        if words:
            out.append(FolioLine(folio, words))
    return out


def load_v101(path: str | Path, comma_is_space: bool = True) -> list[FolioLine]:
    """Claston v101 dosyasını okur. Yalnızca düz numaralı (paragraf) satırlar alınır.

    comma_is_space: v101'de virgül "belirsiz boşluk" demek. True ise boşluk
    sayılır, False ise kelime birleştirilir. Sonuçların buna duyarlılığı
    ayrıca test edilmeli.
    """
    out: list[FolioLine] = []
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        m = _V101_TAG.match(raw)
        if not m:
            continue
        folio, _, body = m.groups()
        body = body.rstrip("-=")
        body = body.replace(",", "." if comma_is_space else "")
        words = [w for w in body.split(".") if w and "?" not in w]
        if words:
            out.append(FolioLine(folio, words))
    return out


def load_ivtff(
    path: str | Path,
    glyph_mode: str = "basic",
    locus_types: tuple[str, ...] = ("P0",),
    comma_is_space: bool = True,
) -> list[FolioLine]:
    """IVTFF 2.0 biçimindeki EVA dosyasını okur (Zandbergen ve Landini, ZL).

    locus_types: varsayılan yalnız olağan paragraf metni (P0). Bu, Takahashi
    dosyasındaki P satırlarının karşılığıdır; başlık (Pt), ortalanmış ya da sağa
    yaslı son satır (Pc, Pr) ve özel bloklar (P1, Pb) dışarıda kalır.

    Biçim kuralları: `<!...>` yorumdur; `<->` çizimin metni böldüğü yerdir ve
    kelime sınırı sayılır; `<%>` ile `<$>` paragraf başı ve sonudur; `[a:b]`
    alternatif okumadır, ilki alınır; `{...}` ve `@123;` nadir ya da bileşik bir
    gliftir, her farklı içerik tek bir sembole eşlenir; virgül belirsiz
    boşluktur; `?` okunamayan gliftir, içeren kelime atılır. Tek tırnak (çizgi
    eklentisi) atılır.
    """
    if glyph_mode not in ("basic", "glyph"):
        raise ValueError(f"glyph_mode 'basic' ya da 'glyph' olmalı: {glyph_mode}")
    rare: dict[str, str] = {}

    def rare_glyph(m: re.Match) -> str:
        return rare.setdefault(m.group(0), chr(_RARE_BASE + len(rare)))

    out: list[FolioLine] = []
    for raw in Path(path).read_text(encoding="latin-1").splitlines():
        m = _IVTFF_LOCUS.match(raw)
        if not m:
            continue
        folio, locus, body = m.groups()
        if locus not in locus_types:
            continue
        body = _IVTFF_COMMENT.sub("", body).replace("<->", ".")
        body = _IVTFF_TAG.sub("", body)
        body = _IVTFF_ALTERNATIVE.sub(r"\1", body)
        body = _IVTFF_RARE.sub(rare_glyph, body.lower()).replace("'", "").replace(" ", "")
        body = body.replace(",", "." if comma_is_space else "")
        words = [w for w in body.split(".") if w and "?" not in w]
        if glyph_mode == "glyph":
            words = [_merge_eva_ligatures(w) for w in words]
        if words:
            out.append(FolioLine(folio, words))
    return out


_IVTFF_PAGE = re.compile(r"^<f(\w+)>\s*<!(.*)>\s*$")


def ivtff_page_variables(path: str | Path) -> dict[str, dict[str, str]]:
    """IVTFF sayfa başlıklarındaki değişkenler: {folio: {değişken: değer}}.

    Kullanılanlar: L = Currier dili (A ya da B), H = el, I = çizim türü
    (H bitki, A astronomi, Z zodyak, B banyo, C kozmoloji, P eczacılık,
    S yıldızlı reçete, T yalnız metin).
    """
    out: dict[str, dict[str, str]] = {}
    for raw in Path(path).read_text(encoding="latin-1").splitlines():
        m = _IVTFF_PAGE.match(raw)
        if m:
            out[m.group(1)] = dict(re.findall(r"\$(\w)=(\S+)", m.group(2)))
    return out


def load_views(raw_dir: str | Path) -> dict[str, list[FolioLine]]:
    """Mevcut bütün transliterasyon görünümlerini yükler."""
    raw_dir = Path(raw_dir)
    eva, v101 = raw_dir / "takahashi_eva.txt", raw_dir / "claston_v101.txt"
    zl = raw_dir / "zl_ivtff.txt"
    views: dict[str, list[FolioLine]] = {}
    if eva.exists():
        views["eva_basic"] = load_takahashi(eva, "basic")
        views["eva_glyph"] = load_takahashi(eva, "glyph")
    if v101.exists():
        views["v101"] = load_v101(v101)
    if zl.exists():
        views["zl_basic"] = load_ivtff(zl, "basic")
        views["zl_glyph"] = load_ivtff(zl, "glyph")
    if not views:
        raise FileNotFoundError(f"{raw_dir} içinde transliterasyon yok, önce 'fetch' çalıştır")
    return views


def to_windows(
    lines: list[FolioLine], window_words: int
) -> list[tuple[str, list[list[str]]]]:
    """Ardışık satırları ~window_words kelimelik pencerelere böler.

    Dönen her öğe: ("f1r..f8v" gibi folio aralığı, satırlar). Sondaki eksik
    pencere atılır, çünkü feature'lar pencere boyutuna duyarlı.
    """
    windows, cur, count = [], [], 0
    for ln in lines:
        cur.append(ln)
        count += len(ln.words)
        if count >= window_words:
            label = f"{cur[0].folio}..{cur[-1].folio}"
            windows.append((label, [c.words for c in cur]))
            cur, count = [], 0
    return windows
