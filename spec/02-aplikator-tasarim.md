# 02. Aplikatör tasarımı

Çizimler: plak ailesi tek sayfa [figures/plak-ailesi.svg](../figures/plak-ailesi.svg); her boy için
üstten görünüş ve kesit `figures/plak-12mm.svg` … `figures/plak-20mm.svg` ve çentikli sürümler
`figures/plak-16mm-centik.svg` … `figures/plak-20mm-centik.svg`; ayrıntılı etiketli
kesit [figures/kesit.svg](../figures/kesit.svg). Çizimler `tools/draw_plaques.py` ile geometri
kurallarından üretilir; parametre değişince yeniden çalıştırılır.

| Çap | Kubbe derinliği (sagitta) | Yarım açı | Not |
|-----|---------------------------|-----------|-----|
| 12 mm | 1,6 mm | 29° | |
| 14 mm | 2,2 mm | 35° | |
| 16 mm | 3,0 mm | 41° | |
| 18 mm | 3,9 mm | 47° | |
| 20 mm | 5,1 mm | 54° | En büyük boy; 22 mm kubbe derinliği ve kas yapışma yerleri nedeniyle aileden çıkarıldı |

## Temel ilke

HDR kaynağı bir devre içinde dolaşmaz. Her kanal **kör uçlu** bir tüptür; kaynak kanala girer,
programlanan bekleme pozisyonlarında durur ve aynı yoldan geri çekilir. Aplikatör bu yüzden
birbirinden bağımsız, tek bir giriş bloğunda toplanan paralel kör kanallardan oluşur.

## Genel geometri

| Parametre | Değer | Not |
|-----------|-------|-----|
| İç eğrilik yarıçapı | 12,3 mm | COMS ile aynı, mevcut dikim tekniği geçerli |
| Çap ailesi | Yuvarlak 12, 14, 16, 18, 20 mm; çentikli 16, 18, 20 mm | Tümör tabanı 8 ile 16 mm; her boyun çizimi figures/plak-XXmm.svg ve plak-XXmm-centik.svg |
| Toplam kalınlık, merkezde | 4,25 mm | COMS yaklaşık 3,5 mm; orbita toleransı cerrahi ekiple teyit edilecek |
| Kenar duvarı | **Plak eksenine paralel** (silindirik kesim); sırt izdüşümü taban izdüşümüyle aynı, sırt tabandan taşmaz | Katmanlar küre merkezinden ışınsal kesilseydi sırt tabandan %35 geniş olur ve mantar biçimi alırdı |
| Kenar duvar yüksekliği | 12 mm: 4,7 · 14 mm: 4,9 · 16 mm: 5,2 · 18 mm: 5,5 · 20 mm: 6,0 mm | Eş merkezli katmanlar dik kesilince kenarda eksenel kalınlık artar; altın normal kalınlığı her yerde 1,5 mm kalır |
| Kenar kalkanı | Sırt kabuğuyla tek parça altın, sklera temasına kadar iner, kalınlık 0,5 mm | Plak kenarı her yönde kapalıdır; yalnızca giriş hattı yuvası açıktır. Yanal doz kolimasyonu |
| Kenar profili | Dış kenar **1,5 mm yarıçaplı yuvarlatılmış** (fillet) sırta bağlanır; dik duvar altta kalır, keskin köşe yok. Alt kenar 0,3 mm yuvarlatılmış | Dupere 2021 aplikatörünün kabuk görünüşü; Tenon ve konjonktiva için pürüzsüz kenar, dikişte takılma yok. Fillet tam olarak altın sırt kalınlığı kadardır, koruma kalınlığı kenarda azalmaz |
| Plak seçim kuralı | **Tümör tabanının en geniş çapı + 4 mm** | Her yönde 2 mm marj; sklera/apeks oranını düşürmenin en etkili yolu (belge 07) |
| Kütle, 16 mm | Yaklaşık 4 ile 6 g | Altın sırt ile; tungsten alaşım daha hafif |

Koordinat kuralı: kanal, bekleme pozisyonu ve çentik koordinatları plak **taban düzleminde**
(x, y) tanımlanır ve katmanlara **eksenel** izdüşürülür; (x, y) katmanlar boyunca değişmez, yalnızca
yükseklik küreden gelir. `tools/geometry.py` ve 3B model aynı kuralı kullanır.

## Katmanlar, skleradan dışa doğru

