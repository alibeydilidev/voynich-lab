# Yönlendirilmiş arama raporu: her hipotezin ulaşabildiği en iyi nokta

Her (sınıf, görünüm) için 5 tur, tur başına 600 deneme, en yakın 100 ayar tutuldu. Tablolardaki mesafeler, son turda kalan ayarların her biriyle yeniden üretilen 2 taze örnekten hesaplandı (toplam 200).

Mesafe birimi ve ölçüt `abc.md` ile aynı: bir hipotezin taze örnekleri Voynich öz mesafesinin içine giriyorsa, o hipotez bu feature kümesinde Voynich'ten ayırt edilemez.

## 1. Taze örneklerin medyan mesafesi (parantezde rejection ABC'deki değer)

| görünüm | Voynich öz mesafesi (medyan, en çok) | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.91, 1.65 | 5.84 (6.19) | 3.17 (2.77) | 4.15 (5.35) | 3.76 (4.46) | 3.29 (3.10) | 3.80 (3.26) | 4.08 (3.99) |
| eva_glyph | 0.96, 1.64 | 3.64 (3.96) | 2.81 (2.49) | 3.04 (4.20) | 2.83 (3.57) | 2.85 (2.82) | 3.34 (2.94) | 3.33 (3.57) |
| v101 | 0.97, 1.42 | 2.96 (3.36) | 3.39 (2.53) | 2.63 (3.02) | 3.17 (3.90) | 3.54 (2.95) | 3.47 (2.84) | 3.31 (3.27) |
| zl_basic | 0.96, 1.52 | 4.99 (5.36) | 2.98 (2.44) | 3.67 (4.71) | 3.36 (3.96) | 3.17 (2.73) | 3.40 (2.94) | 3.52 (3.26) |
| zl_glyph | 1.03, 1.43 | 3.17 (3.54) | 2.46 (2.15) | 2.98 (3.76) | 2.64 (3.12) | 2.54 (2.43) | 2.65 (2.51) | 2.72 (2.89) |

## 2. Voynich'in en uç penceresi kadar yakın olan taze örneklerin oranı

| görünüm | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|
| eva_basic | %0 | %0 | %0 | %0 | %0 | %0 | %0 |
| eva_glyph | %0 | %0 | %0 | %0 | %0 | %0 | %0 |
| v101 | %0 | %0 | %0 | %0 | %0 | %0 | %0 |
| zl_basic | %0 | %0 | %0 | %0 | %0 | %0 | %0 |
| zl_glyph | %0 | %0 | %0 | %0 | %0 | %0 | %0 |

## 3. Arama yakınsadı mı (tur tur, tutulan ayarların medyan mesafesi)

| görünüm | sınıf | turlar |
|---|---|---|
| eva_basic | abjad | 5.97 -> 5.74 -> 5.59 -> 5.43 -> 5.34 |
| eva_basic | grille | 2.89 -> 2.75 -> 2.70 -> 2.56 -> 2.60 |
| eva_basic | plain | 4.75 -> 4.14 -> 3.93 -> 3.93 -> 3.86 |
| eva_basic | selfcite | 4.17 -> 3.88 -> 3.73 -> 3.44 -> 3.36 |
| eva_basic | slotcite | 3.14 -> 2.98 -> 2.93 -> 2.78 -> 2.70 |
| eva_basic | slotgram | 3.52 -> 3.29 -> 3.13 -> 3.22 -> 3.08 |
| eva_basic | verbose | 3.91 -> 3.64 -> 3.61 -> 3.51 -> 3.54 |
| eva_glyph | abjad | 3.71 -> 3.53 -> 3.44 -> 3.40 -> 3.36 |
| eva_glyph | grille | 2.59 -> 2.43 -> 2.45 -> 2.33 -> 2.24 |
| eva_glyph | plain | 3.65 -> 3.16 -> 2.94 -> 2.79 -> 2.79 |
| eva_glyph | selfcite | 3.19 -> 2.97 -> 2.79 -> 2.69 -> 2.62 |
| eva_glyph | slotcite | 2.84 -> 2.72 -> 2.66 -> 2.50 -> 2.42 |
| eva_glyph | slotgram | 3.02 -> 2.95 -> 2.94 -> 2.87 -> 2.80 |
| eva_glyph | verbose | 3.45 -> 3.36 -> 3.20 -> 3.05 -> 2.93 |
| v101 | abjad | 3.01 -> 2.84 -> 2.71 -> 2.68 -> 2.61 |
| v101 | grille | 2.94 -> 2.95 -> 2.90 -> 2.68 -> 2.76 |
| v101 | plain | 2.70 -> 2.46 -> 2.40 -> 2.40 -> 2.36 |
| v101 | selfcite | 3.58 -> 3.27 -> 3.12 -> 2.87 -> 2.79 |
| v101 | slotcite | 3.29 -> 3.19 -> 2.97 -> 2.90 -> 2.93 |
| v101 | slotgram | 3.19 -> 3.15 -> 2.99 -> 2.85 -> 2.85 |
| v101 | verbose | 3.15 -> 3.04 -> 2.84 -> 2.80 -> 2.70 |
| zl_basic | abjad | 5.20 -> 5.00 -> 4.70 -> 4.59 -> 4.50 |
| zl_basic | grille | 2.66 -> 2.42 -> 2.46 -> 2.40 -> 2.41 |
| zl_basic | plain | 4.06 -> 3.68 -> 3.56 -> 3.52 -> 3.48 |
| zl_basic | selfcite | 3.66 -> 3.40 -> 3.20 -> 3.13 -> 3.05 |
| zl_basic | slotcite | 2.79 -> 2.69 -> 2.69 -> 2.64 -> 2.59 |
| zl_basic | slotgram | 3.05 -> 2.97 -> 2.84 -> 2.85 -> 2.78 |
| zl_basic | verbose | 3.20 -> 3.18 -> 3.00 -> 2.99 -> 2.90 |
| zl_glyph | abjad | 3.29 -> 3.13 -> 3.04 -> 2.92 -> 2.87 |
| zl_glyph | grille | 2.28 -> 2.21 -> 2.12 -> 2.08 -> 1.96 |
| zl_glyph | plain | 3.22 -> 2.91 -> 2.80 -> 2.77 -> 2.76 |
| zl_glyph | selfcite | 2.91 -> 2.72 -> 2.56 -> 2.43 -> 2.38 |
| zl_glyph | slotcite | 2.55 -> 2.42 -> 2.26 -> 2.23 -> 2.09 |
| zl_glyph | slotgram | 2.67 -> 2.55 -> 2.34 -> 2.27 -> 2.22 |
| zl_glyph | verbose | 2.78 -> 2.61 -> 2.54 -> 2.42 -> 2.37 |

## eva_basic: sınıf sınıf

