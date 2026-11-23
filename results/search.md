# Yönlendirilmiş arama raporu: her hipotezin ulaşabildiği en iyi nokta

Her (sınıf, görünüm) için 5 tur, tur başına 600 deneme, en yakın 100 ayar tutuldu. Tablolardaki mesafeler, son turda kalan ayarların her biriyle yeniden üretilen 2 taze örnekten hesaplandı (toplam 200).

Mesafe birimi ve ölçüt `abc.md` ile aynı: bir hipotezin taze örnekleri Voynich öz mesafesinin içine giriyorsa, o hipotez bu feature kümesinde Voynich'ten ayırt edilemez.

## 1. Taze örneklerin medyan mesafesi (parantezde rejection ABC'deki değer)

| görünüm | Voynich öz mesafesi (medyan, en çok) | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|---|
| eva_basic | 0.91, 1.64 | 5.80 (6.19) | 3.29 (2.76) | 4.14 (5.32) | 3.62 (4.43) | 4.18 (3.98) |
| eva_glyph | 0.96, 1.63 | 3.59 (3.96) | 2.81 (2.48) | 3.05 (4.20) | 2.87 (3.56) | 3.65 (3.56) |
| v101 | 0.97, 1.42 | 2.94 (3.36) | 3.54 (2.53) | 2.62 (3.02) | 3.39 (3.90) | 3.41 (3.27) |
| zl_basic | 0.96, 1.52 | 4.97 (5.36) | 3.13 (2.44) | 3.68 (4.71) | 3.47 (3.96) | 3.47 (3.26) |
| zl_glyph | 1.03, 1.43 | 3.26 (3.54) | 2.46 (2.15) | 2.90 (3.76) | 2.55 (3.12) | 2.84 (2.89) |

## 2. Voynich'in en uç penceresi kadar yakın olan taze örneklerin oranı

| görünüm | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|
| eva_basic | %0 | %0 | %0 | %0 | %0 |
| eva_glyph | %0 | %0 | %0 | %0 | %0 |
| v101 | %0 | %0 | %0 | %0 | %0 |
| zl_basic | %0 | %0 | %0 | %0 | %0 |
| zl_glyph | %0 | %0 | %0 | %0 | %0 |

## 3. Arama yakınsadı mı (tur tur, tutulan ayarların medyan mesafesi)

| görünüm | sınıf | turlar |
|---|---|---|
| eva_basic | abjad | 5.98 -> 5.73 -> 5.63 -> 5.42 -> 5.29 |
| eva_basic | grille | 2.92 -> 2.81 -> 2.70 -> 2.64 -> 2.57 |
| eva_basic | plain | 4.86 -> 4.11 -> 3.97 -> 3.96 -> 3.88 |
| eva_basic | selfcite | 4.12 -> 3.78 -> 3.53 -> 3.34 -> 3.28 |
| eva_basic | verbose | 3.88 -> 3.76 -> 3.66 -> 3.65 -> 3.53 |
| eva_glyph | abjad | 3.66 -> 3.52 -> 3.38 -> 3.36 -> 3.27 |
| eva_glyph | grille | 2.61 -> 2.40 -> 2.45 -> 2.31 -> 2.34 |
| eva_glyph | plain | 3.62 -> 3.10 -> 2.91 -> 2.83 -> 2.79 |
| eva_glyph | selfcite | 3.35 -> 3.09 -> 2.91 -> 2.79 -> 2.65 |
| eva_glyph | verbose | 3.45 -> 3.30 -> 3.22 -> 3.13 -> 3.17 |
| v101 | abjad | 3.02 -> 2.81 -> 2.71 -> 2.66 -> 2.64 |
| v101 | grille | 2.99 -> 2.80 -> 2.86 -> 2.78 -> 2.80 |
| v101 | plain | 2.66 -> 2.46 -> 2.40 -> 2.38 -> 2.37 |
| v101 | selfcite | 3.53 -> 3.34 -> 3.15 -> 3.07 -> 2.85 |
| v101 | verbose | 3.22 -> 3.03 -> 2.95 -> 2.89 -> 2.83 |
| zl_basic | abjad | 5.28 -> 5.11 -> 4.97 -> 4.66 -> 4.58 |
| zl_basic | grille | 2.61 -> 2.60 -> 2.57 -> 2.53 -> 2.43 |
| zl_basic | plain | 4.10 -> 3.66 -> 3.55 -> 3.49 -> 3.44 |
| zl_basic | selfcite | 3.71 -> 3.36 -> 3.25 -> 3.13 -> 3.02 |
| zl_basic | verbose | 3.09 -> 3.10 -> 3.07 -> 3.05 -> 2.97 |
| zl_glyph | abjad | 3.36 -> 3.20 -> 3.05 -> 3.06 -> 2.97 |
| zl_glyph | grille | 2.30 -> 2.24 -> 2.17 -> 2.10 -> 2.03 |
| zl_glyph | plain | 3.24 -> 2.86 -> 2.75 -> 2.71 -> 2.69 |
| zl_glyph | selfcite | 2.89 -> 2.71 -> 2.56 -> 2.41 -> 2.31 |
| zl_glyph | verbose | 2.80 -> 2.67 -> 2.55 -> 2.50 -> 2.45 |