| Katman | Kalınlık | Malzeme | İşlev |
|--------|----------|---------|-------|
| 1. Ara katman | 0,85 mm | PEEK veya tıbbi silikon | Bekleme eksenini skleradan 1,5 mm'ye taşır, skleral sıcak noktayı düşürür |
| 2. Kanal katmanı | 1,90 mm | PEEK gövde içinde 316L paslanmaz veya nitinol tüp | Kör kanallar; iç çap 1,2 mm (Varian 0,9 mm kapsül için), dış çap 1,6 mm |
| 3. Sırt koruması | 1,50 mm | 18 ayar altın veya %95 W ağır alaşım | Yb-169 orbita dozunu keser; çevre dudak dahil tek parça |
| 4. Kaplama | 10 ile 25 µm | Altın kaplama (tungsten alaşım kullanılırsa) veya parilen | Biyouyumluluk, korozyon |

Katman 1 ve 2 tek bir polimer ek parça olarak üretilir ve altın kabuğa yerleştirilir;
COMS'taki silastik seed taşıyıcının işlevsel karşılığıdır. Kabuk ile ek parça geri dönüşsüz
birleştirilir (yapıştırma ve mekanik kilit); klinikte sökülmez.

### Bekleme ekseni yüksekliği kararı

`tools/geometry.py` çıktısı, 16 mm plak ve 5 mm apeks için sklera merkez dozunun apeks dozuna
oranını verir:

| Bekleme ekseni, skleradan | Sklera/apeks, merkez | Sıcak nokta/apeks | Toplam kalınlık |
|---------------------------|----------------------|-------------------|-----------------|
| 1,0 mm | 4,5 | 5,4 | ~3,7 mm |
| **1,5 mm** | **4,1** | **4,3** | **~4,2 mm** |
| 2,0 mm | 3,8 | 3,9 | ~4,7 mm |

1,5 mm seçildi: sıcak nokta ile merkez farkı kapanır, kalınlık orbita sınırında kalır.
Bu sayılar nokta kaynak ve eşit bekleme süresi varsayımıyladır; optimizasyon ve gerçek kaynak
geometrisi ile değişir.

## Kanal yerleşimi: paralel kirişler, sayı ve konum optimizasyonla

Tasarım kararı (belge 07): **paralel kör kirişler; kanal sayısı ve konumları doğrusal programlama
ile seçilir; her kanal anterior kenardan kendi altın ağzıyla çıkar ve kendi kateteri, kendi
transfer tüpü vardır.** Yelpaze ve tek giriş hattı düzenleri kaldırılmıştır (belge 07).

Kaç kanal gerektiği sorusunun cevabı (sklera maks / reçete, konumlar her sayı için optimize):

| Plak, apeks | 1 kanal | 2 kanal | 3 kanal | 4 kanal | 5 kanal |
|-------------|---------|---------|---------|---------|---------|
| 12 mm, 3 mm | 5,6 | 4,1 | **3,4** | 3,4 | 3,5 |
| 14 mm, 5 mm | 9,5 | 5,2 | **4,8** | 4,5 | 4,4 |
| 16 mm, 5 mm | 7,9 | 4,3 | **3,9** | 3,8 | 3,5 |
| 16 mm, 8 mm | 13,8 | 7,2 | **6,4** | 6,2 | 5,8 |
| 18 mm, 5 mm | 8,3 | 4,1 | 3,6 | 3,3 | **3,2** |
| 20 mm, 5 mm | 8,2 | 3,7 | 3,0 | 2,7 | **2,6** |
| 20 mm, 8 mm | 9,6 | 5,5 | 4,4 | 4,0 | **4,0** |

- **Tek kanal yetmez**: sklera oranı iki kat. **İki kanal** üç kanaldan %10 ile 25 kötü.
- **Üç kanal**, 12 ile 16 mm plaklarda beş kanala %3 ile 11 yakındır ve seçilmiştir.
- **Beş kanal** 18 ve 20 mm'de %10 ile 15 kazandırır ve orada seçilmiştir.
- Optimum konumlar dış kanalları kenara yakın koyar (halka benzeri dağılım); eski eşit aralık
  kuralı terk edilmiştir.
- Optimum bölge düzdür: 1 mm bekleme adımıyla yapılan taramada dış kanalın kenardan 2,5 ile
  3,5 mm, iç kanalın 2,0 ile 3,0 mm arasındaki konumları sklera oranını %5'ten az değiştirir.
  Bu yüzden konumlar **tek bir kurala** bağlanmıştır: **dış kanal kenardan 3,0 mm içeride
  (x = r − 3,0), 5 kanallıda iç kanallar ± 2,5 mm, merkez kanal 0.** Kural her boyda LP
  optimumunun %5 içindedir.

