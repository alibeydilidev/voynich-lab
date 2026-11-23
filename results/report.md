# Voynich süreç sınıflandırma raporu

Pencere boyutu: 2000 kelime.

## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)

Doğruluk: **0.981**

| gerçek \ tahmin | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|
| abjad | 452 | 0 | 3 | 1 | 0 |
| grille | 1 | 524 | 2 | 1 | 0 |
| plain | 4 | 7 | 500 | 0 | 17 |
| selfcite | 0 | 4 | 0 | 524 | 0 |
| verbose | 2 | 0 | 6 | 0 | 520 |

## 2. Voynich hangi sürece benziyor

| görünüm | pencere | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|---|
| eva_basic | 16 | 0.00 | 0.49 | 0.01 | 0.50 | 0.01 |
| eva_glyph | 16 | 0.00 | 0.74 | 0.00 | 0.25 | 0.00 |
| v101 | 17 | 0.00 | 0.83 | 0.01 | 0.16 | 0.00 |

## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)

Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "en az kötü eşleşme"dir, bulgu değil.

| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |
|---|---|---|---|
| eva_basic | grille: 14, verbose: 2 | 99 | 1.8x |
| eva_glyph | grille: 16 | 95 | 1.4x |
| v101 | grille: 17 | 96 | 1.5x |

### eva_basic: tahmin `selfcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_autocorr1 | +2.27 | 0.127 | +0.8 |
| rep_adjacent_exact | -1.63 | 0.009 | -0.2 |
| h2 | -0.33 | 2.016 | -2.0 |
| char_double_rate | -0.22 | 0.067 | -0.2 |
| rep_within3 | -0.18 | 0.026 | -0.3 |
| top1_freq | -0.15 | 0.034 | -0.5 |

### eva_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_skew | +1.51 | 0.183 | -0.8 |
| h2 | +0.93 | 2.131 | -1.7 |
| wlen_autocorr1 | -0.64 | 0.103 | +0.6 |
| rep_adjacent_exact | +0.48 | 0.009 | -0.2 |
| wlen_std | -0.30 | 1.552 | -0.6 |
| vocab_ed1_density | -0.23 | 0.850 | +0.7 |

### v101: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_skew | +1.21 | 0.225 | -0.7 |
| h2 | +0.79 | 2.383 | -1.1 |
| wlen_autocorr1 | -0.69 | 0.179 | +1.1 |
| rep_adjacent_exact | +0.64 | 0.006 | -0.3 |
| wlen_std | +0.52 | 1.469 | -0.7 |
| vocab_ed1_density | -0.23 | 0.854 | +0.7 |
