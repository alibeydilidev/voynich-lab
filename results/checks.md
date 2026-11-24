# Sınama: EVA'laştırma sınıflandırıcının kararını değiştiriyor mu

Her süreçten 300 anlamsız metin örneği üretildi. Her örnek iki kez sınıflandırıldı: özgün hâliyle ve altı glifi EVA'daki gibi çok harfli diziye açılmış hâliyle. Tablo oy sayısını verir.

| süreç | yazım | abjad | automaton | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|---|
| grille | özgün | 1 | 2 | 2 | 276 | 0 | 0 | 6 | 12 | 1 |
| grille | EVA'laştırılmış | 0 | 6 | 0 | 176 | 1 | 0 | 2 | 14 | 101 |
| selfcite | özgün | 0 | 0 | 0 | 0 | 0 | 278 | 18 | 4 | 0 |
| selfcite | EVA'laştırılmış | 0 | 0 | 0 | 0 | 0 | 88 | 88 | 77 | 47 |
| slotcite | özgün | 0 | 0 | 0 | 13 | 0 | 7 | 266 | 13 | 1 |
| slotcite | EVA'laştırılmış | 0 | 4 | 0 | 5 | 0 | 0 | 232 | 19 | 40 |
| slotgram | özgün | 3 | 11 | 2 | 14 | 0 | 7 | 26 | 237 | 0 |
| slotgram | EVA'laştırılmış | 0 | 22 | 0 | 10 | 0 | 2 | 29 | 179 | 58 |
| automaton | özgün | 0 | 297 | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| automaton | EVA'laştırılmış | 0 | 256 | 0 | 10 | 0 | 0 | 0 | 4 | 30 |

# Sınama: tek bir tablo Voynich kadar değişken metin üretiyor mu

Her süreçten 12 el yazması üretildi; her biri tek tablo ve tek ayar kümesiyle 8 pencere. Birim Voynich pencereleri arası değişkenlik. "İç": pencerelerin kendi el yazmasının ortalamasına uzaklığı. "Arası": farklı el yazmalarının ortalamaları arasındaki uzaklık.

| görünüm | Voynich iç | grille iç | grille arası | selfcite iç | selfcite arası | slotcite iç | slotcite arası | slotgram iç | slotgram arası | automaton iç | automaton arası |
|---|---|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.92 | 0.33 | 6.21 | 1.69 | 6.88 | 0.82 | 7.59 | 0.75 | 11.53 | 0.43 | 7.49 |
| eva_glyph | 0.93 | 0.31 | 5.49 | 1.37 | 5.91 | 0.72 | 6.68 | 0.70 | 9.98 | 0.41 | 6.73 |
| v101 | 0.94 | 0.28 | 4.58 | 1.62 | 6.48 | 0.85 | 6.82 | 0.82 | 11.70 | 0.45 | 6.86 |
| zl_basic | 0.95 | 0.27 | 4.58 | 1.56 | 5.84 | 0.78 | 6.64 | 0.75 | 10.76 | 0.41 | 6.86 |
| zl_glyph | 0.95 | 0.26 | 3.78 | 1.26 | 4.88 | 0.68 | 5.65 | 0.69 | 9.39 | 0.40 | 6.07 |

# Sınama: kelimeler bir sözlükten mi geliyor

Her metnin ilk 16000 kelimesinden kelime içi glif zinciri öğrenildi (k = 1 ve 2) ve aynı sayıda kelime bağımsız çekildi (vekil). Tür oranı: vekildeki farklı kelime sayısı / gerçek metindeki. Yeni kelime oranı: vekilde, ilk yarıda görülmemiş kelimelerin payı / gerçek ikinci yarıda aynı pay. İkisi de 1'e yakınsa metin, harf dizilişi kurallarının izin verdiği her kelimeyi kullanıyor demektir (sözlük kısıtı görünmüyor); 1'in belirgin üstündeyse kelimeler bu kuralların izin verdiğinden çok daha dar bir kümeden geliyor demektir.

