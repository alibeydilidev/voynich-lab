# ABC raporu: her hipotez Voynich'e ne kadar yaklaşabiliyor

Sentetik örnek: 60400. Her sınıfta Voynich'e en yakın %1 kabul edildi.

Mesafe birimi Voynich'in kendi pencereleri arasındaki değişkenliktir. "Voynich öz mesafesi" bir Voynich penceresinin diğerlerinin ortalamasına uzaklığıdır; bir hipotezin mesafesi bu aralığa girmiyorsa o hipotez Voynich'i (bu feature kümesinde) üretemiyor demektir.

## 1. Kabul edilen örneklerin medyan mesafesi

| görünüm | Voynich öz mesafesi (medyan, en çok) | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.91, 1.65 | 6.19 | 2.77 | 5.35 | 4.46 | 3.10 | 3.26 | 3.99 |
| eva_glyph | 0.96, 1.64 | 3.96 | 2.49 | 4.20 | 3.57 | 2.82 | 2.94 | 3.57 |
| v101 | 0.97, 1.42 | 3.36 | 2.53 | 3.02 | 3.90 | 2.95 | 2.84 | 3.27 |
| zl_basic | 0.96, 1.52 | 5.36 | 2.44 | 4.71 | 3.96 | 2.73 | 2.94 | 3.26 |
| zl_glyph | 1.03, 1.43 | 3.54 | 2.15 | 3.76 | 3.12 | 2.43 | 2.51 | 2.89 |

## 2. En iyi tek örneğin mesafesi

| görünüm | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|
| eva_basic | 4.98 | 1.74 | 3.94 | 3.48 | 2.42 | 2.14 | 3.12 |
| eva_glyph | 3.17 | 1.50 | 2.98 | 2.83 | 1.86 | 2.12 | 2.59 |
| v101 | 2.63 | 1.74 | 2.29 | 2.88 | 2.05 | 1.96 | 2.34 |
| zl_basic | 4.35 | 1.67 | 3.54 | 2.96 | 2.02 | 2.25 | 2.54 |
| zl_glyph | 2.94 | 1.48 | 2.87 | 2.43 | 1.52 | 1.72 | 2.11 |

## 3. Voynich'in en uç penceresi kadar yakın olan örneklerin oranı

| görünüm | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|
| eva_basic | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| eva_glyph | %0.00 | %0.01 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| v101 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| zl_basic | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| zl_glyph | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |

## eva_basic: sınıf sınıf

### grille: medyan mesafe 2.77 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_autocorr1 | -3.3 | 0.127 | 0.000 |
| h2 | +3.1 | 2.016 | 2.390 |
| h2_over_h1 | +3.0 | 0.524 | 0.616 |
| hapax_ratio | -2.9 | 0.717 | 0.653 |
| jsd_line_final | -2.6 | 0.109 | 0.026 |
| rep_adjacent_ed1 | -2.6 | 0.032 | 0.015 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 83 |
| l_allo_per_glyph | 0.215 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0108 | 0 [0, 0] | 25 |

### slotcite: medyan mesafe 3.10 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -4.7 | 0.717 | 0.613 |
| h2 | +3.7 | 2.016 | 2.458 |
| h2_over_h1 | +3.7 | 0.524 | 0.638 |
| zipf_slope | +3.3 | -0.778 | -0.568 |
| jsd_last | -3.2 | 0.719 | 0.567 |
| rep_adjacent_exact | +2.6 | 0.009 | 0.017 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 83 |
| p_exact | 0.4 | 0.22 [0.154, 0.348] | 20 |
| l_initial_forms_k | 1 | 0 [0, 3] | 24 |
| l_allo_per_glyph | 0.222 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0109 | 0 [0, 0] | 25 |
| l_final_forms_k | 1 | 0 [0, 2] | 25 |

### slotgram: medyan mesafe 3.26 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| zipf_slope | +4.3 | -0.778 | -0.508 |
| wlen_autocorr1 | -2.9 | 0.127 | 0.014 |
| vocab_ed1_density | +2.9 | 0.823 | 0.895 |
| top10_coverage | -2.6 | 0.171 | 0.076 |
| jsd_last | -2.4 | 0.719 | 0.604 |
| jsd_line_final | -2.3 | 0.109 | 0.034 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.233 | 0 [0, 0.377] | 20 |
| l_allo_per_glyph | 0.281 | 0 [0, 0] | 24 |
| l_allo_rate | 0.0149 | 0 [0, 0] | 24 |
| l_initial_forms_k | 1 | 0 [0, 1.5] | 24 |

