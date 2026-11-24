# Yönlendirilmiş arama raporu: her hipotezin ulaşabildiği en iyi nokta

Her (sınıf, görünüm) için 5 tur, tur başına 600 deneme, en yakın 100 ayar tutuldu. Tablolardaki mesafeler, son turda kalan ayarların her biriyle yeniden üretilen 2 taze örnekten hesaplandı (toplam 200).

Mesafe birimi ve ölçüt `abc.md` ile aynı: bir hipotezin taze örnekleri Voynich öz mesafesinin içine giriyorsa, o hipotez bu feature kümesinde Voynich'ten ayırt edilemez.

## 1. Taze örneklerin medyan mesafesi (parantezde rejection ABC'deki değer)

| görünüm | Voynich öz mesafesi (medyan, en çok) | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.91, 1.65 | 5.91 (6.18) | 4.42 (4.76) | 3.34 (2.86) | 4.10 (5.36) | 3.69 (4.48) | 3.29 (3.10) | 3.82 (3.36) | 3.84 (4.06) |
| eva_glyph | 0.96, 1.64 | 3.63 (4.04) | 4.02 (4.31) | 2.77 (2.54) | 2.98 (4.13) | 2.76 (3.53) | 2.94 (2.84) | 3.33 (2.93) | 3.48 (3.59) |
| v101 | 0.97, 1.42 | 2.95 (3.27) | 3.38 (3.94) | 3.44 (2.60) | 2.60 (3.05) | 3.14 (3.83) | 3.70 (2.96) | 3.39 (2.83) | 3.21 (3.41) |
| zl_basic | 0.96, 1.52 | 5.03 (5.40) | 4.42 (4.77) | 2.94 (2.47) | 3.67 (4.66) | 3.41 (3.94) | 2.86 (2.62) | 3.47 (2.97) | 3.25 (3.37) |
| zl_glyph | 1.03, 1.43 | 3.25 (3.61) | 3.47 (4.04) | 2.56 (2.15) | 2.93 (3.76) | 2.62 (3.10) | 2.56 (2.27) | 2.93 (2.49) | 2.95 (2.99) |

## 2. Voynich'in en uç penceresi kadar yakın olan taze örneklerin oranı

| görünüm | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 |
| eva_glyph | %0 | %0 | %1 | %0 | %0 | %0 | %0 | %0 |
| v101 | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 |
| zl_basic | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 |
| zl_glyph | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 |

## 3. Arama yakınsadı mı (tur tur, tutulan ayarların medyan mesafesi)

| görünüm | sınıf | turlar |
|---|---|---|
| eva_basic | abjad | 6.03 -> 5.75 -> 5.58 -> 5.45 -> 5.42 |
| eva_basic | codebook | 4.81 -> 4.66 -> 4.46 -> 4.37 -> 4.23 |
| eva_basic | grille | 2.88 -> 2.80 -> 2.74 -> 2.65 -> 2.66 |
| eva_basic | plain | 4.91 -> 4.15 -> 3.96 -> 3.93 -> 3.88 |
| eva_basic | selfcite | 3.99 -> 3.70 -> 3.58 -> 3.41 -> 3.34 |
| eva_basic | slotcite | 3.07 -> 3.03 -> 2.89 -> 2.82 -> 2.74 |
| eva_basic | slotgram | 3.34 -> 3.21 -> 3.17 -> 3.22 -> 3.21 |
| eva_basic | verbose | 3.88 -> 3.67 -> 3.53 -> 3.50 -> 3.41 |
| eva_glyph | abjad | 3.80 -> 3.55 -> 3.40 -> 3.32 -> 3.28 |
| eva_glyph | codebook | 4.28 -> 4.06 -> 3.94 -> 3.75 -> 3.72 |
| eva_glyph | grille | 2.60 -> 2.44 -> 2.34 -> 2.36 -> 2.30 |
| eva_glyph | plain | 3.54 -> 3.09 -> 2.93 -> 2.84 -> 2.78 |
| eva_glyph | selfcite | 3.19 -> 2.89 -> 2.84 -> 2.70 -> 2.50 |
| eva_glyph | slotcite | 2.84 -> 2.68 -> 2.51 -> 2.50 -> 2.45 |
| eva_glyph | slotgram | 3.12 -> 3.02 -> 2.86 -> 2.91 -> 2.77 |
| eva_glyph | verbose | 3.62 -> 3.50 -> 3.29 -> 3.22 -> 3.12 |
| v101 | abjad | 2.96 -> 2.80 -> 2.71 -> 2.67 -> 2.62 |
| v101 | codebook | 3.85 -> 3.60 -> 3.37 -> 3.27 -> 3.18 |
| v101 | grille | 2.92 -> 2.76 -> 2.75 -> 2.75 -> 2.76 |
| v101 | plain | 2.66 -> 2.48 -> 2.44 -> 2.37 -> 2.37 |
| v101 | selfcite | 3.54 -> 3.25 -> 3.10 -> 2.97 -> 2.89 |
| v101 | slotcite | 3.14 -> 3.06 -> 3.00 -> 2.81 -> 2.81 |
| v101 | slotgram | 3.03 -> 2.90 -> 2.85 -> 2.91 -> 2.78 |
| v101 | verbose | 3.30 -> 3.13 -> 3.01 -> 2.82 -> 2.76 |
| zl_basic | abjad | 5.25 -> 5.08 -> 4.79 -> 4.67 -> 4.54 |
| zl_basic | codebook | 4.77 -> 4.61 -> 4.41 -> 4.25 -> 4.13 |
| zl_basic | grille | 2.75 -> 2.60 -> 2.45 -> 2.43 -> 2.33 |
| zl_basic | plain | 4.10 -> 3.67 -> 3.56 -> 3.52 -> 3.46 |
| zl_basic | selfcite | 3.75 -> 3.43 -> 3.21 -> 3.09 -> 3.02 |
| zl_basic | slotcite | 2.83 -> 2.72 -> 2.59 -> 2.43 -> 2.43 |
| zl_basic | slotgram | 3.03 -> 2.91 -> 2.90 -> 2.81 -> 2.86 |
| zl_basic | verbose | 3.25 -> 3.15 -> 3.00 -> 2.95 -> 2.83 |
| zl_glyph | abjad | 3.37 -> 3.12 -> 3.03 -> 2.99 -> 2.96 |
| zl_glyph | codebook | 3.99 -> 3.72 -> 3.49 -> 3.26 -> 3.26 |
| zl_glyph | grille | 2.29 -> 2.19 -> 2.12 -> 2.08 -> 1.99 |
| zl_glyph | plain | 3.17 -> 2.90 -> 2.75 -> 2.76 -> 2.73 |
| zl_glyph | selfcite | 2.87 -> 2.63 -> 2.55 -> 2.44 -> 2.36 |
| zl_glyph | slotcite | 2.45 -> 2.24 -> 2.17 -> 2.16 -> 2.12 |
| zl_glyph | slotgram | 2.70 -> 2.59 -> 2.53 -> 2.44 -> 2.38 |
| zl_glyph | verbose | 2.93 -> 2.85 -> 2.68 -> 2.68 -> 2.57 |

## eva_basic: sınıf sınıf

### slotcite: taze medyan mesafe 3.29, en iyi 1.89

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -4.4 | 0.717 | 0.621 |
| h2_over_h1 | +3.2 | 0.524 | 0.622 |
| h2 | +3.1 | 2.016 | 2.393 |
| zipf_slope | +2.9 | -0.778 | -0.593 |
| vocab_ed1_density | +2.5 | 0.823 | 0.885 |
| jsd_line_final | -2.2 | 0.109 | 0.038 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.24 [5.89, 10.2] | 5 .. 13 |
| l_width_jitter | 0.239 [0.0942, 0.311] | 0 .. 0.35 |
| l_para_lines | 0 [0, 8.16] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.557 [0.369, 0.789] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.485 [0.269, 0.69] | 0.1 .. 0.9 |
| l_line_final_p | 0.1 [0, 0.327] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.541] | 0.3 .. 1 |
| p_alphabet | 21 [18, 23] | 15 .. 25 |
| p_slot_overlap | 0.317 [0.109, 0.63] | 0 .. 1 |
| p_n_edge | 26 [20, 35.2] | 5 .. 40 |
| p_n_mid | 28 [18, 58.2] | 10 .. 120 |
| p_empty | 0.253 [0.195, 0.32] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_copy | 0.572 [0.5, 0.678] | 0.5 .. 0.97 |
| p_exact | 0.178 [0.113, 0.244] | 0.1 .. 0.7 |
| p_reach | 10 [4.75, 19] | 1 .. 30 |
| p_same_line | 0.162 [0.0332, 0.25] | 0 .. 0.5 |
| p_mut_prefix | 0.241 [0.082, 0.415] | 0 .. 1 |
| p_mut_mid | 0.395 [0.211, 0.559] | 0 .. 1 |
| p_mut_suffix | 0.349 [0.191, 0.502] | 0 .. 1 |

