# ABC raporu: her hipotez Voynich'e ne kadar yaklaşabiliyor

Sentetik örnek: 78000. Her sınıfta Voynich'e en yakın %1 kabul edildi.

Mesafe birimi Voynich'in kendi pencereleri arasındaki değişkenliktir. "Voynich öz mesafesi" bir Voynich penceresinin diğerlerinin ortalamasına uzaklığıdır; bir hipotezin mesafesi bu aralığa girmiyorsa o hipotez Voynich'i (bu feature kümesinde) üretemiyor demektir.

## 1. Kabul edilen örneklerin medyan mesafesi

| görünüm | Voynich öz mesafesi (medyan, en çok) | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.91, 1.65 | 6.10 | 3.49 | 4.71 | 2.86 | 5.31 | 4.44 | 3.09 | 3.36 | 4.02 |
| eva_glyph | 0.96, 1.64 | 4.01 | 3.48 | 4.28 | 2.56 | 4.08 | 3.52 | 2.85 | 2.93 | 3.55 |
| v101 | 0.96, 1.40 | 3.25 | 2.96 | 3.91 | 2.62 | 3.03 | 3.81 | 2.96 | 2.84 | 3.37 |
| zl_basic | 0.95, 1.51 | 5.34 | 3.38 | 4.73 | 2.49 | 4.60 | 3.92 | 2.64 | 2.97 | 3.33 |
| zl_glyph | 1.03, 1.43 | 3.58 | 3.07 | 4.03 | 2.18 | 3.72 | 3.11 | 2.33 | 2.53 | 2.96 |

## 2. En iyi tek örneğin mesafesi

| görünüm | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 5.24 | 2.76 | 3.95 | 2.28 | 3.78 | 3.56 | 2.52 | 2.33 | 2.50 |
| eva_glyph | 3.28 | 2.59 | 3.24 | 2.04 | 2.91 | 2.93 | 1.96 | 2.19 | 2.39 |
| v101 | 2.45 | 2.10 | 3.24 | 1.84 | 2.12 | 2.79 | 2.10 | 2.13 | 2.46 |
| zl_basic | 4.37 | 2.70 | 3.77 | 1.85 | 3.27 | 3.06 | 2.14 | 2.19 | 2.14 |
| zl_glyph | 2.91 | 2.42 | 2.87 | 1.81 | 2.81 | 2.50 | 1.73 | 1.86 | 2.23 |

## 3. Voynich'in en uç penceresi kadar yakın olan örneklerin oranı

| görünüm | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|
| eva_basic | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| eva_glyph | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| v101 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| zl_basic | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |
| zl_glyph | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 | %0.00 |

## eva_basic: sınıf sınıf

### grille: medyan mesafe 2.86 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +3.4 | 2.016 | 2.431 |
| h2_over_h1 | +3.4 | 0.524 | 0.630 |
| wlen_autocorr1 | -3.2 | 0.127 | 0.006 |
| jsd_line_final | -2.9 | 0.109 | 0.016 |
| rep_adjacent_ed1 | -2.8 | 0.032 | 0.013 |
| hapax_ratio | -2.8 | 0.717 | 0.655 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 83 |
| l_line_final_p | 0.239 | 0 [0, 0.413] | 20 |

### slotcite: medyan mesafe 3.09 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -5.8 | 0.717 | 0.588 |
| rep_adjacent_exact | +3.4 | 0.009 | 0.019 |
| h2 | +3.4 | 2.016 | 2.421 |
| h2_over_h1 | +3.3 | 0.524 | 0.627 |
| zipf_slope | +3.1 | -0.778 | -0.584 |
| vocab_ed1_density | +2.9 | 0.823 | 0.894 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 83 |
| p_exact | 0.396 | 0.217 [0.174, 0.328] | 20 |
| l_allo_per_glyph | 0.224 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0111 | 0 [0, 0] | 25 |

### slotgram: medyan mesafe 3.36 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| zipf_slope | +3.8 | -0.778 | -0.541 |
| jsd_last | -3.4 | 0.719 | 0.558 |
| edge_mi | -2.9 | 0.179 | -0.007 |
| wlen_autocorr1 | -2.8 | 0.127 | 0.021 |
| h2_over_h1 | +2.7 | 0.524 | 0.608 |
| word_entropy_norm | +2.6 | 0.804 | 0.887 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.24 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0119 | 0 [0, 0] | 25 |

