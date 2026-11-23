# Voynich süreç sınıflandırma raporu

Pencere boyutu: 2000 kelime.

## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)

Doğruluk: **0.907**

| gerçek \ tahmin | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|
| abjad | 430 | 0 | 2 | 0 | 0 | 17 | 7 |
| grille | 1 | 487 | 1 | 0 | 14 | 24 | 1 |
| plain | 3 | 4 | 483 | 0 | 0 | 4 | 34 |
| selfcite | 1 | 0 | 0 | 496 | 26 | 5 | 0 |
| slotcite | 0 | 25 | 0 | 15 | 452 | 36 | 0 |
| slotgram | 4 | 32 | 0 | 10 | 47 | 434 | 1 |
| verbose | 7 | 7 | 8 | 0 | 0 | 2 | 504 |

## 2. Voynich hangi sürece benziyor

| görünüm | pencere | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | 16 | 0.00 | 0.23 | 0.00 | 0.00 | 0.68 | 0.09 | 0.00 |
| eva_glyph | 16 | 0.00 | 0.28 | 0.00 | 0.00 | 0.61 | 0.11 | 0.00 |
| v101 | 17 | 0.00 | 0.30 | 0.00 | 0.00 | 0.20 | 0.47 | 0.02 |
| zl_basic | 16 | 0.00 | 0.21 | 0.00 | 0.00 | 0.70 | 0.09 | 0.00 |
| zl_glyph | 16 | 0.00 | 0.26 | 0.00 | 0.00 | 0.61 | 0.13 | 0.00 |

## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)

Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "en az kötü eşleşme"dir, bulgu değil.

| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |
|---|---|---|---|
| eva_basic | slotgram: 16 | 62 | 1.1x |
| eva_glyph | slotgram: 15, grille: 1 | 45 | 1.0x |
| v101 | slotcite: 12, grille: 4, slotgram: 1 | 79 | 1.2x |
| zl_basic | slotgram: 15, grille: 1 | 49 | 1.0x |
| zl_glyph | slotgram: 16 | 34 | 0.9x |

### eva_basic: tahmin `slotcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -0.78 | 0.009 | -0.4 |
| wlen_autocorr1 | +0.70 | 0.127 | +0.7 |
| h3 | +0.39 | 1.694 | -1.0 |
| rep_adjacent_ed1 | +0.38 | 0.032 | -0.5 |
| wlen_skew | +0.32 | 0.074 | -0.7 |
| rep_within3 | -0.27 | 0.026 | -0.5 |

### eva_glyph: tahmin `slotcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -0.79 | 0.009 | -0.4 |
| wlen_autocorr1 | +0.70 | 0.103 | +0.5 |
| rep_adjacent_ed1 | +0.26 | 0.039 | -0.4 |
| rep_within3 | -0.25 | 0.026 | -0.5 |
| h3 | +0.25 | 1.818 | -0.7 |
| jsd_first | +0.19 | 0.350 | -0.3 |

### v101: tahmin `slotgram`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| top10_coverage | -0.45 | 0.166 | -0.4 |
| char_double_rate | +0.40 | 0.015 | -0.8 |
| h2 | +0.34 | 2.383 | -0.7 |
| wlen_autocorr1 | +0.31 | 0.179 | +1.0 |
| zipf_slope | -0.25 | -0.776 | +0.0 |
| hapax_ratio | +0.25 | 0.741 | +0.7 |

### zl_basic: tahmin `slotcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -0.81 | 0.008 | -0.4 |
| wlen_autocorr1 | +0.75 | 0.123 | +0.7 |
| wlen_skew | +0.45 | 0.025 | -0.8 |
| h3 | +0.36 | 1.692 | -1.0 |
| rep_adjacent_ed1 | +0.32 | 0.034 | -0.4 |
| rep_within3 | -0.22 | 0.027 | -0.5 |

### zl_glyph: tahmin `slotcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -0.82 | 0.008 | -0.4 |
| wlen_autocorr1 | +0.68 | 0.102 | +0.5 |
| wlen_skew | +0.24 | 0.154 | -0.6 |
| h3 | +0.23 | 1.817 | -0.7 |
| jsd_first | +0.22 | 0.351 | -0.3 |
| rep_adjacent_ed1 | +0.22 | 0.041 | -0.3 |
