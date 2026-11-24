# El yazması düzeyinde karşılaştırma

Her sınıftan önselden 2000 el yazması üretildi; her biri tek tablo ve tek ayar kümesiyle 16 pencere (8 seçim + 8 doğrulama). Her sınıfta seçim yarısına göre Voynich'e en yakın 20 aday seçildi; tablolar bu adayların DOĞRULAMA yarısındaki değerlerini verir.

T yaklaşık 1 ise adayın ortalama profili Voynich'ten ayırt edilemez. Referans, Voynich'in kendi yarılarının birbirine karşı T değeridir: rastgele bölmelerde beklenen düzey ve ardışık bölmede (ilk yarı ile son yarı) gerçekte olan.

## 1. Seçilen adayların doğrulama yarısında medyan T (parantezde seçim yarısındaki değer)

| görünüm | Voynich: rastgele medyan, %95, ardışık | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.89, 1.49, 1.70 | 14.8 (14.7) | 9.3 (9.5) | 6.7 (6.7) | 12.9 (12.7) | 10.5 (10.4) | 7.1 (7.1) | 7.4 (7.4) | 9.0 (9.0) |
| eva_glyph | 0.89, 1.55, 1.71 | 9.5 (9.7) | 8.1 (8.4) | 5.8 (5.8) | 10.0 (10.1) | 8.2 (8.2) | 6.4 (6.3) | 6.5 (6.3) | 8.2 (8.3) |
| v101 | 0.90, 1.53, 1.44 | 7.4 (7.2) | 8.1 (8.4) | 5.6 (5.7) | 7.3 (7.2) | 8.9 (8.9) | 6.8 (6.9) | 6.5 (6.4) | 7.8 (7.8) |
| zl_basic | 0.90, 1.54, 1.54 | 12.6 (12.5) | 9.4 (9.6) | 5.9 (5.9) | 11.4 (11.2) | 9.1 (8.9) | 6.6 (6.6) | 6.3 (6.3) | 7.6 (7.7) |
| zl_glyph | 0.90, 1.55, 1.66 | 8.4 (8.5) | 7.3 (7.7) | 5.2 (5.2) | 9.3 (9.1) | 7.0 (6.9) | 5.6 (5.5) | 5.5 (5.5) | 7.0 (6.9) |

## 2. Doğrulama yarısında en iyi tek aday (T)

| görünüm | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | 13.1 | 8.3 | 5.5 | 9.6 | 7.9 | 5.7 | 6.0 | 8.0 |
| eva_glyph | 8.3 | 6.7 | 4.4 | 7.6 | 5.9 | 4.7 | 5.3 | 6.8 |
| v101 | 6.7 | 5.7 | 4.6 | 6.3 | 6.4 | 6.0 | 4.8 | 6.6 |
| zl_basic | 11.2 | 6.7 | 4.8 | 8.7 | 7.0 | 3.7 | 5.4 | 6.6 |
| zl_glyph | 7.7 | 5.3 | 3.6 | 7.1 | 5.9 | 3.7 | 4.3 | 5.5 |

## 3. Aynı ayar, yeni tablo: seçilen ayarlar yeni tohumla yeniden üretilince medyan T

| görünüm | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | 15.2 | 11.3 | 9.9 | 12.5 | 9.7 | 8.0 | 8.8 | 10.9 |
| eva_glyph | 9.2 | 9.3 | 7.5 | 9.5 | 7.7 | 7.5 | 8.5 | 9.3 |
| v101 | 7.7 | 8.6 | 7.8 | 6.5 | 8.3 | 9.3 | 8.2 | 9.0 |
| zl_basic | 13.2 | 11.2 | 8.0 | 10.5 | 8.8 | 7.6 | 8.5 | 9.5 |
| zl_glyph | 8.5 | 8.4 | 6.7 | 8.5 | 6.6 | 6.0 | 7.3 | 7.2 |

## 4. İç değişkenlik: seçilen adayların yayılım oranı (Voynich = 1)