### automaton: medyan mesafe 3.49 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| jsd_first | +8.1 | 0.385 | 0.660 |
| wlen_skew | +5.8 | 0.074 | 0.825 |
| first_entropy_ratio | -5.2 | 0.806 | 0.714 |
| char_double_rate | -4.8 | 0.067 | 0.000 |
| wlen_autocorr1 | -3.4 | 0.127 | -0.002 |
| edge_mi | -2.6 | 0.179 | 0.008 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_alphabet | 20 | 17 [16, 18] | 22 |
| l_final_forms_share | 0.109 | 0 [0, 0.35] | 25 |
| l_initial_forms_k | 1 | 0 [0, 2] | 25 |

### verbose: medyan mesafe 4.02 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 19

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -8.4 | 0.717 | 0.532 |
| wlen_frac_le2 | +6.7 | 0.077 | 0.154 |
| jsd_last | -5.6 | 0.719 | 0.455 |
| wlen_autocorr1 | -4.3 | 0.127 | -0.036 |
| ttr | -3.8 | 0.443 | 0.233 |
| wlen_skew | +3.8 | 0.074 | 0.560 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 87 |
| l_initial_forms_k | 1 | 0 [0, 3] | 25 |

### selfcite: medyan mesafe 4.44 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +7.3 | 2.016 | 2.898 |
| h2_over_h1 | +6.8 | 0.524 | 0.735 |
| char_double_rate | +5.8 | 0.067 | 0.147 |
| rep_adjacent_exact | +5.7 | 0.009 | 0.026 |
| hapax_ratio | -5.3 | 0.717 | 0.598 |
| type_len_mean | -5.1 | 5.692 | 4.827 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 6 | 18 [13, 23] | 85 |
| p_affix | 0.602 | 0.77 [0.601, 0.845] | 78 |
| p_alphabet | 20 | 17 [16, 19] | 22 |
| p_same_line | 0.149 | 0.0735 [0.0273, 0.128] | 25 |
| l_allo_per_glyph | 0.211 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0105 | 0 [0, 0] | 25 |

### codebook: medyan mesafe 4.71 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | -13.5 | 1.693 | 0.705 |
| type_len_mean | -8.6 | 5.692 | 4.228 |
| vocab_ed1_density | +6.7 | 0.823 | 0.990 |
| wlen_frac_le2 | -5.6 | 0.077 | 0.012 |
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

### plain: medyan mesafe 5.31 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| eff_symbols | +11.1 | 14.240 | 17.797 |
| h1 | +9.0 | 3.845 | 4.056 |
| h2 | +8.2 | 2.016 | 3.010 |
| h2_over_h1 | +7.0 | 0.524 | 0.742 |
| n_symbols | +6.2 | 19.562 | 27.000 |
| type_len_mean | -5.7 | 5.692 | 4.714 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.249 | 0 [0, 0.336] | 20 |
| l_allo_per_glyph | 0.212 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |

### abjad: medyan mesafe 6.10 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac_le2 | +21.3 | 0.077 | 0.323 |
| first_entropy_ratio | +9.2 | 0.806 | 0.970 |
| wlen_frac1 | +8.7 | 0.017 | 0.114 |
| h2_over_h1 | +7.5 | 0.524 | 0.756 |
| type_len_mean | -7.4 | 5.692 | 4.422 |
| wlen_mean | -7.0 | 5.066 | 3.436 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.231 | 0 [0, 0.419] | 20 |


## eva_glyph: sınıf sınıf

### grille: medyan mesafe 2.56 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_autocorr1 | -3.0 | 0.103 | 0.002 |
| edge_mi | -3.0 | 0.187 | -0.005 |
| hapax_ratio | -2.7 | 0.717 | 0.656 |
| vocab_ed1_density | +2.6 | 0.850 | 0.908 |
| h2_over_h1 | +2.2 | 0.556 | 0.640 |
| jsd_line_final | -2.2 | 0.110 | 0.041 |

### slotcite: medyan mesafe 2.85 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -4.5 | 0.717 | 0.617 |
| rep_adjacent_exact | +3.2 | 0.009 | 0.019 |
| edge_mi | -3.0 | 0.187 | -0.010 |
| zipf_slope | +2.9 | -0.778 | -0.594 |
| h2 | +2.4 | 2.131 | 2.507 |
| first_entropy_ratio | -2.4 | 0.867 | 0.814 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_exact | 0.396 | 0.245 [0.167, 0.35] | 24 |
| p_same_line | 0.248 | 0.121 [0.0549, 0.235] | 25 |
| l_allo_per_glyph | 0.224 | 0 [0, 0.557] | 25 |
| l_allo_rate | 0.0111 | 0 [0, 0.083] | 25 |