### grille: taze medyan mesafe 3.17, en iyi 1.78

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -3.5 | 0.127 | -0.006 |
| h2_over_h1 | +3.3 | 0.524 | 0.626 |
| h2 | +2.9 | 2.016 | 2.371 |
| jsd_line_final | -2.9 | 0.109 | 0.017 |
| hapax_ratio | -2.6 | 0.717 | 0.659 |
| rep_adjacent_ed1 | -2.5 | 0.032 | 0.016 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.13 [6.38, 11.5] | 5 .. 13 |
| l_width_jitter | 0.147 [0.0775, 0.231] | 0 .. 0.35 |
| l_para_lines | 5.59 [0, 11.9] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.645 [0.474, 0.76] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1.25] | 0 .. 4 |
| l_line_initial_p | 0.191 [0, 0.447] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.214] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.488] | 0.3 .. 1 |
| p_alphabet | 19 [17, 21] | 15 .. 25 |
| p_rows | 1.14e+03 [720, 2.18e+03] | 60 .. 3000 |
| p_slot_overlap | 0.572 [0.355, 0.869] | 0 .. 1 |
| p_n_edge | 22 [15, 30.2] | 5 .. 40 |
| p_n_mid | 39.5 [25, 75] | 10 .. 120 |
| p_empty | 0.247 [0.182, 0.313] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_n_grilles | 6 [4, 7] | 3 .. 8 |

### slotcite: taze medyan mesafe 3.29, en iyi 1.76

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -5.6 | 0.717 | 0.592 |
| h2_over_h1 | +3.7 | 0.524 | 0.639 |
| h2 | +3.5 | 2.016 | 2.437 |
| zipf_slope | +2.9 | -0.778 | -0.594 |
| jsd_line_final | -2.7 | 0.109 | 0.022 |
| wlen_autocorr1 | -2.3 | 0.127 | 0.039 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.45 [8.01, 11.1] | 5 .. 13 |
| l_width_jitter | 0.169 [0.0564, 0.266] | 0 .. 0.35 |
| l_para_lines | 0 [0, 5.53] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.553 [0.381, 0.72] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.466 [0.075, 0.677] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.269] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.762] | 0.3 .. 1 |
| p_alphabet | 18 [16, 20] | 15 .. 25 |
| p_slot_overlap | 0.641 [0.378, 0.867] | 0 .. 1 |
| p_n_edge | 25 [19, 33] | 5 .. 40 |
| p_n_mid | 30 [14, 74.8] | 10 .. 120 |
| p_empty | 0.257 [0.206, 0.318] | 0 .. 0.6 |
| p_len_edge | 3 [3, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_copy | 0.638 [0.549, 0.774] | 0.5 .. 0.97 |
| p_exact | 0.224 [0.131, 0.35] | 0.1 .. 0.7 |
| p_reach | 14 [6, 22.2] | 1 .. 30 |
| p_same_line | 0.073 [0.0086, 0.168] | 0 .. 0.5 |
| p_mut_prefix | 0.26 [0.114, 0.412] | 0 .. 1 |
| p_mut_mid | 0.489 [0.318, 0.663] | 0 .. 1 |
| p_mut_suffix | 0.231 [0.119, 0.38] | 0 .. 1 |

### selfcite: taze medyan mesafe 3.76, en iyi 2.65

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -6.0 | 0.717 | 0.583 |
| h2 | +5.8 | 2.016 | 2.715 |
| h2_over_h1 | +5.7 | 0.524 | 0.702 |
| first_entropy_ratio | +5.2 | 0.806 | 0.899 |
| char_double_rate | +5.0 | 0.067 | 0.135 |
| vocab_ed1_density | +4.7 | 0.823 | 0.940 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.7 [8.95, 12.2] | 5 .. 13 |
| l_width_jitter | 0.199 [0.151, 0.261] | 0 .. 0.35 |
| l_para_lines | 4.91 [0, 9.84] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.739 [0.647, 0.85] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.206] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.449 [0.162, 0.677] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.278] | 0.1 .. 0.9 |
| l_para_initial_p | 0.333 [0, 0.625] | 0.3 .. 1 |
| p_alphabet | 17 [15, 18] | 15 .. 25 |
| p_glyph_classes | 5 [5, 6] | 4 .. 7 |
| p_copy | 0.885 [0.865, 0.903] | 0.85 .. 0.97 |
| p_exact | 0.371 [0.266, 0.484] | 0.2 .. 0.8 |
| p_reach | 21.5 [15, 26] | 1 .. 30 |
| p_same_line | 0.0451 [0.0163, 0.0712] | 0 .. 0.3 |
| p_slot_overlap | 0.308 [0.139, 0.467] | 0 .. 1 |
| p_affix | 0.777 [0.695, 0.86] | 0.3 .. 0.9 |
| p_mut_substitute | 0.532 [0.279, 0.709] | 0 .. 1 |
| p_mut_prefix | 0.44 [0.314, 0.539] | 0 .. 1 |
| p_mut_delete | 0.0662 [0, 0.126] | 0 .. 1 |
| p_mut_double | 0.14 [0.0859, 0.228] | 0 .. 1 |

### slotgram: taze medyan mesafe 3.80, en iyi 2.22

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| zipf_slope | +3.7 | -0.778 | -0.547 |
| h1 | -3.3 | 3.845 | 3.768 |
| jsd_line_final | -3.1 | 0.109 | 0.009 |
| wlen_autocorr1 | -3.1 | 0.127 | 0.009 |
| wlen_std | +2.7 | 1.693 | 1.893 |
| vocab_ed1_density | +2.6 | 0.823 | 0.888 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.2 [7.69, 12] | 5 .. 13 |
| l_width_jitter | 0.178 [0.0923, 0.289] | 0 .. 0.35 |
| l_para_lines | 5.86 [0, 10.8] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.057] | 0.01 .. 0.15 |
| l_final_forms_share | 0.591 [0.426, 0.715] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.532] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.185] | 0.1 .. 0.9 |
| l_para_initial_p | 0.415 [0, 0.735] | 0.3 .. 1 |
| p_alphabet | 20 [17, 22] | 15 .. 25 |
| p_n_slots | 6 [5, 7] | 3 .. 8 |
| p_slot_overlap | 0.401 [0.189, 0.624] | 0 .. 1 |
| p_n_inv | 5 [3, 9] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.459 [0.352, 0.525] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0.394] | 0.3 .. 0.95 |
| p_exact | 0.264 [0.145, 0.398] | 0 .. 0.5 |
| p_reach | 8 [2.75, 16.2] | 1 .. 30 |
| p_same_line | 0.199 [0.0863, 0.365] | 0 .. 0.5 |

### verbose: taze medyan mesafe 4.08, en iyi 2.71

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -8.8 | 0.717 | 0.523 |
| wlen_frac_le2 | +8.5 | 0.077 | 0.175 |
| wlen_frac1 | +4.8 | 0.017 | 0.070 |
| wlen_autocorr1 | -4.2 | 0.127 | -0.034 |
| wlen_skew | +4.1 | 0.074 | 0.609 |
| first_entropy_ratio | +3.9 | 0.806 | 0.876 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.15 [5.99, 10.7] | 5 .. 13 |
| l_width_jitter | 0.195 [0.0603, 0.303] | 0 .. 0.35 |
| l_para_lines | 6.69 [0, 12.9] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.552] | 0.2 .. 3 |
| l_allo_rate | 0.0614 [0, 0.105] | 0.01 .. 0.15 |
| l_final_forms_share | 0.549 [0.243, 0.698] | 0.1 .. 1 |
| l_final_forms_k | 3 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0.109 [0, 0.307] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.451 [0.293, 0.589] | 0.1 .. 0.9 |
| l_line_final_p | 0.227 [0, 0.415] | 0.1 .. 0.9 |
| l_para_initial_p | 0.3 [0, 0.618] | 0.3 .. 1 |
| p_alphabet | 13 [12, 15] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Czech 32, Italian 28, Croatian 15, Romanian 9, Polish 7

