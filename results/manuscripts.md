# El yazması düzeyinde karşılaştırma

Her sınıftan önselden 2000 el yazması üretildi; her biri tek tablo ve tek ayar kümesiyle 16 pencere (8 seçim + 8 doğrulama). Her sınıfta seçim yarısına göre Voynich'e en yakın 20 aday seçildi; tablolar bu adayların DOĞRULAMA yarısındaki değerlerini verir.

T yaklaşık 1 ise adayın ortalama profili Voynich'ten ayırt edilemez. Referans, Voynich'in kendi yarılarının birbirine karşı T değeridir: rastgele bölmelerde beklenen düzey ve ardışık bölmede (ilk yarı ile son yarı) gerçekte olan.

## 1. Seçilen adayların doğrulama yarısında medyan T (parantezde seçim yarısındaki değer)

| görünüm | Voynich: rastgele medyan, %95, ardışık | abjad | grille | plain | selfcite | slotcite | verbose |
|---|---|---|---|---|---|---|---|
| eva_basic | 0.89, 1.49, 1.70 | 14.3 (14.5) | 6.6 (6.6) | 12.3 (12.4) | 10.5 (10.5) | 6.7 (6.9) | 8.9 (8.7) |
| eva_glyph | 0.89, 1.55, 1.71 | 9.3 (9.4) | 5.9 (5.8) | 10.1 (10.2) | 8.8 (8.6) | 6.0 (6.0) | 8.2 (8.3) |
| v101 | 0.90, 1.53, 1.44 | 7.6 (7.6) | 6.0 (6.0) | 7.3 (7.3) | 9.6 (9.3) | 6.9 (6.8) | 7.7 (7.6) |
| zl_basic | 0.90, 1.54, 1.54 | 12.8 (12.7) | 5.6 (5.6) | 11.3 (11.1) | 9.1 (9.2) | 6.0 (6.1) | 7.5 (7.4) |
| zl_glyph | 0.90, 1.55, 1.66 | 8.4 (8.4) | 5.1 (5.1) | 9.2 (9.3) | 7.4 (7.2) | 5.2 (5.3) | 6.6 (6.7) |

## 2. Doğrulama yarısında en iyi tek aday (T)

| görünüm | abjad | grille | plain | selfcite | slotcite | verbose |
|---|---|---|---|---|---|---|
| eva_basic | 12.8 | 5.2 | 8.9 | 7.5 | 5.2 | 8.0 |
| eva_glyph | 8.1 | 4.3 | 6.1 | 6.7 | 4.9 | 6.9 |
| v101 | 6.0 | 5.2 | 5.4 | 7.9 | 5.4 | 6.0 |
| zl_basic | 11.3 | 4.9 | 8.3 | 6.9 | 4.6 | 6.0 |
| zl_glyph | 7.2 | 4.4 | 6.1 | 5.6 | 4.7 | 5.4 |

## 3. Aynı ayar, yeni tablo: seçilen ayarlar yeni tohumla yeniden üretilince medyan T

| görünüm | abjad | grille | plain | selfcite | slotcite | verbose |
|---|---|---|---|---|---|---|
| eva_basic | 14.4 | 8.6 | 10.6 | 10.1 | 8.0 | 10.1 |
| eva_glyph | 9.2 | 7.5 | 8.0 | 7.9 | 7.0 | 9.3 |
| v101 | 7.1 | 8.5 | 7.0 | 9.3 | 7.9 | 8.5 |
| zl_basic | 12.9 | 7.3 | 9.6 | 8.4 | 7.0 | 8.6 |
| zl_glyph | 8.3 | 6.9 | 7.5 | 6.5 | 6.3 | 6.8 |

## 4. İç değişkenlik: seçilen adayların yayılım oranı (Voynich = 1)

| görünüm | abjad | grille | plain | selfcite | slotcite | verbose |
|---|---|---|---|---|---|---|
| eva_basic | 0.60 | 0.16 | 0.50 | 0.94 | 0.39 | 0.41 |
| eva_glyph | 0.51 | 0.15 | 0.40 | 0.87 | 0.36 | 0.36 |
| v101 | 0.54 | 0.17 | 0.46 | 0.83 | 0.41 | 0.44 |
| zl_basic | 0.56 | 0.15 | 0.45 | 0.85 | 0.44 | 0.38 |
| zl_glyph | 0.47 | 0.15 | 0.38 | 0.74 | 0.37 | 0.34 |

