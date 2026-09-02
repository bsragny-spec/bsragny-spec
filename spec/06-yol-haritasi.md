# 06. Geliştirme yol haritası ve açık sorular

## Fazlar

| Faz | İçerik | Çıktı | Tahmini süre |
|-----|--------|-------|--------------|
| 0. Fizibilite | Afterloader üreticisiyle özel kaynak ve kanal uyumu görüşmesi; Yb-169 tedarikçi ve fiyat; tümör yükseklik dağılımının retrospektif analizi; radyobiyoloji danışmanlığı | Devam/dur kararı | 2 ile 3 ay |
| 1. Tasarım dondurma | Monte Carlo ile katman kalınlıkları, bekleme ekseni, koruma faktörü; kablo bükülme yarıçapı teyidi; CAD | Üretim çizimleri, MC raporu | 3 ay |
| 2. Prototip | 16 mm plak, 2 adet; ilk aşamada **Ir-192 ile** kanal geçişi ve pozisyon doğruluğu testleri (koruma hariç her şey aynı); film dozimetrisi | Kabul testi raporu | 3 ile 4 ay |
| 3. Yb-169 kaynağı | Özel kaynak üretimi, kalibrasyon yöntemi, TG-43 parametreleri, TPS tanımı, plan kütüphanesi | Kaynak sertifikası, TPS komisyonlama raporu | 6 ay, faz 1 ile paralel |
| 4. Mevzuat | NDK lisans değişikliği, ameliyathane koruma projesi, etik kurul, klinik araştırma başvurusu, cihaz için araştırma amaçlı kullanım izni | Onaylar | 6 ile 9 ay, paralel |
| 5. Hazırlık | Tatbikatlar, formlar, ekip eğitimi, kadavra veya göz fantomunda dikim ve ultrason provası | Hazırlık kontrol listesi | 1 ay |
| 6. Faz I klinik | 9 ile 15 hasta, belge 03 doz kademesi | 6 aylık toksisite raporu | 12 ile 18 ay |
| 7. v0.2 | Çentikli plak, 14 ve 18 mm boyutlar, tungsten alaşım seçeneği | | |

Kritik yol: **kaynak üretimi ve kalibrasyonu**. Aplikatör tasarımı bundan bağımsız
ilerleyebilir ve Ir-192 ile test edilebilir.

## Açık sorular, karar bekleyenler

| No | Soru | Etkisi | Sorumlu |
|----|------|--------|---------|
| A1 | Tek fraksiyonda sklera toleransı. LQ modeli 25 Gy apeks için 5 mm tümörde ~100 Gy sklera verir, bu 55 ile 65 Gy başlangıç sınırının üzerindedir | Reçeteyi ve endikasyon aralığını belirler. Faz I'de reçete sklera sınırıyla kesilir | Radyasyon onkolojisi + radyobiyoloji danışmanı |
| A2 | Afterloader üreticisi özel Yb-169 kaynağını ve daha ince kabloyu cihazında kullanmayı kabul eder mi; bükülme yarıçapı ≤ 12 mm sağlanır mı | Sağlanmazsa plak yarıçapı büyütülemez; kanal düzleştirilemez; proje cihaz değişikliğine bağlanır | Fizik + üretici |
| A3 | Yb-169 kuyu odası kalibrasyon izlenebilirliği | Klinik kullanım ön şartı | Fizik + tedarikçi + kalibrasyon laboratuvarı |
| A4 | Plak kalınlığı 4,2 mm orbitada tolere edilir mi, özellikle posterior yerleşimde | Kalınlık azaltılırsa koruma veya bekleme yüksekliği ödün verir | Cerrah |
| A5 | Transfer tüpünün forniksten çıkışı: kapak ekartörü altında tüp yolu, konjonktiva basısı | Giriş bloğu ve kılıf tasarımı | Cerrah + tasarım |
| A6 | Makula ve optik disk için tek fraksiyon kısıtları | Faz I'de kayıt, sonra sınır | Klinik |
| A7 | Yıllık 6 ile 8 kaynak değişiminin maliyeti hasta sayısıyla karşılanıyor mu | Sürdürülebilirlik | Yönetim |
| A8 | Kaynak tedarik zinciri kesilirse yedek plan: Ir-192 ile bunkerde tek seans (koruma ödünüyle) | Süreklilik | Fizik |

## Riskler

| Risk | Olasılık | Etki | Azaltma |
|------|----------|------|---------|
| Tek fraksiyon skleral nekroz | Orta | Yüksek | Düşük başlangıç dozu, büyük plak, sklera sınırıyla reçete kesme, yakın takip |
| Kaynak takılması | Düşük | Yüksek | Kabul testleri, sahte kaynak turu, acil plak çıkarma prosedürü |
| Plak kayması ışınlama sırasında | Düşük | Orta | 3 sütür, kılıf tespiti, ultrason doğrulama, kısa süre |
| Kaynak tedariki gecikmesi, aktivite düşük gelmesi | Orta | Orta | 8 ile 10 Ci teslim, hasta programı aktiviteye göre |
| Ameliyathane koruma yetersiz | Düşük | Orta | İlk hastada ölçüm, paravan sayısı artırma |
| TPS aplikatör modelinde hata | Düşük | Yüksek | MC ile film doğrulaması, bağımsız ikinci hesap |

## Değişiklik geçmişi

| Sürüm | Tarih | Değişiklik |
|-------|-------|-----------|
| v0.1 | 2026-09-02 | İlk taslak: kaynak seçimi, geometri, dozimetri yaklaşımı, iş akışı, açık sorular |
