# Sınama: EVA'laştırma sınıflandırıcının kararını değiştiriyor mu

Her süreçten 300 anlamsız metin örneği üretildi. Her örnek iki kez sınıflandırıldı: özgün hâliyle ve altı glifi EVA'daki gibi çok harfli diziye açılmış hâliyle. Tablo oy sayısını verir.

| süreç | yazım | abjad | codebook | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|---|
| grille | özgün | 1 | 2 | 278 | 0 | 0 | 4 | 15 | 0 |
| grille | EVA'laştırılmış | 0 | 0 | 171 | 0 | 0 | 1 | 23 | 105 |
| selfcite | özgün | 0 | 0 | 0 | 0 | 282 | 15 | 3 | 0 |
| selfcite | EVA'laştırılmış | 1 | 0 | 0 | 0 | 86 | 93 | 87 | 33 |
| slotcite | özgün | 0 | 0 | 13 | 0 | 6 | 270 | 10 | 1 |
| slotcite | EVA'laştırılmış | 0 | 0 | 6 | 0 | 0 | 244 | 23 | 27 |
| slotgram | özgün | 5 | 3 | 14 | 0 | 8 | 24 | 246 | 0 |
| slotgram | EVA'laştırılmış | 0 | 0 | 10 | 0 | 2 | 34 | 199 | 55 |

# Sınama: tek bir tablo Voynich kadar değişken metin üretiyor mu

Her süreçten 12 el yazması üretildi; her biri tek tablo ve tek ayar kümesiyle 8 pencere. Birim Voynich pencereleri arası değişkenlik. "İç": pencerelerin kendi el yazmasının ortalamasına uzaklığı. "Arası": farklı el yazmalarının ortalamaları arasındaki uzaklık.

| görünüm | Voynich iç | grille iç | grille arası | selfcite iç | selfcite arası | slotcite iç | slotcite arası | slotgram iç | slotgram arası |
|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.92 | 0.33 | 6.17 | 1.68 | 6.83 | 0.82 | 7.55 | 0.75 | 11.50 |
| eva_glyph | 0.93 | 0.31 | 5.46 | 1.37 | 5.89 | 0.72 | 6.67 | 0.70 | 9.97 |
| v101 | 0.94 | 0.28 | 4.58 | 1.62 | 6.48 | 0.85 | 6.82 | 0.82 | 11.70 |
| zl_basic | 0.95 | 0.27 | 4.58 | 1.56 | 5.84 | 0.78 | 6.64 | 0.75 | 10.76 |
| zl_glyph | 0.95 | 0.26 | 3.78 | 1.26 | 4.88 | 0.68 | 5.65 | 0.69 | 9.39 |

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
| verbose (medyan [en az, en çok]) | 6 | 4.8 | 2.46 [1.72, 6.46] | 1.77 [1.17, 2.33] | 4.57 [2.57, 19.40] | 2.79 [1.28, 4.65] |
| codebook (medyan [en az, en çok]) | 6 | 6.0 | 1.52 [1.18, 2.53] | 1.03 [0.87, 1.81] | 2.34 [1.77, 3.17] | 1.15 [0.37, 2.14] |
| grille (medyan [en az, en çok]) | 6 | 3.7 | 3.83 [1.88, 5.80] | 1.46 [1.15, 1.87] | 27.02 [6.57, 614.80] | 9.48 [2.56, 69.60] |
| selfcite (medyan [en az, en çok]) | 6 | 3.8 | 1.36 [1.16, 1.79] | 1.16 [0.97, 1.81] | 0.93 [0.83, 1.44] | 0.76 [0.56, 0.95] |
| slotcite (medyan [en az, en çok]) | 6 | 4.1 | 3.16 [1.22, 8.70] | 1.18 [1.09, 1.75] | 14.83 [2.05, 54.80] | 2.04 [1.34, 10.67] |
| slotgram (medyan [en az, en çok]) | 6 | 4.3 | 1.18 [0.98, 1.35] | 1.03 [0.85, 1.23] | 1.13 [0.42, 2.87] | 0.88 [0.00, 1.11] |
