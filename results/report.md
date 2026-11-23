# Voynich süreç sınıflandırma raporu

Pencere boyutu: 2000 kelime.

## 1. Model sentetik veride ne kadar iyi (dil bazlı gruplu CV)

Doğruluk: **0.995**

| gerçek \ tahmin | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|
| abjad | 452 | 4 | 0 | 0 | 0 |
| grille | 1 | 527 | 0 | 0 | 0 |
| plain | 1 | 1 | 524 | 0 | 2 |
| selfcite | 0 | 0 | 0 | 528 | 0 |
| verbose | 1 | 0 | 1 | 1 | 525 |

## 2. Voynich hangi sürece benziyor

| görünüm | pencere | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|---|
| eva_basic | 15 | 0.04 | 0.12 | 0.04 | 0.26 | 0.54 |
| eva_glyph | 15 | 0.06 | 0.13 | 0.30 | 0.17 | 0.34 |
| v101 | 17 | 0.04 | 0.13 | 0.31 | 0.34 | 0.18 |

## 3. Dağılım dışı kontrolü (asıl okunacak bölüm)

Yüzdelik 100'e yakınsa Voynich, en yakın sınıfın kendi örneklerinin tamamından uzakta demektir. O durumda bölüm 2'deki olasılıklar "en az kötü eşleşme"dir, bulgu değil.

| görünüm | en yakın sınıf (mesafe) | medyan yüzdelik | mesafe / sınıf medyanı |
|---|---|---|---|
| eva_basic | verbose: 8, selfcite: 7 | 100 | 8.0x |
| eva_glyph | selfcite: 12, plain: 3 | 100 | 8.2x |
| v101 | selfcite: 10, plain: 7 | 100 | 9.0x |

### eva_basic: tahmin `verbose`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_std | -2.83 | 1.921 | -0.3 |
| h2 | +0.54 | 2.036 | -2.1 |
| h2_over_h1 | +0.46 | 0.526 | -3.0 |
| hapax_ratio | +0.36 | 0.726 | +0.9 |
| type_len_mean | -0.21 | 5.933 | +0.0 |
| vocab_ed1_density | -0.06 | 0.789 | +0.5 |

Sentetik aralığın dışına taşan feature'lar (pencere oranı): jsd_last (%100), jsd_line_initial (%100), jsd_line_final (%67), h2_over_h1 (%20), len_ratio_line_final (%20), h2 (%13)

### eva_glyph: tahmin `verbose`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| wlen_std | -2.99 | 1.762 | -0.4 |
| type_len_mean | -0.53 | 5.252 | -0.3 |
| h2 | +0.43 | 2.152 | -1.8 |
| h2_over_h1 | +0.39 | 0.558 | -2.6 |
| hapax_ratio | +0.38 | 0.726 | +0.9 |
| n_symbols | -0.20 | 26.200 | +0.9 |

Sentetik aralığın dışına taşan feature'lar (pencere oranı): jsd_last (%100), jsd_line_initial (%100), jsd_line_final (%67), h2_over_h1 (%20), len_ratio_line_final (%13)

### v101: tahmin `selfcite`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_exact | -1.99 | 0.006 | -0.3 |
| wlen_autocorr1 | +0.79 | 0.179 | +1.1 |
| top10_coverage | -0.12 | 0.166 | -0.5 |
| char_double_rate | -0.10 | 0.015 | -1.0 |
| wlen_frac1 | -0.10 | 0.046 | -0.3 |
| rep_within3 | -0.08 | 0.021 | -0.6 |

Sentetik aralığın dışına taşan feature'lar (pencere oranı): n_symbols (%100), jsd_last (%100), jsd_line_initial (%100), jsd_line_final (%82), len_ratio_line_initial (%18)