## eva_basic: sınıf sınıf

### grille: doğrulama medyan T 6.6, en iyi 5.2

Standart hatanın 2 katından fazla sapan feature sayısı: 18 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| h2_over_h1 | +7.6 | 0.524 | 0.626 |
| hapax_ratio | -7.2 | 0.717 | 0.648 |
| h2 | +7.1 | 2.016 | 2.385 |
| vocab_ed1_density | +6.5 | 0.823 | 0.893 |
| wlen_autocorr1 | -6.5 | 0.127 | 0.020 |
| rep_adjacent_ed1 | -5.6 | 0.032 | 0.016 |

### slotcite: doğrulama medyan T 6.7, en iyi 5.2

Standart hatanın 2 katından fazla sapan feature sayısı: 21 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -10.3 | 0.717 | 0.618 |
| rep_adjacent_exact | +8.0 | 0.009 | 0.019 |
| h2_over_h1 | +7.0 | 0.524 | 0.618 |
| h2 | +6.9 | 2.016 | 2.375 |
| jsd_line_final | -6.9 | 0.109 | 0.013 |
| vocab_ed1_density | +6.8 | 0.823 | 0.897 |

### verbose: doğrulama medyan T 8.9, en iyi 8.0

Standart hatanın 2 katından fazla sapan feature sayısı: 27 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -22.0 | 0.717 | 0.505 |
| wlen_frac_le2 | +13.9 | 0.077 | 0.146 |
| wlen_std | +11.1 | 1.693 | 2.045 |
| wlen_skew | +9.9 | 0.074 | 0.627 |
| wlen_autocorr1 | -9.8 | 0.127 | -0.035 |
| ttr | -9.3 | 0.443 | 0.223 |

### selfcite: doğrulama medyan T 10.5, en iyi 7.5

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| h2 | +15.3 | 2.016 | 2.816 |
| h2_over_h1 | +15.2 | 0.524 | 0.729 |
| first_entropy_ratio | +15.0 | 0.806 | 0.923 |
| char_double_rate | +14.7 | 0.067 | 0.154 |
| hapax_ratio | -12.5 | 0.717 | 0.597 |
| jsd_first | -11.0 | 0.385 | 0.223 |

### plain: doğrulama medyan T 12.3, en iyi 8.9

Standart hatanın 2 katından fazla sapan feature sayısı: 30 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| eff_symbols | +22.1 | 14.240 | 17.468 |
| h1 | +20.7 | 3.845 | 4.055 |
| vocab_ed1_density | -20.1 | 0.823 | 0.607 |
| h2 | +17.8 | 2.016 | 2.944 |
| first_entropy_ratio | +17.5 | 0.806 | 0.942 |
| wlen_skew | +17.5 | 0.074 | 1.051 |

### abjad: doğrulama medyan T 14.3, en iyi 12.8

Standart hatanın 2 katından fazla sapan feature sayısı: 26 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_frac_le2 | +51.3 | 0.077 | 0.334 |
| first_entropy_ratio | +22.0 | 0.806 | 0.977 |
| wlen_frac1 | +20.3 | 0.017 | 0.115 |
| h2_over_h1 | +17.5 | 0.524 | 0.760 |
| type_len_mean | -17.3 | 5.692 | 4.416 |
| wlen_mean | -16.5 | 5.066 | 3.411 |


## eva_glyph: sınıf sınıf

### grille: doğrulama medyan T 5.9, en iyi 4.3

Standart hatanın 2 katından fazla sapan feature sayısı: 20 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_autocorr1 | -6.7 | 0.103 | 0.007 |
| hapax_ratio | -6.0 | 0.717 | 0.659 |
| rep_within3 | -5.6 | 0.026 | 0.009 |
| vocab_ed1_density | +5.3 | 0.850 | 0.901 |
| wlen_skew | -5.2 | 0.183 | -0.055 |
| rep_adjacent_ed1 | -5.1 | 0.039 | 0.017 |