### grille: taze medyan mesafe 3.34, en iyi 2.04

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -3.4 | 0.127 | -0.004 |
| jsd_line_final | -3.2 | 0.109 | 0.005 |
| h2 | +3.2 | 2.016 | 2.406 |
| h2_over_h1 | +3.2 | 0.524 | 0.623 |
| rep_adjacent_ed1 | -2.6 | 0.032 | 0.015 |
| hapax_ratio | -2.4 | 0.717 | 0.664 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.65 [5.71, 10] | 5 .. 13 |
| l_width_jitter | 0.161 [0.0826, 0.256] | 0 .. 0.35 |
| l_para_lines | 6.65 [2.25, 9.45] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.488] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.626 [0.477, 0.739] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.276 [0, 0.608] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.503] | 0.3 .. 1 |
| p_alphabet | 19 [17, 21] | 15 .. 25 |
| p_rows | 1.59e+03 [946, 2.28e+03] | 60 .. 3000 |
| p_slot_overlap | 0.553 [0.17, 0.84] | 0 .. 1 |
| p_n_edge | 24 [17, 36] | 5 .. 40 |
| p_n_mid | 35.5 [18, 57.2] | 10 .. 120 |
| p_empty | 0.282 [0.24, 0.338] | 0 .. 0.6 |
| p_len_edge | 3 [3, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_n_grilles | 7 [5, 8] | 3 .. 8 |

### selfcite: taze medyan mesafe 3.69, en iyi 2.88

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -6.4 | 0.717 | 0.574 |
| char_double_rate | +6.0 | 0.067 | 0.150 |
| h2 | +6.0 | 2.016 | 2.735 |
| h2_over_h1 | +5.9 | 0.524 | 0.708 |
| vocab_ed1_density | +4.7 | 0.823 | 0.941 |
| first_entropy_ratio | +3.9 | 0.806 | 0.876 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.78 [7.35, 11.3] | 5 .. 13 |
| l_width_jitter | 0.151 [0.0703, 0.25] | 0 .. 0.35 |
| l_para_lines | 0 [0, 9.19] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.562 [0.382, 0.78] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.341] | 0.1 .. 1 |
| l_initial_forms_k | 2 [0, 3] | 0 .. 4 |
| l_line_initial_p | 0.05 [0, 0.529] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.106] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.606] | 0.3 .. 1 |
| p_alphabet | 16 [15, 18] | 15 .. 25 |
| p_glyph_classes | 6 [5, 7] | 4 .. 7 |
| p_copy | 0.888 [0.859, 0.914] | 0.85 .. 0.97 |
| p_exact | 0.403 [0.322, 0.523] | 0.2 .. 0.8 |
| p_reach | 26 [22, 30] | 1 .. 30 |
| p_same_line | 0.0364 [0.00327, 0.06] | 0 .. 0.3 |
| p_slot_overlap | 0.248 [0.0456, 0.515] | 0 .. 1 |
| p_affix | 0.831 [0.729, 0.9] | 0.3 .. 0.9 |
| p_mut_substitute | 0.571 [0.409, 0.734] | 0 .. 1 |
| p_mut_prefix | 0.402 [0.298, 0.506] | 0 .. 1 |
| p_mut_delete | 0.037 [0.00351, 0.0828] | 0 .. 1 |
| p_mut_double | 0.166 [0.103, 0.211] | 0 .. 1 |

### slotgram: taze medyan mesafe 3.82, en iyi 2.30

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| zipf_slope | +4.4 | -0.778 | -0.501 |
| wlen_autocorr1 | -2.7 | 0.127 | 0.022 |
| top10_coverage | -2.6 | 0.171 | 0.077 |
| vocab_ed1_density | +2.5 | 0.823 | 0.885 |
| wlen_std | +2.4 | 1.693 | 1.866 |
| word_entropy_norm | +2.3 | 0.804 | 0.877 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.99 [5.98, 10.4] | 5 .. 13 |
| l_width_jitter | 0.196 [0.105, 0.271] | 0 .. 0.35 |
| l_para_lines | 0 [0, 6.82] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.484] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.609 [0.379, 0.772] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.279 [0, 0.554] | 0.1 .. 0.9 |
| l_line_final_p | 0.111 [0, 0.329] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.766] | 0.3 .. 1 |
| p_alphabet | 19 [17, 23] | 15 .. 25 |
| p_n_slots | 6 [5, 7] | 3 .. 8 |
| p_slot_overlap | 0.404 [0.155, 0.735] | 0 .. 1 |
| p_n_inv | 6 [3, 9] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.413 [0.334, 0.518] | 0.1 .. 0.8 |
| p_copy | 0.483 [0, 0.645] | 0.3 .. 0.95 |
| p_exact | 0.288 [0.15, 0.372] | 0 .. 0.5 |
| p_reach | 11.5 [4, 26.2] | 1 .. 30 |
| p_same_line | 0.115 [0.0165, 0.249] | 0 .. 0.5 |

### verbose: taze medyan mesafe 3.84, en iyi 2.52

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -8.7 | 0.717 | 0.524 |
| wlen_frac_le2 | +6.2 | 0.077 | 0.148 |
| wlen_std | +4.5 | 1.693 | 2.021 |
| wlen_autocorr1 | -4.2 | 0.127 | -0.035 |
| first_entropy_ratio | +3.9 | 0.806 | 0.877 |
| wlen_skew | +3.9 | 0.074 | 0.580 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 5.9 [5.2, 7.01] | 5 .. 13 |
| l_width_jitter | 0.162 [0.0356, 0.264] | 0 .. 0.35 |
| l_para_lines | 7.67 [0, 13.3] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.669] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0699] | 0.01 .. 0.15 |
| l_final_forms_share | 0.405 [0, 0.662] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.52 [0.333, 0.679] | 0.1 .. 0.9 |
| l_line_final_p | 0.362 [0.183, 0.456] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.573] | 0.3 .. 1 |
| p_alphabet | 16 [13.8, 18] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.405 [0.323, 0.498] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0.332] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 31, Czech 27, Romanian 26, Croatian 12, Albanian 1

### plain: taze medyan mesafe 4.10, en iyi 3.26

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -7.5 | 0.628 | 0.167 |
| type_len_mean | -6.6 | 5.692 | 4.557 |
| first_entropy_ratio | +6.6 | 0.806 | 0.925 |
| wlen_frac_le2 | +6.5 | 0.077 | 0.152 |
| h2 | +6.4 | 2.016 | 2.783 |
| h2_over_h1 | +6.1 | 0.524 | 0.713 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.86 [6.09, 9.05] | 5 .. 13 |
| l_width_jitter | 0.173 [0.0968, 0.252] | 0 .. 0.35 |
| l_para_lines | 4.38 [0, 10.2] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.905 [0.842, 0.968] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.134] | 0.1 .. 1 |
| l_initial_forms_k | 2 [0, 3] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.163] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.0304] | 0.1 .. 0.9 |
| l_para_initial_p | 0.3 [0, 0.492] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 97, Arabic 3