### slotgram: medyan mesafe 2.93 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| edge_mi | -3.0 | 0.187 | -0.004 |
| zipf_slope | +2.9 | -0.778 | -0.594 |
| wlen_autocorr1 | -2.7 | 0.103 | 0.012 |
| first_entropy_ratio | -2.3 | 0.867 | 0.817 |
| vocab_ed1_density | +2.2 | 0.850 | 0.900 |
| wlen_frac1 | +2.1 | 0.017 | 0.042 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.24 | 0 [0, 0.734] | 25 |
| l_allo_rate | 0.0119 | 0 [0, 0.0796] | 25 |

### automaton: medyan mesafe 3.48 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| jsd_first | +7.7 | 0.350 | 0.667 |
| wlen_skew | +5.6 | 0.183 | 0.778 |
| first_entropy_ratio | -5.3 | 0.867 | 0.750 |
| char_double_rate | -5.2 | 0.076 | 0.001 |
| n_symbols | -4.4 | 25.250 | 20.000 |
| wlen_autocorr1 | -3.1 | 0.103 | -0.000 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_alphabet | 20 | 17 [16, 18] | 22 |
| l_final_forms_share | 0.109 | 0 [0, 0.272] | 25 |
| l_initial_forms_k | 1 | 0 [0, 0] | 25 |

### selfcite: medyan mesafe 3.52 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

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

### verbose: medyan mesafe 3.55 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| hapax_ratio | -7.0 | 0.717 | 0.561 |
| wlen_std | +6.2 | 1.552 | 1.874 |
| wlen_autocorr1 | -4.0 | 0.103 | -0.031 |
| wlen_skew | +4.0 | 0.183 | 0.608 |
| jsd_last | -3.9 | 0.718 | 0.532 |
| ttr | -3.7 | 0.443 | 0.242 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 87 |
| p_alphabet | 17 | 14 [13, 18] | 23 |
| l_initial_forms_k | 1 | 0 [0, 3] | 25 |

### abjad: medyan mesafe 4.01 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

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

### plain: medyan mesafe 4.08 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

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

### codebook: medyan mesafe 4.28 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

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

### grille: medyan mesafe 2.62 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +4.0 | 0.015 | 0.036 |
| wlen_autocorr1 | -2.9 | 0.179 | 0.004 |
| edge_mi | -2.9 | 0.228 | -0.001 |
| n_symbols | -2.8 | 69.529 | 43.500 |
| vocab_ed1_density | +2.7 | 0.854 | 0.916 |
| hapax_ratio | -2.4 | 0.741 | 0.670 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_initial_forms_k | 1 | 0 [0, 1.75] | 25 |

### slotgram: medyan mesafe 2.84 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| n_symbols | -3.7 | 69.529 | 34.500 |
| char_double_rate | +3.1 | 0.015 | 0.032 |
| edge_mi | -3.0 | 0.228 | -0.008 |
| wlen_autocorr1 | -2.8 | 0.179 | 0.014 |
| wlen_frac1 | +2.1 | 0.046 | 0.068 |
| zipf_slope | +2.0 | -0.776 | -0.688 |

### automaton: medyan mesafe 2.96 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| jsd_first | +7.3 | 0.310 | 0.679 |
| wlen_frac1 | -4.5 | 0.046 | 0.000 |
| wlen_skew | +4.2 | 0.225 | 0.797 |
| n_symbols | -3.8 | 69.529 | 34.000 |
| first_entropy_ratio | -3.2 | 0.886 | 0.784 |
| wlen_autocorr1 | -3.0 | 0.179 | 0.002 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_out_degree | 5 | 7 [5.75, 8] | 79 |
| l_final_forms_share | 0.109 | 0 [0, 0.317] | 25 |
| l_initial_forms_k | 1 | 0 [0, 1] | 25 |

