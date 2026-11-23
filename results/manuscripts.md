# El yazması düzeyinde karşılaştırma

Her sınıftan önselden 2000 el yazması üretildi; her biri tek tablo ve tek ayar kümesiyle 16 pencere (8 seçim + 8 doğrulama). Her sınıfta seçim yarısına göre Voynich'e en yakın 20 aday seçildi; tablolar bu adayların DOĞRULAMA yarısındaki değerlerini verir.

T yaklaşık 1 ise adayın ortalama profili Voynich'ten ayırt edilemez. Referans, Voynich'in kendi yarılarının birbirine karşı T değeridir: rastgele bölmelerde beklenen düzey ve ardışık bölmede (ilk yarı ile son yarı) gerçekte olan.

## 1. Seçilen adayların doğrulama yarısında medyan T (parantezde seçim yarısındaki değer)

| görünüm | Voynich: rastgele medyan, %95, ardışık | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.89, 1.49, 1.70 | 14.8 (14.7) | 6.7 (6.7) | 12.8 (12.6) | 10.5 (10.3) | 7.1 (7.1) | 7.4 (7.4) | 8.9 (8.9) |
| eva_glyph | 0.89, 1.55, 1.71 | 9.5 (9.7) | 5.8 (5.8) | 10.0 (10.1) | 8.2 (8.2) | 6.4 (6.3) | 6.4 (6.3) | 8.1 (8.1) |
| v101 | 0.90, 1.53, 1.44 | 7.4 (7.2) | 5.6 (5.7) | 7.3 (7.2) | 8.9 (8.9) | 6.8 (6.9) | 6.5 (6.4) | 7.6 (7.4) |
| zl_basic | 0.90, 1.54, 1.54 | 12.6 (12.5) | 5.9 (5.9) | 11.4 (11.2) | 9.1 (8.9) | 6.6 (6.6) | 6.3 (6.3) | 7.2 (7.3) |
| zl_glyph | 0.90, 1.55, 1.66 | 8.4 (8.5) | 5.2 (5.2) | 9.3 (9.1) | 7.0 (6.9) | 5.6 (5.5) | 5.5 (5.5) | 6.6 (6.5) |

## 2. Doğrulama yarısında en iyi tek aday (T)

| görünüm | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|
| eva_basic | 13.1 | 5.5 | 9.6 | 7.9 | 5.7 | 6.0 | 7.1 |
| eva_glyph | 8.2 | 4.4 | 7.6 | 5.9 | 4.6 | 5.3 | 6.4 |
| v101 | 6.7 | 4.6 | 6.3 | 6.4 | 6.0 | 4.8 | 6.3 |
| zl_basic | 11.2 | 4.8 | 8.7 | 7.0 | 3.7 | 5.4 | 5.9 |
| zl_glyph | 7.7 | 3.6 | 7.1 | 5.9 | 3.7 | 4.3 | 5.3 |

## 3. Aynı ayar, yeni tablo: seçilen ayarlar yeni tohumla yeniden üretilince medyan T

| görünüm | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|
| eva_basic | 15.2 | 9.8 | 12.5 | 9.6 | 8.0 | 8.8 | 9.8 |
| eva_glyph | 9.2 | 7.5 | 9.5 | 7.7 | 7.5 | 8.5 | 8.4 |
| v101 | 7.7 | 7.8 | 6.5 | 8.3 | 9.3 | 8.2 | 9.1 |
| zl_basic | 13.2 | 8.0 | 10.5 | 8.8 | 7.6 | 8.5 | 8.5 |
| zl_glyph | 8.5 | 6.7 | 8.5 | 6.6 | 6.0 | 7.3 | 6.9 |

## 4. İç değişkenlik: seçilen adayların yayılım oranı (Voynich = 1)

