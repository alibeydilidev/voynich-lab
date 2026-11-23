# ABC raporu: her hipotez Voynich'e ne kadar yaklaşabiliyor

Sentetik örnek: 60400. Her sınıfta Voynich'e en yakın %1 kabul edildi.

Mesafe birimi Voynich'in kendi pencereleri arasındaki değişkenliktir. "Voynich öz mesafesi" bir Voynich penceresinin diğerlerinin ortalamasına uzaklığıdır; bir hipotezin mesafesi bu aralığa girmiyorsa o hipotez Voynich'i (bu feature kümesinde) üretemiyor demektir.

## 1. Kabul edilen örneklerin medyan mesafesi

| görünüm | Voynich öz mesafesi (medyan, en çok) | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.91, 1.65 | 6.16 | 2.77 | 5.42 | 4.46 | 3.17 | 3.19 | 4.00 |
| eva_glyph | 0.96, 1.64 | 3.96 | 2.46 | 4.29 | 3.58 | 2.84 | 2.86 | 3.70 |
| v101 | 0.97, 1.42 | 3.22 | 2.54 | 3.11 | 3.84 | 3.02 | 2.83 | 3.43 |
| zl_basic | 0.96, 1.52 | 5.33 | 2.43 | 4.75 | 4.00 | 2.76 | 2.86 | 3.37 |
| zl_glyph | 1.03, 1.43 | 3.53 | 2.15 | 3.94 | 3.17 | 2.43 | 2.54 | 3.01 |

## 2. En iyi tek örneğin mesafesi

| görünüm | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|
| eva_basic | 5.29 | 2.00 | 4.03 | 3.02 | 2.45 | 2.21 | 3.14 |
| eva_glyph | 3.11 | 1.83 | 2.67 | 2.50 | 2.10 | 2.21 | 2.71 |
| v101 | 2.55 | 1.94 | 2.23 | 2.49 | 2.16 | 1.84 | 2.56 |
| zl_basic | 4.54 | 1.62 | 3.52 | 2.68 | 2.20 | 2.13 | 2.62 |
| zl_glyph | 2.81 | 1.64 | 2.55 | 2.31 | 1.68 | 1.88 | 2.25 |

## 3. Voynich'in en uç penceresi kadar yakın olan örneklerin oranı

| görünüm | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|
| eva_basic | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| eva_glyph | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| v101 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| zl_basic | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| zl_glyph | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |

## eva_basic: sınıf sınıf

### grille: medyan mesafe 2.77 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_autocorr1 | -3.3 | 0.127 | 0.002 |
| h2_over_h1 | +3.3 | 0.524 | 0.626 |
| h2 | +3.2 | 2.016 | 2.407 |
| hapax_ratio | -3.2 | 0.717 | 0.647 |
| rep_adjacent_ed1 | -2.6 | 0.032 | 0.015 |
| jsd_last | -2.3 | 0.719 | 0.609 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 84 |
| l_allo_per_glyph | 0.24 | 0 [0, 0] | 25 |
| l_allo_rate | 0.012 | 0 [0, 0] | 25 |

### slotcite: medyan mesafe 3.17 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -5.4 | 0.717 | 0.597 |
| h2_over_h1 | +3.3 | 0.524 | 0.625 |
| h2 | +3.1 | 2.016 | 2.395 |
| rep_adjacent_exact | +3.1 | 0.009 | 0.018 |
| jsd_last | -2.9 | 0.719 | 0.583 |
| wlen_frac_le2 | -2.5 | 0.077 | 0.048 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 83 |
| p_same_line | 0.252 | 0.122 [0.0521, 0.226] | 23 |

### slotgram: medyan mesafe 3.19 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| zipf_slope | +4.4 | -0.778 | -0.505 |
| vocab_ed1_density | +2.8 | 0.823 | 0.892 |
| wlen_autocorr1 | -2.7 | 0.127 | 0.023 |
| h2_over_h1 | +2.7 | 0.524 | 0.607 |
| h2 | +2.6 | 2.016 | 2.336 |
| top10_coverage | -2.6 | 0.171 | 0.075 |

### verbose: medyan mesafe 4.00 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -7.5 | 0.717 | 0.551 |
| wlen_frac_le2 | +6.2 | 0.077 | 0.148 |
| wlen_std | +4.4 | 1.693 | 2.012 |
| wlen_skew | +4.2 | 0.074 | 0.617 |
| jsd_last | -4.1 | 0.719 | 0.525 |
| wlen_autocorr1 | -4.0 | 0.127 | -0.026 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 88 |
| l_allo_per_glyph | 0.203 | 0 [0, 0.489] | 25 |
| l_allo_rate | 0.0102 | 0 [0, 0.0482] | 25 |

