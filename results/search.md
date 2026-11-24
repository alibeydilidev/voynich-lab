# Yönlendirilmiş arama raporu: her hipotezin ulaşabildiği en iyi nokta

Her (sınıf, görünüm) için 5 tur, tur başına 600 deneme, en yakın 100 ayar tutuldu. Tablolardaki mesafeler, son turda kalan ayarların her biriyle yeniden üretilen 2 taze örnekten hesaplandı (toplam 200).

Mesafe birimi ve ölçüt `abc.md` ile aynı: bir hipotezin taze örnekleri Voynich öz mesafesinin içine giriyorsa, o hipotez bu feature kümesinde Voynich'ten ayırt edilemez.

## 1. Taze örneklerin medyan mesafesi (parantezde rejection ABC'deki değer)

| görünüm | Voynich öz mesafesi (medyan, en çok) | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.91, 1.65 | 5.94 (6.10) | 4.00 (3.49) | 4.32 (4.71) | 3.23 (2.86) | 4.05 (5.31) | 3.52 (4.44) | 3.28 (3.09) | 3.76 (3.36) | 3.82 (4.02) |
| eva_glyph | 0.96, 1.64 | 3.58 (4.01) | 3.90 (3.48) | 3.97 (4.28) | 2.80 (2.56) | 3.02 (4.08) | 2.91 (3.52) | 2.76 (2.85) | 3.25 (2.93) | 3.57 (3.55) |
| v101 | 0.96, 1.40 | 2.92 (3.25) | 3.58 (2.96) | 3.41 (3.91) | 3.74 (2.62) | 2.66 (3.03) | 3.33 (3.81) | 3.81 (2.96) | 3.35 (2.84) | 3.37 (3.37) |
| zl_basic | 0.95, 1.51 | 5.02 (5.34) | 4.23 (3.38) | 4.35 (4.73) | 2.95 (2.49) | 3.68 (4.60) | 3.29 (3.92) | 3.11 (2.64) | 3.20 (2.97) | 3.24 (3.33) |
| zl_glyph | 1.03, 1.43 | 3.29 (3.58) | 3.74 (3.07) | 3.26 (4.03) | 2.56 (2.18) | 3.00 (3.72) | 2.64 (3.11) | 2.51 (2.33) | 2.79 (2.53) | 2.90 (2.96) |

## 2. Voynich'in en uç penceresi kadar yakın olan taze örneklerin oranı

| görünüm | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|
| eva_basic | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 |
| eva_glyph | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 |
| v101 | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 |
| zl_basic | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 |
| zl_glyph | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 | %0 |

## 3. Arama yakınsadı mı (tur tur, tutulan ayarların medyan mesafesi)

| görünüm | sınıf | turlar |
|---|---|---|
| eva_basic | abjad | 5.97 -> 5.71 -> 5.57 -> 5.48 -> 5.42 |
| eva_basic | automaton | 3.62 -> 3.40 -> 3.23 -> 3.18 -> 3.16 |
| eva_basic | codebook | 4.68 -> 4.40 -> 4.29 -> 4.13 -> 4.04 |
| eva_basic | grille | 2.96 -> 2.80 -> 2.78 -> 2.64 -> 2.66 |
| eva_basic | plain | 4.79 -> 4.05 -> 3.92 -> 3.85 -> 3.80 |
| eva_basic | selfcite | 3.95 -> 3.66 -> 3.47 -> 3.33 -> 3.26 |
| eva_basic | slotcite | 3.08 -> 2.92 -> 2.82 -> 2.73 -> 2.71 |
| eva_basic | slotgram | 3.37 -> 3.21 -> 3.19 -> 3.13 -> 3.20 |
| eva_basic | verbose | 3.74 -> 3.56 -> 3.53 -> 3.43 -> 3.40 |
| eva_glyph | abjad | 3.77 -> 3.48 -> 3.39 -> 3.34 -> 3.29 |
| eva_glyph | automaton | 3.63 -> 3.53 -> 3.33 -> 3.29 -> 3.17 |
| eva_glyph | codebook | 4.21 -> 4.08 -> 3.84 -> 3.75 -> 3.64 |
| eva_glyph | grille | 2.68 -> 2.51 -> 2.43 -> 2.36 -> 2.24 |
| eva_glyph | plain | 3.53 -> 3.10 -> 2.89 -> 2.84 -> 2.77 |
| eva_glyph | selfcite | 3.22 -> 3.02 -> 2.80 -> 2.72 -> 2.63 |
| eva_glyph | slotcite | 2.80 -> 2.68 -> 2.63 -> 2.51 -> 2.46 |
| eva_glyph | slotgram | 3.07 -> 2.92 -> 2.91 -> 2.89 -> 2.91 |
| eva_glyph | verbose | 3.57 -> 3.42 -> 3.35 -> 3.22 -> 3.11 |
| v101 | abjad | 2.99 -> 2.80 -> 2.72 -> 2.70 -> 2.66 |
| v101 | automaton | 3.15 -> 3.04 -> 2.91 -> 2.83 -> 2.85 |
| v101 | codebook | 3.86 -> 3.64 -> 3.47 -> 3.33 -> 3.22 |
| v101 | grille | 2.83 -> 2.93 -> 2.85 -> 2.74 -> 2.79 |
| v101 | plain | 2.75 -> 2.47 -> 2.45 -> 2.39 -> 2.41 |
| v101 | selfcite | 3.55 -> 3.26 -> 3.14 -> 3.01 -> 2.99 |
| v101 | slotcite | 3.18 -> 3.06 -> 2.99 -> 2.92 -> 2.93 |
| v101 | slotgram | 3.15 -> 2.92 -> 2.98 -> 2.85 -> 2.82 |
| v101 | verbose | 3.33 -> 3.05 -> 3.08 -> 2.89 -> 2.88 |
| zl_basic | abjad | 5.11 -> 4.85 -> 4.72 -> 4.56 -> 4.56 |
| zl_basic | automaton | 3.67 -> 3.46 -> 3.37 -> 3.32 -> 3.22 |
| zl_basic | codebook | 4.68 -> 4.52 -> 4.34 -> 4.16 -> 4.03 |
| zl_basic | grille | 2.69 -> 2.62 -> 2.52 -> 2.53 -> 2.40 |
| zl_basic | plain | 4.02 -> 3.67 -> 3.57 -> 3.50 -> 3.51 |
| zl_basic | selfcite | 3.64 -> 3.35 -> 3.20 -> 3.08 -> 3.03 |
| zl_basic | slotcite | 2.88 -> 2.70 -> 2.68 -> 2.57 -> 2.51 |
| zl_basic | slotgram | 3.07 -> 2.92 -> 2.77 -> 2.78 -> 2.75 |
| zl_basic | verbose | 3.19 -> 3.11 -> 2.97 -> 2.88 -> 2.87 |
| zl_glyph | abjad | 3.39 -> 3.20 -> 3.00 -> 3.01 -> 2.95 |
| zl_glyph | automaton | 3.33 -> 3.16 -> 2.99 -> 2.93 -> 2.95 |
| zl_glyph | codebook | 3.99 -> 3.75 -> 3.49 -> 3.23 -> 3.04 |
| zl_glyph | grille | 2.29 -> 2.21 -> 2.20 -> 2.12 -> 2.08 |
| zl_glyph | plain | 3.18 -> 2.87 -> 2.81 -> 2.79 -> 2.77 |
| zl_glyph | selfcite | 2.91 -> 2.80 -> 2.61 -> 2.43 -> 2.41 |
| zl_glyph | slotcite | 2.48 -> 2.28 -> 2.26 -> 2.20 -> 2.08 |
| zl_glyph | slotgram | 2.77 -> 2.51 -> 2.49 -> 2.42 -> 2.35 |
| zl_glyph | verbose | 2.95 -> 2.81 -> 2.69 -> 2.59 -> 2.62 |

## eva_basic: sınıf sınıf

