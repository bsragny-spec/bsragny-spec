# 08. Afterloader seçimi

Cihaz proje bütçesiyle alınabileceğinden, seçim aplikatöre ve kaynağa göre yapılır; tersi değil.

## Belirleyici ölçüt

**Üreticinin kendi kablo formatında Yb-169 kaynağı sağlamayı veya üçüncü taraf Yb-169
kaynağının cihazda kullanılmasını yazılı olarak kabul etmesi.** Bu olmadan hiçbir cihaz
projeye uygun değildir; teknik özellikler ikinci sıradadır. Satın alma şartnamesine
"Yb-169 kaynak kablosu ve planlama sisteminde Yb-169 kaynak modeli desteği" madde olarak yazılır.

## Teknik ölçütler, öncelik sırasıyla

| No | Ölçüt | İstenen | Neden |
|----|-------|---------|-------|
| 1 | Yb-169 desteği | Yazılı taahhüt; kaynak tedariki, kalibrasyon sertifikası, TPS kaynak modeli | Projenin ön şartı |
| 2 | Kablo minimum bükülme yarıçapı | ≤ 17 mm, küçük olan tercih | Kanal yayı sklera eğrisine yaklaşır, uç sapması azalır (belge 02) |
| 3 | Kaynak kapsül çapı | ≤ 0,9 mm | Kanal iç çapı, kanal aralığı, plak kalınlığı |
| 4 | Aktif uzunluk | ≤ 3,5 mm | Eğri kanalda konum belirsizliği |
| 5 | Kanal sayısı | ≥ 8 | 20 mm plakta 7 kanal + yedek |
| 6 | Bekleme adımı | 1 mm seçilebilir | Optimizasyon serbestliği |
| 7 | Konum doğruluğu | ≤ ± 1 mm, tercihen ± 0,5 mm | Göz ölçeği |
| 8 | Planlama sistemi | Model tabanlı doz hesabı (heterojenite ve koruma), kullanıcı tanımlı aplikatör kütüphanesi, yeni kaynak tanımlama | Altın kalkan ve plak malzemesi TG-43 ile hesaplanamaz |
| 9 | Taşınabilirlik | Tekerlekli, pil destekli acil geri çekme, ameliyathane kapısından geçer | Tedavi ameliyathanede (G3) |
| 10 | Kilitleme ve izleme | Kapı kilidi, alan monitörü, kamera girişleri, anestezi monitörü için uzaktan görüntü | Anestezi altında tedavi |
| 11 | Servis | Türkiye'de yetkili servis, kaynak değişimi için 1 ile 2 ayda bir ziyaret kapasitesi | Yb-169 yarı ömrü 32 gün |
| 12 | Kaynak değişim mekanizması | Yerel servisçe yapılabilen, fabrikaya gönderim gerektirmeyen değişim | Yılda 6 ile 8 değişim |

## Adaylar ve teyit edilecek noktalar

| Cihaz | Kaynak formatı | Bilinen | Teyit edilecek |
|-------|----------------|---------|----------------|
| Varian Bravos | 0,9 mm kapsül, 0,9 mm çelik kablo | Bu formatta Yb-169 prototipi yayımlanmış (belge 01) | Yb-169 tutumu; kablo bükülme yarıçapı; BrachyVision'da Acuros BV ile özel aplikatör |
| Elekta Flexitron | Flexisource, 0,85 mm kapsül | Yaygın servis ağı | Yb-169 tutumu; bükülme yarıçapı; Oncentra ACE ile özel aplikatör |
| Eckert & Ziegler BEBIG SagiNova | Ir-192 ve Co-60 kaynakları | Üretici aynı zamanda kapalı kaynak imalatçısı; özel izotop için en olası muhatap | Yb-169 üretimi ve kablo formatı; bükülme yarıçapı; SagiPlan model tabanlı hesap |

Hiçbir üretici bugün Yb-169'u ürün olarak sunmamaktadır. Karar, üç üreticiye aynı teknik
şartnameyle sorulacak tek soruya göre verilir: "Bu formatta Yb-169 kaynak kablosunu kim,
hangi sürede, hangi kalibrasyon belgesiyle sağlar ve cihazınızda kullanımını onaylar?"

## Kablo bükülme yarıçapının tasarıma etkisi

Seçilen cihazın belgeli bükülme yarıçapı kanal yayı yarıçapı olur. Sapma tablosu (belge 02):
17 mm'de 16 mm kirişte 0,56 mm, 15 mm'de 0,24 mm. Yarıçap 13,8 mm'ye izin veren bir kablo
çıkarsa kanal küreyi tam izler ve sapma sıfırlanır.

## Satın alma öncesi yapılacak test

Cihaz gösterimi sırasında 3B baskı PEEK prototip plak (belge 06, faz 2) ile sahte kaynak
turu: 17 mm yaylı 16 mm kirişte takılma olmadan tam boy ilerleme ve geri çekme, 20 tekrar.
Bu test şartnameye kabul testi olarak yazılır.
