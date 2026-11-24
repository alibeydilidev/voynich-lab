# ABC raporu: her hipotez Voynich'e ne kadar yaklaşabiliyor

Sentetik örnek: 69200. Her sınıfta Voynich'e en yakın %1 kabul edildi.

Mesafe birimi Voynich'in kendi pencereleri arasındaki değişkenliktir. "Voynich öz mesafesi" bir Voynich penceresinin diğerlerinin ortalamasına uzaklığıdır; bir hipotezin mesafesi bu aralığa girmiyorsa o hipotez Voynich'i (bu feature kümesinde) üretemiyor demektir.

## 1. Kabul edilen örneklerin medyan mesafesi

| görünüm | Voynich öz mesafesi (medyan, en çok) | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.91, 1.65 | 6.18 | 4.76 | 2.86 | 5.36 | 4.48 | 3.10 | 3.36 | 4.06 |
| eva_glyph | 0.96, 1.64 | 4.04 | 4.31 | 2.54 | 4.13 | 3.53 | 2.84 | 2.93 | 3.59 |
| v101 | 0.97, 1.42 | 3.27 | 3.94 | 2.60 | 3.05 | 3.83 | 2.96 | 2.83 | 3.41 |
| zl_basic | 0.96, 1.52 | 5.40 | 4.77 | 2.47 | 4.66 | 3.94 | 2.62 | 2.97 | 3.37 |
| zl_glyph | 1.03, 1.43 | 3.61 | 4.04 | 2.15 | 3.76 | 3.10 | 2.27 | 2.49 | 2.99 |

## 2. En iyi tek örneğin mesafesi

| görünüm | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | 5.29 | 3.99 | 2.27 | 3.80 | 3.58 | 2.51 | 2.31 | 2.49 |
| eva_glyph | 3.29 | 3.25 | 2.00 | 2.91 | 2.92 | 1.91 | 2.16 | 2.38 |
| v101 | 2.47 | 3.25 | 1.79 | 2.10 | 2.76 | 2.08 | 2.07 | 2.47 |
| zl_basic | 4.40 | 3.80 | 1.79 | 3.28 | 3.04 | 2.10 | 2.14 | 2.11 |
| zl_glyph | 2.89 | 2.86 | 1.73 | 2.80 | 2.45 | 1.63 | 1.79 | 2.20 |

## 3. Voynich'in en uç penceresi kadar yakın olan örneklerin oranı

| görünüm | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| eva_glyph | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| v101 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| zl_basic | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| zl_glyph | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |

## eva_basic: sınıf sınıf

### grille: medyan mesafe 2.86 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +3.4 | 2.016 | 2.427 |
| h2_over_h1 | +3.3 | 0.524 | 0.627 |
| wlen_autocorr1 | -3.2 | 0.127 | 0.005 |
| jsd_line_final | -2.9 | 0.109 | 0.016 |
| rep_adjacent_ed1 | -2.8 | 0.032 | 0.013 |
| hapax_ratio | -2.8 | 0.717 | 0.655 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 83 |
| l_line_final_p | 0.239 | 0 [0, 0.402] | 20 |

### slotcite: medyan mesafe 3.10 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -5.8 | 0.717 | 0.589 |
| h2 | +3.4 | 2.016 | 2.427 |
| h2_over_h1 | +3.3 | 0.524 | 0.627 |
| rep_adjacent_exact | +3.3 | 0.009 | 0.019 |
| zipf_slope | +3.1 | -0.778 | -0.584 |
| jsd_last | -3.0 | 0.719 | 0.575 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 83 |
| p_exact | 0.396 | 0.217 [0.17, 0.328] | 20 |
| l_allo_per_glyph | 0.224 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0111 | 0 [0, 0] | 25 |