| metin | n | ort. kelime uzunluğu | tür oranı k=1 | tür oranı k=2 | yeni kelime oranı k=1 | yeni kelime oranı k=2 |
|---|---|---|---|---|---|---|
| Voynich eva_basic | 1 | 4.9 | 1.39 | 1.06 | 1.56 | 0.93 |
| Voynich eva_glyph | 1 | 4.3 | 1.36 | 1.02 | 1.41 | 0.84 |
| Voynich v101 | 1 | 3.8 | 1.14 | 0.96 | 1.35 | 0.92 |
| Voynich zl_basic | 1 | 4.8 | 1.39 | 1.06 | 1.62 | 0.95 |
| Voynich zl_glyph | 1 | 4.2 | 1.31 | 1.00 | 1.40 | 0.85 |
| Voynich v101, belirsiz boşluk birleşik | 1 | 4.0 | 1.15 | 0.97 | 1.24 | 0.84 |
| doğal dil, düz (medyan [en az, en çok]) | 22 | 4.4 | 2.80 [1.85, 4.91] | 2.24 [1.56, 3.34] | 3.91 [2.34, 7.97] | 2.92 [1.92, 5.29] |
| doğal dil, seslisiz (medyan [en az, en çok]) | 19 | 2.6 | 2.16 [1.72, 3.02] | 1.56 [1.39, 1.79] | 2.39 [1.32, 4.64] | 1.60 [0.97, 2.59] |
| dönem metni (15. yy), düz (medyan [en az, en çok]) | 5 | 4.7 | 2.12 [1.90, 3.08] | 1.81 [1.74, 2.36] | 3.79 [3.09, 6.07] | 3.22 [2.93, 4.53] |
| dönem metni (15. yy), seslisiz (medyan [en az, en çok]) | 5 | 2.5 | 1.61 [1.53, 2.33] | 1.40 [1.23, 1.70] | 2.59 [2.11, 4.31] | 1.95 [1.80, 2.93] |
| verbose (medyan [en az, en çok]) | 30 | 4.0 | 1.80 [1.02, 4.29] | 1.25 [0.98, 2.66] | 3.47 [1.45, 21.75] | 1.78 [1.06, 5.77] |
| codebook (medyan [en az, en çok]) | 30 | 4.4 | 1.32 [1.02, 2.89] | 0.98 [0.77, 1.83] | 2.26 [0.33, 5.29] | 0.72 [0.02, 2.67] |
| grille (medyan [en az, en çok]) | 30 | 4.6 | 3.10 [1.24, 14.14] | 1.47 [0.93, 3.72] | 19.76 [2.09, 349.19] | 5.59 [0.96, 176.66] |
| selfcite (medyan [en az, en çok]) | 30 | 4.3 | 1.47 [0.95, 2.75] | 1.36 [0.96, 2.56] | 0.83 [0.72, 0.98] | 0.77 [0.50, 0.91] |
| slotcite (medyan [en az, en çok]) | 30 | 3.8 | 2.35 [0.97, 9.03] | 1.13 [0.90, 3.02] | 6.97 [1.49, 374812500.00] | 1.65 [0.35, 46687500.00] |
| slotgram (medyan [en az, en çok]) | 30 | 3.2 | 1.25 [0.78, 7.67] | 0.97 [0.81, 1.35] | 1.43 [0.79, 132.83] | 0.84 [0.00, 1.71] |
| automaton (medyan [en az, en çok]) | 30 | 4.6 | 1.00 [0.89, 1.30] | 0.98 [0.83, 1.04] | 1.03 [0.85, 11.14] | 0.96 [0.08, 1.39] |

## Voynich bölüm bölüm (yarı boyu 5000 kelime)

Bölümler kısa olduğu için daha küçük yarı boyuyla ölçüldü; doğal dil tabanı aynı boyda yeniden hesaplandı. Yeterince uzun olmayan bölümler ölçülemedi.

| metin | ort. kelime uzunluğu | tür oranı k=1 | tür oranı k=2 | yeni kelime oranı k=1 | yeni kelime oranı k=2 |
|---|---|---|---|---|---|
| Voynich Currier A (zl_glyph) | 3.9 | 1.14 | 0.93 | 0.98 | 0.61 |
| Voynich Currier B (zl_glyph) | 4.4 | 1.18 | 0.99 | 1.79 | 1.19 |
| Voynich v101, belirsiz boşluk birleşik | 3.8 | 1.00 | 0.93 | 0.92 | 0.71 |
| Voynich zl_glyph, belirsiz boşluk birleşik | 4.3 | 1.07 | 0.96 | 1.03 | 0.73 |
| Voynich çizim türü A (zl_glyph) | metin kısa | | | | |
| Voynich çizim türü B (zl_glyph) | metin kısa | | | | |
| Voynich çizim türü C (zl_glyph) | metin kısa | | | | |
| Voynich çizim türü H (zl_glyph) | 4.0 | 1.07 | 0.95 | 1.07 | 0.71 |
| Voynich çizim türü P (zl_glyph) | metin kısa | | | | |
| Voynich çizim türü S (zl_glyph) | 4.7 | 1.11 | 0.99 | 1.54 | 1.10 |
| Voynich çizim türü T (zl_glyph) | metin kısa | | | | |
| doğal dil, düz, 22 dil (medyan [en az, en çok]) | 4.4 | 2.21 [1.52, 3.51] | 1.84 [1.32, 2.66] | 3.19 [2.01, 4.84] | 2.36 [1.41, 3.52] |

