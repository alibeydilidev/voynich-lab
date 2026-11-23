# Yönlendirilmiş arama raporu: her hipotezin ulaşabildiği en iyi nokta

Her (sınıf, görünüm) için 5 tur, tur başına 600 deneme, en yakın 100 ayar tutuldu. Tablolardaki mesafeler, son turda kalan ayarların her biriyle yeniden üretilen 2 taze örnekten hesaplandı (toplam 200).

Mesafe birimi ve ölçüt `abc.md` ile aynı: bir hipotezin taze örnekleri Voynich öz mesafesinin içine giriyorsa, o hipotez bu feature kümesinde Voynich'ten ayırt edilemez.

## 1. Taze örneklerin medyan mesafesi (parantezde rejection ABC'deki değer)

| görünüm | Voynich öz mesafesi (medyan, en çok) | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.91, 1.65 | 6.08 (6.16) | 3.19 (2.77) | 4.07 (5.42) | 3.78 (4.46) | 3.27 (3.17) | 3.88 (3.19) | 3.80 (4.00) |
| eva_glyph | 0.96, 1.64 | 3.61 (3.96) | 2.75 (2.46) | 3.05 (4.29) | 2.96 (3.58) | 3.03 (2.84) | 3.17 (2.86) | 3.47 (3.70) |
| v101 | 0.97, 1.42 | 2.94 (3.22) | 3.52 (2.54) | 2.66 (3.11) | 3.22 (3.84) | 3.47 (3.02) | 3.52 (2.83) | 3.33 (3.43) |
| zl_basic | 0.96, 1.52 | 5.04 (5.33) | 3.04 (2.43) | 3.66 (4.75) | 3.36 (4.00) | 3.12 (2.76) | 3.39 (2.86) | 3.13 (3.37) |
| zl_glyph | 1.03, 1.43 | 3.23 (3.53) | 2.44 (2.15) | 2.90 (3.94) | 2.58 (3.17) | 2.73 (2.43) | 3.00 (2.54) | 2.81 (3.01) |

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
| eva_basic | abjad | 5.99 -> 5.77 -> 5.75 -> 5.57 -> 5.49 |
| eva_basic | grille | 2.91 -> 2.80 -> 2.69 -> 2.64 -> 2.56 |
| eva_basic | plain | 5.07 -> 4.31 -> 3.99 -> 3.90 -> 3.81 |
| eva_basic | selfcite | 4.13 -> 3.77 -> 3.50 -> 3.33 -> 3.25 |
| eva_basic | slotcite | 3.11 -> 3.06 -> 2.96 -> 2.85 -> 2.73 |
| eva_basic | slotgram | 3.45 -> 3.10 -> 3.07 -> 3.17 -> 3.12 |
| eva_basic | verbose | 3.74 -> 3.62 -> 3.45 -> 3.41 -> 3.35 |
| eva_glyph | abjad | 3.73 -> 3.47 -> 3.41 -> 3.31 -> 3.27 |
| eva_glyph | grille | 2.68 -> 2.47 -> 2.43 -> 2.29 -> 2.34 |
| eva_glyph | plain | 3.78 -> 3.11 -> 2.87 -> 2.80 -> 2.75 |
| eva_glyph | selfcite | 3.29 -> 3.09 -> 2.87 -> 2.77 -> 2.62 |
| eva_glyph | slotcite | 2.90 -> 2.74 -> 2.65 -> 2.51 -> 2.53 |
| eva_glyph | slotgram | 3.01 -> 2.96 -> 3.00 -> 2.78 -> 2.71 |
| eva_glyph | verbose | 3.62 -> 3.36 -> 3.19 -> 3.18 -> 3.05 |
| v101 | abjad | 2.95 -> 2.81 -> 2.72 -> 2.68 -> 2.66 |
| v101 | grille | 2.91 -> 2.87 -> 2.79 -> 2.70 -> 2.72 |
| v101 | plain | 2.76 -> 2.54 -> 2.46 -> 2.40 -> 2.40 |
| v101 | selfcite | 3.61 -> 3.44 -> 3.15 -> 3.00 -> 2.93 |
| v101 | slotcite | 3.25 -> 3.09 -> 2.92 -> 2.79 -> 2.75 |
| v101 | slotgram | 3.07 -> 3.16 -> 3.05 -> 2.95 -> 2.83 |
| v101 | verbose | 3.30 -> 3.21 -> 3.14 -> 2.95 -> 2.83 |
| zl_basic | abjad | 5.21 -> 4.96 -> 4.90 -> 4.79 -> 4.65 |
| zl_basic | grille | 2.68 -> 2.53 -> 2.47 -> 2.41 -> 2.45 |
| zl_basic | plain | 4.18 -> 3.75 -> 3.58 -> 3.51 -> 3.46 |
| zl_basic | selfcite | 3.70 -> 3.39 -> 3.17 -> 3.08 -> 2.96 |
| zl_basic | slotcite | 2.92 -> 2.70 -> 2.60 -> 2.52 -> 2.49 |
| zl_basic | slotgram | 3.05 -> 2.92 -> 2.91 -> 2.84 -> 2.74 |
| zl_basic | verbose | 3.17 -> 3.08 -> 2.93 -> 2.76 -> 2.70 |
| zl_glyph | abjad | 3.33 -> 3.16 -> 3.04 -> 3.01 -> 3.00 |
| zl_glyph | grille | 2.38 -> 2.21 -> 2.13 -> 2.16 -> 2.07 |
| zl_glyph | plain | 3.37 -> 3.03 -> 2.85 -> 2.77 -> 2.74 |
| zl_glyph | selfcite | 2.83 -> 2.61 -> 2.49 -> 2.35 -> 2.20 |
| zl_glyph | slotcite | 2.55 -> 2.46 -> 2.30 -> 2.26 -> 2.26 |
| zl_glyph | slotgram | 2.70 -> 2.57 -> 2.58 -> 2.37 -> 2.43 |
| zl_glyph | verbose | 2.90 -> 2.70 -> 2.60 -> 2.51 -> 2.40 |

## eva_basic: sınıf sınıf

### grille: taze medyan mesafe 3.19, en iyi 1.79

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| h2_over_h1 | +3.5 | 0.524 | 0.632 |
| wlen_autocorr1 | -3.5 | 0.127 | -0.005 |
| h2 | +3.2 | 2.016 | 2.407 |
| jsd_line_final | -3.1 | 0.109 | 0.009 |
| rep_adjacent_ed1 | -2.6 | 0.032 | 0.015 |
| rep_within3 | -2.5 | 0.026 | 0.008 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.81 [5.96, 10.2] | 5 .. 13 |
| l_width_jitter | 0.271 [0.169, 0.33] | 0 .. 0.35 |
| l_para_lines | 4.58 [0, 8.82] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0355] | 0.01 .. 0.15 |
| l_final_forms_share | 0.644 [0.492, 0.757] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.195 [0, 0.52] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.19] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.582] | 0.3 .. 1 |
| p_alphabet | 19 [17.8, 21] | 15 .. 25 |
| p_rows | 1.37e+03 [701, 1.96e+03] | 60 .. 3000 |
| p_slot_overlap | 0.429 [0.196, 0.619] | 0 .. 1 |
| p_n_edge | 26.5 [19.8, 32.2] | 5 .. 40 |
| p_n_mid | 40.5 [24, 74] | 10 .. 120 |
| p_empty | 0.269 [0.214, 0.315] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3.5 [3, 4] | 2 .. 5 |
| p_n_grilles | 6 [4, 7] | 3 .. 8 |