### slotgram: medyan mesafe 3.36 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| zipf_slope | +3.7 | -0.778 | -0.545 |
| jsd_last | -3.4 | 0.719 | 0.558 |
| wlen_autocorr1 | -2.7 | 0.127 | 0.022 |
| h2_over_h1 | +2.7 | 0.524 | 0.608 |
| h2 | +2.6 | 2.016 | 2.328 |
| word_entropy_norm | +2.6 | 0.804 | 0.887 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.24 | 0 [0, 0.0789] | 25 |
| l_allo_rate | 0.0119 | 0 [0, 0.0044] | 25 |

### verbose: medyan mesafe 4.06 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -8.2 | 0.717 | 0.536 |
| wlen_frac_le2 | +6.7 | 0.077 | 0.154 |
| jsd_last | -5.6 | 0.719 | 0.455 |
| wlen_autocorr1 | -4.3 | 0.127 | -0.038 |
| ttr | -3.8 | 0.443 | 0.235 |
| wlen_skew | +3.8 | 0.074 | 0.560 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 87 |

### selfcite: medyan mesafe 4.48 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 19

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +7.3 | 2.016 | 2.895 |
| h2_over_h1 | +6.7 | 0.524 | 0.733 |
| char_double_rate | +5.9 | 0.067 | 0.148 |
| rep_adjacent_exact | +5.6 | 0.009 | 0.026 |
| hapax_ratio | -5.3 | 0.717 | 0.598 |
| type_len_mean | -5.1 | 5.692 | 4.827 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 6 | 18 [13, 23] | 85 |
| p_affix | 0.602 | 0.774 [0.606, 0.845] | 79 |
| p_alphabet | 20 | 17 [16, 19] | 22 |
| p_same_line | 0.149 | 0.0735 [0.0273, 0.128] | 25 |
| l_allo_per_glyph | 0.211 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0105 | 0 [0, 0] | 25 |

### codebook: medyan mesafe 4.76 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | -13.5 | 1.693 | 0.705 |
| type_len_mean | -8.6 | 5.692 | 4.228 |
| vocab_ed1_density | +6.7 | 0.823 | 0.989 |
| wlen_frac_le2 | -5.6 | 0.077 | 0.011 |
| wlen_mean | -4.4 | 5.066 | 4.047 |
| jsd_first | +4.3 | 0.385 | 0.532 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_slot_overlap | 0.502 | 0.125 [0.0562, 0.19] | 13 |
| p_order | 1 | 2 [1, 2] | 84 |
| l_final_forms_k | 1 | 0 [0, 3] | 25 |
| p_zero_empty | 1 | 0 [0, 1] | 25 |
| l_allo_per_glyph | 0.2 | 0 [0, 0.738] | 25 |
| l_allo_rate | 0.0101 | 0 [0, 0.0823] | 25 |

### plain: medyan mesafe 5.36 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| eff_symbols | +10.9 | 14.240 | 17.797 |
| h1 | +9.0 | 3.845 | 4.056 |
| h2 | +8.2 | 2.016 | 3.010 |
| h2_over_h1 | +7.0 | 0.524 | 0.742 |
| n_symbols | +6.1 | 19.562 | 27.000 |
| type_len_mean | -5.7 | 5.692 | 4.714 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.249 | 0 [0, 0.336] | 20 |
| l_allo_per_glyph | 0.212 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |

### abjad: medyan mesafe 6.18 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac_le2 | +21.3 | 0.077 | 0.323 |
| first_entropy_ratio | +8.9 | 0.806 | 0.966 |
| wlen_frac1 | +8.7 | 0.017 | 0.114 |
| h2_over_h1 | +7.5 | 0.524 | 0.755 |
| type_len_mean | -7.4 | 5.692 | 4.422 |
| wlen_mean | -7.0 | 5.066 | 3.444 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.231 | 0 [0, 0.419] | 20 |


## eva_glyph: sınıf sınıf

