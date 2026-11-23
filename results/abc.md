# ABC raporu: her hipotez Voynich'e ne kadar yaklaşabiliyor

Sentetik örnek: 42800. Her sınıfta Voynich'e en yakın %1 kabul edildi.

Mesafe birimi Voynich'in kendi pencereleri arasındaki değişkenliktir. "Voynich öz mesafesi" bir Voynich penceresinin diğerlerinin ortalamasına uzaklığıdır; bir hipotezin mesafesi bu aralığa girmiyorsa o hipotez Voynich'i (bu feature kümesinde) üretemiyor demektir.

## 1. Kabul edilen örneklerin medyan mesafesi

| görünüm | Voynich öz mesafesi (medyan, en çok) | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|---|
| eva_basic | 0.91, 1.65 | 6.19 | 2.80 | 5.33 | 4.54 | 3.98 |
| eva_glyph | 0.96, 1.63 | 3.96 | 2.31 | 4.20 | 3.63 | 3.56 |
| v101 | 0.97, 1.42 | 3.36 | 2.21 | 3.02 | 3.97 | 3.27 |
| zl_basic | 0.96, 1.52 | 5.36 | 2.61 | 4.71 | 3.99 | 3.26 |
| zl_glyph | 1.03, 1.43 | 3.54 | 2.07 | 3.76 | 3.20 | 2.89 |

## 2. En iyi tek örneğin mesafesi

| görünüm | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|
| eva_basic | 4.98 | 2.44 | 3.94 | 3.57 | 3.12 |
| eva_glyph | 3.17 | 1.68 | 2.98 | 2.90 | 2.59 |
| v101 | 2.63 | 1.46 | 2.29 | 3.07 | 2.34 |
| zl_basic | 4.35 | 2.13 | 3.54 | 3.30 | 2.54 |
| zl_glyph | 2.94 | 1.65 | 2.87 | 2.61 | 2.11 |

## 3. Voynich'in en uç penceresi kadar yakın olan örneklerin oranı

| görünüm | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|
| eva_basic | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| eva_glyph | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| v101 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| zl_basic | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| zl_glyph | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |

## eva_basic: sınıf sınıf

### grille: medyan mesafe 2.80 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| type_len_mean | -4.8 | 5.692 | 4.875 |
| wlen_std | -4.6 | 1.693 | 1.354 |
| vocab_ed1_density | +4.5 | 0.823 | 0.936 |
| wlen_autocorr1 | -3.5 | 0.127 | -0.007 |
| hapax_ratio | -3.3 | 0.717 | 0.644 |
| h2_over_h1 | +2.7 | 0.524 | 0.607 |

### verbose: medyan mesafe 3.98 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -8.9 | 0.717 | 0.521 |
| wlen_frac_le2 | +5.6 | 0.077 | 0.142 |
| jsd_last | -5.0 | 0.719 | 0.480 |
| wlen_autocorr1 | -4.4 | 0.127 | -0.040 |
| wlen_std | +4.2 | 1.693 | 1.996 |
| wlen_skew | +4.1 | 0.074 | 0.600 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 88 |

### selfcite: medyan mesafe 4.54 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 19

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +6.7 | 2.016 | 2.828 |
| h2_over_h1 | +6.3 | 0.524 | 0.721 |
| char_double_rate | +5.9 | 0.067 | 0.148 |
| hapax_ratio | -5.8 | 0.717 | 0.589 |
| type_len_mean | -4.9 | 5.692 | 4.860 |
| rep_adjacent_exact | +4.9 | 0.009 | 0.024 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 5 | 19 [12.8, 24] | 87 |
| p_same_line | 0.149 | 0.0733 [0.0419, 0.127] | 24 |
| l_allo_per_glyph | 0.207 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |

### plain: medyan mesafe 5.33 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| eff_symbols | +10.7 | 14.240 | 17.785 |
| h1 | +9.2 | 3.845 | 4.060 |
| h2 | +8.2 | 2.016 | 3.006 |
| h2_over_h1 | +7.0 | 0.524 | 0.741 |
| n_symbols | +6.6 | 19.562 | 28.000 |
| jsd_last | -6.3 | 0.719 | 0.422 |

### abjad: medyan mesafe 6.19 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac_le2 | +20.9 | 0.077 | 0.319 |
| first_entropy_ratio | +8.7 | 0.806 | 0.963 |
| type_len_mean | -8.0 | 5.692 | 4.334 |
| wlen_frac1 | +7.9 | 0.017 | 0.105 |
| h2_over_h1 | +7.8 | 0.524 | 0.768 |
| h2 | +7.3 | 2.016 | 2.898 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.203 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |


## eva_glyph: sınıf sınıf

### grille: medyan mesafe 2.31 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | +3.5 | 0.850 | 0.927 |
| wlen_autocorr1 | -3.2 | 0.103 | -0.004 |
| wlen_std | -3.2 | 1.552 | 1.382 |
| hapax_ratio | -2.6 | 0.717 | 0.659 |
| rep_within3 | -2.1 | 0.026 | 0.011 |
| h2_over_h1 | +1.9 | 0.556 | 0.628 |