### plain: taze medyan mesafe 4.15, en iyi 3.58

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -8.0 | 0.628 | 0.140 |
| first_entropy_ratio | +7.4 | 0.806 | 0.938 |
| type_len_mean | -6.6 | 5.692 | 4.561 |
| h2 | +6.6 | 2.016 | 2.808 |
| wlen_frac_le2 | +6.5 | 0.077 | 0.152 |
| h2_over_h1 | +6.3 | 0.524 | 0.719 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.5 [7.84, 12.5] | 5 .. 13 |
| l_width_jitter | 0.222 [0.105, 0.298] | 0 .. 0.35 |
| l_para_lines | 0 [0, 7.14] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.905 [0.822, 0.976] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0.5 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_line_final_p | 0.1 [0, 0.213] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.516] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 82, Arabic 18

### abjad: taze medyan mesafe 5.84, en iyi 4.42

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +22.3 | 0.077 | 0.335 |
| wlen_frac1 | +8.6 | 0.017 | 0.114 |
| wlen_mean | -7.3 | 5.066 | 3.386 |
| type_len_mean | -7.2 | 5.692 | 4.459 |
| h2_over_h1 | +5.6 | 0.524 | 0.698 |
| h2 | +5.6 | 2.016 | 2.690 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.39 [5, 7.81] | 5 .. 13 |
| l_width_jitter | 0.124 [0.0323, 0.192] | 0 .. 0.35 |
| l_para_lines | 3 [0, 6.76] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.658 [0.556, 0.762] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.497 [0.404, 0.584] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 3] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.503] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0.305 [0, 0.623] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100


## eva_glyph: sınıf sınıf

### grille: taze medyan mesafe 2.81, en iyi 1.53

Voynich'ten 2 birimden fazla sapan feature sayısı: 3

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -3.2 | 0.103 | -0.005 |
| hapax_ratio | -2.5 | 0.717 | 0.662 |
| h2_over_h1 | +2.0 | 0.556 | 0.631 |
| vocab_ed1_density | +2.0 | 0.850 | 0.894 |
| h2 | +1.9 | 2.131 | 2.434 |
| rep_within3 | -1.8 | 0.026 | 0.013 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.25 [6.43, 11.4] | 5 .. 13 |
| l_width_jitter | 0.208 [0.0934, 0.298] | 0 .. 0.35 |
| l_para_lines | 4.77 [0, 8.03] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.62 [0.479, 0.779] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.367 [0, 0.612] | 0.1 .. 0.9 |
| l_line_final_p | 0.191 [0, 0.358] | 0.1 .. 0.9 |
| l_para_initial_p | 0.315 [0, 0.6] | 0.3 .. 1 |
| p_alphabet | 20 [18, 22] | 15 .. 25 |
| p_rows | 1.26e+03 [690, 2.07e+03] | 60 .. 3000 |
| p_slot_overlap | 0.568 [0.422, 0.74] | 0 .. 1 |
| p_n_edge | 30.5 [23, 35.2] | 5 .. 40 |
| p_n_mid | 33 [15, 60.5] | 10 .. 120 |
| p_empty | 0.337 [0.278, 0.406] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2.75, 4] | 2 .. 5 |
| p_n_grilles | 6 [5, 7] | 3 .. 8 |

### selfcite: taze medyan mesafe 2.83, en iyi 2.17

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -6.2 | 0.717 | 0.579 |
| h2_over_h1 | +4.3 | 0.556 | 0.718 |
| h2 | +4.2 | 2.131 | 2.781 |
| vocab_ed1_density | +3.9 | 0.850 | 0.936 |
| n_symbols | -3.4 | 25.250 | 21.000 |
| zipf_slope | +2.8 | -0.778 | -0.603 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.91 [9, 11.2] | 5 .. 13 |
| l_width_jitter | 0.131 [0.0303, 0.256] | 0 .. 0.35 |
| l_para_lines | 7.27 [0, 9.48] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.705] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.685 [0.596, 0.759] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.605] | 0.1 .. 0.9 |
| l_line_final_p | 0.1 [0, 0.242] | 0.1 .. 0.9 |
| l_para_initial_p | 0.15 [0, 0.594] | 0.3 .. 1 |
| p_alphabet | 18 [16, 20] | 15 .. 25 |
| p_glyph_classes | 6 [5, 7] | 4 .. 7 |
| p_copy | 0.869 [0.85, 0.897] | 0.85 .. 0.97 |
| p_exact | 0.307 [0.244, 0.448] | 0.2 .. 0.8 |
| p_reach | 19 [16, 23] | 1 .. 30 |
| p_same_line | 0.0218 [0.0037, 0.0437] | 0 .. 0.3 |
| p_slot_overlap | 0.297 [0.0847, 0.64] | 0 .. 1 |
| p_affix | 0.78 [0.682, 0.856] | 0.3 .. 0.9 |
| p_mut_substitute | 0.411 [0.191, 0.637] | 0 .. 1 |
| p_mut_prefix | 0.597 [0.417, 0.718] | 0 .. 1 |
| p_mut_delete | 0.0524 [0.0148, 0.114] | 0 .. 1 |
| p_mut_double | 0.0671 [0.0392, 0.118] | 0 .. 1 |

### slotcite: taze medyan mesafe 2.85, en iyi 1.83

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -3.7 | 0.717 | 0.636 |
| zipf_slope | +2.9 | -0.778 | -0.593 |
| jsd_line_final | -2.9 | 0.110 | 0.018 |
| h2_over_h1 | +2.7 | 0.556 | 0.658 |
| n_symbols | -2.6 | 25.250 | 22.000 |
| h2 | +2.5 | 2.131 | 2.523 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.57 [6.09, 9.74] | 5 .. 13 |
| l_width_jitter | 0.158 [0.0695, 0.253] | 0 .. 0.35 |
| l_para_lines | 5.14 [0, 9.62] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0.0668 [0, 0.124] | 0.01 .. 0.15 |
| l_final_forms_share | 0.587 [0.407, 0.712] | 0.1 .. 1 |
| l_final_forms_k | 3 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.635 [0.463, 0.795] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.276] | 0.1 .. 0.9 |
| l_para_initial_p | 0.486 [0, 0.77] | 0.3 .. 1 |
| p_alphabet | 18 [16, 21] | 15 .. 25 |
| p_slot_overlap | 0.723 [0.414, 0.913] | 0 .. 1 |
| p_n_edge | 27 [20.8, 33.2] | 5 .. 40 |
| p_n_mid | 48 [30.8, 85.8] | 10 .. 120 |
| p_empty | 0.253 [0.206, 0.294] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_copy | 0.577 [0.505, 0.658] | 0.5 .. 0.97 |
| p_exact | 0.307 [0.173, 0.401] | 0.1 .. 0.7 |
| p_reach | 17 [8, 27] | 1 .. 30 |
| p_same_line | 0.0506 [0.0143, 0.133] | 0 .. 0.5 |
| p_mut_prefix | 0.34 [0.227, 0.493] | 0 .. 1 |
| p_mut_mid | 0.297 [0.0777, 0.542] | 0 .. 1 |
| p_mut_suffix | 0.396 [0.223, 0.555] | 0 .. 1 |