| görünüm | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|
| eva_basic | 0.61 | 0.18 | 0.48 | 0.88 | 0.42 | 0.29 | 0.37 |
| eva_glyph | 0.56 | 0.15 | 0.44 | 0.81 | 0.34 | 0.28 | 0.35 |
| v101 | 0.57 | 0.19 | 0.47 | 0.74 | 0.40 | 0.30 | 0.40 |
| zl_basic | 0.57 | 0.17 | 0.48 | 0.89 | 0.40 | 0.29 | 0.36 |
| zl_glyph | 0.49 | 0.14 | 0.42 | 0.74 | 0.35 | 0.28 | 0.30 |

## eva_basic: sınıf sınıf

### grille: doğrulama medyan T 6.7, en iyi 5.5

Standart hatanın 2 katından fazla sapan feature sayısı: 19 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -9.0 | 0.717 | 0.631 |
| wlen_autocorr1 | -8.2 | 0.127 | -0.010 |
| jsd_line_final | -7.0 | 0.109 | 0.011 |
| h2_over_h1 | +6.9 | 0.524 | 0.617 |
| jsd_last | -6.6 | 0.719 | 0.584 |
| h2 | +6.3 | 2.016 | 2.344 |

### slotcite: doğrulama medyan T 7.1, en iyi 5.7

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -13.6 | 0.717 | 0.586 |
| wlen_frac_le2 | -9.2 | 0.077 | 0.031 |
| h2 | +8.4 | 2.016 | 2.456 |
| rep_adjacent_exact | +8.4 | 0.009 | 0.020 |
| jsd_last | -8.3 | 0.719 | 0.548 |
| zipf_slope | +8.1 | -0.778 | -0.557 |

### slotgram: doğrulama medyan T 7.4, en iyi 6.0

Standart hatanın 2 katından fazla sapan feature sayısı: 22 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | +9.9 | 0.823 | 0.930 |
| zipf_slope | +8.6 | -0.778 | -0.544 |
| hapax_ratio | -7.8 | 0.717 | 0.643 |
| wlen_autocorr1 | -7.4 | 0.127 | 0.004 |
| n_symbols | +6.3 | 19.562 | 23.000 |
| type_len_mean | -5.5 | 5.692 | 5.283 |

### verbose: doğrulama medyan T 8.9, en iyi 7.1

Standart hatanın 2 katından fazla sapan feature sayısı: 26 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -21.2 | 0.717 | 0.514 |
| wlen_frac_le2 | +15.7 | 0.077 | 0.155 |
| jsd_last | -12.7 | 0.719 | 0.459 |
| wlen_autocorr1 | -10.7 | 0.127 | -0.050 |
| wlen_std | +10.4 | 1.693 | 2.023 |
| wlen_skew | +10.2 | 0.074 | 0.646 |

### selfcite: doğrulama medyan T 10.5, en iyi 7.9

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| h2 | +16.6 | 2.016 | 2.883 |
| h2_over_h1 | +14.8 | 0.524 | 0.723 |
| first_entropy_ratio | +11.8 | 0.806 | 0.898 |
| hapax_ratio | -11.4 | 0.717 | 0.608 |
| type_len_mean | -10.2 | 5.692 | 4.942 |
| char_double_rate | +10.0 | 0.067 | 0.126 |

### plain: doğrulama medyan T 12.8, en iyi 9.6

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| eff_symbols | +24.6 | 14.240 | 17.832 |
| h1 | +22.1 | 3.845 | 4.070 |
| h2 | +21.4 | 2.016 | 3.136 |
| jsd_last | -21.4 | 0.719 | 0.280 |
| h2_over_h1 | +18.7 | 0.524 | 0.775 |
| wlen_frac_le2 | +16.0 | 0.077 | 0.157 |

### abjad: doğrulama medyan T 14.8, en iyi 13.1

Standart hatanın 2 katından fazla sapan feature sayısı: 24 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_frac_le2 | +52.6 | 0.077 | 0.340 |
| first_entropy_ratio | +22.2 | 0.806 | 0.979 |
| wlen_frac1 | +21.0 | 0.017 | 0.119 |
| type_len_mean | -19.1 | 5.692 | 4.284 |
| h2_over_h1 | +17.5 | 0.524 | 0.759 |
| h2 | +17.4 | 2.016 | 2.925 |