### grille: medyan mesafe 2.54 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_autocorr1 | -3.0 | 0.103 | 0.002 |
| hapax_ratio | -2.7 | 0.717 | 0.656 |
| vocab_ed1_density | +2.6 | 0.850 | 0.908 |
| h2_over_h1 | +2.2 | 0.556 | 0.640 |
| jsd_line_final | -2.2 | 0.110 | 0.041 |
| rep_within3 | -2.1 | 0.026 | 0.011 |

### slotcite: medyan mesafe 2.84 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -4.5 | 0.717 | 0.617 |
| rep_adjacent_exact | +3.2 | 0.009 | 0.019 |
| zipf_slope | +2.9 | -0.778 | -0.594 |
| h2 | +2.4 | 2.131 | 2.507 |
| first_entropy_ratio | -2.4 | 0.867 | 0.814 |
| h2_over_h1 | +2.4 | 0.556 | 0.645 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_exact | 0.396 | 0.245 [0.167, 0.35] | 24 |
| p_same_line | 0.248 | 0.121 [0.0549, 0.235] | 25 |
| l_allo_per_glyph | 0.224 | 0 [0, 0.557] | 25 |
| l_allo_rate | 0.0111 | 0 [0, 0.083] | 25 |

### slotgram: medyan mesafe 2.93 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| zipf_slope | +2.9 | -0.778 | -0.596 |
| wlen_autocorr1 | -2.7 | 0.103 | 0.013 |
| vocab_ed1_density | +2.2 | 0.850 | 0.900 |
| first_entropy_ratio | -2.2 | 0.867 | 0.817 |
| wlen_frac1 | +2.1 | 0.017 | 0.042 |
| jsd_last | -2.0 | 0.718 | 0.621 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.24 | 0 [0, 0.737] | 25 |
| l_allo_rate | 0.0119 | 0 [0, 0.0538] | 25 |

### selfcite: medyan mesafe 3.53 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -5.3 | 0.717 | 0.599 |
| h2 | +5.1 | 2.131 | 2.929 |
| rep_adjacent_exact | +4.9 | 0.009 | 0.024 |
| h2_over_h1 | +4.8 | 0.556 | 0.738 |
| h1 | +4.4 | 3.832 | 3.951 |
| rep_within3 | +3.6 | 0.026 | 0.053 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 6 | 18 [12, 23.2] | 85 |
| p_same_line | 0.149 | 0.0735 [0.0235, 0.129] | 25 |
| l_allo_per_glyph | 0.211 | 0 [0, 0.0542] | 25 |
| l_allo_rate | 0.0105 | 0 [0, 0.00251] | 25 |

### verbose: medyan mesafe 3.59 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -7.0 | 0.717 | 0.561 |
| wlen_std | +6.2 | 1.552 | 1.874 |
| jsd_last | -4.1 | 0.718 | 0.523 |
| wlen_autocorr1 | -4.1 | 0.103 | -0.032 |
| wlen_skew | +4.0 | 0.183 | 0.608 |
| ttr | -3.7 | 0.443 | 0.243 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 87 |
| l_initial_forms_k | 1 | 0 [0, 3] | 25 |

### abjad: medyan mesafe 4.04 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac1 | +8.6 | 0.017 | 0.118 |
| wlen_frac_le2 | +7.6 | 0.099 | 0.336 |
| first_entropy_ratio | +5.2 | 0.867 | 0.983 |
| h2_over_h1 | +5.2 | 0.556 | 0.751 |
| wlen_skew | +5.1 | 0.183 | 0.729 |
| h2 | +4.6 | 2.131 | 2.848 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_final_forms_share | 0.117 | 0.607 [0.271, 0.802] | 77 |

### plain: medyan mesafe 4.13 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h1 | +9.0 | 3.832 | 4.077 |
| eff_symbols | +8.5 | 14.404 | 18.384 |
| h2 | +6.9 | 2.131 | 3.207 |
| h2_over_h1 | +6.0 | 0.556 | 0.782 |
| vocab_ed1_density | -6.0 | 0.850 | 0.718 |
| char_double_rate | -4.6 | 0.076 | 0.009 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.249 | 0 [0, 0.318] | 20 |
| l_allo_per_glyph | 0.212 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |

