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
| Toplam kalınlık (kenar hariç) | ≤ 4,2 mm hedef, ≤ 4,5 mm üst sınır | COMS yaklaşık 3,5 mm; orbita toleransı cerrahi ekiple teyit edilecek |
| Kenar kalkanı | Sırt kabuğuyla tek parça altın, **tam yükseklikte** sklera temasına kadar iner, kalınlık 0,5 mm | Plak kenarı her yönde kapalıdır; yalnızca giriş bloğu yuvası açıktır. Yanal doz kolimasyonu |
| Plak seçim kuralı | **Tümör tabanının en geniş çapı + 4 mm** | Her yönde 2 mm marj; sklera/apeks oranını düşürmenin en etkili yolu (belge 07) |
| Kütle, 16 mm | Yaklaşık 4 ile 6 g | Altın sırt ile; tungsten alaşım daha hafif |

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

## Kanal yerleşimi

Tasarım kararı (belge 07'deki karşılaştırmaya dayanır): **plağa tek giriş, içeride paralel
kör kirişler, bekleme süreleri doğrusal programlama ile optimize.** Kablo sürücülü HDR
kaynağıyla uygulanabilen düzenler arasında en iyi sklera/reçete oranını bu verir; tek kiriş
oranı iki kat kötüleştirir, halka ve spiral düzenler kabloyla uygulanamaz.

- Kanallar plak tabanına paralel **kirişler** boyunca uzanır, hepsi anterior (limbal) kenardaki
  giriş bloğundan girer. Radyal yerleşim elendi: kanallar bir merkezde toplanınca giriş bloğu
  plak ortasına gelir ve bükülme yarıçapı sağlanamaz.
- Kanallar sklera eğrisini izler; eksen yarıçapı 13,8 mm'lik küre kabuğu üzerindedir.
  Kurumdaki GammaMedplus iX kablosunun bildirilen minimum bükülme yarıçapı 13 mm'dir (belge 01),
  yani küreyi tam izleyen kanal kablo sınırının içindedir. Bu değer Varian teknik föyünden teyit
  edilene kadar (A2b) **yedek tasarım** 17 mm yaylı kanaldır: kiriş ortası skleradan 1,5 mm'de,
  uçlar küreden dışa doğru hafifçe ayrılır:

  | Kiriş uzunluğu | Düz kanal sapması | R = 17 mm kanal sapması |
  |----------------|-------------------|-------------------------|
  | 8 mm | 0,59 mm | 0,12 mm |
  | 12 mm | 1,37 mm | 0,28 mm |
  | 14 mm | 1,91 mm | 0,40 mm |
  | 16 mm | 2,56 mm | 0,56 mm |

  Yedek tasarımda sapma kanal katmanı içinde karşılanır; uçlarda bekleme yüksekliği 1,5 mm'den
  en fazla 0,6 mm artar ve plan kütüphanesinde gerçek koordinatlarla hesaba girer. Düz kanal
  her iki durumda da elenir.
- Kanal yarıçapı ne olursa olsun 20 tekrarlı sahte kaynak geçiş testi kabul şartıdır (belge 04);
  13 mm sınırına yakın çalışıldığı için bu test özellikle önemlidir.
- Giriş bloğu ile kanal arasında ek büküm yoktur; transfer tüpü bloğa kanal yayına teğet girer.
- Kanal tüpü kenar kalkanının 0,3 mm içine kadar uzanır; kör uçta kaynağın ulaşamadığı boşluk **2,0 mm** kabul edilmiştir; kaynak modeline göre
  otoradyografiyle ölçülür ve TPS'e girilir.
- Bekleme pozisyonu adımı 2,5 mm; planlama sistemi izin veriyorsa 1,0 mm adımla optimizasyon.

| Çap | Kanal sayısı | Kanal aralığı | Bekleme pozisyonu sayısı | En uzun kanal yayı |
|-----|--------------|---------------|--------------------------|--------------------|
| 12 mm | 3 | 3,50 mm | 7 | 9,2 mm |
| 14 mm | 5 | 2,25 mm | 16 | 11,3 mm |
| 16 mm | 5 | 2,75 mm | 19 | 13,5 mm |
| 18 mm | 5 | 3,25 mm | 22 | 15,9 mm |
| 20 mm | 7 | 2,50 mm | 35 | 18,3 mm |

Kanal aralığı 2,25 mm'de komşu tüpler arası duvar 0,75 mm kalır; PEEK için yeterlidir,
üretim yöntemi belirlenince teyit edilir. Belge 07'deki karşılaştırmaya göre 5 kanal ile
7 kanal arasındaki fark %3'ün altındadır; 20 mm plakta 5 veya 7 kanal seçimi Monte Carlo'da
sklera yüzeyi dalgalanmasına göre yapılır.

## Çentikli sürümler (jukstapapiller tümörler)

Optik disk komşuluğundaki tümörler için 16, 18 ve 20 mm plakların posterior kenarı U çentiklidir.

| Parametre | Değer | Gerekçe |
|-----------|-------|---------|
| Çentik biçimi | U, yarım daire tabanlı | Sinir kılıfına oturur, köşe yok |
| Çentik genişliği | 8 mm | Sinir dural kılıfı globda 5 ile 7 mm; 5 mm altı çentik sinire sıkışır ve plağın posterior kenarı diske oturmaz (Eye Physics kılavuzu) |
| Yarım daire merkezi | Plak merkezinden 9 mm posteriorda | Eye Physics / COMS çentik modeli; çentik dibi merkezden 5 mm'de |
| Çentik kenarı | 0,5 mm altın kalkan çentik hattını izler | Kenar her yerde kapalı kalır |
| Tümör yerleşimi | Tümörün posterior kenarı çentik dibinde; taban çapı ≤ plak çapı − 4 mm | Lateral ve anterior marj 2 mm'den büyük olur |
| Sütür delikleri | 2 lateral, 1 anterior | Posterior kenar çentik nedeniyle kullanılamaz |

Kanal düzeni çentikli sürümlerde değişir. Çentiğe giren üç iç kanal (x = 0 ve ± 2,65 mm) çentik
sınırında kısaltılır; çentiğin iki yanında **tam boy yan kanallar** (x = ± 5,3 mm) sinirin iki
yanından geçer ve disk komşuluğundaki tümör kenarını besler. 20 mm'de bir dış kanal çifti
daha vardır (x = ± 7,3 mm).

| Çap | Kanal | Kısaltılmış | Yan kanal | Bekleme pozisyonu |
|-----|-------|-------------|-----------|-------------------|
| 16 mm | 5 | 3 | 2 | 18 |
| 18 mm | 5 | 3 | 2 | 20 |
| 20 mm | 7 | 3 | 4 | 31 |

14 mm çentikli sürüm yoktur: 8 mm çentiğin yanında yan kanala yer kalmaz. Disk komşuluğunda
10 mm ve altı tabanlı tümörler 16 mm çentikli plakla tedavi edilir.

`tools/optimize.py` çentikli karşılaştırması (nokta kaynak, LP optimizasyonu, tümör posterior
kenarı çentik dibinde):

| Plak | Düzen | Sklera/Rx | Disk merkezi/Rx |
|------|-------|-----------|-----------------|
| 16 mm | Yuvarlak, sinir yok sayılır | 3,8 | 0,63 |
| 16 mm | **Çentikli** | 3,9 | 0,56 |
| 20 mm | Yuvarlak, sinir yok sayılır | 3,5 | 1,14 |
| 20 mm | **Çentikli** | 3,6 | 0,73 |

Yan kanallar ve bekleme optimizasyonu sayesinde çentik, tümör kapsamasını bozmadan disk dozunu
düşürür. Bu, seed çıkarılan LDR çentikli plaklara göre HDR'nin somut bir avantajıdır: eksik
seed'in yerini bekleme süreleri doldurur.

## Giriş bloğu ve transfer tüpleri

- **Plağa tek giriş vardır.** Kenar kalkanında tek bir yuva açılır; transfer tüpleri tek kılıf
  ve tek kilitli konektörle bu yuvaya bağlanır. Kaynak, afterloader tarafından her kör kanala
  sırayla gönderilir; cerrahın gördüğü tek bir kablo çıkışıdır.
- Giriş bloğu plağın anterior kenarında, plak yüzeyinden **≤ 3 mm** çıkıntı yapar.
  Kanal girişleri blokta yan yana dizilir; her giriş numaralı ve renk kodludur.
- Kanallar bloğa **teğet** girer; blokta ek büküm yoktur. Tüm büküm kanal içindeki küre
  kabuğu eğrisidir.
- Transfer tüpleri bloğa tek bir kilitli konektörle bağlanır (tek hareketle 3 ile 7 kanal).
  Konektörden sonra tüpler 20 cm boyunca tek kılıf içinde gider, sonra afterloader
  bağlantıları için ayrılır. Toplam uzunluk cihazın standart transfer tüpü uzunluğuna eşittir.
- Konektör kilitli değilken afterloader kanal kontrolü hata verir (tüp uzunluğu ölçümü ile).
- Tüpler kapaklar arasından forniksten çıkar; göz kapağı ekartörü tedavi boyunca yerinde kalır.
  Kılıf kapağa veya alına steril bantla tespit edilir; plağa yük binmez.

## Dikim ve tespit

- Sırt kabuğunun dudağında 3 sütür deliği: 2 posterior yarıda simetrik, 1 anterior kenarda
  giriş bloğunun yanında. Delik çapı 0,8 mm, kenarları yuvarlatılmış; 5-0 naylon veya
  merşilen için.
- Giriş bloğu tarafı anteriorda kalacak şekilde dikilir; posterior tümörlerde blok ekvator
  civarında olur, tüp fornikse yönlenir.
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