### grille: taze medyan mesafe 3.23, en iyi 1.94

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -3.5 | 0.127 | -0.005 |
| h2_over_h1 | +3.3 | 0.524 | 0.626 |
| h2 | +3.2 | 2.016 | 2.397 |
| jsd_line_final | -3.0 | 0.109 | 0.012 |
| edge_mi | -2.8 | 0.179 | -0.004 |
| rep_adjacent_ed1 | -2.6 | 0.032 | 0.015 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.5 [8.18, 12.2] | 5 .. 13 |
| l_width_jitter | 0.202 [0.138, 0.321] | 0 .. 0.35 |
| l_para_lines | 3 [0, 8.46] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.514 [0.36, 0.653] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.312] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.184] | 0.1 .. 0.9 |
| l_para_initial_p | 0.372 [0, 0.713] | 0.3 .. 1 |
| p_alphabet | 19 [17.8, 21] | 15 .. 25 |
| p_rows | 1.41e+03 [648, 2.63e+03] | 60 .. 3000 |
| p_slot_overlap | 0.497 [0.192, 0.755] | 0 .. 1 |
| p_n_edge | 26 [19, 34] | 5 .. 40 |
| p_n_mid | 28 [18, 52] | 10 .. 120 |
| p_empty | 0.262 [0.207, 0.306] | 0 .. 0.6 |
| p_len_edge | 3 [3, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_n_grilles | 5 [4, 6] | 3 .. 8 |

### slotcite: taze medyan mesafe 3.28, en iyi 2.10

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -4.5 | 0.717 | 0.617 |
| h2_over_h1 | +3.5 | 0.524 | 0.632 |
| h2 | +3.4 | 2.016 | 2.423 |
| zipf_slope | +2.9 | -0.778 | -0.594 |
| edge_mi | -2.9 | 0.179 | -0.007 |
| vocab_ed1_density | +2.7 | 0.823 | 0.890 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.13 [5.97, 8.44] | 5 .. 13 |
| l_width_jitter | 0.201 [0.071, 0.302] | 0 .. 0.35 |
| l_para_lines | 5.55 [0, 11.2] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.613 [0.475, 0.773] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.556 [0.359, 0.723] | 0.1 .. 0.9 |
| l_line_final_p | 0.142 [0, 0.273] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.748] | 0.3 .. 1 |
| p_alphabet | 19 [17, 21] | 15 .. 25 |
| p_slot_overlap | 0.589 [0.439, 0.779] | 0 .. 1 |
| p_n_edge | 31 [23, 39] | 5 .. 40 |
| p_n_mid | 19 [13, 40.2] | 10 .. 120 |
| p_empty | 0.2 [0.151, 0.281] | 0 .. 0.6 |
| p_len_edge | 3 [3, 3] | 1 .. 3 |
| p_len_mid | 3 [2.75, 4] | 2 .. 5 |
| p_copy | 0.634 [0.55, 0.777] | 0.5 .. 0.97 |
| p_exact | 0.2 [0.116, 0.296] | 0.1 .. 0.7 |
| p_reach | 11.5 [5, 24.2] | 1 .. 30 |
| p_same_line | 0.0991 [0.0337, 0.192] | 0 .. 0.5 |
| p_mut_prefix | 0.252 [0.147, 0.383] | 0 .. 1 |
| p_mut_mid | 0.418 [0.195, 0.647] | 0 .. 1 |
| p_mut_suffix | 0.345 [0.164, 0.501] | 0 .. 1 |

### selfcite: taze medyan mesafe 3.52, en iyi 2.76

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -6.3 | 0.717 | 0.578 |
| h2 | +5.9 | 2.016 | 2.731 |
| h2_over_h1 | +5.8 | 0.524 | 0.704 |
| vocab_ed1_density | +4.5 | 0.823 | 0.935 |
| char_double_rate | +4.5 | 0.067 | 0.128 |
| type_len_mean | -4.4 | 5.692 | 4.943 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.5 [8.79, 12.2] | 5 .. 13 |
| l_width_jitter | 0.163 [0.0904, 0.219] | 0 .. 0.35 |
| l_para_lines | 9.08 [0, 11.4] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.05] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.598 [0.476, 0.674] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.33] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 3] | 0 .. 4 |
| l_line_initial_p | 0.38 [0, 0.549] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.588] | 0.3 .. 1 |
| p_alphabet | 17.5 [16, 19] | 15 .. 25 |
| p_glyph_classes | 5 [4.75, 6] | 4 .. 7 |
| p_copy | 0.871 [0.857, 0.897] | 0.85 .. 0.97 |
| p_exact | 0.387 [0.264, 0.524] | 0.2 .. 0.8 |
| p_reach | 22 [18, 28] | 1 .. 30 |
| p_same_line | 0.0253 [0.00352, 0.0506] | 0 .. 0.3 |
| p_slot_overlap | 0.163 [0, 0.284] | 0 .. 1 |
| p_affix | 0.86 [0.795, 0.9] | 0.3 .. 0.9 |
| p_mut_substitute | 0.437 [0.264, 0.669] | 0 .. 1 |
| p_mut_prefix | 0.556 [0.383, 0.732] | 0 .. 1 |
| p_mut_delete | 0.0415 [0.00651, 0.0775] | 0 .. 1 |
| p_mut_double | 0.142 [0.0572, 0.208] | 0 .. 1 |

### slotgram: taze medyan mesafe 3.76, en iyi 1.91

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| zipf_slope | +3.8 | -0.778 | -0.540 |
| h2_over_h1 | +3.3 | 0.524 | 0.626 |
| h2 | +3.0 | 2.016 | 2.378 |
| wlen_autocorr1 | -3.0 | 0.127 | 0.014 |
| edge_mi | -2.8 | 0.179 | -0.004 |
| jsd_last | -2.5 | 0.719 | 0.599 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.87 [6.68, 9.89] | 5 .. 13 |
| l_width_jitter | 0.166 [0.105, 0.234] | 0 .. 0.35 |
| l_para_lines | 0 [0, 0] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.445 [0.147, 0.63] | 0.1 .. 1 |
| l_final_forms_k | 1.5 [0.75, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.269 [0, 0.628] | 0.1 .. 0.9 |
| l_line_final_p | 0.118 [0, 0.311] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.379] | 0.3 .. 1 |
| p_alphabet | 19 [18, 21] | 15 .. 25 |
| p_n_slots | 5 [5, 6] | 3 .. 8 |
| p_slot_overlap | 0.494 [0.154, 0.715] | 0 .. 1 |
| p_n_inv | 8 [5, 11] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.389 [0.325, 0.452] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0.686] | 0.3 .. 0.95 |
| p_exact | 0.213 [0.0793, 0.335] | 0 .. 0.5 |
| p_reach | 7 [3, 18] | 1 .. 30 |
| p_same_line | 0.144 [0.0317, 0.329] | 0 .. 0.5 |

### verbose: taze medyan mesafe 3.82, en iyi 2.83

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -9.1 | 0.717 | 0.516 |
| wlen_frac_le2 | +5.4 | 0.077 | 0.140 |
| wlen_std | +4.4 | 1.693 | 2.012 |
| first_entropy_ratio | +4.3 | 0.806 | 0.883 |
| jsd_last | -4.2 | 0.719 | 0.519 |
| wlen_autocorr1 | -4.0 | 0.127 | -0.026 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.73 [6.15, 10.2] | 5 .. 13 |
| l_width_jitter | 0.194 [0.0931, 0.289] | 0 .. 0.35 |
| l_para_lines | 4.05 [0, 8.02] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.652] | 0.2 .. 3 |
| l_allo_rate | 0.00915 [0, 0.074] | 0.01 .. 0.15 |
| l_final_forms_share | 0.3 [0, 0.509] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.354 [0.18, 0.473] | 0.1 .. 0.9 |
| l_line_final_p | 0.349 [0.2, 0.461] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.602] | 0.3 .. 1 |
| p_alphabet | 16 [14, 19] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.368 [0.3, 0.45] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 29, Romanian 25, Croatian 24, Czech 13, Finnish 3

### automaton: taze medyan mesafe 4.00, en iyi 2.50

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| jsd_first | +8.8 | 0.385 | 0.685 |
| first_entropy_ratio | -7.4 | 0.806 | 0.674 |
| wlen_skew | +5.1 | 0.074 | 0.731 |
| char_double_rate | -4.7 | 0.067 | 0.001 |
| jsd_last | -3.9 | 0.719 | 0.532 |
| wlen_autocorr1 | -3.3 | 0.127 | 0.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.11 [5.88, 8.66] | 5 .. 13 |
| l_width_jitter | 0.24 [0.113, 0.32] | 0 .. 0.35 |
| l_para_lines | 6.77 [3.45, 10.1] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_final_forms_k | 0 [0, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.615 [0.42, 0.732] | 0.1 .. 0.9 |
| l_line_final_p | 0.147 [0, 0.295] | 0.1 .. 0.9 |
| l_para_initial_p | 0.739 [0.225, 0.963] | 0.3 .. 1 |
| p_alphabet | 16 [15, 17] | 15 .. 25 |
| p_levels | 6 [5, 6] | 3 .. 8 |
| p_out_degree | 6 [4, 7] | 2 .. 8 |
| p_concentration | 2.18 [1.67, 2.66] | 0.2 .. 3 |
| p_stay | 0.482 [0.391, 0.599] | 0 .. 1 |
| p_end_from | 3 [2, 3] | 1 .. 3 |
| p_link | 0.145 [0, 0.484] | 0.1 .. 1 |

### plain: taze medyan mesafe 4.05, en iyi 3.41

Voynich'ten 2 birimden fazla sapan feature sayısı: 20

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -8.1 | 0.628 | 0.133 |
| first_entropy_ratio | +7.0 | 0.806 | 0.932 |
| wlen_frac_le2 | +6.8 | 0.077 | 0.155 |
| type_len_mean | -6.6 | 5.692 | 4.569 |
| h2 | +6.1 | 2.016 | 2.758 |
| h2_over_h1 | +6.0 | 0.524 | 0.712 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.5 [7.62, 12.3] | 5 .. 13 |
| l_width_jitter | 0.189 [0.0759, 0.268] | 0 .. 0.35 |
| l_para_lines | 5.33 [0, 10.5] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.00265] | 0.01 .. 0.15 |
| l_final_forms_share | 0.941 [0.847, 0.976] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.232] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.479] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 98, Arabic 2