### codebook: medyan mesafe 4.31 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | -13.5 | 1.552 | 0.846 |
| type_len_mean | -6.4 | 5.032 | 3.658 |
| vocab_ed1_density | +6.2 | 0.850 | 0.989 |
| wlen_skew | -3.7 | 0.183 | -0.210 |
| jsd_first | +3.7 | 0.350 | 0.501 |
| wlen_mean | -3.6 | 4.528 | 3.417 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_slot_overlap | 0.502 | 0.0983 [0.0562, 0.158] | 11 |
| p_order | 1 | 2 [1, 2] | 84 |
| p_len_max | 2 | 1 [1, 2] | 25 |
| l_final_forms_k | 1 | 0 [0, 2] | 25 |


## v101: sınıf sınıf

### grille: medyan mesafe 2.60 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +3.8 | 0.015 | 0.036 |
| wlen_autocorr1 | -3.0 | 0.179 | 0.003 |
| n_symbols | -2.8 | 69.529 | 43.000 |
| vocab_ed1_density | +2.7 | 0.854 | 0.916 |
| hapax_ratio | -2.4 | 0.741 | 0.672 |
| rep_adjacent_ed1 | -2.0 | 0.043 | 0.029 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_initial_forms_k | 1 | 0 [0, 1.75] | 25 |

### slotgram: medyan mesafe 2.83 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| n_symbols | -3.8 | 69.529 | 34.000 |
| char_double_rate | +2.9 | 0.015 | 0.031 |
| wlen_autocorr1 | -2.8 | 0.179 | 0.014 |
| wlen_frac1 | +2.1 | 0.046 | 0.068 |
| zipf_slope | +2.0 | -0.776 | -0.688 |
| wlen_frac_le2 | +1.9 | 0.184 | 0.233 |

### slotcite: medyan mesafe 2.96 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +5.3 | 0.015 | 0.044 |
| rep_adjacent_exact | +3.4 | 0.006 | 0.014 |
| vocab_ed1_density | +2.8 | 0.854 | 0.918 |
| n_symbols | -2.7 | 69.529 | 44.000 |
| wlen_frac1 | -2.6 | 0.046 | 0.019 |
| first_entropy_ratio | -2.3 | 0.886 | 0.812 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_rate | 0.0111 | 0.0888 [0.0417, 0.115] | 79 |
| l_allo_per_glyph | 0.224 | 1.62 [0.748, 2.24] | 76 |

### plain: medyan mesafe 3.05 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | -5.3 | 0.854 | 0.732 |
| h2 | +5.2 | 2.383 | 3.263 |
| rep_adjacent_ed1 | -4.6 | 0.043 | 0.010 |
| h2_over_h1 | +4.6 | 0.595 | 0.784 |
| wlen_frac1 | -4.5 | 0.046 | 0.000 |
| n_symbols | -4.4 | 69.529 | 28.000 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.249 | 0 [0, 0.301] | 20 |
| l_allo_per_glyph | 0.212 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |

### abjad: medyan mesafe 3.27 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac1 | +5.9 | 0.046 | 0.107 |
| wlen_frac_le2 | +5.4 | 0.184 | 0.328 |
| h2 | +4.1 | 2.383 | 3.087 |
| h2_over_h1 | +4.0 | 0.595 | 0.762 |
| n_symbols | -3.8 | 69.529 | 34.000 |
| vocab_ed1_density | -3.5 | 0.854 | 0.772 |