## eva_glyph: sınıf sınıf

### grille: doğrulama medyan T 5.8, en iyi 4.4

Standart hatanın 2 katından fazla sapan feature sayısı: 19 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -8.9 | 0.717 | 0.632 |
| jsd_line_final | -7.1 | 0.110 | 0.011 |
| wlen_autocorr1 | -6.8 | 0.103 | 0.005 |
| vocab_ed1_density | +6.4 | 0.850 | 0.912 |
| zipf_slope | +5.3 | -0.778 | -0.635 |
| h2_over_h1 | +5.1 | 0.556 | 0.640 |

### slotcite: doğrulama medyan T 6.4, en iyi 4.6

Standart hatanın 2 katından fazla sapan feature sayısı: 20 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -10.7 | 0.717 | 0.615 |
| zipf_slope | +8.2 | -0.778 | -0.554 |
| jsd_line_final | -6.6 | 0.110 | 0.019 |
| rep_adjacent_exact | +6.2 | 0.009 | 0.017 |
| first_entropy_ratio | -5.7 | 0.867 | 0.812 |
| h2_over_h1 | +5.6 | 0.556 | 0.647 |

### slotgram: doğrulama medyan T 6.4, en iyi 5.3

Standart hatanın 2 katından fazla sapan feature sayısı: 21 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| jsd_last | -8.2 | 0.718 | 0.549 |
| wlen_frac1 | +6.9 | 0.017 | 0.052 |
| jsd_line_final | -6.9 | 0.110 | 0.014 |
| wlen_autocorr1 | -6.8 | 0.103 | 0.005 |
| vocab_ed1_density | +6.4 | 0.850 | 0.912 |
| wlen_frac_le2 | +6.3 | 0.099 | 0.184 |

### verbose: doğrulama medyan T 8.1, en iyi 6.4

Standart hatanın 2 katından fazla sapan feature sayısı: 26 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -17.3 | 0.717 | 0.550 |
| wlen_std | +15.4 | 1.552 | 1.901 |
| wlen_frac1 | +11.8 | 0.017 | 0.077 |
| jsd_last | -11.0 | 0.718 | 0.491 |
| wlen_skew | +10.6 | 0.183 | 0.669 |
| ttr | -8.3 | 0.443 | 0.247 |

### selfcite: doğrulama medyan T 8.2, en iyi 5.9

Standart hatanın 2 katından fazla sapan feature sayısı: 26 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -12.6 | 0.717 | 0.596 |
| h2 | +10.5 | 2.131 | 2.838 |
| h2_over_h1 | +10.2 | 0.556 | 0.722 |
| rep_adjacent_exact | +8.3 | 0.009 | 0.020 |
| vocab_ed1_density | +7.9 | 0.850 | 0.926 |
| type_len_mean | -6.8 | 5.032 | 4.396 |

### abjad: doğrulama medyan T 9.5, en iyi 8.2

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_frac1 | +21.6 | 0.017 | 0.126 |
| wlen_frac_le2 | +18.2 | 0.099 | 0.346 |
| wlen_skew | +12.7 | 0.183 | 0.765 |
| h2_over_h1 | +11.9 | 0.556 | 0.750 |
| eff_symbols | +11.2 | 14.404 | 16.676 |
| h2 | +10.8 | 2.131 | 2.857 |

### plain: doğrulama medyan T 10.0, en iyi 7.6

Standart hatanın 2 katından fazla sapan feature sayısı: 24 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| h1 | +21.1 | 3.832 | 4.081 |
| eff_symbols | +19.8 | 14.404 | 18.412 |
| h2 | +16.8 | 2.131 | 3.262 |
| vocab_ed1_density | -16.1 | 0.850 | 0.696 |
| h2_over_h1 | +14.7 | 0.556 | 0.796 |
| char_double_rate | -10.5 | 0.076 | 0.010 |


