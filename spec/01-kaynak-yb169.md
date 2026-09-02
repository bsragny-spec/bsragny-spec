# 01. Kaynak: Yb-169

## Fiziksel özellikler

| Özellik | Değer | Not |
|---------|-------|-----|
| Yarı ömür | 32,0 gün | Kaynak değişimi 1 ile 2 ayda bir |
| Bozunum | Elektron yakalama, Tm-169'a | Beta yok, kapsül içinde bremsstrahlung sorunu yok |
| Başlıca fotonlar | 50 ile 52 keV (Tm K x-ışını), 63 keV, 110 keV, 130 keV, 177 keV, 198 keV, 308 keV | 177 ve 198 keV çizgileri toplam verimin önemli kısmıdır |
| Ortalama foton enerjisi | ~93 keV | Spektrum iki bileşenli düşünülmelidir |
| Üretim | Yb-168 (n,γ) Yb-169 | Termal kesit yaklaşık 2300 barn, zenginleştirilmiş hedef şart |
| Ulaşılabilir spesifik aktivite | Birkaç bin Ci/g | Reaktör akısına ve ışınlama süresine bağlı |

## Koruma açısından anlamı

Düşük enerjili bileşen (50 ile 130 keV) altın veya tungstenin ilk yarım milimetresinde
tamamen kesilir. Geçen doz 177, 198 ve 308 keV çizgilerinden gelir. Bu nedenle:

- Sırt korumasında **ilk HVL ile sonraki HVL'ler farklıdır**; tek bir HVL değeriyle hesap yapılmaz.
- Tasarım hedefi: 1,5 mm altın veya tungsten ağır alaşım arkasında, plak sırtından 5 mm
  uzaklıkta doz, korumasız duruma göre **%10'un altında**. Bu hedef Monte Carlo ile
  doğrulanacak, gerekiyorsa kalınlık 2,0 mm'ye çıkarılacaktır.
- Ameliyathane koruma hesabı için 3 mm kurşun paravan yeterli kabul edilir; ölçümle teyit edilir.

## Cihaz: Varian GammaMedplus iX (kurumda mevcut)

Bütün HDR afterloader'lar yalnızca üreticinin kendi kaynak kablosu formatıyla çalışır ve kaynak
değişimi üretici servisi tarafından yapılır. Kurumdaki cihaz **GammaMedplus iX**'tir ve
Yb-169 için uygun formattadır. Yb-169 kaynağı bu kablo formatında üretilmeli ve cihazda
kullanımı için Varian ile anlaşma yapılmalıdır (belge 06, A2). Varian olumsuz yanıt verirse
proje bütçesiyle başka cihaz alınması belge 08'deki ölçütlere göre değerlendirilir.

GammaMedplus iX kaynak kablosu, açık kaynaklardan derlenen özellikler:

| Özellik | Değer | Durum |
|---------|-------|-------|
| Kapsül | 0,9 mm dış çap, yaklaşık 4,5 mm uzunluk | Yayımlanmış |
| Aktif Ir-192 peleti | 0,6 mm çap, 3,5 mm uzunluk | Yayımlanmış |
| Kablo | Örgülü çelik, uçtaki 200 mm ultra esnek | Ürün tanıtımı |
| **Minimum bükülme yarıçapı** | **13 mm** | Ürün tanıtımı; Varian teknik föyünden teyit edilecek (A2b) |
| Tedavi uzunluğu | Aplikatör + transfer tüpü toplam 1300 mm sabit | Yayımlanmış |
| Kanal | 3 veya 24 | Yayımlanmış |

13 mm değeri teyit edilirse plak kanalları 13,8 mm yarıçaplı sklera küresini **tam izleyebilir**
(belge 02); aksi halde 17 mm yaylı tasarım geçerlidir.

| Varian modeli | Kaynak formatı | Yb-169 uygunluğu |
|---------------|----------------|------------------|
| GammaMedplus iX, Bravos | 0,9 mm çaplı kapsül, 4,5 mm uzunluk, 0,6 mm × 3,5 mm aktif Ir-192 peleti, 0,9 mm çelik kablo | **Uygun.** Bu formatta Yb-169 prototipi üretilmiş ve dozimetrisi yayımlanmıştır (Safaeipour 2021: 0,9 mm dış çap, 4,73 mm uzunluk, 0,6 × 2,6 mm Yb₂O₃ seramik çekirdek, çift kapsül). Flynn 2019 de GammaMed Plus kapsülünü uzatılmış Yb-169 kapsülü için aday göstermiştir |
| VariSource iX | 0,59 mm nitinol tel içinde 0,34 mm çaplı, 5 mm uzun Ir-192 çizgi kaynak | **Uygun değil.** Aktif hacim 0,45 mm³; Yb-169 için 1 ile 4 mm³ gerekir (Flynn 2019). Bu formatta klinik aktivite elde edilemez |

Varian modelinin hangisi olduğu teyit edilmelidir. VariSource ise Yb-169 yolu kapalıdır ve
proje Ir-192 ile bunkerde tek seans (belge 06, A8) senaryosuna döner.

## Kaynak spesifikasyonu (tedarikçiye verilecek)

