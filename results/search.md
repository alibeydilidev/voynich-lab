# Yönlendirilmiş arama raporu: her hipotezin ulaşabildiği en iyi nokta

Her (sınıf, görünüm) için 5 tur, tur başına 600 deneme, en yakın 100 ayar tutuldu. Tablolardaki mesafeler, son turda kalan ayarların her biriyle yeniden üretilen 2 taze örnekten hesaplandı (toplam 200).

Mesafe birimi ve ölçüt `abc.md` ile aynı: bir hipotezin taze örnekleri Voynich öz mesafesinin içine giriyorsa, o hipotez bu feature kümesinde Voynich'ten ayırt edilemez.

## 1. Taze örneklerin medyan mesafesi (parantezde rejection ABC'deki değer)

| görünüm | Voynich öz mesafesi (medyan, en çok) | abjad | grille | plain | selfcite | slotcite | verbose |
|---|---|---|---|---|---|---|---|
| eva_basic | 0.91, 1.65 | 5.87 (6.19) | 3.12 (2.77) | 4.15 (5.34) | 3.71 (4.45) | 3.50 (3.09) | 4.14 (3.98) |
| eva_glyph | 0.96, 1.63 | 3.50 (3.96) | 2.63 (2.49) | 3.00 (4.20) | 2.84 (3.57) | 2.96 (2.82) | 3.44 (3.57) |
| v101 | 0.97, 1.42 | 2.94 (3.36) | 3.54 (2.53) | 2.62 (3.02) | 3.39 (3.90) | 3.81 (2.95) | 3.50 (3.27) |
| zl_basic | 0.96, 1.52 | 4.97 (5.36) | 3.13 (2.44) | 3.68 (4.71) | 3.47 (3.96) | 3.00 (2.73) | 3.56 (3.26) |
| zl_glyph | 1.03, 1.43 | 3.26 (3.54) | 2.46 (2.15) | 2.90 (3.76) | 2.55 (3.12) | 2.60 (2.43) | 2.77 (2.89) |

## 2. Voynich'in en uç penceresi kadar yakın olan taze örneklerin oranı

| görünüm | abjad | grille | plain | selfcite | slotcite | verbose |
|---|---|---|---|---|---|---|
| eva_basic | %0 | %0 | %0 | %0 | %0 | %0 |
| eva_glyph | %0 | %0 | %0 | %0 | %0 | %0 |
| v101 | %0 | %0 | %0 | %0 | %0 | %0 |
| zl_basic | %0 | %0 | %0 | %0 | %0 | %0 |
| zl_glyph | %0 | %0 | %0 | %0 | %0 | %0 |

## 3. Arama yakınsadı mı (tur tur, tutulan ayarların medyan mesafesi)