## eva_basic: sınıf sınıf

### grille: taze medyan mesafe 3.29, en iyi 1.80

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -3.4 | 0.127 | -0.005 |
| vocab_ed1_density | +3.3 | 0.823 | 0.905 |
| hapax_ratio | -3.1 | 0.717 | 0.648 |
| h2_over_h1 | +2.7 | 0.524 | 0.610 |
| jsd_line_final | -2.7 | 0.109 | 0.022 |
| h2 | +2.4 | 2.016 | 2.302 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.02 [6.69, 11] | 5 .. 13 |
| l_width_jitter | 0.172 [0.0735, 0.288] | 0 .. 0.35 |
| l_para_lines | 8.36 [0, 11.4] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.521 [0.376, 0.7] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.321 [0, 0.48] | 0.1 .. 0.9 |
| l_line_final_p | 0.112 [0, 0.298] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.586] | 0.3 .. 1 |
| p_alphabet | 19 [17, 21] | 15 .. 25 |
| p_rows | 1.08e+03 [676, 1.66e+03] | 60 .. 3000 |
| p_slot_overlap | 0.253 [0.0665, 0.735] | 0 .. 1 |
| p_n_edge | 22 [14, 31] | 5 .. 40 |
| p_n_mid | 40 [27.8, 56.2] | 10 .. 120 |
| p_empty | 0.248 [0.2, 0.311] | 0 .. 0.6 |
| p_len_edge | 3 [2.75, 3] | 1 .. 3 |
| p_len_mid | 3 [3, 4] | 2 .. 5 |
| p_n_grilles | 7 [5, 8] | 3 .. 8 |

### selfcite: taze medyan mesafe 3.62, en iyi 2.65

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -6.6 | 0.717 | 0.571 |
| h2 | +5.8 | 2.016 | 2.714 |
| h2_over_h1 | +5.7 | 0.524 | 0.700 |
| type_len_mean | -4.6 | 5.692 | 4.899 |
| vocab_ed1_density | +4.6 | 0.823 | 0.939 |
| first_entropy_ratio | +4.4 | 0.806 | 0.886 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 11 [9.36, 12.1] | 5 .. 13 |
| l_width_jitter | 0.199 [0.132, 0.262] | 0 .. 0.35 |
| l_para_lines | 6.47 [0, 9.68] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.746 [0.543, 0.915] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.141 [0, 0.412] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.23] | 0.1 .. 0.9 |
| l_para_initial_p | 0.407 [0, 0.675] | 0.3 .. 1 |
| p_alphabet | 16.5 [15, 18] | 15 .. 25 |
| p_glyph_classes | 6 [5, 7] | 4 .. 7 |
| p_copy | 0.876 [0.851, 0.906] | 0.85 .. 0.97 |
| p_exact | 0.395 [0.3, 0.467] | 0.2 .. 0.8 |
| p_reach | 21 [14.8, 27] | 1 .. 30 |
| p_same_line | 0.03 [0.0176, 0.0636] | 0 .. 0.3 |
| p_slot_overlap | 0.409 [0.134, 0.687] | 0 .. 1 |
| p_affix | 0.854 [0.773, 0.9] | 0.3 .. 0.9 |
| p_mut_substitute | 0.284 [0.17, 0.488] | 0 .. 1 |
| p_mut_prefix | 0.454 [0.32, 0.639] | 0 .. 1 |
| p_mut_delete | 0.0447 [0.00941, 0.083] | 0 .. 1 |
| p_mut_double | 0.0765 [0.0426, 0.175] | 0 .. 1 |

### plain: taze medyan mesafe 4.14, en iyi 3.42

Voynich'ten 2 birimden fazla sapan feature sayısı: 21

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -7.8 | 0.628 | 0.152 |
| first_entropy_ratio | +7.0 | 0.806 | 0.931 |
| h2 | +6.6 | 2.016 | 2.816 |
| h2_over_h1 | +6.3 | 0.524 | 0.719 |
| wlen_frac_le2 | +6.1 | 0.077 | 0.147 |
| type_len_mean | -6.0 | 5.692 | 4.672 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 11.4 [8.44, 12.8] | 5 .. 13 |
| l_width_jitter | 0.185 [0.119, 0.252] | 0 .. 0.35 |
| l_para_lines | 3.2 [0, 8.75] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.907 [0.848, 0.968] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.256] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 64, Arabic 36