### selfcite: medyan mesafe 4.46 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +6.9 | 2.016 | 2.850 |
| char_double_rate | +6.9 | 0.067 | 0.162 |
| h2_over_h1 | +6.5 | 0.524 | 0.727 |
| hapax_ratio | -5.7 | 0.717 | 0.592 |
| rep_adjacent_exact | +5.4 | 0.009 | 0.025 |
| first_entropy_ratio | +4.8 | 0.806 | 0.892 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 5 | 17 [11.8, 23.2] | 84 |
| p_mut_prefix | 0.16 | 0.344 [0.186, 0.51] | 78 |
| p_same_line | 0.149 | 0.0714 [0.0386, 0.117] | 24 |

### plain: medyan mesafe 5.42 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| eff_symbols | +10.6 | 14.240 | 17.717 |
| h1 | +9.4 | 3.845 | 4.066 |
| jsd_last | -8.6 | 0.719 | 0.310 |
| h2 | +8.4 | 2.016 | 3.030 |
| h2_over_h1 | +7.1 | 0.524 | 0.744 |
| n_symbols | +6.9 | 19.562 | 28.000 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.237 | 0 [0, 0.331] | 20 |
| l_allo_per_glyph | 0.256 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0124 | 0 [0, 0] | 25 |
| l_final_forms_share | 0.107 | 0 [0, 0.707] | 25 |

### abjad: medyan mesafe 6.16 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac_le2 | +21.0 | 0.077 | 0.320 |
| first_entropy_ratio | +9.7 | 0.806 | 0.981 |
| wlen_frac1 | +8.6 | 0.017 | 0.114 |
| type_len_mean | -7.8 | 5.692 | 4.354 |
| h2_over_h1 | +7.4 | 0.524 | 0.754 |
| h2 | +7.1 | 2.016 | 2.873 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_final_forms_share | 0 | 0.537 [0.272, 0.791] | 75 |
| l_allo_per_glyph | 0.203 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0102 | 0 [0, 0] | 25 |


## eva_glyph: sınıf sınıf

### grille: medyan mesafe 2.46 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -3.1 | 0.717 | 0.648 |
| wlen_autocorr1 | -2.9 | 0.103 | 0.008 |
| vocab_ed1_density | +2.6 | 0.850 | 0.908 |
| h2_over_h1 | +2.1 | 0.556 | 0.634 |
| h2 | +1.9 | 2.131 | 2.421 |
| rep_within3 | -1.8 | 0.026 | 0.013 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.24 | 0 [0, 0.507] | 25 |
| l_allo_rate | 0.012 | 0 [0, 0.0824] | 25 |
| l_initial_forms_k | 1 | 0 [0, 2] | 25 |

### slotcite: medyan mesafe 2.84 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -4.4 | 0.717 | 0.621 |
| jsd_last | -3.1 | 0.718 | 0.569 |
| rep_adjacent_exact | +2.8 | 0.009 | 0.017 |
| vocab_ed1_density | +2.8 | 0.850 | 0.913 |
| zipf_slope | +2.7 | -0.778 | -0.608 |
| h2_over_h1 | +2.6 | 0.556 | 0.654 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_exact | 0.404 | 0.238 [0.172, 0.401] | 23 |

### slotgram: medyan mesafe 2.86 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 3

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_autocorr1 | -2.8 | 0.103 | 0.009 |
| vocab_ed1_density | +2.7 | 0.850 | 0.911 |
| zipf_slope | +2.7 | -0.778 | -0.609 |
| first_entropy_ratio | -2.0 | 0.867 | 0.823 |
| rep_within3 | -1.9 | 0.026 | 0.012 |
| h2_over_h1 | +1.9 | 0.556 | 0.627 |

### selfcite: medyan mesafe 3.58 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -5.5 | 0.717 | 0.596 |
| rep_adjacent_exact | +5.4 | 0.009 | 0.025 |
| h2 | +4.8 | 2.131 | 2.885 |
| h2_over_h1 | +4.8 | 0.556 | 0.738 |
| char_double_rate | +4.2 | 0.076 | 0.137 |
| jsd_last | -3.9 | 0.718 | 0.533 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 5 | 17 [12, 24] | 84 |
| p_mut_prefix | 0.16 | 0.318 [0.122, 0.499] | 75 |

