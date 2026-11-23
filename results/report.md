# Voynich süreç sınıflandırma raporu

Pencere boyutu: 2000 kelime.

## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)

Doğruluk: **0.979**

| gerçek \ tahmin | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|
| abjad | 448 | 1 | 2 | 1 | 4 |
| grille | 1 | 520 | 1 | 2 | 4 |
| plain | 2 | 2 | 506 | 0 | 18 |
| selfcite | 0 | 3 | 0 | 525 | 0 |
| verbose | 3 | 5 | 5 | 0 | 515 |

## 2. Voynich hangi sürece benziyor

| görünüm | pencere | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|---|
| eva_basic | 16 | 0.00 | 0.94 | 0.00 | 0.06 | 0.00 |
| eva_glyph | 16 | 0.00 | 0.93 | 0.00 | 0.06 | 0.00 |
| v101 | 17 | 0.00 | 0.66 | 0.02 | 0.31 | 0.01 |
| zl_basic | 16 | 0.00 | 0.95 | 0.00 | 0.05 | 0.00 |
| zl_glyph | 16 | 0.00 | 0.91 | 0.00 | 0.08 | 0.00 |

## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)

Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "en az kötü eşleşme"dir, bulgu değil.

| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |
|---|---|---|---|
| eva_basic | grille: 16 | 86 | 1.3x |
| eva_glyph | grille: 16 | 68 | 1.1x |
| v101 | grille: 17 | 93 | 1.4x |
| zl_basic | grille: 16 | 85 | 1.2x |
| zl_glyph | grille: 16 | 72 | 1.1x |

### eva_basic: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_skew | +1.89 | 0.074 | -1.0 |
| wlen_autocorr1 | -1.26 | 0.127 | +0.7 |
| rep_adjacent_exact | +0.69 | 0.009 | -0.2 |
| h2 | +0.54 | 2.016 | -1.8 |
| h3 | +0.37 | 1.694 | -1.2 |
| char_double_rate | +0.32 | 0.067 | -0.1 |

### eva_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_skew | +1.73 | 0.183 | -0.8 |
| wlen_autocorr1 | -0.99 | 0.103 | +0.6 |
| rep_adjacent_exact | +0.70 | 0.009 | -0.2 |
| h2 | +0.60 | 2.131 | -1.6 |
| char_double_rate | +0.32 | 0.076 | -0.0 |
| h3 | +0.27 | 1.818 | -0.8 |

### v101: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_skew | +1.48 | 0.225 | -0.7 |
| wlen_autocorr1 | -1.24 | 0.179 | +1.0 |
| char_double_rate | -0.61 | 0.015 | -0.8 |
| h2 | +0.55 | 2.383 | -1.0 |
| rep_adjacent_exact | +0.52 | 0.006 | -0.3 |
| wlen_std | +0.18 | 1.469 | -0.6 |

### zl_basic: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_skew | +2.00 | 0.025 | -1.1 |
| wlen_autocorr1 | -1.11 | 0.123 | +0.7 |
| rep_adjacent_exact | +0.69 | 0.008 | -0.2 |
| h2 | +0.54 | 2.013 | -1.8 |
| h3 | +0.35 | 1.692 | -1.2 |
| char_double_rate | +0.31 | 0.066 | -0.1 |

### zl_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_skew | +1.78 | 0.154 | -0.9 |
| wlen_autocorr1 | -1.04 | 0.102 | +0.6 |
| rep_adjacent_exact | +0.70 | 0.008 | -0.2 |
| h2 | +0.60 | 2.127 | -1.6 |
| char_double_rate | +0.32 | 0.076 | -0.0 |
| h3 | +0.28 | 1.817 | -0.8 |