### verbose: medyan mesafe 3.99 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -8.9 | 0.717 | 0.520 |
| wlen_frac_le2 | +5.5 | 0.077 | 0.141 |
| jsd_last | -5.2 | 0.719 | 0.472 |
| wlen_autocorr1 | -4.5 | 0.127 | -0.044 |
| wlen_std | +4.1 | 1.693 | 1.993 |
| wlen_skew | +4.1 | 0.074 | 0.600 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 88 |

### selfcite: medyan mesafe 4.46 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +7.1 | 2.016 | 2.872 |
| h2_over_h1 | +6.9 | 0.524 | 0.740 |
| char_double_rate | +6.5 | 0.067 | 0.156 |
| rep_adjacent_exact | +5.2 | 0.009 | 0.025 |
| hapax_ratio | -5.1 | 0.717 | 0.604 |
| first_entropy_ratio | +4.7 | 0.806 | 0.890 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 5 | 18 [12, 23.2] | 85 |
| p_alphabet | 20 | 17 [16, 19] | 23 |
| l_allo_per_glyph | 0.213 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0105 | 0 [0, 0] | 25 |

### plain: medyan mesafe 5.35 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| eff_symbols | +10.8 | 14.240 | 17.785 |
| h1 | +9.2 | 3.845 | 4.060 |
| h2 | +8.2 | 2.016 | 3.006 |
| h2_over_h1 | +7.0 | 0.524 | 0.741 |
| n_symbols | +6.8 | 19.562 | 28.000 |
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

### grille: medyan mesafe 2.49 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_autocorr1 | -3.1 | 0.103 | 0.001 |
| hapax_ratio | -2.8 | 0.717 | 0.655 |
| vocab_ed1_density | +2.5 | 0.850 | 0.905 |
| h2_over_h1 | +2.1 | 0.556 | 0.634 |
| rep_within3 | -2.1 | 0.026 | 0.011 |
| first_entropy_ratio | -2.0 | 0.867 | 0.822 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_final_forms_k | 1 | 0 [0, 2] | 25 |
| l_allo_per_glyph | 0.215 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0108 | 0 [0, 0] | 25 |

### slotcite: medyan mesafe 2.82 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -3.9 | 0.717 | 0.631 |
| jsd_last | -3.2 | 0.718 | 0.565 |
| rep_adjacent_exact | +2.9 | 0.009 | 0.018 |
| first_entropy_ratio | -2.5 | 0.867 | 0.810 |
| h2_over_h1 | +2.5 | 0.556 | 0.651 |
| zipf_slope | +2.5 | -0.778 | -0.621 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_exact | 0.4 | 0.225 [0.172, 0.353] | 21 |
| l_initial_forms_k | 1 | 0 [0, 3] | 24 |
| l_allo_per_glyph | 0.222 | 0 [0, 0.475] | 25 |
| l_allo_rate | 0.0109 | 0 [0, 0.0622] | 25 |
| l_final_forms_k | 1 | 0 [0, 2] | 25 |

### slotgram: medyan mesafe 2.94 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_autocorr1 | -2.8 | 0.103 | 0.011 |
| zipf_slope | +2.7 | -0.778 | -0.611 |
| vocab_ed1_density | +2.5 | 0.850 | 0.907 |
| jsd_last | -2.4 | 0.718 | 0.603 |
| first_entropy_ratio | -2.4 | 0.867 | 0.814 |
| wlen_frac1 | +1.9 | 0.017 | 0.040 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.281 | 0 [0, 0.398] | 24 |
| l_allo_rate | 0.0149 | 0 [0, 0.0669] | 24 |
| l_initial_forms_k | 1 | 0 [0, 3] | 24 |

### selfcite: medyan mesafe 3.57 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -5.3 | 0.717 | 0.599 |
| h2_over_h1 | +5.0 | 0.556 | 0.745 |
| h2 | +5.0 | 2.131 | 2.911 |
| rep_adjacent_exact | +4.5 | 0.009 | 0.022 |
| char_double_rate | +3.8 | 0.076 | 0.131 |
| vocab_ed1_density | +3.7 | 0.850 | 0.932 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 5 | 19 [13, 24.2] | 86 |
| p_same_line | 0.149 | 0.0659 [0.025, 0.118] | 22 |
| l_allo_per_glyph | 0.213 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0105 | 0 [0, 0] | 25 |