### verbose: medyan mesafe 3.41 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | +5.3 | 1.469 | 1.798 |
| wlen_frac1 | +4.5 | 0.046 | 0.092 |
| type_len_mean | +4.4 | 4.440 | 4.977 |
| hapax_ratio | -4.0 | 0.741 | 0.622 |
| n_symbols | -3.7 | 69.529 | 35.000 |
| jsd_last | -3.5 | 0.679 | 0.500 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 87 |
| l_initial_forms_k | 1 | 0 [0, 2] | 25 |

### selfcite: medyan mesafe 3.83 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +8.9 | 0.015 | 0.063 |
| rep_adjacent_exact | +6.4 | 0.006 | 0.020 |
| rep_within3 | +4.2 | 0.021 | 0.043 |
| h2 | +4.1 | 2.383 | 3.076 |
| h2_over_h1 | +3.6 | 0.595 | 0.744 |
| h1 | +3.5 | 4.005 | 4.122 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_mut_double | 0.137 | 0.0256 [0.00726, 0.046] | 15 |
| p_reach | 6 | 17 [12.8, 20.2] | 83 |
| p_same_line | 0.149 | 0.074 [0.0297, 0.137] | 25 |

### codebook: medyan mesafe 3.94 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | -10.5 | 1.469 | 0.821 |
| type_len_mean | -7.8 | 4.440 | 3.490 |
| vocab_ed1_density | +5.9 | 0.854 | 0.989 |
| jsd_first | +4.1 | 0.310 | 0.515 |
| wlen_mean | -3.9 | 3.859 | 3.265 |
| n_symbols | -3.6 | 69.529 | 35.500 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_slot_overlap | 0.502 | 0.0903 [0.0481, 0.169] | 10 |
| p_order | 1 | 2 [1, 2] | 84 |
| p_len_max | 2 | 1 [1, 2] | 25 |
| l_final_forms_k | 1 | 0 [0, 3] | 25 |


## zl_basic: sınıf sınıf

### grille: medyan mesafe 2.47 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | +2.8 | 0.823 | 0.883 |
| h2_over_h1 | +2.7 | 0.521 | 0.612 |
| h2 | +2.7 | 2.013 | 2.385 |
| wlen_autocorr1 | -2.5 | 0.123 | 0.007 |
| rep_adjacent_ed1 | -2.4 | 0.034 | 0.018 |
| jsd_line_final | -2.2 | 0.110 | 0.025 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.239 | 0 [0, 0.329] | 20 |
| l_initial_forms_k | 1 | 0 [0, 3] | 25 |

### slotcite: medyan mesafe 2.62 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2_over_h1 | +2.8 | 0.521 | 0.616 |
| h2 | +2.8 | 2.013 | 2.400 |
| vocab_ed1_density | +2.8 | 0.823 | 0.883 |
| rep_adjacent_exact | +2.6 | 0.008 | 0.015 |
| hapax_ratio | -2.2 | 0.715 | 0.643 |
| eff_symbols | +2.0 | 14.493 | 15.289 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 83 |
| l_line_final_p | 0.243 | 0 [0, 0.345] | 20 |
| p_exact | 0.396 | 0.233 [0.171, 0.389] | 22 |

### slotgram: medyan mesafe 2.97 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| jsd_last | -3.3 | 0.712 | 0.563 |
| zipf_slope | +3.1 | -0.785 | -0.575 |
| vocab_ed1_density | +2.5 | 0.823 | 0.878 |
| h2_over_h1 | +2.5 | 0.521 | 0.604 |
| top10_coverage | -2.2 | 0.175 | 0.092 |
| wlen_autocorr1 | -2.2 | 0.123 | 0.019 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.24 | 0 [0, 1.38] | 25 |
| l_allo_rate | 0.0119 | 0 [0, 0.0809] | 25 |
| l_final_forms_k | 1 | 0 [0, 2] | 25 |