### slotcite: taze medyan mesafe 3.27, en iyi 2.02

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -5.2 | 0.717 | 0.601 |
| h2_over_h1 | +3.4 | 0.524 | 0.631 |
| h2 | +3.2 | 2.016 | 2.407 |
| jsd_line_final | -3.1 | 0.109 | 0.009 |
| zipf_slope | +2.6 | -0.778 | -0.613 |
| wlen_autocorr1 | -2.2 | 0.127 | 0.043 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.21 [6.74, 10.8] | 5 .. 13 |
| l_width_jitter | 0.268 [0.143, 0.326] | 0 .. 0.35 |
| l_para_lines | 5.24 [0, 9.6] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.602 [0.412, 0.734] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.458 [0, 0.639] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.171] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.397] | 0.3 .. 1 |
| p_alphabet | 20 [17.8, 21.2] | 15 .. 25 |
| p_slot_overlap | 0.398 [0.177, 0.701] | 0 .. 1 |
| p_n_edge | 26.5 [18, 33] | 5 .. 40 |
| p_n_mid | 39.5 [24.8, 51.2] | 10 .. 120 |
| p_empty | 0.254 [0.185, 0.319] | 0 .. 0.6 |
| p_len_edge | 3 [3, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_copy | 0.576 [0.513, 0.643] | 0.5 .. 0.97 |
| p_exact | 0.245 [0.123, 0.453] | 0.1 .. 0.7 |
| p_reach | 8 [3, 20.2] | 1 .. 30 |
| p_same_line | 0.0861 [0.0501, 0.147] | 0 .. 0.5 |
| p_mut_prefix | 0.471 [0.252, 0.754] | 0 .. 1 |
| p_mut_mid | 0.253 [0.128, 0.421] | 0 .. 1 |
| p_mut_suffix | 0.222 [0.0555, 0.389] | 0 .. 1 |

### selfcite: taze medyan mesafe 3.78, en iyi 2.42

Voynich'ten 2 birimden fazla sapan feature sayısı: 13

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -6.0 | 0.717 | 0.584 |
| h2_over_h1 | +5.5 | 0.524 | 0.695 |
| h2 | +5.4 | 2.016 | 2.672 |
| type_len_mean | -4.9 | 5.692 | 4.851 |
| vocab_ed1_density | +4.2 | 0.823 | 0.927 |
| char_double_rate | +3.6 | 0.067 | 0.117 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.68 [5.26, 8.57] | 5 .. 13 |
| l_width_jitter | 0.133 [0.063, 0.211] | 0 .. 0.35 |
| l_para_lines | 3.68 [0, 6.97] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.627 [0.413, 0.78] | 0.1 .. 1 |
| l_final_forms_k | 2 [0, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.204] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.579 [0.135, 0.779] | 0.1 .. 0.9 |
| l_line_final_p | 0.201 [0, 0.346] | 0.1 .. 0.9 |
| l_para_initial_p | 0.616 [0, 0.833] | 0.3 .. 1 |
| p_alphabet | 16 [15, 18] | 15 .. 25 |
| p_glyph_classes | 5 [4, 5] | 4 .. 7 |
| p_copy | 0.869 [0.856, 0.899] | 0.85 .. 0.97 |
| p_exact | 0.461 [0.314, 0.638] | 0.2 .. 0.8 |
| p_reach | 23.5 [17.8, 28] | 1 .. 30 |
| p_same_line | 0.0391 [0.0105, 0.0756] | 0 .. 0.3 |
| p_slot_overlap | 0.124 [0.00252, 0.259] | 0 .. 1 |
| p_affix | 0.856 [0.8, 0.894] | 0.3 .. 0.9 |
| p_mut_substitute | 0.304 [0.0653, 0.462] | 0 .. 1 |
| p_mut_prefix | 0.691 [0.457, 0.895] | 0 .. 1 |
| p_mut_delete | 0.0683 [0.0274, 0.0962] | 0 .. 1 |
| p_mut_double | 0.0618 [0.0168, 0.107] | 0 .. 1 |

### verbose: taze medyan mesafe 3.80, en iyi 2.30

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -6.9 | 0.717 | 0.563 |
| wlen_frac_le2 | +5.4 | 0.077 | 0.140 |
| wlen_std | +4.7 | 1.693 | 2.039 |
| first_entropy_ratio | +4.7 | 0.806 | 0.891 |
| wlen_skew | +4.4 | 0.074 | 0.636 |
| wlen_autocorr1 | -4.1 | 0.127 | -0.030 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.53 [5.57, 8.86] | 5 .. 13 |
| l_width_jitter | 0.141 [0.0661, 0.292] | 0 .. 0.35 |
| l_para_lines | 9.15 [0, 12.6] | 3 .. 15 |
| l_allo_per_glyph | 0.237 [0, 0.671] | 0.2 .. 3 |
| l_allo_rate | 0.0566 [0, 0.0876] | 0.01 .. 0.15 |
| l_final_forms_share | 0.626 [0.394, 0.796] | 0.1 .. 1 |
| l_final_forms_k | 2 [0.75, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.439 [0.237, 0.611] | 0.1 .. 0.9 |
| l_line_final_p | 0.248 [0, 0.445] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.549] | 0.3 .. 1 |
| p_alphabet | 13 [12, 15] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.375 [0.3, 0.419] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Czech 49, Italian 21, Romanian 14, Croatian 8, Russian 3

### slotgram: taze medyan mesafe 3.88, en iyi 2.26

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| zipf_slope | +4.2 | -0.778 | -0.517 |
| jsd_line_final | -3.1 | 0.109 | 0.011 |
| h2_over_h1 | +3.0 | 0.524 | 0.617 |
| wlen_autocorr1 | -2.9 | 0.127 | 0.017 |
| hapax_ratio | -2.6 | 0.717 | 0.660 |
| top10_coverage | -2.5 | 0.171 | 0.081 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.59 [6.79, 11.9] | 5 .. 13 |
| l_width_jitter | 0.236 [0.126, 0.312] | 0 .. 0.35 |
| l_para_lines | 8.56 [0, 12.1] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.486 [0.301, 0.692] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.133 [0, 0.526] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.147] | 0.1 .. 0.9 |
| l_para_initial_p | 0.452 [0, 0.723] | 0.3 .. 1 |
| p_alphabet | 20 [17, 22] | 15 .. 25 |
| p_n_slots | 6 [5, 7] | 3 .. 8 |
| p_slot_overlap | 0.537 [0.249, 0.83] | 0 .. 1 |
| p_n_inv | 6 [4, 9.25] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.42 [0.334, 0.494] | 0.1 .. 0.8 |
| p_copy | 0.324 [0, 0.539] | 0.3 .. 0.95 |
| p_exact | 0.169 [0.0706, 0.363] | 0 .. 0.5 |
| p_reach | 10 [4, 17] | 1 .. 30 |
| p_same_line | 0.14 [0.0458, 0.295] | 0 .. 0.5 |

### plain: taze medyan mesafe 4.07, en iyi 3.29

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -7.0 | 0.628 | 0.198 |
| wlen_frac_le2 | +6.7 | 0.077 | 0.154 |
| type_len_mean | -6.7 | 5.692 | 4.546 |
| h2 | +6.7 | 2.016 | 2.824 |
| first_entropy_ratio | +6.6 | 0.806 | 0.925 |
| h2_over_h1 | +6.4 | 0.524 | 0.721 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.51 [5.98, 9.01] | 5 .. 13 |
| l_width_jitter | 0.195 [0.0635, 0.284] | 0 .. 0.35 |
| l_para_lines | 10.9 [3, 14] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.903 [0.833, 0.967] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.0255] | 0.1 .. 1 |
| l_initial_forms_k | 1 [1, 1] | 0 .. 4 |
| l_line_initial_p | 0.246 [0, 0.508] | 0.1 .. 0.9 |
| l_line_final_p | 0.273 [0, 0.371] | 0.1 .. 0.9 |
| l_para_initial_p | 0.354 [0, 0.795] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 98, Arabic 2