| görünüm | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.61 | 0.33 | 0.18 | 0.48 | 0.88 | 0.42 | 0.29 | 0.39 |
| eva_glyph | 0.56 | 0.41 | 0.15 | 0.44 | 0.81 | 0.34 | 0.28 | 0.37 |
| v101 | 0.57 | 0.40 | 0.19 | 0.47 | 0.74 | 0.40 | 0.30 | 0.41 |
| zl_basic | 0.57 | 0.37 | 0.17 | 0.48 | 0.89 | 0.40 | 0.29 | 0.37 |
| zl_glyph | 0.49 | 0.45 | 0.14 | 0.42 | 0.74 | 0.35 | 0.28 | 0.34 |

## 5. Büyüme profili (16000 kelimede; doğrulama yarısı)

Sıra: tür / kelime, hapax / tür, "bir harf farklı" komşusu olan türlerin oranı. Voynich için iki yarının değeri; sınıflar için önseldeki medyan [%5, %95].

| görünüm | Voynich (ilk yarı; ikinci yarı) | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.25, 0.68, 0.86; 0.26, 0.68, 0.86 | 0.18 [0.10, 0.33]<br>0.61 [0.49, 0.75]<br>0.86 [0.79, 0.91] | 0.25 [0.11, 0.47]<br>0.63 [0.42, 0.78]<br>0.99 [0.94, 1.00] | 0.10 [0.02, 0.35]<br>0.37 [0.04, 0.66]<br>0.99 [0.90, 1.00] | 0.28 [0.15, 0.49]<br>0.68 [0.54, 0.82]<br>0.63 [0.45, 0.78] | 0.39 [0.18, 0.67]<br>0.62 [0.46, 0.81]<br>0.93 [0.80, 0.98] | 0.14 [0.03, 0.43]<br>0.43 [0.14, 0.71]<br>0.98 [0.87, 1.00] | 0.20 [0.01, 0.88]<br>0.55 [0.12, 0.91]<br>0.98 [0.57, 1.00] | 0.20 [0.06, 0.49]<br>0.65 [0.40, 0.84]<br>0.68 [0.35, 0.91] |
| eva_glyph | 0.25, 0.68, 0.88; 0.26, 0.68, 0.88 | 0.18 [0.10, 0.33]<br>0.61 [0.49, 0.75]<br>0.86 [0.79, 0.91] | 0.25 [0.11, 0.47]<br>0.63 [0.42, 0.78]<br>0.99 [0.94, 1.00] | 0.10 [0.02, 0.35]<br>0.37 [0.04, 0.66]<br>0.99 [0.90, 1.00] | 0.28 [0.15, 0.49]<br>0.68 [0.54, 0.82]<br>0.63 [0.45, 0.78] | 0.39 [0.18, 0.67]<br>0.62 [0.46, 0.81]<br>0.93 [0.80, 0.98] | 0.14 [0.03, 0.43]<br>0.43 [0.14, 0.71]<br>0.98 [0.87, 1.00] | 0.20 [0.01, 0.88]<br>0.55 [0.12, 0.91]<br>0.98 [0.57, 1.00] | 0.20 [0.06, 0.49]<br>0.65 [0.40, 0.84]<br>0.68 [0.35, 0.91] |
| v101 | 0.30, 0.72, 0.89; 0.27, 0.70, 0.89 | 0.18 [0.10, 0.33]<br>0.61 [0.49, 0.75]<br>0.86 [0.79, 0.91] | 0.25 [0.11, 0.47]<br>0.63 [0.42, 0.78]<br>0.99 [0.94, 1.00] | 0.10 [0.02, 0.35]<br>0.37 [0.04, 0.66]<br>0.99 [0.90, 1.00] | 0.28 [0.15, 0.49]<br>0.68 [0.54, 0.82]<br>0.63 [0.45, 0.78] | 0.39 [0.18, 0.67]<br>0.62 [0.46, 0.81]<br>0.93 [0.80, 0.98] | 0.14 [0.03, 0.43]<br>0.43 [0.14, 0.71]<br>0.98 [0.87, 1.00] | 0.20 [0.01, 0.88]<br>0.55 [0.12, 0.91]<br>0.98 [0.57, 1.00] | 0.20 [0.06, 0.49]<br>0.65 [0.40, 0.84]<br>0.68 [0.35, 0.91] |
| zl_basic | 0.25, 0.69, 0.87; 0.26, 0.69, 0.86 | 0.18 [0.10, 0.33]<br>0.61 [0.49, 0.75]<br>0.86 [0.79, 0.91] | 0.25 [0.11, 0.47]<br>0.63 [0.42, 0.78]<br>0.99 [0.94, 1.00] | 0.10 [0.02, 0.35]<br>0.37 [0.04, 0.66]<br>0.99 [0.90, 1.00] | 0.28 [0.15, 0.49]<br>0.68 [0.54, 0.82]<br>0.63 [0.45, 0.78] | 0.39 [0.18, 0.67]<br>0.62 [0.46, 0.81]<br>0.93 [0.80, 0.98] | 0.14 [0.03, 0.43]<br>0.43 [0.14, 0.71]<br>0.98 [0.87, 1.00] | 0.20 [0.01, 0.88]<br>0.55 [0.12, 0.91]<br>0.98 [0.57, 1.00] | 0.20 [0.06, 0.49]<br>0.65 [0.40, 0.84]<br>0.68 [0.35, 0.91] |
| zl_glyph | 0.25, 0.69, 0.89; 0.26, 0.69, 0.88 | 0.18 [0.10, 0.33]<br>0.61 [0.49, 0.75]<br>0.86 [0.79, 0.91] | 0.25 [0.11, 0.47]<br>0.63 [0.42, 0.78]<br>0.99 [0.94, 1.00] | 0.10 [0.02, 0.35]<br>0.37 [0.04, 0.66]<br>0.99 [0.90, 1.00] | 0.28 [0.15, 0.49]<br>0.68 [0.54, 0.82]<br>0.63 [0.45, 0.78] | 0.39 [0.18, 0.67]<br>0.62 [0.46, 0.81]<br>0.93 [0.80, 0.98] | 0.14 [0.03, 0.43]<br>0.43 [0.14, 0.71]<br>0.98 [0.87, 1.00] | 0.20 [0.01, 0.88]<br>0.55 [0.12, 0.91]<br>0.98 [0.57, 1.00] | 0.20 [0.06, 0.49]<br>0.65 [0.40, 0.84]<br>0.68 [0.35, 0.91] |

