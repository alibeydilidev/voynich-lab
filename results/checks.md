# Sınama: EVA'laştırma sınıflandırıcının kararını değiştiriyor mu

Her süreçten 300 anlamsız metin örneği üretildi. Her örnek iki kez sınıflandırıldı: özgün hâliyle ve altı glifi EVA'daki gibi çok harfli diziye açılmış hâliyle. Tablo oy sayısını verir.

| süreç | yazım | abjad | grille | plain | selfcite | slotcite | verbose |
|---|---|---|---|---|---|---|---|
| grille | özgün | 1 | 293 | 0 | 0 | 6 | 0 |
| grille | EVA'laştırılmış | 0 | 179 | 1 | 0 | 15 | 105 |
| selfcite | özgün | 0 | 0 | 0 | 280 | 20 | 0 |
| selfcite | EVA'laştırılmış | 0 | 0 | 0 | 145 | 150 | 5 |
| slotcite | özgün | 0 | 16 | 0 | 13 | 271 | 0 |
| slotcite | EVA'laştırılmış | 0 | 4 | 0 | 0 | 285 | 11 |

# Sınama: tek bir tablo Voynich kadar değişken metin üretiyor mu

Her süreçten 12 el yazması üretildi; her biri tek tablo ve tek ayar kümesiyle 8 pencere. Birim Voynich pencereleri arası değişkenlik. "İç": pencerelerin kendi el yazmasının ortalamasına uzaklığı. "Arası": farklı el yazmalarının ortalamaları arasındaki uzaklık.

| görünüm | Voynich iç | grille iç | grille arası | selfcite iç | selfcite arası | slotcite iç | slotcite arası |
|---|---|---|---|---|---|---|---|
| eva_basic | 0.92 | 0.32 | 6.07 | 1.68 | 6.76 | 0.82 | 7.48 |
| eva_glyph | 0.93 | 0.30 | 5.38 | 1.37 | 5.84 | 0.71 | 6.62 |
| v101 | 0.94 | 0.28 | 4.58 | 1.62 | 6.48 | 0.85 | 6.82 |
| zl_basic | 0.95 | 0.27 | 4.58 | 1.56 | 5.84 | 0.78 | 6.64 |
| zl_glyph | 0.95 | 0.26 | 3.78 | 1.26 | 4.88 | 0.68 | 5.65 |