## v101: sınıf sınıf

### grille: doğrulama medyan T 5.6, en iyi 4.6

Standart hatanın 2 katından fazla sapan feature sayısı: 18 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| char_double_rate | +12.1 | 0.015 | 0.043 |
| wlen_autocorr1 | -7.2 | 0.179 | -0.005 |
| jsd_last | -6.5 | 0.679 | 0.535 |
| rep_adjacent_ed1 | -6.0 | 0.043 | 0.025 |
| jsd_line_final | -5.7 | 0.133 | 0.028 |
| eff_symbols | +5.5 | 17.392 | 18.629 |

### slotgram: doğrulama medyan T 6.5, en iyi 4.8

Standart hatanın 2 katından fazla sapan feature sayısı: 20 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| char_double_rate | +10.1 | 0.015 | 0.038 |
| n_symbols | -8.3 | 69.529 | 36.125 |
| wlen_autocorr1 | -7.0 | 0.179 | 0.000 |
| vocab_ed1_density | +6.5 | 0.854 | 0.918 |
| jsd_last | +5.8 | 0.679 | 0.806 |
| zipf_slope | +4.8 | -0.776 | -0.686 |

### slotcite: doğrulama medyan T 6.8, en iyi 6.0

Standart hatanın 2 katından fazla sapan feature sayısı: 20 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| char_double_rate | +10.2 | 0.015 | 0.039 |
| rep_adjacent_exact | +8.6 | 0.006 | 0.014 |
| n_symbols | -7.0 | 69.529 | 41.250 |
| zipf_slope | +5.8 | -0.776 | -0.667 |
| wlen_autocorr1 | -5.4 | 0.179 | 0.043 |
| vocab_ed1_density | +5.0 | 0.854 | 0.903 |

### plain: doğrulama medyan T 7.3, en iyi 6.3

Standart hatanın 2 katından fazla sapan feature sayısı: 20 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | -14.7 | 0.854 | 0.708 |
| h2 | +12.0 | 2.383 | 3.256 |
| h2_over_h1 | +10.8 | 0.595 | 0.787 |
| wlen_frac1 | -10.5 | 0.046 | 0.000 |
| rep_adjacent_ed1 | -10.4 | 0.043 | 0.011 |
| n_symbols | -10.2 | 69.529 | 28.500 |

### abjad: doğrulama medyan T 7.4, en iyi 6.7

Standart hatanın 2 katından fazla sapan feature sayısı: 26 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_frac1 | +15.3 | 0.046 | 0.114 |
| wlen_frac_le2 | +12.9 | 0.184 | 0.330 |
| eff_symbols | +9.7 | 17.392 | 19.578 |
| h2 | +9.3 | 2.383 | 3.062 |
| vocab_ed1_density | -9.2 | 0.854 | 0.762 |
| h2_over_h1 | +9.1 | 0.595 | 0.758 |

### verbose: doğrulama medyan T 7.6, en iyi 6.3

Standart hatanın 2 katından fazla sapan feature sayısı: 27 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_std | +13.1 | 1.469 | 1.815 |
| jsd_last | -12.4 | 0.679 | 0.405 |
| char_double_rate | +8.3 | 0.015 | 0.034 |
| wlen_skew | +8.1 | 0.225 | 0.700 |
| wlen_autocorr1 | -8.1 | 0.179 | -0.027 |
| wlen_frac1 | +7.6 | 0.046 | 0.080 |

### selfcite: doğrulama medyan T 8.9, en iyi 6.4

Standart hatanın 2 katından fazla sapan feature sayısı: 20 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| char_double_rate | +26.4 | 0.015 | 0.076 |
| rep_adjacent_exact | +11.1 | 0.006 | 0.016 |
| h2 | +10.9 | 2.383 | 3.176 |
| jsd_last | -10.1 | 0.679 | 0.456 |
| h2_over_h1 | +9.5 | 0.595 | 0.764 |
| zipf_slope | +9.0 | -0.776 | -0.606 |