## 6. Büyüme profili Voynich'e uyan el yazması sayısı ve bunların doğrulama T'si (medyan; en iyi)

Uyma ölçütü: üç ölçünün her birinde Voynich ortalamasından fark en çok 0.05.

| görünüm | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | 335 (28.0; 13.6) | 0 | 2 (29.6; 22.9) | 8 (13.1; 11.9) | 3 (34.3; 30.6) | 16 (18.0; 12.6) | 29 (21.2; 9.8) | 24 (22.3; 13.5) |
| eva_glyph | 266 (19.9; 8.9) | 0 | 14 (18.0; 9.5) | 3 (10.1; 8.5) | 16 (21.1; 15.5) | 34 (16.8; 10.0) | 35 (14.8; 6.4) | 13 (16.4; 11.3) |
| v101 | 105 (15.1; 7.2) | 0 | 15 (13.1; 6.7) | 5 (11.2; 7.3) | 18 (23.1; 11.8) | 26 (13.0; 6.3) | 33 (10.7; 6.5) | 4 (11.0; 9.1) |
| zl_basic | 322 (22.3; 11.7) | 0 | 2 (18.0; 16.3) | 6 (11.4; 10.5) | 5 (27.0; 25.6) | 19 (11.5; 7.9) | 29 (16.2; 7.5) | 22 (14.7; 7.8) |
| zl_glyph | 240 (16.1; 7.7) | 0 | 15 (10.2; 6.5) | 2 (10.3; 8.0) | 15 (19.2; 14.4) | 36 (9.6; 5.1) | 35 (10.5; 5.5) | 14 (11.0; 6.8) |

## eva_basic: sınıf sınıf

### grille: doğrulama medyan T 6.7, en iyi 5.5

Standart hatanın 2 katından fazla sapan feature sayısı: 19 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -9.6 | 0.717 | 0.625 |
| wlen_autocorr1 | -8.2 | 0.127 | -0.010 |
| jsd_line_final | -7.0 | 0.109 | 0.011 |
| h2_over_h1 | +6.9 | 0.524 | 0.617 |
| jsd_last | -6.6 | 0.719 | 0.584 |
| rep_adjacent_ed1 | -6.5 | 0.032 | 0.013 |

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