### slotcite: doğrulama medyan T 6.0, en iyi 4.9

Standart hatanın 2 katından fazla sapan feature sayısı: 15 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -9.7 | 0.717 | 0.624 |
| rep_adjacent_exact | +8.2 | 0.009 | 0.020 |
| vocab_ed1_density | +6.9 | 0.850 | 0.916 |
| jsd_line_final | -6.8 | 0.110 | 0.017 |
| zipf_slope | +5.5 | -0.778 | -0.629 |
| wlen_skew | -5.3 | 0.183 | -0.062 |

### verbose: doğrulama medyan T 8.2, en iyi 6.9

Standart hatanın 2 katından fazla sapan feature sayısı: 27 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -19.5 | 0.717 | 0.529 |
| wlen_std | +13.8 | 1.552 | 1.866 |
| jsd_last | -13.6 | 0.718 | 0.437 |
| wlen_autocorr1 | -9.8 | 0.103 | -0.038 |
| ttr | -8.7 | 0.443 | 0.238 |
| wlen_skew | +8.4 | 0.183 | 0.568 |

### selfcite: doğrulama medyan T 8.8, en iyi 6.7

Standart hatanın 2 katından fazla sapan feature sayısı: 26 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -14.5 | 0.717 | 0.578 |
| rep_adjacent_exact | +11.8 | 0.009 | 0.024 |
| h2 | +10.7 | 2.131 | 2.853 |
| h2_over_h1 | +10.5 | 0.556 | 0.727 |
| char_double_rate | +7.8 | 0.076 | 0.125 |
| h1 | +7.5 | 3.832 | 3.921 |

### abjad: doğrulama medyan T 9.3, en iyi 8.1

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_frac1 | +19.4 | 0.017 | 0.115 |
| wlen_frac_le2 | +17.7 | 0.099 | 0.339 |
| h2_over_h1 | +12.5 | 0.556 | 0.760 |
| wlen_skew | +12.4 | 0.183 | 0.751 |
| first_entropy_ratio | +11.4 | 0.867 | 0.977 |
| h2 | +10.4 | 2.131 | 2.833 |

### plain: doğrulama medyan T 10.1, en iyi 6.1

Standart hatanın 2 katından fazla sapan feature sayısı: 23 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| h1 | +22.9 | 3.832 | 4.103 |
| eff_symbols | +21.9 | 14.404 | 18.838 |
| jsd_last | -19.8 | 0.718 | 0.308 |
| h2 | +18.0 | 2.131 | 3.345 |
| h2_over_h1 | +15.6 | 0.556 | 0.810 |
| vocab_ed1_density | -15.1 | 0.850 | 0.705 |


## v101: sınıf sınıf

### grille: doğrulama medyan T 6.0, en iyi 5.2

Standart hatanın 2 katından fazla sapan feature sayısı: 17 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | +8.2 | 0.854 | 0.935 |
| hapax_ratio | -7.8 | 0.741 | 0.643 |
| n_symbols | -7.6 | 69.529 | 39.000 |
| wlen_autocorr1 | -7.1 | 0.179 | -0.003 |
| char_double_rate | +6.1 | 0.015 | 0.029 |
| rep_adjacent_ed1 | -5.1 | 0.043 | 0.027 |

### slotcite: doğrulama medyan T 6.9, en iyi 5.4

Standart hatanın 2 katından fazla sapan feature sayısı: 19 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| char_double_rate | +11.3 | 0.015 | 0.041 |
| rep_adjacent_exact | +10.6 | 0.006 | 0.016 |
| hapax_ratio | -8.0 | 0.741 | 0.640 |
| n_symbols | -7.1 | 69.529 | 40.875 |
| jsd_last | -6.9 | 0.679 | 0.528 |
| rep_within3 | +6.5 | 0.021 | 0.036 |

### plain: doğrulama medyan T 7.3, en iyi 5.4

Standart hatanın 2 katından fazla sapan feature sayısı: 19 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | -13.6 | 0.854 | 0.719 |
| h2 | +13.1 | 2.383 | 3.340 |
| jsd_last | -13.1 | 0.679 | 0.391 |
| h2_over_h1 | +11.9 | 0.595 | 0.807 |
| rep_adjacent_ed1 | -10.7 | 0.043 | 0.010 |
| wlen_frac1 | -10.5 | 0.046 | 0.000 |

