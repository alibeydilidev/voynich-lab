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
7. **Sınıflandırıcının sınıf adı başlık değildir.** 2026-11-23 oturumunda sınıflandırıcının kararı, yalnız bir üretecin önseli genişletildiği için üç kez yön değiştirdi (v0.2 `grille`, v0.3 düz EVA'da `verbose`, v0.4 her yerde `grille`). Bir hipotez hakkında hüküm el yazması düzeyinde ve doğrulama yarısında verilir (`cli manuscripts`) ve iki ölçüt birlikte aranır: (a) pencere profili: tek tablo ve tek ayarla üretilen uzun metnin, seçimde kullanılmayan yarısı Voynich'in kendi yarıları kadar yakın mı (T); (b) büyüme profili: aynı yarının tamamında dağarcık Voynich'inki gibi büyüyor mu. Yalnız biri tutuyorsa hipotez geçmiş sayılmaz. Sınıflandırıcı raporu, pencere düzeyi ABC ve arama yardımcı göstergedir.

## Komutlar

```bash
uv sync --extra dev --locked        # sürümler uv.lock ile sabit, Python 3.12
source .venv/bin/activate
python -m voynich_lab.cli fetch     # ham veri -> data/raw (depoya girmez)
python -m voynich_lab.cli build     # sentetik feature tablosu, ~80 sn
python -m voynich_lab.cli report    # CV + eğitim + Voynich analizi -> results/report.md
python -m voynich_lab.cli all       # fetch + build + report, ~1 dk
python -m voynich_lab.cli abc       # büyük tablo + ABC raporu -> results/abc.md, 4 çekirdekte ~3 dk
python -m voynich_lab.cli search    # abc tablosundan başlayan yönlendirilmiş arama -> results/search.md, ~6 dk
python -m voynich_lab.cli manuscripts --rebuild --ms-per-class 2000   # el yazması düzeyi -> results/manuscripts.md, ~8 dk
python -m voynich_lab.cli checks    # hattın kendi sonuçlarını sınayan deneyler -> results/checks.md
pytest -q
```

Parametreler: `--window 2000`, `--per-language 24`, `--seed 7`. ABC için: `--abc-per-language 100`, `--abc-seeds 4`, `--accept 0.01`, `--jobs 4`; var olan tabloyu yeniden kullanır, `--rebuild` baştan üretir. Arama için: `--rounds 5`, `--keep 100`, `--children 6`, `--fresh 2`. El yazması için: `--ms-per-class`, `--ms-windows 16`, `--ms-top 20`, `--ms-reseed-top 5`, `--ms-reseeds 6`. Sıra önemli: `all` -> `abc --rebuild` -> `search` -> `manuscripts --rebuild` -> `checks`; üreteç değişince hepsi yeniden koşulur.

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
| `search.py` | Yönlendirilmiş arama: ABC'nin en yakın örneklerinin ayarlarından başlar, önsel sınırları içinde oynatır, sonucu taze örneklerle ölçer. Sonsal dağılım vermez; "bu hipotezin Voynich'ten ayırt edilemeyen bir ayar bölgesi var mı" sorusunu yanıtlar |
| `manuscripts.py` | El yazması düzeyinde karşılaştırma: aday = ayarlar + tohum, tek tablodan 16 pencere, 8'i seçim 8'i doğrulama. İstatistik T (standart hataya bölünmüş ortalama farkı; Voynich'in kendi yarıları için yaklaşık 1), yayılım oranı (iç değişkenlik) ve büyüme profili (yarı başına 16 bin kelimede tür/kelime, hapax/tür, ed1 oranı). Asıl hüküm buradan verilir |
| `checks.py` | Hattın kendi sonuçlarını sınayan deneyler: EVA'laştırma (bilinen anlamsız metni çok harfli yazınca sınıflandırıcı ne diyor) ve homojenlik (tek tablo Voynich kadar değişken metin üretiyor mu) |
| `cli.py`, `fetch.py` | Komut satırı ve indirme |

Ortak veri tipi `Lines = list[list[str]]`: satırlar, kelimeler, her karakter bir glif. Çok harfli glifler Unicode özel kullanım alanındaki tek karaktere eşlenir.

Sınıflar: `plain` (doğal dil, tek alfabeli ikame dahil), `abjad` (seslisiz yazım), `verbose` (harf başına 1-3 sembol), `grille` (Rugg tablosu: önek, gövde, sonek heceleri; sütunların glif kümeleri ayrık ya da örtüşük), `selfcite` (Timm ve Schinner kendinden kopyalama; yeni kelimeler yuva yapısından), `slotcite` (melez: kelimeler grille gibi hece üçlüsü, metin selfcite gibi kopyalayıp bir heceyi değiştirerek ilerler), `slotgram` (çok yuvalı kelime grameri: 3 ila 8 sıralı seçmeli yuva, isteğe bağlı yerel kopyalama).

Yeni süreç eklemek: fonksiyonu `generators.py` içine yaz, ayarları `Knobs.get` ile çek (böylece hem kaydedilir hem dışarıdan sabitlenebilir), sınırlarını `PROCESS_PRIOR` tablosuna yaz, sonunda `lay_out(kelimeler, rng, layout, rec)` çağır, ilgili sözlüğe ekle. `test_priors_cover_what_is_drawn` tablo ile çekimin tutarlılığını denetler.

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

Tarihçe; raporlar git geçmişinde (`c0c69d1`). Buradaki sıralama ("beş görünümde en yakın `grille`") v0.4'te taze örnek ölçütüyle zayıfladı, aşağıya bak. Raporlar: `results/report.md` (sınıflandırıcı) ve `results/abc.md` (ABC, 42800 sentetik örnek, sınıf başına en yakın %1 kabul).

Eklenenler: `abc.py` ve `cli abc`; Zandbergen-Landini transliterasyonu (`zl_basic`, `zl_glyph`); `verbose` için hece hece yazma ve sürekli boşluk ekleme; üreteçlerin çektiği ayarların kaydı.

- **ABC ölçütüyle hiçbir hipotez Voynich'i üretemiyor.** Mesafe birimi Voynich'in kendi pencereleri arası değişkenlik. Voynich öz mesafesi medyan 0.9 ila 1.0, en çok 1.4 ila 1.65. Hiçbir sınıfta, hiçbir görünümde, Voynich'in en uç penceresi kadar yakın tek bir örnek yok (%0.00). En iyi tek örnek: `grille`, v101'de 1.46 (sınır 1.42).
- **Sıralama beş görünümde de aynı yönde:** `grille` en yakın (kabul edilenlerin medyanı 2.07 ila 2.80), beşte dördünde ikinci `verbose` (2.89 ila 3.98), sonra `selfcite`, `plain`, `abjad`.
- **v0.2'deki bir sonuç geri alındı.** v0.2'de `verbose` üreteci kelime sınırlarını neredeyse hep koruyordu ve dil tabanlı sınıflar 0.02'nin altında olasılık alıyordu. `verbose` hece hece yazabilir olunca sınıflandırıcı düz EVA görünümlerinde `verbose` dedi (`eva_basic` 0.61, `zl_basic` 0.75), birleşik glif ve v101 görünümlerinde `grille` (0.46 ila 0.82). ABC'de kabul edilen `verbose` örneklerinin tamamına yakını hece modunda. Ders: bir hipotezin elenmesi, o hipotezin üretecinin dar yazılmış olmasından kaynaklanabilir. Dil tarafı hâlâ eksik, o yüzden hiçbir yönde hüküm yok.
- **Sınıflandırıcının kararı harf tanımına bağlı, okuyana değil.** Takahashi ile Zandbergen-Landini aynı modda aynı sonucu veriyor (`eva_basic` ve `zl_basic` ikisi de `verbose`; `eva_glyph` ve `zl_glyph` ikisi de `grille`). Ayrışma "hangi çizgiler tek harf" kararından geliyor: düz EVA tek glifi birkaç harfle yazdığı için (ch, sh, cth, iin) metin kendiliğinden verbose şifreye benziyor.
- **Düz EVA görünümlerindeki `verbose` kararı yazım biçiminin ürünü (sınandı, `results/checks.md`).** 300 `grille` örneği özgün hâliyle 300/300 `grille` sınıflanıyor. Aynı örneklerde altı glif EVA'daki kalıpla çok harfli yazılınca (iki sık glif C+H ve S+H, dört seyrek glif C+T+H) 291/300 `verbose` sınıflanıyor. `selfcite` etkilenmiyor (293/300 yine `selfcite`). Sonuç: sınıflandırıcının `verbose` sınıfı "altında dil var" demek değil, "semboller sabit gruplar hâlinde geliyor" demek. Düz EVA görünümleri (`eva_basic`, `zl_basic`) "dilin şifresi mi, anlamsız mı" ayrımında kullanılamaz. Bu ayrım için ya birleşik glif görünümleri ya da gruplar çözüldükten sonra altta kalan dizinin dile benzeyip benzemediğini ölçen ayrı bir sınama gerekir.
- **Sınıflandırıcı ile ABC farklı soruya cevap veriyor.** Sınıflandırıcı "beş sınıftan hangisi", ABC "bu sınıf ne kadar yaklaşabiliyor" der. Düz EVA'da sınıflandırıcı `verbose`, ABC `grille` diyor. İkisi tutmadığı sürece sınıf adı bulgu değildir.
- **`grille` neyi tutturamıyor (beş görünümde tekrar edenler):** `wlen_autocorr1` (komşu kelime uzunluk benzerliği üretemiyor, -2.5 ila -3.5 birim), `vocab_ed1_density` (fazla yoğun, +2.2 ila +4.6), `wlen_std` ve `type_len_mean` (kelimeler kısa ve dar), `hapax_ratio` (az).
- **`verbose` neyi tutturamıyor:** `hapax_ratio` (az), `jsd_last` (kelime sonu kısıtı zayıf), `wlen_std` ve `wlen_skew` (kelime uzunluğu fazla yayvan ve çarpık), `wlen_autocorr1`.
- **`selfcite` neyi tutturamıyor:** `h2` (fazla yüksek), `char_double_rate`, `rep_adjacent_exact` (fazla tekrar). Kabul edilen örneklerde geriye bakış uzaklığı önselin üst ucuna kayıyor (5 -> 19 satır): yakın kopyalama Voynich'e uymuyor.
- **Bu ABC'nin sınırı.** Rejection ABC rastgele dener; 32 feature'ı aynı anda tutturan örnek seyrek olduğu için yazıcı katmanı ayarları neredeyse hiç kısıtlanmıyor (kabul edilenlerde `jsd_line_final` 0.02, Voynich 0.11). Yani mesafeler hipotezlerin gerçekte ulaşabileceğinden kötü. Sıradaki iş, en yakın örneklerin çevresinde yeniden arayan ABC (SMC); bunun için üreteçler ayarları dışarıdan alabilmeli.
- **Sınıflandırıcı raporu:** CV 0.977. OOD oranı 1.4 ila 1.6x, yüzdelik 94 ila 98; hiçbir feature aralık dışında değil.

## v0.4 bulguları: yönlendirilmiş arama ve taze örnek ölçütü (2026-11-24, seed 7, pencere 2000)

Tarihçe (`9e9cc52`). Buradaki "karşılaştırma birimi yanlıştı" teşhisi v0.5'te giderildi; pencere düzeyindeki sıralamalar yerine v0.5 tablosu okunur. Raporlar: `results/report.md`, `results/abc.md`, `results/search.md`, `results/checks.md`.

Eklenenler: üreteçler ayarları dışarıdan alabiliyor (`Knobs`, `PROCESS_PRIOR`, `layout_from_params`); `search.py` ve `cli search`; `grille` için hece uzunluğu ve boş hücre payı ayarları; `checks` içine homojenlik deneyi.

- **Taze örnek ölçütüyle hiçbir hipotez Voynich'i üretemiyor.** Arama sonunda kalan 100 ayarın her biriyle 2 taze örnek üretildi. Taze örneklerin medyan mesafesi her sınıfta, her görünümde 2.46 ila 5.80; Voynich öz mesafesi medyan 0.9 ila 1.0, en çok 1.4 ila 1.65. Sınırın içine düşen taze örnek: yalnız `grille`, `eva_glyph` ve `zl_glyph` görünümlerinde 200'de 1.
- **Sıralama görünüme bağlı ve farklar küçük.** `eva_basic`, `eva_glyph`, `zl_basic`, `zl_glyph`: `grille` en yakın (2.46 ila 3.29), hemen ardında `selfcite` (2.55 ila 3.62). v101: `plain` en yakın (2.62), `grille` sonuncu (3.54; `char_double_rate` +7.9 birim). İlke 5 gereği "en yakın hipotez" diye bir bulgu yok.
- **Rejection ABC'deki mesafeler iyimserdi.** `grille` için ABC'de kabul edilenlerin medyanı 2.15 ila 2.76 iken aynı bölgenin taze örnekleri 2.46 ila 3.54. Kabul edilen örnekler kısmen şansla seçilmişti. Arama tur içi medyanı düşürüyor (ör. `eva_basic` `grille` 2.92 -> 2.57) ama taze örnekte bu kazanç kalmıyor.
- **Neden: örnekler arası farkı ayarlar değil tablo belirliyor (`results/checks.md`, homojenlik).** Aynı tablo ve ayarla üretilen 8 pencerenin kendi ortalamasına uzaklığı `grille` için 0.26 ila 0.32, farklı tabloların ortalamaları arası uzaklık 3.8 ila 6.0. Yani her örnekte tablo baştan çekildiği sürece ayar araması gürültüde kayboluyor.
- **Tek bir `grille` tablosu Voynich'ten çok daha tekdüze metin üretiyor.** Voynich'in iç değişkenliği 0.92 ila 0.95, tek tablonun 0.26 ila 0.32. `selfcite` ise fazla değişken (1.26 ila 1.67). Voynich'in bölümler arası farkını (Currier A ve B, çizim bölümleri) hiçbir üreteç taklit etmiyor; üreteçler durağan.
- **Sonuç: karşılaştırma birimi yanlıştı.** Şimdiye kadar "bir sentetik örnek = yeni bir el yazması" ile "bir Voynich penceresi = aynı el yazmasının parçası" kıyaslandı. Doğru kıyas el yazması düzeyinde: tek tablo ve tek ayarla uzun metin üret, pencerelere böl, hem ortalamayı hem iç değişkenliği Voynich'inkiyle karşılaştır; tabloyu bir yarıda seç, öbür yarıda doğrula. Sıradaki iş bu (yol haritası 2).
- **Sınıflandırıcı raporu:** beş görünümde de `grille` (0.66 ila 0.95), OOD oranı 1.1 ila 1.4x, yüzdelik 68 ila 93. İlk kez hem dağılım içi hem görünümler arası tutarlı. Yine de bulgu sayılmıyor (ilke 7): bu karar yalnız `grille` üretecine hece uzunluğu ayarı eklenince oluştu ve taze örnek ölçütü geçilmedi.
- **EVA'laştırma sınaması güncellendi.** Yeni `grille` ile 300 örneğin 299'u özgün hâliyle `grille`; EVA'laştırılınca 114'ü `verbose` oluyor (v0.3'te 291 idi). Etki küçüldü ama sürüyor; düz EVA görünümleri hakkındaki uyarı geçerli.

## v0.5 bulguları: el yazması düzeyinde karşılaştırma (2026-11-24, seed 7, pencere 2000)

Tarihçe (`143fd50`); beş hipotezli tablo. Sonundaki melez hipotezi v0.6'da sınandı ve tutmadı. Rapor: `results/manuscripts.md` (sınıf başına 2000 el yazması, her biri 16 pencere; sınıf başına seçim yarısına göre en yakın 20 aday, sayılar doğrulama yarısından).

- **Ölçü artık kararlı.** Seçim yarısı ile doğrulama yarısı aynı değeri veriyor (ör. `eva_basic` `grille` 6.5 ve 6.5). Pencere düzeyindeki seçim iyimserliği burada yok: bir tablonun profili kendi metni boyunca sabit.
- **Referans.** Voynich'in kendi yarıları birbirine karşı T: rastgele bölmede medyan 0.9, %95'lik 1.5; ardışık bölmede (ilk yarı ile son yarı) 1.4 ila 1.7.
- **Hiçbir hipotez Voynich'in ortalama profilini üretemiyor.** Seçilen adayların doğrulama T medyanı: `grille` 5.1 ila 6.5, `verbose` 6.4 ila 8.5, `selfcite` 7.4 ila 10.4, `plain` 7.3 ila 12.2, `abjad` 7.6 ila 14.3. En iyi tek aday 4.3 (`grille`, `eva_glyph`). Referansın %95'liğine giren aday yok.
- **Sıralama beş görünümde de aynı: en yakın `grille`.** İkinci, dört görünümde `verbose`; v101'de `plain` ile `verbose` başa baş (7.3 ve 7.5). Bu, oturumun doğrulama yarısında ölçülmüş ve görünümler arası tutarlı ilk sıralamasıdır. Anlamı sınırlı: "beş hipotezden en az uzak olan", "doğru olan" değil; fark 5'e 7, referans 1.5.
- **Ayarlar bilgi taşıyor ama tablo da önemli.** Seçilen ayarlar yeni tohumla (yeni tablo) yeniden üretilince `grille` 6.9 ila 8.6'ya çıkıyor. Yani seçilen adayların iyi oluşunun bir kısmı ayar bölgesinden, bir kısmı o tablonun kendisinden.
- **İç değişkenlik (yayılım oranı, Voynich = 1):** `grille` 0.15 ila 0.17, `verbose` 0.32 ila 0.41, `plain` 0.38 ila 0.50, `abjad` 0.47 ila 0.60, `selfcite` 0.74 ila 0.94. Voynich, 32 bin kelimelik doğal dil metninden (İncil) yaklaşık iki kat, tek tablodan altı kat daha değişken. Kaynağı sınanmadı; Currier A ve B ile çizim bölümleri aday.
- **`grille` neyi tutturamıyor (beş görünümde tekrar eden, standart hata biriminde):** `wlen_autocorr1` (-6 ila -7: komşu kelimeler uzunlukça benzemiyor), `hapax_ratio` (-6 ila -8: tek geçen kelime az), `vocab_ed1_density` (+5 ila +8: dağarcık fazla sıkı), `rep_adjacent_ed1` (-5 ila -6: komşuda "bir harf farklı" kelime az). Dördü de aynı şeyi söylüyor: tablo kelimeleri birbirinden bağımsız çekiyor, Voynich'te ise komşu kelimeler birbirine benziyor ve sürekli yeni çeşitleme üretiliyor.
- **`selfcite` tam tersini tutturuyor ve başka yerde kalıyor:** iç değişkenlik ve komşu benzerliği yakın, ama `h2` çok yüksek (+11 ila +15), `char_double_rate` ve `rep_adjacent_exact` fazla, `hapax_ratio` az.
- **Çıkarım (hipotez, sınanmadı):** Voynich, yuva yapılı kelime (grille'in iyi yaptığı) ile yerel kopyalayıp değiştirme (selfcite'ın iyi yaptığı) birleşimine benziyor. Sıradaki üreteç bu melez; ayrıca dil tarafında aynı iki özelliği (komşu benzerliği, bol hapax) üretebilecek bir hipotez de yazılmalı ki kıyas adil olsun (VL-001).

## v0.6 bulguları: melez üreteç sınandı, öngörü tutmadı (2026-11-24, seed 7, pencere 2000)

Tarihçe (`a4a6dd7`). Sonundaki çok yuvalı gramer hipotezi v0.7'de sınandı ve tutmadı. Raporlar: `results/manuscripts.md` (asıl hüküm; altı sınıf, sınıf başına 2000 el yazması), `results/report.md`, `results/abc.md`, `results/search.md`, `results/checks.md`.

Eklenen: `slotcite` sınıfı. Hipotez sınanmadan önce v0.5 bölümüne yazılmıştı; ölçüt, el yazması düzeyinde doğrulama T'sinin `grille`'den belirgin düşük çıkmasıydı.

- **Öngörü tutmadı.** Doğrulama T medyanı: `slotcite` 5.2 ila 6.9, `grille` 5.1 ila 6.6. Beş görünümün hiçbirinde `slotcite` daha iyi değil (v101'de belirgin kötü: 6.9 ve 6.0). En iyi tek aday da benzer (4.6 ila 5.4; `grille` 4.3 ila 5.2). Referans hâlâ 1.5.
- **Melezin düzelttiği:** iç değişkenlik (yayılım oranı 0.36 ila 0.44; `grille` 0.15; homojenlik sınamasında iç 0.68 ila 0.85, Voynich 0.92 ila 0.95) ve komşu kelime uzunluk benzerliği (`wlen_autocorr1` dört görünümde artık ilk yedi açık arasında değil).
- **Melezin bozduğu:** `rep_adjacent_exact` (+5 ila +11: kopyalama Voynich'te olmayan kadar aynen tekrar üretiyor). Seçilen adaylarda aynen kopyalama olasılığı önselin alt ucuna kayıyor (medyan 0.20, önsel 0.1 ila 0.7), yani veri bu mekanizmayı istemiyor.
- **Üç anlamsız metin üretecinde de kalan ortak açık:** `hapax_ratio` az (-6 ila -10) ve `vocab_ed1_density` fazla (+5 ila +8). Üç yuvalı, az sayıda sık heceden kurulan dağarcık kapalı kalıyor: Voynich'te tek geçen kelime çok daha fazla, ama dağarcık doğal dildeki kadar da dağınık değil. Doğal dil sınıflarında durum ters (hapax tutuyor, `vocab_ed1_density` çok düşük).
- **Sıralama (doğrulama T):** `grille` ve `slotcite` başa baş (5.1 ila 6.9), sonra `verbose` (6.6 ila 8.9), `selfcite`, `plain`, `abjad`. Beş görünümde aynı yönde.
- **Sınıflandırıcı raporu (yardımcı):** CV 0.952; düz EVA görünümlerinde `slotcite` (0.59, 0.60), diğerlerinde `grille` (0.56 ila 0.74); OOD yüzdeliği 52 ila 86. İlke 7 gereği başlık değil.
- **Yeni hipotez (sınanmadı, ölçüt aynı):** açık, yuva sayısından geliyor. Üç yerine dört ila altı seçmeli yuvadan kurulan kelime (literatürdeki çok yuvalı Voynich kelime gramerleri) hem daha çok tek geçen kelime üretir hem dağarcığı "bir harf farklı" komşularla dolu tutar. Öngörü: çok yuvalı `grille`, doğrulama T'sinde 5.1'in belirgin altına iner ve `hapax_ratio` ile `vocab_ed1_density` açıkları birlikte küçülür. İnmezse açık yuva sayısından değil, başka yerden geliyor demektir.

## v0.7 bulguları: çok yuvalı gramer sınandı, öngörü tutmadı (2026-11-24, seed 7, pencere 2000)

Tarihçe (`321bae9`). Buradaki T sıralaması geçerli ama tek başına okunmamalı; v0.8 büyüme profilini ekledi ve sıralamanın anlamını değiştirdi. Raporlar: `results/manuscripts.md` (asıl hüküm; yedi sınıf, sınıf başına 2000 el yazması) ve yardımcı raporlar.

Eklenen: `slotgram` sınıfı; kopyalama döngüsü `_cite_text` yardımcısına taşındı (`slotcite` çıktısı bayt bayt aynı kaldı). Tohumlar artık sınıf ve görünüm adına bağlı (`_stable_id`), bu yüzden v0.6'ya göre bütün sayılar birkaç ondalık oynadı; bundan sonra yeni sınıf eklemek eskilerin sayılarını değiştirmez.

- **Öngörü tutmadı.** Doğrulama T medyanı: `slotgram` 5.5 ila 7.4, `grille` 5.2 ila 6.7. Hiçbir görünümde `slotgram` daha iyi değil. Seçilen adaylarda yuva sayısı önselden kaymadı (medyan 5, önsel 3 ila 8).
- **Açık küçülmedi, büyüdü.** `vocab_ed1_density` sapması +6 ila +10 (grille'de +5 ila +8); `hapax_ratio` hâlâ az; `zipf_slope` fazla dik. Yuva sayısını artırmak dağarcığı daha da sıkı yaptı. Demek ki açık yuva sayısından gelmiyor.
- **Yerel kopyalama yine istenmedi.** Seçilen `slotgram` adaylarında kopyalama olasılığının medyanı 0 (kapalı).
- **Arka arkaya iki öngörü tutmadı (melez, çok yuva).** İkisi de "hangi mekanizma eksik" sorusuna feature tablosuna bakarak verilmiş cevaplardı. Ders: açığın kaynağı üreteç yazmadan önce doğrudan Voynich verisinde ölçülmeli (dağarcık büyüme eğrisi, komşuluk yapısı), ve aday mekanizma tam zincir koşulmadan önce yalnız el yazması adımıyla ucuza sınanmalı.
- **Sıralama (doğrulama T):** `grille` 5.2 ila 6.7; `slotcite` 5.6 ila 7.1; `slotgram` 5.5 ila 7.4; `verbose` 6.6 ila 8.9; `selfcite` 7.0 ila 10.5; `plain` 7.3 ila 12.8; `abjad` 7.4 ila 14.8. Beş görünümde aynı yönde. Referans 1.5.
- **Sınıflandırıcı raporu (yardımcı):** CV 0.920; kararı üç anlamsız metin sınıfı arasında bölünüyor; OOD yüzdeliği 36 ila 81.

## v0.8 bulguları: büyüme profili (2026-11-24, seed 7, pencere 2000)

Tarihçe (`00d487a`). Sonundaki bileşim hipotezi v0.9'da sınandı ve tutmadı. Rapor: `results/manuscripts.md` bölüm 5 ve 6. Üreteçler değişmedi; T değerleri v0.7 ile aynı (doğrulandı), yalnız ölçüme büyüme profili eklendi.

- **Voynich'in dağarcığı doymuyor.** 16 bin kelimelik yarıda: tür/kelime 0.25 ila 0.30, hapax/tür 0.68 ila 0.72, "bir harf farklı" komşusu olan tür oranı 0.86 ila 0.89. İki yarı birbirini 0.03 içinde tutuyor. 32 bin kelimede 6700 ila 7700 farklı kelime var ve hapax oranı 500 kelimeden 32 bin kelimeye yalnız 0.79'dan 0.68'e düşüyor.
- **Tablo üreteçlerinin dağarcığı doyuyor.** `grille` önselinde tür/kelime medyanı 0.10, hapax 0.37, ed1 0.99. 2000 kelimelik pencerede Voynich kadar çeşitli görünen tablo, 16 bin kelimede kendini tekrar ediyor. Pencere düzeyi feature'lar bunu göremiyordu.
- **Pencere profiline göre seçilen adaylar büyüme profiline uymuyor.** T'ye göre en iyi 20 `grille` adayında tür/kelime 0.12 ila 0.18, hapax 0.28 ila 0.52, ed1 0.97 ila 0.99. Yani v0.5 ila v0.7'deki "en yakın `grille`" sıralaması, 2000 kelimelik pencerenin göremediği bir uyumsuzluğu saklıyordu.
- **Büyüme profiline en çok uyan sınıf seslisiz yazılmış doğal dil (`abjad`).** 2000 el yazmasından üç ölçüde de 0.05 içinde kalanların sayısı: `abjad` 105 ila 335, `verbose` 11 ila 40, `slotgram` 29 ila 35, `slotcite` 16 ila 36, `selfcite` 3 ila 18, `grille` 2 ila 15, `plain` 2 ila 8. Düz doğal dilde (`plain`) tür/kelime ve hapax tutuyor ama ed1 oranı düşük (medyan 0.63); sesliler atılınca ed1 Voynich düzeyine çıkıyor (0.86). Ayrı ölçüm: 22 dilin düz metninde 32 bin kelimede ed1 oranı 0.41 ila 0.62, yalnız zaten seslisiz yazılan İbranice (0.89) ve Arapça (0.78) yüksek.
- **Ama büyümeye uyan `abjad` el yazmalarının pencere profili çok uzak.** Uyanların doğrulama T'si medyan 15 ila 28, en iyi 7.2 ila 13.6. Seslisiz yazımda kelimeler Voynich'e göre fazla kısa ve harf dizilişi fazla öngörülemez (`h2` yüksek).
- **İki ölçütü birlikte sağlayan hipotez yok.** Büyümeye uyanlar içinde en iyi T: `slotcite` 5.1 (`zl_glyph`), `slotgram` 5.5 ila 9.8, `grille` 6.5 ila 22.7, `verbose` 7.2 ila 9.9, `abjad` 7.2 ila 13.6, `plain` 7.3 ila 11.8. Referans 1.5. İki ölçüt birbirine karşı çalışıyor: pencere profilini tutturan aday dağarcığı kapatıyor, dağarcığı açan aday pencere profilinden uzaklaşıyor.
- **Sıralama artık net değil.** Ortak ölçütte `grille` önde değil; yuva gramerleri, `verbose` ve `abjad` 5 ila 10 bandında iç içe. "Anlamsız metin üreteçleri dil hipotezlerinden yakın" cümlesi yalnız pencere profili için doğruydu.
- **Yeni hipotez (sınanmadı):** `abjad` büyüme profilini, `verbose` kelime uzunluğunu ve düşük `h2`'yi getiriyor. İkisinin bileşimi (önce sesliler atılır, sonra her harf bir ila üç gliflik gruba açılır) iki ölçütü birlikte tutturabilir. Öngörü: bileşimde büyümeye uyan el yazması sayısı `verbose`'un 11 ila 40'ının belirgin üstüne çıkar ve uyanlar içinde en iyi T, beş görünümün çoğunda 5'in altına iner. Risk: bir harf farkı çok glifli koda dönüşünce ed1 oranı düşebilir; düşerse öngörü tutmaz.

## v0.9 bulguları: seslisiz yazım + şifre bileşimi sınandı, öngörü tutmadı (2026-11-24, seed 7, pencere 2000)

Güncel durum budur. Rapor: `results/manuscripts.md`.

Eklenen: `verbose` için iki ayar, `p_drop_vowels` (şifrelemeden önce sesliler atılır) ve `p_short` (kodların kısalığı). Ayarlar duruyor, çünkü dil tarafının hipotez uzayını genişletiyorlar.

- **Öngörü tutmadı, v0.8'de yazılan risk gerçekleşti.** Büyümeye uyan `verbose` el yazması sayısı artmadı, azaldı (11 ila 40'tan 4 ila 24'e); uyanlar içinde en iyi T de kötüleşti (7.2 ila 9.9'dan 6.8 ila 13.3'e). Seslisi atılmış `verbose` el yazmalarında ed1 oranının medyanı 0.72 (`abjad`'da 0.86, Voynich'te 0.86 ila 0.89): bir harflik fark çok glifli koda dönüşünce "bir harf farklı" komşuluk kayboluyor. T'ye göre seçilen `verbose` adaylarının hiçbiri seslileri atmıyor.
- **Arka arkaya üç öngörü tutmadı (melez, çok yuva, bileşim).** Üçü de var olan mekanizmaları yeniden birleştiriyordu. Ortak ders: iki ölçüt aynı anda ancak şu üçü birlikte sağlanırsa tutar ve şu ana kadarki hiçbir üreteçte üçü birden yok: (1) açık dağarcık (doğal dil ya da sınırsız çeşitleme), (2) sıkı kelime biçimi (yuva yapısı), (3) kelime türleri arasında yoğun "bir harf farklı" komşuluk. Tablo (2) ve (3)'ü verir, (1)'i vermez. Doğal dil (1)'i verir, (2)'yi vermez. Seslisiz yazım (1) ve (3)'ü verir, (2)'yi vermez. Harf harf şifre (2)'yi verir, (3)'ü bozar.
- **Ortak ölçütte sıralama (büyümeye uyanlar içinde en iyi T):** `slotcite` 5.1 ila 12.5, `slotgram` 5.5 ila 9.8, `grille` 6.5 ila 22.7, `verbose` 6.8 ila 13.3, `abjad` 7.2 ila 13.6, `plain` 7.3 ila 11.9, `selfcite` 11.8 ila 30.4. Referans 1.5. Net bir kazanan yok.
- **Yeni hipotez (sınanmadı):** kelime kelime kodlama (kod defteri). Düz metnin her kelime türü, yuva yapılı bir kod kelimesine bire bir eşlenir; kod, kelimenin sıra numarasının yuvalara "basamak" olarak yazılmasıdır. Bu, yukarıdaki üç koşulu yapısı gereği sağlar: dağarcık büyümesi doğal dilinkiyle aynıdır (1), her kod yuva yapısına uyar (2), kod uzayı sık dolu olduğu için komşuluk yoğundur (3). Sıra numarası ilk geçiş sırasına göre verilirse, yakında ilk kez geçen kelimeler ardışık numara alır ve komşu kelimeler birbirine benzer. Öngörü: `codebook` sınıfında büyümeye uyan el yazması sayısı yüzlerle ölçülür ve uyanlar içinde en iyi T, beş görünümün çoğunda 5'in altına iner. İnmezse, üç koşul gerekli ama yeterli değil demektir.

## Yol haritası (öncelik sırasıyla)

1. **Üreteç sadakati.** Asıl kaldıraç burada.
   - ~~Satır farkındalığı~~: yapıldı (v0.1, ortak yazıcı katmanı). Paragraf düzeyi feature yok; paragraf başı `p`/`t` etkisi yalnız `jsd_line_initial` içinden dolaylı görünüyor.
   - ~~Kelime içi konum grameri~~: yapıldı (v0.2). Üç yuvayla sınırlı; literatürdeki çok yuvalı kelime gramerleri denenmedi.
   - Verbose şifreye konuma duyarlı kod tabloları.
   - `selfcite` parametrelerini Timm ve Schinner 2019 makalesindeki değerlere çek.
   - Yeni sınıflar: homofonik şifre, hece yazısı, kısaltmalı Latince (ortaçağ abbreviatura).
2. **ABC ile parametre kestirimi.** Rejection ABC (v0.3), yönlendirilmiş arama (v0.4) ve el yazması düzeyinde karşılaştırma (v0.5) yapıldı. Melez üreteç (v0.6) ve çok yuvalı gramer (v0.7) sınandı, ikisi de tutmadı. Büyüme profili ölçüldü (v0.8); `abjad` ile `verbose` bileşimi sınandı, tutmadı (v0.9). **Sıradaki:** (a) kelime kelime kodlama (`codebook`, v0.9'daki hipotez); (b) dil tarafında komşu benzerliği ve bol hapax üretebilecek hipotez; (c) durağan olmayan üreteçler (bölümden bölüme kayan ayar ya da tablo), Voynich tarafında bölüm sınırları ZL sayfa değişkenlerinden; (d) el yazması düzeyinde yönlendirilmiş arama.
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