| görünüm | sınıf | turlar |
|---|---|---|
| eva_basic | abjad | 5.96 -> 5.78 -> 5.53 -> 5.46 -> 5.31 |
| eva_basic | grille | 2.95 -> 2.80 -> 2.69 -> 2.66 -> 2.58 |
| eva_basic | plain | 4.87 -> 4.21 -> 3.99 -> 3.90 -> 3.87 |
| eva_basic | selfcite | 4.14 -> 3.82 -> 3.71 -> 3.50 -> 3.44 |
| eva_basic | slotcite | 3.09 -> 3.08 -> 2.93 -> 2.86 -> 2.85 |
| eva_basic | verbose | 3.87 -> 3.63 -> 3.67 -> 3.63 -> 3.60 |
| eva_glyph | abjad | 3.65 -> 3.50 -> 3.35 -> 3.31 -> 3.19 |
| eva_glyph | grille | 2.52 -> 2.45 -> 2.39 -> 2.26 -> 2.27 |
| eva_glyph | plain | 3.78 -> 3.20 -> 2.90 -> 2.80 -> 2.81 |
| eva_glyph | selfcite | 3.28 -> 3.05 -> 2.82 -> 2.70 -> 2.62 |
| eva_glyph | slotcite | 2.89 -> 2.74 -> 2.55 -> 2.49 -> 2.43 |
| eva_glyph | verbose | 3.51 -> 3.36 -> 3.09 -> 3.09 -> 3.02 |
| v101 | abjad | 3.02 -> 2.81 -> 2.71 -> 2.66 -> 2.64 |
| v101 | grille | 2.99 -> 2.80 -> 2.86 -> 2.78 -> 2.80 |
| v101 | plain | 2.66 -> 2.46 -> 2.40 -> 2.38 -> 2.37 |
| v101 | selfcite | 3.53 -> 3.34 -> 3.15 -> 3.07 -> 2.85 |
| v101 | slotcite | 3.15 -> 3.05 -> 2.98 -> 2.97 -> 2.93 |
| v101 | verbose | 3.25 -> 2.99 -> 2.87 -> 2.89 -> 2.80 |
| zl_basic | abjad | 5.28 -> 5.11 -> 4.97 -> 4.66 -> 4.58 |
| zl_basic | grille | 2.61 -> 2.60 -> 2.57 -> 2.53 -> 2.43 |
| zl_basic | plain | 4.10 -> 3.66 -> 3.55 -> 3.49 -> 3.44 |
| zl_basic | selfcite | 3.71 -> 3.36 -> 3.25 -> 3.13 -> 3.02 |
| zl_basic | slotcite | 2.87 -> 2.68 -> 2.55 -> 2.55 -> 2.43 |
| zl_basic | verbose | 3.16 -> 3.07 -> 3.06 -> 3.06 -> 3.02 |
| zl_glyph | abjad | 3.36 -> 3.20 -> 3.05 -> 3.06 -> 2.97 |
| zl_glyph | grille | 2.30 -> 2.24 -> 2.17 -> 2.10 -> 2.03 |
| zl_glyph | plain | 3.24 -> 2.86 -> 2.75 -> 2.71 -> 2.69 |
| zl_glyph | selfcite | 2.89 -> 2.71 -> 2.56 -> 2.41 -> 2.31 |
| zl_glyph | slotcite | 2.54 -> 2.36 -> 2.25 -> 2.19 -> 2.09 |
| zl_glyph | verbose | 2.78 -> 2.64 -> 2.57 -> 2.46 -> 2.43 |

## eva_basic: sınıf sınıf

### grille: taze medyan mesafe 3.12, en iyi 1.94

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -3.3 | 0.127 | -0.000 |
| h2_over_h1 | +3.2 | 0.524 | 0.623 |
| jsd_line_final | -3.0 | 0.109 | 0.014 |
| h2 | +2.9 | 2.016 | 2.370 |
| hapax_ratio | -2.9 | 0.717 | 0.653 |
| rep_adjacent_ed1 | -2.6 | 0.032 | 0.015 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.36 [6.09, 9.27] | 5 .. 13 |
| l_width_jitter | 0.172 [0.0914, 0.27] | 0 .. 0.35 |
| l_para_lines | 4.77 [0, 7.87] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.507 [0.361, 0.655] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.139 [0, 0.49] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.233] | 0.1 .. 0.9 |
| l_para_initial_p | 0.615 [0.225, 0.824] | 0.3 .. 1 |
| p_alphabet | 20 [18, 22] | 15 .. 25 |
| p_rows | 1.25e+03 [778, 1.81e+03] | 60 .. 3000 |
| p_slot_overlap | 0.367 [0.206, 0.631] | 0 .. 1 |
| p_n_edge | 25 [18, 33] | 5 .. 40 |
| p_n_mid | 22.5 [13, 44.2] | 10 .. 120 |
| p_empty | 0.233 [0.17, 0.289] | 0 .. 0.6 |
| p_len_edge | 3 [3, 3] | 1 .. 3 |
| p_len_mid | 3 [3, 4] | 2 .. 5 |
| p_n_grilles | 5 [4, 7] | 3 .. 8 |