## zl_basic: sınıf sınıf

### grille: doğrulama medyan T 5.9, en iyi 4.8

Standart hatanın 2 katından fazla sapan feature sayısı: 18 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| h2_over_h1 | +7.9 | 0.521 | 0.636 |
| h2 | +7.0 | 2.013 | 2.437 |
| wlen_autocorr1 | -6.3 | 0.123 | -0.006 |
| rep_adjacent_ed1 | -6.0 | 0.034 | 0.016 |
| vocab_ed1_density | +6.0 | 0.823 | 0.879 |
| jsd_line_final | -5.6 | 0.110 | 0.017 |

### slotgram: doğrulama medyan T 6.3, en iyi 5.4

Standart hatanın 2 katından fazla sapan feature sayısı: 27 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | +10.3 | 0.823 | 0.919 |
| wlen_frac_le2 | +6.0 | 0.097 | 0.131 |
| zipf_slope | +5.6 | -0.785 | -0.619 |
| wlen_autocorr1 | -5.4 | 0.123 | 0.013 |
| type_len_mean | -5.2 | 5.640 | 5.231 |
| hapax_ratio | -5.1 | 0.715 | 0.643 |

### slotcite: doğrulama medyan T 6.6, en iyi 3.7

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| rep_adjacent_exact | +8.4 | 0.008 | 0.017 |
| hapax_ratio | -8.0 | 0.715 | 0.604 |
| wlen_frac_le2 | -7.8 | 0.097 | 0.052 |
| h2 | +7.4 | 2.013 | 2.456 |
| h2_over_h1 | +7.2 | 0.521 | 0.625 |
| zipf_slope | +6.3 | -0.785 | -0.598 |

### verbose: doğrulama medyan T 7.2, en iyi 5.9

Standart hatanın 2 katından fazla sapan feature sayısı: 27 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_skew | +12.0 | 0.025 | 0.556 |
| jsd_last | -11.6 | 0.712 | 0.483 |
| hapax_ratio | -11.0 | 0.715 | 0.562 |
| wlen_frac_le2 | +9.6 | 0.097 | 0.153 |
| wlen_std | +8.9 | 1.768 | 2.000 |
| wlen_autocorr1 | -7.4 | 0.123 | -0.027 |

### selfcite: doğrulama medyan T 9.1, en iyi 7.0

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| h2 | +13.8 | 2.013 | 2.842 |
| h2_over_h1 | +13.1 | 0.521 | 0.711 |
| rep_adjacent_exact | +12.4 | 0.008 | 0.022 |
| type_len_mean | -9.9 | 5.640 | 4.867 |
| eff_symbols | +9.6 | 14.493 | 16.153 |
| vocab_ed1_density | +8.9 | 0.823 | 0.906 |

### plain: doğrulama medyan T 11.4, en iyi 8.7

Standart hatanın 2 katından fazla sapan feature sayısı: 26 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| eff_symbols | +22.9 | 14.493 | 18.453 |
| h2 | +19.8 | 2.013 | 3.207 |
| h2_over_h1 | +17.1 | 0.521 | 0.771 |
| h1 | +15.9 | 3.862 | 4.088 |
| vocab_ed1_density | -14.9 | 0.823 | 0.685 |
| wlen_std | -14.3 | 1.768 | 1.392 |

### abjad: doğrulama medyan T 12.6, en iyi 11.2

Standart hatanın 2 katından fazla sapan feature sayısı: 24 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_frac_le2 | +40.2 | 0.097 | 0.330 |
| wlen_frac1 | +19.8 | 0.033 | 0.121 |
| first_entropy_ratio | +18.9 | 0.817 | 0.956 |
| type_len_mean | -16.7 | 5.640 | 4.331 |
| wlen_mean | -16.2 | 4.961 | 3.369 |
| wlen_skew | +15.6 | 0.025 | 0.714 |


