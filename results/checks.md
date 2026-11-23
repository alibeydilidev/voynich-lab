# Sınama: EVA'laştırma sınıflandırıcının kararını değiştiriyor mu

Her süreçten 300 anlamsız metin örneği üretildi. Her örnek iki kez sınıflandırıldı: özgün hâliyle ve altı glifi EVA'daki gibi çok harfli diziye açılmış hâliyle. Tablo oy sayısını verir.

| süreç | yazım | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| grille | özgün | 1 | 279 | 0 | 0 | 9 | 11 | 0 |
| grille | EVA'laştırılmış | 0 | 160 | 1 | 0 | 15 | 32 | 92 |
| selfcite | özgün | 0 | 0 | 0 | 277 | 19 | 4 | 0 |
| selfcite | EVA'laştırılmış | 0 | 0 | 0 | 114 | 120 | 58 | 8 |
| slotcite | özgün | 0 | 12 | 0 | 12 | 267 | 9 | 0 |
| slotcite | EVA'laştırılmış | 0 | 4 | 0 | 0 | 253 | 21 | 22 |
| slotgram | özgün | 6 | 16 | 0 | 9 | 29 | 240 | 0 |
| slotgram | EVA'laştırılmış | 4 | 9 | 0 | 0 | 39 | 205 | 43 |

# Sınama: tek bir tablo Voynich kadar değişken metin üretiyor mu

Her süreçten 12 el yazması üretildi; her biri tek tablo ve tek ayar kümesiyle 8 pencere. Birim Voynich pencereleri arası değişkenlik. "İç": pencerelerin kendi el yazmasının ortalamasına uzaklığı. "Arası": farklı el yazmalarının ortalamaları arasındaki uzaklık.

| görünüm | Voynich iç | grille iç | grille arası | selfcite iç | selfcite arası | slotcite iç | slotcite arası | slotgram iç | slotgram arası |
|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.92 | 0.32 | 6.11 | 1.68 | 6.78 | 0.82 | 7.50 | 0.75 | 11.47 |
| eva_glyph | 0.93 | 0.30 | 5.41 | 1.37 | 5.86 | 0.72 | 6.64 | 0.70 | 9.96 |
| v101 | 0.94 | 0.28 | 4.58 | 1.62 | 6.48 | 0.85 | 6.82 | 0.82 | 11.70 |
| zl_basic | 0.95 | 0.27 | 4.58 | 1.56 | 5.84 | 0.78 | 6.64 | 0.75 | 10.76 |
| zl_glyph | 0.95 | 0.26 | 3.78 | 1.26 | 4.88 | 0.68 | 5.65 | 0.69 | 9.39 |
