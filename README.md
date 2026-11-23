# voynich-lab

Uzun vadeli amaç Voynich el yazmasının kanıtlanabilir tercümesi. Bugünkü kod bunun ilk basamağı: metne anlam atamaz, onu üreten sürecin türünü simüle edilmiş hipotezlerle karşılaştırarak sınıflandırır. Anlam atayan kod, `CLAUDE.md` içindeki çözme kapısı açılmadan yazılmaz.

```bash
uv sync --extra dev --locked   # sürümler uv.lock ile sabit
uv run python -m voynich_lab.cli all   # sınıflandırma raporu
uv run python -m voynich_lab.cli abc   # her hipotez Voynich'e ne kadar yaklaşabiliyor
```

Çıktı: `results/report.md` ve `results/abc.md`.

Mimari, ilkeler, ilk bulgular ve yol haritası için `CLAUDE.md` dosyasına bak.