### plain: taze medyan mesafe 3.04, en iyi 2.52

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -6.6 | 0.626 | 0.245 |
| h2 | +4.6 | 2.131 | 2.853 |
| h2_over_h1 | +4.6 | 0.556 | 0.729 |
| char_double_rate | -4.6 | 0.076 | 0.009 |
| wlen_std | -4.5 | 1.552 | 1.316 |
| eff_symbols | +3.5 | 14.404 | 16.034 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.9 [7.64, 12.5] | 5 .. 13 |
| l_width_jitter | 0.192 [0.0437, 0.321] | 0 .. 0.35 |
| l_para_lines | 5.15 [0, 9.65] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.856 [0.757, 0.925] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.31] | 0.1 .. 0.9 |
| l_line_final_p | 0.185 [0, 0.286] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.351] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### verbose: taze medyan mesafe 3.33, en iyi 2.41

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +6.2 | 1.552 | 1.877 |
| hapax_ratio | -5.3 | 0.717 | 0.599 |
| wlen_skew | +4.3 | 0.183 | 0.643 |
| wlen_autocorr1 | -4.0 | 0.103 | -0.031 |
| wlen_frac1 | +3.8 | 0.017 | 0.062 |
| ttr | -3.1 | 0.443 | 0.275 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.76 [6.23, 9.41] | 5 .. 13 |
| l_width_jitter | 0.189 [0.0932, 0.273] | 0 .. 0.35 |
| l_para_lines | 6.73 [3, 11.1] | 3 .. 15 |
| l_allo_per_glyph | 0.791 [0.498, 1.04] | 0.2 .. 3 |
| l_allo_rate | 0.0688 [0.0426, 0.107] | 0.01 .. 0.15 |
| l_final_forms_share | 0.409 [0, 0.547] | 0.1 .. 1 |
| l_final_forms_k | 2.5 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.123] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.372 [0.23, 0.507] | 0.1 .. 0.9 |
| l_line_final_p | 0.245 [0, 0.355] | 0.1 .. 0.9 |
| l_para_initial_p | 0.412 [0, 0.633] | 0.3 .. 1 |
| p_alphabet | 13 [12, 14] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Croatian 47, Romanian 25, Italian 16, Turkish 11, Hungarian 1

### slotgram: taze medyan mesafe 3.34, en iyi 1.92

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| n_symbols | -3.4 | 25.250 | 21.000 |
| first_entropy_ratio | -2.9 | 0.867 | 0.803 |
| zipf_slope | +2.8 | -0.778 | -0.603 |
| wlen_autocorr1 | -2.7 | 0.103 | 0.015 |
| vocab_ed1_density | +2.1 | 0.850 | 0.896 |
| h2_over_h1 | +2.0 | 0.556 | 0.631 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.61 [7.04, 10.7] | 5 .. 13 |
| l_width_jitter | 0.22 [0.121, 0.299] | 0 .. 0.35 |
| l_para_lines | 3.08 [0, 10.2] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.2] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0476] | 0.01 .. 0.15 |
| l_final_forms_share | 0.525 [0.334, 0.668] | 0.1 .. 1 |
| l_final_forms_k | 2 [0, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0.5 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.189 [0, 0.622] | 0.1 .. 0.9 |
| l_line_final_p | 0.115 [0, 0.277] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.531] | 0.3 .. 1 |
| p_alphabet | 20 [17, 22] | 15 .. 25 |
| p_n_slots | 5 [4, 5] | 3 .. 8 |
| p_slot_overlap | 0.544 [0.262, 0.793] | 0 .. 1 |
| p_n_inv | 8 [5, 16] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.388 [0.273, 0.482] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0.367] | 0.3 .. 0.95 |
| p_exact | 0.223 [0.0823, 0.361] | 0 .. 0.5 |
| p_reach | 12.5 [3, 22.2] | 1 .. 30 |
| p_same_line | 0.241 [0.118, 0.367] | 0 .. 0.5 |

### abjad: taze medyan mesafe 3.64, en iyi 2.83

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +8.2 | 0.017 | 0.113 |
| wlen_frac_le2 | +7.5 | 0.099 | 0.335 |
| first_entropy_ratio | +6.4 | 0.867 | 1.009 |
| h2_over_h1 | +4.7 | 0.556 | 0.732 |
| wlen_skew | +4.6 | 0.183 | 0.673 |
| h2 | +4.5 | 2.131 | 2.834 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.84 [6.02, 11.1] | 5 .. 13 |
| l_width_jitter | 0.188 [0.0562, 0.323] | 0 .. 0.35 |
| l_para_lines | 8.86 [0, 12.5] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.705 [0.624, 0.817] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.286] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.356] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.312] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.572] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 99, Finnish 1


## v101: sınıf sınıf

### plain: taze medyan mesafe 2.63, en iyi 2.14

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| vocab_ed1_density | -4.8 | 0.854 | 0.742 |
| n_symbols | -4.6 | 69.529 | 26.000 |
| wlen_frac1 | -4.5 | 0.046 | 0.000 |
| h2 | +4.1 | 2.383 | 3.088 |
| h2_over_h1 | +3.9 | 0.595 | 0.758 |
| rep_adjacent_ed1 | -3.8 | 0.043 | 0.016 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.99 [5.96, 10.7] | 5 .. 13 |
| l_width_jitter | 0.236 [0.146, 0.316] | 0 .. 0.35 |
| l_para_lines | 6.02 [0, 11.6] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.00275] | 0.01 .. 0.15 |
| l_final_forms_share | 0.64 [0.565, 0.726] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.413] | 0.1 .. 0.9 |
| l_line_final_p | 0.245 [0, 0.344] | 0.1 .. 0.9 |
| l_para_initial_p | 0.377 [0, 0.683] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### abjad: taze medyan mesafe 2.96, en iyi 2.20

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +6.3 | 0.046 | 0.111 |
| wlen_frac_le2 | +5.6 | 0.184 | 0.332 |
| n_symbols | -4.6 | 69.529 | 26.000 |
| wlen_skew | +3.4 | 0.225 | 0.686 |
| h2_over_h1 | +3.3 | 0.595 | 0.733 |
| vocab_ed1_density | -3.3 | 0.854 | 0.777 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.63 [5.72, 9.63] | 5 .. 13 |
| l_width_jitter | 0.206 [0.143, 0.279] | 0 .. 0.35 |
| l_para_lines | 3.5 [0, 6.03] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.042] | 0.01 .. 0.15 |
| l_final_forms_share | 0.62 [0.55, 0.774] | 0.1 .. 1 |
| l_final_forms_k | 3 [3, 4] | 0 .. 4 |
| l_initial_forms_share | 0.311 [0.126, 0.397] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 3] | 0 .. 4 |
| l_line_initial_p | 0.519 [0.292, 0.656] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.286] | 0.1 .. 0.9 |
| l_para_initial_p | 0.512 [0.225, 0.692] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100

