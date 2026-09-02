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
| Paralel kirişler, 3 ile 7 kanal | 13,8 mm | Evet | Kanallar arası vadi, optimizasyonla kapanır | Evet | **Seçildi (v0.1)** |
| Spiral, tek kanal | 0 ile 6 mm | Hayır | Mükemmel | Evet, ama ulaşılamaz | Elendi |
| Tek C halkası + merkez kiriş | 5,5 ile 7,2 mm | Hayır, özel kablo ile belki 20 mm plakta | İyi | Merkez kirişle | 20 mm için v0.2'de değerlendirilebilir |
| Eş merkezli C halkaları | İç halka 2 ile 3 mm | Hayır | Mükemmel | Evet | Yalnızca pelet dizisiyle |
| Dupere halkası, pelet dizisi | Sınırsız | Hayır, pelet yükleyici | Mükemmel, statik | Konik kolimasyonla | Referans; G6 nedeniyle elendi |
| Yelpaze, kenardan merkeze yakınsayan kirişler | Kirişler düz, ~13,8 mm | Evet | Merkezde yoğunlaşma, kenarda seyrek | Evet | Paralel kirişe göre avantaj yok, giriş bloğu genişler |

## Paralel kiriş tasarımına referanstan alınacaklar

- **Konik kolimasyon fikri**: kanallar arasındaki PEEK duvarlar yerine, her kanalın sklera
  tarafında altın veya tungsten ara perde ile kanal başına yönlü açıklık. Yanal dozu ve iris
  ile lens dozunu düşürebilir. v0.2 için Monte Carlo ile değerlendirilecek; kalınlık artışı
  getirmediği sürece eklenir.
- **1,3 mm altın koruma** referans değerinin bizim 1,5 mm hedefimizle uyumu, koruma
  hesabına girdi olarak kullanılacak.
- Optik sinir ve iris doz azalmalarının bizim geometride de elde edilip edilmediği,
  belge 03'teki Monte Carlo çalışmasında I-125 COMS karşılaştırması eklenerek kontrol edilecek.

## Sonuç

Sklera eğrisine uyan kubbe plak fikri korunur ve referans tasarımdan daha iyidir. Spiral kanal,
kablo sürücülü HDR kaynağının sertliği ve bükülme sınırı nedeniyle 12 ile 16 mm plaklarda
fiziksel olarak çalışmaz; ancak pelet dizisiyle mümkündür ve o zaman standart afterloader
şartı düşer. Bu iki şart arasında seçim yapılmalıdır:

- **Standart afterloader korunacaksa**: paralel kirişler (mevcut tasarım).
- **Spiral veya eş merkezli halka isteniyorsa**: pelet dizili özel yükleyici; proje kapsamı
  cihaz geliştirmeyi de içerecek şekilde büyür.

Karar belge 06'da A9 olarak kaydedilmiştir.