### abjad: doğrulama medyan T 7.6, en iyi 6.0

Standart hatanın 2 katından fazla sapan feature sayısı: 22 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_frac1 | +13.8 | 0.046 | 0.107 |
| wlen_frac_le2 | +13.6 | 0.184 | 0.338 |
| vocab_ed1_density | -9.1 | 0.854 | 0.763 |
| h2 | +9.0 | 2.383 | 3.041 |
| n_symbols | -8.7 | 69.529 | 34.312 |
| h2_over_h1 | +8.7 | 0.595 | 0.749 |

### verbose: doğrulama medyan T 7.7, en iyi 6.0

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_std | +12.8 | 1.469 | 1.808 |
| jsd_last | -10.4 | 0.679 | 0.450 |
| wlen_frac1 | +9.3 | 0.046 | 0.087 |
| hapax_ratio | -9.3 | 0.741 | 0.623 |
| top10_coverage | +8.9 | 0.166 | 0.254 |
| type_len_mean | +8.7 | 4.440 | 4.893 |

### selfcite: doğrulama medyan T 9.6, en iyi 7.9

Standart hatanın 2 katından fazla sapan feature sayısı: 21 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| char_double_rate | +28.3 | 0.015 | 0.081 |
| rep_adjacent_exact | +19.5 | 0.006 | 0.024 |
| rep_within3 | +13.3 | 0.021 | 0.051 |
| h2 | +8.6 | 2.383 | 3.010 |
| hapax_ratio | -8.0 | 0.741 | 0.639 |
| h2_over_h1 | +7.9 | 0.595 | 0.737 |


## zl_basic: sınıf sınıf

### grille: doğrulama medyan T 5.6, en iyi 4.9

Standart hatanın 2 katından fazla sapan feature sayısı: 19 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| h2_over_h1 | +6.8 | 0.521 | 0.620 |
| wlen_autocorr1 | -6.4 | 0.123 | -0.007 |
| h2 | +6.2 | 2.013 | 2.385 |
| rep_adjacent_ed1 | -5.8 | 0.034 | 0.016 |
| vocab_ed1_density | +5.2 | 0.823 | 0.872 |
| rep_within3 | -5.1 | 0.027 | 0.010 |

### slotcite: doğrulama medyan T 6.0, en iyi 4.6

Standart hatanın 2 katından fazla sapan feature sayısı: 19 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| rep_adjacent_exact | +7.7 | 0.008 | 0.017 |
| h2 | +7.0 | 2.013 | 2.434 |
| h2_over_h1 | +6.9 | 0.521 | 0.622 |
| hapax_ratio | -5.6 | 0.715 | 0.636 |
| eff_symbols | +5.0 | 14.493 | 15.362 |
| jsd_line_final | -5.0 | 0.110 | 0.027 |

### verbose: doğrulama medyan T 7.5, en iyi 6.0

Standart hatanın 2 katından fazla sapan feature sayısı: 28 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -13.4 | 0.715 | 0.528 |
| wlen_skew | +12.3 | 0.025 | 0.567 |
| jsd_last | -10.2 | 0.712 | 0.511 |
| wlen_std | +10.0 | 1.768 | 2.031 |
| first_entropy_ratio | +7.7 | 0.817 | 0.874 |
| ttr | -7.6 | 0.434 | 0.232 |

### selfcite: doğrulama medyan T 9.1, en iyi 6.9

Standart hatanın 2 katından fazla sapan feature sayısı: 27 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| h2_over_h1 | +14.1 | 0.521 | 0.727 |
| first_entropy_ratio | +14.1 | 0.817 | 0.921 |
| h2 | +13.5 | 2.013 | 2.827 |
| char_double_rate | +13.3 | 0.066 | 0.152 |
| eff_symbols | +10.4 | 14.493 | 16.290 |
| jsd_first | -9.4 | 0.385 | 0.227 |

### plain: doğrulama medyan T 11.3, en iyi 8.3