### selfcite: taze medyan mesafe 3.17, en iyi 2.13

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +7.7 | 0.015 | 0.057 |
| n_symbols | -4.7 | 69.529 | 25.000 |
| hapax_ratio | -4.0 | 0.741 | 0.624 |
| zipf_slope | +3.5 | -0.776 | -0.624 |
| h2_over_h1 | +3.2 | 0.595 | 0.728 |
| h2 | +3.2 | 2.383 | 2.924 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.86 [6.34, 9.51] | 5 .. 13 |
| l_width_jitter | 0.208 [0.0927, 0.305] | 0 .. 0.35 |
| l_para_lines | 5.55 [3, 9.33] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.51] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0767] | 0.01 .. 0.15 |
| l_final_forms_share | 0.745 [0.634, 0.836] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.328] | 0.1 .. 0.9 |
| l_line_final_p | 0.25 [0, 0.394] | 0.1 .. 0.9 |
| l_para_initial_p | 0.526 [0, 0.859] | 0.3 .. 1 |
| p_alphabet | 19 [18, 21] | 15 .. 25 |
| p_glyph_classes | 5 [5, 6] | 4 .. 7 |
| p_copy | 0.87 [0.857, 0.891] | 0.85 .. 0.97 |
| p_exact | 0.329 [0.243, 0.406] | 0.2 .. 0.8 |
| p_reach | 22 [18.8, 27] | 1 .. 30 |
| p_same_line | 0.0254 [0.00287, 0.0589] | 0 .. 0.3 |
| p_slot_overlap | 0.634 [0.393, 0.795] | 0 .. 1 |
| p_affix | 0.736 [0.629, 0.809] | 0.3 .. 0.9 |
| p_mut_substitute | 0.458 [0.294, 0.65] | 0 .. 1 |
| p_mut_prefix | 0.421 [0.297, 0.551] | 0 .. 1 |
| p_mut_delete | 0.205 [0.113, 0.305] | 0 .. 1 |
| p_mut_double | 0.00371 [0, 0.018] | 0 .. 1 |

### verbose: taze medyan mesafe 3.31, en iyi 2.16

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +6.5 | 1.469 | 1.867 |
| type_len_mean | +5.5 | 4.440 | 5.109 |
| char_double_rate | +5.1 | 0.015 | 0.043 |
| jsd_last | -3.9 | 0.679 | 0.478 |
| wlen_autocorr1 | -3.5 | 0.179 | -0.029 |
| rep_adjacent_ed1 | -3.4 | 0.043 | 0.019 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.92 [6.88, 10.9] | 5 .. 13 |
| l_width_jitter | 0.162 [0.0691, 0.241] | 0 .. 0.35 |
| l_para_lines | 0 [0, 3] | 3 .. 15 |
| l_allo_per_glyph | 2.27 [1.76, 2.74] | 0.2 .. 3 |
| l_allo_rate | 0.0931 [0.0722, 0.113] | 0.01 .. 0.15 |
| l_final_forms_share | 0.05 [0, 0.417] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.179 [0, 0.518] | 0.1 .. 0.9 |
| l_line_final_p | 0.209 [0, 0.416] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0] | 0.3 .. 1 |
| p_alphabet | 15 [13, 16] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Croatian 57, Romanian 34, Turkish 5, Italian 3, German 1

### grille: taze medyan mesafe 3.39, en iyi 1.69

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +6.5 | 0.015 | 0.050 |
| vocab_ed1_density | +3.2 | 0.854 | 0.928 |
| wlen_autocorr1 | -3.0 | 0.179 | 0.001 |
| hapax_ratio | -2.9 | 0.741 | 0.655 |
| n_symbols | -2.9 | 69.529 | 42.500 |
| jsd_line_final | -2.6 | 0.133 | 0.022 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.89 [6.46, 8.97] | 5 .. 13 |
| l_width_jitter | 0.179 [0.0745, 0.252] | 0 .. 0.35 |
| l_para_lines | 4.21 [0, 7.91] | 3 .. 15 |
| l_allo_per_glyph | 1.46 [0.938, 1.91] | 0.2 .. 3 |
| l_allo_rate | 0.0635 [0, 0.0929] | 0.01 .. 0.15 |
| l_final_forms_share | 0.513 [0.303, 0.766] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.422 [0, 0.729] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.297] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.778] | 0.3 .. 1 |
| p_alphabet | 22 [20, 24] | 15 .. 25 |
| p_rows | 978 [554, 1.58e+03] | 60 .. 3000 |
| p_slot_overlap | 0.796 [0.544, 0.935] | 0 .. 1 |
| p_n_edge | 24 [15, 33] | 5 .. 40 |
| p_n_mid | 39.5 [20, 54.2] | 10 .. 120 |
| p_empty | 0.391 [0.321, 0.474] | 0 .. 0.6 |
| p_len_edge | 2 [1, 2] | 1 .. 3 |
| p_len_mid | 3 [2.75, 4] | 2 .. 5 |
| p_n_grilles | 4 [3, 5] | 3 .. 8 |

### slotgram: taze medyan mesafe 3.47, en iyi 2.26

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| n_symbols | -4.5 | 69.529 | 27.000 |
| h1 | -3.1 | 4.005 | 3.899 |
| wlen_autocorr1 | -2.9 | 0.179 | 0.004 |
| char_double_rate | +2.9 | 0.015 | 0.031 |
| last_entropy_ratio | -2.8 | 0.704 | 0.529 |
| wlen_std | -2.5 | 1.469 | 1.314 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.39 [5.5, 10.5] | 5 .. 13 |
| l_width_jitter | 0.176 [0.0763, 0.271] | 0 .. 0.35 |
| l_para_lines | 7.92 [0, 10.8] | 3 .. 15 |
| l_allo_per_glyph | 0.735 [0, 1.77] | 0.2 .. 3 |
| l_allo_rate | 0.0597 [0, 0.114] | 0.01 .. 0.15 |
| l_final_forms_share | 0.795 [0.524, 0.925] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.158 [0, 0.537] | 0.1 .. 0.9 |
| l_line_final_p | 0.123 [0, 0.417] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.618] | 0.3 .. 1 |
| p_alphabet | 21 [18, 24] | 15 .. 25 |
| p_n_slots | 7 [4, 8] | 3 .. 8 |
| p_slot_overlap | 0.451 [0.172, 0.711] | 0 .. 1 |
| p_n_inv | 13 [6, 20.2] | 2 .. 30 |
| p_len_max | 1 [1, 2] | 1 .. 2 |
| p_empty | 0.5 [0.417, 0.559] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0] | 0.3 .. 0.95 |
| p_exact | 0.209 [0.15, 0.353] | 0 .. 0.5 |
| p_reach | 11 [4.75, 22] | 1 .. 30 |
| p_same_line | 0.247 [0.123, 0.354] | 0 .. 0.5 |