| Çap | Kanal | Konumlar x (mm) | Bekleme pozisyonu | En uzun kanal yayı |
|-----|-------|-----------------|-------------------|--------------------|
| 12 mm | 3 | 0, ± 3,0 | 10 | 10,9 mm |
| 14 mm | 3 | 0, ± 4,0 | 10 | 13,1 mm |
| 16 mm | 3 | 0, ± 5,0 | 13 | 15,4 mm |
| 18 mm | 5 | 0, ± 2,5, ± 6,0 | 26 | 17,8 mm |
| 20 mm | 5 | 0, ± 2,5, ± 7,0 | 29 | 20,4 mm |

- Kanallar sklera eğrisini izler; eksen yarıçapı 13,8 mm'lik küre kabuğu üzerindedir.
  GammaMedplus iX kablosunun bildirilen minimum bükülme yarıçapı 13 mm'dir (belge 01, A2b).
  Teyit edilene kadar yedek tasarım 17 mm yaylı kanaldır (uç sapması 16 mm kirişte 0,56 mm).
- Kanal tüpü her iki uçta kenar kalkanının 0,5 mm içine kadar uzanır; kör uçta kaynağın
  ulaşamadığı boşluk **2,0 mm**; bekleme adımı 2,5 mm (TPS izin verirse 1 mm).
- Kanal iç çapı 1,2 mm (Varian 0,9 mm kapsül), tüp dış çapı 1,6 mm.

Çentikli plakta dış kanallar sinirin iki yanından geçer (x = ± 6,3 mm), iç kanallar çentik
sınırında kısaltılır. Çentiklide kanal sayısı: 16 ve 18 mm'de **4** (x = ± 3,15, ± 6,3; merkez
kanal çentikte zaten kısa olduğu için katkısı küçük), 20 mm'de **5**.

| Çentikli plak | 3 kanal | 4 kanal | 5 kanal |
|---------------|---------|---------|---------|
| 16 mm | 7,7 | **6,4** | 5,9 |
| 18 mm | 5,4 | **4,7** | 4,6 |
| 20 mm | | | **3,8** |

## Kanal ağızları ve kateterler

Kabuk dıştan Dupere 2021 aplikatörü gibidir: pürüzsüz, kenarı yuvarlatılmış altın kubbe. Giriş
tarafında ise ortak sap veya kılıf yoktur: **her kanal anterior kenardan kendi altın ağzıyla
çıkar, her kanalın kendi kateteri ve kendi transfer tüpü vardır.** Bu, standart interstisyel HDR
uygulamasıyla aynı iş akışıdır ve çok lümenli sap, oval kök, yuvarlak demete geçiş gibi özel
parçaları ortadan kaldırır.

| Parametre | Değer | Gerekçe |
|-----------|-------|---------|
| Altın ağız | Kanal başına, kabukla tek parça, dış çap 2,4 mm, uzunluk 3 mm, kabuğa teğet, sklera eğrisini izler | Kanal tüpünü kabuktan dışarı korunaklı ve sağlam çıkarır; kenar kalkanındaki açıklık ağızla kapanır |
| Kateter | Kanal başına 1 adet, dış çap 2,0 mm (6F sınıfı esnek implant kateteri), ağızdan itibaren 30 ile 50 mm, ucunda cihazın standart konektörü | Üreticinin doğrulanmış kateteri ve konektörü; ölü boşluk ve uzunluk cihazca bilinir |
| Tüp bağlantısı | Kateter ağız içinde kanal tüpüne yapıştırılır veya sıkma ile birleştirilir; geçişte iç çap sabit 1,2 mm | Kaynak geçişinde kademe yok |
| Toplam uzunluk | Aplikatör + transfer tüpü 1300 mm sabit (GammaMedplus) | Cihaz kuralı |
| Fornikste | 3 veya 5 kateter yan yana, konjonktiva altından fornikse; kapağa steril bantla tespit | Plağa yük binmez |

- Kanal sayısı kadar transfer tüpü bağlanır: yuvarlak 12 ile 16 mm'de 3, 18 ile 20 mm'de 5; çentikli 16 ile 18 mm'de 4, 20 mm'de 5.
  Her kanal numaralı ve renk kodludur; cihazda kanal indeksi ile eşleşir.
- Ağızlar anterior kenarda, kanal konumlarında (x = 0, ± 3,5 … ± 6,6 mm) yer alır; kenar kalkanı
  ağızlar arasında kesintisizdir.
