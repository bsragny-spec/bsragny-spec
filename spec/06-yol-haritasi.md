# 06. Geliştirme yol haritası ve açık sorular

## Fazlar

| Faz | İçerik | Çıktı | Tahmini süre |
|-----|--------|-------|--------------|
| 0. Fizibilite | Varian ile Yb-169 kaynak kablosu ve BrachyVision kaynak modeli görüşmesi (A2), cihaz modeli ve kablo bükülme yarıçapı teyidi (A2b); Yb-169 tedarikçi ve fiyat; tümör yükseklik dağılımının retrospektif analizi; radyobiyoloji danışmanlığı | Devam/dur kararı | 2 ile 3 ay |
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
| A2 | Varian, GammaMedplus iX kablo formatında Yb-169 kaynağını sağlar veya onaylar mı; BrachyVision'a Yb-169 kaynak modeli eklenir mi | Projenin kaynak tarafındaki ön şartı. Olumsuzsa belge 08'e göre başka cihaz alımı, o da olmazsa A8 | Fizik + Varian |
| A2b | GammaMedplus iX kablosunun bildirilen 13 mm minimum bükülme yarıçapının Varian teknik föyünden teyidi | Teyit edilirse kanallar 13,8 mm küreyi tam izler; edilmezse 17 mm yaylı yedek tasarım | Fizik |
| A3 | Yb-169 kuyu odası kalibrasyon izlenebilirliği | Klinik kullanım ön şartı | Fizik + tedarikçi + kalibrasyon laboratuvarı |
| A4 | Plak kalınlığı 4,2 mm orbitada tolere edilir mi, özellikle posterior yerleşimde | Kalınlık azaltılırsa koruma veya bekleme yüksekliği ödün verir | Cerrah |
| A5 | Transfer tüpünün forniksten çıkışı: kapak ekartörü altında tüp yolu, konjonktiva basısı | Giriş bloğu ve kılıf tasarımı | Cerrah + tasarım |
| A6 | Makula ve optik disk için tek fraksiyon kısıtları | Faz I'de kayıt, sonra sınır | Klinik |
| A7 | Yıllık 6 ile 8 kaynak değişiminin maliyeti hasta sayısıyla karşılanıyor mu | Sürdürülebilirlik | Yönetim |
| A8 | Yb-169 sağlanamazsa yedek plan: **aynı aplikatör, Varian'ın Ir-192 kaynağı, bunkerde tek seans**. Kanal geometrisi ve dikim aynı kalır; sırt koruması etkisiz olur, ameliyathane yerine bunker gerekir | Süreklilik; aplikatör geliştirmesi her iki senaryoda ortaktır | Fizik |
| A9 | Kanal topolojisi: standart afterloader ile paralel kiriş mi, pelet dizili özel yükleyici ile spiral veya halka mı (belge 07) | Proje kapsamını ve cihaz bağımlılığını belirler | Klinik + fizik |

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
| v0.1.6 | 2026-09-02 | Plak ailesi 12 ile 22 mm; tools/draw_plaques.py ile her boy için üstten görünüş ve kesit çizimleri, tek sayfa aile çizimi |
| v0.1.5 | 2026-09-02 | Mevcut cihaz GammaMedplus iX olarak sabitlendi; bildirilen 13 mm bükülme yarıçapı ile küreyi tam izleyen kanal ana tasarım, 17 mm yay yedek tasarım; belge 08 satın alma yalnızca Varian olumsuzsa |
| v0.1.4 | 2026-09-02 | Cihaz proje ile alınacak: belge 08 afterloader seçim ölçütleri, adaylar ve kabul testi; A2 üreticiden bağımsız yazıldı |
| v0.1.3 | 2026-09-02 | Cihaz kısıtı: Varian HDR afterloader. Kaynak Varian 0,9 mm kapsül formatına bağlandı, kanal yayı 17 mm bükülme yarıçapına göre yeniden tanımlandı, A2 ve A8 güncellendi, Flynn 2019 ve Safaeipour 2021 referansları eklendi |
| v0.1.2 | 2026-09-02 | Plak seçim kuralı taban + 4 mm, tam yükseklik kenar kalkanı, tek giriş ilkesi; optimize.py ile kanal düzeni karşılaştırması belge 07'ye eklendi |
| v0.1.1 | 2026-09-02 | Belge 07 eklendi: Dupere 2021 Yb-169 halka aplikatörü referansı, spiral kanal analizi, topoloji karşılaştırması; A9 açık sorusu |