### slotcite: taze medyan mesafe 3.54, en iyi 1.87

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +7.9 | 0.015 | 0.058 |
| n_symbols | -3.9 | 69.529 | 32.500 |
| hapax_ratio | -2.7 | 0.741 | 0.661 |
| rep_adjacent_exact | +2.7 | 0.006 | 0.012 |
| vocab_ed1_density | +2.6 | 0.854 | 0.913 |
| wlen_autocorr1 | -2.4 | 0.179 | 0.034 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.85 [6.8, 11.8] | 5 .. 13 |
| l_width_jitter | 0.192 [0.0813, 0.279] | 0 .. 0.35 |
| l_para_lines | 9.18 [0, 11.4] | 3 .. 15 |
| l_allo_per_glyph | 0.558 [0, 1.8] | 0.2 .. 3 |
| l_allo_rate | 0.0604 [0, 0.104] | 0.01 .. 0.15 |
| l_final_forms_share | 0.438 [0.252, 0.599] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.434 [0.241, 0.685] | 0.1 .. 0.9 |
| l_line_final_p | 0.18 [0, 0.376] | 0.1 .. 0.9 |
| l_para_initial_p | 0.55 [0, 0.866] | 0.3 .. 1 |
| p_alphabet | 22 [20, 24] | 15 .. 25 |
| p_slot_overlap | 0.718 [0.547, 0.894] | 0 .. 1 |
| p_n_edge | 24.5 [17, 32.2] | 5 .. 40 |
| p_n_mid | 59 [24.8, 96.2] | 10 .. 120 |
| p_empty | 0.342 [0.294, 0.403] | 0 .. 0.6 |
| p_len_edge | 2 [2, 2] | 1 .. 3 |
| p_len_mid | 2 [2, 3] | 2 .. 5 |
| p_copy | 0.634 [0.555, 0.802] | 0.5 .. 0.97 |
| p_exact | 0.18 [0.106, 0.29] | 0.1 .. 0.7 |
| p_reach | 15 [8.75, 24] | 1 .. 30 |
| p_same_line | 0.0966 [0.00741, 0.183] | 0 .. 0.5 |
| p_mut_prefix | 0.228 [0.0916, 0.429] | 0 .. 1 |
| p_mut_mid | 0.417 [0.228, 0.574] | 0 .. 1 |
| p_mut_suffix | 0.314 [0.154, 0.433] | 0 .. 1 |


## zl_basic: sınıf sınıf

### grille: taze medyan mesafe 2.98, en iyi 1.53

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| h2_over_h1 | +3.0 | 0.521 | 0.621 |
| h2 | +2.7 | 2.013 | 2.393 |
| wlen_autocorr1 | -2.7 | 0.123 | -0.002 |
| rep_adjacent_ed1 | -2.5 | 0.034 | 0.016 |
| vocab_ed1_density | +2.5 | 0.823 | 0.877 |
| jsd_line_initial | -2.4 | 0.233 | 0.040 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.64 [5.57, 10.7] | 5 .. 13 |
| l_width_jitter | 0.181 [0.0564, 0.26] | 0 .. 0.35 |
| l_para_lines | 5.43 [0, 9.77] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.62] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.058] | 0.01 .. 0.15 |
| l_final_forms_share | 0.577 [0.419, 0.668] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.441] | 0.1 .. 0.9 |
| l_line_final_p | 0.108 [0, 0.292] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.604] | 0.3 .. 1 |
| p_alphabet | 19 [17, 23] | 15 .. 25 |
| p_rows | 1.41e+03 [848, 2.05e+03] | 60 .. 3000 |
| p_slot_overlap | 0.472 [0.207, 0.782] | 0 .. 1 |
| p_n_edge | 26 [15, 35] | 5 .. 40 |
| p_n_mid | 24.5 [12.8, 56.2] | 10 .. 120 |
| p_empty | 0.3 [0.248, 0.368] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 5] | 2 .. 5 |
| p_n_grilles | 6 [5, 7] | 3 .. 8 |

### slotcite: taze medyan mesafe 3.17, en iyi 1.83

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -3.9 | 0.715 | 0.588 |
| vocab_ed1_density | +3.1 | 0.823 | 0.890 |
| zipf_slope | +2.5 | -0.785 | -0.617 |
| jsd_line_final | -2.5 | 0.110 | 0.016 |
| h2_over_h1 | +2.3 | 0.521 | 0.599 |
| h2 | +2.1 | 2.013 | 2.311 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.15 [6.37, 10.8] | 5 .. 13 |
| l_width_jitter | 0.173 [0.0819, 0.277] | 0 .. 0.35 |
| l_para_lines | 0 [0, 7.95] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0475] | 0.01 .. 0.15 |
| l_final_forms_share | 0.467 [0.305, 0.649] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0.5 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.511 [0, 0.717] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.255] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.505] | 0.3 .. 1 |
| p_alphabet | 21.5 [18, 24] | 15 .. 25 |
| p_slot_overlap | 0.259 [0.0756, 0.553] | 0 .. 1 |
| p_n_edge | 24 [17, 33] | 5 .. 40 |
| p_n_mid | 20 [10.8, 50.8] | 10 .. 120 |
| p_empty | 0.29 [0.223, 0.345] | 0 .. 0.6 |
| p_len_edge | 3 [3, 3] | 1 .. 3 |
| p_len_mid | 3 [3, 4] | 2 .. 5 |
| p_copy | 0.598 [0.508, 0.677] | 0.5 .. 0.97 |
| p_exact | 0.213 [0.117, 0.369] | 0.1 .. 0.7 |
| p_reach | 8 [3.75, 16.2] | 1 .. 30 |
| p_same_line | 0.0605 [0.02, 0.103] | 0 .. 0.5 |
| p_mut_prefix | 0.445 [0.292, 0.58] | 0 .. 1 |
| p_mut_mid | 0.387 [0.201, 0.548] | 0 .. 1 |
| p_mut_suffix | 0.292 [0.105, 0.433] | 0 .. 1 |

### selfcite: taze medyan mesafe 3.36, en iyi 2.33

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +5.2 | 0.066 | 0.144 |
| vocab_ed1_density | +5.1 | 0.823 | 0.933 |
| h2_over_h1 | +4.6 | 0.521 | 0.675 |
| h2 | +4.4 | 2.013 | 2.622 |
| hapax_ratio | -4.3 | 0.715 | 0.578 |
| first_entropy_ratio | +3.6 | 0.817 | 0.878 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 11.2 [9.72, 12.5] | 5 .. 13 |
| l_width_jitter | 0.27 [0.195, 0.329] | 0 .. 0.35 |
| l_para_lines | 9.26 [3.75, 11.8] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0118] | 0.01 .. 0.15 |
| l_final_forms_share | 0.781 [0.664, 0.891] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0.235 [0, 0.391] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 3] | 0 .. 4 |
| l_line_initial_p | 0.494 [0.252, 0.701] | 0.1 .. 0.9 |
| l_line_final_p | 0.1 [0, 0.308] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.581] | 0.3 .. 1 |
| p_alphabet | 16.5 [15.8, 18] | 15 .. 25 |
| p_glyph_classes | 6 [5, 7] | 4 .. 7 |
| p_copy | 0.881 [0.859, 0.902] | 0.85 .. 0.97 |
| p_exact | 0.449 [0.381, 0.532] | 0.2 .. 0.8 |
| p_reach | 27 [22.8, 30] | 1 .. 30 |
| p_same_line | 0.0398 [0.013, 0.0592] | 0 .. 0.3 |
| p_slot_overlap | 0.218 [0.0355, 0.511] | 0 .. 1 |
| p_affix | 0.824 [0.753, 0.873] | 0.3 .. 0.9 |
| p_mut_substitute | 0.315 [0.106, 0.485] | 0 .. 1 |
| p_mut_prefix | 0.587 [0.41, 0.786] | 0 .. 1 |
| p_mut_delete | 0.0635 [0.00692, 0.166] | 0 .. 1 |
| p_mut_double | 0.184 [0.0995, 0.292] | 0 .. 1 |

