# Voynich süreç sınıflandırma raporu

Pencere boyutu: 2000 kelime.

## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)

Doğruluk: **0.977**

| gerçek \ tahmin | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|
| abjad | 447 | 0 | 3 | 3 | 3 |
| grille | 3 | 523 | 0 | 2 | 0 |
| plain | 2 | 11 | 498 | 0 | 17 |
| selfcite | 0 | 5 | 0 | 522 | 1 |
| verbose | 3 | 0 | 5 | 0 | 520 |

## 2. Voynich hangi sürece benziyor

| görünüm | pencere | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|---|
| eva_basic | 16 | 0.00 | 0.09 | 0.00 | 0.30 | 0.61 |
| eva_glyph | 16 | 0.00 | 0.60 | 0.00 | 0.31 | 0.08 |
| v101 | 17 | 0.00 | 0.82 | 0.02 | 0.14 | 0.01 |
| zl_basic | 16 | 0.00 | 0.03 | 0.00 | 0.22 | 0.75 |
| zl_glyph | 16 | 0.00 | 0.46 | 0.00 | 0.32 | 0.23 |

## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)

Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "en az kötü eşleşme"dir, bulgu değil.

| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |
|---|---|---|---|
| eva_basic | verbose: 15, grille: 1 | 98 | 1.6x |
| eva_glyph | grille: 12, verbose: 4 | 94 | 1.5x |
| v101 | grille: 17 | 95 | 1.5x |
| zl_basic | verbose: 14, grille: 2 | 98 | 1.5x |
| zl_glyph | grille: 11, verbose: 5 | 94 | 1.4x |

### eva_basic: tahmin `verbose`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| h3 | +1.29 | 1.694 | -1.4 |
| h2 | +0.79 | 2.016 | -1.9 |
| wlen_skew | -0.50 | 0.074 | -1.0 |
| zipf_slope | -0.49 | -0.778 | +0.1 |
| wlen_frac1 | -0.48 | 0.017 | -0.8 |
| h2_over_h1 | +0.36 | 0.524 | -1.9 |

### eva_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_skew | +1.35 | 0.183 | -0.8 |
| wlen_std | -0.85 | 1.552 | -0.5 |
| h2 | +0.83 | 2.131 | -1.6 |
| vocab_ed1_density | -0.58 | 0.850 | +0.6 |
| rep_adjacent_exact | +0.27 | 0.009 | -0.2 |
| wlen_autocorr1 | -0.23 | 0.103 | +0.6 |

### v101: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_skew | +0.97 | 0.225 | -0.7 |
| h2 | +0.70 | 2.383 | -1.0 |
| vocab_ed1_density | -0.52 | 0.854 | +0.6 |
| rep_adjacent_exact | +0.40 | 0.006 | -0.3 |
| wlen_autocorr1 | -0.32 | 0.179 | +1.0 |
| wlen_std | +0.25 | 1.469 | -0.6 |

### zl_basic: tahmin `verbose`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| h3 | +1.33 | 1.692 | -1.4 |
| h2 | +0.88 | 2.013 | -1.9 |
| wlen_skew | -0.52 | 0.025 | -1.1 |
| zipf_slope | -0.46 | -0.785 | +0.0 |
| wlen_frac1 | -0.40 | 0.033 | -0.6 |
| h2_over_h1 | +0.37 | 0.521 | -1.9 |

### zl_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_std | -1.70 | 1.615 | -0.5 |
| wlen_skew | +1.57 | 0.154 | -0.8 |
| h2 | +0.77 | 2.127 | -1.6 |
| vocab_ed1_density | -0.61 | 0.852 | +0.6 |
| rep_adjacent_exact | +0.27 | 0.008 | -0.2 |
| wlen_autocorr1 | -0.20 | 0.102 | +0.6 |