# Sınama: kelimelerin sırası bilgi taşıyor mu

Her metnin ilk 16000 kelimesinden kelime ikilisi modeli öğrenildi; görülmemiş sonraki 16000 kelimede, tek kelime sıklığı modeline göre kelime başına kaç bit kazandırdığı ölçüldü. Aynı ölçüm her satırın kelimeleri kendi içinde karıştırılarak tekrarlandı. "Sıra" sütunu ikisinin farkıdır: sıranın, birlikte geçmenin ötesinde taşıdığı bilgi (bit/kelime). Bire bir kelime kodlaması kaynak dille aynı değeri verir.

| metin | n | sıra (bit/kelime) | gerçek kazanç | karıştırılmış kazanç |
|---|---|---|---|---|
| Voynich eva_basic (aile düzeyinde: +0.032) | 1 | -0.007 | -0.012 | -0.005 |
| Voynich eva_glyph (aile düzeyinde: +0.017) | 1 | -0.008 | -0.012 | -0.004 |
| Voynich v101 (aile düzeyinde: +0.025) | 1 | +0.020 | +0.016 | -0.003 |
| Voynich zl_basic (aile düzeyinde: +0.024) | 1 | +0.010 | +0.002 | -0.008 |
| Voynich zl_glyph (aile düzeyinde: +0.019) | 1 | +0.005 | +0.002 | -0.003 |
| Voynich v101, belirsiz boşluk birleşik (aile düzeyinde: +0.010) | 1 | +0.009 | +0.003 | -0.006 |
| doğal dil, düz (medyan [en az, en çok]) | 22 | +0.522 [+0.164, +0.961] | +0.525 [+0.164, +0.983] | +0.003 [-0.004, +0.031] |
| dönem ve tür metinleri (medyan [en az, en çok]) | 5 | +0.254 [+0.181, +0.833] | +0.253 [+0.180, +0.840] | -0.001 [-0.001, +0.007] |
| verbose (medyan [en az, en çok]) | 20 | +0.458 [+0.020, +1.486] | +0.457 [+0.020, +1.568] | +0.000 [-0.001, +0.082] |
| codebook (medyan [en az, en çok]) | 20 | +0.255 [+0.013, +0.984] | +0.265 [+0.013, +0.985] | +0.002 [-0.004, +0.029] |
| grille (medyan [en az, en çok]) | 20 | +2.611 [+0.068, +5.590] | +2.915 [+0.068, +6.434] | +0.113 [+0.000, +1.145] |
| selfcite (medyan [en az, en çok]) | 20 | +0.005 [-0.001, +0.027] | +0.005 [-0.001, +0.037] | +0.000 [-0.001, +0.019] |
| slotcite (medyan [en az, en çok]) | 20 | +0.013 [+0.000, +0.070] | +0.013 [+0.000, +0.108] | +0.000 [-0.001, +0.074] |
| slotgram (medyan [en az, en çok]) | 20 | +0.000 [+0.000, +0.036] | +0.000 [+0.000, +0.077] | +0.000 [+0.000, +0.042] |
| automaton (medyan [en az, en çok]) | 20 | +0.000 [+0.000, +0.071] | +0.000 [+0.000, +0.071] | +0.000 [-0.001, +0.000] |
| italian_alberti_1440 | 1 | +0.295 | +0.294 | -0.001 |
| italian_cennini_tarif_1400 | 1 | +0.833 | +0.840 | +0.007 |
| latin_kempis_1420 | 1 | +0.181 | +0.180 | -0.001 |
| latin_pliny_bitki | 1 | +0.221 | +0.221 | +0.000 |
| spanish_celestina_1499 | 1 | +0.254 | +0.253 | -0.001 |

## Kısa metinler ve Voynich bölümleri (yarı boyu 3500 kelime)