### slotgram: taze medyan mesafe 3.40, en iyi 2.04

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| zipf_slope | +3.4 | -0.785 | -0.551 |
| h2_over_h1 | +2.8 | 0.521 | 0.615 |
| h2 | +2.6 | 2.013 | 2.368 |
| top10_coverage | -2.4 | 0.175 | 0.085 |
| wlen_autocorr1 | -2.3 | 0.123 | 0.012 |
| jsd_line_final | -2.3 | 0.110 | 0.023 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.85 [7.13, 11.5] | 5 .. 13 |
| l_width_jitter | 0.229 [0.124, 0.291] | 0 .. 0.35 |
| l_para_lines | 5.24 [0, 11.4] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.3] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0766] | 0.01 .. 0.15 |
| l_final_forms_share | 0.527 [0.325, 0.671] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.442] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.287] | 0.1 .. 0.9 |
| l_para_initial_p | 0.316 [0, 0.737] | 0.3 .. 1 |
| p_alphabet | 19 [18, 22] | 15 .. 25 |
| p_n_slots | 6 [5, 7] | 3 .. 8 |
| p_slot_overlap | 0.443 [0.22, 0.719] | 0 .. 1 |
| p_n_inv | 7 [3, 10] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.432 [0.361, 0.505] | 0.1 .. 0.8 |
| p_copy | 0.3 [0, 0.751] | 0.3 .. 0.95 |
| p_exact | 0.32 [0.0844, 0.448] | 0 .. 0.5 |
| p_reach | 11 [4, 21.2] | 1 .. 30 |
| p_same_line | 0.077 [0.0209, 0.18] | 0 .. 0.5 |

### verbose: taze medyan mesafe 3.52, en iyi 2.40

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +6.6 | 0.097 | 0.185 |
| wlen_skew | +5.3 | 0.025 | 0.569 |
| first_entropy_ratio | +4.2 | 0.817 | 0.888 |
| hapax_ratio | -3.8 | 0.715 | 0.592 |
| wlen_autocorr1 | -3.4 | 0.123 | -0.035 |
| wlen_frac1 | +3.3 | 0.033 | 0.067 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.1 [7.33, 11.7] | 5 .. 13 |
| l_width_jitter | 0.183 [0.091, 0.3] | 0 .. 0.35 |
| l_para_lines | 0 [0, 9.35] | 3 .. 15 |
| l_allo_per_glyph | 1.37 [0.313, 2.25] | 0.2 .. 3 |
| l_allo_rate | 0.0393 [0, 0.0682] | 0.01 .. 0.15 |
| l_final_forms_share | 0.507 [0.342, 0.724] | 0.1 .. 1 |
| l_final_forms_k | 2 [0.75, 3.25] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.119] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.281 [0, 0.553] | 0.1 .. 0.9 |
| l_line_final_p | 0.1 [0, 0.259] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.589] | 0.3 .. 1 |
| p_alphabet | 13 [12, 15] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0.0689] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 35, Romanian 12, Turkish 11, Croatian 11, Albanian 8

### plain: taze medyan mesafe 3.67, en iyi 3.16

Voynich'ten 2 birimden fazla sapan feature sayısı: 21

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -8.5 | 0.636 | 0.081 |
| first_entropy_ratio | +6.1 | 0.817 | 0.921 |
| h2 | +5.8 | 2.013 | 2.815 |
| h2_over_h1 | +5.7 | 0.521 | 0.714 |
| jsd_last | +5.4 | 0.712 | 0.959 |
| vocab_ed1_density | -5.2 | 0.823 | 0.712 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 11.4 [10.4, 12.4] | 5 .. 13 |
| l_width_jitter | 0.0933 [0.0373, 0.189] | 0 .. 0.35 |
| l_para_lines | 0 [0, 11.4] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.936 [0.872, 0.97] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.735] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Arabic 86, Hebrew 14

### abjad: taze medyan mesafe 4.99, en iyi 3.88

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +18.0 | 0.097 | 0.338 |
| wlen_frac1 | +8.1 | 0.033 | 0.116 |
| wlen_mean | -7.1 | 4.961 | 3.354 |
| type_len_mean | -6.8 | 5.640 | 4.416 |
| wlen_skew | +6.2 | 0.025 | 0.661 |
| h2_over_h1 | +5.3 | 0.521 | 0.701 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.17 [5, 8.15] | 5 .. 13 |
| l_width_jitter | 0.134 [0.0458, 0.247] | 0 .. 0.35 |
| l_para_lines | 4.43 [0, 8.35] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.471] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.676 [0.572, 0.786] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.451 [0.354, 0.513] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 2.25] | 0 .. 4 |
| l_line_initial_p | 0.334 [0, 0.573] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0.493 [0.3, 0.632] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100


## zl_glyph: sınıf sınıf

### grille: taze medyan mesafe 2.46, en iyi 1.55

Voynich'ten 2 birimden fazla sapan feature sayısı: 3

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -2.6 | 0.102 | -0.003 |
| n_symbols | -2.4 | 44.750 | 22.000 |
| h2_over_h1 | +2.2 | 0.554 | 0.642 |
| vocab_ed1_density | +1.9 | 0.852 | 0.883 |
| h2 | +1.8 | 2.127 | 2.446 |
| hapax_ratio | -1.8 | 0.715 | 0.657 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.67 [6.61, 10.7] | 5 .. 13 |
| l_width_jitter | 0.189 [0.0941, 0.274] | 0 .. 0.35 |
| l_para_lines | 4.48 [0, 9.12] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.49] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0225] | 0.01 .. 0.15 |
| l_final_forms_share | 0.608 [0.504, 0.722] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.288 [0, 0.442] | 0.1 .. 0.9 |
| l_line_final_p | 0.144 [0, 0.339] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.871] | 0.3 .. 1 |
| p_alphabet | 18 [16, 20] | 15 .. 25 |
| p_rows | 1.25e+03 [708, 2.25e+03] | 60 .. 3000 |
| p_slot_overlap | 0.674 [0.45, 0.852] | 0 .. 1 |
| p_n_edge | 27 [21, 40] | 5 .. 40 |
| p_n_mid | 34 [19.8, 52.5] | 10 .. 120 |
| p_empty | 0.389 [0.338, 0.441] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_n_grilles | 7 [6, 8] | 3 .. 8 |

### slotcite: taze medyan mesafe 2.54, en iyi 1.61

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| jsd_line_final | -2.3 | 0.110 | 0.022 |
| h2_over_h1 | +2.3 | 0.554 | 0.647 |
| n_symbols | -2.3 | 44.750 | 23.000 |
| h2 | +2.1 | 2.127 | 2.501 |
| vocab_ed1_density | +2.1 | 0.852 | 0.886 |
| rep_adjacent_exact | +2.1 | 0.008 | 0.014 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.7 [8.17, 12.6] | 5 .. 13 |
| l_width_jitter | 0.123 [0.0226, 0.235] | 0 .. 0.35 |
| l_para_lines | 7.86 [0, 10.9] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.87] | 0.2 .. 3 |
| l_allo_rate | 0.0197 [0, 0.0806] | 0.01 .. 0.15 |
| l_final_forms_share | 0.62 [0.438, 0.725] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.404 [0.177, 0.586] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.268] | 0.1 .. 0.9 |
| l_para_initial_p | 0.48 [0, 0.712] | 0.3 .. 1 |
| p_alphabet | 18 [16.8, 20] | 15 .. 25 |
| p_slot_overlap | 0.605 [0.401, 0.844] | 0 .. 1 |
| p_n_edge | 28 [17, 40] | 5 .. 40 |
| p_n_mid | 40 [21.8, 61] | 10 .. 120 |
| p_empty | 0.325 [0.262, 0.41] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_copy | 0.595 [0.531, 0.714] | 0.5 .. 0.97 |
| p_exact | 0.193 [0.123, 0.27] | 0.1 .. 0.7 |
| p_reach | 9 [4, 16.2] | 1 .. 30 |
| p_same_line | 0.161 [0.0692, 0.282] | 0 .. 0.5 |
| p_mut_prefix | 0.208 [0.0692, 0.362] | 0 .. 1 |
| p_mut_mid | 0.535 [0.368, 0.649] | 0 .. 1 |
| p_mut_suffix | 0.202 [0.0371, 0.366] | 0 .. 1 |

