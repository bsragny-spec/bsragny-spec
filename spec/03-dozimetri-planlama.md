# 03. Dozimetri ve planlama

## Reçete noktası ve tek fraksiyon dozu

Reçete noktası COMS geleneğiyle aynıdır: merkez eksende, iç sklera yüzeyinden tümör apeks
yüksekliği kadar içeride; apeks 5 mm'den alçaksa 5 mm.

LDR plağın biyolojik eşdeğeri lineer kuadratik modelle tek fraksiyona çevrilmiştir. Varsayımlar:
LDR 85 Gy apeks, ortalama doz hızı 0,7 Gy/saat, onarım yarı zamanı 1,5 saat, tümör α/β 10 Gy,
geç yanıt veren doku α/β 3 Gy. Sonuçlar yaklaşıktır ve radyobiyoloji danışmanınca gözden
geçirilmelidir.

| Nokta | LDR plak, tipik | LDR BED | Tek fraksiyon eşdeğeri |
|-------|-----------------|---------|------------------------|
| Apeks, tümör (α/β 10) | 85 Gy | ~110 Gy₁₀ | ~28 Gy |
| Apeks, geç doku (α/β 3) | 85 Gy | ~170 Gy₃ | ~21 Gy |
| Sklera, plak altı (α/β 3) | 250 Gy | ~950 Gy₃ | ~52 Gy |

### Faz I doz kademesi

| Kademe | Apeks dozu | Sklera üst sınırı | Hasta sayısı |
|--------|-----------|-------------------|--------------|
| 1 | 20 Gy | 55 Gy | 3 |
| 2 | 22 Gy | 60 Gy | 3 ile 6 |
| 3 | 25 Gy | 65 Gy | 3 ile 6 |

Kademe geçişi 6 aylık akut toksisite penceresine göre karar verilir. Sklera sınırı aşılıyorsa
apeks dozu düşürülür, kademe atlanmaz. 8 mm üzeri tümörlerde sklera sınırı apeks dozunu
kısıtlar; bu hastalar ilk iki kademede alınmaz.

### Kısıtlar (tek fraksiyon, izlenecek noktalar)

| Yapı | Kayıt noktası | Başlangıç hedefi |
|------|---------------|------------------|
| Sklera | Bekleme pozisyonu altı, dış sklera yüzeyi | ≤ 55 ile 65 Gy, kademeye göre |
| Makula | Fovea merkezi | Mümkün olan en düşük; 10 Gy üstü retinopati riski olarak kaydedilir |
| Optik disk | Disk merkezi | Aynı |
| Lens | Arka kapsül merkezi | ≤ 5 Gy hedef |
| Karşı göz | Lens | ≤ 0,1 Gy; sırt korumasının doğrulaması |
| Orbita kemiği, plak arkası | Sırt yüzeyinden 5 mm | Korumasızın ≤ %10'u |

Makula ve optik disk için tek fraksiyon eşik değerleri literatürde yoktur; ilk hastalarda
kaydedilir, ikinci yılda toksisite verisiyle sınır oluşturulur.

## Doz hesabı yöntemi

### TG-43 yetmez

Plak sırtı, PEEK ek parça ve gözün heterojen olmayan ama sonlu geometrisi nedeniyle su içinde
nokta kaynak varsayımı hatalıdır. Yb-169'un düşük enerjili bileşeni altında saçılma eksikliği
etkisi belirgindir. Yöntem:

1. **Kaynak TG-43 parametreleri**: kapsül çizimi ile Monte Carlo (egs_brachy veya MCNP);
   Λ, g(r), F(r,θ). Tedarikçi verisiyle karşılaştırılır.
2. **Aplikatör içi Monte Carlo**: her plak boyutu için tam geometri, sklera ve göz küresi
   modeli, kabul edilen tümör yükseklikleri için doz haritaları. Bu haritalar TPS'e
   girilen düzeltme faktörlerinin ve plan kütüphanesinin kaynağıdır.
3. **Ölçüm doğrulaması**: katı su fantomunda plak kesitine uygun oyuk, EBT3 film sklera
   düzleminde ve 3, 5, 8 mm derinliklerde; ayrıca plak arkasında koruma faktörü ölçümü.
   Kabul: MC ile film farkı tümör ekseninde ≤ %5, sklera düzleminde ≤ %8.