## zl_glyph: sınıf sınıf

### grille: doğrulama medyan T 5.2, en iyi 3.6

Standart hatanın 2 katından fazla sapan feature sayısı: 15 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | +7.4 | 0.852 | 0.903 |
| wlen_autocorr1 | -5.7 | 0.102 | 0.003 |
| jsd_line_final | -5.7 | 0.110 | 0.017 |
| rep_adjacent_ed1 | -5.2 | 0.041 | 0.019 |
| h2_over_h1 | +4.6 | 0.554 | 0.636 |
| h2 | +4.3 | 2.127 | 2.449 |

### slotgram: doğrulama medyan T 5.5, en iyi 4.3

Standart hatanın 2 katından fazla sapan feature sayısı: 17 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | +8.5 | 0.852 | 0.911 |
| jsd_last | -7.1 | 0.712 | 0.570 |
| jsd_line_final | -5.8 | 0.110 | 0.014 |
| wlen_autocorr1 | -5.5 | 0.102 | 0.008 |
| wlen_frac_le2 | +5.3 | 0.119 | 0.196 |
| wlen_frac1 | +5.3 | 0.033 | 0.058 |

### slotcite: doğrulama medyan T 5.6, en iyi 3.7

Standart hatanın 2 katından fazla sapan feature sayısı: 19 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| rep_adjacent_exact | +7.3 | 0.008 | 0.016 |
| vocab_ed1_density | +5.7 | 0.852 | 0.892 |
| h2_over_h1 | +5.2 | 0.554 | 0.647 |
| jsd_line_final | -5.2 | 0.110 | 0.024 |
| h1 | +5.1 | 3.836 | 3.927 |
| wlen_frac1 | -4.9 | 0.033 | 0.011 |

### verbose: doğrulama medyan T 6.6, en iyi 5.3

Standart hatanın 2 katından fazla sapan feature sayısı: 26 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_std | +11.8 | 1.615 | 1.898 |
| jsd_last | -11.2 | 0.712 | 0.488 |
| wlen_skew | +10.6 | 0.154 | 0.618 |
| hapax_ratio | -10.4 | 0.715 | 0.570 |
| wlen_frac1 | +7.8 | 0.033 | 0.069 |
| wlen_autocorr1 | -7.1 | 0.102 | -0.020 |

### selfcite: doğrulama medyan T 7.0, en iyi 5.9

Standart hatanın 2 katından fazla sapan feature sayısı: 22 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | +10.1 | 0.852 | 0.922 |
| h2 | +9.8 | 2.127 | 2.868 |
| h2_over_h1 | +9.7 | 0.554 | 0.725 |
| rep_adjacent_exact | +9.4 | 0.008 | 0.019 |
| eff_symbols | +8.5 | 14.529 | 16.872 |
| h1 | +8.3 | 3.836 | 3.982 |

### abjad: doğrulama medyan T 8.4, en iyi 7.7

Standart hatanın 2 katından fazla sapan feature sayısı: 22 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_frac1 | +19.6 | 0.033 | 0.124 |
| wlen_frac_le2 | +15.6 | 0.119 | 0.343 |
| wlen_skew | +13.1 | 0.154 | 0.729 |
| vocab_ed1_density | -12.2 | 0.852 | 0.768 |
| eff_symbols | +11.7 | 14.529 | 17.766 |
| h2_over_h1 | +10.4 | 0.554 | 0.739 |

### plain: doğrulama medyan T 9.3, en iyi 7.1

Standart hatanın 2 katından fazla sapan feature sayısı: 23 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | -20.9 | 0.852 | 0.707 |
| eff_symbols | +15.6 | 14.529 | 18.845 |
| h1 | +14.7 | 3.836 | 4.096 |
| h2 | +14.3 | 2.127 | 3.207 |
| h2_over_h1 | +12.0 | 0.554 | 0.767 |
| wlen_std | -11.0 | 1.615 | 1.351 |
