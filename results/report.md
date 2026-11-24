# Voynich süreç sınıflandırma raporu

Pencere boyutu: 2000 kelime.

## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)

Doğruluk: **0.927**

| gerçek \ tahmin | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|
| abjad | 431 | 0 | 0 | 1 | 2 | 0 | 0 | 18 | 4 |
| automaton | 0 | 521 | 1 | 1 | 0 | 0 | 0 | 4 | 1 |
| codebook | 0 | 0 | 507 | 7 | 0 | 0 | 0 | 14 | 0 |
| grille | 2 | 1 | 5 | 489 | 0 | 0 | 12 | 17 | 2 |
| plain | 2 | 1 | 0 | 3 | 494 | 0 | 1 | 0 | 27 |
| selfcite | 1 | 0 | 0 | 0 | 0 | 499 | 25 | 3 | 0 |
| slotcite | 0 | 1 | 0 | 15 | 0 | 19 | 464 | 29 | 0 |
| slotgram | 5 | 10 | 1 | 31 | 0 | 11 | 48 | 422 | 0 |
| verbose | 0 | 0 | 0 | 7 | 6 | 0 | 0 | 4 | 511 |

## 2. Voynich hangi sürece benziyor

| görünüm | pencere | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 16 | 0.00 | 0.00 | 0.00 | 0.72 | 0.00 | 0.00 | 0.18 | 0.04 | 0.05 |
| eva_glyph | 16 | 0.00 | 0.00 | 0.00 | 0.78 | 0.00 | 0.00 | 0.10 | 0.08 | 0.03 |
| v101 | 17 | 0.00 | 0.01 | 0.01 | 0.54 | 0.01 | 0.02 | 0.13 | 0.15 | 0.14 |
| zl_basic | 16 | 0.00 | 0.00 | 0.00 | 0.78 | 0.00 | 0.00 | 0.13 | 0.04 | 0.04 |
| zl_glyph | 16 | 0.00 | 0.00 | 0.00 | 0.84 | 0.00 | 0.00 | 0.07 | 0.06 | 0.03 |

## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)

Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "en az kötü eşleşme"dir, bulgu değil.

| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |
|---|---|---|---|
| eva_basic | verbose: 14, grille: 2 | 98 | 1.6x |
| eva_glyph | verbose: 11, grille: 5 | 98 | 1.5x |
| v101 | verbose: 10, grille: 7 | 99 | 1.6x |
| zl_basic | verbose: 12, grille: 4 | 98 | 1.5x |
| zl_glyph | verbose: 9, grille: 7 | 96 | 1.5x |

### eva_basic: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| hapax_ratio | -0.72 | 0.717 | +0.5 |
| wlen_skew | +0.67 | 0.074 | -0.4 |
| edge_mi | +0.57 | 0.179 | +1.5 |
| h3 | +0.55 | 1.694 | -0.8 |
| wlen_autocorr1 | -0.51 | 0.127 | +0.8 |
| h2 | -0.50 | 2.016 | -1.0 |

### eva_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| hapax_ratio | -0.73 | 0.717 | +0.5 |
| wlen_skew | +0.62 | 0.183 | -0.3 |
| edge_mi | +0.55 | 0.187 | +1.6 |
| wlen_autocorr1 | -0.48 | 0.103 | +0.6 |
| h3 | +0.47 | 1.818 | -0.5 |
| h2 | -0.39 | 2.131 | -0.8 |

### v101: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| char_double_rate | -0.88 | 0.015 | -0.7 |
| hapax_ratio | -0.82 | 0.741 | +0.6 |
| wlen_autocorr1 | -0.56 | 0.179 | +1.1 |
| wlen_skew | +0.45 | 0.225 | -0.2 |
| rep_adjacent_exact | +0.36 | 0.006 | -0.4 |
| edge_mi | +0.35 | 0.228 | +2.1 |

### zl_basic: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_skew | +0.68 | 0.025 | -0.4 |
| hapax_ratio | -0.64 | 0.715 | +0.4 |
| edge_mi | +0.54 | 0.192 | +1.7 |
| h3 | +0.54 | 1.692 | -0.8 |
| h2 | -0.46 | 2.013 | -1.0 |
| wlen_autocorr1 | -0.46 | 0.123 | +0.7 |

### zl_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_skew | +0.66 | 0.154 | -0.3 |
| hapax_ratio | -0.62 | 0.715 | +0.4 |
| edge_mi | +0.52 | 0.199 | +1.8 |
| h3 | +0.49 | 1.817 | -0.5 |
| rep_adjacent_exact | +0.43 | 0.008 | -0.4 |
| wlen_autocorr1 | -0.40 | 0.102 | +0.6 |
