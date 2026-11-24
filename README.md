# voynich-lab

Amaç: Voynich el yazmasının (Beinecke MS 408) metninin ne tür bir süreçten çıktığını ve bir doğal dili doğrudan yazıp yazmadığını, tek komutla yeniden üretilebilen ölçümlerle göstermek. Kod metne anlam atamaz: metni simüle edilmiş hipotezlerle ve gerçek dil metinleriyle karşılaştırır. Tercüme denemesi `CLAUDE.md` içindeki çözme kapısının arkasındadır; kapı açılmadan anlam atayan kod yazılmaz.

```bash
uv sync --extra dev --locked   # sürümler uv.lock ile sabit
uv run python -m voynich_lab.cli all   # sınıflandırma raporu
uv run python -m voynich_lab.cli abc --rebuild   # her hipotez Voynich'e ne kadar yaklaşabiliyor
uv run python -m voynich_lab.cli search          # yönlendirilmiş arama, taze örnekle ölçüm
uv run python -m voynich_lab.cli manuscripts --rebuild --ms-per-class 2000   # el yazması düzeyi, asıl hüküm
uv run python -m voynich_lab.cli checks          # hattın kendi sonuçlarını sınayan deneyler
```

Çıktı: `results/` altında `report.md`, `abc.md`, `search.md`, `manuscripts.md`, `checks.md`. Güncel hüküm `CLAUDE.md` içindeki en son "bulgular" bölümündedir.

Mimari, ilkeler, ilk bulgular ve yol haritası için `CLAUDE.md` dosyasına bak.