### selfcite: taze medyan mesafe 2.64, en iyi 1.59

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| h2_over_h1 | +4.0 | 0.554 | 0.719 |
| vocab_ed1_density | +4.0 | 0.852 | 0.916 |
| h2 | +3.8 | 2.127 | 2.790 |
| hapax_ratio | -3.4 | 0.715 | 0.606 |
| rep_adjacent_exact | +2.6 | 0.008 | 0.015 |
| wlen_std | -2.3 | 1.615 | 1.490 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.22 [7.75, 10.5] | 5 .. 13 |
| l_width_jitter | 0.16 [0.0465, 0.291] | 0 .. 0.35 |
| l_para_lines | 3.93 [0, 10] | 3 .. 15 |
| l_allo_per_glyph | 0.491 [0, 1.76] | 0.2 .. 3 |
| l_allo_rate | 0.0463 [0, 0.0753] | 0.01 .. 0.15 |
| l_final_forms_share | 0.649 [0.503, 0.773] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.385 [0.133, 0.582] | 0.1 .. 0.9 |
| l_line_final_p | 0.229 [0, 0.32] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.459] | 0.3 .. 1 |
| p_alphabet | 16 [15.8, 18] | 15 .. 25 |
| p_glyph_classes | 6 [5, 7] | 4 .. 7 |
| p_copy | 0.876 [0.859, 0.895] | 0.85 .. 0.97 |
| p_exact | 0.406 [0.293, 0.58] | 0.2 .. 0.8 |
| p_reach | 25 [19, 29] | 1 .. 30 |
| p_same_line | 0.0174 [0, 0.0611] | 0 .. 0.3 |
| p_slot_overlap | 0.2 [0.0395, 0.482] | 0 .. 1 |
| p_affix | 0.762 [0.655, 0.857] | 0.3 .. 0.9 |
| p_mut_substitute | 0.262 [0.123, 0.596] | 0 .. 1 |
| p_mut_prefix | 0.564 [0.365, 0.697] | 0 .. 1 |
| p_mut_delete | 0.113 [0.0472, 0.164] | 0 .. 1 |
| p_mut_double | 0.0755 [0.0253, 0.118] | 0 .. 1 |

### slotgram: taze medyan mesafe 2.65, en iyi 1.68

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| vocab_ed1_density | +3.2 | 0.852 | 0.903 |
| jsd_line_final | -2.5 | 0.110 | 0.014 |
| n_symbols | -2.4 | 44.750 | 22.000 |
| wlen_autocorr1 | -2.2 | 0.102 | 0.013 |
| h2_over_h1 | +2.0 | 0.554 | 0.636 |
| zipf_slope | +2.0 | -0.785 | -0.649 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10 [7.65, 12] | 5 .. 13 |
| l_width_jitter | 0.175 [0.0545, 0.277] | 0 .. 0.35 |
| l_para_lines | 9.3 [5.35, 12.1] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.643 [0.511, 0.808] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.201 [0, 0.471] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.21] | 0.1 .. 0.9 |
| l_para_initial_p | 0.158 [0, 0.757] | 0.3 .. 1 |
| p_alphabet | 20 [18, 23] | 15 .. 25 |
| p_n_slots | 4 [4, 5] | 3 .. 8 |
| p_slot_overlap | 0.569 [0.282, 0.831] | 0 .. 1 |
| p_n_inv | 12 [9, 19.2] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.382 [0.342, 0.432] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0.739] | 0.3 .. 0.95 |
| p_exact | 0.153 [0.0577, 0.358] | 0 .. 0.5 |
| p_reach | 16 [6, 28] | 1 .. 30 |
| p_same_line | 0.112 [0.0349, 0.29] | 0 .. 0.5 |

### verbose: taze medyan mesafe 2.72, en iyi 1.87

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_skew | +4.8 | 0.154 | 0.637 |
| wlen_std | +4.7 | 1.615 | 1.876 |
| wlen_autocorr1 | -3.3 | 0.102 | -0.028 |
| jsd_last | -2.7 | 0.712 | 0.590 |
| wlen_frac1 | +2.6 | 0.033 | 0.061 |
| rep_adjacent_exact | -2.4 | 0.008 | 0.003 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.62 [7.46, 10.2] | 5 .. 13 |
| l_width_jitter | 0.126 [0.0318, 0.23] | 0 .. 0.35 |
| l_para_lines | 4.89 [0, 8.53] | 3 .. 15 |
| l_allo_per_glyph | 2.24 [1.67, 2.84] | 0.2 .. 3 |
| l_allo_rate | 0.0618 [0.045, 0.0766] | 0.01 .. 0.15 |
| l_final_forms_share | 0.381 [0.238, 0.515] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.118] | 0.1 .. 1 |
| l_initial_forms_k | 2 [0, 3] | 0 .. 4 |
| l_line_initial_p | 0.191 [0, 0.482] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.245] | 0.1 .. 0.9 |
| l_para_initial_p | 0.3 [0, 0.462] | 0.3 .. 1 |
| p_alphabet | 12 [12, 13] | 12 .. 22 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Croatian 63, Romanian 29, Italian 8

### plain: taze medyan mesafe 2.98, en iyi 2.45

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -5.4 | 0.636 | 0.300 |
| wlen_std | -5.4 | 1.615 | 1.315 |
| vocab_ed1_density | -4.7 | 0.852 | 0.777 |
| h2_over_h1 | +4.5 | 0.554 | 0.736 |
| h2 | +4.5 | 2.127 | 2.904 |
| char_double_rate | -4.2 | 0.076 | 0.009 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.72 [7.57, 11.7] | 5 .. 13 |
| l_width_jitter | 0.221 [0.151, 0.304] | 0 .. 0.35 |
| l_para_lines | 6.36 [0, 10.6] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.811 [0.737, 0.886] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.572] | 0.1 .. 0.9 |
| l_line_final_p | 0.25 [0.0781, 0.384] | 0.1 .. 0.9 |
| l_para_initial_p | 0.531 [0, 0.709] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### abjad: taze medyan mesafe 3.17, en iyi 2.50

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +7.3 | 0.033 | 0.111 |
| wlen_frac_le2 | +6.3 | 0.119 | 0.329 |
| wlen_skew | +5.1 | 0.154 | 0.672 |
| vocab_ed1_density | -4.1 | 0.852 | 0.786 |
| h2_over_h1 | +3.8 | 0.554 | 0.710 |
| h2 | +3.6 | 2.127 | 2.760 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.45 [5, 8.1] | 5 .. 13 |
| l_width_jitter | 0.154 [0.0548, 0.262] | 0 .. 0.35 |
| l_para_lines | 6.83 [0, 9.26] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.712 [0.646, 0.778] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.371 [0.271, 0.435] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 3] | 0 .. 4 |
| l_line_initial_p | 0.359 [0, 0.611] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0.468 [0.3, 0.607] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100
