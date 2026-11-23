# voynich-lab

Voynich el yazmasına (Beinecke MS 408) "ne yazıyor" diye değil, "bunu nasıl bir süreç üretti" diye soran hat. Yöntem simülasyon tabanlı çıkarım: aday üretim süreçlerini simüle et, sembol adından bağımsız feature çıkar, XGBoost ile süreç sınıflandırıcısı eğit, Voynich'i içine at.

Bu dosya projenin devir notudur. Kararların gerekçesi burada, kodu değiştirmeden önce oku.

## Amaç ve hedef merdiveni (Ali kararı, 2026-11-23)

Birincil amaç: Voynich el yazmasını toplulukça kabul edilebilir ve kanıtlanabilir biçimde tercüme etmek. Tercüme sözü verilmez; metnin anlam taşıdığı bile belli değil. Bu yüzden amaç basamaklıdır ve her basamak kendi başına başarı sayılır:

1. **Süreç:** metni hangi süreç üretti. Mevcut hat bu basamaktır. Sonuç "anlamsız üretim" çıkarsa tercüme yoktur ve bu, kanıtıyla birlikte yayınlanabilir bir sonuçtur.
2. **Daraltma:** metin anlam taşıyorsa hangi dil ailesi ve hangi şifre ya da yazım türü.
3. **Çözme denemesi:** yalnız 1. ve 2. basamak geçildiyse, aşağıdaki çözme kapısıyla birlikte.

Sonuç hangi basamakta kalırsa iddia o basamağın adıyla yapılır. Kapıdan geçmemiş bir çıktı için "çözüldü" denmez.

### Çözme kapısı

Metne anlam atayan kod ancak şu koşulların hepsi sağlanınca yazılır:

- 1. basamak sonucu anlam taşıyan bir süreci gösteriyor ve Voynich o sınıf için dağılım içi (ilke 2).
- 2. basamak aday dil ve şifre türünü daraltmış.
- Aşağıdaki beş sınav, çözme kodundan ÖNCE koda yazılmış ve sentetik bilinen-cevaplı metinde çalıştığı gösterilmiş:
  1. **Tek sabit kural:** bütün metne aynı kural uygulanır, kelime bazında serbest seçim yok.
  2. **Görülmemiş sayfa sınavı:** kural bir sayfa kümesinden çıkarılır, hiç bakılmamış sayfalarda sınanır.
  3. **Boş sınav:** aynı yöntem karıştırılmış ve sahte (üreteç çıktısı) metinde "anlam" çıkarmamalı.
  4. **Çizimle kör eşleşme:** çıktı çizimlere bakılmadan üretilir, eşleşme sonradan ölçülür.
  5. **Tekrarlanabilirlik:** kilitli ortamda tek komutla aynı sonuç.
- Kapının açıldığına Ali karar verir.

## Değişmez ilkeler

1. **Kapı geçilmeden çeviri iddiası ve anlam atayan kod yok.** Ground truth yok, loss tanımlanamıyor. LLM'e "çevir" demek akıcı uydurma üretir. Metne anlam atayan kod yalnız yukarıdaki çözme kapısı açılınca yazılır. (2026-11-23 öncesi bu ilke mutlak yasaktı; Ali kararıyla kapıya çevrildi.)
2. **Her iddia yanlışlanabilir olmalı.** Çıktı "X sürecine benziyor" ise yanında dağılım dışı (OOD) skoru durur. OOD kötüyse sınıf olasılığı bulgu sayılmaz.
3. **Feature'lar sembol adına bakmaz.** Yalnızca dağılım şekli. Bu sayede Latince, İbranice, EVA ve v101 aynı uzayda durur. Testi: `test_monoalphabetic_substitution_is_invisible`.
4. **Pencere boyutu her yerde aynı.** Entropi ve TTR örneklem boyutuna duyarlı. Sentetik ve Voynich pencereleri aynı `--window` ile kesilir.
5. **En az iki transliterasyon.** Tek transliterasyonda çıkan sonuç, transliterasyonun eseri olabilir. Sonuç görünümler arasında tutarlı değilse bulgu değildir.
6. **CV dil bazında gruplu.** Model hiç görmediği dilde sınanır.