### verbose: taze medyan mesafe 4.18, en iyi 2.80

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +8.9 | 0.077 | 0.180 |
| hapax_ratio | -8.9 | 0.717 | 0.520 |
| wlen_frac1 | +4.7 | 0.017 | 0.070 |
| first_entropy_ratio | +4.6 | 0.806 | 0.889 |
| wlen_autocorr1 | -4.2 | 0.127 | -0.033 |
| jsd_first | -3.9 | 0.385 | 0.252 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.69 [5.39, 8.3] | 5 .. 13 |
| l_width_jitter | 0.137 [0.0745, 0.24] | 0 .. 0.35 |
| l_para_lines | 5.03 [0, 7.12] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.527] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0385] | 0.01 .. 0.15 |
| l_final_forms_share | 0.544 [0, 0.801] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.1] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.484 [0.222, 0.753] | 0.1 .. 0.9 |
| l_line_final_p | 0.261 [0, 0.446] | 0.1 .. 0.9 |
| l_para_initial_p | 0.579 [0, 0.724] | 0.3 .. 1 |
| p_alphabet | 15 [12.8, 17] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 24, Czech 21, Croatian 20, Polish 12, Russian 8

### abjad: taze medyan mesafe 5.80, en iyi 4.30

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +22.1 | 0.077 | 0.333 |
| wlen_frac1 | +8.5 | 0.017 | 0.113 |
| wlen_mean | -7.2 | 5.066 | 3.388 |
| type_len_mean | -7.1 | 5.692 | 4.477 |
| h2 | +5.6 | 2.016 | 2.691 |
| h2_over_h1 | +5.5 | 0.524 | 0.696 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.11 [5.35, 7.21] | 5 .. 13 |
| l_width_jitter | 0.178 [0.0726, 0.268] | 0 .. 0.35 |
| l_para_lines | 4.44 [2.25, 7] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.793 [0.642, 0.892] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.394 [0.32, 0.526] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 2] | 0 .. 4 |
| l_line_initial_p | 0.543 [0, 0.678] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0.444 [0, 0.616] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100


## eva_glyph: sınıf sınıf

### grille: taze medyan mesafe 2.81, en iyi 1.42

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| n_symbols | -3.3 | 25.250 | 21.000 |
| wlen_autocorr1 | -3.2 | 0.103 | -0.002 |
| h2_over_h1 | +2.3 | 0.556 | 0.644 |
| rep_within3 | -2.1 | 0.026 | 0.011 |
| h2 | +2.1 | 2.131 | 2.453 |
| rep_adjacent_ed1 | -1.9 | 0.039 | 0.020 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.44 [6.09, 9.32] | 5 .. 13 |
| l_width_jitter | 0.192 [0.11, 0.261] | 0 .. 0.35 |
| l_para_lines | 4.48 [0, 9.22] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.573 [0.466, 0.69] | 0.1 .. 1 |
| l_final_forms_k | 1.5 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 3] | 0 .. 4 |
| l_line_initial_p | 0.399 [0, 0.606] | 0.1 .. 0.9 |
| l_line_final_p | 0.127 [0, 0.341] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.566] | 0.3 .. 1 |
| p_alphabet | 19 [17, 21] | 15 .. 25 |
| p_rows | 1.46e+03 [1.02e+03, 2.36e+03] | 60 .. 3000 |
| p_slot_overlap | 0.689 [0.426, 0.92] | 0 .. 1 |
| p_n_edge | 30.5 [21.5, 37] | 5 .. 40 |
| p_n_mid | 38.5 [20.8, 64] | 10 .. 120 |
| p_empty | 0.323 [0.218, 0.382] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_n_grilles | 6 [5, 7] | 3 .. 8 |

### selfcite: taze medyan mesafe 2.87, en iyi 2.23

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -5.6 | 0.717 | 0.593 |
| h2_over_h1 | +4.4 | 0.556 | 0.723 |
| h2 | +4.4 | 2.131 | 2.810 |
| vocab_ed1_density | +4.0 | 0.850 | 0.940 |
| zipf_slope | +3.4 | -0.778 | -0.567 |
| n_symbols | -3.3 | 25.250 | 21.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 11.6 [10, 12.9] | 5 .. 13 |
| l_width_jitter | 0.176 [0.127, 0.244] | 0 .. 0.35 |
| l_para_lines | 4.57 [0, 7.91] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.635 [0.541, 0.785] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.1] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.594 [0.256, 0.768] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.198] | 0.1 .. 0.9 |
| l_para_initial_p | 0.305 [0, 0.598] | 0.3 .. 1 |
| p_alphabet | 17 [16, 19] | 15 .. 25 |
| p_glyph_classes | 5 [4, 6] | 4 .. 7 |
| p_copy | 0.88 [0.868, 0.908] | 0.85 .. 0.97 |
| p_exact | 0.392 [0.298, 0.478] | 0.2 .. 0.8 |
| p_reach | 20 [16, 25.2] | 1 .. 30 |
| p_same_line | 0.0191 [0.00495, 0.04] | 0 .. 0.3 |
| p_slot_overlap | 0.206 [0.0473, 0.347] | 0 .. 1 |
| p_affix | 0.825 [0.755, 0.883] | 0.3 .. 0.9 |
| p_mut_substitute | 0.56 [0.393, 0.716] | 0 .. 1 |
| p_mut_prefix | 0.419 [0.298, 0.54] | 0 .. 1 |
| p_mut_delete | 0.16 [0.0693, 0.26] | 0 .. 1 |
| p_mut_double | 0.104 [0.0418, 0.169] | 0 .. 1 |