### codebook: taze medyan mesafe 4.32, en iyi 3.24

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| type_len_mean | -11.5 | 5.692 | 3.723 |
| wlen_std | -9.9 | 1.693 | 0.970 |
| vocab_ed1_density | +7.0 | 0.823 | 0.998 |
| wlen_mean | -6.1 | 5.066 | 3.649 |
| jsd_first | +5.4 | 0.385 | 0.567 |
| char_double_rate | -4.5 | 0.067 | 0.004 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.32 [5.68, 11.4] | 5 .. 13 |
| l_width_jitter | 0.246 [0.119, 0.318] | 0 .. 0.35 |
| l_para_lines | 9.64 [3.01, 13.4] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.153 [0, 0.407] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.474 [0.185, 0.771] | 0.1 .. 0.9 |
| l_line_final_p | 0.197 [0, 0.339] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.533] | 0.3 .. 1 |
| p_alphabet | 18 [17, 20] | 15 .. 25 |
| p_n_slots | 6 [6, 6] | 3 .. 6 |
| p_slot_overlap | 0.0125 [0.00113, 0.0326] | 0 .. 1 |
| p_len_max | 1 [1, 1] | 1 .. 2 |
| p_zero_empty | 1 [1, 1] | 0 .. 1 |
| p_order | 2 [2, 2] | 0 .. 2 |

Kaynak dil (son nüfusta en sık): Turkish 27, Croatian 18, Finnish 18, Czech 7, Russian 6

### abjad: taze medyan mesafe 5.94, en iyi 4.76

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +22.7 | 0.077 | 0.340 |
| wlen_frac1 | +8.5 | 0.017 | 0.112 |
| wlen_mean | -7.4 | 5.066 | 3.357 |
| type_len_mean | -7.3 | 5.692 | 4.446 |
| h2_over_h1 | +5.8 | 0.524 | 0.703 |
| h2 | +5.7 | 2.016 | 2.706 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.14 [6.71, 11.5] | 5 .. 13 |
| l_width_jitter | 0.181 [0.0728, 0.264] | 0 .. 0.35 |
| l_para_lines | 0 [0, 10.5] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.644 [0.5, 0.856] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0.468 [0.323, 0.544] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 3] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.412] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.142] | 0.1 .. 0.9 |
| l_para_initial_p | 0.3 [0, 0.586] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 98, Finnish 2


## eva_glyph: sınıf sınıf

### slotcite: taze medyan mesafe 2.76, en iyi 1.77

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -4.3 | 0.717 | 0.621 |
| edge_mi | -3.0 | 0.187 | -0.008 |
| zipf_slope | +2.8 | -0.778 | -0.604 |
| n_symbols | -2.7 | 25.250 | 22.000 |
| h2_over_h1 | +2.1 | 0.556 | 0.635 |
| vocab_ed1_density | +2.1 | 0.850 | 0.896 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.25 [6.27, 9.28] | 5 .. 13 |
| l_width_jitter | 0.219 [0.0942, 0.313] | 0 .. 0.35 |
| l_para_lines | 5.23 [0, 10.3] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.681 [0.544, 0.809] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.367 [0, 0.647] | 0.1 .. 0.9 |
| l_line_final_p | 0.233 [0, 0.37] | 0.1 .. 0.9 |
| l_para_initial_p | 0.43 [0, 0.708] | 0.3 .. 1 |
| p_alphabet | 19 [17, 21.2] | 15 .. 25 |
| p_slot_overlap | 0.688 [0.436, 0.902] | 0 .. 1 |
| p_n_edge | 33.5 [28.8, 37] | 5 .. 40 |
| p_n_mid | 25.5 [13, 61.2] | 10 .. 120 |
| p_empty | 0.225 [0.175, 0.286] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 2 [2, 3] | 2 .. 5 |
| p_copy | 0.624 [0.557, 0.686] | 0.5 .. 0.97 |
| p_exact | 0.184 [0.111, 0.29] | 0.1 .. 0.7 |
| p_reach | 7 [2, 15.2] | 1 .. 30 |
| p_same_line | 0.0565 [0.00339, 0.152] | 0 .. 0.5 |
| p_mut_prefix | 0.302 [0.199, 0.413] | 0 .. 1 |
| p_mut_mid | 0.443 [0.204, 0.634] | 0 .. 1 |
| p_mut_suffix | 0.125 [0.0208, 0.22] | 0 .. 1 |

### grille: taze medyan mesafe 2.80, en iyi 1.61

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -3.0 | 0.103 | 0.002 |
| jsd_line_final | -3.0 | 0.110 | 0.014 |
| edge_mi | -3.0 | 0.187 | -0.004 |
| n_symbols | -2.7 | 25.250 | 22.000 |
| h2_over_h1 | +2.4 | 0.556 | 0.647 |
| h2 | +2.4 | 2.131 | 2.508 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.79 [6.45, 12] | 5 .. 13 |
| l_width_jitter | 0.207 [0.102, 0.263] | 0 .. 0.35 |
| l_para_lines | 3.24 [0, 5.91] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.586 [0.492, 0.657] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.389] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.236] | 0.1 .. 0.9 |
| l_para_initial_p | 0.333 [0, 0.546] | 0.3 .. 1 |
| p_alphabet | 21 [18, 23] | 15 .. 25 |
| p_rows | 1.26e+03 [780, 2.33e+03] | 60 .. 3000 |
| p_slot_overlap | 0.492 [0.293, 0.728] | 0 .. 1 |
| p_n_edge | 32 [27, 39] | 5 .. 40 |
| p_n_mid | 56.5 [33, 97.5] | 10 .. 120 |
| p_empty | 0.318 [0.252, 0.392] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_n_grilles | 5 [3, 6] | 3 .. 8 |

### selfcite: taze medyan mesafe 2.91, en iyi 2.20

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -5.2 | 0.717 | 0.603 |
| h2_over_h1 | +4.4 | 0.556 | 0.722 |
| h2 | +4.2 | 2.131 | 2.782 |
| vocab_ed1_density | +3.6 | 0.850 | 0.930 |
| char_double_rate | +3.1 | 0.076 | 0.121 |
| edge_mi | -3.0 | 0.187 | -0.007 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.33 [8.02, 10.8] | 5 .. 13 |
| l_width_jitter | 0.248 [0.169, 0.327] | 0 .. 0.35 |
| l_para_lines | 9.16 [4.19, 13.3] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.38] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.678 [0.521, 0.876] | 0.1 .. 1 |
| l_final_forms_k | 3 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.467 [0, 0.617] | 0.1 .. 0.9 |
| l_line_final_p | 0.248 [0.115, 0.33] | 0.1 .. 0.9 |
| l_para_initial_p | 0.641 [0, 0.871] | 0.3 .. 1 |
| p_alphabet | 17 [16, 18] | 15 .. 25 |
| p_glyph_classes | 5 [4, 6] | 4 .. 7 |
| p_copy | 0.87 [0.854, 0.886] | 0.85 .. 0.97 |
| p_exact | 0.427 [0.252, 0.575] | 0.2 .. 0.8 |
| p_reach | 21 [13, 27.2] | 1 .. 30 |
| p_same_line | 0.0221 [0, 0.0557] | 0 .. 0.3 |
| p_slot_overlap | 0.181 [0.0467, 0.461] | 0 .. 1 |
| p_affix | 0.784 [0.665, 0.891] | 0.3 .. 0.9 |
| p_mut_substitute | 0.406 [0.205, 0.598] | 0 .. 1 |
| p_mut_prefix | 0.554 [0.414, 0.68] | 0 .. 1 |
| p_mut_delete | 0.0864 [0.0264, 0.196] | 0 .. 1 |
| p_mut_double | 0.12 [0.0512, 0.187] | 0 .. 1 |

### plain: taze medyan mesafe 3.02, en iyi 2.37

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -6.1 | 0.626 | 0.275 |
| h2 | +4.8 | 2.131 | 2.881 |
| h2_over_h1 | +4.7 | 0.556 | 0.735 |
| char_double_rate | -4.6 | 0.076 | 0.009 |
| wlen_std | -4.6 | 1.552 | 1.314 |
| eff_symbols | +3.4 | 14.404 | 16.002 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.2 [7.36, 11.9] | 5 .. 13 |
| l_width_jitter | 0.163 [0.0702, 0.272] | 0 .. 0.35 |
| l_para_lines | 5.26 [0, 8.73] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.822 [0.758, 0.882] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_line_final_p | 0.195 [0, 0.313] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.541] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### slotgram: taze medyan mesafe 3.25, en iyi 2.08

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| n_symbols | -4.4 | 25.250 | 20.000 |
| edge_mi | -3.0 | 0.187 | -0.005 |
| wlen_autocorr1 | -2.8 | 0.103 | 0.011 |
| zipf_slope | +2.6 | -0.778 | -0.613 |
| wlen_std | +2.3 | 1.552 | 1.674 |
| vocab_ed1_density | +2.3 | 0.850 | 0.901 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.97 [8.42, 11.9] | 5 .. 13 |
| l_width_jitter | 0.149 [0.0701, 0.24] | 0 .. 0.35 |
| l_para_lines | 0 [0, 9.51] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.702 [0.461, 0.849] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.252 [0, 0.554] | 0.1 .. 0.9 |
| l_line_final_p | 0.163 [0, 0.29] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.544] | 0.3 .. 1 |
| p_alphabet | 18 [16, 21] | 15 .. 25 |
| p_n_slots | 5 [4, 5] | 3 .. 8 |
| p_slot_overlap | 0.375 [0.164, 0.507] | 0 .. 1 |
| p_n_inv | 11 [8, 18] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.422 [0.362, 0.476] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0.463] | 0.3 .. 0.95 |
| p_exact | 0.289 [0.157, 0.415] | 0 .. 0.5 |
| p_reach | 5 [2, 14] | 1 .. 30 |
| p_same_line | 0.176 [0.0709, 0.279] | 0 .. 0.5 |

