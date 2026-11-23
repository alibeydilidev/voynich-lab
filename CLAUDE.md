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
python -m voynich_lab.cli all
pytest -q
```

Parametreler: `--window 2000`, `--per-language 24`, `--seed 7`.

## Mimari

| Dosya | Görev |
|---|---|
| `transliteration.py` | Takahashi EVA ve Claston v101 ayrıştırıcıları, üç görünüm (`eva_basic`, `eva_glyph`, `v101`), pencereleme |
| `corpus.py` | 22 dilde paralel İncil, yazıya göre normalizasyon |
| `generators.py` | Üretim süreçleri. `LANGUAGE_PROCESSES` gerçek metni dönüştürür, `GIBBERISH_PROCESSES` sıfırdan üretir |
| `features.py` | 32 feature: entropi, kelime uzunluğu, dağarcık, tekrar, kelime içi konum, satır konumu |
| `dataset.py` | Sentetik korpus fabrikası: (dil penceresi x süreç) -> satır |
| `model.py` | XGBoost, `GroupKFold` |
| `analyze.py` | Voynich çıkarımı, SHAP katkıları (`pred_contribs`), Mahalanobis tabanlı OOD |
| `cli.py`, `fetch.py` | Komut satırı ve indirme |

Ortak veri tipi `Lines = list[list[str]]`: satırlar, kelimeler, her karakter bir glif. Çok harfli glifler Unicode özel kullanım alanındaki tek karaktere eşlenir.

Sınıflar: `plain` (doğal dil, tek alfabeli ikame dahil), `abjad` (seslisiz yazım), `verbose` (harf başına 1-3 sembol), `grille` (Rugg tablosu), `selfcite` (Timm ve Schinner kendinden kopyalama).

Yeni süreç eklemek: fonksiyonu `generators.py` içine yaz, ilgili sözlüğe ekle. Başka hiçbir yere dokunmak gerekmez.

## v0 bulguları (2026-11-23, seed 7, pencere 2000)

Tam rapor: `results/report.md`.

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

## Yol haritası (öncelik sırasıyla)

1. **Üreteç sadakati.** Asıl kaldıraç burada.
   - Satır farkındalığı: satır başı ve sonu için ayrı kurallar (her sınıfa parametre olarak).
   - Kelime içi konum grameri: önek, gövde, sonek yuvalarına bağlı glif kümeleri (Voynich "kelime grameri" literatürü).
   - Verbose şifreye konuma duyarlı kod tabloları.
   - `selfcite` parametrelerini Timm ve Schinner 2019 makalesindeki değerlere çek.
   - Yeni sınıflar: homofonik şifre, hece yazısı, kısaltmalı Latince (ortaçağ abbreviatura).
2. **ABC ile parametre kestirimi.** Sınıflandırmanın ötesi: her üreteç için Voynich'e en yakın parametre bölgesini ara (approximate Bayesian computation). "Hangi süreç" yerine "hangi süreç, hangi ayarla, ne kadar yakın".
3. **Dönem metinleri.** İncil çevirileri modern. 15. yüzyıl Latince, İtalyanca, Almanca, İbranice, Osmanlıca öncesi Türkçe tıbbi ve botanik metinler ekle. `corpus.py` düz kelime listesi bekliyor, yeni yükleyici yazmak yeterli.
4. **Üçüncü transliterasyon.** Zandbergen ve Landini (ZL, IVTFF). voynich.nu üzerinde, bu ortamdan erişilemedi, elle indirip `data/raw` altına koy, `transliteration.py` içine ayrıştırıcı ekle.
5. **Bölüm ve lehçe kırılımı.** Currier A ve B, beş yazıcı eli, çizim bölümleri (bitki, astronomi, banyo, reçete) için ayrı analiz. Folio aralıkları zaten pencere etiketinde.
6. **İkinci hat: char-level Transformer.** Yalnızca Voynich üzerinde küçük bir model eğit, sayfa embedding'leri çizim bölümlerine göre kümeleniyor mu bak. Kümeleniyorsa metin konuyla ilişkili. Kontrol: aynı testi satırları karıştırılmış metinde ve `selfcite` çıktısında tekrarla.

## Bilinen tuzaklar

- v101'de virgül "belirsiz boşluk". Varsayılan boşluk sayılıyor (`comma_is_space=True`). Tersini de koş, sonuç değişiyorsa raporla.
- `n_symbols` v101'de 70 civarı, sentetik evrende en çok 55. v101 görünümü yalnızca bu yüzden bile OOD çıkar. Ya üreteç alfabelerini genişlet ya da v101 için nadir glifleri birleştir.
- `eva_glyph` yalnızca ch, sh ve sehpalı gallows'ları birleştiriyor. `iin`, `ain` gibi diziler de tek glif olabilir, tartışmalı.
- Mahalanobis mesafeleri sınıf içi örneklerle (in-sample) kalibre ediliyor, biraz iyimser. Örnek sayısı feature sayısının çok üstünde olduğu için etkisi küçük.
- Veri küçük (yaklaşık 38 bin kelime, pencere başına 2000). Pencere boyutunu küçültmek pencere sayısını artırır ama entropi tahminlerini bozar.

## Veri kaynakları

- Takahashi EVA: `alephmembeth/voynich` (GitHub)
- Claston v101: `musyoku/voynich-transcription` (GitHub)
- İncil korpusu: `christos-c/bible-corpus` (GitHub)

Ham veri depoya girmez, `fetch` ile yeniden üretilir.