### verbose: medyan mesafe 3.56 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -6.6 | 0.717 | 0.571 |
| wlen_std | +5.8 | 1.552 | 1.860 |
| jsd_last | -5.1 | 0.718 | 0.474 |
| wlen_autocorr1 | -4.1 | 0.103 | -0.035 |
| wlen_skew | +3.8 | 0.183 | 0.586 |
| ttr | -3.5 | 0.443 | 0.252 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 88 |

### selfcite: medyan mesafe 3.63 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -5.6 | 0.717 | 0.593 |
| rep_adjacent_exact | +4.8 | 0.009 | 0.023 |
| h2 | +4.7 | 2.131 | 2.859 |
| h2_over_h1 | +4.5 | 0.556 | 0.727 |
| char_double_rate | +4.0 | 0.076 | 0.135 |
| jsd_last | -3.9 | 0.718 | 0.533 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 5 | 19 [11, 24] | 87 |
| l_allo_per_glyph | 0.207 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |

### abjad: medyan mesafe 3.96 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac1 | +8.7 | 0.017 | 0.119 |
| wlen_frac_le2 | +7.6 | 0.099 | 0.336 |
| wlen_skew | +5.6 | 0.183 | 0.772 |
| first_entropy_ratio | +5.4 | 0.867 | 0.986 |
| h2_over_h1 | +5.1 | 0.556 | 0.746 |
| h2 | +4.8 | 2.131 | 2.874 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.203 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |

### plain: medyan mesafe 4.20 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h1 | +8.9 | 3.832 | 4.076 |
| eff_symbols | +8.8 | 14.404 | 18.503 |
| h2 | +7.5 | 2.131 | 3.291 |
| vocab_ed1_density | -6.6 | 0.850 | 0.705 |
| h2_over_h1 | +6.4 | 0.556 | 0.798 |
| jsd_last | -5.8 | 0.718 | 0.442 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_initial_p | 0.238 | 0 [0, 0.443] | 20 |


## v101: sınıf sınıf

### grille: medyan mesafe 2.21 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +3.5 | 0.015 | 0.034 |
| wlen_autocorr1 | -3.1 | 0.179 | -0.005 |
| rep_adjacent_ed1 | -2.5 | 0.043 | 0.025 |
| n_symbols | -2.5 | 69.529 | 46.000 |
| vocab_ed1_density | +2.2 | 0.854 | 0.905 |
| hapax_ratio | -1.9 | 0.741 | 0.684 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0 | 1.65 [0.694, 2.23] | 76 |

### plain: medyan mesafe 3.02 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | -5.7 | 0.854 | 0.722 |
| h2 | +5.1 | 2.383 | 3.258 |
| h2_over_h1 | +4.7 | 0.595 | 0.790 |
| rep_adjacent_ed1 | -4.6 | 0.043 | 0.010 |
| wlen_frac1 | -4.5 | 0.046 | 0.000 |
| n_symbols | -4.4 | 69.529 | 28.000 |

### verbose: medyan mesafe 3.27 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | +5.8 | 1.469 | 1.824 |
| type_len_mean | +4.6 | 4.440 | 4.999 |
| jsd_last | -4.1 | 0.679 | 0.467 |
| wlen_autocorr1 | -3.5 | 0.179 | -0.030 |
| rep_adjacent_ed1 | -3.4 | 0.043 | 0.019 |
| hapax_ratio | -3.3 | 0.741 | 0.642 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 88 |
| l_final_forms_share | 0.11 | 0 [0, 0.319] | 25 |
| l_allo_per_glyph | 0 | 1.58 [0.902, 2.25] | 75 |

### abjad: medyan mesafe 3.36 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac1 | +5.7 | 0.046 | 0.105 |
| wlen_frac_le2 | +5.2 | 0.184 | 0.321 |
| n_symbols | -4.1 | 69.529 | 31.000 |
| h2_over_h1 | +4.1 | 0.595 | 0.764 |
| h2 | +3.9 | 2.383 | 3.044 |
| char_double_rate | +3.7 | 0.015 | 0.035 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.203 | 0 [0, 0.449] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0.0471] | 25 |

### selfcite: medyan mesafe 3.97 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +9.6 | 0.015 | 0.067 |
| rep_adjacent_exact | +7.0 | 0.006 | 0.021 |
| rep_within3 | +4.6 | 0.021 | 0.045 |
| h2 | +4.0 | 2.383 | 3.061 |
| h2_over_h1 | +3.5 | 0.595 | 0.742 |
| n_symbols | -3.4 | 69.529 | 38.000 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_mut_double | 0.139 | 0.0236 [0.0104, 0.0381] | 15 |
| p_reach | 5 | 16 [10, 21] | 82 |
| p_same_line | 0.149 | 0.0643 [0.031, 0.107] | 21 |
| l_initial_forms_k | 1 | 0 [0, 3] | 25 |


## zl_basic: sınıf sınıf