### plain: taze medyan mesafe 3.05, en iyi 2.55

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -6.5 | 0.626 | 0.254 |
| h2 | +4.8 | 2.131 | 2.876 |
| h2_over_h1 | +4.7 | 0.556 | 0.734 |
| wlen_std | -4.7 | 1.552 | 1.302 |
| char_double_rate | -4.6 | 0.076 | 0.009 |
| eff_symbols | +3.7 | 14.404 | 16.118 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.98 [7.12, 11] | 5 .. 13 |
| l_width_jitter | 0.22 [0.15, 0.289] | 0 .. 0.35 |
| l_para_lines | 4.7 [0, 8.06] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.558] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.825 [0.735, 0.885] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.361] | 0.1 .. 0.9 |
| l_line_final_p | 0.153 [0, 0.309] | 0.1 .. 0.9 |
| l_para_initial_p | 0.57 [0, 0.853] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### abjad: taze medyan mesafe 3.59, en iyi 2.78

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +8.4 | 0.017 | 0.115 |
| wlen_frac_le2 | +7.5 | 0.099 | 0.334 |
| wlen_skew | +4.7 | 0.183 | 0.681 |
| h2_over_h1 | +4.3 | 0.556 | 0.720 |
| h2 | +4.2 | 2.131 | 2.784 |
| wlen_mean | -3.8 | 4.528 | 3.371 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.69 [5.74, 11] | 5 .. 13 |
| l_width_jitter | 0.246 [0.125, 0.314] | 0 .. 0.35 |
| l_para_lines | 8.5 [0, 12.7] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0172] | 0.01 .. 0.15 |
| l_final_forms_share | 0.698 [0.598, 0.785] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.312 [0, 0.432] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 2] | 0 .. 4 |
| l_line_initial_p | 0.371 [0.154, 0.595] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0.31 [0, 0.683] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100

### verbose: taze medyan mesafe 3.65, en iyi 2.36

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +7.5 | 1.552 | 1.949 |
| jsd_last | -6.6 | 0.718 | 0.403 |
| hapax_ratio | -5.8 | 0.717 | 0.588 |
| wlen_frac1 | +4.9 | 0.017 | 0.075 |
| wlen_autocorr1 | -3.8 | 0.103 | -0.025 |
| wlen_skew | +3.4 | 0.183 | 0.544 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.48 [5.63, 9.3] | 5 .. 13 |
| l_width_jitter | 0.208 [0.108, 0.279] | 0 .. 0.35 |
| l_para_lines | 5.29 [0, 11.6] | 3 .. 15 |
| l_allo_per_glyph | 0.745 [0.51, 0.912] | 0.2 .. 3 |
| l_allo_rate | 0.0747 [0.0466, 0.109] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0.318] | 0.1 .. 1 |
| l_final_forms_k | 2 [0, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.128] | 0.1 .. 1 |
| l_initial_forms_k | 0.5 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.414 [0.195, 0.536] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.231] | 0.1 .. 0.9 |
| l_para_initial_p | 0.409 [0, 0.58] | 0.3 .. 1 |
| p_alphabet | 15 [13, 16] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Romanian 43, Italian 35, Croatian 9, Portuguese 4, Finnish 2


## v101: sınıf sınıf

### plain: taze medyan mesafe 2.62, en iyi 2.14

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| vocab_ed1_density | -4.7 | 0.854 | 0.744 |
| n_symbols | -4.6 | 69.529 | 26.000 |
| wlen_frac1 | -4.5 | 0.046 | 0.000 |
| h2 | +3.9 | 2.383 | 3.049 |
| h2_over_h1 | +3.9 | 0.595 | 0.757 |
| last_entropy_ratio | -3.8 | 0.704 | 0.469 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.6 [7.64, 12.2] | 5 .. 13 |
| l_width_jitter | 0.211 [0.103, 0.304] | 0 .. 0.35 |
| l_para_lines | 4.88 [0, 8.57] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.281] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.678 [0.594, 0.776] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.392] | 0.1 .. 0.9 |
| l_line_final_p | 0.184 [0, 0.301] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.624] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### abjad: taze medyan mesafe 2.94, en iyi 2.34

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +6.3 | 0.046 | 0.111 |
| wlen_frac_le2 | +5.7 | 0.184 | 0.335 |
| n_symbols | -4.6 | 69.529 | 26.000 |
| first_entropy_ratio | +3.6 | 0.886 | 1.002 |
| h2_over_h1 | +3.5 | 0.595 | 0.740 |
| wlen_skew | +3.3 | 0.225 | 0.679 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.29 [7.02, 11.7] | 5 .. 13 |
| l_width_jitter | 0.114 [0.04, 0.197] | 0 .. 0.35 |
| l_para_lines | 5.66 [0, 9.16] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.309] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0347] | 0.01 .. 0.15 |
| l_final_forms_share | 0.699 [0.623, 0.809] | 0.1 .. 1 |
| l_final_forms_k | 4 [3, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.251] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.349 [0, 0.536] | 0.1 .. 0.9 |
| l_line_final_p | 0.264 [0, 0.401] | 0.1 .. 0.9 |
| l_para_initial_p | 0.368 [0, 0.567] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100