### codebook: taze medyan mesafe 4.42, en iyi 3.03

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| type_len_mean | -11.6 | 5.692 | 3.721 |
| wlen_std | -10.1 | 1.693 | 0.954 |
| vocab_ed1_density | +6.9 | 0.823 | 0.996 |
| wlen_mean | -5.9 | 5.066 | 3.702 |
| jsd_first | +5.0 | 0.385 | 0.556 |
| first_entropy_ratio | -4.2 | 0.806 | 0.730 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.4 [7.89, 11.9] | 5 .. 13 |
| l_width_jitter | 0.199 [0.128, 0.279] | 0 .. 0.35 |
| l_para_lines | 7.54 [2.25, 11.6] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.816] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0025] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0.377] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.486 [0.193, 0.667] | 0.1 .. 0.9 |
| l_line_final_p | 0.205 [0, 0.374] | 0.1 .. 0.9 |
| l_para_initial_p | 0.409 [0, 0.73] | 0.3 .. 1 |
| p_alphabet | 19 [17, 20] | 15 .. 25 |
| p_n_slots | 6 [5, 6] | 3 .. 6 |
| p_slot_overlap | 0.0198 [0, 0.0441] | 0 .. 1 |
| p_len_max | 1 [1, 1] | 1 .. 2 |
| p_zero_empty | 1 [1, 1] | 0 .. 1 |
| p_order | 2 [2, 2] | 0 .. 2 |

Kaynak dil (son nüfusta en sık): Turkish 25, Finnish 15, Czech 13, Croatian 9, Arabic 8

### abjad: taze medyan mesafe 5.91, en iyi 4.62

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +22.4 | 0.077 | 0.337 |
| wlen_frac1 | +8.7 | 0.017 | 0.115 |
| wlen_mean | -7.4 | 5.066 | 3.346 |
| type_len_mean | -7.3 | 5.692 | 4.453 |
| h2 | +5.4 | 2.016 | 2.666 |
| eff_symbols | +5.3 | 14.240 | 15.962 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.81 [7.38, 11.6] | 5 .. 13 |
| l_width_jitter | 0.121 [0.024, 0.246] | 0 .. 0.35 |
| l_para_lines | 0 [0, 8.13] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.836 [0.709, 0.953] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.429 [0.205, 0.529] | 0.1 .. 1 |
| l_initial_forms_k | 1 [1, 2] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.398] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100


## eva_glyph: sınıf sınıf

### selfcite: taze medyan mesafe 2.76, en iyi 1.89

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -5.6 | 0.717 | 0.592 |
| h2_over_h1 | +4.3 | 0.556 | 0.720 |
| h2 | +4.2 | 2.131 | 2.784 |
| vocab_ed1_density | +3.5 | 0.850 | 0.928 |
| zipf_slope | +2.8 | -0.778 | -0.603 |
| n_symbols | -2.7 | 25.250 | 22.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.77 [8.84, 11.2] | 5 .. 13 |
| l_width_jitter | 0.178 [0.12, 0.264] | 0 .. 0.35 |
| l_para_lines | 3.03 [0, 9.63] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.512 [0.391, 0.67] | 0.1 .. 1 |
| l_final_forms_k | 3 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.383 [0.211, 0.574] | 0.1 .. 0.9 |
| l_line_final_p | 0.221 [0, 0.346] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.568] | 0.3 .. 1 |
| p_alphabet | 19 [17, 19.2] | 15 .. 25 |
| p_glyph_classes | 6 [5, 7] | 4 .. 7 |
| p_copy | 0.867 [0.85, 0.882] | 0.85 .. 0.97 |
| p_exact | 0.331 [0.252, 0.442] | 0.2 .. 0.8 |
| p_reach | 23 [17.8, 28] | 1 .. 30 |
| p_same_line | 0.0152 [0, 0.036] | 0 .. 0.3 |
| p_slot_overlap | 0.154 [0.019, 0.3] | 0 .. 1 |
| p_affix | 0.821 [0.755, 0.889] | 0.3 .. 0.9 |
| p_mut_substitute | 0.269 [0.112, 0.474] | 0 .. 1 |
| p_mut_prefix | 0.796 [0.523, 0.936] | 0 .. 1 |
| p_mut_delete | 0.0776 [0.0193, 0.128] | 0 .. 1 |
| p_mut_double | 0.0424 [0.0162, 0.0843] | 0 .. 1 |

### grille: taze medyan mesafe 2.77, en iyi 1.60

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -3.1 | 0.103 | -0.001 |
| jsd_line_final | -2.8 | 0.110 | 0.021 |
| n_symbols | -2.7 | 25.250 | 22.000 |
| h2_over_h1 | +2.4 | 0.556 | 0.645 |
| h2 | +2.3 | 2.131 | 2.491 |
| rep_within3 | -2.1 | 0.026 | 0.011 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.8 [5.83, 8.74] | 5 .. 13 |
| l_width_jitter | 0.162 [0.0611, 0.258] | 0 .. 0.35 |
| l_para_lines | 3.1 [0, 7.7] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.73 [0.563, 0.869] | 0.1 .. 1 |
| l_final_forms_k | 3 [3, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.13] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.333 [0, 0.571] | 0.1 .. 0.9 |
| l_line_final_p | 0.0621 [0, 0.326] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.527] | 0.3 .. 1 |
| p_alphabet | 19 [16, 22.2] | 15 .. 25 |
| p_rows | 1.48e+03 [933, 2.19e+03] | 60 .. 3000 |
| p_slot_overlap | 0.57 [0.398, 0.721] | 0 .. 1 |
| p_n_edge | 25.5 [22, 34.2] | 5 .. 40 |
| p_n_mid | 75.5 [38, 119] | 10 .. 120 |
| p_empty | 0.375 [0.307, 0.444] | 0 .. 0.6 |
| p_len_edge | 2 [2, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_n_grilles | 6 [4, 7] | 3 .. 8 |

### slotcite: taze medyan mesafe 2.94, en iyi 1.85

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -4.1 | 0.717 | 0.626 |
| n_symbols | -2.7 | 25.250 | 22.000 |
| zipf_slope | +2.5 | -0.778 | -0.619 |
| vocab_ed1_density | +2.4 | 0.850 | 0.904 |
| first_entropy_ratio | -2.4 | 0.867 | 0.815 |
| h2_over_h1 | +1.8 | 0.556 | 0.624 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.23 [6.63, 9.27] | 5 .. 13 |
| l_width_jitter | 0.129 [0.0134, 0.302] | 0 .. 0.35 |
| l_para_lines | 3.12 [0, 11.2] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.563 [0.25, 0.821] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.478 [0, 0.638] | 0.1 .. 0.9 |
| l_line_final_p | 0.23 [0, 0.333] | 0.1 .. 0.9 |
| l_para_initial_p | 0.3 [0, 0.665] | 0.3 .. 1 |
| p_alphabet | 20 [18, 22.2] | 15 .. 25 |
| p_slot_overlap | 0.478 [0.248, 0.691] | 0 .. 1 |
| p_n_edge | 30.5 [23, 36] | 5 .. 40 |
| p_n_mid | 34 [17.5, 60.2] | 10 .. 120 |
| p_empty | 0.251 [0.201, 0.307] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_copy | 0.588 [0.525, 0.706] | 0.5 .. 0.97 |
| p_exact | 0.127 [0.103, 0.163] | 0.1 .. 0.7 |
| p_reach | 4 [2, 9] | 1 .. 30 |
| p_same_line | 0.0735 [0.0348, 0.196] | 0 .. 0.5 |
| p_mut_prefix | 0.28 [0.159, 0.44] | 0 .. 1 |
| p_mut_mid | 0.303 [0.171, 0.508] | 0 .. 1 |
| p_mut_suffix | 0.483 [0.338, 0.676] | 0 .. 1 |

### plain: taze medyan mesafe 2.98, en iyi 2.48

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -6.5 | 0.626 | 0.251 |
| h2 | +4.8 | 2.131 | 2.877 |
| h2_over_h1 | +4.7 | 0.556 | 0.734 |
| char_double_rate | -4.6 | 0.076 | 0.009 |
| wlen_std | -4.2 | 1.552 | 1.331 |
| vocab_ed1_density | -3.4 | 0.850 | 0.775 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.3 [8.6, 12] | 5 .. 13 |
| l_width_jitter | 0.225 [0.144, 0.275] | 0 .. 0.35 |
| l_para_lines | 4.09 [0, 9.3] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.00369] | 0.01 .. 0.15 |
| l_final_forms_share | 0.824 [0.782, 0.871] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1.25] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_line_final_p | 0.188 [0, 0.256] | 0.1 .. 0.9 |
| l_para_initial_p | 0.302 [0, 0.662] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### slotgram: taze medyan mesafe 3.33, en iyi 1.41

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| n_symbols | -3.5 | 25.250 | 21.000 |
| jsd_line_final | -3.0 | 0.110 | 0.014 |
| wlen_autocorr1 | -2.8 | 0.103 | 0.010 |
| zipf_slope | +2.3 | -0.778 | -0.632 |
| vocab_ed1_density | +2.3 | 0.850 | 0.901 |
| rep_within3 | -2.2 | 0.026 | 0.010 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.31 [6.67, 10.3] | 5 .. 13 |
| l_width_jitter | 0.16 [0.064, 0.238] | 0 .. 0.35 |
| l_para_lines | 8.12 [0, 11.5] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.548 [0.401, 0.736] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 2.25] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.176] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.347 [0, 0.523] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.276] | 0.1 .. 0.9 |
| l_para_initial_p | 0.547 [0, 0.741] | 0.3 .. 1 |
| p_alphabet | 19 [17, 22] | 15 .. 25 |
| p_n_slots | 4 [4, 5] | 3 .. 8 |
| p_slot_overlap | 0.512 [0.265, 0.801] | 0 .. 1 |
| p_n_inv | 10.5 [7.75, 15.2] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.357 [0.243, 0.451] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0] | 0.3 .. 0.95 |
| p_exact | 0.283 [0.135, 0.382] | 0 .. 0.5 |
| p_reach | 7 [2, 19.5] | 1 .. 30 |
| p_same_line | 0.154 [0.0483, 0.329] | 0 .. 0.5 |

