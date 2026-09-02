# 04. Kalite kontrol ve güvenlik

## Aplikatör kabul testleri (her seri numarası, bir kez)

| Test | Yöntem | Kabul |
|------|--------|-------|
| Boyut | Koordinat ölçüm cihazı veya mikro-BT | Belge 02 toleransları |
| Kanal geçişi | Sahte kaynak (dummy) her kanala tam boy, ardından gerçek kaynak boş tedavi | Takılma yok, tüm pozisyonlara ulaşım |
| Bekleme pozisyonu haritası | Otoradyografi, film kanal düzlemine bitişik, her kanal 3 pozisyon | Ölçülen ile tasarım ± 0,5 mm; kör uç ofseti kaydedilir |
| Koruma faktörü | Plak arkasında 5 mm'de iyon odası veya film, korumasız kaynağa oranla | ≤ %10 |
| Doz dağılımı | EBT3 film, sklera düzlemi ve 5 mm derinlik | MC ile ≤ %5 eksen, ≤ %8 sklera düzlemi |
| Sızdırmazlık ve bütünlük | Görsel, kaplama sürekliliği, sterilizasyon sonrası tekrar | Hasar yok |
| Sütür deliği dayanımı | 5 N çekme | Deformasyon yok |

## Kaynak QA

| Sıklık | İşlem |
|--------|-------|
| Her yeni kaynak | Kuyu odası ile hava kerma şiddeti, sertifika ile fark ≤ %3 (belge 01 kalibrasyon notu); silme testi |
| Her tedavi günü | Cihaz günlük QA, kaynak pozisyon doğruluğu ± 1 mm, zamanlayıcı, acil geri çekme |
| Her hasta | Bozunum düzeltilmiş aktivite TPS ile karşılaştırma, ikinci bağımsız hesap (bekleme süresi toplamı için elle veya betikle) |

## Hasta öncesi plan kontrolü

- Plak boyutu ve tümör yüksekliği için plan kütüphanesi kaydı, seri numarası eşleşmesi.
- Reçete noktası, sklera maksimumu, makula, disk ve lens dozları protokol formuna işlenir.
- İki fizikçi imzası; cerrah plak yönelimini (giriş bloğu konumu) planla karşılaştırır.

## Tedavi sırasında

- Kanal bağlantısı: konektör kilidi, cihaz tarafından tüp uzunluğu doğrulaması.
- İlk kanalda sahte kaynak turu, sonra gerçek kaynak.
- Odada kimse kalmaz; hasta anestezi monitörleri ve iki kamera ile izlenir. Anestezi ekibi
  kapıdan uzaktan izleme yapar; standart bunker altı anestezi uygulamasıyla aynıdır.
- Kapı kilidi ve alan monitörü afterloader ile kilitlemelidir (interlock).

## Acil durum

| Durum | Eylem |
|-------|-------|
| Kaynak geri çekilmedi | Cihaz acil geri çekme, ardından manuel krank. Alan monitörü kontrolü |
| Manuel geri çekme başarısız | Odaya giren fizikçi transfer tüpünü giriş bloğundan ayırmaz; **sütürler kesilir, plak tüpüyle birlikte acil kurşun kaba konur**, hasta odadan çıkarılır. Hedef süre 2 dakika. Bunun için sütür makası ve kurşun kap tedavi boyunca odada hazır durur |
| Plak tedavi sırasında yerinden oynadı (ultrason veya gözle) | Tedavi durdurulur, kaynak geri, pozisyon düzeltilir, kalan süre yeniden hesaplanır |
| Anestezi acili | Kaynak geri çekilir, ekip girer; girişten önce alan monitörü |
| Elektrik kesintisi | Cihaz pili ile kaynak geri çekilir; UPS zorunlu |

Acil tatbikat: klinik başlangıcından önce ve yılda iki kez, cerrah, anestezi ve fizik ekibiyle.

## Radyasyon korunması, ameliyathane

- Koruma hesabı Yb-169 spektrumu ile yapılır; iş yükü haftalık hasta sayısı × ortalama
  bekleme süresi toplamı × aktivite. Mobil 3 mm kurşun paravanlar cihaz ve hastanın
  etrafında; kapı ve komşu alanlar için ilk hastada ölçüm.
- Plak sırtı hastanın kendi başı için birincil korumadır; buna rağmen hasta başı çevresine
  kurşun eşdeğeri örtü (0,5 mm) serilebilir.
- Personel dozimetrisi standart; tedavi sırasında odada kimse olmadığı için beklenen doz sıfıra yakındır.
- Kaynak cihaz kasasında kalır; ameliyathaneye cihaz taşıma, park ve kilitleme prosedürü yazılır.
- Düzenleyici kurum (NDK) lisansı: ameliyathanenin denetimli alan olarak tanımlanması,
  Yb-169'un lisansa eklenmesi, taşıma izni.
