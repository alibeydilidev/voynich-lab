# Voynich süreç sınıflandırma raporu

Pencere boyutu: 2000 kelime.

## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)

Doğruluk: **0.952**

| gerçek \ tahmin | abjad | grille | plain | selfcite | slotcite | verbose |
|---|---|---|---|---|---|---|
| abjad | 443 | 2 | 4 | 2 | 1 | 4 |
| grille | 1 | 514 | 0 | 0 | 8 | 5 |
| plain | 1 | 4 | 502 | 1 | 0 | 20 |
| selfcite | 0 | 1 | 0 | 498 | 29 | 0 |
| slotcite | 1 | 30 | 0 | 19 | 478 | 0 |
| verbose | 4 | 6 | 7 | 0 | 0 | 511 |

## 2. Voynich hangi sürece benziyor

| görünüm | pencere | abjad | grille | plain | selfcite | slotcite | verbose |
|---|---|---|---|---|---|---|---|
| eva_basic | 16 | 0.00 | 0.39 | 0.00 | 0.00 | 0.60 | 0.00 |
| eva_glyph | 16 | 0.00 | 0.56 | 0.00 | 0.00 | 0.44 | 0.00 |
| v101 | 17 | 0.00 | 0.74 | 0.01 | 0.03 | 0.22 | 0.01 |
| zl_basic | 16 | 0.00 | 0.40 | 0.00 | 0.00 | 0.59 | 0.00 |
| zl_glyph | 16 | 0.00 | 0.56 | 0.00 | 0.00 | 0.44 | 0.00 |

## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)

Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "en az kötü eşleşme"dir, bulgu değil.

| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |
|---|---|---|---|
| eva_basic | grille: 10, slotcite: 6 | 86 | 1.3x |
| eva_glyph | grille: 12, slotcite: 4 | 68 | 1.1x |
| v101 | slotcite: 17 | 82 | 1.2x |
| zl_basic | slotcite: 14, grille: 2 | 74 | 1.1x |
| zl_glyph | slotcite: 13, grille: 3 | 52 | 1.0x |

### eva_basic: tahmin `slotcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -0.94 | 0.009 | -0.4 |
| rep_within3 | -0.54 | 0.026 | -0.5 |
| wlen_autocorr1 | +0.36 | 0.127 | +0.6 |
| h2 | +0.31 | 2.016 | -1.6 |
| jsd_last | -0.30 | 0.719 | +0.9 |
| char_double_rate | +0.30 | 0.067 | -0.1 |

### eva_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | +1.01 | 0.009 | -0.4 |
| wlen_skew | +0.80 | 0.183 | -0.6 |
| wlen_autocorr1 | -0.55 | 0.103 | +0.5 |
| top1_freq | -0.44 | 0.034 | -0.5 |
| top10_coverage | -0.37 | 0.171 | -0.4 |
| h2 | +0.33 | 2.131 | -1.3 |

### v101: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | +1.26 | 0.006 | -0.4 |
| wlen_skew | +0.70 | 0.225 | -0.5 |
| char_double_rate | -0.61 | 0.015 | -0.8 |
| wlen_autocorr1 | -0.44 | 0.179 | +1.0 |
| top1_freq | -0.33 | 0.034 | -0.5 |
| top10_coverage | -0.31 | 0.166 | -0.5 |

### zl_basic: tahmin `slotcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -1.00 | 0.008 | -0.4 |
| rep_within3 | -0.45 | 0.027 | -0.4 |
| wlen_autocorr1 | +0.39 | 0.123 | +0.6 |
| wlen_skew | +0.34 | 0.025 | -0.9 |
| h2 | +0.32 | 2.013 | -1.6 |
| jsd_last | -0.29 | 0.712 | +0.9 |

### zl_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | +1.08 | 0.008 | -0.4 |
| wlen_skew | +0.91 | 0.154 | -0.6 |
| wlen_autocorr1 | -0.41 | 0.102 | +0.5 |
| top1_freq | -0.40 | 0.034 | -0.5 |
| top10_coverage | -0.33 | 0.175 | -0.4 |
| h2 | +0.31 | 2.127 | -1.3 |