### slotcite: taze medyan mesafe 3.50, en iyi 2.12

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -5.6 | 0.717 | 0.593 |
| h2_over_h1 | +3.4 | 0.524 | 0.631 |
| h2 | +3.3 | 2.016 | 2.408 |
| zipf_slope | +3.0 | -0.778 | -0.591 |
| vocab_ed1_density | +2.6 | 0.823 | 0.888 |
| wlen_frac_le2 | -2.6 | 0.077 | 0.047 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.75 [6.29, 9.92] | 5 .. 13 |
| l_width_jitter | 0.213 [0.108, 0.298] | 0 .. 0.35 |
| l_para_lines | 0 [0, 5.38] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0228] | 0.01 .. 0.15 |
| l_final_forms_share | 0.493 [0.291, 0.66] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.328 [0, 0.531] | 0.1 .. 0.9 |
| l_line_final_p | 0.145 [0, 0.334] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.545] | 0.3 .. 1 |
| p_alphabet | 19 [17, 21] | 15 .. 25 |
| p_slot_overlap | 0.58 [0.389, 0.819] | 0 .. 1 |
| p_n_edge | 25 [16.8, 34] | 5 .. 40 |
| p_n_mid | 29.5 [19, 70] | 10 .. 120 |
| p_empty | 0.235 [0.144, 0.329] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_copy | 0.639 [0.536, 0.752] | 0.5 .. 0.97 |
| p_exact | 0.163 [0.1, 0.28] | 0.1 .. 0.7 |
| p_reach | 11 [6, 18.2] | 1 .. 30 |
| p_same_line | 0.128 [0.0451, 0.217] | 0 .. 0.5 |
| p_mut_prefix | 0.28 [0.17, 0.456] | 0 .. 1 |
| p_mut_mid | 0.425 [0.145, 0.661] | 0 .. 1 |
| p_mut_suffix | 0.296 [0.102, 0.622] | 0 .. 1 |

### selfcite: taze medyan mesafe 3.71, en iyi 2.72

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -6.0 | 0.717 | 0.583 |
| h2 | +6.0 | 2.016 | 2.737 |
| h2_over_h1 | +6.0 | 0.524 | 0.709 |
| char_double_rate | +5.0 | 0.067 | 0.136 |
| first_entropy_ratio | +5.0 | 0.806 | 0.896 |
| vocab_ed1_density | +4.3 | 0.823 | 0.929 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.7 [8.76, 11.6] | 5 .. 13 |
| l_width_jitter | 0.285 [0.204, 0.333] | 0 .. 0.35 |
| l_para_lines | 7.86 [0, 10.4] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.626 [0.438, 0.823] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.335] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.506 [0.356, 0.648] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.284] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.701] | 0.3 .. 1 |
| p_alphabet | 16.5 [15, 18] | 15 .. 25 |
| p_glyph_classes | 6 [5, 7] | 4 .. 7 |
| p_copy | 0.893 [0.865, 0.921] | 0.85 .. 0.97 |
| p_exact | 0.476 [0.354, 0.587] | 0.2 .. 0.8 |
| p_reach | 26 [21, 30] | 1 .. 30 |
| p_same_line | 0.0422 [0.0136, 0.0643] | 0 .. 0.3 |
| p_slot_overlap | 0.394 [0.188, 0.595] | 0 .. 1 |
| p_affix | 0.865 [0.812, 0.9] | 0.3 .. 0.9 |
| p_mut_substitute | 0.518 [0.355, 0.751] | 0 .. 1 |
| p_mut_prefix | 0.416 [0.291, 0.54] | 0 .. 1 |
| p_mut_delete | 0.102 [0.0373, 0.174] | 0 .. 1 |
| p_mut_double | 0.167 [0.0971, 0.272] | 0 .. 1 |

### verbose: taze medyan mesafe 4.14, en iyi 2.58

Voynich'ten 2 birimden fazla sapan feature sayısı: 19

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -8.8 | 0.717 | 0.521 |
| wlen_frac_le2 | +8.3 | 0.077 | 0.173 |
| first_entropy_ratio | +4.9 | 0.806 | 0.894 |
| wlen_frac1 | +4.5 | 0.017 | 0.068 |
| wlen_std | +4.3 | 1.693 | 2.005 |
| wlen_autocorr1 | -4.2 | 0.127 | -0.033 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.31 [6.12, 10.5] | 5 .. 13 |
| l_width_jitter | 0.248 [0.16, 0.303] | 0 .. 0.35 |
| l_para_lines | 4.21 [0, 8.96] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0155] | 0.01 .. 0.15 |
| l_final_forms_share | 0.614 [0.292, 0.829] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.181] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.438 [0.236, 0.583] | 0.1 .. 0.9 |
| l_line_final_p | 0.31 [0, 0.415] | 0.1 .. 0.9 |
| l_para_initial_p | 0.482 [0.225, 0.78] | 0.3 .. 1 |
| p_alphabet | 14 [13, 16] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0.0127] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 23, Croatian 18, Polish 18, Finnish 11, Russian 11