### verbose: taze medyan mesafe 3.48, en iyi 2.41

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +8.0 | 1.552 | 1.972 |
| hapax_ratio | -5.0 | 0.717 | 0.605 |
| wlen_skew | +4.2 | 0.183 | 0.630 |
| wlen_autocorr1 | -4.0 | 0.103 | -0.032 |
| jsd_last | -3.8 | 0.718 | 0.534 |
| jsd_first | -3.1 | 0.350 | 0.224 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.43 [5.99, 11.6] | 5 .. 13 |
| l_width_jitter | 0.22 [0.125, 0.28] | 0 .. 0.35 |
| l_para_lines | 0 [0, 6.01] | 3 .. 15 |
| l_allo_per_glyph | 0.849 [0.586, 1.11] | 0.2 .. 3 |
| l_allo_rate | 0.0746 [0.0462, 0.0979] | 0.01 .. 0.15 |
| l_final_forms_share | 0.402 [0, 0.526] | 0.1 .. 1 |
| l_final_forms_k | 2 [0, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.354 [0, 0.556] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.346] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0] | 0.3 .. 1 |
| p_alphabet | 13 [12, 15] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.477 [0.381, 0.559] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Czech 36, Croatian 27, Italian 13, Romanian 13, Polish 3

### abjad: taze medyan mesafe 3.63, en iyi 2.83

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +8.4 | 0.017 | 0.115 |
| wlen_frac_le2 | +7.7 | 0.099 | 0.341 |
| wlen_skew | +4.7 | 0.183 | 0.679 |
| h2_over_h1 | +4.3 | 0.556 | 0.716 |
| h2 | +4.1 | 2.131 | 2.770 |
| wlen_mean | -3.8 | 4.528 | 3.349 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.23 [6.29, 11.7] | 5 .. 13 |
| l_width_jitter | 0.232 [0.0842, 0.331] | 0 .. 0.35 |
| l_para_lines | 3.81 [0, 8.75] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.743 [0.633, 0.846] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.283 [0, 0.404] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 3] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.178] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.331] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.755] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100

### codebook: taze medyan mesafe 4.02, en iyi 2.59

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | -10.5 | 1.552 | 1.004 |
| vocab_ed1_density | +6.3 | 0.850 | 0.990 |
| type_len_mean | -5.6 | 5.032 | 3.828 |
| first_entropy_ratio | -5.3 | 0.867 | 0.749 |
| wlen_skew | -4.7 | 0.183 | -0.317 |
| h1 | -3.6 | 3.832 | 3.734 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.35 [6.61, 11] | 5 .. 13 |
| l_width_jitter | 0.211 [0.105, 0.28] | 0 .. 0.35 |
| l_para_lines | 7.16 [0, 10.9] | 3 .. 15 |
| l_allo_per_glyph | 0.727 [0, 1.76] | 0.2 .. 3 |
| l_allo_rate | 0.0374 [0, 0.113] | 0.01 .. 0.15 |
| l_final_forms_share | 0.521 [0.216, 0.76] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.301 [0, 0.55] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.336] | 0.1 .. 0.9 |
| l_para_initial_p | 0.512 [0, 0.822] | 0.3 .. 1 |
| p_alphabet | 16 [15, 18] | 15 .. 25 |
| p_n_slots | 6 [5, 6] | 3 .. 6 |
| p_slot_overlap | 0.0155 [0, 0.0573] | 0 .. 1 |
| p_len_max | 1 [1, 2] | 1 .. 2 |
| p_zero_empty | 1 [1, 1] | 0 .. 1 |
| p_order | 2 [1, 2] | 0 .. 2 |

Kaynak dil (son nüfusta en sık): Turkish 17, Arabic 14, Italian 13, Croatian 12, Dutch 8


## v101: sınıf sınıf

### plain: taze medyan mesafe 2.60, en iyi 2.15

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| n_symbols | -4.6 | 69.529 | 26.000 |
| vocab_ed1_density | -4.5 | 0.854 | 0.750 |
| wlen_frac1 | -4.5 | 0.046 | 0.000 |
| h2 | +4.0 | 2.383 | 3.057 |
| last_entropy_ratio | -3.9 | 0.704 | 0.463 |
| h2_over_h1 | +3.8 | 0.595 | 0.752 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.77 [5.65, 11.4] | 5 .. 13 |
| l_width_jitter | 0.125 [0.0305, 0.231] | 0 .. 0.35 |
| l_para_lines | 0 [0, 8.44] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0449] | 0.01 .. 0.15 |
| l_final_forms_share | 0.714 [0.624, 0.813] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.48] | 0.1 .. 0.9 |
| l_line_final_p | 0.265 [0, 0.335] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.433] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### abjad: taze medyan mesafe 2.95, en iyi 2.38

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +6.1 | 0.046 | 0.109 |
| wlen_frac_le2 | +5.6 | 0.184 | 0.333 |
| n_symbols | -4.7 | 69.529 | 25.000 |
| h2_over_h1 | +3.4 | 0.595 | 0.735 |
| first_entropy_ratio | +3.3 | 0.886 | 0.994 |
| wlen_skew | +3.3 | 0.225 | 0.678 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.22 [5.31, 7.6] | 5 .. 13 |
| l_width_jitter | 0.181 [0.0724, 0.275] | 0 .. 0.35 |
| l_para_lines | 0 [0, 6.85] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.804 [0.711, 0.888] | 0.1 .. 1 |
| l_final_forms_k | 4 [3, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.236] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.36 [0.146, 0.589] | 0.1 .. 0.9 |
| l_line_final_p | 0.356 [0.187, 0.44] | 0.1 .. 0.9 |
| l_para_initial_p | 0.446 [0, 0.728] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100

### selfcite: taze medyan mesafe 3.14, en iyi 2.22

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +7.6 | 0.015 | 0.056 |
| n_symbols | -4.7 | 69.529 | 25.000 |
| hapax_ratio | -4.0 | 0.741 | 0.622 |
| zipf_slope | +3.6 | -0.776 | -0.618 |
| last_entropy_ratio | -3.4 | 0.704 | 0.497 |
| h2 | +3.2 | 2.383 | 2.932 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.47 [7.31, 11.2] | 5 .. 13 |
| l_width_jitter | 0.0999 [0.0349, 0.217] | 0 .. 0.35 |
| l_para_lines | 6.66 [0, 11.1] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.754] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0256] | 0.01 .. 0.15 |
| l_final_forms_share | 0.818 [0.714, 0.93] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.708 [0.529, 0.824] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.294] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.802] | 0.3 .. 1 |
| p_alphabet | 20 [18, 22] | 15 .. 25 |
| p_glyph_classes | 5 [4, 6] | 4 .. 7 |
| p_copy | 0.864 [0.851, 0.88] | 0.85 .. 0.97 |
| p_exact | 0.357 [0.227, 0.466] | 0.2 .. 0.8 |
| p_reach | 23 [16, 29] | 1 .. 30 |
| p_same_line | 0.0319 [0.00657, 0.091] | 0 .. 0.3 |
| p_slot_overlap | 0.68 [0.54, 0.882] | 0 .. 1 |
| p_affix | 0.745 [0.625, 0.844] | 0.3 .. 0.9 |
| p_mut_substitute | 0.435 [0.272, 0.639] | 0 .. 1 |
| p_mut_prefix | 0.495 [0.327, 0.654] | 0 .. 1 |
| p_mut_delete | 0.262 [0.169, 0.398] | 0 .. 1 |
| p_mut_double | 0.00977 [0, 0.0239] | 0 .. 1 |

