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
| eva_basic | 15 | 0.05 | 0.16 | 0.05 | 0.25 | 0.50 |
| eva_glyph | 15 | 0.06 | 0.16 | 0.35 | 0.17 | 0.26 |
| v101 | 17 | 0.04 | 0.15 | 0.40 | 0.27 | 0.14 |

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
| wlen_std | -2.93 | 1.921 | -0.3 |
| h2 | +0.49 | 2.036 | -2.1 |
| h2_over_h1 | +0.43 | 0.526 | -3.0 |
| hapax_ratio | +0.28 | 0.726 | +0.9 |
| type_len_mean | -0.19 | 5.933 | +0.0 |
| h3 | +0.07 | 1.706 | -1.3 |

Sentetik aralığın dışına taşan feature'lar (pencere oranı): jsd_last (%100), jsd_line_initial (%100), jsd_line_final (%67), h2_over_h1 (%20), len_ratio_line_final (%20), h2 (%13)

### eva_glyph: tahmin `plain`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| h1 | -1.37 | 3.856 | +0.3 |
| n_symbols | +1.31 | 26.200 | +0.9 |
| rep_adjacent_ed1 | -0.87 | 0.039 | -0.3 |
| vocab_ed1_density | -0.77 | 0.814 | +0.5 |
| h2 | -0.38 | 2.152 | -1.8 |
| h2_over_h1 | -0.26 | 0.558 | -2.6 |

Sentetik aralığın dışına taşan feature'lar (pencere oranı): jsd_last (%100), jsd_line_initial (%100), jsd_line_final (%67), h2_over_h1 (%20), len_ratio_line_final (%13)

### v101: tahmin `plain`, en etkili feature'lar

| feature | katkı | Voynich ort. | sentetik evrene göre z |
|---|---|---|---|
| rep_adjacent_ed1 | -1.91 | 0.043 | -0.2 |
| n_symbols | +1.19 | 69.529 | +8.5 |
| vocab_ed1_density | -0.81 | 0.854 | +0.7 |
| h1 | +0.69 | 4.005 | +0.8 |
| h2 | -0.66 | 2.383 | -1.2 |
| h2_over_h1 | -0.48 | 0.595 | -2.1 |

Sentetik aralığın dışına taşan feature'lar (pencere oranı): n_symbols (%100), jsd_last (%100), jsd_line_initial (%100), jsd_line_final (%82), len_ratio_line_initial (%18)