### abjad: taze medyan mesafe 6.08, en iyi 4.85

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +22.8 | 0.077 | 0.341 |
| wlen_frac1 | +8.8 | 0.017 | 0.116 |
| type_len_mean | -7.4 | 5.692 | 4.421 |
| wlen_mean | -7.3 | 5.066 | 3.365 |
| eff_symbols | +6.6 | 14.240 | 16.396 |
| first_entropy_ratio | +6.1 | 0.806 | 0.915 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.5 [7.24, 11.8] | 5 .. 13 |
| l_width_jitter | 0.201 [0.11, 0.298] | 0 .. 0.35 |
| l_para_lines | 8.11 [0, 13.6] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.833 [0.683, 0.914] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0.359 [0, 0.536] | 0.1 .. 1 |
| l_initial_forms_k | 1 [1, 2] | 0 .. 4 |
| l_line_initial_p | 0.44 [0, 0.711] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.212] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 98, Finnish 2


## eva_glyph: sınıf sınıf

### grille: taze medyan mesafe 2.75, en iyi 1.46

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -3.2 | 0.103 | -0.003 |
| jsd_line_final | -3.0 | 0.110 | 0.013 |
| h2_over_h1 | +2.7 | 0.556 | 0.657 |
| n_symbols | -2.6 | 25.250 | 22.000 |
| h2 | +2.4 | 2.131 | 2.509 |
| rep_within3 | -2.3 | 0.026 | 0.010 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.75 [5.17, 10.2] | 5 .. 13 |
| l_width_jitter | 0.188 [0.128, 0.265] | 0 .. 0.35 |
| l_para_lines | 0 [0, 7.58] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.727] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.668 [0.539, 0.792] | 0.1 .. 1 |
| l_final_forms_k | 2.5 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.343 [0, 0.511] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.247] | 0.1 .. 0.9 |
| l_para_initial_p | 0.15 [0, 0.502] | 0.3 .. 1 |
| p_alphabet | 18 [16.8, 21] | 15 .. 25 |
| p_rows | 1.22e+03 [635, 1.77e+03] | 60 .. 3000 |
| p_slot_overlap | 0.726 [0.481, 0.883] | 0 .. 1 |
| p_n_edge | 27 [19, 33] | 5 .. 40 |
| p_n_mid | 57.5 [36, 94.5] | 10 .. 120 |
| p_empty | 0.319 [0.264, 0.394] | 0 .. 0.6 |
| p_len_edge | 2 [2, 2] | 1 .. 3 |
| p_len_mid | 4 [3, 4] | 2 .. 5 |
| p_n_grilles | 6 [4, 7] | 3 .. 8 |

### selfcite: taze medyan mesafe 2.96, en iyi 2.14

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -5.1 | 0.717 | 0.605 |
| h2_over_h1 | +4.1 | 0.556 | 0.711 |
| h2 | +3.9 | 2.131 | 2.740 |
| vocab_ed1_density | +3.7 | 0.850 | 0.932 |
| char_double_rate | +3.4 | 0.076 | 0.126 |
| zipf_slope | +2.9 | -0.778 | -0.595 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.32 [6.13, 8.78] | 5 .. 13 |
| l_width_jitter | 0.0934 [0.0428, 0.17] | 0 .. 0.35 |
| l_para_lines | 6.85 [4.22, 10.3] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.563 [0.469, 0.679] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0.281 [0, 0.359] | 0.1 .. 1 |
| l_initial_forms_k | 3 [2, 3.25] | 0 .. 4 |
| l_line_initial_p | 0.389 [0, 0.686] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.272] | 0.1 .. 0.9 |
| l_para_initial_p | 0.723 [0.39, 0.893] | 0.3 .. 1 |
| p_alphabet | 17 [15, 19] | 15 .. 25 |
| p_glyph_classes | 5 [4, 6] | 4 .. 7 |
| p_copy | 0.87 [0.85, 0.906] | 0.85 .. 0.97 |
| p_exact | 0.364 [0.244, 0.573] | 0.2 .. 0.8 |
| p_reach | 25 [20, 30] | 1 .. 30 |
| p_same_line | 0.0328 [0.00936, 0.0597] | 0 .. 0.3 |
| p_slot_overlap | 0.142 [0.0457, 0.298] | 0 .. 1 |
| p_affix | 0.801 [0.683, 0.882] | 0.3 .. 0.9 |
| p_mut_substitute | 0.399 [0.296, 0.544] | 0 .. 1 |
| p_mut_prefix | 0.533 [0.427, 0.641] | 0 .. 1 |
| p_mut_delete | 0.138 [0.0789, 0.209] | 0 .. 1 |
| p_mut_double | 0.123 [0.0761, 0.174] | 0 .. 1 |

### slotcite: taze medyan mesafe 3.03, en iyi 1.71

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| hapax_ratio | -3.9 | 0.717 | 0.630 |
| jsd_line_final | -2.6 | 0.110 | 0.026 |
| h2_over_h1 | +2.6 | 0.556 | 0.655 |
| h2 | +2.5 | 2.131 | 2.524 |
| zipf_slope | +2.3 | -0.778 | -0.631 |
| rep_adjacent_exact | +2.2 | 0.009 | 0.016 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.75 [7.35, 12.2] | 5 .. 13 |
| l_width_jitter | 0.214 [0.127, 0.287] | 0 .. 0.35 |
| l_para_lines | 5.95 [0, 9.92] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.622] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0892] | 0.01 .. 0.15 |
| l_final_forms_share | 0.497 [0.353, 0.65] | 0.1 .. 1 |
| l_final_forms_k | 1.5 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.462 [0.112, 0.679] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.235] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.736] | 0.3 .. 1 |
| p_alphabet | 18 [16, 20] | 15 .. 25 |
| p_slot_overlap | 0.718 [0.427, 0.915] | 0 .. 1 |
| p_n_edge | 30 [22, 39.2] | 5 .. 40 |
| p_n_mid | 44.5 [25, 72] | 10 .. 120 |
| p_empty | 0.275 [0.202, 0.342] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_copy | 0.721 [0.612, 0.815] | 0.5 .. 0.97 |
| p_exact | 0.168 [0.103, 0.287] | 0.1 .. 0.7 |
| p_reach | 8.5 [4, 18] | 1 .. 30 |
| p_same_line | 0.117 [0.0527, 0.224] | 0 .. 0.5 |
| p_mut_prefix | 0.388 [0.25, 0.562] | 0 .. 1 |
| p_mut_mid | 0.379 [0.267, 0.52] | 0 .. 1 |
| p_mut_suffix | 0.382 [0.259, 0.557] | 0 .. 1 |