4. **Kaynak değişiminde**: yeni kaynak aynı modelse yalnızca aktivite güncellenir; kapsül
   değişirse 1 ile 3 tekrarlanır.

### Planlama sistemi

- Aplikatör, TPS'te **sabit geometrili aplikatör** olarak tanımlanır; kanal koordinatları ve
  kör uç ofsetleri seri numarasına göre kütüphaneden gelir. Hasta BT'si gerekmez.
- Model tabanlı doz hesabı (Acuros BV, ACE veya eşdeğeri) varsa plak malzemesi tanımlanır;
  yoksa TG-43 sonucu MC türetilmiş düzeltme tablosuyla ölçeklenir.
- **Plan kütüphanesi**: her plak boyutu için apeks yüksekliği 2'den 10 mm'ye 1 mm adımlarla
  önceden optimize edilmiş bekleme süresi setleri. Ameliyat sabahı ultrason ölçümüyle plan
  seçilir; hasta özel değişiklik yalnızca bekleme süresi ölçeklemesidir.
- Optimizasyon amacı: apeks noktasında reçete, tümör tabanı boyunca sklera düzleminde
  homojenlik, giriş bloğu tarafındaki ilk bekleme pozisyonlarının ağırlığını sınırlama.

## Beklenen sklera/apeks oranları

`tools/geometry.py` çıktısı, bekleme ekseni 1,5 mm, eşit bekleme süreleri, nokta kaynak:

| Çap | h = 3 mm | h = 5 mm | h = 8 mm | h = 10 mm |
|-----|---------|---------|---------|----------|
| 12 mm | 3,3 | 5,7 | 10,9 | 15,4 |
| 16 mm | 2,5 | 4,1 | 7,4 | 10,3 |
| 20 mm | 2,1 | 3,1 | 5,2 | 7,1 |

Sonuç: 25 Gy apeks reçetesi ile 16 mm plakta 5 mm tümörde sklera yaklaşık 100 Gy'ye çıkar.
Bu, tablodaki 55 ile 65 Gy sklera sınırının **üzerindedir**. Buradan çıkan tasarım sonuçları:

- Plak seçim kuralı **tümör tabanı en geniş çapı + 4 mm** olarak sabitlenmiştir (belge 02).
  `tools/optimize.py` sonuçlarına göre bu kural ve bekleme optimizasyonu birlikte sklera
  oranını eşit süreli küçük plağa göre %20 ile 30 düşürür.
- Bekleme optimizasyonu (belge 07) kenar pozisyonlarını güçlendirip merkezi zayıflatarak
  oranı 16 mm plakta 5,2'den 4,1'e indirir.
- Buna rağmen 5 mm üzeri tümörlerde sklera sınırı reçeteyi belirleyecektir. Faz I'de
  reçete "apeks 20 ile 25 Gy **veya** sklera sınırı, hangisi önce" olarak yazılır.
- LDR'de sklera 250 ile 400 Gy'yi tolere ediyor olması, tek fraksiyonda 100 Gy'nin
  tolere edileceği anlamına gelmez; LQ modeli 400 Gy LDR için bile ~65 Gy tek fraksiyon verir.

Bu bölüm projenin en kritik açık noktasıdır ve belge 06'da yer alır.

## Işınlama süresi

16 mm plak, 25 Gy apeks, 1 Ci Yb-169 için suda 1 cm'de 18 Gy/saat varsayımıyla:

| Apeks yüksekliği | 8 Ci | 4 Ci | 2 Ci |
|------------------|------|------|------|
| 3 mm | 3,5 dk | 7 dk | 14 dk |
| 5 mm | 5,6 dk | 11 dk | 22 dk |
| 8 mm | 10 dk | 20 dk | 40 dk |

Gereksinim G2 kaynak aktivitesi 2 Ci'nin altına inmeden karşılanır. Transit doz, kısa
süreler ve düşük enerji nedeniyle ihmal edilebilir düzeydedir; MC ile teyit edilir.