### plain: taze medyan mesafe 4.15, en iyi 3.33

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -7.4 | 0.628 | 0.175 |
| first_entropy_ratio | +7.4 | 0.806 | 0.939 |
| h2 | +6.7 | 2.016 | 2.819 |
| type_len_mean | -6.6 | 5.692 | 4.567 |
| wlen_frac_le2 | +6.5 | 0.077 | 0.152 |
| h2_over_h1 | +6.4 | 0.524 | 0.722 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.6 [7.94, 12.3] | 5 .. 13 |
| l_width_jitter | 0.242 [0.132, 0.326] | 0 .. 0.35 |
| l_para_lines | 0 [0, 6.51] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.875 [0.826, 0.948] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.411] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.264] | 0.1 .. 0.9 |
| l_para_initial_p | 0.422 [0, 0.803] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 84, Arabic 16

### abjad: taze medyan mesafe 5.87, en iyi 4.53

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +22.2 | 0.077 | 0.333 |
| wlen_frac1 | +8.4 | 0.017 | 0.111 |
| wlen_mean | -7.2 | 5.066 | 3.388 |
| type_len_mean | -7.1 | 5.692 | 4.480 |
| h2 | +5.8 | 2.016 | 2.710 |
| h2_over_h1 | +5.7 | 0.524 | 0.702 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.77 [5.29, 8.29] | 5 .. 13 |
| l_width_jitter | 0.225 [0.0968, 0.331] | 0 .. 0.35 |
| l_para_lines | 6.45 [0, 11.5] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.685 [0.57, 0.825] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 2.25] | 0 .. 4 |
| l_initial_forms_share | 0.49 [0.412, 0.594] | 0.1 .. 1 |
| l_initial_forms_k | 2 [2, 3] | 0 .. 4 |
| l_line_initial_p | 0.497 [0, 0.745] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.326] | 0.1 .. 0.9 |
| l_para_initial_p | 0.453 [0.225, 0.674] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100


## eva_glyph: sınıf sınıf

### grille: taze medyan mesafe 2.63, en iyi 1.60

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -3.4 | 0.103 | -0.009 |
| jsd_line_final | -3.1 | 0.110 | 0.011 |
| n_symbols | -2.6 | 25.250 | 22.000 |
| hapax_ratio | -2.6 | 0.717 | 0.660 |
| rep_within3 | -2.3 | 0.026 | 0.010 |
| vocab_ed1_density | +2.1 | 0.850 | 0.897 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.62 [6.58, 10.1] | 5 .. 13 |
| l_width_jitter | 0.185 [0.0863, 0.299] | 0 .. 0.35 |
| l_para_lines | 7.09 [0, 10.3] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0269] | 0.01 .. 0.15 |
| l_final_forms_share | 0.564 [0.481, 0.682] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.215 [0, 0.416] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.259] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.471] | 0.3 .. 1 |
| p_alphabet | 19 [18, 21] | 15 .. 25 |
| p_rows | 1.52e+03 [920, 2.45e+03] | 60 .. 3000 |
| p_slot_overlap | 0.484 [0.251, 0.87] | 0 .. 1 |
| p_n_edge | 27.5 [21, 34] | 5 .. 40 |
| p_n_mid | 42 [22, 75] | 10 .. 120 |
| p_empty | 0.294 [0.244, 0.371] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_n_grilles | 6 [5, 8] | 3 .. 8 |