### verbose: medyan mesafe 3.37 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -5.1 | 0.715 | 0.551 |
| wlen_skew | +5.0 | 0.025 | 0.536 |
| wlen_frac_le2 | +4.9 | 0.097 | 0.163 |
| jsd_last | -4.7 | 0.712 | 0.497 |
| wlen_std | +3.4 | 1.768 | 1.974 |
| wlen_autocorr1 | -3.4 | 0.123 | -0.036 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 87 |
| l_initial_forms_k | 1 | 0 [0, 2.5] | 25 |

### selfcite: medyan mesafe 3.94 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +6.1 | 2.013 | 2.867 |
| h2_over_h1 | +6.0 | 0.521 | 0.723 |
| rep_adjacent_exact | +5.7 | 0.008 | 0.023 |
| char_double_rate | +5.2 | 0.066 | 0.145 |
| vocab_ed1_density | +4.5 | 0.823 | 0.921 |
| eff_symbols | +4.4 | 14.493 | 16.250 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 6 | 19 [13, 25] | 87 |
| p_same_line | 0.149 | 0.0574 [0.0239, 0.12] | 19 |
| p_mut_prefix | 0.159 | 0.338 [0.149, 0.527] | 78 |
| l_allo_per_glyph | 0.211 | 0 [0, 0.853] | 25 |
| l_allo_rate | 0.0105 | 0 [0, 0.0503] | 25 |

### plain: medyan mesafe 4.66 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 19

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| eff_symbols | +9.3 | 14.493 | 18.221 |
| h2 | +7.4 | 2.013 | 3.044 |
| h2_over_h1 | +6.6 | 0.521 | 0.744 |
| wlen_std | -6.6 | 1.768 | 1.367 |
| h1 | +6.6 | 3.862 | 4.078 |
| type_len_mean | -5.9 | 5.640 | 4.569 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.249 | 0 [0, 0.294] | 20 |
| l_final_forms_share | 0.111 | 0.589 [0.141, 0.788] | 77 |
| l_allo_per_glyph | 0.212 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |

### codebook: medyan mesafe 4.77 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | -16.8 | 1.768 | 0.753 |
| type_len_mean | -7.4 | 5.640 | 4.305 |
| vocab_ed1_density | +7.3 | 0.823 | 0.981 |
| wlen_frac_le2 | -5.9 | 0.097 | 0.018 |
| jsd_first | +3.8 | 0.385 | 0.536 |
| wlen_mean | -3.8 | 4.961 | 4.096 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_slot_overlap | 0.502 | 0.072 [0.0356, 0.158] | 8 |
| p_order | 1 | 2 [1, 2] | 84 |
| l_final_forms_k | 1 | 0 [0, 3] | 25 |
| p_zero_empty | 1 | 0 [0, 1] | 25 |

### abjad: medyan mesafe 5.40 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac_le2 | +17.0 | 0.097 | 0.325 |
| wlen_frac1 | +8.4 | 0.033 | 0.119 |
| first_entropy_ratio | +7.7 | 0.817 | 0.948 |
| wlen_skew | +7.0 | 0.025 | 0.742 |
| h2_over_h1 | +6.8 | 0.521 | 0.750 |
| wlen_mean | -6.8 | 4.961 | 3.431 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_final_forms_share | 0.117 | 0.579 [0.349, 0.824] | 75 |


## zl_glyph: sınıf sınıf

### grille: medyan mesafe 2.15 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 3

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | +3.3 | 0.852 | 0.905 |
| wlen_autocorr1 | -2.4 | 0.102 | 0.007 |
| jsd_line_final | -2.3 | 0.110 | 0.024 |
| h2 | +1.9 | 2.127 | 2.460 |
| hapax_ratio | -1.8 | 0.715 | 0.657 |
| h2_over_h1 | +1.8 | 0.554 | 0.628 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.239 | 0 [0, 0.319] | 20 |
| l_initial_forms_k | 1 | 0 [0, 2] | 25 |