### selfcite: taze medyan mesafe 3.39, en iyi 2.33

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +8.4 | 0.015 | 0.060 |
| n_symbols | -4.4 | 69.529 | 28.000 |
| h2 | +3.8 | 2.383 | 3.036 |
| zipf_slope | +3.7 | -0.776 | -0.612 |
| h2_over_h1 | +3.6 | 0.595 | 0.745 |
| hapax_ratio | -3.2 | 0.741 | 0.647 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.41 [5.72, 10.4] | 5 .. 13 |
| l_width_jitter | 0.183 [0.089, 0.3] | 0 .. 0.35 |
| l_para_lines | 8.91 [3.78, 12] | 3 .. 15 |
| l_allo_per_glyph | 0.523 [0, 2.17] | 0.2 .. 3 |
| l_allo_rate | 0.0442 [0, 0.098] | 0.01 .. 0.15 |
| l_final_forms_share | 0.601 [0.487, 0.77] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.662] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.305] | 0.1 .. 0.9 |
| l_para_initial_p | 0.681 [0, 0.854] | 0.3 .. 1 |
| p_alphabet | 18 [16, 20] | 15 .. 25 |
| p_glyph_classes | 5 [4, 6.25] | 4 .. 7 |
| p_copy | 0.883 [0.857, 0.911] | 0.85 .. 0.97 |
| p_exact | 0.353 [0.245, 0.492] | 0.2 .. 0.8 |
| p_reach | 24 [20, 27] | 1 .. 30 |
| p_same_line | 0.034 [0, 0.0839] | 0 .. 0.3 |
| p_slot_overlap | 0.634 [0.289, 0.872] | 0 .. 1 |
| p_affix | 0.712 [0.572, 0.819] | 0.3 .. 0.9 |
| p_mut_substitute | 0.61 [0.438, 0.765] | 0 .. 1 |
| p_mut_prefix | 0.409 [0.249, 0.576] | 0 .. 1 |
| p_mut_delete | 0.161 [0.0866, 0.24] | 0 .. 1 |
| p_mut_double | 0.00399 [0, 0.0202] | 0 .. 1 |

### verbose: taze medyan mesafe 3.41, en iyi 2.02

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +6.4 | 1.469 | 1.864 |
| char_double_rate | +5.7 | 0.015 | 0.046 |
| type_len_mean | +5.5 | 4.440 | 5.106 |
| jsd_last | -4.1 | 0.679 | 0.467 |
| rep_adjacent_ed1 | -3.7 | 0.043 | 0.017 |
| wlen_autocorr1 | -3.5 | 0.179 | -0.032 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.53 [7.6, 11.3] | 5 .. 13 |
| l_width_jitter | 0.26 [0.149, 0.329] | 0 .. 0.35 |
| l_para_lines | 0 [0, 12.9] | 3 .. 15 |
| l_allo_per_glyph | 1.89 [1.43, 2.31] | 0.2 .. 3 |
| l_allo_rate | 0.0965 [0.0726, 0.118] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0.194] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.528] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.352] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.442] | 0.3 .. 1 |
| p_alphabet | 17 [15, 19] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Croatian 72, Romanian 19, Italian 7, Turkish 1, Swedish 1

