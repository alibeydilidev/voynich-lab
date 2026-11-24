# Sınama: EVA'laştırma sınıflandırıcının kararını değiştiriyor mu

Her süreçten 300 anlamsız metin örneği üretildi. Her örnek iki kez sınıflandırıldı: özgün hâliyle ve altı glifi EVA'daki gibi çok harfli diziye açılmış hâliyle. Tablo oy sayısını verir.

| süreç | yazım | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|---|
| grille | özgün | 1 | 2 | 2 | 278 | 0 | 0 | 5 | 11 | 1 |
| grille | EVA'laştırılmış | 0 | 8 | 0 | 181 | 1 | 0 | 1 | 16 | 93 |
| selfcite | özgün | 0 | 0 | 0 | 0 | 0 | 281 | 15 | 4 | 0 |
| selfcite | EVA'laştırılmış | 0 | 0 | 0 | 0 | 0 | 88 | 82 | 83 | 47 |
| slotcite | özgün | 0 | 0 | 0 | 14 | 0 | 8 | 266 | 11 | 1 |
| slotcite | EVA'laştırılmış | 0 | 5 | 0 | 5 | 0 | 0 | 234 | 23 | 33 |
| slotgram | özgün | 5 | 12 | 3 | 13 | 0 | 10 | 23 | 234 | 0 |
| slotgram | EVA'laştırılmış | 0 | 22 | 0 | 9 | 0 | 1 | 32 | 178 | 58 |
| automaton | özgün | 0 | 299 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| automaton | EVA'laştırılmış | 0 | 264 | 0 | 6 | 0 | 0 | 0 | 3 | 27 |

# Sınama: tek bir tablo Voynich kadar değişken metin üretiyor mu

Her süreçten 12 el yazması üretildi; her biri tek tablo ve tek ayar kümesiyle 8 pencere. Birim Voynich pencereleri arası değişkenlik. "İç": pencerelerin kendi el yazmasının ortalamasına uzaklığı. "Arası": farklı el yazmalarının ortalamaları arasındaki uzaklık.

| görünüm | Voynich iç | grille iç | grille arası | selfcite iç | selfcite arası | slotcite iç | slotcite arası | slotgram iç | slotgram arası | automaton iç | automaton arası |
|---|---|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.92 | 0.33 | 6.21 | 1.69 | 6.88 | 0.82 | 7.58 | 0.75 | 11.53 | 0.50 | 8.88 |
| eva_glyph | 0.93 | 0.31 | 5.49 | 1.37 | 5.91 | 0.72 | 6.69 | 0.70 | 9.98 | 0.49 | 8.08 |
| v101 | 0.94 | 0.28 | 4.58 | 1.62 | 6.48 | 0.85 | 6.82 | 0.82 | 11.70 | 0.50 | 8.87 |
| zl_basic | 0.95 | 0.27 | 4.58 | 1.56 | 5.84 | 0.78 | 6.64 | 0.75 | 10.76 | 0.48 | 8.31 |
| zl_glyph | 0.95 | 0.26 | 3.78 | 1.26 | 4.88 | 0.68 | 5.65 | 0.69 | 9.39 | 0.47 | 7.56 |

# Sınama: kelimeler bir sözlükten mi geliyor

Her metnin ilk 16000 kelimesinden kelime içi glif zinciri öğrenildi (k = 1 ve 2) ve aynı sayıda kelime bağımsız çekildi (vekil). Tür oranı: vekildeki farklı kelime sayısı / gerçek metindeki. Yeni kelime oranı: vekilde, ilk yarıda görülmemiş kelimelerin payı / gerçek ikinci yarıda aynı pay. İkisi de 1'e yakınsa metin, harf dizilişi kurallarının izin verdiği her kelimeyi kullanıyor demektir (sözlük kısıtı görünmüyor); 1'in belirgin üstündeyse kelimeler bu kuralların izin verdiğinden çok daha dar bir kümeden geliyor demektir.