### verbose: taze medyan mesafe 3.57, en iyi 2.47

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +8.7 | 1.552 | 2.006 |
| hapax_ratio | -5.7 | 0.717 | 0.591 |
| wlen_autocorr1 | -4.0 | 0.103 | -0.030 |
| wlen_frac1 | +3.6 | 0.017 | 0.059 |
| wlen_skew | +3.4 | 0.183 | 0.548 |
| ttr | -3.1 | 0.443 | 0.272 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.27 [5.62, 9.35] | 5 .. 13 |
| l_width_jitter | 0.184 [0.0842, 0.279] | 0 .. 0.35 |
| l_para_lines | 6.44 [0, 11.8] | 3 .. 15 |
| l_allo_per_glyph | 0.679 [0.393, 0.958] | 0.2 .. 3 |
| l_allo_rate | 0.0653 [0.038, 0.0854] | 0.01 .. 0.15 |
| l_final_forms_share | 0.492 [0.285, 0.687] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.147] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 3] | 0 .. 4 |
| l_line_initial_p | 0.239 [0, 0.415] | 0.1 .. 0.9 |
| l_line_final_p | 0.282 [0, 0.421] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.075] | 0.3 .. 1 |
| p_alphabet | 14 [12, 15] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.495 [0.373, 0.624] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 39, Romanian 28, Czech 14, Croatian 9, Polish 5

### abjad: taze medyan mesafe 3.58, en iyi 2.73

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +8.3 | 0.017 | 0.114 |
| wlen_frac_le2 | +7.6 | 0.099 | 0.338 |
| wlen_skew | +4.7 | 0.183 | 0.680 |
| h2_over_h1 | +4.2 | 0.556 | 0.714 |
| h2 | +4.1 | 2.131 | 2.762 |
| wlen_mean | -3.8 | 4.528 | 3.348 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.1 [5.69, 11] | 5 .. 13 |
| l_width_jitter | 0.112 [0.0649, 0.221] | 0 .. 0.35 |
| l_para_lines | 4.69 [0, 8.38] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.737 [0.643, 0.845] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.292 [0.075, 0.432] | 0.1 .. 1 |
| l_initial_forms_k | 1 [1, 2] | 0 .. 4 |
| l_line_initial_p | 0.05 [0, 0.359] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.436] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100

### automaton: taze medyan mesafe 3.90, en iyi 2.42

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| jsd_first | +7.9 | 0.350 | 0.674 |
| first_entropy_ratio | -7.7 | 0.867 | 0.696 |
| n_symbols | -6.1 | 25.250 | 18.000 |
| wlen_skew | +5.5 | 0.183 | 0.762 |
| char_double_rate | -5.1 | 0.076 | 0.001 |
| wlen_autocorr1 | -3.1 | 0.103 | -0.001 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.38 [5.86, 9.92] | 5 .. 13 |
| l_width_jitter | 0.126 [0.0692, 0.193] | 0 .. 0.35 |
| l_para_lines | 8.48 [3.79, 12.1] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.59] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0025] | 0.01 .. 0.15 |
| l_final_forms_share | 0.342 [0, 0.502] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3.25] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.587 [0.39, 0.736] | 0.1 .. 0.9 |
| l_line_final_p | 0.263 [0, 0.359] | 0.1 .. 0.9 |
| l_para_initial_p | 0.569 [0.334, 0.757] | 0.3 .. 1 |
| p_alphabet | 16 [15, 16] | 15 .. 25 |
| p_levels | 5 [5, 6] | 3 .. 8 |
| p_out_degree | 7 [5, 8] | 2 .. 8 |
| p_concentration | 2.37 [1.82, 2.8] | 0.2 .. 3 |
| p_stay | 0.392 [0.328, 0.475] | 0 .. 1 |
| p_end_from | 2 [1, 3] | 1 .. 3 |
| p_link | 0.682 [0.228, 0.838] | 0.1 .. 1 |

### codebook: taze medyan mesafe 3.97, en iyi 2.92

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | -10.9 | 1.552 | 0.983 |
| vocab_ed1_density | +6.6 | 0.850 | 0.996 |
| type_len_mean | -6.2 | 5.032 | 3.690 |
| first_entropy_ratio | -5.8 | 0.867 | 0.739 |
| n_symbols | -5.2 | 25.250 | 19.000 |
| char_double_rate | -4.9 | 0.076 | 0.005 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.29 [5.82, 10.9] | 5 .. 13 |
| l_width_jitter | 0.227 [0.0665, 0.337] | 0 .. 0.35 |
| l_para_lines | 8.64 [0, 12] | 3 .. 15 |
| l_allo_per_glyph | 0.222 [0, 1.12] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0694] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0.48] | 0.1 .. 1 |
| l_final_forms_k | 0.5 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.479 [0.299, 0.661] | 0.1 .. 0.9 |
| l_line_final_p | 0.1 [0, 0.362] | 0.1 .. 0.9 |
| l_para_initial_p | 0.405 [0, 0.818] | 0.3 .. 1 |
| p_alphabet | 19 [17, 20] | 15 .. 25 |
| p_n_slots | 6 [6, 6] | 3 .. 6 |
| p_slot_overlap | 0.00771 [0, 0.0279] | 0 .. 1 |
| p_len_max | 1 [1, 1] | 1 .. 2 |
| p_zero_empty | 1 [1, 1] | 0 .. 1 |
| p_order | 2 [2, 2] | 0 .. 2 |

Kaynak dil (son nüfusta en sık): Finnish 23, Russian 18, Croatian 17, Hebrew 11, Italian 7


## v101: sınıf sınıf

### plain: taze medyan mesafe 2.66, en iyi 2.16

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| vocab_ed1_density | -5.1 | 0.854 | 0.736 |
| n_symbols | -4.6 | 69.529 | 26.000 |
| wlen_frac1 | -4.5 | 0.046 | 0.000 |
| h2 | +4.1 | 2.383 | 3.079 |
| h2_over_h1 | +3.8 | 0.595 | 0.755 |
| rep_adjacent_ed1 | -3.7 | 0.043 | 0.017 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.3 [8.07, 11.2] | 5 .. 13 |
| l_width_jitter | 0.096 [0.0312, 0.172] | 0 .. 0.35 |
| l_para_lines | 0 [0, 8.33] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.312] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0636] | 0.01 .. 0.15 |
| l_final_forms_share | 0.674 [0.58, 0.755] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.244 [0, 0.422] | 0.1 .. 0.9 |
| l_line_final_p | 0.102 [0, 0.325] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.463] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### abjad: taze medyan mesafe 2.92, en iyi 2.24

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +5.9 | 0.046 | 0.107 |
| wlen_frac_le2 | +5.8 | 0.184 | 0.338 |
| n_symbols | -4.7 | 69.529 | 25.000 |
| wlen_skew | +3.4 | 0.225 | 0.695 |
| first_entropy_ratio | +3.3 | 0.886 | 0.992 |
| wlen_mean | -3.3 | 3.859 | 3.360 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.86 [5.56, 8.73] | 5 .. 13 |
| l_width_jitter | 0.22 [0.0862, 0.293] | 0 .. 0.35 |
| l_para_lines | 6.23 [4.04, 8.21] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.804 [0.684, 0.916] | 0.1 .. 1 |
| l_final_forms_k | 4 [3, 4] | 0 .. 4 |
| l_initial_forms_share | 0.101 [0, 0.24] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 4] | 0 .. 4 |
| l_line_initial_p | 0.213 [0, 0.407] | 0.1 .. 0.9 |
| l_line_final_p | 0.334 [0.205, 0.449] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.607] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100

### selfcite: taze medyan mesafe 3.33, en iyi 2.16

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +9.1 | 0.015 | 0.064 |
| n_symbols | -4.5 | 69.529 | 27.500 |
| hapax_ratio | -3.7 | 0.741 | 0.630 |
| rep_adjacent_exact | +3.6 | 0.006 | 0.014 |
| last_entropy_ratio | -3.2 | 0.704 | 0.505 |
| zipf_slope | +3.1 | -0.776 | -0.640 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.44 [7.1, 11.1] | 5 .. 13 |
| l_width_jitter | 0.209 [0.116, 0.284] | 0 .. 0.35 |
| l_para_lines | 6.62 [0, 11.6] | 3 .. 15 |
| l_allo_per_glyph | 1.19 [0, 2.29] | 0.2 .. 3 |
| l_allo_rate | 0.0174 [0, 0.065] | 0.01 .. 0.15 |
| l_final_forms_share | 0.776 [0.623, 0.887] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.498 [0, 0.716] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.301] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.383] | 0.3 .. 1 |
| p_alphabet | 19 [17, 21] | 15 .. 25 |
| p_glyph_classes | 5 [4, 6] | 4 .. 7 |
| p_copy | 0.872 [0.859, 0.885] | 0.85 .. 0.97 |
| p_exact | 0.348 [0.245, 0.47] | 0.2 .. 0.8 |
| p_reach | 25 [20, 30] | 1 .. 30 |
| p_same_line | 0.0468 [0.0138, 0.0965] | 0 .. 0.3 |
| p_slot_overlap | 0.496 [0.261, 0.806] | 0 .. 1 |
| p_affix | 0.678 [0.541, 0.846] | 0.3 .. 0.9 |
| p_mut_substitute | 0.398 [0.227, 0.598] | 0 .. 1 |
| p_mut_prefix | 0.477 [0.287, 0.683] | 0 .. 1 |
| p_mut_delete | 0.183 [0.0999, 0.263] | 0 .. 1 |
| p_mut_double | 0.00158 [0, 0.0254] | 0 .. 1 |