### plain: taze medyan mesafe 3.05, en iyi 2.50

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -5.9 | 0.626 | 0.285 |
| h2 | +4.9 | 2.131 | 2.901 |
| h2_over_h1 | +4.8 | 0.556 | 0.736 |
| char_double_rate | -4.6 | 0.076 | 0.009 |
| wlen_std | -4.5 | 1.552 | 1.319 |
| eff_symbols | +4.1 | 14.404 | 16.337 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 6.87 [5.95, 8.94] | 5 .. 13 |
| l_width_jitter | 0.157 [0.0512, 0.264] | 0 .. 0.35 |
| l_para_lines | 7.88 [0, 11.4] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.842 [0.752, 0.916] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.176 [0, 0.506] | 0.1 .. 0.9 |
| l_line_final_p | 0.225 [0, 0.292] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.418] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### slotgram: taze medyan mesafe 3.17, en iyi 1.99

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| n_symbols | -3.5 | 25.250 | 21.000 |
| wlen_autocorr1 | -2.7 | 0.103 | 0.013 |
| wlen_frac1 | +2.6 | 0.017 | 0.047 |
| jsd_line_final | -2.6 | 0.110 | 0.028 |
| zipf_slope | +2.5 | -0.778 | -0.622 |
| wlen_frac_le2 | +2.3 | 0.099 | 0.172 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.95 [5.97, 11.3] | 5 .. 13 |
| l_width_jitter | 0.318 [0.189, 0.35] | 0 .. 0.35 |
| l_para_lines | 3.37 [0, 6.81] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.538 [0.386, 0.695] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.288 [0, 0.569] | 0.1 .. 0.9 |
| l_line_final_p | 0.1 [0, 0.275] | 0.1 .. 0.9 |
| l_para_initial_p | 0.417 [0, 0.699] | 0.3 .. 1 |
| p_alphabet | 20 [18, 23] | 15 .. 25 |
| p_n_slots | 5 [4, 5] | 3 .. 8 |
| p_slot_overlap | 0.278 [0.0957, 0.565] | 0 .. 1 |
| p_n_inv | 10 [7, 13] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.425 [0.384, 0.485] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0.414] | 0.3 .. 0.95 |
| p_exact | 0.265 [0.0795, 0.422] | 0 .. 0.5 |
| p_reach | 6 [2, 18.2] | 1 .. 30 |
| p_same_line | 0.131 [0.0426, 0.238] | 0 .. 0.5 |

### verbose: taze medyan mesafe 3.47, en iyi 2.54

Voynich'ten 2 birimden fazla sapan feature sayısı: 18

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +7.4 | 1.552 | 1.939 |
| hapax_ratio | -4.5 | 0.717 | 0.618 |
| wlen_skew | +4.0 | 0.183 | 0.606 |
| wlen_autocorr1 | -3.9 | 0.103 | -0.028 |
| jsd_first | -3.1 | 0.350 | 0.225 |
| wlen_frac1 | +3.1 | 0.017 | 0.053 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.97 [6.45, 10.6] | 5 .. 13 |
| l_width_jitter | 0.231 [0.125, 0.302] | 0 .. 0.35 |
| l_para_lines | 0 [0, 8.46] | 3 .. 15 |
| l_allo_per_glyph | 0.926 [0.655, 1.16] | 0.2 .. 3 |
| l_allo_rate | 0.105 [0.0738, 0.126] | 0.01 .. 0.15 |
| l_final_forms_share | 0.439 [0, 0.662] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.502 [0, 0.693] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.27] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.45] | 0.3 .. 1 |
| p_alphabet | 13 [12, 14] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.483 [0.367, 0.647] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0.304] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Croatian 45, Italian 18, Romanian 11, Finnish 9, Polish 4

### abjad: taze medyan mesafe 3.61, en iyi 2.83

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +8.3 | 0.017 | 0.114 |
| wlen_frac_le2 | +7.6 | 0.099 | 0.337 |
| wlen_skew | +4.6 | 0.183 | 0.672 |
| first_entropy_ratio | +4.5 | 0.867 | 0.967 |
| h2_over_h1 | +4.4 | 0.556 | 0.720 |
| h2 | +4.3 | 2.131 | 2.805 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.38 [5.83, 10.8] | 5 .. 13 |
| l_width_jitter | 0.219 [0.109, 0.312] | 0 .. 0.35 |
| l_para_lines | 7.2 [0, 10.8] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0185] | 0.01 .. 0.15 |
| l_final_forms_share | 0.735 [0.644, 0.833] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.211 [0, 0.352] | 0.1 .. 1 |
| l_initial_forms_k | 1 [1, 2] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.303] | 0.1 .. 0.9 |
| l_line_final_p | 0.152 [0, 0.291] | 0.1 .. 0.9 |
| l_para_initial_p | 0.403 [0, 0.826] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100


## v101: sınıf sınıf

### plain: taze medyan mesafe 2.66, en iyi 2.17

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| vocab_ed1_density | -4.7 | 0.854 | 0.746 |
| n_symbols | -4.6 | 69.529 | 26.000 |
| wlen_frac1 | -4.5 | 0.046 | 0.000 |
| last_entropy_ratio | -4.0 | 0.704 | 0.459 |
| h2 | +3.9 | 2.383 | 3.045 |
| h2_over_h1 | +3.7 | 0.595 | 0.750 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.31 [6.55, 11.1] | 5 .. 13 |
| l_width_jitter | 0.199 [0.12, 0.28] | 0 .. 0.35 |
| l_para_lines | 4.81 [0, 9.25] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.725 [0.619, 0.827] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.525] | 0.1 .. 0.9 |
| l_line_final_p | 0.159 [0, 0.255] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.494] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### abjad: taze medyan mesafe 2.94, en iyi 2.20

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +6.3 | 0.046 | 0.112 |
| wlen_frac_le2 | +5.7 | 0.184 | 0.336 |
| n_symbols | -4.7 | 69.529 | 25.000 |
| vocab_ed1_density | -3.7 | 0.854 | 0.769 |
| first_entropy_ratio | +3.4 | 0.886 | 0.996 |
| h2_over_h1 | +3.4 | 0.595 | 0.736 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.27 [5.19, 9.02] | 5 .. 13 |
| l_width_jitter | 0.218 [0.144, 0.299] | 0 .. 0.35 |
| l_para_lines | 8.2 [2.51, 11.9] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.96] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.755 [0.638, 0.858] | 0.1 .. 1 |
| l_final_forms_k | 4 [3, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.204] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.476] | 0.1 .. 0.9 |
| l_line_final_p | 0.309 [0.163, 0.402] | 0.1 .. 0.9 |
| l_para_initial_p | 0.15 [0, 0.541] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100

### selfcite: taze medyan mesafe 3.22, en iyi 2.24

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +8.3 | 0.015 | 0.060 |
| n_symbols | -4.4 | 69.529 | 28.000 |
| hapax_ratio | -3.7 | 0.741 | 0.632 |
| h2 | +3.1 | 2.383 | 2.915 |
| zipf_slope | +3.1 | -0.776 | -0.639 |
| h2_over_h1 | +3.1 | 0.595 | 0.724 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.3 [7.17, 12.3] | 5 .. 13 |
| l_width_jitter | 0.112 [0.045, 0.208] | 0 .. 0.35 |
| l_para_lines | 3.25 [0, 8.09] | 3 .. 15 |
| l_allo_per_glyph | 1.61 [0, 2.27] | 0.2 .. 3 |
| l_allo_rate | 0.0171 [0, 0.0867] | 0.01 .. 0.15 |
| l_final_forms_share | 0.746 [0.632, 0.872] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.417 [0, 0.636] | 0.1 .. 0.9 |
| l_line_final_p | 0.208 [0, 0.383] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.472] | 0.3 .. 1 |
| p_alphabet | 19 [17, 21] | 15 .. 25 |
| p_glyph_classes | 6 [5, 7] | 4 .. 7 |
| p_copy | 0.866 [0.851, 0.891] | 0.85 .. 0.97 |
| p_exact | 0.381 [0.273, 0.459] | 0.2 .. 0.8 |
| p_reach | 19 [14, 26.2] | 1 .. 30 |
| p_same_line | 0.00931 [0, 0.0297] | 0 .. 0.3 |
| p_slot_overlap | 0.602 [0.311, 0.817] | 0 .. 1 |
| p_affix | 0.657 [0.523, 0.84] | 0.3 .. 0.9 |
| p_mut_substitute | 0.485 [0.343, 0.655] | 0 .. 1 |
| p_mut_prefix | 0.413 [0.29, 0.606] | 0 .. 1 |
| p_mut_delete | 0.154 [0.0692, 0.294] | 0 .. 1 |
| p_mut_double | 0.00862 [0, 0.0288] | 0 .. 1 |