### grille: taze medyan mesafe 3.54, en iyi 1.89

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +7.9 | 0.015 | 0.058 |
| wlen_autocorr1 | -3.0 | 0.179 | -0.000 |
| vocab_ed1_density | +2.9 | 0.854 | 0.920 |
| n_symbols | -2.3 | 69.529 | 47.500 |
| hapax_ratio | -2.2 | 0.741 | 0.677 |
| jsd_line_initial | -1.8 | 0.287 | 0.128 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.47 [6.01, 10.5] | 5 .. 13 |
| l_width_jitter | 0.21 [0.116, 0.307] | 0 .. 0.35 |
| l_para_lines | 6.87 [0, 12.8] | 3 .. 15 |
| l_allo_per_glyph | 1.68 [0.943, 2.44] | 0.2 .. 3 |
| l_allo_rate | 0.0733 [0.0372, 0.111] | 0.01 .. 0.15 |
| l_final_forms_share | 0.513 [0.222, 0.674] | 0.1 .. 1 |
| l_final_forms_k | 2.5 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.243 [0, 0.543] | 0.1 .. 0.9 |
| l_line_final_p | 0.134 [0, 0.342] | 0.1 .. 0.9 |
| l_para_initial_p | 0.385 [0, 0.769] | 0.3 .. 1 |
| p_alphabet | 21 [18, 23] | 15 .. 25 |
| p_rows | 938 [522, 1.69e+03] | 60 .. 3000 |
| p_slot_overlap | 0.83 [0.624, 1] | 0 .. 1 |
| p_n_edge | 25 [13.8, 37.8] | 5 .. 40 |
| p_n_mid | 32 [17.2, 61.5] | 10 .. 120 |
| p_empty | 0.397 [0.321, 0.48] | 0 .. 0.6 |
| p_len_edge | 2 [1, 2] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_n_grilles | 5 [4, 6] | 3 .. 8 |


## zl_basic: sınıf sınıf

### grille: taze medyan mesafe 3.13, en iyi 1.92

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| h2_over_h1 | +3.2 | 0.521 | 0.628 |
| h2 | +2.9 | 2.013 | 2.413 |
| wlen_autocorr1 | -2.6 | 0.123 | -0.000 |
| vocab_ed1_density | +2.5 | 0.823 | 0.877 |
| rep_adjacent_ed1 | -2.4 | 0.034 | 0.018 |
| hapax_ratio | -2.1 | 0.715 | 0.647 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.3 [6.98, 12.1] | 5 .. 13 |
| l_width_jitter | 0.168 [0.0662, 0.273] | 0 .. 0.35 |
| l_para_lines | 4.49 [0, 11.1] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.998] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0443] | 0.01 .. 0.15 |
| l_final_forms_share | 0.538 [0.403, 0.732] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.192 [0, 0.501] | 0.1 .. 0.9 |
| l_line_final_p | 0.243 [0, 0.35] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.493] | 0.3 .. 1 |
| p_alphabet | 19 [17, 21] | 15 .. 25 |
| p_rows | 1.09e+03 [556, 1.63e+03] | 60 .. 3000 |
| p_slot_overlap | 0.607 [0.273, 0.852] | 0 .. 1 |
| p_n_edge | 22 [16, 30] | 5 .. 40 |
| p_n_mid | 31 [18.5, 86.2] | 10 .. 120 |
| p_empty | 0.349 [0.282, 0.413] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 5] | 2 .. 5 |
| p_n_grilles | 7 [4.75, 8] | 3 .. 8 |

### verbose: taze medyan mesafe 3.47, en iyi 2.21

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +5.8 | 0.097 | 0.175 |
| wlen_skew | +5.0 | 0.025 | 0.531 |
| hapax_ratio | -4.8 | 0.715 | 0.561 |
| wlen_std | +4.3 | 1.768 | 2.029 |
| first_entropy_ratio | +4.0 | 0.817 | 0.885 |
| wlen_frac1 | +3.8 | 0.033 | 0.071 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.27 [7.21, 11.7] | 5 .. 13 |
| l_width_jitter | 0.151 [0.0377, 0.251] | 0 .. 0.35 |
| l_para_lines | 5.04 [0, 11.5] | 3 .. 15 |
| l_allo_per_glyph | 0.565 [0, 1.1] | 0.2 .. 3 |
| l_allo_rate | 0.0757 [0, 0.119] | 0.01 .. 0.15 |
| l_final_forms_share | 0.443 [0.108, 0.623] | 0.1 .. 1 |
| l_final_forms_k | 2.5 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.259] | 0.1 .. 1 |
| l_initial_forms_k | 0.5 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.32 [0, 0.483] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.331] | 0.1 .. 0.9 |
| l_para_initial_p | 0.396 [0, 0.637] | 0.3 .. 1 |
| p_alphabet | 14 [12, 16] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 56, Polish 19, Czech 13, Albanian 4, Croatian 4