### verbose: medyan mesafe 3.70 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -7.3 | 0.717 | 0.554 |
| wlen_std | +6.9 | 1.552 | 1.912 |
| jsd_last | -4.3 | 0.718 | 0.510 |
| wlen_skew | +4.3 | 0.183 | 0.641 |
| wlen_autocorr1 | -4.2 | 0.103 | -0.036 |
| ttr | -3.5 | 0.443 | 0.249 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 88 |

### abjad: medyan mesafe 3.96 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac1 | +8.4 | 0.017 | 0.115 |
| wlen_frac_le2 | +7.2 | 0.099 | 0.325 |
| first_entropy_ratio | +5.7 | 0.867 | 0.995 |
| h2_over_h1 | +5.0 | 0.556 | 0.743 |
| wlen_skew | +4.9 | 0.183 | 0.703 |
| h2 | +4.5 | 2.131 | 2.839 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_initial_p | 0.234 | 0 [0, 0.417] | 20 |
| l_final_forms_share | 0 | 0.605 [0.373, 0.817] | 79 |
| l_allo_per_glyph | 0.203 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0102 | 0 [0, 0] | 25 |

### plain: medyan mesafe 4.29 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h1 | +9.1 | 3.832 | 4.081 |
| eff_symbols | +8.6 | 14.404 | 18.437 |
| jsd_last | -8.2 | 0.718 | 0.325 |
| h2 | +7.6 | 2.131 | 3.312 |
| h2_over_h1 | +6.6 | 0.556 | 0.803 |
| vocab_ed1_density | -6.3 | 0.850 | 0.712 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.256 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0124 | 0 [0, 0] | 25 |
| l_final_forms_share | 0.107 | 0 [0, 0.649] | 25 |


## v101: sınıf sınıf

### grille: medyan mesafe 2.54 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +4.4 | 0.015 | 0.039 |
| wlen_autocorr1 | -3.1 | 0.179 | -0.006 |
| vocab_ed1_density | +2.8 | 0.854 | 0.919 |
| hapax_ratio | -2.7 | 0.741 | 0.662 |
| n_symbols | -2.4 | 69.529 | 47.000 |
| rep_adjacent_ed1 | -1.9 | 0.043 | 0.030 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_rate | 0.012 | 0.0875 [0.0253, 0.109] | 78 |
| l_initial_forms_k | 1 | 0 [0, 3] | 25 |

### slotgram: medyan mesafe 2.83 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| n_symbols | -3.9 | 69.529 | 33.000 |
| zipf_slope | +2.9 | -0.776 | -0.647 |
| wlen_autocorr1 | -2.9 | 0.179 | 0.009 |
| char_double_rate | +2.5 | 0.015 | 0.028 |
| first_entropy_ratio | -2.0 | 0.886 | 0.822 |
| jsd_line_initial | -2.0 | 0.287 | 0.115 |

### slotcite: medyan mesafe 3.02 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +5.3 | 0.015 | 0.044 |
| rep_adjacent_exact | +3.5 | 0.006 | 0.014 |
| jsd_last | -3.4 | 0.679 | 0.506 |
| vocab_ed1_density | +2.8 | 0.854 | 0.918 |
| zipf_slope | +2.3 | -0.776 | -0.675 |
| wlen_autocorr1 | -2.2 | 0.179 | 0.047 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0 | 1.75 [0.872, 2.45] | 78 |
| l_allo_rate | 0 | 0.0844 [0.0474, 0.114] | 77 |

### plain: medyan mesafe 3.11 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | -6.0 | 0.854 | 0.715 |
| jsd_last | -5.7 | 0.679 | 0.386 |
| h2 | +5.5 | 2.383 | 3.327 |
| h2_over_h1 | +5.0 | 0.595 | 0.803 |
| rep_adjacent_ed1 | -4.6 | 0.043 | 0.010 |
| wlen_frac1 | -4.5 | 0.046 | 0.000 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_initial_forms_k | 0 | 3 [2, 3] | 81 |
| l_line_final_p | 0.237 | 0 [0, 0.358] | 20 |
| l_allo_per_glyph | 0.256 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0124 | 0 [0, 0] | 25 |

### abjad: medyan mesafe 3.22 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac1 | +5.8 | 0.046 | 0.106 |
| wlen_frac_le2 | +5.4 | 0.184 | 0.326 |
| h2 | +4.0 | 2.383 | 3.059 |
| h2_over_h1 | +3.8 | 0.595 | 0.753 |
| n_symbols | -3.8 | 69.529 | 34.000 |
| vocab_ed1_density | -3.5 | 0.854 | 0.773 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_final_forms_share | 0 | 0.572 [0.404, 0.749] | 77 |
| l_allo_per_glyph | 0.203 | 0 [0, 0.268] | 25 |
| l_allo_rate | 0.0102 | 0 [0, 0.0178] | 25 |