### verbose: taze medyan mesafe 3.33, en iyi 2.28

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +6.1 | 0.015 | 0.048 |
| wlen_std | +5.1 | 1.469 | 1.780 |
| jsd_last | -4.7 | 0.679 | 0.437 |
| wlen_frac1 | +3.9 | 0.046 | 0.086 |
| wlen_skew | +3.6 | 0.225 | 0.717 |
| wlen_autocorr1 | -3.5 | 0.179 | -0.032 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.47 [6.52, 10.5] | 5 .. 13 |
| l_width_jitter | 0.0821 [0.0365, 0.146] | 0 .. 0.35 |
| l_para_lines | 0 [0, 3.41] | 3 .. 15 |
| l_allo_per_glyph | 2.51 [1.93, 2.9] | 0.2 .. 3 |
| l_allo_rate | 0.103 [0.0836, 0.126] | 0.01 .. 0.15 |
| l_final_forms_share | 0 [0, 0.351] | 0.1 .. 1 |
| l_final_forms_k | 1 [0, 2] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.481] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.417] | 0.1 .. 0.9 |
| l_para_initial_p | 0.373 [0, 0.675] | 0.3 .. 1 |
| p_alphabet | 14 [12, 16.2] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.695 [0.627, 0.838] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Croatian 63, Turkish 10, Italian 10, Romanian 7, Czech 6

### slotcite: taze medyan mesafe 3.47, en iyi 1.89

Voynich'ten 2 birimden fazla sapan feature sayısı: 9

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +7.3 | 0.015 | 0.055 |
| wlen_std | -3.0 | 1.469 | 1.285 |
| vocab_ed1_density | +2.8 | 0.854 | 0.919 |
| jsd_line_final | -2.7 | 0.133 | 0.016 |
| wlen_autocorr1 | -2.5 | 0.179 | 0.029 |
| zipf_slope | +2.4 | -0.776 | -0.670 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.95 [5.85, 9.82] | 5 .. 13 |
| l_width_jitter | 0.254 [0.146, 0.324] | 0 .. 0.35 |
| l_para_lines | 7.52 [0, 12.1] | 3 .. 15 |
| l_allo_per_glyph | 2.28 [1.62, 2.77] | 0.2 .. 3 |
| l_allo_rate | 0.0511 [0.0219, 0.0924] | 0.01 .. 0.15 |
| l_final_forms_share | 0.607 [0.448, 0.796] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.552 [0.309, 0.715] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.166] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.362] | 0.3 .. 1 |
| p_alphabet | 22.5 [20, 24] | 15 .. 25 |
| p_slot_overlap | 0.7 [0.488, 0.862] | 0 .. 1 |
| p_n_edge | 20.5 [12.8, 29] | 5 .. 40 |
| p_n_mid | 44.5 [25, 80.2] | 10 .. 120 |
| p_empty | 0.305 [0.23, 0.351] | 0 .. 0.6 |
| p_len_edge | 2 [2, 2] | 1 .. 3 |
| p_len_mid | 2.5 [2, 3] | 2 .. 5 |
| p_copy | 0.617 [0.554, 0.713] | 0.5 .. 0.97 |
| p_exact | 0.2 [0.115, 0.343] | 0.1 .. 0.7 |
| p_reach | 12.5 [7, 23.2] | 1 .. 30 |
| p_same_line | 0.063 [0.0111, 0.121] | 0 .. 0.5 |
| p_mut_prefix | 0.213 [0.103, 0.373] | 0 .. 1 |
| p_mut_mid | 0.428 [0.281, 0.567] | 0 .. 1 |
| p_mut_suffix | 0.304 [0.0961, 0.51] | 0 .. 1 |

### slotgram: taze medyan mesafe 3.52, en iyi 2.01

Voynich'ten 2 birimden fazla sapan feature sayısı: 8

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| n_symbols | -4.5 | 69.529 | 27.000 |
| char_double_rate | +3.5 | 0.015 | 0.034 |
| wlen_autocorr1 | -2.9 | 0.179 | 0.008 |
| vocab_ed1_density | +2.8 | 0.854 | 0.918 |
| jsd_line_final | -2.5 | 0.133 | 0.023 |
| jsd_line_initial | -2.3 | 0.287 | 0.086 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.12 [6.54, 10.7] | 5 .. 13 |
| l_width_jitter | 0.236 [0.144, 0.314] | 0 .. 0.35 |
| l_para_lines | 3.46 [0, 7.8] | 3 .. 15 |
| l_allo_per_glyph | 1.67 [0, 2.16] | 0.2 .. 3 |
| l_allo_rate | 0.0261 [0, 0.104] | 0.01 .. 0.15 |
| l_final_forms_share | 0.651 [0.493, 0.794] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.391] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.42] | 0.1 .. 0.9 |
| l_para_initial_p | 0.425 [0, 0.71] | 0.3 .. 1 |
| p_alphabet | 21 [20, 24] | 15 .. 25 |
| p_n_slots | 5 [4, 7] | 3 .. 8 |
| p_slot_overlap | 0.634 [0.207, 0.923] | 0 .. 1 |
| p_n_inv | 10 [4, 19] | 2 .. 30 |
| p_len_max | 2 [1, 2] | 1 .. 2 |
| p_empty | 0.469 [0.358, 0.524] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0.545] | 0.3 .. 0.95 |
| p_exact | 0.327 [0.12, 0.454] | 0 .. 0.5 |
| p_reach | 10 [4, 22] | 1 .. 30 |
| p_same_line | 0.121 [0, 0.236] | 0 .. 0.5 |

### grille: taze medyan mesafe 3.52, en iyi 1.72

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| char_double_rate | +7.7 | 0.015 | 0.057 |
| n_symbols | -3.9 | 69.529 | 32.500 |
| wlen_autocorr1 | -3.1 | 0.179 | -0.004 |
| vocab_ed1_density | +2.6 | 0.854 | 0.915 |
| hapax_ratio | -2.4 | 0.741 | 0.670 |
| jsd_line_final | -2.1 | 0.133 | 0.041 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.4 [6.68, 10.5] | 5 .. 13 |
| l_width_jitter | 0.214 [0.0555, 0.299] | 0 .. 0.35 |
| l_para_lines | 0 [0, 9.3] | 3 .. 15 |
| l_allo_per_glyph | 1.02 [0, 2.1] | 0.2 .. 3 |
| l_allo_rate | 0.0676 [0, 0.107] | 0.01 .. 0.15 |
| l_final_forms_share | 0.538 [0.308, 0.694] | 0.1 .. 1 |
| l_final_forms_k | 2.5 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.286 [0, 0.646] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.331] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.485] | 0.3 .. 1 |
| p_alphabet | 22 [18, 25] | 15 .. 25 |
| p_rows | 732 [476, 1.48e+03] | 60 .. 3000 |
| p_slot_overlap | 0.852 [0.64, 0.996] | 0 .. 1 |
| p_n_edge | 17 [12, 26] | 5 .. 40 |
| p_n_mid | 48.5 [29, 93.2] | 10 .. 120 |
| p_empty | 0.369 [0.288, 0.476] | 0 .. 0.6 |
| p_len_edge | 2 [2, 2.25] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_n_grilles | 6 [4, 7] | 3 .. 8 |


## zl_basic: sınıf sınıf

### grille: taze medyan mesafe 3.04, en iyi 1.47