### selfcite: taze medyan mesafe 2.84, en iyi 2.06

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| h2 | +4.4 | 2.131 | 2.813 |
| h2_over_h1 | +4.3 | 0.556 | 0.718 |
| hapax_ratio | -4.2 | 0.717 | 0.624 |
| vocab_ed1_density | +3.6 | 0.850 | 0.930 |
| zipf_slope | +3.0 | -0.778 | -0.592 |
| n_symbols | -2.6 | 25.250 | 22.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.98 [7.8, 12.1] | 5 .. 13 |
| l_width_jitter | 0.0647 [0.0161, 0.128] | 0 .. 0.35 |
| l_para_lines | 4.96 [3, 6.95] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.901] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.769 [0.652, 0.894] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.369 [0, 0.503] | 0.1 .. 0.9 |
| l_line_final_p | 0.354 [0.265, 0.434] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.344] | 0.3 .. 1 |
| p_alphabet | 18 [16, 20] | 15 .. 25 |
| p_glyph_classes | 5 [4, 6] | 4 .. 7 |
| p_copy | 0.874 [0.859, 0.895] | 0.85 .. 0.97 |
| p_exact | 0.268 [0.224, 0.329] | 0.2 .. 0.8 |
| p_reach | 25 [20, 29] | 1 .. 30 |
| p_same_line | 0.0194 [0.00488, 0.0398] | 0 .. 0.3 |
| p_slot_overlap | 0.603 [0.176, 0.848] | 0 .. 1 |
| p_affix | 0.803 [0.694, 0.849] | 0.3 .. 0.9 |
| p_mut_substitute | 0.282 [0.123, 0.402] | 0 .. 1 |
| p_mut_prefix | 0.706 [0.581, 0.832] | 0 .. 1 |
| p_mut_delete | 0.108 [0.0381, 0.16] | 0 .. 1 |
| p_mut_double | 0.0946 [0.0591, 0.14] | 0 .. 1 |

### slotcite: taze medyan mesafe 2.96, en iyi 1.47

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -3.8 | 0.717 | 0.632 |
| jsd_line_final | -3.0 | 0.110 | 0.015 |
| n_symbols | -2.6 | 25.250 | 22.000 |
| h2_over_h1 | +2.5 | 0.556 | 0.649 |
| h2 | +2.3 | 2.131 | 2.491 |
| zipf_slope | +2.3 | -0.778 | -0.634 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.88 [8.08, 11.8] | 5 .. 13 |
| l_width_jitter | 0.112 [0.0335, 0.218] | 0 .. 0.35 |
| l_para_lines | 3.54 [0, 12.1] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0261] | 0.01 .. 0.15 |
| l_final_forms_share | 0.585 [0.425, 0.695] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.571 [0.446, 0.704] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.254] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.528] | 0.3 .. 1 |
| p_alphabet | 19 [17, 22] | 15 .. 25 |
| p_slot_overlap | 0.474 [0.283, 0.699] | 0 .. 1 |
| p_n_edge | 33 [25.8, 38] | 5 .. 40 |
| p_n_mid | 41.5 [25.5, 75.2] | 10 .. 120 |
| p_empty | 0.272 [0.21, 0.34] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 3] | 2 .. 5 |
| p_copy | 0.589 [0.54, 0.672] | 0.5 .. 0.97 |
| p_exact | 0.158 [0.107, 0.294] | 0.1 .. 0.7 |
| p_reach | 8.5 [5, 16.8] | 1 .. 30 |
| p_same_line | 0.141 [0.0664, 0.298] | 0 .. 0.5 |
| p_mut_prefix | 0.243 [0.119, 0.363] | 0 .. 1 |
| p_mut_mid | 0.347 [0.197, 0.623] | 0 .. 1 |
| p_mut_suffix | 0.438 [0.216, 0.632] | 0 .. 1 |