| metin | n | ort. kelime uzunluğu | tür oranı k=1 | tür oranı k=2 | yeni kelime oranı k=1 | yeni kelime oranı k=2 |
|---|---|---|---|---|---|---|
| Voynich eva_basic | 1 | 4.9 | 1.39 | 1.06 | 1.56 | 0.93 |
| Voynich eva_glyph | 1 | 4.3 | 1.36 | 1.02 | 1.41 | 0.84 |
| Voynich v101 | 1 | 3.8 | 1.14 | 0.96 | 1.35 | 0.92 |
| Voynich zl_basic | 1 | 4.8 | 1.39 | 1.06 | 1.62 | 0.95 |
| Voynich zl_glyph | 1 | 4.2 | 1.31 | 1.00 | 1.40 | 0.85 |
| doğal dil, düz (medyan [en az, en çok]) | 22 | 4.4 | 2.79 [1.86, 4.91] | 2.26 [1.55, 3.24] | 3.92 [2.35, 7.92] | 2.88 [1.89, 5.18] |
| doğal dil, seslisiz (medyan [en az, en çok]) | 19 | 2.6 | 2.16 [1.73, 3.07] | 1.53 [1.37, 1.80] | 2.40 [1.30, 4.64] | 1.58 [0.96, 2.66] |
| dönem metni (15. yy), düz (medyan [en az, en çok]) | 5 | 4.7 | 2.09 [1.89, 3.03] | 1.78 [1.76, 2.35] | 3.76 [3.09, 6.04] | 3.19 [2.93, 4.50] |
| dönem metni (15. yy), seslisiz (medyan [en az, en çok]) | 5 | 2.5 | 1.66 [1.52, 2.41] | 1.41 [1.25, 1.72] | 2.54 [2.15, 4.43] | 1.96 [1.82, 2.93] |
| verbose (medyan [en az, en çok]) | 30 | 4.6 | 1.70 [1.04, 6.60] | 1.31 [0.98, 4.80] | 3.14 [1.63, 17.91] | 1.73 [0.90, 5.63] |
| codebook (medyan [en az, en çok]) | 30 | 4.0 | 1.34 [1.06, 5.56] | 0.98 [0.78, 1.68] | 1.99 [0.81, 6.89] | 0.76 [0.04, 2.97] |
| grille (medyan [en az, en çok]) | 30 | 4.0 | 2.62 [1.29, 17.82] | 1.36 [1.02, 9.53] | 13.44 [2.43, 392250000.00] | 4.09 [1.30, 111812500.00] |
| selfcite (medyan [en az, en çok]) | 30 | 4.3 | 1.47 [1.14, 3.30] | 1.38 [1.14, 2.87] | 0.82 [0.73, 0.96] | 0.80 [0.58, 0.92] |
| slotcite (medyan [en az, en çok]) | 30 | 4.1 | 2.48 [1.37, 8.88] | 1.36 [0.94, 2.74] | 6.61 [1.91, 62687500.00] | 2.04 [0.00, 23.75] |
| slotgram (medyan [en az, en çok]) | 30 | 4.2 | 1.12 [0.73, 2.83] | 1.00 [0.87, 1.15] | 1.43 [0.78, 137000000.00] | 0.89 [0.00, 1.95] |
| automaton (medyan [en az, en çok]) | 30 | 4.2 | 1.01 [0.93, 1.48] | 0.96 [0.91, 1.01] | 1.06 [0.84, 8.05] | 0.94 [0.38, 1.12] |

## Voynich bölüm bölüm (yarı boyu 5000 kelime)

Bölümler kısa olduğu için daha küçük yarı boyuyla ölçüldü; doğal dil tabanı aynı boyda yeniden hesaplandı. Yeterince uzun olmayan bölümler ölçülemedi.