### slotcite: medyan mesafe 2.96 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +5.3 | 0.015 | 0.044 |
| rep_adjacent_exact | +3.4 | 0.006 | 0.014 |
| edge_mi | -3.0 | 0.228 | -0.011 |
| vocab_ed1_density | +2.8 | 0.854 | 0.918 |
| n_symbols | -2.7 | 69.529 | 44.000 |
| wlen_frac1 | -2.6 | 0.046 | 0.019 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_rate | 0.0111 | 0.0888 [0.0417, 0.115] | 79 |
| l_allo_per_glyph | 0.224 | 1.62 [0.748, 2.24] | 76 |

### plain: medyan mesafe 3.03 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | -5.3 | 0.854 | 0.731 |
| h2 | +5.2 | 2.383 | 3.268 |
| rep_adjacent_ed1 | -4.6 | 0.043 | 0.010 |
| h2_over_h1 | +4.6 | 0.595 | 0.788 |
| wlen_frac1 | -4.5 | 0.046 | 0.000 |
| n_symbols | -4.4 | 69.529 | 28.000 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.249 | 0 [0, 0.301] | 20 |
| l_allo_per_glyph | 0.212 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |

### abjad: medyan mesafe 3.25 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac1 | +5.9 | 0.046 | 0.107 |
| wlen_frac_le2 | +5.4 | 0.184 | 0.328 |
| h2 | +4.1 | 2.383 | 3.087 |
| h2_over_h1 | +4.0 | 0.595 | 0.762 |
| n_symbols | -3.8 | 69.529 | 34.000 |
| vocab_ed1_density | -3.5 | 0.854 | 0.772 |

### verbose: medyan mesafe 3.37 (88 / 8800 örnek kabul)

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

### selfcite: medyan mesafe 3.81 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| char_double_rate | +8.9 | 0.015 | 0.063 |
| rep_adjacent_exact | +6.4 | 0.006 | 0.020 |
| rep_within3 | +4.2 | 0.021 | 0.043 |
| h2 | +4.1 | 2.383 | 3.080 |
| h2_over_h1 | +3.6 | 0.595 | 0.744 |
| zipf_slope | +3.5 | -0.776 | -0.623 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_mut_double | 0.137 | 0.0235 [0.00726, 0.0451] | 14 |
| p_reach | 6 | 16.5 [12.8, 20] | 82 |
| p_same_line | 0.149 | 0.074 [0.0297, 0.137] | 25 |

### codebook: medyan mesafe 3.91 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | -10.4 | 1.469 | 0.827 |
| type_len_mean | -7.9 | 4.440 | 3.477 |
| vocab_ed1_density | +5.9 | 0.854 | 0.989 |
| jsd_first | +4.1 | 0.310 | 0.515 |
| wlen_mean | -4.0 | 3.859 | 3.258 |
| n_symbols | -3.6 | 69.529 | 35.500 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_slot_overlap | 0.502 | 0.0903 [0.0481, 0.169] | 10 |
| p_order | 1 | 2 [1, 2] | 84 |
| p_len_max | 2 | 1 [1, 2] | 25 |
| l_final_forms_k | 1 | 0 [0, 3] | 25 |


## zl_basic: sınıf sınıf

### grille: medyan mesafe 2.49 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| edge_mi | -3.2 | 0.192 | -0.004 |
| vocab_ed1_density | +2.8 | 0.823 | 0.883 |
| h2_over_h1 | +2.7 | 0.521 | 0.612 |
| h2 | +2.7 | 2.013 | 2.385 |
| wlen_autocorr1 | -2.5 | 0.123 | 0.006 |
| rep_adjacent_ed1 | -2.4 | 0.034 | 0.017 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.239 | 0 [0, 0.323] | 20 |
| l_initial_forms_k | 1 | 0 [0, 3] | 25 |

### slotcite: medyan mesafe 2.64 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| edge_mi | -3.3 | 0.192 | -0.009 |
| h2_over_h1 | +2.8 | 0.521 | 0.616 |
| h2 | +2.8 | 2.013 | 2.400 |
| vocab_ed1_density | +2.7 | 0.823 | 0.882 |
| rep_adjacent_exact | +2.6 | 0.008 | 0.015 |
| hapax_ratio | -2.2 | 0.715 | 0.643 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_len_edge | 2 | 3 [2, 3] | 83 |
| l_line_final_p | 0.243 | 0 [0, 0.345] | 20 |
| p_exact | 0.396 | 0.228 [0.168, 0.378] | 21 |