### grille: medyan mesafe 2.61 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | -5.5 | 1.768 | 1.435 |
| vocab_ed1_density | +4.6 | 0.823 | 0.922 |
| type_len_mean | -4.5 | 5.640 | 4.824 |
| wlen_autocorr1 | -2.8 | 0.123 | -0.008 |
| wlen_mean | -2.6 | 4.961 | 4.371 |
| h2_over_h1 | +2.4 | 0.521 | 0.602 |

### verbose: medyan mesafe 3.26 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_skew | +5.2 | 0.025 | 0.553 |
| wlen_frac_le2 | +4.5 | 0.097 | 0.157 |
| hapax_ratio | -4.3 | 0.715 | 0.576 |
| jsd_last | -3.6 | 0.712 | 0.549 |
| wlen_autocorr1 | -3.6 | 0.123 | -0.044 |
| wlen_std | +3.2 | 1.768 | 1.961 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 88 |

### selfcite: medyan mesafe 3.99 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +5.9 | 2.013 | 2.839 |
| h2_over_h1 | +5.7 | 0.521 | 0.711 |
| char_double_rate | +5.5 | 0.066 | 0.148 |
| rep_adjacent_exact | +5.3 | 0.008 | 0.022 |
| vocab_ed1_density | +4.2 | 0.823 | 0.914 |
| type_len_mean | -4.1 | 5.640 | 4.902 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 5 | 19 [13.8, 26] | 87 |
| p_mut_prefix | 0.159 | 0.323 [0.164, 0.496] | 76 |
| p_same_line | 0.149 | 0.0728 [0.0375, 0.12] | 24 |

### plain: medyan mesafe 4.71 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| eff_symbols | +9.7 | 14.493 | 18.368 |
| h2 | +7.4 | 2.013 | 3.035 |
| h1 | +7.0 | 3.862 | 4.092 |
| h2_over_h1 | +6.7 | 0.521 | 0.747 |
| type_len_mean | -5.8 | 5.640 | 4.588 |
| wlen_std | -5.8 | 1.768 | 1.416 |

### abjad: medyan mesafe 5.36 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac_le2 | +16.6 | 0.097 | 0.319 |
| wlen_frac1 | +7.7 | 0.033 | 0.112 |
| first_entropy_ratio | +7.7 | 0.817 | 0.948 |
| type_len_mean | -7.2 | 5.640 | 4.347 |
| h2_over_h1 | +7.2 | 0.521 | 0.762 |
| wlen_skew | +7.1 | 0.025 | 0.749 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.203 | 0 [0, 0.223] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0.0163] | 25 |


## zl_glyph: sınıf sınıf

### grille: medyan mesafe 2.07 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 3

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | -3.6 | 1.615 | 1.418 |
| vocab_ed1_density | +3.5 | 0.852 | 0.908 |
| wlen_autocorr1 | -2.5 | 0.102 | 0.002 |
| rep_within3 | -1.8 | 0.027 | 0.013 |
| h2_over_h1 | +1.7 | 0.554 | 0.624 |
| rep_adjacent_exact | -1.6 | 0.008 | 0.005 |

### verbose: medyan mesafe 2.89 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| jsd_last | -4.7 | 0.712 | 0.496 |
| wlen_skew | +4.1 | 0.154 | 0.572 |
| wlen_std | +4.1 | 1.615 | 1.840 |
| wlen_autocorr1 | -3.6 | 0.102 | -0.043 |
| hapax_ratio | -3.6 | 0.715 | 0.599 |
| ttr | -2.7 | 0.434 | 0.267 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 88 |

### selfcite: medyan mesafe 3.20 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| rep_adjacent_exact | +4.9 | 0.008 | 0.021 |
| h2 | +4.2 | 2.127 | 2.867 |
| h2_over_h1 | +3.9 | 0.554 | 0.714 |
| vocab_ed1_density | +3.9 | 0.852 | 0.914 |
| h1 | +3.8 | 3.836 | 3.989 |
| char_double_rate | +3.8 | 0.076 | 0.135 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 5 | 18 [12.8, 24] | 85 |
| p_same_line | 0.149 | 0.0623 [0.03, 0.0961] | 20 |
| l_final_forms_share | 0.105 | 0.613 [0.252, 0.818] | 79 |

### abjad: medyan mesafe 3.54 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac1 | +8.1 | 0.033 | 0.119 |
| wlen_frac_le2 | +6.4 | 0.119 | 0.333 |
| wlen_skew | +6.0 | 0.154 | 0.764 |
| h2_over_h1 | +4.7 | 0.554 | 0.746 |
| first_entropy_ratio | +4.5 | 0.875 | 0.986 |
| h2 | +4.4 | 2.127 | 2.887 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_final_forms_share | 0 | 0.567 [0.422, 0.705] | 76 |
| l_allo_per_glyph | 0.203 | 0 [0, 0.364] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0.0213] | 25 |

### plain: medyan mesafe 3.76 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | -8.0 | 0.852 | 0.723 |
| eff_symbols | +6.3 | 14.529 | 18.557 |
| h1 | +6.1 | 3.836 | 4.085 |
| h2 | +5.8 | 2.127 | 3.146 |
| wlen_std | -5.1 | 1.615 | 1.331 |
| h2_over_h1 | +5.0 | 0.554 | 0.757 |
