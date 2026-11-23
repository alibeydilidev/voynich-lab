# Voynich süreç sınıflandırma raporu

Pencere boyutu: 2000 kelime.

## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)

Doğruluk: **0.920**

| gerçek \ tahmin | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|
| abjad | 425 | 1 | 2 | 0 | 0 | 25 | 3 |
| grille | 1 | 494 | 0 | 1 | 8 | 21 | 3 |
| plain | 3 | 4 | 496 | 0 | 0 | 2 | 23 |
| selfcite | 0 | 0 | 0 | 498 | 27 | 3 | 0 |
| slotcite | 1 | 28 | 0 | 16 | 459 | 24 | 0 |
| slotgram | 8 | 31 | 0 | 8 | 36 | 445 | 0 |
| verbose | 3 | 7 | 2 | 0 | 0 | 0 | 516 |

## 2. Voynich hangi sürece benziyor

| görünüm | pencere | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | 16 | 0.00 | 0.31 | 0.00 | 0.00 | 0.54 | 0.14 | 0.01 |
| eva_glyph | 16 | 0.00 | 0.42 | 0.00 | 0.00 | 0.40 | 0.18 | 0.00 |
| v101 | 17 | 0.00 | 0.48 | 0.00 | 0.00 | 0.08 | 0.42 | 0.01 |
| zl_basic | 16 | 0.00 | 0.35 | 0.00 | 0.00 | 0.44 | 0.20 | 0.01 |
| zl_glyph | 16 | 0.00 | 0.46 | 0.00 | 0.00 | 0.32 | 0.21 | 0.00 |

## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)

Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "en az kötü eşleşme"dir, bulgu değil.

| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |
|---|---|---|---|
| eva_basic | slotgram: 16 | 59 | 1.1x |
| eva_glyph | slotgram: 16 | 45 | 1.0x |
| v101 | slotcite: 14, slotgram: 3 | 81 | 1.2x |
| zl_basic | slotgram: 16 | 50 | 1.0x |
| zl_glyph | slotgram: 15, grille: 1 | 36 | 0.9x |

### eva_basic: tahmin `slotcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -0.82 | 0.009 | -0.4 |
| wlen_autocorr1 | +0.42 | 0.127 | +0.7 |
| h3 | +0.39 | 1.694 | -1.0 |
| rep_within3 | -0.30 | 0.026 | -0.5 |
| rep_adjacent_ed1 | +0.24 | 0.032 | -0.5 |
| wlen_skew | +0.23 | 0.074 | -0.7 |

### eva_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | +0.79 | 0.009 | -0.4 |
| wlen_skew | +0.68 | 0.183 | -0.5 |
| wlen_autocorr1 | -0.45 | 0.103 | +0.5 |
| rep_within3 | -0.42 | 0.026 | -0.5 |
| top10_coverage | -0.30 | 0.171 | -0.4 |
| hapax_ratio | -0.30 | 0.717 | +0.5 |

### v101: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | +0.95 | 0.006 | -0.5 |
| char_double_rate | -0.90 | 0.015 | -0.8 |
| wlen_skew | +0.44 | 0.225 | -0.4 |
| wlen_autocorr1 | -0.34 | 0.179 | +1.0 |
| hapax_ratio | -0.34 | 0.741 | +0.6 |
| top10_coverage | -0.24 | 0.166 | -0.4 |

### zl_basic: tahmin `slotcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -0.90 | 0.008 | -0.4 |
| wlen_autocorr1 | +0.42 | 0.123 | +0.6 |
| h3 | +0.37 | 1.692 | -1.0 |
| wlen_skew | +0.27 | 0.025 | -0.8 |
| rep_within3 | -0.26 | 0.027 | -0.4 |
| rep_adjacent_ed1 | +0.22 | 0.034 | -0.4 |

### zl_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | +0.84 | 0.008 | -0.4 |
| wlen_skew | +0.75 | 0.154 | -0.6 |
| rep_within3 | -0.46 | 0.027 | -0.4 |
| wlen_autocorr1 | -0.32 | 0.102 | +0.5 |
| hapax_ratio | -0.29 | 0.715 | +0.5 |
| top10_coverage | -0.27 | 0.175 | -0.3 |
