# Voynich süreç sınıflandırma raporu

Pencere boyutu: 2000 kelime.

## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)

Doğruluk: **0.997**

| gerçek \ tahmin | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|
| abjad | 455 | 0 | 0 | 0 | 1 |
| grille | 1 | 527 | 0 | 0 | 0 |
| plain | 0 | 1 | 526 | 0 | 1 |
| selfcite | 0 | 0 | 0 | 528 | 0 |
| verbose | 2 | 0 | 1 | 0 | 525 |

## 2. Voynich hangi sürece benziyor

| görünüm | pencere | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|---|
| eva_basic | 16 | 0.04 | 0.54 | 0.05 | 0.29 | 0.08 |
| eva_glyph | 16 | 0.05 | 0.54 | 0.10 | 0.21 | 0.10 |
| v101 | 17 | 0.05 | 0.27 | 0.26 | 0.36 | 0.06 |

## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)

Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "en az kötü eşleşme"dir, bulgu değil.

| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |
|---|---|---|---|
| eva_basic | grille: 16 | 100 | 2.3x |
| eva_glyph | grille: 16 | 100 | 2.1x |
| v101 | plain: 9, grille: 8 | 100 | 5.0x |

### eva_basic: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| hapax_ratio | -2.62 | 0.717 | +0.7 |
| wlen_skew | +1.19 | 0.074 | -1.2 |
| wlen_std | -0.38 | 1.693 | -0.5 |
| ttr | -0.14 | 0.443 | +0.4 |
| h2 | +0.12 | 2.016 | -2.3 |
| first_entropy_ratio | +0.11 | 0.806 | -1.4 |

Sentetik aralığın dışına taşan feature'lar (pencere oranı): jsd_last (%100), h2_over_h1 (%31), h2 (%25)

### eva_glyph: tahmin `grille`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| hapax_ratio | -2.73 | 0.717 | +0.7 |
| wlen_skew | +0.99 | 0.183 | -1.0 |
| wlen_std | -0.19 | 1.552 | -0.6 |
| ttr | -0.14 | 0.443 | +0.4 |
| h2 | +0.11 | 2.131 | -2.0 |
| eff_symbols | -0.04 | 14.404 | -0.1 |

Sentetik aralığın dışına taşan feature'lar (pencere oranı): jsd_last (%100), h2 (%12), h2_over_h1 (%12)

### v101: tahmin `selfcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -1.50 | 0.006 | -0.3 |
| wlen_autocorr1 | +0.79 | 0.179 | +0.8 |
| top10_coverage | -0.44 | 0.166 | -0.3 |
| char_double_rate | -0.24 | 0.015 | -1.0 |
| wlen_frac1 | -0.13 | 0.046 | -0.3 |
| rep_within3 | -0.09 | 0.021 | -0.5 |

Sentetik aralığın dışına taşan feature'lar (pencere oranı): jsd_last (%100), n_symbols (%94)
