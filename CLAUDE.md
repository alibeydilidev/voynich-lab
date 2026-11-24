# voynich-lab

Voynich el yazmasına (Beinecke MS 408) "ne yazıyor" diye değil, "bunu nasıl bir süreç üretti" diye soran hat. Yöntem simülasyon tabanlı çıkarım: aday üretim süreçlerini simüle et, sembol adından bağımsız feature çıkar, XGBoost ile süreç sınıflandırıcısı eğit, Voynich'i içine at.

Bu dosya projenin devir notudur. Kararların gerekçesi burada, kodu değiştirmeden önce oku.

## Amaç ve hedef merdiveni (Ali kararı, 2026-11-23; yeniden çerçeveleme 2026-11-24)

**Birincil amaç (Ali kararı, 2026-11-24):** Voynich metninin ne tür bir süreçten çıktığını ve bir doğal dili doğrudan yazıp yazmadığını, başkasının tek komutla yeniden üretebileceği ölçümlerle göstermek. Dışarıya kurulacak cümle "Claude çözdü" değil, "Claude şunu ölçtü" biçimindedir.

İlk amaç (2026-11-23) kanıtlanabilir tercümeydi. Ali bunu v0.14 hükmü üzerine değiştirdi. O hükmün bir cümlesi ("B doğruysa hiçbir tercüme sınanamaz") v0.15'te düzeltildi: anahtarla geri okunabilen bir şifre ihtimali istatistikle elenemiyor ve böyle bir çözüm ilke olarak sınanabilir. Bu yüzden tercüme "ulaşılamaz" diye kapatılmış değildir; üçüncü basamak olarak, çözme kapısının arkasında durur. Tercüme sözü verilmez.

Yazıya dökme (Ali kararı, 2026-11-24): önce literatür okunur (VL-013). Yeni bir ölçüm varsa o yazılır; yoksa var olan bulguların bağımsız doğrulaması olarak yazılır. Okunmamış kaynak varken "ilk kez" denmez. Yayın ve duyuru kararı her seferinde Ali'nindir.

