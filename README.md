# Yb-169 HDR Episkleral Aplikatör Spesifikasyonu

Uveal melanom için, mevcut LDR plak brakiterapisinin yerine **tek anestezi seansında**
tamamlanan yüksek doz hızlı (HDR) episkleral brakiterapi aplikatörünün tasarım
spesifikasyonu. Kaynak olarak **iterbiyum-169** seçilmiştir; aplikatör mevcut COMS tipi
plakların şeklini örnek alır, skleraya dikilir ve HDR afterloader ile ameliyathanede
ışınlanır.

> Durum: **taslak v0.1**, tasarım dondurulmamıştır. Bütün sayısal değerler tasarım
> hedefidir; Monte Carlo ve ölçümle doğrulanmadan klinik anlam taşımaz.

## Belgeler

| No | Belge | İçerik |
|----|-------|--------|
| 00 | [Klinik amaç ve gereksinimler](spec/00-klinik-amac.md) | Neden HDR, neden tek seans, neden Yb-169, zorunlu gereksinimler |
| 01 | [Kaynak: Yb-169](spec/01-kaynak-yb169.md) | Fiziksel özellikler, kaynak ve kablo spesifikasyonu, tedarik |
| 02 | [Aplikatör tasarımı](spec/02-aplikator-tasarim.md) | Katmanlar, kanal geometrisi, boyut ailesi, giriş bloğu, malzeme, toleranslar |
| 03 | [Dozimetri ve planlama](spec/03-dozimetri-planlama.md) | Reçete, kısıtlar, doz hesabı yöntemi, plan kütüphanesi |
| 04 | [Kalite kontrol ve güvenlik](spec/04-qa-guvenlik.md) | Kabul testleri, hasta öncesi QA, acil durum, radyasyon korunması |
| 05 | [Tek seans iş akışı](spec/05-is-akisi.md) | Ameliyathanede dikimden çıkarıma adım adım akış |
| 06 | [Geliştirme yol haritası ve açık sorular](spec/06-yol-haritasi.md) | Fazlar, mevzuat, riskler, karar bekleyen konular |
| 07 | [Kanal topolojisi](spec/07-kanal-topolojisi.md) | Dupere 2021 Yb-169 halka aplikatörü ile karşılaştırma, spiral kanalın bükülme yarıçapı analizi |
| 08 | [Afterloader seçimi](spec/08-cihaz-secimi.md) | Cihaz proje ile alınacaksa seçim ölçütleri, adaylar, kabul testi |

## Çizimler

- [figures/plak-ailesi.svg](figures/plak-ailesi.svg): 12, 14, 16, 18, 20, 22 mm plakların üstten görünüş ve kesitleri tek sayfada
- `figures/plak-12mm.svg` … `figures/plak-22mm.svg`: her boy için ölçülü çizim ve özellik listesi
- [figures/kesit.svg](figures/kesit.svg): kanal eksenine dik kesit, katmanlar ve tümör ilişkisi, etiketli
- [figures/ustten.svg](figures/ustten.svg): 16 mm plak, üstten kanal ve bekleme pozisyonu yerleşimi, etiketli

Çizimler `python3 tools/draw_plaques.py` ile geometri kurallarından yeniden üretilir.

## Kaynakça

- Flynn RT ve ark. Efficient ¹⁶⁹Yb HDR brachytherapy source production using reactivation. Med Phys 2019. Varian GammaMed Plus dahil kapsül formatları, gereken aktivite ve üretim ekonomisi.
- Safaeipour E ve ark. Evaluation of dosimetric functions for a new ¹⁶⁹Yb HDR brachytherapy source. 2021. 0,9 mm kapsül formatında Yb-169 prototipi.

- Dupere JM, Munro JJ III, Medich DC. Shielded high dose rate ocular brachytherapy using Yb-169. Phys Med Biol 2021;66(12). DOI 10.1088/1361-6560/ac02d6. Yb-169 ve altın koruma seçimini bağımsız olarak destekleyen referans tasarım; halka geometrisi ve pelet dizisi kullanır.

## Araçlar

`tools/geometry.py` kanal yerleşimini, bekleme pozisyonlarını, sklera/apeks doz oranını ve
toplam bekleme süresini kaba olarak hesaplar. `tools/optimize.py` kanal düzenlerini (tek kiriş,
paralel kirişler, halka, eş merkezli halkalar) bekleme süresi optimizasyonu ile karşılaştırır.
Yalnızca tasarım kararlarını beslemek içindir.

```
python3 tools/geometry.py
pip install numpy scipy && python3 tools/optimize.py
```

## Tasarımın bir bakışta özeti

- Cihaz: kurumdaki **Varian GammaMedplus iX**, Yb-169 için uygun format. Kaynak 0,9 mm kapsül
  formatında Yb-169; Varian ile kaynak anlaşması ön şart, olmazsa belge 08'e göre cihaz alımı.
  Kablo bükülme yarıçapı 13 mm bildiriliyor; teyit edilirse kanallar sklera küresini tam izler.
- Plak çapı = tümör tabanının en geniş çapı + 4 mm. Kenar tam yükseklikte altın kalkanla kapalı.
- İç eğrilik yarıçapı 12,3 mm, çap ailesi 12 ile 22 mm, COMS ile aynı dikim tekniği.
- Skleradan dışa doğru: 0,85 mm polimer ara katman, kör uçlu paralel kanallar
  (bekleme ekseni skleradan 1,5 mm), 1,5 mm altın veya tungsten sırt koruması.
- Plağa tek giriş; içeride 3, 5 veya 7 paralel kör kanal. Kabloyla uygulanabilen düzenler
  arasında en iyi sklera/reçete oranını veren düzen budur (belge 07).
- Tek fraksiyon, hedef apeks dozu başlangıçta 22 Gy, faz I protokolüyle kademeli artış.
- Işınlama süresi 4 Ci kaynakla 5 mm tümörde yaklaşık 11 dakika.