Voynich'ten 2 birimden fazla sapan feature sayısı: 6

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| h2_over_h1 | +2.7 | 0.521 | 0.612 |
| wlen_autocorr1 | -2.7 | 0.123 | -0.005 |
| h2 | +2.7 | 2.013 | 2.388 |
| hapax_ratio | -2.5 | 0.715 | 0.636 |
| jsd_line_final | -2.4 | 0.110 | 0.017 |
| rep_adjacent_ed1 | -2.4 | 0.034 | 0.017 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.54 [6.15, 10.6] | 5 .. 13 |
| l_width_jitter | 0.192 [0.0496, 0.285] | 0 .. 0.35 |
| l_para_lines | 0 [0, 7.47] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.749] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0132] | 0.01 .. 0.15 |
| l_final_forms_share | 0.577 [0.397, 0.769] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.19 [0, 0.505] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.228] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.618] | 0.3 .. 1 |
| p_alphabet | 20 [18, 22] | 15 .. 25 |
| p_rows | 1.24e+03 [720, 1.91e+03] | 60 .. 3000 |
| p_slot_overlap | 0.368 [0.201, 0.539] | 0 .. 1 |
| p_n_edge | 25 [14, 35] | 5 .. 40 |
| p_n_mid | 34.5 [18, 64] | 10 .. 120 |
| p_empty | 0.354 [0.283, 0.411] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 4 [3, 5] | 2 .. 5 |
| p_n_grilles | 6 [5, 7] | 3 .. 8 |

### slotcite: taze medyan mesafe 3.12, en iyi 1.75

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| h2_over_h1 | +3.1 | 0.521 | 0.625 |
| h2 | +2.9 | 2.013 | 2.411 |
| hapax_ratio | -2.7 | 0.715 | 0.627 |
| char_double_rate | +2.0 | 0.066 | 0.097 |
| wlen_autocorr1 | -2.0 | 0.123 | 0.027 |
| n_symbols | -1.9 | 40.438 | 23.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.29 [7.13, 11.9] | 5 .. 13 |
| l_width_jitter | 0.178 [0.0923, 0.249] | 0 .. 0.35 |
| l_para_lines | 0 [0, 11.7] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.66] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0521] | 0.01 .. 0.15 |
| l_final_forms_share | 0.611 [0.395, 0.811] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.174] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.508 [0.232, 0.683] | 0.1 .. 0.9 |
| l_line_final_p | 0.117 [0, 0.296] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.075] | 0.3 .. 1 |
| p_alphabet | 18 [16, 20.2] | 15 .. 25 |
| p_slot_overlap | 0.302 [0.119, 0.578] | 0 .. 1 |
| p_n_edge | 26 [19, 37.2] | 5 .. 40 |
| p_n_mid | 39.5 [13.5, 92] | 10 .. 120 |
| p_empty | 0.344 [0.28, 0.405] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 4 [4, 5] | 2 .. 5 |
| p_copy | 0.564 [0.5, 0.668] | 0.5 .. 0.97 |
| p_exact | 0.302 [0.167, 0.426] | 0.1 .. 0.7 |
| p_reach | 10 [4, 23] | 1 .. 30 |
| p_same_line | 0.0602 [0.00414, 0.11] | 0 .. 0.5 |
| p_mut_prefix | 0.486 [0.262, 0.732] | 0 .. 1 |
| p_mut_mid | 0.309 [0.0998, 0.627] | 0 .. 1 |
| p_mut_suffix | 0.215 [0.0846, 0.377] | 0 .. 1 |

### verbose: taze medyan mesafe 3.13, en iyi 2.02

Voynich'ten 2 birimden fazla sapan feature sayısı: 14

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +4.6 | 1.768 | 2.044 |
| first_entropy_ratio | +4.5 | 0.817 | 0.894 |
| wlen_skew | +4.2 | 0.025 | 0.458 |
| wlen_autocorr1 | -3.5 | 0.123 | -0.044 |
| jsd_first | -3.4 | 0.385 | 0.252 |
| rep_adjacent_ed1 | -3.0 | 0.034 | 0.013 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.1 [8, 11.5] | 5 .. 13 |
| l_width_jitter | 0.076 [0.0175, 0.142] | 0 .. 0.35 |
| l_para_lines | 0 [0, 6.1] | 3 .. 15 |
| l_allo_per_glyph | 1.79 [1.21, 2.36] | 0.2 .. 3 |
| l_allo_rate | 0.0496 [0.0242, 0.0655] | 0.01 .. 0.15 |
| l_final_forms_share | 0.493 [0.218, 0.653] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.345 [0, 0.487] | 0.1 .. 0.9 |
| l_line_final_p | 0.16 [0, 0.323] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.688] | 0.3 .. 1 |
| p_alphabet | 14 [12, 15] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.367 [0.324, 0.439] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Italian 80, Croatian 13, Czech 3, Portuguese 2, Finnish 1

### selfcite: taze medyan mesafe 3.36, en iyi 2.54

Voynich'ten 2 birimden fazla sapan feature sayısı: 12

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| vocab_ed1_density | +5.0 | 0.823 | 0.931 |
| h2_over_h1 | +4.9 | 0.521 | 0.685 |
| h2 | +4.7 | 2.013 | 2.661 |
| char_double_rate | +3.9 | 0.066 | 0.124 |
| type_len_mean | -3.5 | 5.640 | 5.001 |
| hapax_ratio | -3.4 | 0.715 | 0.607 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.92 [6.15, 10.8] | 5 .. 13 |
| l_width_jitter | 0.134 [0.0665, 0.289] | 0 .. 0.35 |
| l_para_lines | 5.23 [0, 11.1] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 1.68] | 0.2 .. 3 |
| l_allo_rate | 0.0158 [0, 0.049] | 0.01 .. 0.15 |
| l_final_forms_share | 0.686 [0.531, 0.83] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0.308] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 3] | 0 .. 4 |
| l_line_initial_p | 0.263 [0, 0.702] | 0.1 .. 0.9 |
| l_line_final_p | 0.222 [0, 0.316] | 0.1 .. 0.9 |
| l_para_initial_p | 0.695 [0, 0.949] | 0.3 .. 1 |
| p_alphabet | 17 [15, 19] | 15 .. 25 |
| p_glyph_classes | 6 [5, 7] | 4 .. 7 |
| p_copy | 0.919 [0.878, 0.947] | 0.85 .. 0.97 |
| p_exact | 0.353 [0.243, 0.486] | 0.2 .. 0.8 |
| p_reach | 22 [14, 27] | 1 .. 30 |
| p_same_line | 0.013 [0, 0.0364] | 0 .. 0.3 |
| p_slot_overlap | 0.184 [0.0343, 0.31] | 0 .. 1 |
| p_affix | 0.859 [0.81, 0.894] | 0.3 .. 0.9 |
| p_mut_substitute | 0.323 [0.202, 0.557] | 0 .. 1 |
| p_mut_prefix | 0.566 [0.404, 0.769] | 0 .. 1 |
| p_mut_delete | 0.0812 [0.0161, 0.164] | 0 .. 1 |
| p_mut_double | 0.111 [0.0502, 0.194] | 0 .. 1 |

### slotgram: taze medyan mesafe 3.39, en iyi 2.13

Voynich'ten 2 birimden fazla sapan feature sayısı: 10

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| zipf_slope | +3.6 | -0.785 | -0.540 |
| jsd_line_final | -2.5 | 0.110 | 0.014 |
| h2_over_h1 | +2.4 | 0.521 | 0.603 |
| vocab_ed1_density | +2.4 | 0.823 | 0.875 |
| top10_coverage | -2.3 | 0.175 | 0.087 |
| n_symbols | -2.2 | 40.438 | 20.000 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.76 [6.87, 10.8] | 5 .. 13 |
| l_width_jitter | 0.217 [0.134, 0.311] | 0 .. 0.35 |
| l_para_lines | 7.7 [0, 10.7] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.74 [0.531, 0.896] | 0.1 .. 1 |
| l_final_forms_k | 3 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.474 [0, 0.643] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.315] | 0.1 .. 0.9 |
| l_para_initial_p | 0.524 [0, 0.721] | 0.3 .. 1 |
| p_alphabet | 19 [17.8, 21] | 15 .. 25 |
| p_n_slots | 5 [5, 6] | 3 .. 8 |
| p_slot_overlap | 0.661 [0.39, 0.782] | 0 .. 1 |
| p_n_inv | 5 [4, 8] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.426 [0.333, 0.48] | 0.1 .. 0.8 |
| p_copy | 0.3 [0, 0.447] | 0.3 .. 0.95 |
| p_exact | 0.147 [0.0654, 0.29] | 0 .. 0.5 |
| p_reach | 4 [2, 9.25] | 1 .. 30 |
| p_same_line | 0.131 [0.0464, 0.239] | 0 .. 0.5 |