Basamaklar; her biri kendi başına başarı sayılır:

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
8. **Zincirden önce ön sınama.** Yeni bir mekanizma üreteç sınıfı olarak yazılmadan ve zincir koşulmadan önce `probe` ile ölçülür (Python'dan `probe.run(make)`, var olan sınıflar için `cli probe`). Büyüme bandına hiçbir el yazması girmiyorsa sınıf yazılmaz, zincir koşulmaz; sonuç yine de CLAUDE.md'ye yazılır. Gerekçe: 2026-11-24'te dört hipotez arka arkaya yarım saatlik zincirlerle sınandı ve dördü de saniyede görülebilecek tek bir ölçü yüzünden tutmadı.
9. **Eleme ve "sınanamaz" cümlesinden önce bilinen cevaplı denetim (Ali kararı, 2026-11-24).** "Şu ihtimal elendi" ya da "şu sınanamaz" cümlesi, cevabı bilinen bir denetim metni aynı ölçümden geçirilmeden yazılmaz ve Ali'ye söylenmez. Denetim metni, elenen ihtimalin gerçek bir örneği olmalıdır (ör. içinde dil olduğu bilinen şifreli metin); yeri `checks` içindeki denetim deneyidir. Uygun denetim metni yoksa cümle "elendi" diye değil, "şu örneklerde görülmedi" diye kurulur. Gerekçe: erken hüküm iki kez geri alındı (v0.11 "harf harf şifre elenir", v0.14 "B doğruysa hiçbir tercüme sınanamaz"); ikincisi Ali'nin amaç kararına dayanak olmuştu.

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
python -m voynich_lab.cli checks    # hattın kendi sonuçlarını sınayan deneyler -> results/checks.md, ~1 dk
python -m voynich_lab.cli probe --label abjad --probe-n 12   # ön sınama, saniyeler; --set anahtar=değer ile ayar sabitlenir
pytest -q
```

Parametreler: `--window 2000`, `--per-language 24`, `--seed 7`. ABC için: `--abc-per-language 100`, `--abc-seeds 4`, `--accept 0.01`, `--jobs 4`; var olan tabloyu yeniden kullanır, `--rebuild` baştan üretir. Arama için: `--rounds 5`, `--keep 100`, `--children 6`, `--fresh 2`. El yazması için: `--ms-per-class`, `--ms-windows 16`, `--ms-top 20`, `--ms-reseed-top 5`, `--ms-reseeds 6`. Sıra önemli: `all` -> `abc --rebuild` -> `search` -> `manuscripts --rebuild` -> `checks`; üreteç değişince hepsi yeniden koşulur.

## Mimari

| Dosya | Görev |
|---|---|
| `transliteration.py` | Takahashi EVA, Claston v101 ve Zandbergen-Landini (IVTFF) ayrıştırıcıları, beş görünüm (`eva_basic`, `eva_glyph`, `v101`, `zl_basic`, `zl_glyph`), etiketsiz düz EVA okuyucu (`load_eva_plain`, denetim metinleri için), pencereleme |
| `corpus.py` | 22 dilde paralel İncil, yazıya göre normalizasyon; 15. yüzyıl dönem metinleri (`load_period`) |
| `generators.py` | Üretim süreçleri. `LANGUAGE_PROCESSES` gerçek metni dönüştürür, `GIBBERISH_PROCESSES` sıfırdan üretir. Hepsinin üstünde ortak yazıcı katmanı (`Layout`, `lay_out`, `finish`): nadir harf çeşitlemeleri, kelime başı ve sonu için özel harf biçimleri, satırı genişliğe göre doldurma, paragraf, satır başı, satır sonu ve paragraf başı alışkanlıkları |
| `features.py` | 33 feature: entropi, kelime uzunluğu, dağarcık, tekrar, kelime içi konum, satır konumu, kelimeler arası uç bağı (`edge_mi`, v0.18) |
| `dataset.py` | Sentetik korpus fabrikası: (dil penceresi x süreç) -> satır. Her satır üreten ayarları da taşır (`p_` süreç, `l_` yazıcı katmanı) |
| `model.py` | XGBoost, `GroupKFold` |
| `analyze.py` | Voynich çıkarımı, SHAP katkıları (`pred_contribs`), Mahalanobis tabanlı OOD |
| `abc.py` | Rejection ABC: her sınıf Voynich'e en fazla ne kadar yaklaşıyor, neyi tutturamıyor, hangi ayarlarla. Mesafe birimi Voynich'in kendi pencereleri arası değişkenlik |
| `search.py` | Yönlendirilmiş arama: ABC'nin en yakın örneklerinin ayarlarından başlar, önsel sınırları içinde oynatır, sonucu taze örneklerle ölçer. Sonsal dağılım vermez; "bu hipotezin Voynich'ten ayırt edilemeyen bir ayar bölgesi var mı" sorusunu yanıtlar |
| `manuscripts.py` | El yazması düzeyinde karşılaştırma: aday = ayarlar + tohum, tek tablodan 16 pencere, 8'i seçim 8'i doğrulama. İstatistik T (standart hataya bölünmüş ortalama farkı; Voynich'in kendi yarıları için yaklaşık 1), yayılım oranı (iç değişkenlik) ve büyüme profili (yarı başına 16 bin kelimede tür/kelime, hapax/tür, ed1 oranı). Asıl hüküm buradan verilir |
| `checks.py` | Hattın kendi sonuçlarını sınayan deneyler: EVA'laştırma (bilinen anlamsız metni çok harfli yazınca sınıflandırıcı ne diyor), homojenlik (tek tablo Voynich kadar değişken metin üretiyor mu) sözlük sınaması (kelimeler sınırlı bir sözlükten mi geliyor), sıra sınaması (kelimelerin sırası görülmemiş metinde bilgi taşıyor mu) bozulma taraması (gerçek dil hangi bozulma altında Voynich gibi görünür) ve denetim deneyi (yayımlanmış Naibbe şifresiyle yazılmış gerçek Latince, şifreli ve anahtarla çözülmüş hâliyle, aynı ölçümlerde nasıl görünüyor) ve kelime ucu deneyi (bir kelimenin son glifi sonrakinin ilk glifini ne kadar öngörüyor). Son beşi üretece ve önsele dayanmaz |
| `probe.py` | Ön sınama (bekçi): bir mekanizmayı birkaç el yazmasında saniyeler içinde ölçer (büyüme ölçüleri ve seçilmiş pencere feature'ları), Voynich ile yan yana koyar. Eleme aracıdır, hüküm aracı değildir |
| `cli.py`, `fetch.py` | Komut satırı ve indirme. `fetch` dönem metinlerini de indirir; Wikisource hız sınırı koyduğu için istekler arası 4 sn bekler ve 429 gelirse söylenen süre kadar bekleyip yeniden dener (ilk indirme ~3 dk) |

Ortak veri tipi `Lines = list[list[str]]`: satırlar, kelimeler, her karakter bir glif. Çok harfli glifler Unicode özel kullanım alanındaki tek karaktere eşlenir.

Sınıflar: `plain` (doğal dil, tek alfabeli ikame dahil), `abjad` (seslisiz yazım), `verbose` (harf başına 1-3 sembol), `grille` (Rugg tablosu: önek, gövde, sonek heceleri; sütunların glif kümeleri ayrık ya da örtüşük), `selfcite` (Timm ve Schinner kendinden kopyalama; yeni kelimeler yuva yapısından), `slotcite` (melez: kelimeler grille gibi hece üçlüsü, metin selfcite gibi kopyalayıp bir heceyi değiştirerek ilerler), `slotgram` (çok yuvalı kelime grameri: 3 ila 8 sıralı seçmeli yuva, isteğe bağlı yerel kopyalama), `codebook` (kelime kelime kodlama: her kelime türü, sıra numarasının yuvalara basamak olarak yazıldığı tek bir kod kelimesi), `automaton` (rastgele kurulmuş katmanlı glif otomatı: her kelime gliften glife bir yürüyüş, sözlük yok; isteğe bağlı olarak kelimenin ilk glifi önceki kelimenin son glifine bağlanır).

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

Tarihçe (`ba025a9`). Sonundaki kod defteri hipotezi v0.10'da sınandı ve tutmadı. Rapor: `results/manuscripts.md`.

Eklenen: `verbose` için iki ayar, `p_drop_vowels` (şifrelemeden önce sesliler atılır) ve `p_short` (kodların kısalığı). Ayarlar duruyor, çünkü dil tarafının hipotez uzayını genişletiyorlar.

- **Öngörü tutmadı, v0.8'de yazılan risk gerçekleşti.** Büyümeye uyan `verbose` el yazması sayısı artmadı, azaldı (11 ila 40'tan 4 ila 24'e); uyanlar içinde en iyi T de kötüleşti (7.2 ila 9.9'dan 6.8 ila 13.3'e). Seslisi atılmış `verbose` el yazmalarında ed1 oranının medyanı 0.72 (`abjad`'da 0.86, Voynich'te 0.86 ila 0.89): bir harflik fark çok glifli koda dönüşünce "bir harf farklı" komşuluk kayboluyor. T'ye göre seçilen `verbose` adaylarının hiçbiri seslileri atmıyor.
- **Arka arkaya üç öngörü tutmadı (melez, çok yuva, bileşim).** Üçü de var olan mekanizmaları yeniden birleştiriyordu. Ortak ders: iki ölçüt aynı anda ancak şu üçü birlikte sağlanırsa tutar ve şu ana kadarki hiçbir üreteçte üçü birden yok: (1) açık dağarcık (doğal dil ya da sınırsız çeşitleme), (2) sıkı kelime biçimi (yuva yapısı), (3) kelime türleri arasında yoğun "bir harf farklı" komşuluk. Tablo (2) ve (3)'ü verir, (1)'i vermez. Doğal dil (1)'i verir, (2)'yi vermez. Seslisiz yazım (1) ve (3)'ü verir, (2)'yi vermez. Harf harf şifre (2)'yi verir, (3)'ü bozar.
- **Ortak ölçütte sıralama (büyümeye uyanlar içinde en iyi T):** `slotcite` 5.1 ila 12.5, `slotgram` 5.5 ila 9.8, `grille` 6.5 ila 22.7, `verbose` 6.8 ila 13.3, `abjad` 7.2 ila 13.6, `plain` 7.3 ila 11.9, `selfcite` 11.8 ila 30.4. Referans 1.5. Net bir kazanan yok.
- **Yeni hipotez (sınanmadı):** kelime kelime kodlama (kod defteri). Düz metnin her kelime türü, yuva yapılı bir kod kelimesine bire bir eşlenir; kod, kelimenin sıra numarasının yuvalara "basamak" olarak yazılmasıdır. Bu, yukarıdaki üç koşulu yapısı gereği sağlar: dağarcık büyümesi doğal dilinkiyle aynıdır (1), her kod yuva yapısına uyar (2), kod uzayı sık dolu olduğu için komşuluk yoğundur (3). Sıra numarası ilk geçiş sırasına göre verilirse, yakında ilk kez geçen kelimeler ardışık numara alır ve komşu kelimeler birbirine benzer. Öngörü: `codebook` sınıfında büyümeye uyan el yazması sayısı yüzlerle ölçülür ve uyanlar içinde en iyi T, beş görünümün çoğunda 5'in altına iner. İnmezse, üç koşul gerekli ama yeterli değil demektir.

## v0.10 bulguları: kod defteri sınandı, öngörü tutmadı (2026-11-24, seed 7, pencere 2000)

Tarihçe (`9b92a97`). El yazması tablosu ve sıralamalar hâlâ geçerli (üreteçler v0.11'de değişmedi). Sonundaki aday v0.11'de ön sınamada elendi. Rapor: `results/manuscripts.md` (sekiz sınıf, sınıf başına 2000 el yazması).

Eklenen: `codebook` sınıfı (dil tabanlı).

- **Öngörü tutmadı.** 2000 `codebook` el yazmasından büyüme profiline uyan yok (beş görünümde de 0). Tür/kelime ve hapax tutuyor (önsel medyanı 0.25 ve 0.63; Voynich 0.25 ila 0.30 ve 0.68 ila 0.72), ama ed1 oranı 0.99 (Voynich 0.86 ila 0.89). Numara sırasıyla dizilen kodlar kod uzayını boşluksuz dolduruyor; neredeyse her kelimenin "bir harf farklı" komşusu var. Numaranın neye göre verildiği, boş basamak ve yuva sayısı bunu değiştirmiyor (hepsinde 0.99 ila 1.00).
- **Pencere profili de uzak.** Doğrulama T medyanı 7.3 ila 9.4 (`grille` 5.2 ila 6.7). En büyük açık kelime uzunluğunun yayılımı (`wlen_std` -10 ila -27): kodlar neredeyse eşit uzunlukta.
- **v0.9'daki üç koşul yanlış kurulmuştu.** "Yoğun komşuluk" demiştim; doğrusu "yoğun ama doymamış komşuluk". Voynich'in ed1 oranı (0.86 ila 0.89) iki ucun arasında dar bir bantta: tablo ve kod defteri 0.97 ila 1.00, düz doğal dil 0.41 ila 0.62. Bu banda denenen sekiz sınıftan yalnız seslisiz yazılmış doğal dil (`abjad`, önsel medyanı 0.86) ve zaten seslisiz yazılan diller (İbranice 0.89) kendiliğinden düşüyor.
- **Arka arkaya dört öngörü tutmadı** (melez, çok yuva, bileşim, kod defteri). Dördü de bir zincir koşusuna (yaklaşık 30 dakika) mal oldu ve dördünde de sonucu belirleyen şey tek bir büyüme ölçüsüydü. Ders (v0.7'deki dersin sertleşmiş hâli): yeni bir mekanizma, üreteç sınıfı olarak yazılıp zincire sokulmadan önce, üç büyüme ölçüsünü ve birkaç pencere feature'ını tek el yazmasında, saniyeler içinde ölçen bir ön sınamadan geçmeli. Ön sınamada bandı tutturamayan mekanizma için zincir koşulmaz.
- **Ortak ölçütte sıralama değişmedi** (büyümeye uyanlar içinde en iyi T): `slotcite` 5.1 ila 12.6, `slotgram` 5.5 ila 9.8, `grille` 6.5 ila 22.9, `verbose` 6.8 ila 13.5, `abjad` 7.2 ila 13.6, `plain` 7.3 ila 11.9, `selfcite` 11.8 ila 30.6, `codebook` uyan yok. Referans 1.5.
- **Elde kalan en sağlam veri bulgusu (hipotezden bağımsız):** Voynich'in dağarcık büyüme profili (16 bin kelimede tür/kelime 0.25 ila 0.30, hapax 0.68 ila 0.72, ed1 0.86 ila 0.89; iki yarı 0.03 içinde tutarlı; beş görünümde aynı) seslisiz yazılmış çekimli bir doğal dilinkiyle örtüşüyor ve kapalı tablo üreteçlerininkiyle örtüşmüyor. Pencere profili ise tam tersini söylüyor. Hiçbir hipotez ikisini birleştiremiyor.
- **Sıradaki aday (yazıldı, sınanmadı, önce ön sınama):** komşuluğu koruyan genişletme. `abjad` büyüme profilini veriyor ama kelimeleri kısa ve `h2`'si yüksek. Harf harf şifre kelimeyi uzatıp `h2`'yi düşürüyor ama bir harflik farkı çok glifli farka çevirip komşuluğu bozuyor. İkisini uzlaştırabilecek tek tür kodlama, her ünsüzü tek glifle yazıp aralara konuma bağlı, öngörülebilir dolgu glifleri koyandır: bir ünsüzü farklı iki kelime yine tek glifle ayrışır (komşuluk korunur), kelime uzar, dolgu öngörülebilir olduğu için `h2` düşer, dolgunun yeri sabit olduğu için konum yapısı güçlenir.

## v0.11 bulguları: ön sınama aracı ve sözlük sınaması (2026-11-24, seed 7)

Tarihçe (`e53aecc`). Sözlük sınamasının sayıları v0.12'de dönem metinleri, bölümler ve daha çok örnekle yenilendi; buradaki "harf harf şifre elenir" cümlesi v0.12'de düzeltildi. Üreteçler değişmedi; `results/manuscripts.md` v0.10 ile aynı. Yeni rapor: `results/checks.md` üçüncü bölüm.

- **Ön sınama aracı (`probe`) yazıldı, ilke 8 oldu.** Var olan bir sınıfı 12 el yazmasında 9 saniyede ölçüyor.
- **v0.10'daki aday ön sınamada elendi.** "Ünsüz başına tek glif + konuma bağlı dolgu" altı dilde ve beş ayarda denendi (30 düzen, 18 saniye): büyüme bandına giren el yazması yok. ed1 oranı 0.51 ila 0.76 çıktı, yalın seslisiz yazımın (0.86) altında. Neden: seslisiz yazımdaki komşulukların çoğu harf ekleme ya da silmeyle oluşuyor; dolgu konuma bağlı olunca bir harf eklemek öbür harflerin dolgusunu da değiştiriyor. Sınıf yazılmadı, zincir koşulmadı.
- **Ortak adaylar nerede kalıyor (mevcut tablodan).** Büyümeye uyan en iyi 30 adayın ortak açıkları: çok fazla bir ve iki glifli kelime (`wlen_frac1` +6 ila +19, `wlen_frac_le2` +6 ila +17), `h2` yüksek (+7 ila +11), `jsd_last` düşük (-10 ila -11). Yani elimizdeki açık dağarcıklı üreteçler yoğun komşuluğu kısa kelimelerle elde ediyor; Voynich ise aynı yoğunluğu 4 ila 5 glifli kelimelerle ve çok öngörülebilir bir harf dizilişiyle elde ediyor.
- **Sözlük sınaması: Voynich'in dağarcığında sözlük kısıtı görünmüyor.** Yöntem üretece ve önsele dayanmaz: metnin ilk 16 bin kelimesinden kelime içi glif zinciri öğrenilir, aynı sayıda kelime bağımsız çekilir (vekil), vekil hem gerçek metnin kendisiyle hem görülmemiş ikinci yarıyla karşılaştırılır. Sonuç (k = 2):
  - Voynich, beş görünüm: tür oranı 0.96 ila 1.06, yeni kelime oranı 0.84 ila 0.95. Yani harf dizilişinden serbestçe üretilen kelimeler, gerçek metinle aynı sayıda farklı kelime veriyor ve gerçek metin, görülmemiş yarıda vekil kadar sık yeni kelime üretiyor.
  - 22 doğal dil, düz metin: tür oranı 1.55 ila 3.24 (medyan 2.26), yeni kelime oranı 1.89 ila 5.18 (medyan 2.88). En düşükler İbranice ve Arapça (1.55, 1.62). Voynich aralığına giren dil yok.
  - Aynı diller seslisiz yazılınca (19 dil): tür oranı 1.37 ila 1.80, yeni kelime oranı 0.96 ila 2.66. Tür oranında Voynich aralığına giren yok.
  - k = 1'de de ayrım sürüyor: Voynich tür oranı 1.14 ila 1.39, diller en az 1.86.
  - Üreteçler (sınıf başına 6 örnek): `slotgram` 0.85 ila 1.23 ve 0.00 ila 1.11; `selfcite` 0.97 ila 1.81 ve 0.56 ila 0.95; `codebook` 0.87 ila 1.81 ve 0.37 ila 2.14; `verbose` 1.17 ila 2.33 ve 1.28 ila 4.65; `grille` 1.15 ila 1.87 ve 2.56 ila 69.6 (kapalı tablo görülmemiş yarıda neredeyse hiç yeni kelime üretmez); `slotcite` 1.09 ila 1.75 ve 1.34 ila 10.7.
- **Bunun anlamı ve sınırı.** Voynich kelimeleri, bir alfabeyle (sesli ya da seslisiz) bire bir yazılmış bir doğal dilin kelimeleri gibi davranmıyor: doğal dilde harf dizilişi kurallarına uyan olası kelimelerin çoğu sözlükte yoktur, Voynich'te ise kurala uyan her şey yazılıyor gibi. Bu, "metin anlamsız" demek değildir. Aynı imzayı verenler: sözlüksüz üretim (`slotgram`, `selfcite`) ve kod uzayını sık dolduran kelime kelime kodlama (`codebook` örneklerinin yarısı). Elenen: düz ya da seslisiz yazılmış doğal dil ve (altı örnekle) harf harf şifre. Sınırlar: diller modern İncil çevirileri (dönem metni yok); `verbose` ve `codebook` için örnek sayısı az; hece ya da kelime parçası yazan sistemler ayrıca sınanmadı.
- **Hedef merdiveni açısından:** bu, 2. basamağa (daraltma) ait ilk veri bulgusu: aday "dil ve yazım türü" kümesinden "alfabeyle bire bir yazılmış doğal dil" çıkıyor. 1. basamak hâlâ geçilmedi: Voynich'i üreten bir süreç gösterilemedi.
- **Sıradaki aday (yazıldı, sınanmadı; önce ön sınama):** Voynich'in kendi düşük dereceli glif zincirinden bağımsız çekilen kelimeler büyüme ölçülerini büyük ölçüde tutturuyor (k = 2 vekilde tür/kelime 0.25 ila 0.29, hapax 0.70 ila 0.73, ed1 0.75 ila 0.81; Voynich 0.25 ila 0.30, 0.68 ila 0.72, 0.86 ila 0.89). Bu, Voynich'ten öğrenilmiş bir betimlemedir, hipotez değil. Hipotez hâli: rastgele kurulmuş seyrek bir glif otomatı (önselden çekilen geçiş yapısı, Voynich'e bakmadan) aynı profili üretir mi. Ölçüt aynı: büyüme bandı ve doğrulama T'si.

## v0.12 bulguları: sözlük sınamasının sınırları (2026-11-24, seed 7)

Tarihçe (`2468f9f`). Sonundaki otomat öngörüsü v0.13'te sınandı. Rapor: `results/checks.md` üçüncü bölüm.

Eklenen: dönem metinleri (`fetch_period`, `load_period`), ZL sayfa değişkenleri (`ivtff_page_variables`), sözlük sınamasında dönem metni grubu, Voynich bölümleri ve sınıf başına 30 örnek.

VL-012'de yazılan dört sınırın durumu:

- **1. "Diller modern çeviri" sınırı kapandı (üç dil için).** 15. yüzyıl metinlerinde sözlük kısıtı modern metinlerdeki kadar belirgin: tür oranı (k = 2) Latince 1.75, İspanyolca 1.79, İtalyanca 1.96; yeni kelime oranı 3.14 ila 3.57. Seslisiz yazılınca tür oranı 1.24 ila 1.48, yeni kelime oranı 1.92 ila 2.23. Voynich (0.96 ila 1.06; 0.84 ila 0.95) aralığına giren yok. Açık kalan: Almanca, İbranice ve tıbbi ya da botanik tür için dönem metni yok.
- **2. Örnek sayısı artınca `verbose` hükmü değişti: elenmiyor.** 30 örnekte tür oranı 0.97 ila 3.00 (medyan 1.29), yeni kelime oranı 0.99 ila 8.27 (medyan 2.03); 2 örnek Voynich aralığında. Ayrı ölçüm (90 örnek, ayar kaydıyla): Voynich aralığına girenlerin neredeyse hepsi kelime içine yüksek olasılıkla (0.58 ila 0.65) rastgele boşluk koyan düzenler. Bu düzenlerde "kelime" düz metnin kelimesi değil, harf kodlarının rastgele parçası; sözlük yapısı zaten kayboluyor. Ama bu örneklerin kelimeleri çok kısa (ortalama 1.8 ila 2.5 glif; Voynich 3.8 ila 4.9) ve dağarcıkları küçük (16 bin kelimede 1000 ila 2600 tür; Voynich'te yaklaşık 4000). Kelime sınırını koruyan ya da hece hece yazan `verbose` düzenlerinde tür oranı en az 1.10 (medyan 1.97 ve 1.68).
- **Sınıf başına 30 örnekte Voynich aralığına (tür oranı 0.90 ila 1.10, yeni kelime oranı 0.75 ila 1.10) girenler:** `slotgram` 13, `codebook` 6, `slotcite` 6, `verbose` 2, `selfcite` 1, `grille` 0. `grille` kapalı tablo olduğu için görülmemiş yarıda neredeyse hiç yeni kelime üretmiyor (yeni kelime oranı en az 1.42).
- **4. Sonuç bölümlerin karışımından doğmuyor.** 5000 kelimelik yarılarla: Currier A tür oranı 0.97, Currier B 0.98, bitki bölümü 0.95, yıldızlı reçete bölümü 0.99. Aynı boyda 22 doğal dil: en az 1.32, medyan 1.84. Yeni kelime oranı bölümden bölüme oynuyor (A 0.65, B 1.18, bitki 0.71, yıldız 1.10; diller en az 1.41); B ve yıldız bölümünde ilk yarıdan öğrenilen zincir ikinci yarıyı biraz daha az kapsıyor, yani bu bölümlerin içi tam durağan değil. Banyo, eczacılık ve yalnız metin bölümleri ölçmek için kısa.
- **3 ve 5 açık.** Hece ya da kelime parçası yazan sistemler ayrı sınıf olarak sınanmadı (yalnız `verbose` hece modu: tür oranı en az 1.20). Kelime uzunluğu eşlenmiş karşılaştırma yapılmadı; tabloda ortalama uzunluklar yan yana duruyor (Voynich 3.8 ila 4.9, düz diller 4.4, dönem metinleri 4.4 ila 5.4).
- **Ön sınama (ilke 8): rastgele katmanlı glif otomatı geçti.** Glifler 4 ila 8 katmana dağıtılır, geçişler aynı ya da sonraki iki katmana gider, her kelime bağımsız bir yürüyüştür; yapı Voynich'e bakılmadan rastgele kurulur. 96 ayar düzeni, düzen başına 4 el yazması, 48 saniye: 4 düzende büyüme bandına giren el yazması var (en iyisi 24 glif, 8 katman, glif başına 5 çıkış, düz ağırlık: tür/kelime 0.22, hapax 0.67, ed1 0.86; `h2` 1.64, kelime uzunluğu 5.1 ± 2.0, `jsd_last` 0.42). Komşu kelime benzerliği yok (0.00; Voynich +0.10 ila +0.18), bu bilinen açık. Öngörü (zincirden önce yazıldı): `automaton` sınıfında büyümeye uyan el yazması sayısı `slotgram`'ın 29 ila 35'inin üstüne çıkar ve uyanlar içinde en iyi doğrulama T'si beş görünümün çoğunda 5'in altına iner. İnmezse otomat da iki ölçütü birleştiremiyor demektir.
- **Hüküm (v0.11'deki cümlenin düzeltilmiş hâli).** Voynich'in kelimeleri, kelime sınırı düz metnin kelime sınırı olan ve harfleri bire bir (sesli ya da seslisiz) yazan bir doğal dil metni gibi davranmıyor; bu, 22 modern ve 3 dönem metninde, beş Voynich görünümünde ve ölçülebilen dört bölümde ayrı ayrı tutuyor. Elenmeyenler: sözlüksüz üretim (`slotgram`, `slotcite`, `selfcite`), kod uzayını sık dolduran kelime kelime kodlama (`codebook`), ve Voynich "kelimesi"nin düz metin kelimesi olmadığı her sistem (kelime içi boşluklu şifre gibi). Sözlük sınaması tek başına "anlamlı mı, anlamsız mı" sorusunu yanıtlamaz; yanıtladığı soru "kelimeler bir dilin sözlüğünden mi geliyor" sorusudur.

## v0.13 bulguları: rastgele glif otomatı sınandı, öngörünün yarısı tuttu (2026-11-24, seed 7, pencere 2000)

Tarihçe (`7a86eab`); el yazması tablosu hâlâ geçerli. Rapor: `results/manuscripts.md` (dokuz sınıf, sınıf başına 2000 el yazması). Eklenen: `automaton` sınıfı. Ön sınama ve öngörü v0.12 bölümünde, zincirden önce yazıldı.

- **Tutan yarı:** büyüme profiline uyan `automaton` el yazması sayısı 88 ila 112 (2000'de); `slotgram` 29 ila 35, `slotcite` 16 ila 36, `grille` 2 ila 15. Anlamsız metin üreteçleri içinde en yükseği; yalnız `abjad` daha yüksek (105 ila 335).
- **Tutmayan yarı:** uyanlar içinde en iyi doğrulama T'si 6.1 ila 8.9; hiçbir görünümde 5'in altına inmedi. Yalnız pencere profiline göre seçilenlerde T medyanı 6.9 ila 8.5 (`grille` 5.2 ila 6.7). Otomat da iki ölçütü birleştiremiyor.
- **Otomatın açıkları (pencere profiline göre seçilenler, `eva_glyph`):** `jsd_first` +18 ve `first_entropy_ratio` -15 (kelime başı fazla kısıtlı: yürüyüş hep ilk iki katmandan başlıyor), `char_double_rate` -12, `wlen_skew` +11, `wlen_autocorr1` -7 (komşu kelime benzerliği yok, beklenen açık). İç değişkenlik düşük (yayılım oranı 0.19 ila 0.26).
- **Sözlük sınamasında otomat Voynich ile aynı imzayı veriyor:** 30 örnekte tür oranı 0.89 ila 1.03 (medyan 0.98), yeni kelime oranı medyan 0.93; 24 örnek Voynich aralığında (sınıflar içinde en yüksek; `slotgram` 13).
- **Ortak ölçütte sıralama** (büyümeye uyanlar içinde en iyi T): `slotcite` 5.1 ila 12.7, `slotgram` 5.5 ila 9.9, `automaton` 6.1 ila 8.9, `grille` 6.5 ila 23.1, `verbose` 6.8 ila 13.7, `abjad` 7.2 ila 13.6, `plain` 7.3 ila 11.9, `selfcite` 11.8 ila 30.6, `codebook` uyan yok. Referans 1.5. Dokuz hipotezin hiçbiri Voynich'i üretemiyor.
- **Sınıflandırıcı raporu (yardımcı):** CV 0.922; kararı anlamsız metin sınıfları arasında bölünüyor.

## v0.14 bulguları: kelime sırası, bozulma taraması ve hedef hakkında hüküm (2026-11-24, seed 7)

Tarihçe (`aa5e142`). Ölçümler geçerli. "Hedef açısından sonuç" paragrafındaki bir cümle yanlıştı ve v0.15'te düzeltildi; literatür notunun yerini v0.15'teki okuma aldı. Rapor: `results/checks.md` (dördüncü ve beşinci bölüm). Üreteçler değişmedi; `results/manuscripts.md` ve `results/report.md` v0.13 ile aynı.

Eklenen: `checks` içine sıra deneyi (`order_stats`), kelime aileleri (`word_families`), bozulma taraması (`degradation_experiment`); tür denetimi metinleri; Wikisource üst bilgisi temizliği.

### Kelime sırası sınaması

Yöntem üretece ve önsele dayanmaz. İlk 16 bin kelimeden kelime ikilisi modeli öğrenilir; görülmemiş sonraki 16 bin kelimede, tek kelime sıklığına göre kelime başına kaç bit kazandırdığı ölçülür; aynı ölçüm satır içi karıştırılmış metinde tekrarlanır ve fark alınır.

- **Voynich'te kelime sırası bilgi taşımıyor.** Beş görünüm: -0.008 ila +0.020 bit/kelime. Karışım ağırlığı eğitim yarısında 0.05 ila 0.1 seçiliyor, yani model sıranın işe yaramadığını kendisi buluyor.
- **Her doğal dil metninde taşıyor.** 22 dil: en az 0.164 (Macarca), medyan 0.522, en çok 0.961. Dönem ve tür metinleri: Kempis 0.181, Plinius (bitki) 0.221, Celestina 0.254, Alberti 0.295, Cennini (tarif, yaklaşık 1400) 0.833. Voynich, en düşük doğal dil metninin sekizde birinden az.
- **"Liste gibi metin" itirazı tutmuyor.** Tarif ve ilaç metinlerinde sıra bilgisi düşük değil, yüksek (kalıplaşmış ifadeler): 3500 kelimelik yarıyla Celsus 0.805, Apicius 0.629, Cennini 0.500, Macer 0.322. Aynı boyda Voynich 0.000 ila 0.011, bölümleri (Currier A ve B, bitki, yıldız) 0.000 ila 0.006; 22 dilin en düşüğü 0.131. Bu boyda en düşük gerçek metinler Kempis 0.054 ve Cato 0.076; boy küçüldükçe ayrım daralıyor ama kapanmıyor.
- **Üreteçler (sınıf başına 20 örnek; sayılar örnekleme ile oynar):** bağımsız kelime çekenler sıfır (`automaton` 20/20, `slotgram` 20/20, `selfcite` 20/20, `slotcite` 19/20 örnek 0.04'ün altında). `grille` çok yüksek (medyan 2.61, hiçbiri 0.04'ün altında değil; tablo döngüsü). Dil tabanlılar: `verbose` medyan 0.458, `codebook` medyan 0.255; 20 örnekten sırasıyla 3 ve 2'si 0.04'ün altında (yazıcı katmanındaki harf çeşitlemeleri kelime kimliğini bozduğunda).
- **Aile düzeyinde** (kelime türleri "bir harf farklı" ailelerine toplanınca) Voynich +0.017 ila +0.032: sıfırdan büyük ama çok küçük.

### Bozulma taraması: sınamaların eleyemediği tek dil ihtimali

Soru: gerçek bir dil metni hangi bozulma altında sözlük, sıra ve büyüme ölçülerinde birden Voynich gibi görünür? 287 düzen (22 dil; sesli ve seslisiz; kelimelerin 0.3, 0.6, 0.9'unun bir harf farklı yazılması; harflerin bir bölümünün 2 ya da 3 eşseslisi).

- **Kelime sınırı hatası açıklamıyor** (ayrı deneme): boşlukların %40'ı yanlış olsa bile sıra bilgisi 0.15 ila 0.25 kalıyor.
- **Sesli yazımda üçü birden tutmuyor.** 154 düzenden 54'ü sözlük ve sırayı tutturuyor, ama hepsinde dağarcık Voynich'inkinden çok daha hızlı büyüyor (tür/kelime en az 0.44; Voynich 0.25 ila 0.30).
- **Üçünü birden tutturan 25 düzenin hepsi seslisiz yazım + yoğun yazım çeşitlemesi** (21'i kelimelerin 0.3 ila 0.9'u bir harf farklı, 4'ü eşsesli yazım). Bu düzenlerde kelimeler çok kısa (ortalama 2.3 ila 3.1 harf; Voynich 3.8 ila 4.9 glif) ve aile düzeyinde bile sıra bilgisi geri gelmiyor (-0.014 ila +0.002). Yani dil bilgisi istatistik olarak görünmez hâle geliyor.

### Hüküm

Üretece dayanmayan üç ölçüm (sözlük, sıra, büyüme) birlikte şunu söylüyor. Voynich şunlardan biri gibi davranmıyor:

1. Alfabeyle (sesli ya da seslisiz) bire bir yazılmış doğal dil: sözlük sınaması ve sıra sınaması ayrı ayrı eliyor.
2. Kelime sırası korunmuş kelime kelime kodlama (yoğun yazım çeşitlemesi eklenmedikçe): kelime kimliği korunduğu için kaynak dilin sıra bilgisini taşır (22 dilde en az 0.165); Voynich'te yok.
3. Kelimesi düz metnin harfi ya da hecesi olan yazım (yoğun yazım çeşitlemesi eklenmedikçe): komşu parçalar arasında güçlü bağ olur (`verbose` medyan 0.458); Voynich'te yok.

Sınamaların eleyemediği iki ihtimal kalıyor:

- **A. Anlam taşımayan üretim:** kelimeler harf dizilişi kurallarından, sözlüksüz ve birbirinden bağımsız (ya da zayıf bağlı) üretilmiş. `automaton`, `slotgram`, `slotcite`, `selfcite` bu türden; hiçbiri Voynich'i tam üretemiyor (v0.13), ama üç ölçümde de Voynich ile aynı tarafta duruyorlar.
- **B. Dil bilgisinin istatistik olarak silindiği yazım:** örneğin kısa ünsüz iskeletleri ve kelimelerin çoğunda yazım çeşitlemesi, ya da kelime sırasını ve kelime kimliğini bilerek bozan bir şifre.

**Hedef açısından sonuç (DÜZELTİLDİ, v0.15'e bak: "B doğruysa hiçbir tercüme sınavlardan geçemez" cümlesi anahtarla geri okunan şifreler için yanlış).** Birincil amaç "toplulukça kabul edilebilir ve kanıtlanabilir tercüme" idi. A doğruysa tercüme edilecek bir şey yok. B doğruysa, önerilen hiçbir tercüme çözme kapısındaki sınavlardan geçemez: boş sınav (aynı yöntem karıştırılmış metinde anlam çıkarmamalı) geçilemez, çünkü Voynich'in kendisi kelime sırası bakımından karıştırılmış metinden ayırt edilemiyor; sözlüğe dayalı doğrulama yapılamaz, çünkü kelimeler bir sözlük kısıtı göstermiyor. Yani iki durumda da amaca istatistik yoldan ulaşılamaz. Bu bir kanıt değil, ölçüme dayalı güçlü bir gerekçedir; sınırları aşağıda.

**Sınırlar (dışarıya söylenmeden önce):** (1) 22 modern dil ve 6 dönem ya da tür metni; Semitik ve Türk dilleri için dönem metni yok. (2) Kelime sınırı: belirsiz boşluklar kelime sınırı sayılmayınca sonuç değişmiyor (`results/checks.md`, "belirsiz boşluk birleşik" satırları: v101'de tür oranı 0.97, sıra +0.009; 5000 ve 3500 kelimelik yarılarla v101 ve `zl_glyph` tür oranı 0.93 ve 0.96, sıra +0.003 ve +0.001). Kesin boşlukların kendisinin yanlış olması ihtimali ayrı deneme ile sınandı (gerçek dilde boşlukların %40'ı bozulunca sıra bilgisi 0.15 ila 0.25 kalıyor), depoda kalıcı sınaması yok. (3) Sıra ölçümü komşu iki kelimeye bakıyor. Daha uzak bağlar için yalnız ayrı bir deneme yapıldı (depoda kalıcı sınaması yok, VL-014): son 200 kelimenin, sırasından bağımsız, sonraki kelimeyi tahmine katkısı görülmemiş yarıda Voynich'te +0.12 ila +0.13 bit/kelime, İncil çevirilerinde +0.38 ila +1.12, dönem ve tür metinlerinde +0.04 ila +0.23. Voynich'teki katkı bölümler arası kelime dağılımı farkından geliyor: tek bir bölümün içinde (Currier A, bitki, yıldız) +0.03 civarı, A'dan öğrenip B'de sınayınca +0.74. Yani bir bölümün içinde kelimeler neredeyse bağımsız çekilmiş gibi, bölümler ise birbirinden farklı dağılımlar kullanıyor. Bu, anlamlı metinle de anlamsız üretimle de bağdaşır; hükmü değiştirmez ama 1. basamak için yön gösterir (bölüme göre değişen ayarlarla bağımsız kelime üretimi). (4) Literatür yalnız üstünkörü tarandı, aşağıdaki nota bak. (5) "B" ihtimali ancak dışarıdan bilgiyle (anahtar, eşleşen bir kaynak metin) sınanabilir.

**Literatür notu (2026-11-24, yalnız arama özetlerinden; makaleler sonradan okundu, güncel hâli v0.15'te).** İlgili görünen işler: Montemurro ve Zanette 2013 (PLOS ONE), uzun mesafeli kelime kümelenmesini anlamlı metin lehine yorumluyor, sınır (3) ile doğrudan ilgili; Lindemann ve Bowern 2020 (arXiv 2010.14697), karakter düzeyinde koşullu entropi; Stolfi'nin kelime grameri ve Zattera 2022 yuva modeli, gramerlerin gözlenen kelimelerden çok daha fazlasını ürettiği biliniyor; Timm ve Schinner, kendinden kopyalama; 2026 tarihli ön baskılar: kelime sınırı ötesi karşılıklı bilgi ve karıştırma sınaması (arXiv 2604.19762), "A Glyph Is Not a Letter, a Token Is Not a Word, a Space Is Not a Space" (arXiv 2608.17096), üretici gramer ve "pastiche" hipotezi (arXiv 2609.20835). Sözlük sınamasının ve görülmemiş yarıyla sıra sınamasının bu hâlleriyle yeni olup olmadığı bilinmiyor; dışarıya "ilk kez" denmez. Bu makaleler okunmadan v0.14 hükmü yayımlanmaz (VL-013).

## v0.15 bulguları: literatür okuması, Naibbe denetimi ve hükmün düzeltilmesi (2026-11-24, seed 7)

Hüküm bölümü güncel; v0.16 buna kelime ucu bağını ekledi, v0.17 üreteç tarafını değiştirdi. Rapor: `results/checks.md` (altıncı bölüm). Bu sürümde üreteçler değişmemişti.

Eklenen: `fetch` iki denetim dosyası indirir (`data/raw/controls/`: Naibbe örnek şifreli metni ve aynı metnin anahtarla geri okunmuş hâli); `load_eva_plain`; `checks` içine denetim deneyi (`control_experiment`).

### Literatür okuması (VL-013)

Tam metinler indirildi, PDF'ler yerelde metne çevrildi. Reddy ve Knight, Caruana ve ark. ile Rozanova ve Temerev'in ana bölümleri doğrudan okundu; ötekiler alt ajan özetiyle, satır numaralı alıntılarla. Her kaynak için yalnız bizim ölçümlerle ilgili kısım:

- **Reddy ve Knight 2011** (ACL LaTeCH atölyesi). Currier B, 17.6 bin kelime, 10 katlı çapraz doğrulama: önceki kelimeyi bilmek sonraki kelimeyi tahmini Voynich'te %8.85 iyileştiriyor; İngilizce %151, Arapça %252, Macarca %123, Çince %19.7. Kendi cümleleri: "One of the most puzzling features of the VMS is its weak word order". Bir kelimeden uzakta (d > 1) neredeyse hiç bağ bulmuyorlar; sayfa düzeyinde konu etkisi buluyorlar.
- **Rozanova ve Temerev 2026** (arXiv 2608.17096, ön baskı; hakem denetimi belirtilmiyor). ZL 3b, 32.7 bin kelime. Satır içi karıştırmayla düzeltilmiş komşu kelime bağı Voynich'te 0.066 bit (kelime entropisinin %0.79'u); dokuz denetim metninde %2.0 ila %15.8 (Plinius, Celsus, Culpeper ve Linnaeus kataloğu dahil). Currier A ve B ayrı ayrı sıfıra yakın; belirsiz boşluklar birleştirilince %0.54. Ek bulguları: (a) sıra bilgisi kelime kimliğinde değil kelime uçlarında: bir kelimenin son glifi ile sonrakinin ilk glifi arasında 0.197 bit (düz yazıda 0.018 ila 0.120), satır içi karıştırmada %88 ila %93'ü kayboluyor; (b) komşu kelimeler karıştırılmış metne göre %12 ila %16 daha sık "bir harf farklı"; (c) Naibbe şifresi ve Timm-Schinner üreteci düşük entropiyi ve zayıf sırayı üretiyor, ikisi de kelime ucu bağını (0.006 ila 0.009 bit) ve tek geçen kelime bolluğunu (türlerin %41'i ve %59 ila %60'ı; Voynich %70) üretemiyor. Vardıkları yer: bu özellikler "consistent with meaningless text but do not establish it"; "We do not claim that the manuscript lacks language or meaning".
- **Montemurro ve Zanette 2013** (PLOS ONE). Ölçtükleri şey kelimelerin metnin bölümlerine eşitsiz dağılması; tek karşılaştırma bütün kelimelerin karıştırılması. Komşu kelime sırası ölçülmemiş, anlamsız metin üreteciyle karşılaştırma yok, "kelimeler bağımsız çekiliyor ama dağılım bölümden bölüme değişiyor" ihtimali tartışılmamış. v0.14 sınır (3)'teki denememizle çelişmiyor: bir bölümün içinde bağ +0.03'e düşüyor, bölümler arasında büyük.
- **Amancio ve ark. 2013** (PLOS ONE). Kelime karıştırmaya karşı ağ ve kesiklilik ölçüleri; "the VMS is not compatible with shuffled texts". Sayı tabloları görsel olduğu için okunamadı. İki ölçüde doğal dillerle uyuşmadığını kendileri yazıyor; metinden anlaşıldığı kadarıyla bunlar tekrar eden kelime ikilisi sayısı ve kesiklilik (simgeler okunamadı).
- **Caruana, Layfield ve Abela 2022.** Üç kelimelik pencerede yönlü kelime çiftleri; Voynich'te karıştırılmış metnin iki katından biraz fazla, doğal dillerde fark çok daha büyük. Yalnız iki dil, sayılar grafikte.
- **Timm 2014** (arXiv 1407.6639). Nitel gözlemler: "in most cases all conceivable spelling permutations of a glyph group exist"; kelime düzeyinde kural yok; en az üç kelimelik dizilerden yalnız 35'i en az üç kez geçiyor. Sözlük sınamamızın nitel öncülü.
- **Zattera 2022.** 12 yuvalı kelime kalıbı kelimelerin %86.6'sını, türlerin %51.3'ünü kapsıyor; kalıbın üretebildiği 4.6 milyon diziden 2617'si gözleniyor (Stolfi gramerinde 1.4e20 diziden 4527'si). Bu, olasılıksız küme sayımıdır; bizim sözlük sınaması olasılık ağırlıklı çekimle, aynı kelime sayısında karşılaştırır. İki sonuç çelişmez: olası dizilerin çoğu çok düşük olasılıklıdır.
- **Gaskell ve Bowern 2022; Bowern ve Gaskell 2022.** 200 kelimelik örnekler, 42 ölçü. İnsanların uydurduğu anlamsız metin 42 ölçünün 41'inde Voynich ile bağdaşıyor; bazı şifreleme işlemleri de kelime düzeyi ölçülerle bağdaşıyor. Uzun metin gerektiren ölçüm yok.
- **Lindemann 2022** (kayan pencerede tür/kelime oranı). "Rastgele harflerden kurulan kelimelerde bu oran aşırı çıkar" gerekçesiyle anlamlı metin lehine yorumluyor. Bizim vekil ve `automaton` sonuçları bu gerekçeyi desteklemiyor: Voynich'in kendi harf dizilişinden bağımsız çekilen kelimeler gerçek metinle aynı sayıda tür veriyor.
- **Lindemann ve Bowern 2020.** Yalnız karakter düzeyi: Voynich h2 1.91 ila 2.56; 311 dil örneğinin en düşüğü 2.77. Seslisiz yazım düşük h2'yi açıklamıyor (seslisiz yazılar daha yüksek h2 veriyor); v0.8 ve v0.11'deki gözlemimizle aynı yönde.
- **Parisel 2026** (arXiv 2604.19762): kelime sınırı ötesi glif bağı (0.230 bit), kelime kimliği düzeyinde ölçüm yok. **Turenne 2026** (arXiv 2609.20835): bizim ölçümlerle örtüşmüyor.

Okunamayanlar: Timm ve Schinner 2020 (Cryptologia; erişilemedi, yalnız Rozanova-Temerev'in aktarımı), Greshko 2025 makalesinin kendisi (yalnız depo ve aktarım), Stolfi'nin gramer sayfası (verilen adres 404), Schinner 2007, Landini 2001, Voynich Ninja forumu.

**Yenilik durumu.** (1) Kelime sırası sınaması yeni değil: 2011'de çapraz doğrulamayla, 2026'da tür denetim metinleri ve sağlamlık denetimleriyle yayımlanmış. Bizimki bağımsız bir doğrulama: farklı kestirici, 22 dil, beş görünüm, aynı sonuç. (2) Sözlük sınaması (olasılık ağırlıklı vekille tür oranı ve görülmemiş yarıda yeni kelime oranı) okunan kaynakların hiçbirinde bu hâliyle yok; komşuları Timm'in nitel gözlemi, Zattera'nın sayımı ve Rozanova-Temerev'in tek geçen kelime payı. (3) Büyüme profili (16 bin kelimede ed1 bandı) ve bozulma taraması okunan kaynaklarda yok. (2) ve (3) için: forumlar ve yukarıdaki okunamayanlar bakılmadan "ilk kez" denmez. (4) Bizim atladığımız, literatürün bulduğu şey: sıra bilgisi sıfır değil, kelime uçlarında. Kelimeleri birbirinden bağımsız çeken üreteçlerimiz (`automaton`, `slotgram`) bunu üretemez; 1. basamak için yeni bir ölçüt.

### Naibbe denetimi

Naibbe şifresi (Greshko 2025, Cryptologia): düz metnin boşlukları silinir, harfler tekli ve ikili parçalara bölünür, her parça birkaç eşsesli glif dizisinden biriyle yazılır; elle uygulanabilir ve anahtarı bilen metni geri okur. Yazarın yayımladığı örnek (Plinius, 34.8 bin şifreli kelime) ve aynı metnin anahtarla geri okunmuş hâli (her şifreli kelimenin yerinde bir ya da iki harflik parça) Voynich ile aynı ölçümlerden geçirildi. 16 bin kelimelik yarıyla (`results/checks.md`; 8 binlik yarı da orada):

| metin | sıra (bit/kelime) | tür oranı k=2 | yeni kelime oranı k=2 | görülmemiş yarıda yeni kelime payı | hapax/tür | ed1 |
|---|---|---|---|---|---|---|
| Naibbe, şifreli (iki EVA görünümü) | +0.009 | 1.13 ila 1.16 | 1.89 ila 1.99 | 0.127 | 0.506 | 0.986 ila 0.991 |
| Naibbe, anahtarla çözülmüş parçalar | +0.396 | yorumlanmaz | yorumlanmaz | 0.004 | yorumlanmaz | yorumlanmaz |
| Voynich (`eva_basic`, `eva_glyph`) | -0.007 | 1.03 ila 1.07 | 0.86 ila 0.95 | 0.215 | 0.681 | 0.861 ila 0.884 |

- **İçinde gerçek Latince olan bir metin sıra sınamasında Voynich gibi sıfır veriyor.** Bu, v0.14 hükmünün 3. maddesindeki "yoğun yazım çeşitlemesi eklenmedikçe" kaydının somut ve yayımlanmış örneği; Rozanova ve Temerev'in ölçümüyle de uyuşuyor (%1.1 ila %1.3).
- **Doğru anahtar sıra bilgisini geri getiriyor.** Aynı metin anahtarla parçalarına çevrilince görülmemiş yarıda +0.396 bit/kelime (8 binlik yarıyla +0.259). Örnekte her şifreli kelime türü tek bir parçaya gidiyor (ayrı deneme: 5600 tür, 437 parça, parça başına medyan 9 yazılış).
- **Naibbe örneği dağarcık bakımından Voynich'ten ayrışıyor.** Tek geçen kelime payı düşük (0.51; Voynich 0.68), görülmemiş yarıda yeni kelime seyrek (0.127; Voynich 0.215), vekile göre yeni kelime oranı yüksek (1.9 ila 2.0; Voynich 0.86 ila 0.95), "bir harf farklı" komşuluk doymuş (0.99; Voynich 0.86 ila 0.88). Tür oranındaki fark küçük (1.13 ila 1.16 ve 1.03 ila 1.07) ve 8 binlik yarıda daha da daralıyor (1.06 ila 1.08 ve 0.99 ila 1.03); tek başına ayırıcı sayılmaz. Yani şifrenin yayımlanan ayarları Voynich'ten daha kapalı bir dağarcık üretiyor. Tek örnek, tek düz metin; şifrenin başka ayarları denenmedi.

### Hükmün düzeltilmesi

v0.14 şunu söylüyordu: "B doğruysa, önerilen hiçbir tercüme çözme kapısındaki sınavlardan geçemez." Bu cümle yanlıştı. Hata şuradaydı: "dil bilgisinin silindiği yazım" başlığı altında iki ayrı şeyi birleştirmiştim.

- **B1, anahtarla geri okunan şifre** (Naibbe gibi: her şifreli kelime türü tek bir düz metin parçasına gider, bir parçanın çok sayıda yazılışı vardır). Şifreli metinde dil bilgisi görünmez, ama silinmemiştir: doğru anahtar onu geri getirir ve bu, görülmemiş sayfalarda ölçülebilir (yukarıdaki tablo). Böyle bir çözüm kapıdaki sınavlardan ilke olarak geçebilir: tek sabit kural vardır, karıştırılmış metne uygulanınca düzen çıkmaz, görülmemiş sayfada sıra bilgisi geri gelir.
- **B2, geri alınamayan bozulma** (rastgele yazım çeşitlemesi gibi, v0.14 bozulma taramasındaki düzenler). Burada bilgi gerçekten kaybolmuştur; v0.14'teki cümle yalnız bunun için doğru.

Düzeltilmiş hüküm:

1. Voynich, alfabeyle bire bir yazılmış bir doğal dil gibi ve kelime sırası korunmuş kelime kelime kodlama gibi davranmıyor (v0.14, değişmedi; sıra kısmı literatürde de var).
2. Yüzeydeki istatistikler "anlamsız üretim" (A) ile "anahtarla geri okunan şifre" (B1) arasında karar veremiyor. Bu, Rozanova ve Temerev'in vardığı yerle aynı.
3. Elimizdeki tek somut B1 örneği (Naibbe, yayımlanan ayarlarıyla) Voynich'i üretmiyor: dağarcığı daha kapalı (tablo) ve kelime ucu bağı yok (Rozanova-Temerev). Anlamsız üreteçler de üretmiyor (v0.13). Yani 1. basamak iki yönde de açık.
4. Tercüme "ulaşılamaz" değil; ulaşmanın yolu istatistikle karar vermek değil, anahtar aramak ve bulunanı kapıdaki sınavlarla sınamak. Bilinen saldırılar Naibbe'yi göremiyor (Rozanova-Temerev: ayarlı ikame saldırısı Naibbe'de sıfır veriyor). Arama zor ve sonucu belirsiz; söz verilmez.

Bundan çıkan sınanabilir soru (VL-015, yapılmadı): Voynich kelime türlerini birkaç yüz sınıfa indiren ve görülmemiş yarıda sıra bilgisini geri getiren bir eşleme var mı. Önce güç denetimi gerekir: aynı arama, anahtar verilmeden Naibbe örneğinde sıra bilgisini bulabilmeli; bulamıyorsa sınamanın gücü yoktur ve sonucu yazılmaz. Sınıflar adsızdır, metne anlam atanmaz; sınıfları harflere bağlayan her adım çözme kapısının arkasındadır.

**Güç denetiminin ilk denemesi tutmadı (2026-11-24, ayrı deneme; depoda kalıcı sınaması yok).** Ölçüt denemeden önce yazıldı: kelime türleri komşularının dağılımına göre 30, 100 ve 300 sınıfa kümelenir (anahtar verilmez, yalnız ilk yarıdan), sıra sınaması sınıf dizisinde görülmemiş yarıda koşulur; Naibbe örneğinde en az +0.05 bit/kelime bulunmalı. Bulunan: +0.016, +0.020, +0.030 (rastgele eşlemeyle +0.001 ila +0.004; anahtarla +0.396). Yani bu yöntem, cevabı bilinen metinde bile dil bilgisinin onda birini bulamıyor; Voynich'e uygulanmadı ve uygulanırsa sonucu yorumlanamaz. Neden: 16 bin kelimede türlerin yarısı bir kez geçiyor, bir parçanın yazılışları tek tek çok seyrek. Sıradaki aday, kelimenin iç yapısını da kullanan (Naibbe'de kelime = ilk harfin ön dizisi + ikinci harfin son dizisi) bir arama; ölçütü yine önceden yazılır.

**Süreç notu.** v0.14'teki yanlış cümle, kendi bozulma taramamın sonucunu (rastgele bozulma) literatürü okumadan genellememden çıktı ve Ali'ye sabah raporunda öyle söylendi; Ali amaç değişikliğini o raporla onayladı. Düzeltme aynı gün Ali'ye söylendi. Ayrıca v0.14 ve hafıza kayıtlarına tarih 2026-11-25 diye yazılmıştı; commit saatleri 2026-11-24 gösteriyor, tarihler düzeltildi (saate bakmadan yazılmıştı).

## v0.16 bulguları: kelime ucu bağı (2026-11-24, seed 7)

Ölçüm güncel; üreteç tarafı v0.17'de değişti. Rapor: `results/checks.md` (yedinci bölüm).

Eklenen: `checks` içine kelime ucu deneyi (`edge_reduce`, `edge_stats`, `edge_experiment`). Bu, Rozanova ve Temerev 2026'nın bulgusunun (sıra bilgisi kelime kimliğinde değil kelime uçlarında) bizim kestiriciyle, görülmemiş yarıda ve beş görünümde doğrulamasıdır; yeni bir bulgu değildir. Öngörü ölçümden önce yazıldı (VL-014) ve tuttu.

Ölçü: önceki kelimenin son glifi sonraki kelimenin ilk glifini görülmemiş yarıda ne kadar öngörüyor (bit/çift; satır içi karıştırmaya göre; yalnız aynı satırdaki komşular).

| metin | ham kelime sırası | son glif -> sonraki ilk glif | ilk glif -> ilk glif |
|---|---|---|---|
| Voynich, beş görünüm | -0.008 ila +0.018 | +0.166 ila +0.252 | +0.036 ila +0.073 |
| 22 doğal dil | +0.165 ila +0.960 | +0.004 ila +0.161 (medyan +0.059) | medyan +0.052 |
| dönem ve tür metinleri (5) | +0.181 ila +0.832 | +0.013 ila +0.101 | +0.013 ila +0.071 |
| Naibbe, şifreli | +0.009 | +0.004 | 0.000 |
| Naibbe, anahtarla çözülmüş | +0.395 | +0.489 | +0.121 |
| `selfcite` (20 örnek) | -0.003 ila +0.107 | -0.039 ila +0.057 | medyan +0.024 |
| `slotcite`, `slotgram` (20'şer örnek) | en çok +0.079 | -0.008 ila +0.038 | sıfıra yakın |
| `automaton`, bağsız (v0.16'da 6 örnek) | sıfıra yakın | -0.001 ila +0.014 | sıfıra yakın |

- **Voynich'te kelimeler birbirinden bağımsız değil: bağ birleşme yerinde.** Kelime kimliği sonraki kelimeyi öngörmüyor, ama bir kelimenin son glifi sonrakinin ilk glifini 22 dilin hepsinden daha iyi öngörüyor (en yüksek dil +0.161; Voynich en az +0.166). Tek başına bu sayı dillerden keskin ayrılmıyor; ayırıcı olan ikisinin birlikteliği: ham sıra sıfır, uç bağı büyük. Bu bileşimi 22 dilin, 5 dönem metninin ve Naibbe örneğinin hiçbiri vermiyor; v0.16'daki üreteçlerin de hiçbiri vermiyordu. v0.17'de `automaton` sınıfına eklenen bağ ayarı açıkken veriyor (tablodaki sayılar v0.17 koşusundan, sınıf başına 20 örnek).
- **Satır kenarı alışkanlığı değil.** Yalnız satır içi komşular sayılıyor; ayrı denemede satırların ilk ve son kelimesi yerinde bırakılarak karıştırınca da aynı (+0.145 ila +0.208). İlk yazdığım ölçü satır sonu ile sonraki satır başı arasındaki çiftleri de sayıyordu ve üreteçlerde yazıcı katmanının satır kenarı işaretlerini "bağ" gibi gösteriyordu (`automaton` en çok +0.102); düzeltildi (şimdi en çok +0.014).
- **Kopyalama bunu üretmiyor.** `selfcite` komşu kelimeleri birbirine benzetiyor (ilk glif -> ilk glif +0.055), ama birleşme yerinde bağ üretmiyor. Rozanova-Temerev de Timm-Schinner üreteci için aynısını bildiriyor.
- **Naibbe de üretmiyor** (+0.004; onların ölçümü 0.006 bit). Şifrede kelime sınırı ilgisiz düz metin parçalarının arasına düşüyor.
- **1. basamak için yeni ölçüt.** Bir üreteç ya da şifre adayı artık dört şeyi birlikte tutturmalı: pencere profili, büyüme profili, sıfır kelime sırası ve +0.17 dolayında uç bağı. Kelimeleri birbirinden bağımsız çeken hiçbir mekanizma dördüncüyü veremez; kelime, bir öncekinin bittiği glife bakarak başlamalı.

**Akış vekili denemesi (ayrı deneme, depoda kalıcı sınaması yok; öngörü yarım tuttu).** Soru: Voynich'in sıra yapısı, boşluğu da bir işaret sayan kısa hafızalı bir glif zinciriyle açıklanıyor mu. Metnin ilk yarısından k. derece zincir öğrenildi, aynı boyda metin üretildi. k = 3 ile: ham kelime sırası sıfıra yakın (öngörü tuttu), tür sayısı gerçeğin 0.86 ila 0.92'si (sınırda), ama uç bağı (ilk ve son glife indirgenmiş kelimelerle ölçü) gerçeğin yalnız %46 ila %82'si (`eva_glyph` +0.042 ve +0.091; `v101` +0.058 ve +0.071; `zl_glyph` +0.065 ve +0.103); öngörü "0.03 yakınında" idi, üç görünümün ikisinde tutmadı. k = 4'te uç bağı tutuyor ama zincir eğitim metnini ezberlemeye başlıyor (ham sıra +0.04 ila +0.20). Aynı zincir Latince ve İtalyancada k = 3'e kadar kelime sırasının yirmide birinden azını geri getiriyor. Yani Voynich'in sıra yapısının çoğu yerel glif istatistiği, ama hepsi değil; kalan kısım için üç gliften uzun bir bağlam gerekiyor.

## v0.17 bulguları: bağlı otomat sınandı (2026-11-24, seed 7, pencere 2000)

Tarihçe (`a951b97`); sayılar 32 feature ile. v0.18 aynı zinciri 33 feature ile yeniden koştu, sonuç değişmedi. Raporlar git geçmişinde.

Eklenen: `automaton` için `p_link` ayarı. 0 ise kelimeler bağımsız (eski otomat); 0'dan büyükse kelimenin ilk glifi, önceki kelimenin son glifine özgü bir dağılım ile genel başlangıç dağılımının karışımından çekilir. Önsel: yarı yarıya kapalı ya da 0.1 ila 1 arasında.

Ön sınama ve öngörü zincirden önce yazıldı (VL-010; ilke 8).

- **Ön sınama (aynı tohumla 40'ar el yazması, bağ gücü 0, 0.3, 0.6, 0.9): öngörünün üç maddesi de tuttu.** Son glif -> sonraki ilk glif ölçüsü bağ gücüyle büyüyor: medyan +0.002, +0.066, +0.205, +0.396 (Voynich +0.166 ila +0.252). Ham kelime sırası medyanı 0.000 kalıyor. Büyüme bandına giren el yazması sayısı değişmiyor (40'ta 3, 2, 2, 3). Sözlük sınamasında tür oranı medyanı 0.98, değişmiyor.
- **Zincir: pencere profili düzelmedi.** Doğrulama T medyanı `automaton` için 6.7 ila 8.3 (v0.13'te 6.9 ila 8.5); en iyi tek aday 5.7 ila 7.0; büyümeye uyan el yazması sayısı 83 ila 118 (v0.13'te 88 ila 112), bunların en iyi T'si 5.7 ila 7.5 (v0.13'te 6.1 ila 8.9). Referans 1.5. Farklar tohum akışının değişmesiyle açıklanacak kadar küçük. Beklenen buydu: 32 pencere feature'ı arasında birleşme yerindeki bağı gören bir ölçü yok.
- **Seçilen adaylar bağı biraz tercih ediyor.** Pencere profiline göre seçilen 20 adayda bağ gücünün medyanı 0.28 ila 0.41 (önsel medyanı 0.11). Kayma küçük ve T'ye yansımıyor.
- **Kelime ucu sınamasında (`checks`, sınıf başına 20 örnek) Voynich bandına giren tek üreteç örneği bağlı bir otomat** (20'de 1; öteki sınıflarda 0). Bağ açık örneklerde ölçü bağ gücüne göre +0.06 ile +0.64 arasında değişiyor; band dar olduğu için çoğu dışarıda kalıyor.
- **Sıralama değişmedi** (büyümeye uyanlar içinde en iyi T): `slotcite` 5.1 ila 12.7, `slotgram` 5.5 ila 9.9, `automaton` 5.7 ila 7.5, `grille` 6.5 ila 23.1, `verbose` 6.8 ila 13.7, `abjad` 7.2 ila 13.6, `plain` 7.3 ila 11.9, `selfcite` 11.8 ila 30.6, `codebook` uyan yok. Dokuz hipotezin hiçbiri Voynich'i üretemiyor.

**Ne öğrenildi.** Kelime ucu bağı ucuz bir mekanizmayla üretilebiliyor ve öbür üç ölçütü bozmuyor; yani v0.16'daki dördüncü ölçüt "anlamsız üretim" ihtimalini zorlaştırmıyor. Asıl açık yerinde duruyor: pencere profili (T 6 dolayında, hedef 1.5). Otomatın v0.13'te yazılan açıkları (kelime başı fazla kısıtlı, çift glif az, kelime uzunluğu çarpık, komşu kelime uzunluk benzerliği yok) bu ayarla kapanmıyor.

**Sıradaki soru (v0.18'de yapıldı).** Pencere feature'larına birleşme yerindeki bağı ölçen bir feature eklenmeli mi. Eklenirse 32 feature 33 olur ve bütün raporlar değişir; karşılığında el yazması düzeyindeki hüküm dördüncü ölçütü de görür. Yapılmadı; ayrı iş (VL-010).

## v0.18 bulguları: uç bağını gören 33. feature (2026-11-24, seed 7, pencere 2000)

Güncel durum budur (hüküm için v0.15 "Düzeltilmiş hüküm", v0.16 ve v0.17 ile birlikte okunur). Raporlar: `results/manuscripts.md` (asıl hüküm; dokuz sınıf, sınıf başına 2000 el yazması, 33 feature), `results/report.md`, `results/abc.md`, `results/search.md`, `results/checks.md`. Bütün zincir yeniden koşuldu.

Eklenen: `edge_mi` feature'ı. Aynı satırdaki komşu kelimelerde önceki kelimenin son glifi ile sonrakinin ilk glifi arasındaki karşılıklı bilgi, eksi satır içi karıştırılmış metindeki aynı değer (dört sabit tohumlu karıştırmanın ortalaması). Sembol adından bağımsızdır (ilke 3; testi geçiyor). Düz formüllü yanlılık düzeltmeleri denendi ve alfabe boyuna göre kaydığı için kullanılmadı (ayrı deneme): karıştırılmış metinde sıfır vermeleri gerekirken +0.04 ila +0.14 ya da -0.40 verdiler.

Öngörü zincirden önce yazıldı (VL-010).

- **Feature işini yapıyor.** Voynich pencerelerinde +0.18 ila +0.23 (pencereler arası sapma 0.06 ila 0.08); bağ üretemeyen sınıfların seçilen adaylarında -0.01 ila +0.01. Bu sınıflarda `edge_mi` artık "tutmayan feature" tablolarında, -6.5 ila -8.2 standart hata sapmayla duruyor.
- **Öngörü (1), "bağ üretemeyen sınıfların T'si yükselir": yalnız kâğıt üstünde tuttu.** Artış 0.0 ila 0.2 (ör. `grille` 5.2 ila 6.7'den 5.3 ila 6.7'ye; en iyi tek aday 3.6'dan 3.8'e). T 33 feature'ın ortak ölçüsü olduğu için tek bir feature'daki 7 standart hatalık açık onu neredeyse oynatmıyor. Beklediğim belirgin ayrışma olmadı.
- **Öngörü (2), `automaton`: yarım tuttu ve ölçütü kötü kurmuştum.** Seçilen adaylarda bağ gücünün medyanı 0.36 ila 0.44 (v0.17'de 0.28 ila 0.41; eşik 0.4, beş görünümün üçünde aşıldı). "Büyümeye uyanlar içinde en iyi T" sıralamasında `automaton` beş görünümün dördünde birinci (7.4, 6.2, 6.3, 6.3; `zl_glyph`'te 5.7 ile üçüncü). Ama v0.17'de de dördünde ilk ikideydi; öngörüyü yazmadan önce bu tabana bakmamıştım, dolayısıyla sıralama maddesi bir şey sınamadı.
- **Öngörü (3) tuttu:** hiçbir sınıf referansa (en çok 1.7) yaklaşmıyor. Seçilen adayların doğrulama T medyanı: `grille` 5.3 ila 6.7, `slotcite` 5.7 ila 7.1, `slotgram` 5.6 ila 7.4, `automaton` 6.7 ila 8.3, `verbose` 6.9 ila 8.9, `selfcite` 7.0 ila 10.5, `codebook` 7.3 ila 9.3, `plain` 7.3 ila 12.7, `abjad` 7.4 ila 14.6.
- **Büyümeye uyanlar içinde en iyi T:** `slotcite` 5.3 ila 12.6, `slotgram` 5.6 ila 9.8, `automaton` 5.7 ila 7.4, `grille` 6.6 ila 22.8, `verbose` 6.7 ila 13.5, `abjad` 7.1 ila 13.5, `plain` 7.3 ila 11.8, `selfcite` 11.7 ila 30.2, `codebook` uyan yok.

**Ne öğrenildi.** Hüküm tablosu artık dördüncü ölçütü görüyor, ama tablo değişmedi: uzaklığın kaynağı tek bir eksik özellik değil, 33 ölçünün çoğuna yayılmış 5 ila 10 standart hatalık açıklar. `automaton` için en büyükleri aynı: kelime başı fazla kısıtlı (`jsd_first` +13 ila +17), kelime uzunluğu çarpık (`wlen_skew` +6 ila +21), çift glif yok (`char_double_rate` -6 ila -12). Bir sonraki mekanizma tek özelliği değil bu üçünü birlikte hedeflemeli; ya da aramanın kendisi el yazması düzeyine taşınmalı (seçilen adaylar önselden rastgele çekilenlerin en iyileri, yönlendirilmiş arama pencere düzeyinde kaldı).

**Otomat v2 ön sınaması (2026-11-24, ayrı deneme; sınıfa eklenmedi).** Öngörü ve ölçüt önceden yazıldı (VL-010), taban aynı koşuda ölçüldü. Mekanizma: kelime ilk iki katman yerine ilk s katmandan birinde başlayabilir ve gliflerin bir bölümü kendini tekrar edebilir. Aynı tohumlarla 150'şer el yazması, ilk 8 pencerenin Voynich'e karşı T'si (`eva_glyph`, `v101`, `zl_glyph`):

| | büyüme bandında | en iyi %5'lik T | en iyi T | `jsd_first` sapması | `wlen_skew` sapması | `char_double_rate` sapması |
|---|---|---|---|---|---|---|
| eski otomat | 14 | 11.2, 8.9, 9.5 | 8.5, 7.9, 7.1 | 23.4 | 10.6 | 11.0 |
| otomat v2 | 25 | 9.8, 8.2, 8.0 | 6.7, 5.6, 4.9 | 15.1 | 13.4 | 9.6 |

Kesinleşen: serbest başlangıç katmanı büyüme bandına girişi artırıyor (14'ten 25'e) ve en iyi adayları belirgin yaklaştırıyor (150 rastgele çekimde en iyi T 4.9; zincirde 2000 çekimin en iyisi 5.7 idi). Ölçüte göre sonuç: (1) "en iyi %5'lik en az 1.0 düşer" üç görünümün ikisinde tuttu (`v101`'de 0.7); (2) "üç hedef sapma yarıya iner" tutmadı (`jsd_first` üçte bir azaldı, `wlen_skew` kötüleşti); (3) büyüme payı düşmedi, arttı. Ölçüt (1) tam tutmadığı için sınıfa eklenmedi. Sıradaki sürüm kelime uzunluğu çarpıklığını ayrıca hedeflemeli (kelimenin bitme olasılığı katmanla artan bir yürüyüş).

## Yol haritası (öncelik sırasıyla)

1. **Üreteç sadakati.** Asıl kaldıraç burada.
   - ~~Satır farkındalığı~~: yapıldı (v0.1, ortak yazıcı katmanı). Paragraf düzeyi feature yok; paragraf başı `p`/`t` etkisi yalnız `jsd_line_initial` içinden dolaylı görünüyor.
   - ~~Kelime içi konum grameri~~: yapıldı (v0.2). Üç yuvayla sınırlı; literatürdeki çok yuvalı kelime gramerleri denenmedi.
   - Verbose şifreye konuma duyarlı kod tabloları.
   - `selfcite` parametrelerini Timm ve Schinner 2019 makalesindeki değerlere çek.
   - Yeni sınıflar: homofonik şifre, hece yazısı, kısaltmalı Latince (ortaçağ abbreviatura).
2. **ABC ile parametre kestirimi.** Rejection ABC (v0.3), yönlendirilmiş arama (v0.4) ve el yazması düzeyinde karşılaştırma (v0.5) yapıldı. Melez üreteç (v0.6) ve çok yuvalı gramer (v0.7) sınandı, ikisi de tutmadı. Büyüme profili ölçüldü (v0.8); `abjad` ile `verbose` bileşimi sınandı, tutmadı (v0.9). Kod defteri sınandı, tutmadı (v0.10). Ön sınama aracı yazıldı, komşuluğu koruyan genişletme ön sınamada elendi, sözlük sınaması eklendi (v0.11). Sözlük sınaması genişletildi (v0.12); rastgele glif otomatı sınandı, yarısı tuttu (v0.13). Kelime sırası sınaması ve bozulma taraması yapıldı (v0.14). Literatür okundu, Naibbe denetimi eklendi, hüküm düzeltildi (v0.15). **Sıradaki:** (a) sınıf arama sınaması ve güç denetimi (VL-015); (b) kelime ucu bağı ölçüldü (v0.16) ve bağlı otomatla üretildi (v0.17); 33. feature eklendi, hüküm tablosu değişmedi (v0.18); sıradaki, otomatın üç büyük pencere açığını birlikte hedefleyen mekanizma ya da el yazması düzeyinde yönlendirilmiş arama; (c) uzak mesafeli bağlar için kalıcı sınama (VL-014); (d) durağan olmayan üreteçler (bölümden bölüme kayan ayar ya da tablo), Voynich tarafında bölüm sınırları ZL sayfa değişkenlerinden; (e) kalan okumalar (VL-013): Timm ve Schinner 2020, Greshko 2025, forum.
3. **Dönem metinleri.** Üç metin eklendi (v0.12: Latince, İtalyanca, İspanyolca; yalnız sözlük sınamasında kullanılıyor). Eksik: Almanca, İbranice, tıbbi ve botanik tür; dönem metinlerinin üreteçlere kaynak olarak bağlanması (`corpus.load_all` yalnız İncil okuyor).
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
- Dönem ve tür metinleri (`data/raw/period/`). Tür denetimi için: Cennino Cennini, Il libro dell'arte (İtalyanca zanaat tarifleri, yaklaşık 1400; it.wikisource, 189 bölüm, temiz 39.1 bin kelime); Apicius (Latince yemek tarifleri, 7.7 bin); Cato, De agri cultura (15.7 bin); Plinius, Naturalis historia 20 ila 27 (bitki ilaçları, 78.4 bin); Celsus, De medicina 5 ve 6 (ilaç tarifleri, 30.2 bin); Macer Floridus, De viribus herbarum (ortaçağ bitki kitabı, 14.3 bin). Wikisource sayfalarının tekrarlanan üst bilgisi yükleme sırasında atılır (`corpus._strip_page_boilerplate`); atılmazsa kelime sırası ölçümlerini şişirir (Cennini'de 53 bin kelimenin 14 bini üst bilgiydi). Dönem denetimi için: Thomas à Kempis, De imitatione Christi (Latince, yaklaşık 1420; The Latin Library, 41.9 bin kelime); Leon Battista Alberti, I libri della famiglia (İtalyanca, yaklaşık 1440; it.wikisource, 120.8 bin kelime); Fernando de Rojas, La Celestina (İspanyolca, 1499, 1913 baskısı eski yazımı koruyor; es.wikisource, yalnız "aucto" sayfaları, 65.0 bin kelime). Sayfa başlığı ve gezinme metni temizlenmedi (payı küçük); dipnotlar atıldı. Project Gutenberg 2026-11-24'te bakımdaydı, oradan metin alınamadı.

- Denetim metinleri (`data/raw/controls/`): Naibbe şifresi örnek şifreli metni ve çözümü, `greshko/naibbe-cipher` (GitHub, commit `5145f52`; Plinius, 34.8 bin kelime). Greshko, M. A. (2025), The Naibbe cipher, Cryptologia, doi 10.1080/01611194.2025.2566408. Lisans değiştirilmiş MIT: veriyi kullanan her yayın bu makaleyi kaynak göstermek zorunda.

Ham veri depoya girmez, `fetch` ile yeniden üretilir.