### plain: taze medyan mesafe 3.00, en iyi 2.47

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -6.2 | 0.626 | 0.268 |
| h2 | +4.8 | 2.131 | 2.884 |
| h2_over_h1 | +4.8 | 0.556 | 0.736 |
| char_double_rate | -4.6 | 0.076 | 0.009 |
| wlen_std | -4.6 | 1.552 | 1.314 |
| eff_symbols | +3.5 | 14.404 | 16.017 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.66 [6.44, 10.6] | 5 .. 13 |
| l_width_jitter | 0.195 [0.102, 0.279] | 0 .. 0.35 |
| l_para_lines | 4.68 [0, 7] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.652] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.793 [0.728, 0.887] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1.25] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.429] | 0.1 .. 0.9 |
| l_line_final_p | 0.169 [0, 0.321] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.643] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### verbose: taze medyan mesafe 3.44, en iyi 2.13

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +6.4 | 1.552 | 1.886 |
| jsd_last | -4.6 | 0.718 | 0.500 |
| hapax_ratio | -4.4 | 0.717 | 0.619 |
| wlen_skew | +4.0 | 0.183 | 0.609 |
| wlen_frac1 | +3.9 | 0.017 | 0.062 |
| wlen_autocorr1 | -3.9 | 0.103 | -0.026 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.22 [6.56, 10.5] | 5 .. 13 |
| l_width_jitter | 0.243 [0.139, 0.314] | 0 .. 0.35 |
| l_para_lines | 5.49 [0, 9.61] | 3 .. 15 |
| l_allo_per_glyph | 0.813 [0.604, 1.11] | 0.2 .. 3 |
| l_allo_rate | 0.106 [0.0729, 0.139] | 0.01 .. 0.15 |
| l_final_forms_share | 0.311 [0, 0.607] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.109] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.282 [0, 0.625] | 0.1 .. 0.9 |
| l_line_final_p | 0.199 [0, 0.369] | 0.1 .. 0.9 |
| l_para_initial_p | 0.362 [0, 0.582] | 0.3 .. 1 |
| p_alphabet | 13 [12, 14] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Croatian 42, Romanian 36, Italian 14, Finnish 4, Russian 2

### abjad: taze medyan mesafe 3.50, en iyi 2.69

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +8.3 | 0.017 | 0.115 |
| wlen_frac_le2 | +7.6 | 0.099 | 0.338 |
| wlen_skew | +4.7 | 0.183 | 0.679 |
| h2_over_h1 | +3.9 | 0.556 | 0.701 |
| wlen_mean | -3.9 | 4.528 | 3.345 |
| h2 | +3.7 | 2.131 | 2.712 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.4 [5.8, 10.3] | 5 .. 13 |
| l_width_jitter | 0.208 [0.0751, 0.308] | 0 .. 0.35 |
| l_para_lines | 3.44 [0, 9.54] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.699 [0.625, 0.756] | 0.1 .. 1 |
| l_final_forms_k | 2 [1.75, 2] | 0 .. 4 |
| l_initial_forms_share | 0.378 [0.312, 0.446] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1.75, 3] | 0 .. 4 |
| l_line_initial_p | 0.203 [0, 0.44] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0.3 [0, 0.552] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100


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

### verbose: taze medyan mesafe 3.50, en iyi 2.37

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +6.6 | 1.469 | 1.876 |
| char_double_rate | +5.6 | 0.015 | 0.045 |
| type_len_mean | +5.6 | 4.440 | 5.115 |
| jsd_last | -4.0 | 0.679 | 0.474 |
| wlen_autocorr1 | -3.5 | 0.179 | -0.031 |
| rep_adjacent_ed1 | -3.4 | 0.043 | 0.019 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.8 [8.73, 12.2] | 5 .. 13 |
| l_width_jitter | 0.14 [0.0555, 0.229] | 0 .. 0.35 |
| l_para_lines | 0 [0, 8.79] | 3 .. 15 |
| l_allo_per_glyph | 2.31 [1.52, 2.86] | 0.2 .. 3 |
| l_allo_rate | 0.0819 [0.068, 0.103] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0.456] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 3] | 0 .. 4 |
| l_line_initial_p | 0.181 [0, 0.494] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.293] | 0.1 .. 0.9 |
| l_para_initial_p | 0.163 [0, 0.627] | 0.3 .. 1 |
| p_alphabet | 16 [14, 18] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Croatian 54, Romanian 27, Italian 13, Turkish 3, Czech 1

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