| metin | ort. kelime uzunluğu | tür oranı k=1 | tür oranı k=2 | yeni kelime oranı k=1 | yeni kelime oranı k=2 |
|---|---|---|---|---|---|
| Voynich Currier A (zl_glyph) | 3.9 | 1.11 | 0.96 | 0.95 | 0.63 |
| Voynich Currier B (zl_glyph) | 4.4 | 1.14 | 1.00 | 1.70 | 1.19 |
| Voynich çizim türü A (zl_glyph) | metin kısa | | | | |
| Voynich çizim türü B (zl_glyph) | metin kısa | | | | |
| Voynich çizim türü C (zl_glyph) | metin kısa | | | | |
| Voynich çizim türü H (zl_glyph) | 4.0 | 1.10 | 0.94 | 1.08 | 0.71 |
| Voynich çizim türü P (zl_glyph) | metin kısa | | | | |
| Voynich çizim türü S (zl_glyph) | 4.7 | 1.10 | 0.97 | 1.49 | 1.06 |
| Voynich çizim türü T (zl_glyph) | metin kısa | | | | |
| doğal dil, düz, 22 dil (medyan [en az, en çok]) | 4.4 | 2.20 [1.54, 3.60] | 1.83 [1.29, 2.62] | 3.21 [2.02, 4.86] | 2.36 [1.40, 3.59] |

# Sınama: kelimelerin sırası bilgi taşıyor mu

Her metnin ilk 16000 kelimesinden kelime ikilisi modeli öğrenildi; görülmemiş sonraki 16000 kelimede, tek kelime sıklığı modeline göre kelime başına kaç bit kazandırdığı ölçüldü. Aynı ölçüm her satırın kelimeleri kendi içinde karıştırılarak tekrarlandı. "Sıra" sütunu ikisinin farkıdır: sıranın, birlikte geçmenin ötesinde taşıdığı bilgi (bit/kelime). Bire bir kelime kodlaması kaynak dille aynı değeri verir.

| metin | n | sıra (bit/kelime) | gerçek kazanç | karıştırılmış kazanç |
|---|---|---|---|---|
| Voynich eva_basic (aile düzeyinde: +0.032) | 1 | -0.007 | -0.012 | -0.005 |
| Voynich eva_glyph (aile düzeyinde: +0.017) | 1 | -0.008 | -0.012 | -0.004 |
| Voynich v101 (aile düzeyinde: +0.025) | 1 | +0.020 | +0.016 | -0.003 |
| Voynich zl_basic (aile düzeyinde: +0.024) | 1 | +0.010 | +0.002 | -0.008 |
| Voynich zl_glyph (aile düzeyinde: +0.019) | 1 | +0.005 | +0.002 | -0.003 |
| doğal dil, düz (medyan [en az, en çok]) | 22 | +0.522 [+0.165, +0.963] | +0.525 [+0.164, +0.983] | +0.003 [-0.003, +0.035] |
| dönem ve tür metinleri (medyan [en az, en çok]) | 5 | +0.253 [+0.180, +0.832] | +0.253 [+0.180, +0.840] | +0.000 [-0.000, +0.008] |
| verbose (medyan [en az, en çok]) | 20 | +0.204 [+0.029, +1.631] | +0.204 [+0.029, +1.641] | +0.000 [-0.004, +0.012] |
| codebook (medyan [en az, en çok]) | 20 | +0.251 [+0.014, +0.950] | +0.255 [+0.006, +0.957] | +0.000 [-0.008, +0.014] |
| grille (medyan [en az, en çok]) | 20 | +1.330 [+0.000, +3.721] | +1.517 [+0.000, +5.362] | +0.062 [-0.000, +1.641] |
| selfcite (medyan [en az, en çok]) | 20 | +0.003 [-0.003, +0.210] | +0.003 [-0.003, +0.507] | +0.000 [-0.002, +0.297] |
| slotcite (medyan [en az, en çok]) | 20 | +0.006 [-0.001, +0.071] | +0.008 [-0.001, +0.149] | +0.001 [+0.000, +0.090] |
| slotgram (medyan [en az, en çok]) | 20 | +0.000 [+0.000, +0.047] | +0.000 [+0.000, +0.071] | +0.000 [+0.000, +0.024] |
| automaton (medyan [en az, en çok]) | 20 | +0.000 [-0.001, +0.002] | +0.000 [-0.001, +0.002] | +0.000 [+0.000, +0.000] |
| italian_alberti_1440 | 1 | +0.294 | +0.294 | +0.000 |
| italian_cennini_tarif_1400 | 1 | +0.832 | +0.840 | +0.008 |
| latin_kempis_1420 | 1 | +0.180 | +0.180 | +0.000 |
| latin_pliny_bitki | 1 | +0.221 | +0.221 | +0.000 |
| spanish_celestina_1499 | 1 | +0.253 | +0.253 | -0.000 |

