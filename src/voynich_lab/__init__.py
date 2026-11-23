"""voynich-lab: Voynich metnini çözmek yerine, onu üreten süreci sınıflandıran hat.

Ortak veri tipi: bir metin örneği = satır listesi, her satır = kelime listesi,
her kelime = str. Her karakter tek bir sembolü (glifi) temsil eder.
"""

Lines = list[list[str]]

__all__ = ["Lines"]