### verbose: medyan mesafe 3.57 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -6.6 | 0.717 | 0.570 |
| wlen_std | +5.8 | 1.552 | 1.858 |
| jsd_last | -5.2 | 0.718 | 0.469 |
| wlen_autocorr1 | -4.1 | 0.103 | -0.035 |
| wlen_skew | +3.9 | 0.183 | 0.592 |
| ttr | -3.5 | 0.443 | 0.251 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 88 |
| l_final_forms_share | 0.11 | 0 [0, 0.585] | 25 |

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

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h1 | +8.9 | 3.832 | 4.076 |
| eff_symbols | +8.8 | 14.404 | 18.503 |
| h2 | +7.5 | 2.131 | 3.294 |
| vocab_ed1_density | -6.6 | 0.850 | 0.704 |
| h2_over_h1 | +6.5 | 0.556 | 0.800 |
| jsd_last | -6.1 | 0.718 | 0.427 |


## v101: sınıf sınıf

### grille: medyan mesafe 2.53 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +4.0 | 0.015 | 0.037 |
| wlen_autocorr1 | -2.9 | 0.179 | 0.004 |
| vocab_ed1_density | +2.7 | 0.854 | 0.917 |
| n_symbols | -2.2 | 69.529 | 48.500 |
| hapax_ratio | -2.2 | 0.741 | 0.675 |
| jsd_last | -2.1 | 0.679 | 0.569 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.215 | 1.81 [0.919, 2.38] | 78 |
| l_allo_rate | 0.0108 | 0.0872 [0.0466, 0.112] | 78 |

### slotgram: medyan mesafe 2.84 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| n_symbols | -3.4 | 69.529 | 38.000 |
| char_double_rate | +3.2 | 0.015 | 0.032 |
| wlen_autocorr1 | -2.9 | 0.179 | 0.004 |
| zipf_slope | +2.1 | -0.776 | -0.683 |
| rep_within3 | -2.0 | 0.021 | 0.011 |
| top10_coverage | -1.8 | 0.166 | 0.124 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_initial_forms_k | 1 | 0 [0, 3] | 24 |

### slotcite: medyan mesafe 2.95 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +5.0 | 0.015 | 0.042 |
| rep_adjacent_exact | +3.5 | 0.006 | 0.014 |
| vocab_ed1_density | +2.7 | 0.854 | 0.916 |
| jsd_last | -2.5 | 0.679 | 0.553 |
| n_symbols | -2.3 | 69.529 | 47.500 |
| wlen_autocorr1 | -2.2 | 0.179 | 0.046 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_exact | 0.4 | 0.22 [0.17, 0.359] | 20 |
| l_allo_rate | 0.0109 | 0.092 [0.0386, 0.125] | 79 |
| l_allo_per_glyph | 0.222 | 1.72 [0.617, 2.54] | 77 |
| p_same_line | 0.252 | 0.118 [0.0574, 0.24] | 23 |
| l_initial_forms_k | 1 | 0 [0, 1] | 24 |
| l_final_forms_k | 1 | 0 [0, 3] | 25 |

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

### selfcite: medyan mesafe 3.90 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +9.0 | 0.015 | 0.064 |
| rep_adjacent_exact | +6.1 | 0.006 | 0.019 |
| h2 | +4.4 | 2.383 | 3.128 |
| jsd_last | -4.1 | 0.679 | 0.469 |
| h2_over_h1 | +4.0 | 0.595 | 0.759 |
| rep_within3 | +3.7 | 0.021 | 0.041 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_mut_double | 0.136 | 0.0134 [0.00585, 0.0429] | 10 |
| p_reach | 5 | 18 [12, 23] | 85 |
| p_same_line | 0.149 | 0.0605 [0.0341, 0.119] | 20 |


## zl_basic: sınıf sınıf

### grille: medyan mesafe 2.44 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | +3.0 | 0.823 | 0.888 |
| wlen_autocorr1 | -2.5 | 0.123 | 0.005 |
| h2 | +2.4 | 2.013 | 2.343 |
| h2_over_h1 | +2.4 | 0.521 | 0.601 |
| hapax_ratio | -2.2 | 0.715 | 0.645 |
| rep_adjacent_ed1 | -2.0 | 0.034 | 0.020 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 83 |