### verbose: medyan mesafe 3.43 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | +5.5 | 1.469 | 1.805 |
| type_len_mean | +4.3 | 4.440 | 4.956 |
| wlen_frac1 | +4.1 | 0.046 | 0.089 |
| jsd_last | -3.9 | 0.679 | 0.477 |
| hapax_ratio | -3.7 | 0.741 | 0.631 |
| char_double_rate | +3.6 | 0.015 | 0.035 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 88 |

### selfcite: medyan mesafe 3.84 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +9.5 | 0.015 | 0.067 |
| rep_adjacent_exact | +5.7 | 0.006 | 0.018 |
| h2 | +4.3 | 2.383 | 3.112 |
| h2_over_h1 | +3.8 | 0.595 | 0.751 |
| h1 | +3.7 | 4.005 | 4.129 |
| zipf_slope | +3.5 | -0.776 | -0.624 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_mut_double | 0.139 | 0.0186 [0.00563, 0.0517] | 12 |
| p_reach | 5 | 17.5 [11, 24] | 84 |
| p_same_line | 0.149 | 0.0613 [0.0292, 0.112] | 20 |


## zl_basic: sınıf sınıf

### grille: medyan mesafe 2.43 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | +2.8 | 0.823 | 0.882 |
| wlen_autocorr1 | -2.7 | 0.123 | -0.003 |
| rep_adjacent_ed1 | -2.6 | 0.034 | 0.016 |
| h2_over_h1 | +2.4 | 0.521 | 0.603 |
| h2 | +2.4 | 2.013 | 2.348 |
| hapax_ratio | -2.1 | 0.715 | 0.648 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 84 |
| l_initial_forms_k | 1 | 0 [0, 2] | 25 |

### slotcite: medyan mesafe 2.76 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| rep_adjacent_exact | +3.7 | 0.008 | 0.018 |
| h2_over_h1 | +3.1 | 0.521 | 0.625 |
| h2 | +3.0 | 2.013 | 2.428 |
| jsd_last | -2.7 | 0.712 | 0.589 |
| vocab_ed1_density | +2.3 | 0.823 | 0.874 |
| hapax_ratio | -2.0 | 0.715 | 0.651 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 83 |

### slotgram: medyan mesafe 2.86 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| zipf_slope | +3.5 | -0.785 | -0.548 |
| h2_over_h1 | +2.5 | 0.521 | 0.604 |
| h2 | +2.4 | 2.013 | 2.343 |
| word_entropy_norm | +2.3 | 0.799 | 0.882 |
| vocab_ed1_density | +2.3 | 0.823 | 0.873 |
| wlen_autocorr1 | -2.3 | 0.123 | 0.016 |

### verbose: medyan mesafe 3.37 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_skew | +5.6 | 0.025 | 0.595 |
| wlen_frac_le2 | +4.4 | 0.097 | 0.155 |
| hapax_ratio | -4.3 | 0.715 | 0.576 |
| wlen_std | +3.8 | 1.768 | 1.999 |
| jsd_last | -3.5 | 0.712 | 0.554 |
| wlen_autocorr1 | -3.4 | 0.123 | -0.036 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 88 |

### selfcite: medyan mesafe 4.00 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| rep_adjacent_exact | +6.3 | 0.008 | 0.024 |
| h2 | +5.9 | 2.013 | 2.836 |
| char_double_rate | +5.8 | 0.066 | 0.153 |
| h2_over_h1 | +5.6 | 0.521 | 0.710 |
| first_entropy_ratio | +4.8 | 0.817 | 0.898 |
| vocab_ed1_density | +4.4 | 0.823 | 0.917 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 5 | 17 [12.8, 22.2] | 84 |
| p_mut_prefix | 0.16 | 0.369 [0.223, 0.51] | 81 |
| p_same_line | 0.149 | 0.0634 [0.0286, 0.138] | 21 |
| l_final_forms_share | 0 | 0.549 [0.155, 0.776] | 76 |

### plain: medyan mesafe 4.75 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 19

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| eff_symbols | +9.7 | 14.493 | 18.357 |
| h2 | +7.6 | 2.013 | 3.074 |
| h1 | +6.7 | 3.862 | 4.084 |
| h2_over_h1 | +6.7 | 0.521 | 0.747 |
| vocab_ed1_density | -6.5 | 0.823 | 0.683 |
| type_len_mean | -4.8 | 5.640 | 4.771 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.256 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0124 | 0 [0, 0] | 25 |

