# Voynich süreç sınıflandırma raporu

Pencere boyutu: 2000 kelime.

## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)

Doğruluk: **0.922**

| gerçek \ tahmin | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|
| abjad | 419 | 0 | 0 | 1 | 2 | 0 | 0 | 28 | 6 |
| automaton | 0 | 518 | 0 | 2 | 0 | 0 | 0 | 6 | 2 |
| codebook | 0 | 0 | 507 | 9 | 0 | 0 | 0 | 12 | 0 |
| grille | 2 | 1 | 4 | 491 | 0 | 0 | 15 | 15 | 0 |
| plain | 1 | 1 | 0 | 3 | 492 | 0 | 1 | 1 | 29 |
| selfcite | 0 | 0 | 0 | 0 | 0 | 498 | 26 | 4 | 0 |
| slotcite | 0 | 0 | 0 | 15 | 0 | 20 | 462 | 30 | 1 |
| slotgram | 5 | 13 | 4 | 33 | 0 | 13 | 45 | 413 | 2 |
| verbose | 0 | 0 | 0 | 9 | 3 | 0 | 0 | 3 | 513 |

## 2. Voynich hangi sürece benziyor

| görünüm | pencere | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 16 | 0.00 | 0.00 | 0.00 | 0.29 | 0.00 | 0.00 | 0.49 | 0.22 | 0.00 |
| eva_glyph | 16 | 0.00 | 0.00 | 0.00 | 0.32 | 0.00 | 0.00 | 0.37 | 0.30 | 0.00 |
| v101 | 17 | 0.00 | 0.00 | 0.00 | 0.26 | 0.00 | 0.01 | 0.12 | 0.60 | 0.01 |
| zl_basic | 16 | 0.00 | 0.00 | 0.00 | 0.44 | 0.00 | 0.00 | 0.36 | 0.20 | 0.00 |
| zl_glyph | 16 | 0.00 | 0.00 | 0.00 | 0.44 | 0.00 | 0.00 | 0.31 | 0.25 | 0.00 |

## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)

Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "en az kötü eşleşme"dir, bulgu değil.

| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |
|---|---|---|---|
| eva_basic | slotgram: 16 | 58 | 1.1x |
| eva_glyph | slotgram: 15, grille: 1 | 45 | 1.0x |
| v101 | slotcite: 12, slotgram: 4, grille: 1 | 86 | 1.3x |
| zl_basic | slotgram: 16 | 52 | 1.0x |
| zl_glyph | slotgram: 15, grille: 1 | 39 | 0.9x |

### eva_basic: tahmin `slotcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -1.17 | 0.009 | -0.3 |
| wlen_autocorr1 | +0.63 | 0.127 | +0.8 |
| h3 | +0.45 | 1.694 | -0.8 |
| rep_within3 | -0.23 | 0.026 | -0.4 |
| char_double_rate | +0.19 | 0.067 | +0.1 |
| jsd_last | -0.19 | 0.719 | +0.8 |

### eva_glyph: tahmin `slotcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -1.14 | 0.009 | -0.3 |
| wlen_autocorr1 | +0.62 | 0.103 | +0.6 |
| h3 | +0.29 | 1.818 | -0.5 |
| rep_within3 | -0.24 | 0.026 | -0.4 |
| char_double_rate | +0.19 | 0.076 | +0.2 |
| jsd_last | -0.19 | 0.718 | +0.8 |

### v101: tahmin `slotgram`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| n_symbols | -0.48 | 69.529 | +1.2 |
| char_double_rate | +0.32 | 0.015 | -0.7 |
| h2 | +0.27 | 2.383 | -0.3 |
| h3 | -0.25 | 2.015 | +0.1 |
| h1 | -0.24 | 4.005 | +0.1 |
| rep_adjacent_exact | -0.22 | 0.006 | -0.4 |

### zl_basic: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| hapax_ratio | -0.71 | 0.715 | +0.5 |
| wlen_skew | +0.58 | 0.025 | -0.4 |
| h3 | +0.50 | 1.692 | -0.8 |
| rep_adjacent_exact | +0.50 | 0.008 | -0.4 |
| wlen_autocorr1 | -0.44 | 0.123 | +0.7 |
| h2 | -0.41 | 2.013 | -1.0 |

### zl_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| hapax_ratio | -0.72 | 0.715 | +0.5 |
| wlen_skew | +0.58 | 0.154 | -0.3 |
| rep_adjacent_exact | +0.49 | 0.008 | -0.4 |
| h3 | +0.47 | 1.817 | -0.5 |
| wlen_autocorr1 | -0.38 | 0.102 | +0.6 |
| char_double_rate | +0.30 | 0.076 | +0.2 |