### slotcite: medyan mesafe 2.73 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2_over_h1 | +3.1 | 0.521 | 0.627 |
| h2 | +2.9 | 2.013 | 2.418 |
| jsd_last | -2.8 | 0.712 | 0.583 |
| rep_adjacent_exact | +2.4 | 0.008 | 0.015 |
| hapax_ratio | -2.3 | 0.715 | 0.641 |
| vocab_ed1_density | +2.2 | 0.823 | 0.871 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 83 |
| p_exact | 0.4 | 0.216 [0.149, 0.389] | 20 |
| l_line_final_p | 0.232 | 0 [0, 0.377] | 20 |
| l_initial_forms_k | 1 | 0 [0, 2] | 24 |

### slotgram: medyan mesafe 2.94 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| zipf_slope | +2.7 | -0.785 | -0.603 |
| vocab_ed1_density | +2.6 | 0.823 | 0.878 |
| wlen_autocorr1 | -2.4 | 0.123 | 0.011 |
| h2_over_h1 | +2.2 | 0.521 | 0.594 |
| top10_coverage | -2.0 | 0.175 | 0.101 |
| h2 | +1.9 | 2.013 | 2.282 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.281 | 0 [0, 0.926] | 24 |
| l_allo_rate | 0.0149 | 0 [0, 0.0812] | 24 |
| l_initial_forms_k | 1 | 0 [0, 1] | 24 |

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

### selfcite: medyan mesafe 3.96 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +6.0 | 2.013 | 2.854 |
| h2_over_h1 | +5.8 | 0.521 | 0.715 |
| char_double_rate | +5.6 | 0.066 | 0.149 |
| rep_adjacent_exact | +5.5 | 0.008 | 0.022 |
| first_entropy_ratio | +4.6 | 0.817 | 0.896 |
| type_len_mean | -4.2 | 5.640 | 4.884 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 5 | 17.5 [12, 23.2] | 84 |
| p_same_line | 0.149 | 0.0602 [0.0268, 0.118] | 20 |
| l_line_final_p | 0.227 | 0 [0, 0.371] | 20 |
| p_alphabet | 20 | 17 [16, 20] | 23 |
| l_allo_per_glyph | 0.213 | 0 [0, 0.936] | 25 |
| l_allo_rate | 0.0105 | 0 [0, 0.053] | 25 |

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

### grille: medyan mesafe 2.15 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 3

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | +2.9 | 0.852 | 0.898 |
| wlen_autocorr1 | -2.5 | 0.102 | 0.001 |
| jsd_last | -2.0 | 0.712 | 0.620 |
| h2_over_h1 | +1.9 | 0.554 | 0.632 |
| hapax_ratio | -1.8 | 0.715 | 0.657 |
| rep_adjacent_ed1 | -1.8 | 0.041 | 0.024 |

### slotcite: medyan mesafe 2.43 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| rep_adjacent_exact | +2.4 | 0.008 | 0.015 |
| jsd_last | -2.3 | 0.712 | 0.605 |
| h2_over_h1 | +2.2 | 0.554 | 0.642 |
| h2 | +2.1 | 2.127 | 2.500 |
| vocab_ed1_density | +1.8 | 0.852 | 0.880 |
| h1 | +1.8 | 3.836 | 3.909 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.232 | 0 [0, 0.328] | 20 |
| l_initial_forms_k | 1 | 0 [0, 2.25] | 24 |
| l_final_forms_k | 1 | 0 [0, 3] | 25 |

### slotgram: medyan mesafe 2.51 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 2

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_autocorr1 | -2.3 | 0.102 | 0.010 |
| vocab_ed1_density | +2.2 | 0.852 | 0.888 |
| n_symbols | -2.0 | 44.750 | 26.000 |
| zipf_slope | +1.9 | -0.785 | -0.656 |
| wlen_std | +1.8 | 1.615 | 1.712 |
| jsd_line_initial | -1.8 | 0.266 | 0.106 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_initial_forms_k | 1 | 0 [0, 3] | 24 |

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

### selfcite: medyan mesafe 3.12 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| rep_adjacent_exact | +5.1 | 0.008 | 0.021 |
| h2 | +4.5 | 2.127 | 2.920 |
| h2_over_h1 | +4.3 | 0.554 | 0.731 |
| vocab_ed1_density | +3.5 | 0.852 | 0.909 |
| h1 | +3.4 | 3.836 | 3.975 |
| eff_symbols | +3.1 | 14.529 | 16.491 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 5 | 18 [13, 23] | 85 |
| p_same_line | 0.149 | 0.0562 [0.0259, 0.11] | 19 |
| l_final_forms_share | 0 | 0.553 [0.293, 0.732] | 76 |

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