| Parametre | İstenen | Gerekçe |
|-----------|---------|---------|
| Format | Varian GammaMedplus / Bravos kaynak kablosu ile birebir aynı: 0,9 mm kapsül, ≤ 4,8 mm uzunluk, 0,9 mm çelik kablo, aynı kablo uzunluğu ve uç bağlantısı | Cihaz değişikliği yapılmaz |
| Aktif çekirdek | Yb₂O₃ seramik, 0,6 mm çap, 2,6 ile 3,5 mm uzunluk | Safaeipour 2021 prototipi ile aynı sınıf |
| Kapsül malzemesi | Titanyum iç, 316L çelik dış, çift kapsül, kaynaklı | Standart HDR kapsül teknolojisi |
| Kablo bükülme yarıçapı | Varian'ın kendi Ir-192 kablosu için verdiği değerle aynı; tasarım değeri **17 mm** | Plak kanalları bu yarıçapla yapılır (belge 02) |
| Teslimde aktivite | 8 ile 12 Ci | 2 Ci'ye düşene kadar kullanım, yaklaşık 8 ile 10 hafta. Flynn 2019'un 10 Ci Ir-192 eşdeğeri için önerdiği 27 Ci gerekmez; göz mesafeleri kısadır |
| Kullanım alt sınırı | 2 Ci | 8 mm tümörde 25 Gy için ~40 dk, G2 sınırı |
| Sızdırmazlık | ISO 9978 silme testi, ISO 2919 sınıflandırması | Kapalı kaynak mevzuatı |
| Belge | Aktivite sertifikası, hava kerma şiddeti, kapsül çizimi, kablo mekanik testi | TG-43 parametreleri ve TPS için |

Kablo esnekliği tasarım serbestliği **değildir**: kaynak Varian kablo formatında olmak zorunda
olduğundan bükülme yarıçapı Varian'ın Ir-192 kablosu için verdiği değerle sınırlıdır. Bu
kısıt aplikatör kanal yarıçapına yansıtılmıştır (belge 02).

## Referanslar

- Flynn RT ve ark. Efficient ¹⁶⁹Yb high-dose-rate brachytherapy source production using
  reactivation. Med Phys 2019. Kapsül formatları, aktivite ve üretim ekonomisi.
- Safaeipour E ve ark. Evaluation of dosimetric functions for a new ¹⁶⁹Yb HDR brachytherapy
  source. 2021. 0,9 mm kapsül formatında prototip, Λ = 1,21 cGy h⁻¹ U⁻¹.
- Dupere JM ve ark. Shielded HDR ocular brachytherapy using Yb-169. Phys Med Biol 2021 (belge 07).

## Kalibrasyon sorunu

Yb-169 için birincil standart laboratuvarlarında yerleşik hava kerma şiddeti kalibrasyonu
**yoktur**. Kuyu tipi iyon odası kalibrasyonu için iki yol:

1. Tedarikçiden izlenebilir sertifika ve kuyu odası için enerjiye özgü interpolasyon
   (I-125/Pd-103 ile Ir-192 kalibrasyon faktörleri arasında spektrum ağırlıklı interpolasyon).
2. Bağımsız doğrulama: kalibre edilmiş iyon odası ile havada mesafe ölçümü ve Monte Carlo
   hesaplanan spektrum düzeltmesi.

Bu konu belge 06'da açık soru olarak listelenmiştir; klinik kullanım öncesi çözülmüş olmalıdır.

## Tedarik

- Dupere ve arkadaşlarının 2021 çalışmasında (belge 07) Yb-169 HDR kaynağı yazarlardan birinin
  bağlı olduğu kaynak üreticisiyle ilişkilidir; tedarik görüşmelerinde ilk temas adayı olarak
  değerlendirilecek, teyit edilecek.

- Türkiye'de yeterli akıya sahip araştırma reaktörü bulunmadığından hedef ışınlaması yurt
  dışında yapılır; kapsülleme kapalı kaynak üreticisi tarafından yapılır. Flynn 2019 verisi:
  %82 zenginleştirilmiş Yb-168 hedef, 10¹⁴ n/cm²/s akıda 30 günde doyuma yakın aktivite;
  3 mm³ ve üzeri çekirdekler yeniden aktive edilebilir, yıllık hedef malzeme ihtiyacını düşürür.
- Kaynak kablosunun Varian formatında üretimi ve cihazda kullanımı için üç yol: Varian'ın
  kendisinin üretmesi, Varian onayıyla üçüncü taraf üretimi, veya araştırma amaçlı kullanım
  izniyle üçüncü taraf üretimi. Hangisi olursa olsun Varian ile yazılı anlaşma gerekir;
  cihaz garantisi, servis ve yazılım (BrachyVision kaynak kütüphanesi) bu anlaşmaya bağlıdır.
- Kısa yarı ömür nedeniyle **üretim, taşıma, kalibrasyon ve ilk hasta** arasındaki süre
  planlanmalı; taşıma haftası bile aktivitenin %14'ünü götürür.
- Yılda 6 ile 8 kaynak değişimi; maliyet modeline bu girilmelidir.
- Bozunmuş kaynaklar 1 yıl sonra muaf düzeye iner, iade veya kurum içi bekletme planlanır.