## Kısa metinler ve Voynich bölümleri (yarı boyu 3500 kelime)

| metin | sıra (bit/kelime) |
|---|---|
| Voynich eva_basic | +0.000 |
| Voynich eva_glyph | +0.000 |
| Voynich v101 | +0.011 |
| Voynich zl_basic | +0.007 |
| Voynich zl_glyph | +0.007 |
| Voynich Currier A (zl_glyph) | +0.005 |
| Voynich Currier B (zl_glyph) | +0.000 |
| Voynich çizim türü A (zl_glyph) | metin kısa |
| Voynich çizim türü B (zl_glyph) | metin kısa |
| Voynich çizim türü C (zl_glyph) | metin kısa |
| Voynich çizim türü H (zl_glyph) | +0.004 |
| Voynich çizim türü P (zl_glyph) | metin kısa |
| Voynich çizim türü S (zl_glyph) | +0.005 |
| Voynich çizim türü T (zl_glyph) | metin kısa |
| doğal dil, düz, 22 dil (medyan [en az, en çok]) | +0.316 [+0.132, +0.647] |
| italian_alberti_1440 | +0.164 |
| italian_cennini_tarif_1400 | +0.501 |
| latin_apicius_tarif | +0.615 |
| latin_cato_tarim | +0.074 |
| latin_celsus_ilac | +0.806 |
| latin_kempis_1420 | +0.057 |
| latin_macer_bitki | +0.326 |
| latin_pliny_bitki | +0.163 |
| spanish_celestina_1499 | +0.096 |

# Tarama: gerçek dil hangi bozulma altında Voynich gibi görünür