### abjad: medyan mesafe 5.33 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac_le2 | +16.6 | 0.097 | 0.319 |
| first_entropy_ratio | +9.1 | 0.817 | 0.971 |
| wlen_frac1 | +7.3 | 0.033 | 0.107 |
| type_len_mean | -7.1 | 5.640 | 4.350 |
| wlen_mean | -6.8 | 4.961 | 3.424 |
| h2_over_h1 | +6.7 | 0.521 | 0.745 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_final_forms_share | 0 | 0.572 [0.391, 0.812] | 77 |
| l_allo_per_glyph | 0.203 | 0 [0, 0.33] | 25 |
| l_allo_rate | 0.0102 | 0 [0, 0.0172] | 25 |


## zl_glyph: sınıf sınıf

### grille: medyan mesafe 2.15 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 2

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | +3.1 | 0.852 | 0.901 |
| wlen_autocorr1 | -2.4 | 0.102 | 0.006 |
| h2_over_h1 | +1.9 | 0.554 | 0.630 |
| first_entropy_ratio | -1.7 | 0.875 | 0.833 |
| h2 | +1.6 | 2.127 | 2.413 |
| rep_adjacent_ed1 | -1.6 | 0.041 | 0.025 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_initial_forms_k | 1 | 0 [0, 1.25] | 25 |

### slotcite: medyan mesafe 2.43 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| rep_adjacent_exact | +3.2 | 0.008 | 0.017 |
| first_entropy_ratio | -2.3 | 0.875 | 0.818 |
| h2 | +2.2 | 2.127 | 2.507 |
| h2_over_h1 | +2.2 | 0.554 | 0.642 |
| jsd_last | -2.0 | 0.712 | 0.620 |
| vocab_ed1_density | +1.8 | 0.852 | 0.880 |

### slotgram: medyan mesafe 2.54 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_autocorr1 | -2.3 | 0.102 | 0.011 |
| zipf_slope | +2.2 | -0.785 | -0.637 |
| n_symbols | -2.2 | 44.750 | 24.000 |
| vocab_ed1_density | +2.1 | 0.852 | 0.885 |
| jsd_line_final | -2.0 | 0.110 | 0.033 |
| h2_over_h1 | +1.8 | 0.554 | 0.629 |

### verbose: medyan mesafe 3.01 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | +5.0 | 1.615 | 1.893 |
| wlen_skew | +4.8 | 0.154 | 0.641 |
| jsd_last | -4.1 | 0.712 | 0.525 |
| hapax_ratio | -4.0 | 0.715 | 0.588 |
| wlen_autocorr1 | -3.4 | 0.102 | -0.035 |
| ttr | -2.7 | 0.434 | 0.267 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 88 |

### selfcite: medyan mesafe 3.17 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| rep_adjacent_exact | +4.9 | 0.008 | 0.021 |
| h2 | +4.3 | 2.127 | 2.886 |
| vocab_ed1_density | +4.3 | 0.852 | 0.920 |
| h2_over_h1 | +4.2 | 0.554 | 0.725 |
| char_double_rate | +3.0 | 0.076 | 0.123 |
| h1 | +3.0 | 3.836 | 3.957 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 5 | 18 [13, 24] | 85 |
| p_same_line | 0.149 | 0.0667 [0.0309, 0.121] | 22 |

### abjad: medyan mesafe 3.53 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac1 | +7.4 | 0.033 | 0.112 |
| wlen_frac_le2 | +6.2 | 0.119 | 0.325 |
| wlen_skew | +5.4 | 0.154 | 0.700 |
| h2_over_h1 | +4.6 | 0.554 | 0.743 |
| first_entropy_ratio | +4.6 | 0.875 | 0.989 |
| vocab_ed1_density | -4.4 | 0.852 | 0.782 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_initial_p | 0.234 | 0 [0, 0.489] | 20 |
| l_final_forms_share | 0 | 0.618 [0.407, 0.799] | 80 |
| l_allo_per_glyph | 0.203 | 0 [0, 0.33] | 25 |
| l_allo_rate | 0.0102 | 0 [0, 0.0171] | 25 |

### plain: medyan mesafe 3.94 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | -8.1 | 0.852 | 0.723 |
| eff_symbols | +6.6 | 14.529 | 18.778 |
| h1 | +6.6 | 3.836 | 4.105 |
| h2 | +6.3 | 2.127 | 3.235 |
| h2_over_h1 | +5.7 | 0.554 | 0.787 |
| wlen_std | -5.0 | 1.615 | 1.339 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.256 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0124 | 0 [0, 0] | 25 |