### slotcite: medyan mesafe 2.27 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h1 | +2.5 | 3.836 | 3.938 |
| vocab_ed1_density | +2.5 | 0.852 | 0.892 |
| rep_adjacent_exact | +2.4 | 0.008 | 0.015 |
| h2 | +2.2 | 2.127 | 2.513 |
| h2_over_h1 | +2.0 | 0.554 | 0.637 |
| eff_symbols | +1.8 | 14.529 | 15.665 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_exact | 0.396 | 0.241 [0.163, 0.385] | 24 |
| l_final_forms_k | 1 | 0 [0, 3] | 25 |

### slotgram: medyan mesafe 2.49 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | +2.7 | 0.852 | 0.895 |
| wlen_autocorr1 | -2.2 | 0.102 | 0.014 |
| zipf_slope | +2.1 | -0.785 | -0.639 |
| first_entropy_ratio | -2.1 | 0.875 | 0.823 |
| jsd_last | -2.0 | 0.712 | 0.621 |
| n_symbols | -1.7 | 44.750 | 28.000 |

### verbose: medyan mesafe 2.99 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_skew | +4.3 | 0.154 | 0.594 |
| wlen_std | +4.3 | 1.615 | 1.854 |
| hapax_ratio | -4.0 | 0.715 | 0.586 |
| jsd_last | -3.9 | 0.712 | 0.533 |
| wlen_frac1 | +3.5 | 0.033 | 0.071 |
| wlen_autocorr1 | -3.1 | 0.102 | -0.023 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 87 |

### selfcite: medyan mesafe 3.10 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +4.5 | 2.127 | 2.913 |
| h2_over_h1 | +4.4 | 0.554 | 0.734 |
| rep_adjacent_exact | +4.1 | 0.008 | 0.019 |
| vocab_ed1_density | +4.1 | 0.852 | 0.917 |
| h1 | +3.6 | 3.836 | 3.982 |
| eff_symbols | +3.1 | 14.529 | 16.499 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 6 | 19 [14, 24] | 87 |
| p_same_line | 0.149 | 0.0555 [0.0208, 0.104] | 19 |
| l_allo_per_glyph | 0.211 | 0 [0, 1.17] | 25 |
| l_allo_rate | 0.0105 | 0 [0, 0.0603] | 25 |

### abjad: medyan mesafe 3.61 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac1 | +8.0 | 0.033 | 0.119 |
| wlen_frac_le2 | +6.5 | 0.119 | 0.335 |
| wlen_skew | +5.8 | 0.154 | 0.741 |
| vocab_ed1_density | -4.7 | 0.852 | 0.777 |
| h2_over_h1 | +4.7 | 0.554 | 0.746 |
| first_entropy_ratio | +4.5 | 0.875 | 0.988 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_final_forms_share | 0.117 | 0.637 [0.426, 0.817] | 79 |

### plain: medyan mesafe 3.76 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | -7.5 | 0.852 | 0.732 |
| eff_symbols | +6.4 | 14.529 | 18.644 |
| h1 | +6.3 | 3.836 | 4.091 |
| h2 | +5.7 | 2.127 | 3.114 |
| wlen_std | -5.2 | 1.615 | 1.327 |
| h2_over_h1 | +5.1 | 0.554 | 0.762 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.249 | 0 [0, 0.333] | 20 |
| l_final_forms_share | 0.111 | 0.563 [0.218, 0.791] | 75 |
| l_allo_per_glyph | 0.212 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |

### codebook: medyan mesafe 4.04 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | -12.8 | 1.615 | 0.907 |
| vocab_ed1_density | +8.3 | 0.852 | 0.984 |
| type_len_mean | -5.4 | 4.989 | 3.702 |
| wlen_skew | -3.5 | 0.154 | -0.205 |
| wlen_mean | -3.4 | 4.436 | 3.409 |
| rep_adjacent_exact | -3.2 | 0.008 | 0.001 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_slot_overlap | 0.502 | 0.0823 [0.0405, 0.152] | 9 |
| l_final_forms_k | 1 | 0 [0, 3] | 25 |