### plain: taze medyan mesafe 3.66, en iyi 3.13

Voynich'ten 2 birimden fazla sapan feature sayısı: 21

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -8.9 | 0.636 | 0.054 |
| first_entropy_ratio | +6.2 | 0.817 | 0.922 |
| h2_over_h1 | +5.6 | 0.521 | 0.711 |
| jsd_last | +5.6 | 0.712 | 0.967 |
| h2 | +5.6 | 2.013 | 2.790 |
| vocab_ed1_density | -5.3 | 0.823 | 0.709 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10 [7.32, 11.6] | 5 .. 13 |
| l_width_jitter | 0.158 [0.0622, 0.27] | 0 .. 0.35 |
| l_para_lines | 7.81 [0, 12.2] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.948 [0.891, 0.994] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.302] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.813] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Arabic 94, Hebrew 6

### abjad: taze medyan mesafe 5.04, en iyi 4.03

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac_le2 | +17.8 | 0.097 | 0.335 |
| wlen_frac1 | +7.9 | 0.033 | 0.114 |
| wlen_mean | -7.0 | 4.961 | 3.381 |
| type_len_mean | -6.7 | 5.640 | 4.429 |
| wlen_skew | +6.4 | 0.025 | 0.679 |
| h2_over_h1 | +5.4 | 0.521 | 0.704 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.91 [6.68, 11] | 5 .. 13 |
| l_width_jitter | 0.135 [0.0635, 0.256] | 0 .. 0.35 |
| l_para_lines | 6.19 [0, 9.24] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0414] | 0.01 .. 0.15 |
| l_final_forms_share | 0.666 [0.548, 0.845] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.49 [0.387, 0.54] | 0.1 .. 1 |
| l_initial_forms_k | 2 [2, 3] | 0 .. 4 |
| l_line_initial_p | 0.261 [0, 0.563] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.277] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.618] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100


## zl_glyph: sınıf sınıf

### grille: taze medyan mesafe 2.44, en iyi 1.46

Voynich'ten 2 birimden fazla sapan feature sayısı: 5

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_autocorr1 | -2.5 | 0.102 | 0.002 |
| n_symbols | -2.4 | 44.750 | 22.000 |
| jsd_line_initial | -2.1 | 0.266 | 0.074 |
| h2_over_h1 | +2.1 | 0.554 | 0.639 |
| vocab_ed1_density | +2.0 | 0.852 | 0.885 |
| rep_adjacent_ed1 | -2.0 | 0.041 | 0.022 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.07 [5.51, 8.52] | 5 .. 13 |
| l_width_jitter | 0.13 [0.041, 0.235] | 0 .. 0.35 |
| l_para_lines | 4.57 [0, 8.44] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0.494] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0731] | 0.01 .. 0.15 |
| l_final_forms_share | 0.731 [0.633, 0.821] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0 [0, 0.496] | 0.1 .. 0.9 |
| l_line_final_p | 0.259 [0, 0.34] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.819] | 0.3 .. 1 |
| p_alphabet | 18 [16.8, 20] | 15 .. 25 |
| p_rows | 1.12e+03 [689, 2.25e+03] | 60 .. 3000 |
| p_slot_overlap | 0.594 [0.361, 0.781] | 0 .. 1 |
| p_n_edge | 24.5 [17, 33] | 5 .. 40 |
| p_n_mid | 58 [35, 90.2] | 10 .. 120 |
| p_empty | 0.347 [0.302, 0.468] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [2, 4] | 2 .. 5 |
| p_n_grilles | 6 [5, 7] | 3 .. 8 |

### selfcite: taze medyan mesafe 2.58, en iyi 1.75

Voynich'ten 2 birimden fazla sapan feature sayısı: 7

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| h2_over_h1 | +3.8 | 0.554 | 0.709 |
| h2 | +3.5 | 2.127 | 2.738 |
| vocab_ed1_density | +3.4 | 0.852 | 0.907 |
| char_double_rate | +2.9 | 0.076 | 0.121 |
| rep_adjacent_exact | +2.8 | 0.008 | 0.016 |
| hapax_ratio | -2.8 | 0.715 | 0.625 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.3 [7.85, 11.7] | 5 .. 13 |
| l_width_jitter | 0.103 [0.0545, 0.186] | 0 .. 0.35 |
| l_para_lines | 0 [0, 8.73] | 3 .. 15 |
| l_allo_per_glyph | 1.4 [0, 2.08] | 0.2 .. 3 |
| l_allo_rate | 0.0386 [0, 0.0664] | 0.01 .. 0.15 |
| l_final_forms_share | 0.524 [0.388, 0.678] | 0.1 .. 1 |
| l_final_forms_k | 2.5 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 2] | 0 .. 4 |
| l_line_initial_p | 0.177 [0, 0.403] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.279] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.568] | 0.3 .. 1 |
| p_alphabet | 17 [15.8, 19] | 15 .. 25 |
| p_glyph_classes | 5 [4, 6] | 4 .. 7 |
| p_copy | 0.88 [0.859, 0.909] | 0.85 .. 0.97 |
| p_exact | 0.519 [0.413, 0.595] | 0.2 .. 0.8 |
| p_reach | 24.5 [19, 28] | 1 .. 30 |
| p_same_line | 0.0224 [0.00335, 0.0553] | 0 .. 0.3 |
| p_slot_overlap | 0.192 [0.0347, 0.368] | 0 .. 1 |
| p_affix | 0.814 [0.681, 0.895] | 0.3 .. 0.9 |
| p_mut_substitute | 0.171 [0.0141, 0.301] | 0 .. 1 |
| p_mut_prefix | 0.729 [0.533, 0.908] | 0 .. 1 |
| p_mut_delete | 0.101 [0.038, 0.205] | 0 .. 1 |
| p_mut_double | 0.109 [0.0424, 0.159] | 0 .. 1 |

### slotcite: taze medyan mesafe 2.73, en iyi 1.54

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| jsd_line_final | -2.4 | 0.110 | 0.019 |
| h2 | +2.1 | 2.127 | 2.485 |
| rep_adjacent_exact | +2.0 | 0.008 | 0.014 |
| h2_over_h1 | +2.0 | 0.554 | 0.636 |
| vocab_ed1_density | +1.8 | 0.852 | 0.880 |
| hapax_ratio | -1.7 | 0.715 | 0.660 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 9.64 [7.89, 11.7] | 5 .. 13 |
| l_width_jitter | 0.172 [0.0915, 0.232] | 0 .. 0.35 |
| l_para_lines | 0 [0, 7.43] | 3 .. 15 |
| l_allo_per_glyph | 1.32 [0, 2.17] | 0.2 .. 3 |
| l_allo_rate | 0.0715 [0.0075, 0.105] | 0.01 .. 0.15 |
| l_final_forms_share | 0.492 [0.29, 0.719] | 0.1 .. 1 |
| l_final_forms_k | 3 [2, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.286 [0, 0.631] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.15] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.304] | 0.3 .. 1 |
| p_alphabet | 19 [15, 23] | 15 .. 25 |
| p_slot_overlap | 0.267 [0.0475, 0.558] | 0 .. 1 |
| p_n_edge | 27.5 [18, 39] | 5 .. 40 |
| p_n_mid | 45 [16, 82] | 10 .. 120 |
| p_empty | 0.351 [0.3, 0.401] | 0 .. 0.6 |
| p_len_edge | 3 [2, 3] | 1 .. 3 |
| p_len_mid | 3 [3, 5] | 2 .. 5 |
| p_copy | 0.645 [0.556, 0.75] | 0.5 .. 0.97 |
| p_exact | 0.198 [0.13, 0.286] | 0.1 .. 0.7 |
| p_reach | 9 [4, 16] | 1 .. 30 |
| p_same_line | 0.11 [0.037, 0.192] | 0 .. 0.5 |
| p_mut_prefix | 0.365 [0.212, 0.503] | 0 .. 1 |
| p_mut_mid | 0.326 [0.192, 0.482] | 0 .. 1 |
| p_mut_suffix | 0.296 [0.143, 0.432] | 0 .. 1 |