### verbose: taze medyan mesafe 3.21, en iyi 1.98

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| jsd_last | -4.9 | 0.679 | 0.429 |
| char_double_rate | +4.6 | 0.015 | 0.040 |
| wlen_std | +4.3 | 1.469 | 1.733 |
| wlen_frac1 | +3.7 | 0.046 | 0.084 |
| wlen_autocorr1 | -3.6 | 0.179 | -0.038 |
| wlen_skew | +3.6 | 0.225 | 0.719 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.8 [8.65, 12.3] | 5 .. 13 |
| l_width_jitter | 0.102 [0.0324, 0.194] | 0 .. 0.35 |
| l_para_lines | 9.43 [0, 12] | 3 .. 15 |
| l_allo_per_glyph | 2.3 [2.01, 2.75] | 0.2 .. 3 |
| l_allo_rate | 0.0976 [0.0745, 0.122] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0.1] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.151] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.293] | 0.1 .. 0.9 |
| l_line_final_p | 0.146 [0, 0.313] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.634] | 0.3 .. 1 |
| p_alphabet | 15 [14, 17] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.746 [0.65, 0.829] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Croatian 65, Romanian 17, Turkish 8, Italian 5, Czech 4

### codebook: taze medyan mesafe 3.38, en iyi 2.54

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | -7.9 | 1.469 | 0.983 |
| type_len_mean | -6.0 | 4.440 | 3.706 |
| vocab_ed1_density | +5.6 | 0.854 | 0.983 |
| jsd_first | +5.0 | 0.310 | 0.563 |
| first_entropy_ratio | -3.9 | 0.886 | 0.763 |
| wlen_skew | -3.7 | 0.225 | -0.278 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.59 [5.37, 7.7] | 5 .. 13 |
| l_width_jitter | 0.144 [0.0746, 0.232] | 0 .. 0.35 |
| l_para_lines | 5 [0, 13.1] | 3 .. 15 |
| l_allo_per_glyph | 1.51 [0.724, 2.16] | 0.2 .. 3 |
| l_allo_rate | 0.0849 [0.0457, 0.109] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0.425] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.592 [0.342, 0.728] | 0.1 .. 0.9 |
| l_line_final_p | 0.159 [0, 0.347] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.635] | 0.3 .. 1 |
| p_alphabet | 17 [16, 19] | 15 .. 25 |
| p_n_slots | 6 [6, 6] | 3 .. 6 |
| p_slot_overlap | 0.0257 [0.00195, 0.0482] | 0 .. 1 |
| p_len_max | 1 [1, 1] | 1 .. 2 |
| p_zero_empty | 1 [1, 1] | 0 .. 1 |
| p_order | 2 [2, 2] | 0 .. 2 |

Kaynak dil (son nüfusta en sık): Romanian 18, Latin 16, Croatian 9, Italian 8, Greek 6

### slotgram: taze medyan mesafe 3.39, en iyi 1.94

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| n_symbols | -4.7 | 69.529 | 25.000 |
| vocab_ed1_density | +3.1 | 0.854 | 0.925 |
| zipf_slope | +3.1 | -0.776 | -0.642 |
| wlen_std | -2.9 | 1.469 | 1.289 |
| char_double_rate | +2.9 | 0.015 | 0.031 |
| wlen_autocorr1 | -2.9 | 0.179 | 0.009 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.21 [5.9, 9.91] | 5 .. 13 |
| l_width_jitter | 0.206 [0.0984, 0.303] | 0 .. 0.35 |
| l_para_lines | 7.3 [0, 10.3] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.32] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0637] | 0.01 .. 0.15 |
| l_final_forms_share | 0.567 [0.393, 0.825] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.12] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.326 [0, 0.57] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.378] | 0.1 .. 0.9 |
| l_para_initial_p | 0.384 [0, 0.732] | 0.3 .. 1 |
| p_alphabet | 22 [19, 24] | 15 .. 25 |
| p_n_slots | 7 [3.75, 8] | 3 .. 8 |
| p_slot_overlap | 0.411 [0.0318, 0.717] | 0 .. 1 |
| p_n_inv | 16 [9.75, 25.2] | 2 .. 30 |
| p_len_max | 1 [1, 2] | 1 .. 2 |
| p_empty | 0.485 [0.372, 0.534] | 0.1 .. 0.8 |
| p_copy | 0.3 [0, 0.45] | 0.3 .. 0.95 |
| p_exact | 0.194 [0.0605, 0.345] | 0 .. 0.5 |
| p_reach | 8 [2.75, 17] | 1 .. 30 |
| p_same_line | 0.103 [0.0457, 0.227] | 0 .. 0.5 |

### grille: taze medyan mesafe 3.44, en iyi 1.83

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +7.4 | 0.015 | 0.055 |
| n_symbols | -4.4 | 69.529 | 28.000 |
| wlen_autocorr1 | -3.1 | 0.179 | -0.006 |
| vocab_ed1_density | +2.7 | 0.854 | 0.915 |
| jsd_line_final | -2.7 | 0.133 | 0.018 |
| hapax_ratio | -2.5 | 0.741 | 0.668 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.52 [6.04, 10.3] | 5 .. 13 |
| l_width_jitter | 0.232 [0.154, 0.314] | 0 .. 0.35 |
| l_para_lines | 3.54 [0, 11.2] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.96] | 0.2 .. 3 |
| l_allo_rate | 0.0637 [0, 0.0958] | 0.01 .. 0.15 |
| l_final_forms_share | 0.451 [0.271, 0.639] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.377 [0, 0.684] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.301] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.725] | 0.3 .. 1 |
| p_alphabet | 23 [21, 24] | 15 .. 25 |
| p_rows | 1.08e+03 [566, 2.07e+03] | 60 .. 3000 |
| p_slot_overlap | 0.83 [0.573, 1] | 0 .. 1 |
| p_n_edge | 23 [13, 33] | 5 .. 40 |
| p_n_mid | 39 [21, 92.2] | 10 .. 120 |
| p_empty | 0.365 [0.295, 0.417] | 0 .. 0.6 |
| p_len_edge | 2 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_n_grilles | 5 [4, 7] | 3 .. 8 |

### slotcite: taze medyan mesafe 3.70, en iyi 1.51

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +8.7 | 0.015 | 0.062 |
| wlen_autocorr1 | -2.5 | 0.179 | 0.033 |
| rep_adjacent_exact | +2.4 | 0.006 | 0.012 |
| wlen_std | -2.3 | 1.469 | 1.328 |
| n_symbols | -2.3 | 69.529 | 48.000 |
| vocab_ed1_density | +2.2 | 0.854 | 0.905 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.05 [6, 11.2] | 5 .. 13 |
| l_width_jitter | 0.214 [0.119, 0.295] | 0 .. 0.35 |
| l_para_lines | 7.9 [3.29, 10.6] | 3 .. 15 |
| l_allo_per_glyph | 2.13 [1.47, 2.55] | 0.2 .. 3 |
| l_allo_rate | 0.11 [0.0523, 0.131] | 0.01 .. 0.15 |
| l_final_forms_share | 0.501 [0.3, 0.672] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.61 [0.399, 0.76] | 0.1 .. 0.9 |
| l_line_final_p | 0.363 [0.194, 0.477] | 0.1 .. 0.9 |
| l_para_initial_p | 0.15 [0, 0.762] | 0.3 .. 1 |
| p_alphabet | 18 [16, 22] | 15 .. 25 |
| p_slot_overlap | 0.628 [0.42, 0.804] | 0 .. 1 |
| p_n_edge | 21 [12.8, 31] | 5 .. 40 |
| p_n_mid | 41 [16.8, 92.8] | 10 .. 120 |
| p_empty | 0.391 [0.312, 0.458] | 0 .. 0.6 |
| p_len_edge | 2 [1, 2] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_copy | 0.586 [0.529, 0.675] | 0.5 .. 0.97 |
| p_exact | 0.241 [0.138, 0.393] | 0.1 .. 0.7 |
| p_reach | 8 [3, 16] | 1 .. 30 |
| p_same_line | 0.0947 [0.0207, 0.169] | 0 .. 0.5 |
| p_mut_prefix | 0.399 [0.283, 0.506] | 0 .. 1 |
| p_mut_mid | 0.393 [0.299, 0.591] | 0 .. 1 |
| p_mut_suffix | 0.195 [0.0686, 0.352] | 0 .. 1 |


