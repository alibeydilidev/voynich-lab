# Voynich süreç sınıflandırma raporu

Pencere boyutu: 2000 kelime.

## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)

Doğruluk: **0.924**

| gerçek \ tahmin | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|
| abjad | 421 | 0 | 0 | 0 | 3 | 0 | 0 | 27 | 5 |
| automaton | 0 | 521 | 0 | 1 | 0 | 0 | 0 | 5 | 1 |
| codebook | 0 | 0 | 508 | 8 | 0 | 0 | 0 | 12 | 0 |
| grille | 1 | 1 | 4 | 494 | 0 | 0 | 14 | 14 | 0 |
| plain | 1 | 2 | 0 | 3 | 492 | 0 | 1 | 1 | 28 |
| selfcite | 0 | 0 | 0 | 0 | 0 | 501 | 25 | 2 | 0 |
| slotcite | 0 | 0 | 0 | 17 | 0 | 19 | 462 | 28 | 2 |
| slotgram | 5 | 12 | 3 | 36 | 0 | 12 | 43 | 415 | 2 |
| verbose | 1 | 0 | 0 | 10 | 3 | 0 | 0 | 3 | 511 |

## 2. Voynich hangi sürece benziyor

| görünüm | pencere | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 16 | 0.00 | 0.00 | 0.00 | 0.30 | 0.00 | 0.00 | 0.47 | 0.22 | 0.00 |
| eva_glyph | 16 | 0.00 | 0.00 | 0.00 | 0.33 | 0.00 | 0.00 | 0.33 | 0.33 | 0.00 |
| v101 | 17 | 0.00 | 0.00 | 0.00 | 0.29 | 0.00 | 0.02 | 0.15 | 0.54 | 0.01 |
| zl_basic | 16 | 0.00 | 0.00 | 0.00 | 0.45 | 0.00 | 0.00 | 0.33 | 0.21 | 0.00 |
| zl_glyph | 16 | 0.00 | 0.00 | 0.00 | 0.45 | 0.00 | 0.00 | 0.26 | 0.28 | 0.00 |

## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)

Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "en az kötü eşleşme"dir, bulgu değil.

| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |
|---|---|---|---|
| eva_basic | slotgram: 16 | 57 | 1.0x |
| eva_glyph | slotgram: 16 | 45 | 1.0x |
| v101 | slotcite: 12, slotgram: 4, grille: 1 | 86 | 1.3x |
| zl_basic | slotgram: 16 | 52 | 1.0x |
| zl_glyph | slotgram: 15, grille: 1 | 38 | 0.9x |

### eva_basic: tahmin `slotcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -1.22 | 0.009 | -0.4 |
| wlen_autocorr1 | +0.56 | 0.127 | +0.8 |
| h3 | +0.40 | 1.694 | -0.8 |
| rep_within3 | -0.27 | 0.026 | -0.4 |
| rep_adjacent_ed1 | +0.23 | 0.032 | -0.5 |
| char_double_rate | +0.21 | 0.067 | +0.1 |

### eva_glyph: tahmin `slotgram`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| h2 | +1.03 | 2.131 | -0.8 |
| h3 | -0.65 | 1.818 | -0.5 |
| wlen_frac1 | -0.47 | 0.017 | -0.6 |
| h2_over_h1 | +0.29 | 0.556 | -0.7 |
| zipf_slope | -0.22 | -0.778 | +0.1 |
| char_double_rate | -0.19 | 0.076 | +0.2 |

### v101: tahmin `slotgram`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| n_symbols | -0.56 | 69.529 | +1.2 |
| h1 | -0.28 | 4.005 | +0.1 |
| h2 | +0.27 | 2.383 | -0.3 |
| char_double_rate | +0.27 | 0.015 | -0.7 |
| h3 | -0.26 | 2.015 | +0.1 |
| h2_over_h1 | +0.22 | 0.595 | -0.4 |

### zl_basic: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| hapax_ratio | -0.82 | 0.715 | +0.4 |
| wlen_skew | +0.60 | 0.025 | -0.4 |
| rep_adjacent_exact | +0.52 | 0.008 | -0.4 |
| h3 | +0.50 | 1.692 | -0.8 |
| wlen_autocorr1 | -0.46 | 0.123 | +0.7 |
| h2 | -0.43 | 2.013 | -1.0 |

### zl_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| hapax_ratio | -0.85 | 0.715 | +0.4 |
| wlen_skew | +0.57 | 0.154 | -0.3 |
| rep_adjacent_exact | +0.50 | 0.008 | -0.4 |
| h3 | +0.47 | 1.817 | -0.5 |
| wlen_autocorr1 | -0.40 | 0.102 | +0.6 |
| rep_within3 | -0.36 | 0.027 | -0.4 |