### slotgram: medyan mesafe 2.97 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| edge_mi | -3.3 | 0.192 | -0.008 |
| jsd_last | -3.3 | 0.712 | 0.563 |
| zipf_slope | +3.1 | -0.785 | -0.575 |
| vocab_ed1_density | +2.5 | 0.823 | 0.878 |
| h2_over_h1 | +2.5 | 0.521 | 0.604 |
| top10_coverage | -2.2 | 0.175 | 0.092 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_allo_per_glyph | 0.24 | 0 [0, 1.38] | 25 |
| l_allo_rate | 0.0119 | 0 [0, 0.0809] | 25 |
| l_final_forms_k | 1 | 0 [0, 2] | 25 |

### verbose: medyan mesafe 3.33 (88 / 8800 örnek kabul)

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

### automaton: medyan mesafe 3.38 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_skew | +7.2 | 0.025 | 0.763 |
| jsd_first | +6.6 | 0.385 | 0.645 |
| char_double_rate | -4.4 | 0.066 | 0.000 |
| first_entropy_ratio | -3.6 | 0.817 | 0.755 |
| wlen_frac1 | -3.2 | 0.033 | 0.000 |
| edge_mi | -2.9 | 0.192 | 0.016 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_alphabet | 20 | 17 [16, 19] | 22 |
| l_final_forms_share | 0.109 | 0 [0, 0.394] | 25 |
| l_initial_forms_k | 1 | 0 [0, 0] | 25 |

### selfcite: medyan mesafe 3.92 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 19

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +6.1 | 2.013 | 2.867 |
| h2_over_h1 | +5.9 | 0.521 | 0.720 |
| rep_adjacent_exact | +5.5 | 0.008 | 0.022 |
| char_double_rate | +5.4 | 0.066 | 0.147 |
| vocab_ed1_density | +4.5 | 0.823 | 0.921 |
| eff_symbols | +4.5 | 14.493 | 16.286 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 6 | 19 [12.8, 24.2] | 87 |
| p_same_line | 0.149 | 0.0561 [0.0239, 0.12] | 19 |
| p_mut_prefix | 0.159 | 0.345 [0.151, 0.552] | 79 |
| l_allo_per_glyph | 0.211 | 0 [0, 0.974] | 25 |
| l_allo_rate | 0.0105 | 0 [0, 0.0512] | 25 |

### plain: medyan mesafe 4.60 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| eff_symbols | +9.6 | 14.493 | 18.321 |
| h2 | +7.5 | 2.013 | 3.049 |
| h1 | +6.7 | 3.862 | 4.082 |
| h2_over_h1 | +6.6 | 0.521 | 0.744 |
| wlen_std | -6.6 | 1.768 | 1.371 |
| type_len_mean | -5.9 | 5.640 | 4.569 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.249 | 0 [0, 0.267] | 20 |
| l_final_forms_share | 0.111 | 0.563 [0.131, 0.779] | 75 |
| l_allo_per_glyph | 0.212 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |

### codebook: medyan mesafe 4.73 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

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

### abjad: medyan mesafe 5.34 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

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

### grille: medyan mesafe 2.18 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| edge_mi | -3.5 | 0.199 | -0.004 |
| vocab_ed1_density | +3.3 | 0.852 | 0.905 |
| wlen_autocorr1 | -2.4 | 0.102 | 0.008 |
| jsd_line_final | -2.3 | 0.110 | 0.025 |
| h2 | +1.9 | 2.127 | 2.458 |
| hapax_ratio | -1.8 | 0.715 | 0.657 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.239 | 0 [0, 0.328] | 20 |

### slotcite: medyan mesafe 2.33 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| edge_mi | -3.6 | 0.199 | -0.010 |
| vocab_ed1_density | +2.5 | 0.852 | 0.892 |
| rep_adjacent_exact | +2.4 | 0.008 | 0.015 |
| h1 | +2.4 | 3.836 | 3.934 |
| h2 | +2.3 | 2.127 | 2.522 |
| h2_over_h1 | +2.1 | 0.554 | 0.640 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_exact | 0.396 | 0.241 [0.163, 0.373] | 24 |
| l_final_forms_k | 1 | 0 [0, 2.25] | 25 |

### slotgram: medyan mesafe 2.53 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| edge_mi | -3.6 | 0.199 | -0.010 |
| vocab_ed1_density | +2.7 | 0.852 | 0.895 |
| wlen_autocorr1 | -2.2 | 0.102 | 0.014 |
| zipf_slope | +2.1 | -0.785 | -0.643 |
| first_entropy_ratio | -2.1 | 0.875 | 0.823 |
| jsd_last | -1.9 | 0.712 | 0.626 |