## zl_basic: sınıf sınıf

### slotcite: taze medyan mesafe 2.86, en iyi 2.01

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -2.9 | 0.715 | 0.622 |
| h2_over_h1 | +2.9 | 0.521 | 0.617 |
| h2 | +2.6 | 2.013 | 2.371 |
| zipf_slope | +2.4 | -0.785 | -0.623 |
| jsd_line_final | -2.2 | 0.110 | 0.027 |
| n_symbols | -2.0 | 40.438 | 22.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.09 [6.5, 11.3] | 5 .. 13 |
| l_width_jitter | 0.155 [0.0437, 0.255] | 0 .. 0.35 |
| l_para_lines | 5.07 [0, 8.79] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.525] | 0.2 .. 3 |
| l_allo_rate | 0.005 [0, 0.0708] | 0.01 .. 0.15 |
| l_final_forms_share | 0.714 [0.548, 0.827] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3.25] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0.5 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.328 [0, 0.542] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.239] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0] | 0.3 .. 1 |
| p_alphabet | 18 [16, 20] | 15 .. 25 |
| p_slot_overlap | 0.505 [0.239, 0.841] | 0 .. 1 |
| p_n_edge | 29 [23, 38] | 5 .. 40 |
| p_n_mid | 20.5 [13, 48.2] | 10 .. 120 |
| p_empty | 0.251 [0.206, 0.303] | 0 .. 0.6 |
| p_len_edge | 3 [3, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_copy | 0.642 [0.524, 0.753] | 0.5 .. 0.97 |
| p_exact | 0.173 [0.108, 0.261] | 0.1 .. 0.7 |
| p_reach | 8 [4, 15] | 1 .. 30 |
| p_same_line | 0.0937 [0.0213, 0.15] | 0 .. 0.5 |
| p_mut_prefix | 0.406 [0.228, 0.558] | 0 .. 1 |
| p_mut_mid | 0.199 [0.047, 0.558] | 0 .. 1 |
| p_mut_suffix | 0.417 [0.183, 0.598] | 0 .. 1 |

### grille: taze medyan mesafe 2.94, en iyi 1.76

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -2.7 | 0.123 | -0.004 |
| h2_over_h1 | +2.6 | 0.521 | 0.608 |
| rep_adjacent_ed1 | -2.4 | 0.034 | 0.017 |
| h2 | +2.4 | 2.013 | 2.347 |
| hapax_ratio | -2.2 | 0.715 | 0.646 |
| vocab_ed1_density | +2.1 | 0.823 | 0.869 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.04 [5.95, 10.1] | 5 .. 13 |
| l_width_jitter | 0.188 [0.088, 0.28] | 0 .. 0.35 |
| l_para_lines | 4.38 [0, 7.34] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.2] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.568 [0.452, 0.727] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.304 [0, 0.519] | 0.1 .. 0.9 |
| l_line_final_p | 0.255 [0, 0.413] | 0.1 .. 0.9 |
| l_para_initial_p | 0.456 [0, 0.77] | 0.3 .. 1 |
| p_alphabet | 22 [19, 23] | 15 .. 25 |
| p_rows | 790 [542, 1.38e+03] | 60 .. 3000 |
| p_slot_overlap | 0.337 [0.162, 0.642] | 0 .. 1 |
| p_n_edge | 30 [19.8, 40] | 5 .. 40 |
| p_n_mid | 22.5 [12, 36.2] | 10 .. 120 |
| p_empty | 0.344 [0.287, 0.394] | 0 .. 0.6 |
| p_len_edge | 3 [2.75, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_n_grilles | 6 [4, 8] | 3 .. 8 |

### verbose: taze medyan mesafe 3.25, en iyi 2.35

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +4.9 | 1.768 | 2.067 |
| wlen_skew | +4.3 | 0.025 | 0.465 |
| hapax_ratio | -3.6 | 0.715 | 0.600 |
| wlen_autocorr1 | -3.4 | 0.123 | -0.039 |
| wlen_frac_le2 | +3.4 | 0.097 | 0.142 |
| jsd_last | -3.3 | 0.712 | 0.560 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.4 [5.41, 11] | 5 .. 13 |
| l_width_jitter | 0.262 [0.191, 0.333] | 0 .. 0.35 |
| l_para_lines | 4.35 [0, 11.3] | 3 .. 15 |
| l_allo_per_glyph | 1.32 [0.429, 1.89] | 0.2 .. 3 |
| l_allo_rate | 0.0451 [0.0229, 0.0638] | 0.01 .. 0.15 |
| l_final_forms_share | 0.357 [0, 0.533] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.22 [0, 0.378] | 0.1 .. 0.9 |
| l_line_final_p | 0.162 [0, 0.385] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0] | 0.3 .. 1 |
| p_alphabet | 15 [13, 16.2] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.395 [0.326, 0.467] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 60, Romanian 23, Czech 5, Croatian 4, Finnish 3

### selfcite: taze medyan mesafe 3.41, en iyi 2.55

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| vocab_ed1_density | +5.0 | 0.823 | 0.931 |
| char_double_rate | +5.0 | 0.066 | 0.141 |
| h2_over_h1 | +4.9 | 0.521 | 0.685 |
| h2 | +4.7 | 2.013 | 2.671 |
| first_entropy_ratio | +4.0 | 0.817 | 0.885 |
| hapax_ratio | -4.0 | 0.715 | 0.587 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 11.2 [9.07, 12.4] | 5 .. 13 |
| l_width_jitter | 0.18 [0.102, 0.262] | 0 .. 0.35 |
| l_para_lines | 9.61 [0, 11.6] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.14] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0398] | 0.01 .. 0.15 |
| l_final_forms_share | 0.693 [0.529, 0.871] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.275] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.1 [0, 0.545] | 0.1 .. 0.9 |
| l_line_final_p | 0.132 [0, 0.283] | 0.1 .. 0.9 |
| l_para_initial_p | 0.584 [0, 0.774] | 0.3 .. 1 |
| p_alphabet | 17 [15, 19] | 15 .. 25 |
| p_glyph_classes | 6 [5, 7] | 4 .. 7 |
| p_copy | 0.905 [0.886, 0.938] | 0.85 .. 0.97 |
| p_exact | 0.48 [0.39, 0.565] | 0.2 .. 0.8 |
| p_reach | 24.5 [21, 29] | 1 .. 30 |
| p_same_line | 0.018 [0.00337, 0.0312] | 0 .. 0.3 |
| p_slot_overlap | 0.399 [0.212, 0.623] | 0 .. 1 |
| p_affix | 0.79 [0.719, 0.874] | 0.3 .. 0.9 |
| p_mut_substitute | 0.42 [0.264, 0.56] | 0 .. 1 |
| p_mut_prefix | 0.442 [0.298, 0.636] | 0 .. 1 |
| p_mut_delete | 0.0612 [0.00307, 0.12] | 0 .. 1 |
| p_mut_double | 0.141 [0.0842, 0.2] | 0 .. 1 |