### slotcite: taze medyan mesafe 3.81, en iyi 1.77

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +8.8 | 0.015 | 0.063 |
| rep_adjacent_exact | +2.4 | 0.006 | 0.012 |
| hapax_ratio | -2.4 | 0.741 | 0.672 |
| wlen_autocorr1 | -2.3 | 0.179 | 0.040 |
| vocab_ed1_density | +2.2 | 0.854 | 0.904 |
| jsd_line_final | -2.2 | 0.133 | 0.040 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.8 [8.68, 11.6] | 5 .. 13 |
| l_width_jitter | 0.182 [0.0726, 0.301] | 0 .. 0.35 |
| l_para_lines | 3.51 [0, 8.48] | 3 .. 15 |
| l_allo_per_glyph | 1.91 [1.32, 2.36] | 0.2 .. 3 |
| l_allo_rate | 0.083 [0.0435, 0.103] | 0.01 .. 0.15 |
| l_final_forms_share | 0.558 [0.366, 0.708] | 0.1 .. 1 |
| l_final_forms_k | 2.5 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.343 [0, 0.68] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.318] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.638] | 0.3 .. 1 |
| p_alphabet | 20 [18, 24] | 15 .. 25 |
| p_slot_overlap | 0.693 [0.467, 0.868] | 0 .. 1 |
| p_n_edge | 19 [12.8, 27] | 5 .. 40 |
| p_n_mid | 50 [22, 87.5] | 10 .. 120 |
| p_empty | 0.373 [0.31, 0.464] | 0 .. 0.6 |
| p_len_edge | 2 [2, 2] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_copy | 0.746 [0.612, 0.876] | 0.5 .. 0.97 |
| p_exact | 0.201 [0.139, 0.301] | 0.1 .. 0.7 |
| p_reach | 11 [6.75, 18.2] | 1 .. 30 |
| p_same_line | 0.0642 [0.0048, 0.131] | 0 .. 0.5 |
| p_mut_prefix | 0.321 [0.195, 0.484] | 0 .. 1 |
| p_mut_mid | 0.433 [0.233, 0.568] | 0 .. 1 |
| p_mut_suffix | 0.244 [0.104, 0.482] | 0 .. 1 |


## zl_basic: sınıf sınıf

### slotcite: taze medyan mesafe 3.00, en iyi 1.78

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| h2_over_h1 | +3.4 | 0.521 | 0.634 |
| h2 | +3.2 | 2.013 | 2.462 |
| hapax_ratio | -2.7 | 0.715 | 0.627 |
| jsd_line_final | -2.4 | 0.110 | 0.018 |
| zipf_slope | +2.3 | -0.785 | -0.626 |
| vocab_ed1_density | +2.0 | 0.823 | 0.866 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.17 [6.12, 11.2] | 5 .. 13 |
| l_width_jitter | 0.209 [0.101, 0.276] | 0 .. 0.35 |
| l_para_lines | 0 [0, 8.68] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.22] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.546 [0.368, 0.686] | 0.1 .. 1 |
| l_final_forms_k | 2.5 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.485 [0.1, 0.756] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.228] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.604] | 0.3 .. 1 |
| p_alphabet | 18 [16, 20] | 15 .. 25 |
| p_slot_overlap | 0.543 [0.265, 0.874] | 0 .. 1 |
| p_n_edge | 21 [15.8, 31] | 5 .. 40 |
| p_n_mid | 41 [25, 71] | 10 .. 120 |
| p_empty | 0.299 [0.232, 0.345] | 0 .. 0.6 |
| p_len_edge | 3 [3, 3] | 1 .. 3 |
| p_len_mid | 3 [2.75, 4] | 2 .. 5 |
| p_copy | 0.643 [0.555, 0.751] | 0.5 .. 0.97 |
| p_exact | 0.18 [0.105, 0.27] | 0.1 .. 0.7 |
| p_reach | 14 [6, 22.2] | 1 .. 30 |
| p_same_line | 0.0872 [0.0158, 0.158] | 0 .. 0.5 |
| p_mut_prefix | 0.332 [0.195, 0.465] | 0 .. 1 |
| p_mut_mid | 0.429 [0.203, 0.633] | 0 .. 1 |
| p_mut_suffix | 0.303 [0.118, 0.435] | 0 .. 1 |

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

