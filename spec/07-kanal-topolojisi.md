# 07. Kanal topolojisi: paralel kiriş, spiral, halka karşılaştırması

## Referans tasarım

Dupere JM, Munro JJ III, Medich DC. *Shielded high dose rate ocular brachytherapy using
Yb-169.* Phys Med Biol 2021;66(12). DOI 10.1088/1361-6560/ac02d6.

Özeti: Yb-169 orta enerjili HDR kaynağı, 1,3 mm altın korumalı **halka** aplikatör.
Kaynak, halka kanala yerleştirilen **ayrık peletlerden** oluşan bir dizidir; halkanın
sklera tarafında, kaynak tüpüne teğet **konik kolimasyon açıklığı** vardır. Açıklık açısı ve
halka çapı tümör boyutuna göre değişir. MCNP6 ile I-125 COMS plağına karşı doğrulanmıştır;
apeks 3,5 ile 8 mm, taban 10 ile 15 mm. Maksimum dozda azalma I-125'e göre: arka lens %5,2,
iris %9,3, optik sinir %13,8, **sklera %1,3**.

Bu çalışmanın bizim spesifikasyonumuz için anlamı:

1. **Yb-169 seçimini ve altın koruma kalınlığını bağımsız olarak doğrular** (1,3 mm; bizde 1,5 mm).
2. Sklera dozunun I-125'e göre yalnızca %1,3 azalması, **sklera/apeks oranının kaynak ve
   kanal düzeninden bağımsız, geometrik bir sınır** olduğunu gösterir. Belge 06'daki A1 açık
   sorusu bu bulguyla daha da önem kazanır.
3. Halka içinde **kablo ile sürülen tek kaynak değil, pelet dizisi** kullanılmıştır. Bunun nedeni
   aşağıda hesaplanan bükülme yarıçapı sorunudur.
4. Yazarlardan Munro'nun bağlı olduğu kuruluş Yb-169 kaynak üretimi konusunda deneyimlidir;
   belge 01'deki tedarik araştırmasında ilk temas adaylarındandır (teyit edilecek).

Bizim tasarım bu referanstan iki noktada ayrılır: aplikatör **sklera eğrisine uyar** (halka
değil, COMS tipi kubbe) ve **standart kablo sürücülü HDR afterloader** ile çalışır (G6).

## Spiral kanal önerisi

Öneri: plak içinde kenardan merkeze doğru tek bir spiral kanal; kaynak spiral boyunca bekleme
pozisyonlarında durarak tüm tabanı tek kanaldan tarar.

Çekici yanları: tek giriş, tek transfer tüpü, kanallar arası doz vadisi yok, dairesel simetri.

### Neden kablo sürücülü kaynakla çalışmaz

Kaynak kapsülü serttir (3,5 ile 5 mm) ve kablonun izin verilen en küçük bükülme yarıçapı
cihaza göre 10 ile 15 mm'dir. Plak içindeki düzlem eğriliği küre kabuğu eğriliğiyle birleşir:

| Düzlem içi yarıçap r | Küre kabuğu üzerindeki bileşik bükülme yarıçapı |
|----------------------|-------------------------------------------------|
| 2 mm | 2,0 mm |
| 4 mm | 3,8 mm |
| 6 mm | 5,5 mm |
| 6,5 mm (16 mm plağın en dışı) | 5,9 mm |
| 8,5 mm (20 mm plağın en dışı) | 7,2 mm |
| Paralel kiriş (düzlemde düz) | 13,8 mm |

16 mm plakta spiralin **en dış turu bile** 6 mm'nin altında bükülme yarıçapı gerektirir;
merkeze doğru sıfıra iner. Özel üretim esnek kabloyla bile ulaşılabilecek sınır 8 ile 10 mm
civarındadır. Sonuç:

| Plak | Spiral uzunluğu | Bükülme sınırı 6 mm ile kullanılabilir kısım |
|------|-----------------|---------------------------------------------|
| 16 mm, hatve 2,75 mm | 49 mm, 2,4 tur | %15, yalnızca en dış yarım tur |
| 20 mm, hatve 2,5 mm | 92 mm, 3,4 tur | %50, r > 6 mm halkası |

Yani spiral, kablo sürücülü kaynakla 16 mm'ye kadar plaklarda kullanılamaz; 20 mm plakta
yalnızca dış halkası kullanılır ve merkez boş kalır. Merkezi tümör apeksinin altı olduğu
için bu kabul edilemez.

### Spirali mümkün kılan tek yol

Dupere ve arkadaşlarının yaptığı gibi **pelet dizisi**: milimetrik Yb-169 peletleri
pnömatik veya itici telle kanala sürülür, kapsül sertliği ve kablo bükülmesi sorunu kalmaz.
Bunun bedelleri:

- Standart HDR afterloader bunu yapamaz; pelet tipi uzaktan yükleyici gerekir. Bu sınıf
  cihazlar (Selectron benzeri) artık üretilmemektedir; özel cihaz geliştirme ve ruhsat demektir.
  Gereksinim G6 ihlal edilir.
- Pelet dizisinde bekleme pozisyonu optimizasyonu yoktur; doz şekillendirme aktif ve pasif
  pelet sıralamasıyla, yani statik olarak yapılır. Kanal içi doz modülasyonu kaybolur.
- Pelet sıkışması durumunda acil müdahale, tek kaynaklı sisteme göre zordur.

## Değerlendirilen topolojiler

| Topoloji | Bükülme yarıçapı | Standart afterloader | Doz simetrisi | Merkez kapsama | Karar |
|----------|------------------|----------------------|---------------|----------------|-------|
| **Paralel kirişler, 3 veya 5 kanal, konumlar LP ile** | 13,8 mm | **Evet** | Kanallar arası vadi, optimizasyonla kapanır | Evet | **Seçildi (v0.3)**: her kanal kendi ağzı ve kateteriyle |
| Spiral, tek kanal | 0 ile 6 mm | Hayır | Mükemmel | Evet, ama ulaşılamaz | Elendi |
| Tek C halkası + merkez kiriş | 5,5 ile 7,2 mm | Hayır, özel kablo ile belki 20 mm plakta | İyi | Merkez kirişle | 20 mm için v0.2'de değerlendirilebilir |
| Eş merkezli C halkaları | İç halka 2 ile 3 mm | Hayır | Mükemmel | Evet | Yalnızca pelet dizisiyle |
| Dupere halkası, pelet dizisi | Sınırsız | Hayır, pelet yükleyici | Mükemmel, statik | Konik kolimasyonla | Referans; G6 nedeniyle elendi |
| Disk biçimli açık hazne, tek giriş | Yol tanımsız | **Hayır**: kablo haznede bükülür, bekleme pozisyonu ve konum doğruluğu tanımlanamaz | Yalnızca sıvı/jel kaynakla homojen disk; optimize dağılımdan %20 ile 30 kötü | Evet | Elendi. Sıvı kaynak LDR sınıfıdır, HDR aktivitesinde sızıntı riski gözde kabul edilemez |
| Yelpaze, dar giriş sırasından ± 45° düz ışınlar | Işınlar düz, 13,8 mm | Evet | Optimizasyonla paralel kirişe eş | Evet | v0.2'de denendi; tek giriş hattı istenmediği için paralel kirişe dönüldü |

## Paralel kiriş tasarımına referanstan alınacaklar

- **Konik kolimasyon fikri**: kanallar arasındaki PEEK duvarlar yerine, her kanalın sklera
  tarafında altın veya tungsten ara perde ile kanal başına yönlü açıklık. Yanal dozu ve iris
  ile lens dozunu düşürebilir. v0.2 için Monte Carlo ile değerlendirilecek; kalınlık artışı
  getirmediği sürece eklenir.
- **1,3 mm altın koruma** referans değerinin bizim 1,5 mm hedefimizle uyumu, koruma
  hesabına girdi olarak kullanılacak.
- Optik sinir ve iris doz azalmalarının bizim geometride de elde edilip edilmediği,
  belge 03'teki Monte Carlo çalışmasında I-125 COMS karşılaştırması eklenerek kontrol edilecek.

## Dupere aplikatörünün iki yüzü: dış görünüş alınır, kanal alınmaz

Makaledeki şekil, 12 mm aplikatörü iki görünüşte verir. **A**: "9" biçimli halka kanal, içinde
on altı ayrık kaynak peleti, tek teğet giriş. **B**: dıştan pürüzsüz altın kabuk ve kenara
teğet tek sap.

- **Kanal (A)**: halka yarıçapı yaklaşık 4 mm. GammaMedplus kablosunun sınırı 13 mm; kapsül
  bu halkaya giremez. Makale bu yüzden pelet dizisi kullanır. Elimizdeki cihazla uygulanamaz.
  Bu, yukarıdaki spiral analizinin halka biçimli halidir.
- **Dış görünüş (B)**: kabuk için benimsenmiştir (belge 02): pürüzsüz kubbe, yuvarlatılmış kenar,
  dik duvar. Tek sap yerine kanal başına küçük altın ağız ve ayrı kateter kullanılır; ortak
  çok lümenli sap denenmiş (v0.2) ve istenmediği için kaldırılmıştır.

## Sayısal karşılaştırma: hangi düzen en iyi