### slotgram: taze medyan mesafe 3.47, en iyi 2.09

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| zipf_slope | +3.8 | -0.785 | -0.524 |
| vocab_ed1_density | +3.2 | 0.823 | 0.891 |
| h2_over_h1 | +2.7 | 0.521 | 0.610 |
| top10_coverage | -2.4 | 0.175 | 0.086 |
| wlen_autocorr1 | -2.3 | 0.123 | 0.017 |
| n_symbols | -2.2 | 40.438 | 20.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.08 [6.53, 11.4] | 5 .. 13 |
| l_width_jitter | 0.172 [0.0747, 0.316] | 0 .. 0.35 |
| l_para_lines | 0 [0, 9.17] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.87] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0604] | 0.01 .. 0.15 |
| l_final_forms_share | 0.537 [0.283, 0.725] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.396 [0, 0.622] | 0.1 .. 0.9 |
| l_line_final_p | 0.184 [0, 0.322] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.527] | 0.3 .. 1 |
| p_alphabet | 20 [17, 23] | 15 .. 25 |
| p_n_slots | 5 [5, 6] | 3 .. 8 |
| p_slot_overlap | 0.553 [0.287, 0.732] | 0 .. 1 |
| p_n_inv | 5 [3, 8] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.41 [0.326, 0.492] | 0.1 .. 0.8 |
| p_copy | 0.415 [0, 0.626] | 0.3 .. 0.95 |
| p_exact | 0.116 [0.0136, 0.221] | 0 .. 0.5 |
| p_reach | 9 [4, 19] | 1 .. 30 |
| p_same_line | 0.125 [0.0368, 0.251] | 0 .. 0.5 |

### plain: taze medyan mesafe 3.67, en iyi 3.14

Voynich'ten 2 birimden fazla sapan feature sayısı: 21

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -8.2 | 0.636 | 0.097 |
| h2 | +5.5 | 2.013 | 2.780 |
| jsd_last | +5.5 | 0.712 | 0.963 |
| h2_over_h1 | +5.4 | 0.521 | 0.704 |
| first_entropy_ratio | +5.1 | 0.817 | 0.903 |
| eff_symbols | +4.6 | 14.493 | 16.317 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.19 [5.66, 9.25] | 5 .. 13 |
| l_width_jitter | 0.132 [0.0469, 0.264] | 0 .. 0.35 |
| l_para_lines | 4.95 [0, 9.36] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.934 [0.869, 0.983] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0.1 [0, 0.171] | 0.1 .. 1 |
| l_initial_forms_k | 1 [1, 2] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.21] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0.49 [0.3, 0.787] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Arabic 73, Hebrew 27

### codebook: taze medyan mesafe 4.42, en iyi 3.25

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | -13.0 | 1.768 | 0.978 |
| type_len_mean | -10.2 | 5.640 | 3.793 |
| vocab_ed1_density | +7.8 | 0.823 | 0.991 |
| wlen_mean | -5.6 | 4.961 | 3.696 |
| first_entropy_ratio | -4.1 | 0.817 | 0.747 |
| wlen_skew | -3.7 | 0.025 | -0.354 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.6 [7.88, 12.3] | 5 .. 13 |
| l_width_jitter | 0.256 [0.185, 0.342] | 0 .. 0.35 |
| l_para_lines | 7.56 [0, 12.2] | 3 .. 15 |
| l_allo_per_glyph | 1.22 [0, 2.35] | 0.2 .. 3 |
| l_allo_rate | 0.0511 [0, 0.114] | 0.01 .. 0.15 |
| l_final_forms_share | 0.398 [0, 0.687] | 0.1 .. 1 |
| l_final_forms_k | 2 [0, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.58 [0.405, 0.69] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.336] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.61] | 0.3 .. 1 |
| p_alphabet | 17 [16, 19] | 15 .. 25 |
| p_n_slots | 6 [5, 6] | 3 .. 6 |
| p_slot_overlap | 0.00756 [0, 0.0301] | 0 .. 1 |
| p_len_max | 1 [1, 2] | 1 .. 2 |
| p_zero_empty | 1 [1, 1] | 0 .. 1 |
| p_order | 2 [2, 2] | 0 .. 2 |

Kaynak dil (son nüfusta en sık): Croatian 27, Russian 20, Arabic 13, Romanian 9, Swedish 8

### abjad: taze medyan mesafe 5.03, en iyi 3.81

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +17.7 | 0.097 | 0.334 |
| wlen_frac1 | +7.7 | 0.033 | 0.112 |
| wlen_mean | -7.0 | 4.961 | 3.377 |
| type_len_mean | -6.7 | 5.640 | 4.430 |
| wlen_skew | +6.3 | 0.025 | 0.672 |
| h2_over_h1 | +5.0 | 0.521 | 0.690 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.85 [5.77, 9.94] | 5 .. 13 |
| l_width_jitter | 0.108 [0.0389, 0.205] | 0 .. 0.35 |
| l_para_lines | 5.33 [0, 11.3] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0194] | 0.01 .. 0.15 |
| l_final_forms_share | 0.794 [0.648, 0.933] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.452 [0.363, 0.495] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 3] | 0 .. 4 |
| l_line_initial_p | 0.251 [0, 0.51] | 0.1 .. 0.9 |
| l_line_final_p | 0.192 [0, 0.385] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.704] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100


## zl_glyph: sınıf sınıf

### slotcite: taze medyan mesafe 2.56, en iyi 1.45

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -2.6 | 0.715 | 0.631 |
| jsd_line_final | -2.6 | 0.110 | 0.013 |
| n_symbols | -2.3 | 44.750 | 23.000 |
| h2_over_h1 | +2.1 | 0.554 | 0.640 |
| h2 | +2.1 | 2.127 | 2.488 |
| vocab_ed1_density | +2.1 | 0.852 | 0.885 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.71 [6.1, 9.45] | 5 .. 13 |
| l_width_jitter | 0.182 [0.122, 0.241] | 0 .. 0.35 |
| l_para_lines | 4.16 [0, 9.64] | 3 .. 15 |
| l_allo_per_glyph | 0.294 [0, 1.59] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0324] | 0.01 .. 0.15 |
| l_final_forms_share | 0.627 [0.52, 0.761] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.384 [0.209, 0.534] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.214] | 0.1 .. 0.9 |
| l_para_initial_p | 0.425 [0, 0.699] | 0.3 .. 1 |
| p_alphabet | 19 [16.8, 21.2] | 15 .. 25 |
| p_slot_overlap | 0.566 [0.339, 0.857] | 0 .. 1 |
| p_n_edge | 32.5 [25, 39] | 5 .. 40 |
| p_n_mid | 45 [22.8, 94.2] | 10 .. 120 |
| p_empty | 0.291 [0.22, 0.353] | 0 .. 0.6 |
| p_len_edge | 3 [3, 3] | 1 .. 3 |
| p_len_mid | 2.5 [2, 3] | 2 .. 5 |
| p_copy | 0.619 [0.536, 0.68] | 0.5 .. 0.97 |
| p_exact | 0.221 [0.122, 0.311] | 0.1 .. 0.7 |
| p_reach | 9 [5, 16] | 1 .. 30 |
| p_same_line | 0.0743 [0.0303, 0.137] | 0 .. 0.5 |
| p_mut_prefix | 0.291 [0.137, 0.548] | 0 .. 1 |
| p_mut_mid | 0.329 [0.141, 0.567] | 0 .. 1 |
| p_mut_suffix | 0.439 [0.232, 0.632] | 0 .. 1 |