### verbose: taze medyan mesafe 3.56, en iyi 2.24

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +6.7 | 0.097 | 0.186 |
| hapax_ratio | -5.7 | 0.715 | 0.533 |
| wlen_skew | +4.8 | 0.025 | 0.510 |
| first_entropy_ratio | +4.3 | 0.817 | 0.889 |
| wlen_frac1 | +3.7 | 0.033 | 0.071 |
| wlen_std | +3.5 | 1.768 | 1.982 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.82 [6.19, 11] | 5 .. 13 |
| l_width_jitter | 0.192 [0.122, 0.298] | 0 .. 0.35 |
| l_para_lines | 3.93 [0, 9.41] | 3 .. 15 |
| l_allo_per_glyph | 0.535 [0, 1.7] | 0.2 .. 3 |
| l_allo_rate | 0.0179 [0, 0.064] | 0.01 .. 0.15 |
| l_final_forms_share | 0.376 [0.113, 0.595] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 2.25] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.142] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2.25] | 0 .. 4 |
| l_line_initial_p | 0.397 [0, 0.671] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.266] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.663] | 0.3 .. 1 |
| p_alphabet | 15 [13, 19] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0.132] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 54, Polish 12, Romanian 11, Czech 10, Croatian 8

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

### slotcite: taze medyan mesafe 2.60, en iyi 1.42

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| jsd_line_final | -2.5 | 0.110 | 0.017 |
| hapax_ratio | -2.3 | 0.715 | 0.641 |
| h2_over_h1 | +2.2 | 0.554 | 0.643 |
| vocab_ed1_density | +2.1 | 0.852 | 0.886 |
| h2 | +2.1 | 2.127 | 2.492 |
| n_symbols | -2.1 | 44.750 | 25.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.35 [7.09, 12.6] | 5 .. 13 |
| l_width_jitter | 0.153 [0.0682, 0.26] | 0 .. 0.35 |
| l_para_lines | 4.24 [0, 11] | 3 .. 15 |
| l_allo_per_glyph | 0.815 [0, 1.59] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0832] | 0.01 .. 0.15 |
| l_final_forms_share | 0.522 [0.355, 0.651] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.592 [0.352, 0.699] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.155] | 0.1 .. 0.9 |
| l_para_initial_p | 0.365 [0, 0.806] | 0.3 .. 1 |
| p_alphabet | 18 [16, 21] | 15 .. 25 |
| p_slot_overlap | 0.278 [0.112, 0.507] | 0 .. 1 |
| p_n_edge | 25 [16.8, 32.2] | 5 .. 40 |
| p_n_mid | 39 [17.8, 84] | 10 .. 120 |
| p_empty | 0.352 [0.317, 0.432] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 4 [2.75, 4] | 2 .. 5 |
| p_copy | 0.602 [0.527, 0.691] | 0.5 .. 0.97 |
| p_exact | 0.154 [0.103, 0.222] | 0.1 .. 0.7 |
| p_reach | 7 [4, 19.2] | 1 .. 30 |
| p_same_line | 0.101 [0.0511, 0.209] | 0 .. 0.5 |
| p_mut_prefix | 0.343 [0.17, 0.522] | 0 .. 1 |
| p_mut_mid | 0.421 [0.156, 0.656] | 0 .. 1 |
| p_mut_suffix | 0.323 [0.159, 0.465] | 0 .. 1 |

### verbose: taze medyan mesafe 2.77, en iyi 1.56

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +5.4 | 1.615 | 1.916 |
| wlen_skew | +4.3 | 0.154 | 0.590 |
| wlen_frac1 | +3.4 | 0.033 | 0.070 |
| wlen_autocorr1 | -3.0 | 0.102 | -0.019 |
| jsd_first | -2.4 | 0.351 | 0.239 |
| jsd_line_final | -2.3 | 0.110 | 0.022 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.38 [5.46, 9.02] | 5 .. 13 |
| l_width_jitter | 0.129 [0.038, 0.219] | 0 .. 0.35 |
| l_para_lines | 0 [0, 9.48] | 3 .. 15 |
| l_allo_per_glyph | 2.36 [1.74, 2.75] | 0.2 .. 3 |
| l_allo_rate | 0.0539 [0.0401, 0.0634] | 0.01 .. 0.15 |
| l_final_forms_share | 0.494 [0.387, 0.583] | 0.1 .. 1 |
| l_final_forms_k | 1 [0.75, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.217 [0, 0.481] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.349] | 0.1 .. 0.9 |
| l_para_initial_p | 0.15 [0, 0.455] | 0.3 .. 1 |
| p_alphabet | 13 [12, 14] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Romanian 63, Italian 17, Turkish 7, Croatian 6, Russian 4

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
