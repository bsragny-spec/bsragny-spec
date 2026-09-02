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

## Kaynak spesifikasyonu (tedarikçiye verilecek)

| Parametre | İstenen | Gerekçe |
|-----------|---------|---------|
| Kapsül dış çapı | ≤ 0,9 mm, tercihen 0,7 mm | Kanal iç çapı ve bükülme yarıçapı |
| Aktif uzunluk | ≤ 3,5 mm | Sklera eğrisinde konum belirsizliği |
| Kapsül malzemesi | Titanyum veya paslanmaz çelik, kaynaklı | Standart HDR kapsül teknolojisi |
| Kablo | Cihaz üreticisinin sürücü mekanizmasına uyumlu; **minimum bükülme yarıçapı ≤ 12 mm** | Plak kanalı 13,8 mm yarıçaplı küre kabuğunu izler |
| Teslimde aktivite | 6 ile 10 Ci | 2 Ci'ye düşene kadar kullanım, yaklaşık 6 ile 8 hafta |
| Kullanım alt sınırı | 2 Ci | 8 mm tümörde 25 Gy için ~40 dk, G2 sınırı |
| Sızdırmazlık | ISO 9978 silme testi, ISO 2919 sınıflandırması | Kapalı kaynak mevzuatı |
| Belge | Aktivite sertifikası, hava kerma şiddeti, kapsül çizimi, kablo mekanik testi | TG-43 parametreleri ve TPS için |

Kaynak özel üretim olacağı için **kablo esnekliği tasarım serbestliğidir**: standart Ir-192
kablosundan daha ince ve esnek bir kablo istenmeli, bükülme yarıçapı kanal geometrisine göre
belirlenmelidir. Bu, iridyum kablolarının çoğu için sorun olan sklera eğrisi kısıtını ortadan
kaldırır.

## Kalibrasyon sorunu

Yb-169 için birincil standart laboratuvarlarında yerleşik hava kerma şiddeti kalibrasyonu
**yoktur**. Kuyu tipi iyon odası kalibrasyonu için iki yol:

1. Tedarikçiden izlenebilir sertifika ve kuyu odası için enerjiye özgü interpolasyon
   (I-125/Pd-103 ile Ir-192 kalibrasyon faktörleri arasında spektrum ağırlıklı interpolasyon).
2. Bağımsız doğrulama: kalibre edilmiş iyon odası ile havada mesafe ölçümü ve Monte Carlo
   hesaplanan spektrum düzeltmesi.

Bu konu belge 06'da açık soru olarak listelenmiştir; klinik kullanım öncesi çözülmüş olmalıdır.

## Tedarik

- Türkiye'de yeterli akıya sahip araştırma reaktörü bulunmadığından hedef ışınlaması yurt
  dışında yapılır; kapsülleme kapalı kaynak üreticisi tarafından yapılır.
- Kısa yarı ömür nedeniyle **üretim, taşıma, kalibrasyon ve ilk hasta** arasındaki süre
  planlanmalı; taşıma haftası bile aktivitenin %14'ünü götürür.
- Yılda 6 ile 8 kaynak değişimi; maliyet modeline bu girilmelidir.
- Bozunmuş kaynaklar 1 yıl sonra muaf düzeye iner, iade veya kurum içi bekletme planlanır.