### slotgram: taze medyan mesafe 3.35, en iyi 1.97

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| n_symbols | -4.8 | 69.529 | 24.000 |
| edge_mi | -3.0 | 0.228 | -0.005 |
| wlen_autocorr1 | -2.9 | 0.179 | 0.006 |
| h1 | -2.9 | 4.005 | 3.908 |
| jsd_line_final | -2.7 | 0.133 | 0.016 |
| wlen_std | -2.7 | 1.469 | 1.305 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.79 [6.02, 10.3] | 5 .. 13 |
| l_width_jitter | 0.139 [0.0703, 0.238] | 0 .. 0.35 |
| l_para_lines | 7.9 [0, 11.6] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.958] | 0.2 .. 3 |
| l_allo_rate | 0.0294 [0, 0.0674] | 0.01 .. 0.15 |
| l_final_forms_share | 0.739 [0.474, 0.933] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.41 [0.129, 0.617] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.246] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.429] | 0.3 .. 1 |
| p_alphabet | 22 [21, 24] | 15 .. 25 |
| p_n_slots | 7 [6, 8] | 3 .. 8 |
| p_slot_overlap | 0.345 [0.0258, 0.887] | 0 .. 1 |
| p_n_inv | 12 [7, 20] | 2 .. 30 |
| p_len_max | 1 [1, 2] | 1 .. 2 |
| p_empty | 0.53 [0.453, 0.574] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0.399] | 0.3 .. 0.95 |
| p_exact | 0.243 [0.0894, 0.391] | 0 .. 0.5 |
| p_reach | 6.5 [2.75, 16.2] | 1 .. 30 |
| p_same_line | 0.258 [0.101, 0.417] | 0 .. 0.5 |

### verbose: taze medyan mesafe 3.37, en iyi 2.25

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +5.3 | 0.015 | 0.044 |
| jsd_last | -5.2 | 0.679 | 0.413 |
| wlen_std | +5.0 | 1.469 | 1.779 |
| wlen_frac1 | +4.4 | 0.046 | 0.091 |
| wlen_autocorr1 | -3.6 | 0.179 | -0.033 |
| wlen_skew | +3.4 | 0.225 | 0.693 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.4 [6.55, 12.1] | 5 .. 13 |
| l_width_jitter | 0.149 [0.0746, 0.239] | 0 .. 0.35 |
| l_para_lines | 10.4 [5.25, 13.1] | 3 .. 15 |
| l_allo_per_glyph | 2.12 [1.42, 2.6] | 0.2 .. 3 |
| l_allo_rate | 0.0992 [0.076, 0.133] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_final_forms_k | 0.5 [0, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.124] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.461] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.243] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.543] | 0.3 .. 1 |
| p_alphabet | 16 [14, 18] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.759 [0.66, 0.85] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Croatian 46, Romanian 23, Turkish 16, Polish 4, Albanian 3

### codebook: taze medyan mesafe 3.41, en iyi 2.47

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | -8.0 | 1.469 | 0.977 |
| type_len_mean | -6.4 | 4.440 | 3.659 |
| vocab_ed1_density | +5.8 | 0.854 | 0.987 |
| jsd_first | +4.8 | 0.310 | 0.554 |
| n_symbols | -4.1 | 69.529 | 31.000 |
| wlen_skew | -3.7 | 0.225 | -0.286 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.61 [6.55, 11.2] | 5 .. 13 |
| l_width_jitter | 0.195 [0.127, 0.252] | 0 .. 0.35 |
| l_para_lines | 0 [0, 9.78] | 3 .. 15 |
| l_allo_per_glyph | 1.19 [0.475, 1.9] | 0.2 .. 3 |
| l_allo_rate | 0.105 [0.061, 0.133] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0.56] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.588 [0.463, 0.781] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.253] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0] | 0.3 .. 1 |
| p_alphabet | 18 [16, 19] | 15 .. 25 |
| p_n_slots | 6 [5, 6] | 3 .. 6 |
| p_slot_overlap | 0.00703 [0, 0.0294] | 0 .. 1 |
| p_len_max | 1 [1, 1] | 1 .. 2 |
| p_zero_empty | 1 [1, 1] | 0 .. 1 |
| p_order | 2 [2, 2] | 0 .. 2 |

Kaynak dil (son nüfusta en sık): Italian 30, Turkish 18, Latin 12, Swedish 10, Croatian 8

### automaton: taze medyan mesafe 3.58, en iyi 2.05

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| jsd_first | +8.0 | 0.310 | 0.712 |
| first_entropy_ratio | -5.3 | 0.886 | 0.716 |
| n_symbols | -4.7 | 69.529 | 25.500 |
| wlen_skew | +3.8 | 0.225 | 0.742 |
| jsd_last | -3.2 | 0.679 | 0.512 |
| wlen_autocorr1 | -3.0 | 0.179 | 0.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.98 [6.95, 11.8] | 5 .. 13 |
| l_width_jitter | 0.145 [0.0489, 0.248] | 0 .. 0.35 |
| l_para_lines | 0 [0, 8.1] | 3 .. 15 |
| l_allo_per_glyph | 1.75 [0.8, 2.48] | 0.2 .. 3 |
| l_allo_rate | 0.0252 [0, 0.0544] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0.269] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.537 [0.316, 0.752] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.459] | 0.3 .. 1 |
| p_alphabet | 18 [16, 20] | 15 .. 25 |
| p_levels | 5 [4, 5] | 3 .. 8 |
| p_out_degree | 7 [6, 8] | 2 .. 8 |
| p_concentration | 1.65 [1.26, 2.14] | 0.2 .. 3 |
| p_stay | 0.376 [0.301, 0.488] | 0 .. 1 |
| p_end_from | 1 [1, 2] | 1 .. 3 |
| p_link | 0.369 [0, 0.673] | 0.1 .. 1 |

### grille: taze medyan mesafe 3.74, en iyi 1.96

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +8.4 | 0.015 | 0.060 |
| n_symbols | -4.0 | 69.529 | 32.000 |
| wlen_autocorr1 | -3.1 | 0.179 | -0.005 |
| vocab_ed1_density | +3.0 | 0.854 | 0.923 |
| edge_mi | -3.0 | 0.228 | -0.005 |
| hapax_ratio | -2.3 | 0.741 | 0.674 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.32 [6.2, 11.2] | 5 .. 13 |
| l_width_jitter | 0.199 [0.0727, 0.288] | 0 .. 0.35 |
| l_para_lines | 3.05 [0, 9.3] | 3 .. 15 |
| l_allo_per_glyph | 1.55 [0, 2.45] | 0.2 .. 3 |
| l_allo_rate | 0.0692 [0, 0.104] | 0.01 .. 0.15 |
| l_final_forms_share | 0.465 [0.208, 0.849] | 0.1 .. 1 |
| l_final_forms_k | 2.5 [1.75, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.353 [0, 0.585] | 0.1 .. 0.9 |
| l_line_final_p | 0.0543 [0, 0.45] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.601] | 0.3 .. 1 |
| p_alphabet | 22 [21, 24] | 15 .. 25 |
| p_rows | 1.11e+03 [477, 1.96e+03] | 60 .. 3000 |
| p_slot_overlap | 0.615 [0.442, 0.764] | 0 .. 1 |
| p_n_edge | 23 [12.8, 34.2] | 5 .. 40 |
| p_n_mid | 32.5 [23, 79.5] | 10 .. 120 |
| p_empty | 0.354 [0.29, 0.436] | 0 .. 0.6 |
| p_len_edge | 2 [2, 2] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_n_grilles | 5 [4, 7] | 3 .. 8 |

### slotcite: taze medyan mesafe 3.81, en iyi 2.08

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +8.9 | 0.015 | 0.063 |
| edge_mi | -3.0 | 0.228 | -0.007 |
| rep_adjacent_exact | +2.7 | 0.006 | 0.012 |
| wlen_autocorr1 | -2.3 | 0.179 | 0.040 |
| n_symbols | -2.2 | 69.529 | 49.000 |
| jsd_line_final | -2.2 | 0.133 | 0.040 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.71 [7.56, 12] | 5 .. 13 |
| l_width_jitter | 0.155 [0.0782, 0.21] | 0 .. 0.35 |
| l_para_lines | 0 [0, 7.53] | 3 .. 15 |
| l_allo_per_glyph | 1.96 [0.925, 2.67] | 0.2 .. 3 |
| l_allo_rate | 0.0889 [0.0651, 0.112] | 0.01 .. 0.15 |
| l_final_forms_share | 0.497 [0.244, 0.783] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.463 [0.0869, 0.688] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.323] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.717] | 0.3 .. 1 |
| p_alphabet | 20 [17, 23] | 15 .. 25 |
| p_slot_overlap | 0.676 [0.452, 0.857] | 0 .. 1 |
| p_n_edge | 21.5 [13.8, 31] | 5 .. 40 |
| p_n_mid | 55 [28.8, 98.2] | 10 .. 120 |
| p_empty | 0.386 [0.324, 0.458] | 0 .. 0.6 |
| p_len_edge | 2 [2, 2] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_copy | 0.662 [0.569, 0.74] | 0.5 .. 0.97 |
| p_exact | 0.303 [0.172, 0.4] | 0.1 .. 0.7 |
| p_reach | 11.5 [5, 23.2] | 1 .. 30 |
| p_same_line | 0.0755 [0.0187, 0.156] | 0 .. 0.5 |
| p_mut_prefix | 0.255 [0.076, 0.439] | 0 .. 1 |
| p_mut_mid | 0.436 [0.147, 0.727] | 0 .. 1 |
| p_mut_suffix | 0.382 [0.22, 0.54] | 0 .. 1 |