### selfcite: taze medyan mesafe 3.47, en iyi 2.60

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| h2_over_h1 | +5.4 | 0.521 | 0.702 |
| h2 | +4.9 | 2.013 | 2.699 |
| vocab_ed1_density | +4.8 | 0.823 | 0.928 |
| char_double_rate | +4.3 | 0.066 | 0.130 |
| type_len_mean | -4.1 | 5.640 | 4.903 |
| first_entropy_ratio | +4.1 | 0.817 | 0.886 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 11.1 [9.52, 12.6] | 5 .. 13 |
| l_width_jitter | 0.147 [0.0524, 0.239] | 0 .. 0.35 |
| l_para_lines | 7.49 [4.42, 11] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.86] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.704 [0.54, 0.809] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.289] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.53 [0.333, 0.697] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.265] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0] | 0.3 .. 1 |
| p_alphabet | 16 [15, 17] | 15 .. 25 |
| p_glyph_classes | 5 [4, 6] | 4 .. 7 |
| p_copy | 0.891 [0.862, 0.918] | 0.85 .. 0.97 |
| p_exact | 0.321 [0.244, 0.451] | 0.2 .. 0.8 |
| p_reach | 24 [17, 30] | 1 .. 30 |
| p_same_line | 0.0462 [0.0138, 0.0748] | 0 .. 0.3 |
| p_slot_overlap | 0.509 [0.197, 0.828] | 0 .. 1 |
| p_affix | 0.837 [0.725, 0.9] | 0.3 .. 0.9 |
| p_mut_substitute | 0.269 [0.149, 0.446] | 0 .. 1 |
| p_mut_prefix | 0.63 [0.407, 0.82] | 0 .. 1 |
| p_mut_delete | 0.0546 [0.0199, 0.116] | 0 .. 1 |
| p_mut_double | 0.122 [0.0705, 0.163] | 0 .. 1 |

### plain: taze medyan mesafe 3.68, en iyi 3.19

Voynich'ten 2 birimden fazla sapan feature sayısı: 21

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -8.2 | 0.636 | 0.095 |
| first_entropy_ratio | +6.0 | 0.817 | 0.919 |
| h2 | +5.9 | 2.013 | 2.829 |
| h2_over_h1 | +5.8 | 0.521 | 0.717 |
| vocab_ed1_density | -5.3 | 0.823 | 0.710 |
| jsd_last | +4.8 | 0.712 | 0.930 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 11.7 [9.8, 12.4] | 5 .. 13 |
| l_width_jitter | 0.125 [0.0596, 0.214] | 0 .. 0.35 |
| l_para_lines | 1.67 [0, 10.3] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.937 [0.853, 0.989] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0.5 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.349] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.663] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Arabic 95, Hebrew 5

### abjad: taze medyan mesafe 4.97, en iyi 3.66

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +17.2 | 0.097 | 0.327 |
| wlen_frac1 | +7.9 | 0.033 | 0.114 |
| wlen_mean | -6.9 | 4.961 | 3.405 |
| type_len_mean | -6.4 | 5.640 | 4.486 |
| wlen_skew | +6.3 | 0.025 | 0.668 |
| h2_over_h1 | +5.3 | 0.521 | 0.699 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.4 [5.2, 9.59] | 5 .. 13 |
| l_width_jitter | 0.188 [0.0568, 0.258] | 0 .. 0.35 |
| l_para_lines | 5.47 [0, 12.7] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.714 [0.556, 0.806] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0.519 [0.412, 0.585] | 0.1 .. 1 |
| l_initial_forms_k | 2 [2, 3] | 0 .. 4 |
| l_line_initial_p | 0.514 [0.349, 0.671] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0.491 [0.302, 0.62] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 99, Finnish 1


## zl_glyph: sınıf sınıf

### grille: taze medyan mesafe 2.46, en iyi 1.30

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -2.7 | 0.102 | -0.005 |
| vocab_ed1_density | +2.3 | 0.852 | 0.889 |
| n_symbols | -2.2 | 44.750 | 24.000 |
| jsd_line_final | -2.1 | 0.110 | 0.029 |
| h2_over_h1 | +1.9 | 0.554 | 0.632 |
| h2 | +1.6 | 2.127 | 2.413 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.5 [8.5, 11.5] | 5 .. 13 |
| l_width_jitter | 0.208 [0.108, 0.287] | 0 .. 0.35 |
| l_para_lines | 4.77 [0, 9.07] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 2.08] | 0.2 .. 3 |
| l_allo_rate | 0.0414 [0, 0.0658] | 0.01 .. 0.15 |
| l_final_forms_share | 0.565 [0.463, 0.713] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.249 [0, 0.469] | 0.1 .. 0.9 |
| l_line_final_p | 0.065 [0, 0.283] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0] | 0.3 .. 1 |
| p_alphabet | 18 [15.8, 21] | 15 .. 25 |
| p_rows | 1.26e+03 [632, 2.24e+03] | 60 .. 3000 |
| p_slot_overlap | 0.553 [0.31, 0.804] | 0 .. 1 |
| p_n_edge | 26 [19, 33.2] | 5 .. 40 |
| p_n_mid | 35.5 [17, 67] | 10 .. 120 |
| p_empty | 0.361 [0.3, 0.433] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_n_grilles | 7 [5, 8] | 3 .. 8 |