| metin | sıra (bit/kelime) |
|---|---|
| Voynich eva_basic | +0.000 |
| Voynich eva_glyph | +0.000 |
| Voynich v101 | +0.011 |
| Voynich zl_basic | +0.005 |
| Voynich zl_glyph | +0.005 |
| Voynich v101, belirsiz boşluk birleşik | +0.005 |
| Voynich zl_glyph, belirsiz boşluk birleşik | +0.001 |
| Voynich Currier A (zl_glyph) | +0.005 |
| Voynich Currier B (zl_glyph) | +0.000 |
| Voynich çizim türü A (zl_glyph) | metin kısa |
| Voynich çizim türü B (zl_glyph) | metin kısa |
| Voynich çizim türü C (zl_glyph) | metin kısa |
| Voynich çizim türü H (zl_glyph) | +0.004 |
| Voynich çizim türü P (zl_glyph) | metin kısa |
| Voynich çizim türü S (zl_glyph) | +0.005 |
| Voynich çizim türü T (zl_glyph) | metin kısa |
| doğal dil, düz, 22 dil (medyan [en az, en çok]) | +0.316 [+0.131, +0.642] |
| italian_alberti_1440 | +0.162 |
| italian_cennini_tarif_1400 | +0.499 |
| latin_apicius_tarif | +0.620 |
| latin_cato_tarim | +0.074 |
| latin_celsus_ilac | +0.811 |
| latin_kempis_1420 | +0.054 |
| latin_macer_bitki | +0.325 |
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

# Sınama: yayımlanmış bir şifre aynı ölçümlerde nasıl görünüyor

Naibbe şifresi (Greshko 2025, Cryptologia) gerçek Latince metni, her harfi ya da harf çiftini birkaç eşsesli glif dizisinden biriyle yazarak EVA görünümlü metne çevirir; anahtarı bilen metni geri okur. Yazarın yayımladığı örnek şifreli metin (Plinius) burada Voynich ile aynı üç ölçümden geçiriliyor. Soru: içinde gerçek dil olan bir metin bu ölçümlerde Voynich gibi görünebilir mi. "Anahtarla çözülmüş parçalar" satırı aynı metnin, her şifreli kelimenin yerine karşılığı olan bir ya da iki harflik düz metin parçası konmuş hâlidir: doğru anahtar eldeyse sıra bilgisinin geri gelip gelmediğini gösterir (bu satırda sözlük ve büyüme sütunları parçalar çok kısa olduğu için yorumlanmaz).

| metin | yarı | ort. kelime uzunluğu | tür oranı k=2 | yeni kelime oranı k=2 | görülmemiş yarıda yeni kelime payı | sıra (bit/kelime) | tür/kelime | hapax/tür | ed1 |
|---|---|---|---|---|---|---|---|---|---|
| Naibbe, Plinius (eva_basic) | 16000 | 5.23 | 1.16 | 1.99 | 0.127 | +0.009 | 0.241 | 0.506 | 0.986 |
| Naibbe, Plinius (eva_basic) | 8000 | 5.23 | 1.08 | 1.60 | 0.205 | +0.003 | 0.323 | 0.605 | 0.970 |
| Naibbe, Plinius (eva_glyph) | 16000 | 4.80 | 1.13 | 1.89 | 0.127 | +0.009 | 0.241 | 0.506 | 0.991 |
| Naibbe, Plinius (eva_glyph) | 8000 | 4.79 | 1.06 | 1.53 | 0.205 | +0.003 | 0.323 | 0.605 | 0.979 |
| Naibbe, Plinius, anahtarla çözülmüş parçalar | 16000 | 1.55 | 1.12 | 3.70 | 0.004 | +0.396 | 0.025 | 0.142 | 0.970 |
| Naibbe, Plinius, anahtarla çözülmüş parçalar | 8000 | 1.56 | 1.05 | 1.35 | 0.012 | +0.259 | 0.043 | 0.173 | 0.962 |
| Voynich (eva_basic) | 16000 | 4.89 | 1.07 | 0.95 | 0.215 | -0.007 | 0.249 | 0.681 | 0.861 |
| Voynich (eva_basic) | 8000 | 4.78 | 1.03 | 0.97 | 0.248 | +0.009 | 0.311 | 0.688 | 0.856 |
| Voynich (eva_glyph) | 16000 | 4.30 | 1.03 | 0.86 | 0.215 | -0.007 | 0.249 | 0.681 | 0.884 |
| Voynich (eva_glyph) | 8000 | 4.12 | 0.99 | 0.86 | 0.248 | +0.009 | 0.311 | 0.688 | 0.879 |

# Sınama: sıra bilgisi kelime uçlarında mı duruyor

Her kelime ilk ve son glifine indirgendi ve sıra sınaması (16000 kelimelik yarılarla) indirgenmiş dizide yeniden koşuldu. Doğal dilde indirgeme bilgi kaybettirir (uç bağı ham sıranın altında kalır). "Uçlar yerinde" sütununda karşılaştırma metninde satırların ilk ve son kelimesi yerinde bırakıldı: uç bağı ile yakınsa bağ satır başı ve sonu alışkanlıklarından gelmiyor demektir. Voynich bandı: ham sıra en çok +0.038, uç bağı en az +0.056 ve son -> ilk en az +0.146.

