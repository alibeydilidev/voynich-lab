# Voynich süreç sınıflandırma raporu

Pencere boyutu: 2000 kelime.

## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)

Doğruluk: **0.917**

| gerçek \ tahmin | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| abjad | 423 | 0 | 0 | 2 | 0 | 0 | 26 | 5 |
| codebook | 0 | 510 | 9 | 0 | 0 | 0 | 9 | 0 |
| grille | 2 | 5 | 491 | 0 | 0 | 14 | 16 | 0 |
| plain | 2 | 0 | 3 | 490 | 0 | 1 | 3 | 29 |
| selfcite | 1 | 0 | 0 | 0 | 500 | 24 | 3 | 0 |
| slotcite | 0 | 0 | 16 | 0 | 15 | 464 | 32 | 1 |
| slotgram | 5 | 4 | 37 | 0 | 12 | 48 | 420 | 2 |
| verbose | 1 | 0 | 10 | 4 | 0 | 0 | 3 | 510 |

## 2. Voynich hangi sürece benziyor

| görünüm | pencere | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 16 | 0.00 | 0.00 | 0.33 | 0.00 | 0.00 | 0.40 | 0.27 | 0.00 |
| eva_glyph | 16 | 0.00 | 0.00 | 0.33 | 0.00 | 0.00 | 0.25 | 0.41 | 0.00 |
| v101 | 17 | 0.00 | 0.00 | 0.33 | 0.00 | 0.01 | 0.12 | 0.53 | 0.01 |
| zl_basic | 16 | 0.00 | 0.00 | 0.48 | 0.00 | 0.00 | 0.26 | 0.25 | 0.01 |
| zl_glyph | 16 | 0.00 | 0.00 | 0.46 | 0.00 | 0.00 | 0.20 | 0.34 | 0.00 |

## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)

Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "en az kötü eşleşme"dir, bulgu değil.

| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |
|---|---|---|---|
| eva_basic | slotgram: 16 | 56 | 1.0x |
| eva_glyph | slotgram: 16 | 44 | 1.0x |
| v101 | slotcite: 11, slotgram: 5, grille: 1 | 84 | 1.2x |
| zl_basic | slotgram: 16 | 51 | 1.0x |
| zl_glyph | slotgram: 15, grille: 1 | 38 | 0.9x |

### eva_basic: tahmin `slotcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -1.15 | 0.009 | -0.4 |
| h3 | +0.39 | 1.694 | -1.0 |
| wlen_autocorr1 | +0.37 | 0.127 | +0.7 |
| rep_adjacent_ed1 | +0.28 | 0.032 | -0.5 |
| rep_within3 | -0.23 | 0.026 | -0.4 |
| jsd_last | -0.21 | 0.719 | +0.8 |

### eva_glyph: tahmin `slotgram`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| h2 | +1.25 | 2.131 | -1.1 |
| h3 | -0.64 | 1.818 | -0.6 |
| wlen_frac1 | -0.55 | 0.017 | -0.6 |
| h2_over_h1 | +0.34 | 0.556 | -1.2 |
| char_double_rate | -0.28 | 0.076 | +0.1 |
| zipf_slope | -0.25 | -0.778 | +0.1 |

### v101: tahmin `slotgram`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| n_symbols | -0.57 | 69.529 | +1.2 |
| char_double_rate | +0.33 | 0.015 | -0.8 |
| h1 | -0.27 | 4.005 | +0.1 |
| wlen_frac1 | -0.26 | 0.046 | -0.4 |
| h2_over_h1 | +0.26 | 0.595 | -0.8 |
| zipf_slope | -0.23 | -0.776 | +0.1 |

### zl_basic: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| hapax_ratio | -0.77 | 0.715 | +0.5 |
| wlen_skew | +0.59 | 0.025 | -0.4 |
| rep_adjacent_exact | +0.58 | 0.008 | -0.4 |
| h3 | +0.49 | 1.692 | -1.0 |
| wlen_autocorr1 | -0.46 | 0.123 | +0.7 |
| rep_within3 | -0.42 | 0.027 | -0.4 |

### zl_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| hapax_ratio | -0.78 | 0.715 | +0.5 |
| rep_adjacent_exact | +0.57 | 0.008 | -0.4 |
| wlen_skew | +0.54 | 0.154 | -0.3 |
| h3 | +0.46 | 1.817 | -0.6 |
| rep_within3 | -0.44 | 0.027 | -0.4 |
| wlen_autocorr1 | -0.40 | 0.102 | +0.5 |