Standart hatanın 2 katından fazla sapan feature sayısı: 24 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| eff_symbols | +20.6 | 14.493 | 18.069 |
| h2 | +16.8 | 2.013 | 3.022 |
| h1 | +15.8 | 3.862 | 4.088 |
| vocab_ed1_density | -14.8 | 0.823 | 0.685 |
| h2_over_h1 | +14.8 | 0.521 | 0.736 |
| wlen_std | -12.2 | 1.768 | 1.447 |

### abjad: doğrulama medyan T 12.8, en iyi 11.3

Standart hatanın 2 katından fazla sapan feature sayısı: 24 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_frac_le2 | +41.4 | 0.097 | 0.337 |
| first_entropy_ratio | +19.6 | 0.817 | 0.961 |
| wlen_frac1 | +17.8 | 0.033 | 0.112 |
| wlen_skew | +16.4 | 0.025 | 0.751 |
| h2_over_h1 | +16.0 | 0.521 | 0.755 |
| wlen_mean | -15.9 | 4.961 | 3.398 |


## zl_glyph: sınıf sınıf

### grille: doğrulama medyan T 5.1, en iyi 4.4

Standart hatanın 2 katından fazla sapan feature sayısı: 16 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | +7.1 | 0.852 | 0.901 |
| wlen_autocorr1 | -6.2 | 0.102 | -0.005 |
| jsd_last | -5.5 | 0.712 | 0.602 |
| h2_over_h1 | +4.9 | 0.554 | 0.641 |
| wlen_std | -4.8 | 1.615 | 1.499 |
| rep_adjacent_ed1 | -4.7 | 0.041 | 0.021 |

### slotcite: doğrulama medyan T 5.2, en iyi 4.7

Standart hatanın 2 katından fazla sapan feature sayısı: 18 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| h1 | +6.4 | 3.836 | 3.950 |
| vocab_ed1_density | +6.2 | 0.852 | 0.895 |
| hapax_ratio | -5.6 | 0.715 | 0.636 |
| rep_adjacent_exact | +5.3 | 0.008 | 0.014 |
| h2 | +5.0 | 2.127 | 2.503 |
| jsd_line_final | -4.9 | 0.110 | 0.030 |

### verbose: doğrulama medyan T 6.6, en iyi 5.4

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_std | +12.1 | 1.615 | 1.905 |
| hapax_ratio | -11.6 | 0.715 | 0.553 |
| jsd_last | -11.1 | 0.712 | 0.491 |
| wlen_skew | +9.1 | 0.154 | 0.552 |
| wlen_autocorr1 | -8.7 | 0.102 | -0.047 |
| wlen_frac1 | +7.5 | 0.033 | 0.068 |

### selfcite: doğrulama medyan T 7.4, en iyi 5.6

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| char_double_rate | +10.6 | 0.076 | 0.149 |
| h2 | +10.6 | 2.127 | 2.929 |
| rep_adjacent_exact | +9.5 | 0.008 | 0.019 |
| h2_over_h1 | +9.4 | 0.554 | 0.720 |
| vocab_ed1_density | +8.3 | 0.852 | 0.909 |
| h1 | +8.1 | 3.836 | 3.978 |

### abjad: doğrulama medyan T 8.4, en iyi 7.2

Standart hatanın 2 katından fazla sapan feature sayısı: 20 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_frac1 | +17.0 | 0.033 | 0.112 |
| wlen_frac_le2 | +15.1 | 0.119 | 0.336 |
| wlen_skew | +13.2 | 0.154 | 0.731 |
| first_entropy_ratio | +11.5 | 0.875 | 0.999 |
| h2_over_h1 | +11.3 | 0.554 | 0.754 |
| vocab_ed1_density | -11.1 | 0.852 | 0.775 |

### plain: doğrulama medyan T 9.2, en iyi 6.1

Standart hatanın 2 katından fazla sapan feature sayısı: 23 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | -21.2 | 0.852 | 0.705 |
| eff_symbols | +16.4 | 14.529 | 19.068 |
| h1 | +15.9 | 3.836 | 4.117 |
| h2 | +15.8 | 2.127 | 3.324 |
| h2_over_h1 | +14.2 | 0.554 | 0.805 |
| jsd_last | -14.0 | 0.712 | 0.433 |