287 düzen: her dil, sesli ve seslisiz; yazım çeşitlemesi (kelimelerin 0.3, 0.6, 0.9'u bir harf farklı yazılır) ve eşsesli yazım (harflerin bir bölümünün 2 ya da 3 ayrı yazılışı vardır). Voynich bantları: tür oranı 0.90 ila 1.12; sıra en çok 0.040; tür/kelime 0.20 ila 0.35; hapax 0.63 ila 0.77; ed1 0.81 ila 0.94.

| ölçüt | uyan düzen |
|---|---|
| sözlük | 150 |
| sıra | 144 |
| büyüme | 66 |
| sözlük ve sıra | 116 |
| sözlük ve büyüme | 42 |
| sıra ve büyüme | 29 |
| üçü birden | 25 |

## Üç ölçütü birden tutturan düzenler

| dil | seslisiz | bozulma | düzey | tür oranı | sıra | aile düzeyinde sıra | tür/kelime | hapax | ed1 | ort. kelime uzunluğu |
|---|---|---|---|---|---|---|---|---|---|---|
| Albanian | evet | yazım çeşitlemesi | 0.6 | 0.98 | +0.005 | +0.002 | 0.30 | 0.74 | 0.92 | 2.5 |
| Croatian | evet | yazım çeşitlemesi | 0.3 | 1.07 | +0.005 | -0.011 | 0.26 | 0.69 | 0.91 | 2.6 |
| Croatian | evet | yazım çeşitlemesi | 0.6 | 0.97 | -0.003 | -0.014 | 0.34 | 0.75 | 0.90 | 2.6 |
| Croatian | evet | eşsesli yazım | 0.6 x2 | 1.07 | +0.022 | -0.009 | 0.28 | 0.68 | 0.84 | 2.5 |
| Croatian | evet | eşsesli yazım | 0.6 x3 | 1.07 | +0.022 | -0.011 | 0.28 | 0.70 | 0.86 | 2.5 |
| Czech | evet | eşsesli yazım | 1.0 x2 | 1.04 | +0.011 | -0.002 | 0.33 | 0.71 | 0.81 | 2.7 |
| Dutch | evet | yazım çeşitlemesi | 0.6 | 1.03 | +0.002 | +0.000 | 0.30 | 0.72 | 0.91 | 2.7 |
| English | evet | yazım çeşitlemesi | 0.9 | 0.96 | +0.000 | -0.002 | 0.30 | 0.72 | 0.92 | 2.5 |
| Finnish | evet | eşsesli yazım | 0.6 x3 | 1.11 | +0.019 | +0.001 | 0.32 | 0.72 | 0.82 | 3.1 |
| French | evet | yazım çeşitlemesi | 0.6 | 0.98 | +0.005 | +0.001 | 0.26 | 0.71 | 0.93 | 2.4 |
| French | evet | yazım çeşitlemesi | 0.9 | 0.93 | +0.000 | +0.000 | 0.31 | 0.74 | 0.90 | 2.4 |
| German | evet | yazım çeşitlemesi | 0.6 | 1.01 | +0.003 | +0.001 | 0.30 | 0.73 | 0.92 | 2.8 |
| Greek | evet | yazım çeşitlemesi | 0.6 | 0.98 | +0.004 | +0.001 | 0.23 | 0.71 | 0.92 | 2.3 |
| Greek | evet | yazım çeşitlemesi | 0.9 | 0.93 | +0.000 | +0.000 | 0.28 | 0.75 | 0.90 | 2.3 |
| Italian | evet | yazım çeşitlemesi | 0.6 | 1.00 | +0.006 | -0.000 | 0.27 | 0.71 | 0.92 | 2.5 |
| Italian | evet | yazım çeşitlemesi | 0.9 | 0.92 | +0.000 | +0.000 | 0.33 | 0.74 | 0.90 | 2.5 |
| Latin | evet | yazım çeşitlemesi | 0.3 | 1.11 | +0.030 | +0.001 | 0.29 | 0.72 | 0.89 | 3.0 |
| Portuguese | evet | yazım çeşitlemesi | 0.6 | 0.97 | +0.002 | +0.000 | 0.25 | 0.72 | 0.92 | 2.3 |
| Romanian | evet | yazım çeşitlemesi | 0.9 | 0.91 | +0.000 | +0.000 | 0.29 | 0.76 | 0.92 | 2.3 |
| Russian | evet | yazım çeşitlemesi | 0.3 | 1.12 | +0.018 | -0.008 | 0.26 | 0.71 | 0.90 | 2.6 |
| Russian | evet | yazım çeşitlemesi | 0.6 | 0.97 | +0.005 | -0.014 | 0.35 | 0.76 | 0.90 | 2.7 |
| Spanish | evet | yazım çeşitlemesi | 0.6 | 0.97 | +0.002 | -0.001 | 0.27 | 0.73 | 0.93 | 2.4 |
| Spanish | evet | yazım çeşitlemesi | 0.9 | 0.92 | +0.000 | +0.000 | 0.32 | 0.75 | 0.90 | 2.5 |
| Swedish | evet | yazım çeşitlemesi | 0.6 | 1.05 | +0.008 | -0.000 | 0.27 | 0.69 | 0.92 | 2.7 |
| Swedish | evet | yazım çeşitlemesi | 0.9 | 0.97 | +0.000 | +0.000 | 0.33 | 0.71 | 0.90 | 2.7 |