### verbose: medyan mesafe 2.96 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | +4.4 | 1.615 | 1.860 |
| wlen_skew | +4.3 | 0.154 | 0.593 |
| jsd_last | -4.0 | 0.712 | 0.527 |
| hapax_ratio | -4.0 | 0.715 | 0.586 |
| wlen_frac1 | +3.5 | 0.033 | 0.071 |
| wlen_autocorr1 | -3.2 | 0.102 | -0.024 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_by_syllable | 0 | 1 [1, 1] | 87 |

### automaton: medyan mesafe 3.07 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| jsd_first | +6.6 | 0.351 | 0.658 |
| wlen_skew | +5.8 | 0.154 | 0.746 |
| char_double_rate | -4.7 | 0.076 | 0.000 |
| first_entropy_ratio | -4.6 | 0.875 | 0.759 |
| wlen_frac1 | -3.1 | 0.033 | 0.000 |
| edge_mi | -2.7 | 0.199 | 0.043 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_alphabet | 20 | 17 [16, 19] | 22 |
| l_final_forms_share | 0.109 | 0 [0, 0.232] | 25 |
| l_initial_forms_k | 1 | 0 [0, 0.5] | 25 |

### selfcite: medyan mesafe 3.11 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| h2 | +4.5 | 2.127 | 2.913 |
| h2_over_h1 | +4.4 | 0.554 | 0.734 |
| rep_adjacent_exact | +4.1 | 0.008 | 0.019 |
| vocab_ed1_density | +4.1 | 0.852 | 0.917 |
| h1 | +3.6 | 3.836 | 3.982 |
| edge_mi | -3.5 | 0.199 | -0.004 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_reach | 6 | 19 [14, 24] | 87 |
| p_same_line | 0.149 | 0.0555 [0.0208, 0.104] | 19 |
| l_allo_per_glyph | 0.211 | 0 [0, 1.17] | 25 |
| l_allo_rate | 0.0105 | 0 [0, 0.0603] | 25 |

### abjad: medyan mesafe 3.58 (76 / 7600 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_frac1 | +8.0 | 0.033 | 0.119 |
| wlen_frac_le2 | +6.5 | 0.119 | 0.336 |
| wlen_skew | +5.8 | 0.154 | 0.742 |
| vocab_ed1_density | -4.7 | 0.852 | 0.777 |
| h2_over_h1 | +4.6 | 0.554 | 0.744 |
| first_entropy_ratio | +4.5 | 0.875 | 0.988 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_final_forms_share | 0.117 | 0.637 [0.426, 0.808] | 79 |

### plain: medyan mesafe 3.72 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| vocab_ed1_density | -7.3 | 0.852 | 0.735 |
| eff_symbols | +6.4 | 14.529 | 18.594 |
| h1 | +6.2 | 3.836 | 4.089 |
| h2 | +5.7 | 2.127 | 3.114 |
| wlen_std | -5.2 | 1.615 | 1.327 |
| h2_over_h1 | +5.1 | 0.554 | 0.762 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| l_line_final_p | 0.249 | 0 [0, 0.348] | 20 |
| l_final_forms_share | 0.111 | 0.563 [0.218, 0.791] | 75 |
| l_allo_per_glyph | 0.212 | 0 [0, 0] | 25 |
| l_allo_rate | 0.0104 | 0 [0, 0] | 25 |

### codebook: medyan mesafe 4.03 (88 / 8800 örnek kabul)

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | kabul edilenler |
|---|---|---|---|
| wlen_std | -12.8 | 1.615 | 0.907 |
| vocab_ed1_density | +8.4 | 0.852 | 0.986 |
| type_len_mean | -5.5 | 4.989 | 3.684 |
| wlen_skew | -3.5 | 0.154 | -0.205 |
| wlen_mean | -3.4 | 4.436 | 3.403 |
| edge_mi | -3.3 | 0.199 | 0.007 |

| kayan ayar | önsel medyan | kabul edilen medyan [çeyrekler] | önseldeki yüzdelik |
|---|---|---|---|
| p_slot_overlap | 0.502 | 0.0823 [0.0405, 0.152] | 9 |
| l_final_forms_k | 1 | 0 [0, 3] | 25 |