## zl_basic: sınıf sınıf

### grille: taze medyan mesafe 2.95, en iyi 1.84

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| edge_mi | -3.2 | 0.192 | -0.003 |
| h2_over_h1 | +2.8 | 0.521 | 0.614 |
| jsd_line_final | -2.6 | 0.110 | 0.009 |
| wlen_autocorr1 | -2.6 | 0.123 | -0.000 |
| h2 | +2.6 | 2.013 | 2.368 |
| vocab_ed1_density | +2.4 | 0.823 | 0.875 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.99 [6.68, 10.5] | 5 .. 13 |
| l_width_jitter | 0.191 [0.0835, 0.281] | 0 .. 0.35 |
| l_para_lines | 4.93 [0, 10.2] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.58] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0192] | 0.01 .. 0.15 |
| l_final_forms_share | 0.646 [0.558, 0.793] | 0.1 .. 1 |
| l_final_forms_k | 3 [1.75, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.372 [0, 0.609] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.174] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.831] | 0.3 .. 1 |
| p_alphabet | 19.5 [17, 23] | 15 .. 25 |
| p_rows | 1.73e+03 [978, 2.7e+03] | 60 .. 3000 |
| p_slot_overlap | 0.29 [0.109, 0.617] | 0 .. 1 |
| p_n_edge | 25 [20, 30.2] | 5 .. 40 |
| p_n_mid | 29 [16.8, 52.5] | 10 .. 120 |
| p_empty | 0.35 [0.303, 0.407] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 5] | 2 .. 5 |
| p_n_grilles | 6 [5, 7] | 3 .. 8 |

### slotcite: taze medyan mesafe 3.11, en iyi 1.76

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| edge_mi | -3.3 | 0.192 | -0.006 |
| h2_over_h1 | +3.1 | 0.521 | 0.625 |
| h2 | +3.0 | 2.013 | 2.436 |
| hapax_ratio | -2.9 | 0.715 | 0.623 |
| first_entropy_ratio | -2.2 | 0.817 | 0.780 |
| rep_adjacent_exact | +2.1 | 0.008 | 0.014 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.11 [6.54, 10.4] | 5 .. 13 |
| l_width_jitter | 0.191 [0.109, 0.285] | 0 .. 0.35 |
| l_para_lines | 0 [0, 7.05] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.58] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0647] | 0.01 .. 0.15 |
| l_final_forms_share | 0.55 [0.39, 0.664] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0.5 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.119 [0, 0.458] | 0.1 .. 0.9 |
| l_line_final_p | 0.217 [0, 0.333] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0] | 0.3 .. 1 |
| p_alphabet | 19 [17.8, 21] | 15 .. 25 |
| p_slot_overlap | 0.348 [0.0992, 0.625] | 0 .. 1 |
| p_n_edge | 22.5 [16.8, 34] | 5 .. 40 |
| p_n_mid | 38.5 [20, 67.5] | 10 .. 120 |
| p_empty | 0.287 [0.194, 0.374] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 5] | 2 .. 5 |
| p_copy | 0.69 [0.57, 0.815] | 0.5 .. 0.97 |
| p_exact | 0.167 [0.1, 0.257] | 0.1 .. 0.7 |
| p_reach | 11 [3, 21] | 1 .. 30 |
| p_same_line | 0.111 [0.0457, 0.172] | 0 .. 0.5 |
| p_mut_prefix | 0.263 [0.0977, 0.459] | 0 .. 1 |
| p_mut_mid | 0.401 [0.169, 0.583] | 0 .. 1 |
| p_mut_suffix | 0.208 [0.0693, 0.398] | 0 .. 1 |

### slotgram: taze medyan mesafe 3.20, en iyi 2.12

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| edge_mi | -3.2 | 0.192 | -0.005 |
| zipf_slope | +3.0 | -0.785 | -0.579 |
| h2_over_h1 | +2.8 | 0.521 | 0.616 |
| h1 | -2.6 | 3.862 | 3.777 |
| vocab_ed1_density | +2.4 | 0.823 | 0.874 |
| wlen_autocorr1 | -2.4 | 0.123 | 0.012 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.29 [5.94, 9.53] | 5 .. 13 |
| l_width_jitter | 0.213 [0.123, 0.272] | 0 .. 0.35 |
| l_para_lines | 0 [0, 4.76] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.823] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0236] | 0.01 .. 0.15 |
| l_final_forms_share | 0.7 [0.409, 0.866] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.141] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.0507 [0, 0.574] | 0.1 .. 0.9 |
| l_line_final_p | 0.223 [0, 0.344] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0] | 0.3 .. 1 |
| p_alphabet | 18 [16, 21] | 15 .. 25 |
| p_n_slots | 6 [5, 6] | 3 .. 8 |
| p_slot_overlap | 0.525 [0.279, 0.753] | 0 .. 1 |
| p_n_inv | 7 [4, 10] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.427 [0.378, 0.503] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0.564] | 0.3 .. 0.95 |
| p_exact | 0.258 [0.127, 0.385] | 0 .. 0.5 |
| p_reach | 4.5 [2, 12.5] | 1 .. 30 |
| p_same_line | 0.107 [0.00706, 0.283] | 0 .. 0.5 |

### verbose: taze medyan mesafe 3.24, en iyi 2.39

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -5.0 | 0.715 | 0.553 |
| wlen_std | +4.7 | 1.768 | 2.050 |
| wlen_skew | +4.4 | 0.025 | 0.475 |
| jsd_last | -3.8 | 0.712 | 0.541 |
| wlen_autocorr1 | -3.3 | 0.123 | -0.032 |
| wlen_frac_le2 | +3.2 | 0.097 | 0.140 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.45 [5.2, 10] | 5 .. 13 |
| l_width_jitter | 0.183 [0.072, 0.296] | 0 .. 0.35 |
| l_para_lines | 6.96 [0, 12.1] | 3 .. 15 |
| l_allo_per_glyph | 1.12 [0.257, 2.1] | 0.2 .. 3 |
| l_allo_rate | 0.0345 [0, 0.0634] | 0.01 .. 0.15 |
| l_final_forms_share | 0.297 [0, 0.552] | 0.1 .. 1 |
| l_final_forms_k | 1 [0.75, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.395 [0, 0.561] | 0.1 .. 0.9 |
| l_line_final_p | 0.171 [0, 0.303] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.495] | 0.3 .. 1 |
| p_alphabet | 16 [14, 17] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.401 [0.344, 0.463] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 62, Czech 17, Romanian 13, Turkish 3, Albanian 3

### selfcite: taze medyan mesafe 3.29, en iyi 2.61

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| h2_over_h1 | +5.0 | 0.521 | 0.689 |
| h2 | +4.9 | 2.013 | 2.690 |
| char_double_rate | +4.9 | 0.066 | 0.139 |
| vocab_ed1_density | +4.5 | 0.823 | 0.921 |
| type_len_mean | -3.9 | 5.640 | 4.936 |
| hapax_ratio | -3.7 | 0.715 | 0.594 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.5 [8.31, 11.2] | 5 .. 13 |
| l_width_jitter | 0.244 [0.166, 0.322] | 0 .. 0.35 |
| l_para_lines | 0 [0, 8.89] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.762 [0.642, 0.882] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.259 [0.165, 0.33] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2.25] | 0 .. 4 |
| l_line_initial_p | 0.512 [0, 0.673] | 0.1 .. 0.9 |
| l_line_final_p | 0.15 [0, 0.299] | 0.1 .. 0.9 |
| l_para_initial_p | 0.823 [0.422, 0.931] | 0.3 .. 1 |
| p_alphabet | 16 [15, 17.2] | 15 .. 25 |
| p_glyph_classes | 6 [6, 7] | 4 .. 7 |
| p_copy | 0.88 [0.859, 0.909] | 0.85 .. 0.97 |
| p_exact | 0.451 [0.345, 0.529] | 0.2 .. 0.8 |
| p_reach | 25 [20, 28] | 1 .. 30 |
| p_same_line | 0.0256 [0.00859, 0.0502] | 0 .. 0.3 |
| p_slot_overlap | 0.554 [0.338, 0.739] | 0 .. 1 |
| p_affix | 0.854 [0.759, 0.9] | 0.3 .. 0.9 |
| p_mut_substitute | 0.441 [0.252, 0.589] | 0 .. 1 |
| p_mut_prefix | 0.476 [0.318, 0.584] | 0 .. 1 |
| p_mut_delete | 0.133 [0.0823, 0.177] | 0 .. 1 |
| p_mut_double | 0.191 [0.121, 0.254] | 0 .. 1 |

### plain: taze medyan mesafe 3.68, en iyi 3.08

