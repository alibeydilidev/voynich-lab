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
