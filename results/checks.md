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
| dönem metni (15. yy), düz (medyan [en az, en çok]) | 3 | 4.7 | 2.09 [1.96, 2.30] | 1.79 [1.75, 1.96] | 3.67 [3.59, 4.39] | 3.17 [3.14, 3.57] |
| dönem metni (15. yy), seslisiz (medyan [en az, en çok]) | 3 | 2.5 | 1.63 [1.51, 1.87] | 1.35 [1.24, 1.48] | 2.61 [2.45, 2.93] | 1.94 [1.92, 2.23] |
| verbose (medyan [en az, en çok]) | 30 | 4.6 | 1.99 [1.08, 5.89] | 1.29 [0.97, 3.00] | 3.96 [1.41, 24.86] | 2.03 [0.99, 8.27] |
| codebook (medyan [en az, en çok]) | 30 | 3.8 | 1.36 [1.01, 2.19] | 0.98 [0.77, 1.29] | 2.16 [0.70, 11.74] | 0.84 [0.11, 2.85] |
| grille (medyan [en az, en çok]) | 30 | 4.3 | 3.40 [1.18, 17.03] | 1.55 [0.98, 4.33] | 24.83 [2.64, 862812500.00] | 6.41 [1.42, 343000000.00] |
| selfcite (medyan [en az, en çok]) | 30 | 4.3 | 1.36 [0.92, 2.28] | 1.33 [0.98, 2.07] | 0.79 [0.71, 1.01] | 0.77 [0.50, 0.92] |
| slotcite (medyan [en az, en çok]) | 30 | 4.4 | 2.71 [1.05, 10.18] | 1.31 [0.87, 2.78] | 6.75 [1.42, 146.04] | 3.27 [0.53, 40.56] |
| slotgram (medyan [en az, en çok]) | 30 | 3.9 | 1.20 [0.75, 3.90] | 0.95 [0.86, 1.24] | 1.26 [0.61, 2707.00] | 0.91 [0.00, 26.00] |
| automaton (medyan [en az, en çok]) | 30 | 4.5 | 0.99 [0.94, 2.12] | 0.98 [0.89, 1.03] | 1.07 [0.91, 27.07] | 0.93 [0.33, 1.12] |

## Voynich bölüm bölüm (yarı boyu 5000 kelime)

Bölümler kısa olduğu için daha küçük yarı boyuyla ölçüldü; doğal dil tabanı aynı boyda yeniden hesaplandı. Yeterince uzun olmayan bölümler ölçülemedi.

| metin | ort. kelime uzunluğu | tür oranı k=1 | tür oranı k=2 | yeni kelime oranı k=1 | yeni kelime oranı k=2 |
|---|---|---|---|---|---|
| Voynich Currier A (zl_glyph) | 3.9 | 1.10 | 0.97 | 0.94 | 0.65 |
| Voynich Currier B (zl_glyph) | 4.4 | 1.21 | 0.98 | 1.85 | 1.18 |
| Voynich çizim türü A (zl_glyph) | metin kısa | | | | |
| Voynich çizim türü B (zl_glyph) | metin kısa | | | | |
| Voynich çizim türü C (zl_glyph) | metin kısa | | | | |
| Voynich çizim türü H (zl_glyph) | 4.0 | 1.10 | 0.95 | 1.08 | 0.71 |
| Voynich çizim türü P (zl_glyph) | metin kısa | | | | |
| Voynich çizim türü S (zl_glyph) | 4.7 | 1.10 | 0.99 | 1.51 | 1.10 |
| Voynich çizim türü T (zl_glyph) | metin kısa | | | | |
| doğal dil, düz, 22 dil (medyan [en az, en çok]) | 4.4 | 2.22 [1.54, 3.50] | 1.84 [1.32, 2.61] | 3.21 [2.01, 4.79] | 2.37 [1.41, 3.53] |