Voynich'ten 2 birimden fazla sapan feature sayısı: 22

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -8.0 | 0.636 | 0.108 |
| first_entropy_ratio | +5.9 | 0.817 | 0.916 |
| h2 | +5.7 | 2.013 | 2.801 |
| h2_over_h1 | +5.6 | 0.521 | 0.709 |
| jsd_last | +5.0 | 0.712 | 0.941 |
| type_len_mean | -4.2 | 5.640 | 4.876 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.15 [6.04, 11.1] | 5 .. 13 |
| l_width_jitter | 0.0823 [0.00681, 0.181] | 0 .. 0.35 |
| l_para_lines | 0 [0, 5.9] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.922 [0.869, 0.965] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.261] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.455] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Arabic 72, Hebrew 28

### automaton: taze medyan mesafe 4.23, en iyi 2.58

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| first_entropy_ratio | -9.9 | 0.817 | 0.648 |
| jsd_first | +8.4 | 0.385 | 0.713 |
| wlen_skew | +8.2 | 0.025 | 0.859 |
| char_double_rate | -4.4 | 0.066 | 0.000 |
| jsd_last | -3.4 | 0.712 | 0.555 |
| wlen_frac1 | -3.2 | 0.033 | 0.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.02 [5.51, 9.73] | 5 .. 13 |
| l_width_jitter | 0.173 [0.0608, 0.26] | 0 .. 0.35 |
| l_para_lines | 5.59 [0, 9.08] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0.221] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.452 [0.135, 0.67] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.178] | 0.1 .. 0.9 |
| l_para_initial_p | 0.649 [0.225, 0.818] | 0.3 .. 1 |
| p_alphabet | 16 [15, 17] | 15 .. 25 |
| p_levels | 5 [5, 6] | 3 .. 8 |
| p_out_degree | 6 [5, 7] | 2 .. 8 |
| p_concentration | 2.14 [1.5, 2.87] | 0.2 .. 3 |
| p_stay | 0.547 [0.475, 0.663] | 0 .. 1 |
| p_end_from | 2.5 [2, 3] | 1 .. 3 |
| p_link | 0.449 [0, 0.744] | 0.1 .. 1 |

### codebook: taze medyan mesafe 4.35, en iyi 3.59

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | -12.7 | 1.768 | 1.001 |
| type_len_mean | -10.1 | 5.640 | 3.815 |
| vocab_ed1_density | +8.0 | 0.823 | 0.995 |
| wlen_mean | -5.6 | 4.961 | 3.691 |
| h1 | -3.9 | 3.862 | 3.734 |
| first_entropy_ratio | -3.6 | 0.817 | 0.756 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.03 [5.38, 8.93] | 5 .. 13 |
| l_width_jitter | 0.249 [0.176, 0.312] | 0 .. 0.35 |
| l_para_lines | 7.39 [0, 13.6] | 3 .. 15 |
| l_allo_per_glyph | 0.371 [0, 1.69] | 0.2 .. 3 |
| l_allo_rate | 0.0111 [0, 0.0862] | 0.01 .. 0.15 |
| l_final_forms_share | 0.147 [0, 0.428] | 0.1 .. 1 |
| l_final_forms_k | 2 [0, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.509 [0.335, 0.675] | 0.1 .. 0.9 |
| l_line_final_p | 0.191 [0, 0.372] | 0.1 .. 0.9 |
| l_para_initial_p | 0.456 [0, 0.862] | 0.3 .. 1 |
| p_alphabet | 17 [16, 18] | 15 .. 25 |
| p_n_slots | 6 [6, 6] | 3 .. 6 |
| p_slot_overlap | 0.0115 [0, 0.0329] | 0 .. 1 |
| p_len_max | 1 [1, 1] | 1 .. 2 |
| p_zero_empty | 1 [1, 1] | 0 .. 1 |
| p_order | 2 [2, 2] | 0 .. 2 |

Kaynak dil (son nüfusta en sık): Russian 27, Romanian 17, Czech 15, Polish 10, German 8

### abjad: taze medyan mesafe 5.02, en iyi 3.74

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +18.0 | 0.097 | 0.339 |
| wlen_frac1 | +7.8 | 0.033 | 0.113 |
| wlen_mean | -7.0 | 4.961 | 3.370 |
| type_len_mean | -6.6 | 5.640 | 4.456 |
| wlen_skew | +6.5 | 0.025 | 0.690 |
| h2_over_h1 | +5.0 | 0.521 | 0.689 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.03 [5.55, 8.77] | 5 .. 13 |
| l_width_jitter | 0.132 [0.0211, 0.22] | 0 .. 0.35 |
| l_para_lines | 3 [0, 9.43] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.802 [0.625, 0.904] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 3.25] | 0 .. 4 |
| l_initial_forms_share | 0.437 [0.347, 0.54] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 3] | 0 .. 4 |
| l_line_initial_p | 0.273 [0, 0.712] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.241] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.724] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 99, Finnish 1


## zl_glyph: sınıf sınıf

### slotcite: taze medyan mesafe 2.51, en iyi 1.55

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| edge_mi | -3.6 | 0.199 | -0.008 |
| hapax_ratio | -2.8 | 0.715 | 0.623 |
| n_symbols | -2.4 | 44.750 | 22.000 |
| vocab_ed1_density | +2.1 | 0.852 | 0.886 |
| h2_over_h1 | +2.0 | 0.554 | 0.638 |
| first_entropy_ratio | -1.9 | 0.875 | 0.828 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.17 [5.61, 9.88] | 5 .. 13 |
| l_width_jitter | 0.206 [0.12, 0.294] | 0 .. 0.35 |
| l_para_lines | 4.8 [0, 12.7] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.593] | 0.2 .. 3 |
| l_allo_rate | 0.0238 [0, 0.0723] | 0.01 .. 0.15 |
| l_final_forms_share | 0.673 [0.51, 0.788] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.427 [0.227, 0.54] | 0.1 .. 0.9 |
| l_line_final_p | 0.161 [0, 0.291] | 0.1 .. 0.9 |
| l_para_initial_p | 0.687 [0.327, 0.912] | 0.3 .. 1 |
| p_alphabet | 17 [16, 19] | 15 .. 25 |
| p_slot_overlap | 0.512 [0.277, 0.712] | 0 .. 1 |
| p_n_edge | 36 [30, 40] | 5 .. 40 |
| p_n_mid | 22 [15.8, 33] | 10 .. 120 |
| p_empty | 0.302 [0.24, 0.343] | 0 .. 0.6 |
| p_len_edge | 3 [3, 3] | 1 .. 3 |
| p_len_mid | 2 [2, 3] | 2 .. 5 |
| p_copy | 0.715 [0.635, 0.782] | 0.5 .. 0.97 |
| p_exact | 0.289 [0.139, 0.438] | 0.1 .. 0.7 |
| p_reach | 16 [9, 23] | 1 .. 30 |
| p_same_line | 0.0449 [0.00577, 0.0823] | 0 .. 0.5 |
| p_mut_prefix | 0.289 [0.157, 0.464] | 0 .. 1 |
| p_mut_mid | 0.495 [0.154, 0.73] | 0 .. 1 |
| p_mut_suffix | 0.27 [0.179, 0.415] | 0 .. 1 |

### grille: taze medyan mesafe 2.56, en iyi 1.57

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| edge_mi | -3.5 | 0.199 | -0.004 |
| wlen_autocorr1 | -2.6 | 0.102 | -0.001 |
| jsd_line_final | -2.6 | 0.110 | 0.013 |
| n_symbols | -2.3 | 44.750 | 23.000 |
| h2_over_h1 | +2.0 | 0.554 | 0.634 |
| h2 | +1.8 | 2.127 | 2.432 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.56 [6.08, 9.94] | 5 .. 13 |
| l_width_jitter | 0.106 [0.0247, 0.228] | 0 .. 0.35 |
| l_para_lines | 0 [0, 5.24] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.73] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0433] | 0.01 .. 0.15 |
| l_final_forms_share | 0.602 [0.477, 0.713] | 0.1 .. 1 |
| l_final_forms_k | 3 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.104] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.322 [0, 0.503] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.168] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.3] | 0.3 .. 1 |
| p_alphabet | 19 [17, 21] | 15 .. 25 |
| p_rows | 1.56e+03 [1.08e+03, 2.25e+03] | 60 .. 3000 |
| p_slot_overlap | 0.421 [0.268, 0.676] | 0 .. 1 |
| p_n_edge | 32 [24, 40] | 5 .. 40 |
| p_n_mid | 34 [17, 57.2] | 10 .. 120 |
| p_empty | 0.403 [0.335, 0.451] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_n_grilles | 7 [5, 8] | 3 .. 8 |