Son üç sütun uç bağını ayrıştırır: önceki kelimenin son glifi sonrakinin ilk glifini, ilk glifi ilk glifini, son glifi son glifini ne kadar öngörüyor. İlk -> ilk ve son -> son, komşu kelimeler birbirine benzediğinde (kopyalama) yükselir; son -> ilk iki kelimenin birleşme yerindeki bağdır. Bu üç sütunda yalnız aynı satırdaki komşular sayılır (satır sonu ile sonraki satır başı arası dışarıda).

| metin | ham sıra | uç bağı | uç bağı, uçlar yerinde | son -> ilk | ilk -> ilk | son -> son |
|---|---|---|---|---|---|---|
| Voynich (eva_basic) | -0.008 | +0.095 | +0.089 | +0.166 | +0.036 | +0.012 |
| Voynich (eva_glyph) | -0.006 | +0.087 | +0.083 | +0.175 | +0.057 | +0.006 |
| Voynich (v101) | +0.018 | +0.076 | +0.071 | +0.252 | +0.073 | +0.011 |
| Voynich (zl_basic) | +0.005 | +0.078 | +0.075 | +0.190 | +0.037 | +0.007 |
| Voynich (zl_glyph) | +0.005 | +0.103 | +0.097 | +0.190 | +0.058 | +0.011 |
| Naibbe, Plinius (eva_basic) | +0.009 | +0.001 | +0.001 | +0.004 | -0.000 | -0.001 |
| Naibbe, Plinius, anahtarla çözülmüş parçalar | +0.395 | +0.398 | +0.398 | +0.489 | +0.121 | +0.127 |
| italian_alberti_1440 | +0.294 | +0.147 | +0.145 | +0.057 | +0.025 | +0.042 |
| italian_cennini_tarif_1400 | +0.832 | +0.410 | +0.400 | +0.101 | +0.071 | +0.103 |
| latin_apicius_tarif | kısa | | | | | |
| latin_cato_tarim | kısa | | | | | |
| latin_celsus_ilac | kısa | | | | | |
| latin_kempis_1420 | +0.181 | +0.073 | +0.071 | +0.024 | +0.018 | +0.040 |
| latin_macer_bitki | kısa | | | | | |
| latin_pliny_bitki | +0.221 | +0.065 | +0.070 | +0.013 | +0.013 | +0.043 |
| spanish_celestina_1499 | +0.253 | +0.160 | +0.157 | +0.034 | +0.031 | +0.069 |

| grup | n | ham sıra (en az, medyan, en çok) | uç bağı (en az, medyan, en çok) | uç bağı / ham sıra (medyan) | son -> ilk (en az, medyan, en çok) | ilk -> ilk (medyan) | Voynich bandında |
|---|---|---|---|---|---|---|---|
| doğal dil, düz | 22 | +0.165, +0.522, +0.960 | +0.072, +0.274, +0.622 | 0.53 | +0.004, +0.059, +0.161 | +0.052 | 0 |
| abjad | 20 | +0.100, +0.265, +0.616 | +0.032, +0.150, +0.355 | 0.57 | +0.010, +0.052, +0.148 | +0.046 | 0 |
| verbose | 20 | +0.041, +0.200, +1.490 | +0.009, +0.090, +0.476 | 0.37 | +0.004, +0.059, +0.177 | +0.023 | 0 |
| codebook | 20 | +0.075, +0.317, +0.937 | -0.043, +0.022, +0.159 | 0.07 | -0.012, +0.001, +0.063 | +0.003 | 0 |
| grille | 20 | +0.000, +2.249, +5.522 | +0.018, +0.342, +1.855 | 0.23 | +0.002, +0.030, +0.250 | +0.045 | 0 |
| selfcite | 20 | -0.003, +0.000, +0.107 | -0.003, +0.079, +0.323 | ham sıra sıfıra yakın | -0.039, +0.000, +0.057 | +0.024 | 0 |
| slotcite | 20 | +0.000, +0.006, +0.053 | +0.000, +0.021, +0.233 | ham sıra sıfıra yakın | -0.008, +0.002, +0.038 | +0.018 | 0 |
| slotgram | 20 | -0.001, +0.000, +0.079 | -0.001, +0.001, +0.129 | ham sıra sıfıra yakın | -0.006, +0.000, +0.024 | +0.002 | 0 |
| automaton | 20 | -0.001, +0.000, +0.189 | -0.000, +0.008, +0.422 | ham sıra sıfıra yakın | -0.003, +0.007, +0.644 | +0.002 | 1 |