### verbose: taze medyan mesafe 2.81, en iyi 1.83

Voynich'ten 2 birimden fazla sapan feature sayısı: 11

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_std | +6.5 | 1.615 | 1.974 |
| wlen_skew | +3.7 | 0.154 | 0.530 |
| wlen_autocorr1 | -3.1 | 0.102 | -0.023 |
| hapax_ratio | -2.5 | 0.715 | 0.635 |
| rep_adjacent_exact | -2.4 | 0.008 | 0.003 |
| rep_adjacent_ed1 | -2.3 | 0.041 | 0.018 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.8 [5.65, 9.32] | 5 .. 13 |
| l_width_jitter | 0.21 [0.0865, 0.321] | 0 .. 0.35 |
| l_para_lines | 3 [0, 6.56] | 3 .. 15 |
| l_allo_per_glyph | 1.93 [1.24, 2.45] | 0.2 .. 3 |
| l_allo_rate | 0.0499 [0.0322, 0.0685] | 0.01 .. 0.15 |
| l_final_forms_share | 0.546 [0.373, 0.766] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.0709 [0, 0.578] | 0.1 .. 0.9 |
| l_line_final_p | 0.269 [0.143, 0.36] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.466] | 0.3 .. 1 |
| p_alphabet | 13 [12, 14] | 12 .. 22 |
| p_drop_vowels | 0 [0, 0] | 0 .. 1 |
| p_short | 0.493 [0.423, 0.586] | 0.3 .. 1 |
| p_by_syllable | 1 [1, 1] | 0 .. 1 |
| p_split | 0 [0, 0] | 0.05 .. 0.7 |

Kaynak dil (son nüfusta en sık): Romanian 49, Italian 41, Croatian 5, Turkish 2, Czech 2

### plain: taze medyan mesafe 2.90, en iyi 2.47

Voynich'ten 2 birimden fazla sapan feature sayısı: 16

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| last_entropy_ratio | -6.4 | 0.636 | 0.239 |
| wlen_std | -5.2 | 1.615 | 1.328 |
| h2_over_h1 | +4.3 | 0.554 | 0.729 |
| char_double_rate | -4.2 | 0.076 | 0.009 |
| h2 | +4.2 | 2.127 | 2.857 |
| vocab_ed1_density | -4.0 | 0.852 | 0.788 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 7.42 [5.72, 9.42] | 5 .. 13 |
| l_width_jitter | 0.2 [0.0782, 0.292] | 0 .. 0.35 |
| l_para_lines | 6.36 [0, 10.1] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0] | 0.01 .. 0.15 |
| l_final_forms_share | 0.844 [0.784, 0.919] | 0.1 .. 1 |
| l_final_forms_k | 1 [1, 1] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 0 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.25 [0, 0.535] | 0.1 .. 0.9 |
| l_line_final_p | 0.16 [0, 0.347] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.489] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Hebrew 100

### slotgram: taze medyan mesafe 3.00, en iyi 1.48

Voynich'ten 2 birimden fazla sapan feature sayısı: 4

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| vocab_ed1_density | +2.5 | 0.852 | 0.893 |
| wlen_autocorr1 | -2.4 | 0.102 | 0.005 |
| jsd_line_final | -2.4 | 0.110 | 0.019 |
| n_symbols | -2.3 | 44.750 | 23.000 |
| first_entropy_ratio | -1.9 | 0.875 | 0.826 |
| rep_within3 | -1.8 | 0.027 | 0.013 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 8.42 [6.37, 11.5] | 5 .. 13 |
| l_width_jitter | 0.225 [0.115, 0.33] | 0 .. 0.35 |
| l_para_lines | 6.36 [0, 10.5] | 3 .. 15 |
| l_allo_per_glyph | 0.125 [0, 1.99] | 0.2 .. 3 |
| l_allo_rate | 0.014 [0, 0.108] | 0.01 .. 0.15 |
| l_final_forms_share | 0.537 [0.416, 0.674] | 0.1 .. 1 |
| l_final_forms_k | 2 [1, 4] | 0 .. 4 |
| l_initial_forms_share | 0 [0, 0] | 0.1 .. 1 |
| l_initial_forms_k | 1 [0, 1] | 0 .. 4 |
| l_line_initial_p | 0.326 [0, 0.526] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0.342] | 0.1 .. 0.9 |
| l_para_initial_p | 0.422 [0, 0.765] | 0.3 .. 1 |
| p_alphabet | 19 [16, 23] | 15 .. 25 |
| p_n_slots | 5 [4, 5] | 3 .. 8 |
| p_slot_overlap | 0.414 [0.139, 0.686] | 0 .. 1 |
| p_n_inv | 7 [4, 9.25] | 2 .. 30 |
| p_len_max | 2 [2, 2] | 1 .. 2 |
| p_empty | 0.417 [0.329, 0.498] | 0.1 .. 0.8 |
| p_copy | 0 [0, 0] | 0.3 .. 0.95 |
| p_exact | 0.239 [0.131, 0.341] | 0 .. 0.5 |
| p_reach | 4 [2, 12] | 1 .. 30 |
| p_same_line | 0.256 [0.124, 0.385] | 0 .. 0.5 |

### abjad: taze medyan mesafe 3.23, en iyi 2.56

Voynich'ten 2 birimden fazla sapan feature sayısı: 15

| tutmayan feature | sapma (Voynich birimi) | Voynich | taze örnekler |
|---|---|---|---|
| wlen_frac1 | +7.6 | 0.033 | 0.114 |
| wlen_frac_le2 | +6.5 | 0.119 | 0.336 |
| wlen_skew | +5.0 | 0.154 | 0.663 |
| vocab_ed1_density | -4.2 | 0.852 | 0.785 |
| h2_over_h1 | +4.0 | 0.554 | 0.718 |
| h2 | +3.8 | 2.127 | 2.782 |

| ayar | bulunan medyan [çeyrekler] | önsel aralığı |
|---|---|---|
| l_words_per_line | 10.2 [7.21, 11.9] | 5 .. 13 |
| l_width_jitter | 0.14 [0.0558, 0.246] | 0 .. 0.35 |
| l_para_lines | 7.75 [0, 11.2] | 3 .. 15 |
| l_allo_per_glyph | 0 [0, 0] | 0.2 .. 3 |
| l_allo_rate | 0 [0, 0.0761] | 0.01 .. 0.15 |
| l_final_forms_share | 0.699 [0.645, 0.758] | 0.1 .. 1 |
| l_final_forms_k | 2 [2, 3] | 0 .. 4 |
| l_initial_forms_share | 0.321 [0.155, 0.428] | 0.1 .. 1 |
| l_initial_forms_k | 2 [1, 3] | 0 .. 4 |
| l_line_initial_p | 0.337 [0, 0.562] | 0.1 .. 0.9 |
| l_line_final_p | 0 [0, 0] | 0.1 .. 0.9 |
| l_para_initial_p | 0 [0, 0.496] | 0.3 .. 1 |

Kaynak dil (son nüfusta en sık): Turkish 100
