# 09. GammaMedplus iX ile kanal sisteminin uyumu

Kanal sistemi, standart interstisyel HDR kateter mantığıyla aynıdır: kör uçlu, sabit uzunluklu,
kanal başına bir transfer tüpü. Bu yüzden kurumdaki GammaMedplus iX ile **mevcut Ir-192 kaynağı
kullanılarak bugün test edilebilir**. Yb-169 sorusu (A2) kanal sisteminden bağımsızdır.

## Uyum maddeleri

| Konu | Cihazın şartı | Tasarım | Durum |
|------|---------------|---------|-------|
| Kanal sayısı | 3/24 iX modelinde 3 veya 24 kanal | Her plakta 3 kanal | 3 kanallı yapılandırma bütün plak ailesi için yeterlidir |
| Kaynak kapsülü | 0,9 mm dış çap, yaklaşık 4,5 mm uzunluk, örgülü kablo | Kanal iç çapı 1,2 mm | Sert kapsülün 13,8 mm yaylı kanaldaki kiriş sapması 4,5² / (8 × 13,8) = 0,18 mm; 1,2 mm iç çap geçer ama pay 0,15 mm'dir. **Öneri: iç çap 1,3 mm**, sürtünme payı için |
| Bükülme yarıçapı | Bildirilen minimum 13 mm (teyit edilecek, A2b) | Kanal yayı 13,8 mm | Sınıra yakın; kabul testi sahte kaynak turu ile (20 tekrar). Olumsuzsa 17 mm yaylı yedek tasarım |
| Kör uç ve ilk pozisyon | Kaynak kanalın kapalı ucuna kadar gider; pozisyonlar uçtan geriye doğru tanımlanır | Kör uçta 2,0 mm ölü boşluk varsayımı | Gerçek değer = kapsül ucu ile aktif merkez arası + kateter uç kalınlığı; **otoradyografi ile ölçülür**, TPS'e girilir |
| Tedavi uzunluğu | Aplikatör + transfer tüpü toplamı 1300 mm sabit | Kateter 30 ile 50 mm, transfer tüpü buna göre kısaltılmış standart tüp | Cihazın uzunluk kontrolü (tüp uzunluğu ölçümü) doğal olarak sağlanır |
| Bekleme adımı | 1 mm ve katları | 2,5 mm varsayılan, 1 mm optimizasyon | Uyumlu |
| Konum doğruluğu | ± 1 mm | Bekleme yüksekliği toleransı ± 0,15 mm, yanal ± 0,2 mm | Cihaz doğruluğu plak toleransından kaba; klinik plan bu belirsizliği taşır (belge 03) |
| Kateter ve konektör | Üreticinin 6F esnek implant kateteri ve tüp konektörü | Kanal başına aynı kateter, plak içindeki tüpe yapıştırılır | Üçüncü taraf aplikatörler için yerleşik arayüz; kateter değiştirilmeden kullanılır |
| Planlama | BrachyVision: kateter rekonstrüksiyonu BT'den; sabit aplikatörler için katı aplikatör modeli üreticiden | Plak göz fantomu üzerinde bir kez BT'lenir, kateterler rekonstrüksiyon ile tanımlanır, plan şablonu olarak saklanır | Katı aplikatör modeli için Varian'a talep (A2 görüşmesine eklenir); şablon yolu bağımsız çalışır |
| Doz hesabı | BrachyVision TG-43; Acuros BV model tabanlı | Altın kalkan için model tabanlı hesap veya MC düzeltme tablosu | Acuros BV lisansı varsa kullanılır; yoksa belge 03'teki düzeltme tablosu |
| Kaynak | Ir-192 (mevcut) veya Yb-169 (A2) | Aplikatör her ikisiyle aynı | Prototip ve kabul testleri Ir-192 ile; koruma faktörü ölçümü yalnızca Yb-169 ile anlamlı |

## Bugün yapılabilecek test dizisi (Ir-192 ile)

1. **Prototip**: 16 mm plak, 3B baskı reçine veya PEEK ek parça, gömülü 3 adet 6F kateter,
   kanal yayı 13,8 mm; altın kabuk yerine geçici polimer kabuk. Aynı prototipin 17 mm yaylı sürümü.
2. **Sahte kaynak turu**: her kanalda 20 tekrar, takılma ve geri çekme kuvveti gözlemi.
3. **Gerçek kaynak turu**: boş tedavi, her kanal tüm pozisyonlara ulaşım; cihaz hata kaydı.
4. **Otoradyografi**: film kanal düzleminde, her kanal 3 pozisyon; ölü boşluk ve pozisyon
   ofseti ölçümü. Kabul: tasarım ± 0,5 mm.
5. **Film dozimetrisi**: katı su fantomu, sklera düzlemi ve 5 mm derinlik; TG-43 hesabıyla
   karşılaştırma (Ir-192 için kalkan etkisi ihmal edilir).
6. **Plan şablonu**: prototip göz fantomunda BT, BrachyVision'da kateter rekonstrüksiyonu,
   3 kanal için plan kütüphanesi denemesi, optimize bekleme sürelerinin cihaza aktarımı.

Bu altı adım Varian ile Yb-169 görüşmesi sürerken tamamlanabilir ve aplikatör tasarımını
kaynak kararından bağımsız olarak olgunlaştırır.

## Sınırlar

- Aplikatör araştırma amaçlı cihaz sayılır; CE işaretli afterloader ile kullanımı etik kurul ve
  NDK iznine bağlıdır (belge 06, faz 4).
- Ir-192 ile klinik kullanım ancak bunkerde ve sırt koruması olmadan mümkündür (A8 senaryosu).
