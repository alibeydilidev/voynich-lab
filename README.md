# Voynich için dört sınav

Beinecke MS 408 · ölçüm notu · 24 Kasım 2026 · Ali Beydili ve Claude

Voynich el yazmasının metni bir dili doğrudan yazmıyor. Bunu dört ölçümle gösteriyoruz ve bilinen açıklamaların bu ölçümlerde nerede kaldığını yan yana koyuyoruz.

Bu bir çözüm değil. Elimizdeki şey, ileride öne sürülecek her çözümün, her şifre önerisinin ve her "anlamsız metin" modelinin geçmesi gereken dört sınav. Hepsi aynı veriden, bu depodaki kodla yeniden üretiliyor ([nasıl](#yeniden-üretmek)).

*English summary: [at the end](#english-summary).*

## Dört ölçüm

Her ölçümde model metnin ilk 16 bin kelimesinden öğrenir, sayı hiç bakılmamış sonraki 16 bin kelimeden gelir. Voynich için beş ayrı okuma (transliterasyon) kullanıldı; aralıklar bu beş okumanın en düşük ve en yüksek değeridir.

### Sınav 1: kelimeler bir sözlükten gelmiyor

Bir metnin harf dizilişi alışkanlıklarını öğrenip aynı sayıda uydurma kelime üretirseniz, gerçek bir dilde uydurmaların çoğu sözlükte yoktur. Bu yüzden uydurma metin, gerçeğinden çok daha fazla farklı kelime içerir. Voynich'te fark yok: harf dizilişine uyan her şey zaten yazılmış gibi.

| Metin | Uydurma / gerçek farklı kelime | Yeni kelime oranı |
|---|---|---|
| **Voynich, beş okuma** | **0.96 ila 1.06** | **0.84 ila 0.95** |
| 22 doğal dil | 1.56 ila 3.34 | 1.92 ila 5.29 |
| Aynı diller, seslisiz yazılmış (19 dil) | 1.39 ila 1.79 | 0.97 ila 2.59 |
| Eski metinler (5 metin: 15. yüzyıldan dört eser ve Plinius) | 1.74 ila 2.36 | 2.93 ila 4.53 |

1 dolayı: sözlük kısıtı görünmüyor. 1'in belirgin üstü: kelimeler dar bir sözlükten geliyor.

### Sınav 2: bir kelime, sonraki kelimeyi tahmin ettirmiyor

Her dilde kelimelerin sırası bilgi taşır: "ve" sözcüğünden sonra ne geleceği rastgele değildir. Ölçü, önceki kelimeyi bilmenin sonraki kelimeyi tahminde kaç bit kazandırdığıdır; aynı ölçüm kelimeleri satır içinde karıştırılmış metinde tekrarlanıp fark alınır.

| Metin | Kelime sırasının taşıdığı bilgi (bit/kelime) |
|---|---|
| **Voynich, beş okuma** | **-0.008 ila +0.020** |
| 22 doğal dil | +0.164 ila +0.961 |
| Eski metinler (aynı 5 metin; tarif ve bitki kitabı dahil) | +0.181 ila +0.833 |

En zayıf doğal dil metni bile Voynich'in en yüksek değerinin sekiz katını veriyor. Tarif ve ilaç metinleri bunu açıklamıyor: o türde sıra bilgisi düşük değil, yüksek.

### Sınav 3: bağ yalnız kelimelerin birleştiği yerde

Kelimeler yine de birbirinden bağımsız değil. Bir kelimenin son harfi, sonraki kelimenin ilk harfini tahmin ettiriyor. En bilinen örnek: `y` ile biten kelimeden sonra `q` ile başlayan kelime. Paragraf metnindeki 28.901 komşu kelime çiftinde bu birleşme 3.296 kez geçiyor; iki harf birbirinden bağımsız olsaydı yaklaşık 1.880 kez geçerdi.

Folyo 83v'den bir satır (EVA yazımıyla):

```
solkeedy qokeedy qokeedy saiin okaiin chedy qokeedy qolkeedy
```

| Metin | Kelime sırası | Son harf -> sonraki ilk harf (bit) |
|---|---|---|
| **Voynich, beş okuma** | **sıfıra yakın** | **+0.166 ila +0.252** |
| 22 doğal dil | büyük | +0.004 ila +0.161 |
| Eski metinler (aynı 5 metin) | büyük | +0.013 ila +0.101 |

Tek başına bu sayı dillerden keskin ayrılmıyor (en yüksek dil +0.161). Ayırıcı olan ikisinin birlikteliği: kelime sırası sıfır, uç bağı büyük. Karşılaştırdığımız hiçbir dil ya da dönem metni bu bileşimi vermiyor. Satır başı ve satır sonu alışkanlıkları sonucu değiştirmiyor; yalnız aynı satırdaki komşular sayıldı.

### Sınav 4: yayımlanmış şifre önerisi ikinci sınavı geçiyor, ötekilerde kalıyor

Naibbe şifresi (Greshko, 2025) gerçek Latinceyi elle uygulanabilen bir yöntemle Voynich görünümlü metne çeviriyor; anahtarı bilen geri okuyor. Yazarın yayımladığı örnek metni aynı sınavlardan geçirdik.

| Ölçü | Naibbe örneği | Voynich |
|---|---|---|
| Kelime sırası (bit/kelime) | +0.009 | -0.007 |
| Yeni kelime oranı (sınav 1) | 1.89 ila 1.99 | 0.86 ila 0.95 |
| Yalnız bir kez geçen kelimelerin payı | 0.51 | 0.68 |
| Son harf -> sonraki ilk harf (bit) | +0.004 | +0.166 ila +0.175 |

Bu tablodaki Voynich değerleri, Naibbe örneğiyle aynı harf tanımını kullanan iki okumadan (EVA).

Aynı örnek anahtarıyla çözülünce kelime sırası bilgisi geri geliyor: +0.396 bit. İki sonuç çıkıyor. Birincisi, içinde gerçek dil olan bir metin ikinci sınavda Voynich gibi görünebiliyor; yani "kelime sırası yok" bulgusu tek başına "anlam yok" demek değil. İkincisi, doğru bir anahtar bulunursa bu ölçümle sınanabilir.

## Karne: bilinen açıklamalar nerede kalıyor

| Aday | 1 · Sözlük yok | 2 · Sıra yok | 3 · Uç bağı var |
|---|---|---|---|
| **Voynich** | evet | evet | evet |
| Alfabeyle yazılmış doğal dil (22 dil, 5 dönem metni) | kaldı | kaldı | kaldı |
| Seslileri atılarak yazılmış doğal dil | kaldı | kaldı | kaldı |
| Naibbe şifresi, yayımlanan örnek | kaldı | geçti | kaldı |
| Kendinden kopyalama üreteci* | örneğe göre değişiyor | geçti | kaldı |
| Tablo ve ızgara yöntemi* | kaldı | kaldı | kaldı |
| Rastgele harf otomatı, kelimeler arası bağla* | geçti | geçti | bağ ayarı açıkken geçti |

\* Bu üçü literatürdeki fikirlerin bizim yazdığımız sürümleridir, özgün yazarların kodu değildir.

Son satır yanıltmasın: otomat üç sınavı geçiyor ama Voynich'i üretmiyor. Metnin genel istatistik görünüşünü 33 ölçüyle karşılaştırdığımızda en iyi otomat örnekleri Voynich'e 5.7 ila 7.4 birim uzakta kalıyor; Voynich'in kendi iki yarısı birbirine en çok 1.7 birim uzak. Denediğimiz dokuz açıklamanın hiçbiri bu uzaklığı kapatamadı.

## Bu not ne söylemiyor

- Metnin anlamlı mı anlamsız mı olduğuna karar vermiyor. Ölçümler iki ihtimalle de bağdaşıyor: anlam taşımayan bir üretim ya da anahtarla geri okunan bir şifre.
- Tercüme içermiyor ve tercümeye giden bir yol önermiyor. Anahtarsız denediğimiz bir arama, cevabını bildiğimiz Naibbe örneğinde bile işe yaramadı; bu yüzden Voynich'e uygulanmadı.
- "Hiçbir dil böyle davranmaz" demiyor. Karşılaştırma 22 modern İncil çevirisi, 15. yüzyıldan dört eser (Latince, İtalyanca, İspanyolca) ve Plinius'un bitki kitabıyla yapıldı. İbranice, Arapça ve Türkçe için dönem metni yok.
- Naibbe için tek bir örnek ve tek bir düz metin ölçüldü; şifrenin başka ayarları denenmedi.

## Neyi biz bulmadık

İkinci sınavın sonucu 2011'den beri biliniyor (Reddy ve Knight) ve Ağustos 2026'da tarif ve bitki metinleriyle karşılaştırılarak yeniden gösterildi (Rozanova ve Temerev). Üçüncü sınavın sonucu da aynı 2026 makalesinde var. Bizimkiler bağımsız doğrulama: farklı bir hesap yöntemi, 22 dil, beş okuma, aynı sonuç.

Birinci sınav bu hâliyle okuduğumuz on üç kaynakta yok; en yakın öncülü Timm'in 2014'teki sözel gözlemi. Yine de "ilk kez" demiyoruz, çünkü okuyamadıklarımız var: Timm ve Schinner 2020, Greshko'nun makalesinin kendisi, Stolfi'nin kelime grameri, Schinner 2007, Landini 2001 ve Voynich Ninja forumundaki tartışmalar.

## Yeniden üretmek

Gerekenler: [uv](https://docs.astral.sh/uv/) ve internet bağlantısı (ham veri ilk koşuda indirilir, depoya girmez). Python 3.12 ve bütün paket sürümleri `uv.lock` ile sabittir.

```bash
uv sync --extra dev --locked
uv run --locked python -m voynich_lab.cli all      # veriyi indirir, sentetik tabloyu kurar (ilk koşuda birkaç dakika)
uv run --locked python -m voynich_lab.cli checks   # dört sınav -> results/checks.md (birkaç dakika)
uv run --locked pytest -q
```

Tablolardaki sayılar `results/checks.md` dosyasındadır; karnenin altındaki uzaklık değerleri `results/manuscripts.md` dosyasından gelir. Aynı komut iki kez koşulduğunda dosyalar bayt bayt aynı çıkar. Depodaki `results/` klasörü bizim koşumuzun çıktısıdır; kendi koşunuzla karşılaştırmak için `git diff results/` yeter.

Üçüncü sınavdaki `y` -> `q` sayımı rapor dosyalarında yoktur; veri indirildikten sonra şu birkaç satırla yeniden üretilir (çıktı: `28901 3296 1880`):

```bash
uv run --locked python - <<'EOF'
from collections import Counter
from voynich_lab.transliteration import load_views

pairs = yq = 0
last, first = Counter(), Counter()
for line in load_views("data/raw")["eva_basic"]:
    for a, b in zip(line.words, line.words[1:]):
        pairs += 1
        last[a[-1]] += 1
        first[b[0]] += 1
        yq += a[-1] == "y" and b[0] == "q"
print(pairs, yq, round(last["y"] * first["q"] / pairs))
EOF
```

Dokuz üretecin Voynich'e uzaklığını veren tam zincir daha uzundur (yaklaşık 50 dakika):

```bash
uv run --locked python -m voynich_lab.cli all
uv run --locked python -m voynich_lab.cli manuscripts --rebuild --ms-per-class 2000
uv run --locked python -m voynich_lab.cli abc --rebuild
uv run --locked python -m voynich_lab.cli search
uv run --locked python -m voynich_lab.cli checks
```

## Depoda ne var

| Yer | İçerik |
|---|---|
| `src/voynich_lab/` | Kod: transliterasyon okuyucuları, dokuz üreteç, 33 ölçü, sınamalar (`checks.py`) |
| `tests/` | 53 test |
| `results/` | Koşuların çıktısı: `checks.md` (dört sınav), `manuscripts.md` (üreteçlerin uzaklığı), `report.md`, `abc.md`, `search.md` |
| `CLAUDE.md` | Laboratuvar defteri: ilkeler, mimari ve v0'dan v0.18'e bütün denemeler; tutmayan öngörüler ve geri alınan hükümler dahil |

Kod metne anlam atamaz. Tercüme denemesi `CLAUDE.md` içindeki "çözme kapısı"nın arkasındadır; kapı açılmadan anlam atayan kod yazılmaz.

## Veri kaynakları

Ham veri depoda durmaz; `cli fetch` (ya da `cli all`) aşağıdaki yerlerden indirir.

- Voynich transliterasyonları: Takahashi EVA ([alephmembeth/voynich](https://github.com/alephmembeth/voynich)); Zandbergen ve Landini, IVTFF sürüm 3b ([voynich.nu](https://www.voynich.nu/data/ZL3b-n.txt)); Claston v101 ([musyoku/voynich-transcription](https://github.com/musyoku/voynich-transcription)).
- 22 dilde paralel İncil: [christos-c/bible-corpus](https://github.com/christos-c/bible-corpus).
- Dönem ve tür metinleri: Wikisource ve The Latin Library (Kempis, Alberti, Rojas, Cennini, Plinius, Celsus, Apicius, Cato, Macer Floridus). Ayrıntı `CLAUDE.md`, "Veri kaynakları".
- Naibbe şifresi örnek metni ve çözümü: [greshko/naibbe-cipher](https://github.com/greshko/naibbe-cipher). Bu veriyi kullanan her yayın şu makaleyi kaynak göstermek zorundadır: Greshko, M. A. (2025). The Naibbe cipher. *Cryptologia*. [doi:10.1080/01611194.2025.2566408](https://doi.org/10.1080/01611194.2025.2566408)

## Kaynaklar

- Reddy, S. ve Knight, K. (2011). What we know about the Voynich manuscript. ACL LaTeCH atölyesi. [PDF](https://aclanthology.org/W11-1511.pdf)
- Rozanova ve Temerev (2026). A Glyph Is Not a Letter, a Token Is Not a Word, a Space Is Not a Space. [arXiv:2608.17096](https://arxiv.org/abs/2608.17096)
- Greshko, M. A. (2025). The Naibbe cipher. *Cryptologia*. [doi:10.1080/01611194.2025.2566408](https://doi.org/10.1080/01611194.2025.2566408)
- Timm, T. (2014). How the Voynich manuscript was created. [arXiv:1407.6639](https://arxiv.org/abs/1407.6639)

Okunan on üç kaynağın tamamı ve her birinden ne alındığı: `CLAUDE.md`, "v0.15 bulguları".

## Kim ne yaptı

Soruyu soran, projeyi yürüten ve kararları veren: Ali Beydili. Ölçümleri yapan, kodu ve bu notu yazan: Claude (Anthropic'in yapay zekâ modeli). Dışarıya kurulan cümle "Claude çözdü" değil, "Claude şunu ölçtü" biçimindedir.

## English summary

**Four tests for the Voynich manuscript.** This is not a decipherment. It is a set of four reproducible measurements that any proposed solution, cipher or "meaningless text" model has to pass. Each model is fit on the first 16,000 words and scored on the unseen next 16,000; ranges are over five transliteration views.

1. **No lexicon.** Sampling the same number of words from a within-word glyph chain learned on the text yields about as many distinct words as the real text (ratio 0.96 to 1.06). In 22 natural languages the ratio is 1.56 to 3.34: most strings that fit a language's spelling patterns are not words of that language.
2. **No word order.** Knowing the previous word gains -0.008 to +0.020 bits per word over within-line shuffling. The 22 languages give +0.164 to +0.961; five older texts, including recipe and herbal prose, give +0.181 to +0.833.
3. **Coupling only at word joins.** The last glyph of a word predicts the first glyph of the next (+0.166 to +0.252 bits; languages +0.004 to +0.161). Zero word order together with strong edge coupling appears in none of the comparison texts.
4. **A published cipher passes test 2 and fails the others.** The Naibbe cipher sample (Greshko 2025), which encodes real Latin, shows near-zero word order (+0.009) like Voynich, but a more closed vocabulary and no edge coupling (+0.004). Decoded with its key, word order returns (+0.396 bits).

What this does not show: whether the text is meaningful. The measurements are compatible both with meaningless generation and with a key-invertible cipher. None of the nine generators we wrote reproduces the manuscript's overall statistical profile (best distance 5.7 to 7.4; the manuscript's own halves differ by at most 1.7).

Tests 2 and 3 replicate published results (Reddy and Knight 2011; Rozanova and Temerev 2026). Test 1 was not found in this form in the thirteen sources we read; we do not claim priority, since several relevant sources remain unread (listed above).

The lab notebook (`CLAUDE.md`) and the result files are in Turkish. Measurements, code and this note were produced by Claude (Anthropic's AI model); the project was directed by Ali Beydili.
