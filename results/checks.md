# Sınama: EVA'laştırma sınıflandırıcının kararını değiştiriyor mu

Her süreçten 300 anlamsız metin örneği üretildi. Her örnek iki kez sınıflandırıldı: özgün hâliyle ve altı glifi EVA'daki gibi çok harfli diziye açılmış hâliyle. Tablo oy sayısını verir.

| süreç | yazım | abjad | grille | plain | selfcite | slotcite | slotgram | verbose |
|---|---|---|---|---|---|---|---|---|
| grille | özgün | 1 | 282 | 0 | 0 | 3 | 14 | 0 |
| grille | EVA'laştırılmış | 0 | 205 | 0 | 0 | 1 | 17 | 77 |
| selfcite | özgün | 0 | 0 | 0 | 282 | 16 | 2 | 0 |
| selfcite | EVA'laştırılmış | 0 | 0 | 0 | 116 | 76 | 83 | 25 |
| slotcite | özgün | 0 | 14 | 0 | 12 | 264 | 8 | 2 |
| slotcite | EVA'laştırılmış | 0 | 9 | 0 | 0 | 204 | 50 | 37 |
| slotgram | özgün | 5 | 17 | 0 | 8 | 23 | 247 | 0 |
| slotgram | EVA'laştırılmış | 1 | 17 | 0 | 0 | 22 | 201 | 59 |

# Sınama: tek bir tablo Voynich kadar değişken metin üretiyor mu

Her süreçten 12 el yazması üretildi; her biri tek tablo ve tek ayar kümesiyle 8 pencere. Birim Voynich pencereleri arası değişkenlik. "İç": pencerelerin kendi el yazmasının ortalamasına uzaklığı. "Arası": farklı el yazmalarının ortalamaları arasındaki uzaklık.

| görünüm | Voynich iç | grille iç | grille arası | selfcite iç | selfcite arası | slotcite iç | slotcite arası | slotgram iç | slotgram arası |
|---|---|---|---|---|---|---|---|---|---|
| eva_basic | 0.92 | 0.32 | 6.10 | 1.68 | 6.79 | 0.82 | 7.51 | 0.75 | 11.48 |
| eva_glyph | 0.93 | 0.30 | 5.38 | 1.37 | 5.84 | 0.71 | 6.62 | 0.70 | 9.94 |
| v101 | 0.94 | 0.28 | 4.58 | 1.62 | 6.48 | 0.85 | 6.82 | 0.82 | 11.70 |
| zl_basic | 0.95 | 0.27 | 4.58 | 1.56 | 5.84 | 0.78 | 6.64 | 0.75 | 10.76 |
| zl_glyph | 0.95 | 0.26 | 3.78 | 1.26 | 4.88 | 0.68 | 5.65 | 0.69 | 9.39 |
