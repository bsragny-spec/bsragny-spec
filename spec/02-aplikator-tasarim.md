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

## Kanal yerleşimi: yelpaze

Tasarım kararı (belge 07): **plağa tek giriş; kanallar anterior kenardaki dar bir giriş
sırasından düz ışınlar halinde ± 45° yelpaze gibi açılır; bekleme süreleri doğrusal programlama
ile optimize edilir.** Yelpaze, paralel kirişlerle aynı sklera/reçete oranını verir (16 mm'de
4,0'a 4,1; 20 mm'de 3,0'a 3,0) ve giriş genişliğini kanal yayılımından giriş sırasına indirerek
tek giriş hattına izin verir.

- Kanallar **düzlemde düzdür**; eğrilik yalnızca sklera küresinden gelir (13,8 mm). Kablo
  sınırı 13 mm olduğundan düzlem içi eğriliğe pay yoktur: küre ile birleşik eğrilik 13 mm'yi
  aşmamak için düzlem içi yarıçap ≥ 39 mm olmalıdır, bu da 16 mm boyunca yalnızca 3 mm sapmadır.
  Yelpaze bu yüzden kavisli değil düz ışınlarla yapılır.
- Giriş sırasında tüpler yan yana, aralık **1,7 mm** (dış çap 1,6 + 0,1). Işınlar bu sıradan
  posterior kenarda eşit açılarla dağıtılan uçlara gider.
- Kör uçta kaynağın ulaşamadığı boşluk **2,0 mm**; bekleme adımı 2,5 mm (TPS izin verirse 1 mm).
- Kanal iç çapı 1,2 mm (Varian 0,9 mm kapsül), tüp dış çapı 1,6 mm.

| Çap | Işın | Açılar | Bekleme pozisyonu | En uzun kanal | Giriş sırası genişliği |
|-----|------|--------|-------------------|---------------|------------------------|
| 12 mm | 3 | 0, ± 45° | 9 | 9,7 mm | 5,1 mm |
| 14 mm | 5 | 0, ± 22°, ± 45° | 18 | 11,0 mm | 8,5 mm |
| 16 mm | 5 | 0, ± 22°, ± 45° | 23 | 13,2 mm | 8,5 mm |
| 18 mm | 5 | 0, ± 22°, ± 45° | 26 | 15,3 mm | 8,5 mm |
| 20 mm | 7 | 0, ± 15°, ± 30°, ± 45° | 40 | 16,5 mm | 11,9 mm |

Çentikli plakta çentiğe giren ışınlar çentik sınırında kısaltılır, dıştaki ışınlar sinirin
iki yanından geçer. Yelpaze çentiklide paralel düzenden **daha iyidir** (16 mm: 4,6'ya 5,9;
18 mm: 4,3'e 4,6); 20 mm çentiklide ± 55° açı kullanılır (4,6).

## Giriş hattı

Dış görünüş Dupere 2021'in aplikatörünü (belge 07, şekil B) örnek alır: pürüzsüz altın kabuk ve
kabuğun kenarından çıkan **tek giriş hattı**. Kabukta ayrı bir sap, blok veya aparat yoktur;
kenar kalkanındaki tek yuvadan kılıf çıkar. Kabuk düz disk değil sklera eğrisinde kubbedir.

| Parametre | Değer | Gerekçe |
|-----------|-------|---------|
| Çıkış | Anterior kenar kalkanında tek yuva, kabuğa teğet | Fornikse en kısa yol |
| Kök kesiti | Yassı-oval: genişlik giriş sırası + 1,6 mm (5 kanal için 10,1 mm), kalınlık 2,6 mm | Lümenler plak içinde tek sırada olduğu için kök yassıdır |
| Geçiş | İlk 10 mm içinde oval kesit **Ø 4,8 mm yuvarlağa** geçer, 8 mm'den sonra yüzeyden ayrılır | 5 lümen 1 + 4 dizilimi (7 lümen 1 + 6), 0,3 mm duvar; 13 mm bükülme yarıçapı için gereken S geçişi 9 mm |
| Kılıf | Yuvarlak Ø 4,8 mm, yumuşak polimer, forniksten çıkar | Tek hat, tek kilitli konektör |
| Konektör | Kılıf ucunda tek kilitli konektör; cihaz tarafında kanal başına transfer tüpü | Tek hareketle bağlantı, tüp uzunluğu 1300 mm sabit |

- **Plağa tek giriş vardır.** Kaynak, afterloader tarafından her kör kanala sırayla gönderilir;
  cerrahın gördüğü tek bir hattır.
- Lümenler plak içinde tek sıra halinde kalır (kanal katmanı 1,9 mm, tek kat). Yuvarlak demete
  geçiş bu yüzden plak dışında, kılıfın ilk 10 mm'sinde yapılır.
- **Ortadan (kubbe sırtından, skleraya dik) giriş elenmiştir.** Kaynağın dik saptan yüzeye
  paralel kanallara geçmesi 4 mm kalınlık içinde 90° dönüş, yani 2 ile 3 mm bükülme yarıçapı
  ister; kablo sınırı 13 mm'dir. Ayrıca dik sap orbita duvarına bakar ve fornikse ulaşmak için
  orbita içinde kıvrılması gerekir. Yalnızca pelet dizili sistemde mümkündür.
- **Çıkış yuvasının kenardaki yeri serbesttir.** Varsayılan anterior kenar. Tümör kas yapışma
  yerinin altındaysa plak döndürülür ve hat lateral kenardan çıkar; ışınlar yuvaya göre tanımlı
  olduğu için doz düzeni değişmez. Çentikli plakta yuva çentiğin karşısında sabittir.
- Kılıf kapaklar arasından forniksten çıkar; göz kapağı ekartörü tedavi boyunca yerinde kalır.
  Kılıf kapağa veya alına steril bantla tespit edilir; plağa yük binmez.

## Dikim ve tespit

- Sırt kabuğunun dudağında 3 sütür deliği: 2 posterior yarıda simetrik, 1 anterior kenarda
  giriş hattının yanında. Delik çapı 0,8 mm, kenarları yuvarlatılmış; 5-0 naylon veya
  merşilen için.
- Giriş hattı anteriorda kalacak şekilde dikilir; posterior tümörlerde çıkış ekvator
  civarında olur, kılıf fornikse yönlenir.
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
