"""Doğal dil korpusu: çok dilli paralel İncil (christos-c/bible-corpus).

Neden İncil: 22 dilde aynı içerik, Latince, İbranice, Arapça ve Türkçe dahil.
İçerik sabit kaldığı için sınıflandırıcı "konu"yu değil yazı sistemini öğrenir.
Sınırı: çeviriler modern. 15. yüzyıl metinleri eklemek açık iş (bkz. CLAUDE.md).
"""

from __future__ import annotations

import html
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

# İndirilen dosya güvenilmez veri: XML ayrıştırıcı yerine düz regex kullanılır.
_SEG = re.compile(r"<seg[^>]*>(.*?)</seg>", re.S)

# İşaretleri (hareke, nikud, aksan) atılacak yazılar. Latin ve Kiril'de
# aksanlı harfler ayrı harf sayıldığı için (ö, ş, й) dokunulmaz.
_STRIP_MARK_SCRIPTS = ("HEBREW", "ARABIC", "GREEK")

_VOWEL_BASES = set("aeiouyæøœıə" "αεηιουω" "аеиоуыэюяєіїё")
# Sesli harf atma (abjad) süreci yalnızca bu yazılarda anlamlı.
ABJAD_CAPABLE_SCRIPTS = ("LATIN", "GREEK", "CYRILLIC")


@lru_cache(maxsize=4096)
def _script(ch: str) -> str:
    try:
        return unicodedata.name(ch).split(" ")[0]
    except ValueError:
        return "UNKNOWN"


@lru_cache(maxsize=4096)
def is_vowel(ch: str) -> bool:
    base = unicodedata.normalize("NFD", ch)[0]
    return base in _VOWEL_BASES


def normalize(text: str) -> list[str]:
    """Küçük harfe çevirir, harf olmayan her şeyi kelime ayracı sayar."""
    text = unicodedata.normalize("NFD", text.lower())
    out, cur = [], []
    for ch in text:
        cat = unicodedata.category(ch)
        if cat.startswith("L"):
            cur.append(ch)
        elif cat == "Mn":
            # Birleşen işaret: bazı yazılarda at, diğerlerinde harfe geri kat.
            if cur and _script(cur[-1][0]) not in _STRIP_MARK_SCRIPTS:
                merged = unicodedata.normalize("NFC", cur[-1] + ch)
                if len(merged) == 1:  # hazır birleşik harf yoksa işareti at
                    cur[-1] = merged
        else:
            if cur:
                out.append("".join(cur))
                cur = []
    if cur:
        out.append("".join(cur))
    return out


def load_bible(path: str | Path) -> list[str]:
    """Bir İncil XML dosyasını normalize edilmiş kelime listesine çevirir."""
    raw = Path(path).read_text(encoding="utf-8", errors="replace")
    verses = (html.unescape(v) for v in _SEG.findall(raw))
    words: list[str] = []
    for v in verses:
        words.extend(normalize(v))
    return words


def load_period(period_dir: str | Path) -> dict[str, list[str]]:
    """Dönem metinleri: {dosya adı: kelimeler}. Dosyalar `fetch` ile gelen düz metinlerdir.

    Baştaki ve sondaki birkaç yüz kelime (sayfa başlığı, gezinme bağlantıları)
    atılmaz; 30 bin kelimenin üstündeki metinde payları ihmal edilebilir.
    """
    out = {}
    for p in sorted(Path(period_dir).glob("*.txt")):
        words = normalize(p.read_text(encoding="utf-8", errors="replace"))
        if len(words) > 30_000:
            out[p.stem] = words
    return out


def dominant_script(words: list[str], sample: int = 2000) -> str:
    counts: dict[str, int] = {}
    for w in words[:sample]:
        s = _script(w[0])
        counts[s] = counts.get(s, 0) + 1
    return max(counts, key=counts.get)


def load_all(bible_dir: str | Path) -> dict[str, list[str]]:
    """{dil adı: kelimeler}. Dosya adı dil adıdır (Latin.xml -> 'Latin')."""
    out = {}
    for p in sorted(Path(bible_dir).glob("*.xml")):
        words = load_bible(p)
        if len(words) > 50_000:
            out[p.stem] = words
    if not out:
        raise FileNotFoundError(f"{bible_dir} içinde korpus yok, önce 'fetch' çalıştır")
    return out