### grille: taze medyan mesafe 2.56, en iyi 1.47

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -2.6 | 0.102 | -0.003 |
| vocab_ed1_density | +2.5 | 0.852 | 0.893 |
| jsd_line_initial | -2.4 | 0.266 | 0.046 |
| n_symbols | -2.4 | 44.750 | 22.000 |
| jsd_line_final | -2.4 | 0.110 | 0.020 |
| h2_over_h1 | +2.0 | 0.554 | 0.637 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.78 [8.18, 11.1] | 5 .. 13 |
| l_width_jitter | 0.173 [0.11, 0.24] | 0 .. 0.35 |
| l_para_lines | 4.63 [0, 8.63] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.721] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0908] | 0.01 .. 0.15 |
| l_final_forms_share | 0.591 [0.479, 0.667] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.403] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.252] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.3] | 0.3 .. 1 |
| p_alphabet | 20 [18, 22] | 15 .. 25 |
| p_rows | 1.96e+03 [1.02e+03, 2.79e+03] | 60 .. 3000 |
| p_slot_overlap | 0.384 [0.148, 0.584] | 0 .. 1 |
| p_n_edge | 23 [17.8, 34] | 5 .. 40 |
| p_n_mid | 55 [29.8, 85] | 10 .. 120 |
| p_empty | 0.391 [0.337, 0.465] | 0 .. 0.6 |
| p_len_edge | 2 [2, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_n_grilles | 5.5 [4, 7] | 3 .. 8 |

### selfcite: taze medyan mesafe 2.62, en iyi 1.98

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| vocab_ed1_density | +4.6 | 0.852 | 0.926 |
| hapax_ratio | -3.9 | 0.715 | 0.590 |
| h2_over_h1 | +3.8 | 0.554 | 0.709 |
| h2 | +3.6 | 2.127 | 2.756 |
| char_double_rate | +2.5 | 0.076 | 0.116 |
| zipf_slope | +2.3 | -0.785 | -0.631 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.88 [7.77, 12.3] | 5 .. 13 |
| l_width_jitter | 0.271 [0.154, 0.326] | 0 .. 0.35 |
| l_para_lines | 8.53 [3, 11.8] | 3 .. 15 |
| l_allo_per_glyph | 0.149 [0, 1.45] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.655 [0.515, 0.765] | 0.1 .. 1 |
| l_final_forms_k | 2 [1.75, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.473 [0.305, 0.577] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.198] | 0.1 .. 0.9 |
| l_para_initial_p | 0.573 [0, 0.844] | 0.3 .. 1 |
| p_alphabet | 18.5 [17, 20] | 15 .. 25 |
| p_glyph_classes | 5 [4, 7] | 4 .. 7 |
| p_copy | 0.868 [0.857, 0.891] | 0.85 .. 0.97 |
| p_exact | 0.428 [0.361, 0.532] | 0.2 .. 0.8 |
| p_reach | 22 [17.8, 27] | 1 .. 30 |
| p_same_line | 0.017 [0.00597, 0.0319] | 0 .. 0.3 |
| p_slot_overlap | 0.189 [0.0774, 0.329] | 0 .. 1 |
| p_affix | 0.701 [0.633, 0.773] | 0.3 .. 0.9 |
| p_mut_substitute | 0.302 [0.124, 0.457] | 0 .. 1 |
| p_mut_prefix | 0.595 [0.458, 0.796] | 0 .. 1 |
| p_mut_delete | 0.0833 [0.0329, 0.142] | 0 .. 1 |
| p_mut_double | 0.0895 [0.0498, 0.147] | 0 .. 1 |

### plain: taze medyan mesafe 2.93, en iyi 2.46

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | -5.7 | 1.615 | 1.301 |
| last_entropy_ratio | -5.2 | 0.636 | 0.315 |
| vocab_ed1_density | -4.8 | 0.852 | 0.775 |
| h2 | +4.4 | 2.127 | 2.900 |
| h2_over_h1 | +4.4 | 0.554 | 0.735 |
| char_double_rate | -4.2 | 0.076 | 0.009 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.75 [6.73, 10.9] | 5 .. 13 |
| l_width_jitter | 0.21 [0.11, 0.295] | 0 .. 0.35 |
| l_para_lines | 0 [0, 6.18] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.782 [0.727, 0.852] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.265] | 0.1 .. 0.9 |
| l_line_final_p | 0.122 [0, 0.299] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.633] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### slotgram: taze medyan mesafe 2.93, en iyi 1.79

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| vocab_ed1_density | +2.5 | 0.852 | 0.893 |
| jsd_line_final | -2.5 | 0.110 | 0.015 |
| n_symbols | -2.5 | 44.750 | 21.000 |
| wlen_autocorr1 | -2.4 | 0.102 | 0.008 |
| h2_over_h1 | +1.9 | 0.554 | 0.633 |
| zipf_slope | +1.9 | -0.785 | -0.656 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.29 [7.36, 11.7] | 5 .. 13 |
| l_width_jitter | 0.101 [0.0463, 0.202] | 0 .. 0.35 |
| l_para_lines | 4.75 [0, 7.92] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.683] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.062] | 0.01 .. 0.15 |
| l_final_forms_share | 0.621 [0.387, 0.758] | 0.1 .. 1 |
| l_final_forms_k | 2 [0, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.288 [0, 0.675] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.22] | 0.1 .. 0.9 |
| l_para_initial_p | 0.3 [0, 0.578] | 0.3 .. 1 |
| p_alphabet | 18 [16, 20] | 15 .. 25 |
| p_n_slots | 5 [4, 5] | 3 .. 8 |
| p_slot_overlap | 0.266 [0.0447, 0.539] | 0 .. 1 |
| p_n_inv | 10 [6, 17.2] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.429 [0.375, 0.49] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0.075] | 0.3 .. 0.95 |
| p_exact | 0.251 [0.111, 0.416] | 0 .. 0.5 |
| p_reach | 8 [3, 20.2] | 1 .. 30 |
| p_same_line | 0.107 [0.0385, 0.235] | 0 .. 0.5 |

### verbose: taze medyan mesafe 2.95, en iyi 1.72

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +6.5 | 1.615 | 1.974 |
| wlen_skew | +3.1 | 0.154 | 0.473 |
| wlen_frac1 | +3.1 | 0.033 | 0.066 |
| wlen_autocorr1 | -3.1 | 0.102 | -0.021 |
| rep_adjacent_exact | -2.6 | 0.008 | 0.002 |
| jsd_last | -2.5 | 0.712 | 0.598 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.07 [5.46, 10.4] | 5 .. 13 |
| l_width_jitter | 0.176 [0.0988, 0.268] | 0 .. 0.35 |
| l_para_lines | 4.39 [0, 9.26] | 3 .. 15 |
| l_allo_per_glyph | 2.12 [1.08, 2.62] | 0.2 .. 3 |
| l_allo_rate | 0.064 [0.0336, 0.0804] | 0.01 .. 0.15 |
| l_final_forms_share | 0.365 [0.255, 0.527] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.216 [0, 0.703] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.301] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.559] | 0.3 .. 1 |
| p_alphabet | 14 [12, 15] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.58 [0.462, 0.681] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 56, Romanian 28, Croatian 9, Czech 3, Russian 2

### abjad: taze medyan mesafe 3.25, en iyi 2.65

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +7.3 | 0.033 | 0.111 |
| wlen_frac_le2 | +6.5 | 0.119 | 0.336 |
| wlen_skew | +5.2 | 0.154 | 0.682 |
| vocab_ed1_density | -4.0 | 0.852 | 0.788 |
| h2_over_h1 | +3.9 | 0.554 | 0.714 |
| h2 | +3.7 | 2.127 | 2.774 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.22 [5, 7.94] | 5 .. 13 |
| l_width_jitter | 0.257 [0.158, 0.303] | 0 .. 0.35 |
| l_para_lines | 4.21 [0, 7.63] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.778 [0.697, 0.852] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.297 [0, 0.401] | 0.1 .. 1 |
| l_initial_forms_k | 1 [1, 2] | 0 .. 4 |
| l_line_initial_p | 0.201 [0, 0.534] | 0.1 .. 0.9 |
| l_line_final_p | 0.249 [0, 0.353] | 0.1 .. 0.9 |
| l_para_initial_p | 0.3 [0, 0.582] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100

### codebook: taze medyan mesafe 3.47, en iyi 2.06

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| vocab_ed1_density | +7.3 | 0.852 | 0.969 |
| wlen_std | -7.2 | 1.615 | 1.216 |
| type_len_mean | -3.8 | 4.989 | 4.098 |
| first_entropy_ratio | -3.3 | 0.875 | 0.792 |
| wlen_skew | -3.2 | 0.154 | -0.168 |
| rep_adjacent_exact | -3.0 | 0.008 | 0.001 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.79 [6.8, 11.8] | 5 .. 13 |
| l_width_jitter | 0.085 [0.00302, 0.205] | 0 .. 0.35 |
| l_para_lines | 0 [0, 8.12] | 3 .. 15 |
| l_allo_per_glyph | 2.47 [1.87, 2.91] | 0.2 .. 3 |
| l_allo_rate | 0.11 [0.07, 0.135] | 0.01 .. 0.15 |
| l_final_forms_share | 0.658 [0.459, 0.915] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.474] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.497] | 0.3 .. 1 |
| p_alphabet | 15 [15, 16] | 15 .. 25 |
| p_n_slots | 5 [5, 6] | 3 .. 6 |
| p_slot_overlap | 0.0125 [0, 0.0387] | 0 .. 1 |
| p_len_max | 2 [1, 2] | 1 .. 2 |
| p_zero_empty | 1 [1, 1] | 0 .. 1 |
| p_order | 1 [0, 2] | 0 .. 2 |

Kaynak dil (son nüfusta en sık): Turkish 29, Croatian 11, Russian 11, Czech 8, Swedish 7