Standart hatanın 2 katından fazla sapan feature sayısı: 23 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | +9.9 | 0.823 | 0.930 |
| zipf_slope | +8.6 | -0.778 | -0.544 |
| hapax_ratio | -7.8 | 0.717 | 0.643 |
| wlen_autocorr1 | -7.4 | 0.127 | 0.004 |
| n_symbols | +6.5 | 19.562 | 23.000 |
| type_len_mean | -5.5 | 5.692 | 5.283 |

### verbose: doğrulama medyan T 9.0, en iyi 8.0

Standart hatanın 2 katından fazla sapan feature sayısı: 28 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -19.3 | 0.717 | 0.532 |
| wlen_frac_le2 | +15.6 | 0.077 | 0.155 |
| jsd_last | -12.6 | 0.719 | 0.461 |
| wlen_std | +10.9 | 1.693 | 2.039 |
| wlen_autocorr1 | -10.4 | 0.127 | -0.045 |
| ttr | -8.8 | 0.443 | 0.234 |

### codebook: doğrulama medyan T 9.3, en iyi 8.3

Standart hatanın 2 katından fazla sapan feature sayısı: 23 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_std | -26.8 | 1.693 | 0.846 |
| vocab_ed1_density | +12.8 | 0.823 | 0.961 |
| wlen_frac_le2 | -12.5 | 0.077 | 0.014 |
| type_len_mean | -11.9 | 5.692 | 4.813 |
| jsd_first | +11.8 | 0.385 | 0.558 |
| wlen_skew | -10.5 | 0.074 | -0.515 |

### selfcite: doğrulama medyan T 10.5, en iyi 7.9

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| h2 | +16.6 | 2.016 | 2.883 |
| h2_over_h1 | +14.8 | 0.524 | 0.723 |
| first_entropy_ratio | +11.8 | 0.806 | 0.898 |
| hapax_ratio | -11.4 | 0.717 | 0.608 |
| type_len_mean | -10.2 | 5.692 | 4.942 |
| eff_symbols | +10.1 | 14.240 | 15.690 |

### plain: doğrulama medyan T 12.9, en iyi 9.6

Standart hatanın 2 katından fazla sapan feature sayısı: 25 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| eff_symbols | +25.1 | 14.240 | 17.832 |
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

### slotcite: doğrulama medyan T 6.4, en iyi 4.7

Standart hatanın 2 katından fazla sapan feature sayısı: 20 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| hapax_ratio | -10.7 | 0.717 | 0.615 |
| zipf_slope | +8.2 | -0.778 | -0.554 |
| jsd_line_final | -6.6 | 0.110 | 0.019 |
| rep_adjacent_exact | +6.2 | 0.009 | 0.017 |
| first_entropy_ratio | -5.7 | 0.867 | 0.812 |
| h2_over_h1 | +5.6 | 0.556 | 0.647 |

### slotgram: doğrulama medyan T 6.5, en iyi 5.3

Standart hatanın 2 katından fazla sapan feature sayısı: 21 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| jsd_last | -8.2 | 0.718 | 0.549 |
| wlen_frac1 | +6.9 | 0.017 | 0.052 |
| jsd_line_final | -6.9 | 0.110 | 0.014 |
| wlen_autocorr1 | -6.8 | 0.103 | 0.005 |
| vocab_ed1_density | +6.4 | 0.850 | 0.912 |
| wlen_frac_le2 | +6.3 | 0.099 | 0.184 |

### codebook: doğrulama medyan T 8.1, en iyi 6.7

Standart hatanın 2 katından fazla sapan feature sayısı: 22 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_std | -14.7 | 1.552 | 1.220 |
| vocab_ed1_density | +9.1 | 0.850 | 0.938 |
| h2_over_h1 | +9.1 | 0.556 | 0.704 |
| wlen_skew | -9.0 | 0.183 | -0.229 |
| wlen_autocorr1 | -8.8 | 0.103 | -0.025 |
| h2 | +8.0 | 2.131 | 2.667 |

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