- **Ortadan (kubbe sırtından, skleraya dik) giriş elenmiştir.** Kaynağın dik saptan yüzeye
  paralel kanallara geçmesi 4 mm kalınlık içinde 90° dönüş, yani 2 ile 3 mm bükülme yarıçapı
  ister; kablo sınırı 13 mm'dir. Ayrıca dik sap orbita duvarına bakar ve fornikse ulaşmak için
  orbita içinde kıvrılması gerekir. Yalnızca pelet dizili sistemde mümkündür.
- **Ağızların kenardaki yönü serbesttir.** Varsayılan anterior kenar. Tümör kas yapışma yerinin
  altındaysa plak döndürülür ve kateterler lateral kenardan çıkar; kanallar ağızlara göre tanımlı
  olduğu için doz düzeni değişmez. Çentikli plakta ağızlar çentiğin karşısında sabittir.
- Kateterler kapaklar arasından forniksten çıkar; göz kapağı ekartörü tedavi boyunca yerinde
  kalır. Kateterler kapağa veya alına steril bantla tespit edilir.

## Dikim ve tespit

- **Sütür küpeleri: 2 adet**, kenardan dışa taşan altın kulakçık, kabukla tek parça, tabanla
  aynı düzlemde (skleraya yatar), kalınlık 0,5 mm, dış çap 2,4 mm, delik çapı 0,8 mm, kenarları
  yuvarlatılmış; 5-0 naylon veya merşilen için. Konum: **dış kanal ağızlarının hemen yanında**,
  anterior kenarda, ağız merkezinden 2,6 mm yanal. Bu konum plağın yönelimini cerrahiye
  kendiliğinden gösterir: küpeler ve kateterler aynı taraftadır.
- Kanal ağızları anteriorda kalacak şekilde dikilir; posterior tümörlerde ağızlar ekvator
  civarında olur, kateterler fornikse yönlenir.
- Plak konumu ameliyat sırasında B-mod ultrason ile doğrulanır. Metal kabuk ultrasonda
  net görülür; ayrıca ek parçaya 3 adet ekojen işaret (hava kapsülü veya cam boncuk)
  yerleştirilerek plak yönelimi kesitte tanınabilir kılınır.

## Malzeme seçimi: altın mı tungsten mi

| Ölçüt | 18 ayar altın | %95 W ağır alaşım, altın kaplı |
|-------|---------------|-------------------------------|
| Zayıflatma, aynı kalınlık | Referans | Yaklaşık %10 daha iyi |
| Biyouyumluluk | Onlarca yıllık plak deneyimi | Kaplama bütünlüğüne bağlı |
| Üretim | Döküm, sonra CNC | Sinter, CNC; daha sert, ince dudak zor |
| Kütle | Ağır | Biraz daha hafif |
| Maliyet | Yüksek malzeme bedeli | Düşük malzeme, yüksek işleme |

İlk prototip için **altın** önerilir: mevcut plakların düzenleyici ve biyouyumluluk geçmişi
doğrudan kullanılır. Tungsten alaşım kalınlık azaltma gerekirse v0.2'de değerlendirilir.

## Toleranslar

| Özellik | Tolerans | Gerekçe |
|---------|----------|---------|
| Bekleme ekseni yüksekliği | ± 0,15 mm | 1,5 mm'de %10 yükseklik hatası skleral dozu %20 değiştirir |
| Kanal yanal konumu | ± 0,20 mm | Kanallar arası doz vadisi |
| Kör uç konumu | ± 0,30 mm | Pozisyon ofseti otoradyografiyle tek tek ölçülür ve kaydedilir |
| Sırt kalınlığı | + 0,20 / − 0,00 mm | Koruma yönünde emniyet |
| İç eğrilik yarıçapı | ± 0,20 mm | Sklera oturması |

Her aplikatör seri numaralıdır; otoradyografi haritası ve boyut ölçüm raporu seri numarasına
bağlı olarak TPS aplikatör kütüphanesinde saklanır.

## Sterilizasyon ve ömür

- Buhar otoklav 134 °C ile uyumlu malzeme seçimi (PEEK uygundur, silikon uygundur, yapıştırıcı
  buna göre seçilir). Transfer tüpleri tek kullanımlık veya üreticinin protokolüne göre.
- Ömür: 50 sterilizasyon döngüsü veya 2 yıl, hangisi önce. Her 10 kullanımda otoradyografi tekrarı.