## Komutlar

```bash
uv sync --extra dev --locked        # sürümler uv.lock ile sabit, Python 3.12
source .venv/bin/activate
python -m voynich_lab.cli fetch     # ham veri -> data/raw (depoya girmez)
python -m voynich_lab.cli build     # sentetik feature tablosu, ~80 sn
python -m voynich_lab.cli report    # CV + eğitim + Voynich analizi -> results/report.md
python -m voynich_lab.cli all       # fetch + build + report, ~1 dk
python -m voynich_lab.cli abc       # büyük tablo + ABC raporu -> results/abc.md, 4 çekirdekte ~3 dk
pytest -q
```

Parametreler: `--window 2000`, `--per-language 24`, `--seed 7`. ABC için: `--abc-per-language 100`, `--abc-seeds 4`, `--accept 0.01`, `--jobs 4`; var olan tabloyu yeniden kullanır, `--rebuild` baştan üretir.

## Mimari

| Dosya | Görev |
|---|---|
| `transliteration.py` | Takahashi EVA, Claston v101 ve Zandbergen-Landini (IVTFF) ayrıştırıcıları, beş görünüm (`eva_basic`, `eva_glyph`, `v101`, `zl_basic`, `zl_glyph`), pencereleme |
| `corpus.py` | 22 dilde paralel İncil, yazıya göre normalizasyon |
| `generators.py` | Üretim süreçleri. `LANGUAGE_PROCESSES` gerçek metni dönüştürür, `GIBBERISH_PROCESSES` sıfırdan üretir. Hepsinin üstünde ortak yazıcı katmanı (`Layout`, `lay_out`, `finish`): nadir harf çeşitlemeleri, kelime başı ve sonu için özel harf biçimleri, satırı genişliğe göre doldurma, paragraf, satır başı, satır sonu ve paragraf başı alışkanlıkları |
| `features.py` | 32 feature: entropi, kelime uzunluğu, dağarcık, tekrar, kelime içi konum, satır konumu |
| `dataset.py` | Sentetik korpus fabrikası: (dil penceresi x süreç) -> satır. Her satır üreten ayarları da taşır (`p_` süreç, `l_` yazıcı katmanı) |
| `model.py` | XGBoost, `GroupKFold` |
| `analyze.py` | Voynich çıkarımı, SHAP katkıları (`pred_contribs`), Mahalanobis tabanlı OOD |
| `abc.py` | Rejection ABC: her sınıf Voynich'e en fazla ne kadar yaklaşıyor, neyi tutturamıyor, hangi ayarlarla. Mesafe birimi Voynich'in kendi pencereleri arası değişkenlik |
| `cli.py`, `fetch.py` | Komut satırı ve indirme |

Ortak veri tipi `Lines = list[list[str]]`: satırlar, kelimeler, her karakter bir glif. Çok harfli glifler Unicode özel kullanım alanındaki tek karaktere eşlenir.

Sınıflar: `plain` (doğal dil, tek alfabeli ikame dahil), `abjad` (seslisiz yazım), `verbose` (harf başına 1-3 sembol), `grille` (Rugg tablosu: önek, gövde, sonek heceleri; sütunların glif kümeleri ayrık ya da örtüşük), `selfcite` (Timm ve Schinner kendinden kopyalama; yeni kelimeler yuva yapısından).

Yeni süreç eklemek: fonksiyonu `generators.py` içine yaz, sonunda `lay_out(kelimeler, rng, layout)` çağır, ilgili sözlüğe ekle. Başka hiçbir yere dokunmak gerekmez.

Yazıcı katmanının kuralı: parametreleri (`sample_layout`) bütün sınıflar için aynı önselden çekilir ve "hiç satır etkisi yok" durumunu da içerir. Sınıfa özel satır kuralı yazılmaz; yazılırsa sınıflandırıcı onu kestirme yol yapar. Önsel aralıkları Voynich'e göre ayarlanmaz, o iş ABC adımınındır.