### selfcite: taze medyan mesafe 2.55, en iyi 1.93

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| vocab_ed1_density | +4.5 | 0.852 | 0.924 |
| hapax_ratio | -4.1 | 0.715 | 0.583 |
| h2_over_h1 | +4.0 | 0.554 | 0.718 |
| h2 | +3.6 | 2.127 | 2.756 |
| jsd_last | +2.8 | 0.712 | 0.840 |
| n_symbols | -2.6 | 44.750 | 20.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.54 [8.32, 11.1] | 5 .. 13 |
| l_width_jitter | 0.286 [0.189, 0.331] | 0 .. 0.35 |
| l_para_lines | 6.77 [4.19, 8.96] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.25] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0046] | 0.01 .. 0.15 |
| l_final_forms_share | 0.803 [0.657, 0.925] | 0.1 .. 1 |
| l_final_forms_k | 3 [2.75, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.297 [0, 0.475] | 0.1 .. 0.9 |
| l_line_final_p | 0.208 [0.117, 0.302] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.506] | 0.3 .. 1 |
| p_alphabet | 16 [15, 17] | 15 .. 25 |
| p_glyph_classes | 6 [5, 7] | 4 .. 7 |
| p_copy | 0.874 [0.858, 0.885] | 0.85 .. 0.97 |
| p_exact | 0.431 [0.351, 0.575] | 0.2 .. 0.8 |
| p_reach | 25 [19, 28] | 1 .. 30 |
| p_same_line | 0.016 [0.00338, 0.033] | 0 .. 0.3 |
| p_slot_overlap | 0.447 [0.275, 0.675] | 0 .. 1 |
| p_affix | 0.744 [0.669, 0.808] | 0.3 .. 0.9 |
| p_mut_substitute | 0.571 [0.418, 0.713] | 0 .. 1 |
| p_mut_prefix | 0.514 [0.337, 0.617] | 0 .. 1 |
| p_mut_delete | 0.125 [0.0539, 0.198] | 0 .. 1 |
| p_mut_double | 0.0479 [0.0101, 0.0985] | 0 .. 1 |

### verbose: taze medyan mesafe 2.84, en iyi 1.72

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +4.9 | 1.615 | 1.885 |
| wlen_skew | +4.2 | 0.154 | 0.579 |
| jsd_last | -3.5 | 0.712 | 0.551 |
| wlen_frac1 | +3.5 | 0.033 | 0.070 |
| wlen_autocorr1 | -3.2 | 0.102 | -0.024 |
| rep_adjacent_exact | -2.4 | 0.008 | 0.003 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.21 [7.23, 11.3] | 5 .. 13 |
| l_width_jitter | 0.215 [0.117, 0.305] | 0 .. 0.35 |
| l_para_lines | 0 [0, 7.97] | 3 .. 15 |
| l_allo_per_glyph | 2.35 [1.72, 2.76] | 0.2 .. 3 |
| l_allo_rate | 0.0508 [0.0393, 0.0661] | 0.01 .. 0.15 |
| l_final_forms_share | 0.381 [0.206, 0.543] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.477] | 0.1 .. 0.9 |
| l_line_final_p | 0.136 [0, 0.277] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.393] | 0.3 .. 1 |
| p_alphabet | 13 [12, 15] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Romanian 60, Italian 16, Croatian 14, Finnish 3, Czech 2

### plain: taze medyan mesafe 2.90, en iyi 2.37

Voynich'ten 2 birimden fazla sapan feature sayısı: 19

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -6.0 | 0.636 | 0.267 |
| wlen_std | -5.5 | 1.615 | 1.311 |
| vocab_ed1_density | -4.6 | 0.852 | 0.778 |
| h2_over_h1 | +4.5 | 0.554 | 0.736 |
| h2 | +4.4 | 2.127 | 2.888 |
| char_double_rate | -4.2 | 0.076 | 0.009 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.25 [7.43, 11.3] | 5 .. 13 |
| l_width_jitter | 0.224 [0.106, 0.298] | 0 .. 0.35 |
| l_para_lines | 3.03 [0, 11.6] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.127] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.77 [0.701, 0.866] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.333] | 0.1 .. 0.9 |
| l_line_final_p | 0.193 [0, 0.289] | 0.1 .. 0.9 |
| l_para_initial_p | 0.3 [0, 0.552] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 99, Arabic 1

### abjad: taze medyan mesafe 3.26, en iyi 2.40

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +7.3 | 0.033 | 0.111 |
| wlen_frac_le2 | +6.4 | 0.119 | 0.333 |
| wlen_skew | +5.0 | 0.154 | 0.665 |
| vocab_ed1_density | -4.3 | 0.852 | 0.783 |
| h2_over_h1 | +3.8 | 0.554 | 0.711 |
| h2 | +3.8 | 2.127 | 2.794 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.37 [5.46, 9.83] | 5 .. 13 |
| l_width_jitter | 0.213 [0.136, 0.295] | 0 .. 0.35 |
| l_para_lines | 8.46 [0, 12] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.751 [0.645, 0.833] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.369 [0, 0.469] | 0.1 .. 1 |
| l_initial_forms_k | 1.5 [1, 3] | 0 .. 4 |
| l_line_initial_p | 0.413 [0, 0.673] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.328] | 0.1 .. 0.9 |
| l_para_initial_p | 0.551 [0, 0.794] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100