### verbose: doğrulama medyan T 8.2, en iyi 6.8

Standart hatanın 2 katından fazla sapan feature sayısı: 26 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_std | +16.0 | 1.552 | 1.915 |
| hapax_ratio | -15.7 | 0.717 | 0.566 |
| jsd_last | -11.4 | 0.718 | 0.483 |
| wlen_autocorr1 | -9.5 | 0.103 | -0.034 |
| wlen_skew | +9.0 | 0.183 | 0.596 |
| ttr | -7.8 | 0.443 | 0.259 |

### abjad: doğrulama medyan T 9.5, en iyi 8.3

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

### verbose: doğrulama medyan T 7.8, en iyi 6.6

Standart hatanın 2 katından fazla sapan feature sayısı: 23 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_std | +13.0 | 1.469 | 1.812 |
| type_len_mean | +11.9 | 4.440 | 5.060 |
| wlen_frac1 | +10.6 | 0.046 | 0.093 |
| hapax_ratio | -10.3 | 0.741 | 0.610 |
| word_entropy_norm | -8.5 | 0.814 | 0.716 |
| wlen_autocorr1 | -8.2 | 0.179 | -0.029 |

### codebook: doğrulama medyan T 8.1, en iyi 5.7

Standart hatanın 2 katından fazla sapan feature sayısı: 22 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_std | -14.8 | 1.469 | 1.079 |
| n_symbols | -10.4 | 69.529 | 27.750 |
| char_double_rate | +9.6 | 0.015 | 0.037 |
| wlen_autocorr1 | -9.3 | 0.179 | -0.058 |
| jsd_first | +9.1 | 0.310 | 0.507 |
| first_entropy_ratio | -8.6 | 0.886 | 0.768 |

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

### verbose: doğrulama medyan T 7.6, en iyi 6.6

Standart hatanın 2 katından fazla sapan feature sayısı: 28 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_skew | +11.1 | 0.025 | 0.516 |
| jsd_last | -10.8 | 0.712 | 0.500 |
| wlen_frac_le2 | +10.0 | 0.097 | 0.155 |
| wlen_std | +9.0 | 1.768 | 2.005 |
| hapax_ratio | -8.8 | 0.715 | 0.593 |
| wlen_autocorr1 | -8.0 | 0.123 | -0.039 |

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

### codebook: doğrulama medyan T 9.4, en iyi 6.7

Standart hatanın 2 katından fazla sapan feature sayısı: 24 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_std | -26.4 | 1.768 | 1.077 |
| vocab_ed1_density | +11.9 | 0.823 | 0.935 |
| h2_over_h1 | +11.1 | 0.521 | 0.683 |
| type_len_mean | -10.4 | 5.640 | 4.830 |
| h2 | +9.8 | 2.013 | 2.602 |
| rep_adjacent_exact | -7.6 | 0.008 | 0.000 |

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

### verbose: doğrulama medyan T 7.0, en iyi 5.5

Standart hatanın 2 katından fazla sapan feature sayısı: 28 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| wlen_std | +11.4 | 1.615 | 1.889 |
| jsd_last | -11.0 | 0.712 | 0.492 |
| wlen_skew | +9.6 | 0.154 | 0.576 |
| hapax_ratio | -8.7 | 0.715 | 0.594 |
| wlen_autocorr1 | -8.2 | 0.102 | -0.039 |
| ttr | -6.6 | 0.434 | 0.259 |

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

### codebook: doğrulama medyan T 7.3, en iyi 5.3

Standart hatanın 2 katından fazla sapan feature sayısı: 22 / 32

| tutmayan feature | sapma (standart hata) | Voynich | seçilen adaylar |
|---|---|---|---|
| vocab_ed1_density | +10.6 | 0.852 | 0.926 |
| wlen_std | -10.3 | 1.615 | 1.367 |
| wlen_autocorr1 | -10.1 | 0.102 | -0.073 |
| h2_over_h1 | +7.8 | 0.554 | 0.693 |
| rep_adjacent_exact | -7.2 | 0.008 | 0.001 |
| h2 | +6.8 | 2.127 | 2.639 |

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