## v0 bulguları (2026-11-23, seed 7, pencere 2000)

Tarihçe. Güncel durum bir alttaki v0.1 bölümünde; `results/report.md` artık v0.1 raporudur. v0 raporu git geçmişinde (`dcb7aba`).

- **Sentetik veride CV doğruluğu 0.995.** Bu iyi haber değil: sınıflar fazla kolay ayrışıyor, yani üreteçler birbirinden karikatür düzeyinde farklı.
- **Voynich üç görünümde de dağılım dışı.** En yakın sınıfa mesafesi, o sınıfın kendi medyanının 8 ila 9 katı, yüzdelik 100. Dolayısıyla sınıf olasılıkları (`eva_basic`'te `verbose` 0.50, `eva_glyph`'te `plain` 0.35, v101'de `plain` 0.40 önde) şu an bulgu değil, "en az kötü eşleşme".
- **Sınıf tahmini ortama da duyarlı.** İlk v0 raporu başka bir ortamda `eva_glyph` için `verbose`, v101 için `selfcite` vermişti; aynı kod ve seed ile bu ortamda ikisi de `plain` çıktı. CV, feature ortalamaları ve OOD oranları değişmedi. Bu yüzden sürümler `uv.lock` ile sabitlendi (2026-11-23). Kilit güncellenirse rapor yeniden üretilir ve fark raporlanır.
- **Karar transliterasyona göre değişiyor.** İlke 5'in neden var olduğunun kanıtı.
- **Feature'lar bilinen Voynich anomalilerini kendiliğinden yakaladı**, bu hattın doğru şeyi ölçtüğünü gösteriyor:
  - `h2` (koşullu entropi) EVA'da 2.04, doğal dillerde 3.0 ila 3.5. Literatürdeki değerlerle uyumlu.
  - `jsd_last` 0.71, sentetik evrenin tavanı 0.59. Kelime sonu glifleri aşırı kısıtlı.
  - `jsd_line_initial` 0.26 ila 0.29, sentetik tavan 0.12. Satır başı kelimeleri farklı davranıyor. Rastgele satır kırılımıyla bu üretilemez.
  - `vocab_ed1_density` 0.8 civarı, düz doğal dilde 0.4. Kelime dağarcığı "tek harf farklı" komşularla dolu.

Yani v0'ın gerçek çıktısı şu: **beş basit hipotezin hiçbiri Voynich'i üretemiyor, ve hangi dört özellikte çuvalladıkları belli.** Sonraki iş bu dört özelliği üretebilen süreçler yazmak.

## v0.1 bulguları: satır farkındalığı (2026-11-23, seed 7, pencere 2000)

Tarihçe; rapor git geçmişinde (`d0d51d5`). İki değişiklik: Takahashi ayrıştırıcısında hata düzeltmesi ve üreteçlere ortak yazıcı katmanı.

- **Ayrıştırıcı hatası.** Takahashi dosyasında satır ortasındaki `-` (çizimin metni böldüğü yer) glif sayılıyordu: 752 tire, 671 yapışık kelime. Artık kelime sınırı. En çok kelime uzunluğu dağılımını etkiledi: `wlen_skew` 0.79 -> 0.07, `wlen_std` 1.92 -> 1.69 (`eva_basic`). v0'da `eva_basic` tahminini en çok etkileyen feature `wlen_std` idi, yani o tahmin kısmen bu hatanın ürünüydü.
- **Satır etkisi gerçek, ölçüm yanılgısı değil.** Kelimeler pencere içinde karıştırılınca `jsd_line_initial` 0.22 -> 0.013, `jsd_line_final` 0.11 -> 0.012 (`eva_basic`). Paragraf ilk satırları çıkarılınca etki sürüyor (0.21): yalnız paragraf başı süs harfi değil.
- **Hangi glifler (EVA).** Paragraf ilk satırı `p` (%46) ya da `t` (%24) ile başlıyor; satır içinde bunlar %0.5 ve %1.8. Diğer satır başlarında `y`, `d`, `s` fazla, `ch` grubu az. Satır sonunda `m` %18, satır içinde %0.9.
- **Satır başı kelimelerinin uzun olması bulgu değil.** Voynich'in kendi kelimeleri karıştırılıp yalnız genişliğe göre yeniden dizilince satır başı uzunluk oranı 1.09 çıkıyor; gerçek değer 1.09 (üç görünümde de beklenen aralığın içinde). Satırı genişliğe göre dolduran her yazıcı bunu üretir.
- **Satır sonu kelimelerinin kısa olması yalnız EVA'da.** `eva_basic` 0.93, doldurma beklentisi 1.00 [0.97, 1.04]; v101'de 1.00. Görünümler arasında tutarsız, ilke 5 gereği bulgu değil.
- **Yazıcı katmanıyla OOD oranı düştü ama Voynich hâlâ dağılım dışı.** Mesafe / sınıf medyanı: `eva_basic` 8.0x -> 2.3x, `eva_glyph` 8.2x -> 2.1x, v101 9.0x -> 5.0x. Yüzdelik hâlâ 100. Düşüşün neredeyse tamamı yazıcı katmanından (ayrıştırıcı düzeltmesi tek başına 8.0x -> 7.8x).
- **Sınıf tahmini hâlâ bulgu değil.** EVA görünümleri `grille` (0.54), v101 `selfcite` (0.36). Görünümler tutarsız ve OOD.
- **Kestirme yol denetimi.** Yalnız iki satır JSD feature'ı ile CV doğruluğu 0.27 (şans 0.20): yazıcı katmanı sınıf sızdırmıyor. Satır uzunluk oranlarıyla 0.50 çıkıyor, çünkü doldurma etkisinin büyüklüğü kelime uzunluğu yayılımına bağlı (korelasyon 0.86); bu sınıfın meşru sonucu, sızıntı değil.
- **Kalan açık (EVA, en yakın sınıfa göre).** `jsd_last` 0.72 (sentetik tavan 0.59, pencerelerin %100'ü aralık dışı), `h2` ve `h2_over_h1`, `hapax_ratio`. Üçü de kelime içi yapıyla ilgili. v101'de ek olarak `n_symbols`.
- **CV doğruluğu 0.997.** Sınıflar hâlâ fazla kolay ayrışıyor; v0'daki uyarı geçerli.

## v0.2 bulguları: kelime içi yapı (2026-11-23, seed 7, pencere 2000)

Tarihçe; rapor git geçmişinde (`7afdba9`). **Bu bölümdeki "doğal dil tabanlı sınıfların toplamı 0.02'nin altında" sonucu v0.3'te geri alındı**, aşağıya bak. Eklenenler: yazıcı katmanına konuma özgü harf biçimleri (`Forms`) ve nadir harf çeşitlemeleri (`Allographs`); `grille` için ayrık sütun alfabeleri, büyük tablo ve büyük hece envanteri; `selfcite` için yuva yapılı yeni kelimeler ve geniş kopyalama ayarları.

- **Voynich'te glifin kelimedeki yeri aşırı sabit (EVA).** `n` %99 ve `m` %96 kelime sonunda, `q` %99 kelime başında, `y` %88 sonda; `e`, `h`, `i` neredeyse hiç uçta değil. `jsd_last` 0.72 bunun ölçüsü.
- **Artık hiçbir feature sentetik aralığın dışında değil** (üç görünümde de). v0'da altı feature dışarıdaydı.
- **OOD oranı:** `eva_basic` 1.8x (yüzdelik 99), `eva_glyph` 1.4x (95), v101 1.5x (96). v0'da 8 ila 9x idi. Hâlâ sınırda dağılım dışı: en yakın sınıfın örneklerinin %95 ila %99'u Voynich'ten daha merkezde.
- **En yakın sınıf üç görünümde de `grille`.** Sınıf olasılığı: `eva_basic` `grille` 0.49 / `selfcite` 0.50, `eva_glyph` `grille` 0.74, v101 `grille` 0.83. Doğal dil tabanlı üç sınıfın (`plain`, `abjad`, `verbose`) toplamı her görünümde 0.02'nin altında.
- **Bu henüz "Voynich anlamsız" demek değil.** İki neden: (1) OOD sınırı geçilmedi; (2) doğal dil tarafında yalnız üç kodlama ve modern İncil var, anlamsız metin tarafı ise bu oturumda çok daha fazla işlendi. Hece yazısı, homofonik şifre, kısaltmalı Latince ve dönem metinleri eklenmeden dil hipotezi adil sınanmış sayılmaz.
- **Doğal dil sınıflarını Voynich'ten ayıran feature'lar:** `h2` (Voynich 2.0 ila 2.4, `plain` en az 2.6), `wlen_skew` (0.1 ila 0.2, `plain` en az 0.29), `wlen_autocorr1` (+0.10 ila +0.18, `plain` en çok +0.06), `vocab_ed1_density` (0.82 ila 0.85, `plain` en çok 0.75).
- **Komşu kelimeler uzunlukça benziyor ve bu gerçek bir komşuluk etkisi.** `eva_basic`: tüm komşular +0.14; sayfa içinde karıştırınca +0.035, satır içinde karıştırınca +0.07, gerçek satır içi sıra +0.16. Yani sayfa ve satır bileşimi etkinin yarısını açıklıyor, kalanı sıradan geliyor. Doğal dilde bu değer negatif. `grille` bunu üretemiyor (en çok +0.14), `selfcite` üretiyor.
- **`grille` için kalan açık:** kelime uzunluğu (`type_len_mean` 5.7, `wlen_std` 1.7; üç yuvalı tablo bu kadar uzun ve yayvan kelime üretmiyor) ve `wlen_autocorr1`.
- **CV doğruluğu 0.981.** Sınıflar eskisi kadar karikatür değil ama hâlâ kolay ayrışıyor.
- **Kestirme yol denetimi:** satır feature'ları olmadan CV 0.982, yani yazıcı katmanı sınıf bilgisi taşımıyor.

## v0.3 bulguları: ABC, üçüncü transliterasyon, adil şifre hipotezi (2026-11-23, seed 7, pencere 2000)

Güncel durum budur. Raporlar: `results/report.md` (sınıflandırıcı) ve `results/abc.md` (ABC, 42800 sentetik örnek, sınıf başına en yakın %1 kabul).

Eklenenler: `abc.py` ve `cli abc`; Zandbergen-Landini transliterasyonu (`zl_basic`, `zl_glyph`); `verbose` için hece hece yazma ve sürekli boşluk ekleme; üreteçlerin çektiği ayarların kaydı.

- **ABC ölçütüyle hiçbir hipotez Voynich'i üretemiyor.** Mesafe birimi Voynich'in kendi pencereleri arası değişkenlik. Voynich öz mesafesi medyan 0.9 ila 1.0, en çok 1.4 ila 1.65. Hiçbir sınıfta, hiçbir görünümde, Voynich'in en uç penceresi kadar yakın tek bir örnek yok (%0.00). En iyi tek örnek: `grille`, v101'de 1.46 (sınır 1.42).
- **Sıralama beş görünümde de aynı yönde:** `grille` en yakın (kabul edilenlerin medyanı 2.07 ila 2.80), beşte dördünde ikinci `verbose` (2.89 ila 3.98), sonra `selfcite`, `plain`, `abjad`.
- **v0.2'deki bir sonuç geri alındı.** v0.2'de `verbose` üreteci kelime sınırlarını neredeyse hep koruyordu ve dil tabanlı sınıflar 0.02'nin altında olasılık alıyordu. `verbose` hece hece yazabilir olunca sınıflandırıcı düz EVA görünümlerinde `verbose` dedi (`eva_basic` 0.61, `zl_basic` 0.75), birleşik glif ve v101 görünümlerinde `grille` (0.46 ila 0.82). ABC'de kabul edilen `verbose` örneklerinin tamamına yakını hece modunda. Ders: bir hipotezin elenmesi, o hipotezin üretecinin dar yazılmış olmasından kaynaklanabilir. Dil tarafı hâlâ eksik, o yüzden hiçbir yönde hüküm yok.
- **Sınıflandırıcının kararı harf tanımına bağlı, okuyana değil.** Takahashi ile Zandbergen-Landini aynı modda aynı sonucu veriyor (`eva_basic` ve `zl_basic` ikisi de `verbose`; `eva_glyph` ve `zl_glyph` ikisi de `grille`). Ayrışma "hangi çizgiler tek harf" kararından geliyor: düz EVA tek glifi birkaç harfle yazdığı için (ch, sh, cth, iin) metin kendiliğinden verbose şifreye benziyor.
- **Sınıflandırıcı ile ABC farklı soruya cevap veriyor.** Sınıflandırıcı "beş sınıftan hangisi", ABC "bu sınıf ne kadar yaklaşabiliyor" der. Düz EVA'da sınıflandırıcı `verbose`, ABC `grille` diyor. İkisi tutmadığı sürece sınıf adı bulgu değildir.
- **`grille` neyi tutturamıyor (beş görünümde tekrar edenler):** `wlen_autocorr1` (komşu kelime uzunluk benzerliği üretemiyor, -2.5 ila -3.5 birim), `vocab_ed1_density` (fazla yoğun, +2.2 ila +4.6), `wlen_std` ve `type_len_mean` (kelimeler kısa ve dar), `hapax_ratio` (az).
- **`verbose` neyi tutturamıyor:** `hapax_ratio` (az), `jsd_last` (kelime sonu kısıtı zayıf), `wlen_std` ve `wlen_skew` (kelime uzunluğu fazla yayvan ve çarpık), `wlen_autocorr1`.
- **`selfcite` neyi tutturamıyor:** `h2` (fazla yüksek), `char_double_rate`, `rep_adjacent_exact` (fazla tekrar). Kabul edilen örneklerde geriye bakış uzaklığı önselin üst ucuna kayıyor (5 -> 19 satır): yakın kopyalama Voynich'e uymuyor.
- **Bu ABC'nin sınırı.** Rejection ABC rastgele dener; 32 feature'ı aynı anda tutturan örnek seyrek olduğu için yazıcı katmanı ayarları neredeyse hiç kısıtlanmıyor (kabul edilenlerde `jsd_line_final` 0.02, Voynich 0.11). Yani mesafeler hipotezlerin gerçekte ulaşabileceğinden kötü. Sıradaki iş, en yakın örneklerin çevresinde yeniden arayan ABC (SMC); bunun için üreteçler ayarları dışarıdan alabilmeli.
- **Sınıflandırıcı raporu:** CV 0.977. OOD oranı 1.4 ila 1.6x, yüzdelik 94 ila 98; hiçbir feature aralık dışında değil.

## Yol haritası (öncelik sırasıyla)

1. **Üreteç sadakati.** Asıl kaldıraç burada.
   - ~~Satır farkındalığı~~: yapıldı (v0.1, ortak yazıcı katmanı). Paragraf düzeyi feature yok; paragraf başı `p`/`t` etkisi yalnız `jsd_line_initial` içinden dolaylı görünüyor.
   - ~~Kelime içi konum grameri~~: yapıldı (v0.2). Üç yuvayla sınırlı; literatürdeki çok yuvalı kelime gramerleri denenmedi.
   - Verbose şifreye konuma duyarlı kod tabloları.
   - `selfcite` parametrelerini Timm ve Schinner 2019 makalesindeki değerlere çek.
   - Yeni sınıflar: homofonik şifre, hece yazısı, kısaltmalı Latince (ortaçağ abbreviatura).
2. **ABC ile parametre kestirimi.** Rejection ABC yapıldı (v0.3). **Sıradaki:** üreteçleri ayarları dışarıdan alacak hale getir, en yakın örneklerin çevresinde yeniden arayan ABC-SMC yaz. Ölçüt aynı: kabul edilen örnekler Voynich öz mesafesinin içine giriyor mu.
3. **Dönem metinleri.** İncil çevirileri modern. 15. yüzyıl Latince, İtalyanca, Almanca, İbranice, Osmanlıca öncesi Türkçe tıbbi ve botanik metinler ekle. `corpus.py` düz kelime listesi bekliyor, yeni yükleyici yazmak yeterli.
4. ~~Üçüncü transliterasyon~~: yapıldı (v0.3). `fetch` indiriyor; site Python'un varsayılan istemci adını reddettiği için genel bir ad gönderiliyor.
5. **Bölüm ve lehçe kırılımı.** Currier A ve B, beş yazıcı eli, çizim bölümleri (bitki, astronomi, banyo, reçete) için ayrı analiz. Folio aralıkları zaten pencere etiketinde.
6. **İkinci hat: char-level Transformer.** Yalnızca Voynich üzerinde küçük bir model eğit, sayfa embedding'leri çizim bölümlerine göre kümeleniyor mu bak. Kümeleniyorsa metin konuyla ilişkili. Kontrol: aynı testi satırları karıştırılmış metinde ve `selfcite` çıktısında tekrarla.

## Bilinen tuzaklar

- Takahashi'de satır ortasındaki `-` çizim boşluğudur ve melez davranır: boşluktan sonraki kelime satır başı gibi (`y`, `d`, `s` fazla, `q` az), ama boşluktan önceki kelime satır sonu gibi değil (`m` %2.5, gerçek satır sonunda %17). Şu an yalnız kelime sınırı sayılıyor, satır sınırı değil. Satır etkilerini biraz seyreltir. `m` gerçek satır sonuna (kenar boşluğuna) özgü görünüyor.
- v101'de ve ZL'de virgül "belirsiz boşluk". Varsayılan boşluk sayılıyor (`comma_is_space=True`). Tersi hiç koşulmadı; ZL'de 2748 virgül var. Koş, sonuç değişiyorsa raporla.
- ZL'de yalnız `P0` satırları alınıyor (Takahashi `P` satırlarının karşılığı: 3885 ve 3868 satır). Nadir ve bileşik glifler (`{...}`, `@123;`) içerik başına tek sembole eşleniyor: 149 tür, 434 geçiş. Bu yüzden `zl_*` görünümlerinde sembol sayısı yüksek, `Allographs` katmanı bunu kapsıyor.
- ZL dosyası `<->` işaretini "çizim metni kesiyor" diye belgeliyor; Takahashi'deki satır içi `-` yorumumuzu doğrular.
- `n_symbols` v101'de 70 civarı. v0.2'de nadir harf çeşitlemeleri katmanı (`Allographs`) eklendi, sentetik evren artık bunu kapsıyor.
- `eva_glyph` yalnızca ch, sh ve sehpalı gallows'ları birleştiriyor. `iin`, `ain` gibi diziler de tek glif olabilir, tartışmalı.
- Mahalanobis mesafeleri sınıf içi örneklerle (in-sample) kalibre ediliyor, biraz iyimser. Örnek sayısı feature sayısının çok üstünde olduğu için etkisi küçük.
- Veri küçük (paragraf metni: Takahashi 32.8 bin, v101 36 bin kelime; pencere başına 2000). Pencere boyutunu küçültmek pencere sayısını artırır ama entropi tahminlerini bozar.

## Veri kaynakları

- Takahashi EVA: `alephmembeth/voynich` (GitHub)
- Zandbergen ve Landini (ZL), IVTFF 2.0: `voynich.nu/data/ZL3b-n.txt` (sürüm 3b, 13/05/2025). Aynı dizinde Currier dili, el ve çizim türü sayfa değişkenleri olarak hazır (yol haritası 5 için).
- Claston v101: `musyoku/voynich-transcription` (GitHub)
- İncil korpusu: `christos-c/bible-corpus` (GitHub)

Ham veri depoya girmez, `fetch` ile yeniden üretilir.