`tools/optimize.py`: plak çapı = taban + 4 mm; tümör yüzeyinin her noktası ≥ reçete olacak
şekilde bekleme süreleri doğrusal programlama ile optimize edilir, plak altındaki sklera
maksimumu en aza indirilir. Değer, **sklera maksimumu / reçete dozu** oranıdır; küçük iyidir.
"Eşit" sütunu bütün bekleme sürelerinin eşit olduğu plan, "opt." optimize edilmiş plandır.

| Düzen | Bükülme yarıçapı | Kabloyla uygulanır | Taban 8, apeks 3, plak 12 | Taban 12, apeks 5, plak 16 | Taban 12, apeks 8, plak 16 | Taban 16, apeks 5, plak 20 |
|-------|------------------|--------------------|---------------------------|----------------------------|----------------------------|----------------------------|
| Tek çap kirişi | 13,8 mm | Evet | 7,9 → 6,8 | 8,4 → 8,0 | 15,1 → 14,3 | 11,1 → 9,9 |
| 3 paralel kiriş | 13,8 mm | Evet | 5,2 → 4,2 | 5,9 → 5,1 | 10,0 → 8,5 | 6,3 → 4,8 |
| 5 paralel kiriş | 13,8 mm | Evet | 4,8 → 3,9 | 5,2 → 4,1 | 8,9 → 6,9 | 4,3 → 3,0 |
| 7 paralel kiriş | 13,8 mm | Evet | 4,8 → 3,7 | 5,2 → 4,0 | 8,8 → 6,7 | 4,5 → 3,3 |
| **Yelpaze ± 45°, 3/5/5/7 ışın** | 13,8 mm | **Evet** | 5,4 → **4,4** | 5,0 → **4,0** | 8,6 → **6,7** | 4,1 → **3,0** |
| C halkası + merkez | 3,8 ile 6,9 mm | Hayır | 3,7 → 3,3 | 4,1 → 3,9 | 6,7 → 6,3 | 3,7 → 3,3 |
| Eş merkezli halkalar + merkez | 2,5 ile 3,8 mm | Hayır | 3,7 → 3,3 | 4,3 → 3,6 | 7,3 → 5,9 | 3,6 → 2,7 |

Okuma:

- **Tek kanal ile plak içi tarama** (tek kiriş) oranı iki kat kötüleştirir; sklera dozu
  kabul edilemez olur. Tek giriş korunur ama içeride birden fazla kör kanal şarttır.
- **Yelpaze ± 45°** ve **5 paralel kiriş** eşdeğerdir; kabloyla uygulanabilen düzenler içinde en
  iyileridir. Her kanalın kendi ağzı ve kateteriyle çıkması istendiğinden paralel kiriş
  seçilmiştir; yelpazenin tek avantajı olan dar giriş sırası bu durumda gerekmez.
- Kanal **sayısı** ayrıca incelenmiştir (belge 02 tablosu): tek kanal iki kat kötü, iki kanal
  %10 ile 25 kötü, üç kanal 12 ile 16 mm'de beş kanala %3 ile 11 yakın. Karar: 12 ile 16 mm'de 3,
  18 ile 20 mm'de ve çentiklilerde 5 kanal.
- **Halka ve eş merkezli düzenler**, pelet dizili özel yükleyici gerektirir ve 5 kirişe göre
  %5 ile 25 kazandırır. En büyük fark 20 mm plak ve kalın tümörde görülür. Bu kazanç, özel
  cihaz geliştirmenin bedeliyle karşılaştırılmalıdır (A9).
- **Optimizasyon** 5 kirişte oranı %15 ile 30 düşürür; plan kütüphanesi bu optimize edilmiş
  sürelerle kurulur.
- Toplam bekleme süresi düzenler arasında %20'den az değişir; ışınlama süresini düzen değil
  kaynak aktivitesi belirler.

Bu sayılar nokta kaynak yaklaşımıyladır; sıralama Monte Carlo'da değişmez, mutlak değerler değişir.

## Sonuç

Sklera eğrisine uyan kubbe plak fikri korunur ve referans tasarımdan daha iyidir. Spiral kanal,
kablo sürücülü HDR kaynağının sertliği ve bükülme sınırı nedeniyle 12 ile 16 mm plaklarda
fiziksel olarak çalışmaz; ancak pelet dizisiyle mümkündür ve o zaman standart afterloader
şartı düşer. Bu iki şart arasında seçim yapılmalıdır:

- **Standart afterloader korunacaksa**: 3 veya 5 paralel kiriş, konumlar ve bekleme süreleri
  optimize, her kanal kendi ağzı ve kateteriyle (mevcut tasarım). Kabloyla uygulanabilen en iyi
  düzen budur.
- **Spiral veya eş merkezli halka isteniyorsa**: pelet dizili özel yükleyici; proje kapsamı
  cihaz geliştirmeyi de içerecek şekilde büyür.

Karar belge 06'da A9 olarak kaydedilmiştir.