### selfcite: taze medyan mesafe 2.64, en iyi 1.92

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -4.3 | 0.715 | 0.577 |
| h2_over_h1 | +4.0 | 0.554 | 0.717 |
| vocab_ed1_density | +3.9 | 0.852 | 0.914 |
| h2 | +3.7 | 2.127 | 2.764 |
| edge_mi | -3.5 | 0.199 | -0.002 |
| rep_adjacent_exact | +2.6 | 0.008 | 0.015 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 11.6 [9.81, 12.9] | 5 .. 13 |
| l_width_jitter | 0.217 [0.127, 0.29] | 0 .. 0.35 |
| l_para_lines | 8.76 [0, 11.2] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.245] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0555] | 0.01 .. 0.15 |
| l_final_forms_share | 0.642 [0.545, 0.727] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.103] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.505 [0.316, 0.673] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.281] | 0.1 .. 0.9 |
| l_para_initial_p | 0.403 [0, 0.749] | 0.3 .. 1 |
| p_alphabet | 17 [16, 18] | 15 .. 25 |
| p_glyph_classes | 6 [4, 7] | 4 .. 7 |
| p_copy | 0.863 [0.85, 0.903] | 0.85 .. 0.97 |
| p_exact | 0.515 [0.386, 0.588] | 0.2 .. 0.8 |
| p_reach | 23.5 [17.8, 30] | 1 .. 30 |
| p_same_line | 0.0139 [0.000889, 0.0324] | 0 .. 0.3 |
| p_slot_overlap | 0.277 [0.0844, 0.578] | 0 .. 1 |
| p_affix | 0.817 [0.76, 0.872] | 0.3 .. 0.9 |
| p_mut_substitute | 0.349 [0.133, 0.624] | 0 .. 1 |
| p_mut_prefix | 0.522 [0.395, 0.676] | 0 .. 1 |
| p_mut_delete | 0.137 [0.0555, 0.254] | 0 .. 1 |
| p_mut_double | 0.0883 [0.0301, 0.184] | 0 .. 1 |

### slotgram: taze medyan mesafe 2.79, en iyi 1.64

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| edge_mi | -3.5 | 0.199 | -0.005 |
| vocab_ed1_density | +3.0 | 0.852 | 0.900 |
| n_symbols | -2.6 | 44.750 | 20.000 |
| wlen_autocorr1 | -2.3 | 0.102 | 0.010 |
| zipf_slope | +1.9 | -0.785 | -0.655 |
| jsd_line_final | -1.9 | 0.110 | 0.039 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.21 [5.73, 10.1] | 5 .. 13 |
| l_width_jitter | 0.145 [0.0622, 0.232] | 0 .. 0.35 |
| l_para_lines | 6.96 [0, 11.7] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0222] | 0.01 .. 0.15 |
| l_final_forms_share | 0.709 [0.564, 0.812] | 0.1 .. 1 |
| l_final_forms_k | 3 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.422 [0, 0.742] | 0.1 .. 0.9 |
| l_line_final_p | 0.147 [0, 0.308] | 0.1 .. 0.9 |
| l_para_initial_p | 0.3 [0, 0.7] | 0.3 .. 1 |
| p_alphabet | 19 [17, 20.2] | 15 .. 25 |
| p_n_slots | 5 [4, 6] | 3 .. 8 |
| p_slot_overlap | 0.34 [0.146, 0.534] | 0 .. 1 |
| p_n_inv | 9 [6, 12.2] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.424 [0.366, 0.492] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0.614] | 0.3 .. 0.95 |
| p_exact | 0.22 [0.0852, 0.358] | 0 .. 0.5 |
| p_reach | 8.5 [4, 17.2] | 1 .. 30 |
| p_same_line | 0.0988 [0.00601, 0.31] | 0 .. 0.5 |

### verbose: taze medyan mesafe 2.90, en iyi 2.12

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +6.7 | 1.615 | 1.987 |
| jsd_last | -3.8 | 0.712 | 0.538 |
| wlen_autocorr1 | -3.5 | 0.102 | -0.036 |
| wlen_skew | +3.4 | 0.154 | 0.495 |
| wlen_frac1 | +3.0 | 0.033 | 0.065 |
| rep_adjacent_exact | -2.8 | 0.008 | 0.002 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.35 [5.72, 10.4] | 5 .. 13 |
| l_width_jitter | 0.22 [0.121, 0.3] | 0 .. 0.35 |
| l_para_lines | 3 [0, 7.18] | 3 .. 15 |
| l_allo_per_glyph | 1.61 [1.08, 2.06] | 0.2 .. 3 |
| l_allo_rate | 0.0544 [0.0411, 0.0723] | 0.01 .. 0.15 |
| l_final_forms_share | 0.293 [0, 0.488] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.453 [0, 0.632] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.276] | 0.1 .. 0.9 |
| l_para_initial_p | 0.322 [0, 0.507] | 0.3 .. 1 |
| p_alphabet | 14 [13, 16] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.563 [0.459, 0.643] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 68, Czech 12, Croatian 9, Romanian 7, Spanish 3

### plain: taze medyan mesafe 3.00, en iyi 2.51

Voynich'ten 2 birimden fazla sapan feature sayısı: 19

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | -5.5 | 1.615 | 1.311 |
| last_entropy_ratio | -5.4 | 0.636 | 0.302 |
| vocab_ed1_density | -5.1 | 0.852 | 0.771 |
| h2 | +4.4 | 2.127 | 2.901 |
| h2_over_h1 | +4.4 | 0.554 | 0.734 |
| char_double_rate | -4.2 | 0.076 | 0.009 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.1 [7.75, 11.9] | 5 .. 13 |
| l_width_jitter | 0.233 [0.135, 0.3] | 0 .. 0.35 |
| l_para_lines | 0 [0, 9.41] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.01] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.795 [0.698, 0.881] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.44] | 0.1 .. 0.9 |
| l_line_final_p | 0.181 [0, 0.318] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.52] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### codebook: taze medyan mesafe 3.26, en iyi 2.32

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | -7.1 | 1.615 | 1.219 |
| vocab_ed1_density | +7.0 | 0.852 | 0.965 |
| jsd_last | +3.9 | 0.712 | 0.893 |
| type_len_mean | -3.6 | 4.989 | 4.145 |
| wlen_skew | -3.6 | 0.154 | -0.207 |
| edge_mi | -3.4 | 0.199 | 0.004 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.98 [5.53, 9.21] | 5 .. 13 |
| l_width_jitter | 0.108 [0.0432, 0.187] | 0 .. 0.35 |
| l_para_lines | 0 [0, 3.97] | 3 .. 15 |
| l_allo_per_glyph | 2.52 [2.19, 2.88] | 0.2 .. 3 |
| l_allo_rate | 0.113 [0.0798, 0.139] | 0.01 .. 0.15 |
| l_final_forms_share | 0.843 [0.694, 0.929] | 0.1 .. 1 |
| l_final_forms_k | 3.5 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.227] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.0287] | 0.1 .. 0.9 |
| l_para_initial_p | 0.401 [0, 0.718] | 0.3 .. 1 |
| p_alphabet | 15 [15, 16] | 15 .. 25 |
| p_n_slots | 5 [5, 6] | 3 .. 6 |
| p_slot_overlap | 0.00303 [0, 0.0222] | 0 .. 1 |
| p_len_max | 2 [1, 2] | 1 .. 2 |
| p_zero_empty | 1 [1, 1] | 0 .. 1 |
| p_order | 0 [0, 1] | 0 .. 2 |

Kaynak dil (son nüfusta en sık): Turkish 71, Latin 14, Romanian 5, Russian 3, Czech 2

### abjad: taze medyan mesafe 3.29, en iyi 2.55

Voynich'ten 2 birimden fazla sapan feature sayısı: 17

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +7.3 | 0.033 | 0.111 |
| wlen_frac_le2 | +6.5 | 0.119 | 0.335 |
| wlen_skew | +5.3 | 0.154 | 0.694 |
| vocab_ed1_density | -4.2 | 0.852 | 0.785 |
| h2_over_h1 | +4.1 | 0.554 | 0.724 |
| h2 | +3.9 | 2.127 | 2.806 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.95 [5.55, 8.82] | 5 .. 13 |
| l_width_jitter | 0.176 [0.0733, 0.296] | 0 .. 0.35 |
| l_para_lines | 8.29 [3.73, 14.1] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.771 [0.668, 0.823] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.21 [0, 0.43] | 0.1 .. 1 |
| l_initial_forms_k | 1 [1, 2] | 0 .. 4 |
| l_line_initial_p | 0.05 [0, 0.427] | 0.1 .. 0.9 |
| l_line_final_p | 0.157 [0, 0.323] | 0.1 .. 0.9 |
| l_para_initial_p | 0.401 [0, 0.635] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100

### automaton: taze medyan mesafe 3.74, en iyi 1.83

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| first_entropy_ratio | -8.5 | 0.875 | 0.663 |
| jsd_first | +7.7 | 0.351 | 0.705 |
| wlen_skew | +5.1 | 0.154 | 0.671 |
| char_double_rate | -4.7 | 0.076 | 0.001 |
| jsd_last | -4.6 | 0.712 | 0.499 |
| wlen_frac1 | -3.1 | 0.033 | 0.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.48 [5.37, 8.91] | 5 .. 13 |
| l_width_jitter | 0.178 [0.0628, 0.279] | 0 .. 0.35 |
| l_para_lines | 5.55 [3, 10.9] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.339] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0.221] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.545 [0.402, 0.694] | 0.1 .. 0.9 |
| l_line_final_p | 0.05 [0, 0.337] | 0.1 .. 0.9 |
| l_para_initial_p | 0.606 [0.225, 0.811] | 0.3 .. 1 |
| p_alphabet | 16 [15, 17] | 15 .. 25 |
| p_levels | 6 [5, 7] | 3 .. 8 |
| p_out_degree | 6 [5, 7] | 2 .. 8 |
| p_concentration | 2.1 [1.66, 2.66] | 0.2 .. 3 |
| p_stay | 0.425 [0.318, 0.512] | 0 .. 1 |
| p_end_from | 2 [1, 3] | 1 .. 3 |
| p_link | 0.271 [0, 0.616] | 0.1 .. 1 |
