# Sınama: EVA'laştırma sınıflandırıcının kararını değiştiriyor mu

Her süreçten 300 anlamsız metin örneği üretildi. Her örnek iki kez sınıflandırıldı: özgün hâliyle ve altı glifi EVA'daki gibi çok harfli diziye açılmış hâliyle. Tablo oy sayısını verir.

| süreç | yazım | abjad | grille | plain | selfcite | verbose |
|---|---|---|---|---|---|---|
| grille | özgün | 1 | 299 | 0 | 0 | 0 |
| grille | EVA'laştırılmış | 0 | 185 | 1 | 0 | 114 |
| selfcite | özgün | 0 | 1 | 0 | 299 | 0 |
| selfcite | EVA'laştırılmış | 0 | 4 | 0 | 293 | 3 |

# Sınama: tek bir tablo Voynich kadar değişken metin üretiyor mu

Her süreçten 12 el yazması üretildi; her biri tek tablo ve tek ayar kümesiyle 8 pencere. Birim Voynich pencereleri arası değişkenlik. "İç": pencerelerin kendi el yazmasının ortalamasına uzaklığı. "Arası": farklı el yazmalarının ortalamaları arasındaki uzaklık.

| görünüm | Voynich iç | grille iç | grille arası | selfcite iç | selfcite arası |
|---|---|---|---|---|---|
| eva_basic | 0.92 | 0.32 | 6.01 | 1.67 | 6.70 |
| eva_glyph | 0.93 | 0.30 | 5.33 | 1.37 | 5.80 |
| v101 | 0.94 | 0.28 | 4.58 | 1.62 | 6.48 |
| zl_basic | 0.95 | 0.27 | 4.58 | 1.56 | 5.84 |
| zl_glyph | 0.95 | 0.26 | 3.78 | 1.26 | 4.88 |
