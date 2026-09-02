# 00. Klinik amaç ve gereksinimler

## Amaç

Uveal melanomda halen uygulanan LDR episkleral plak brakiterapisinin (I-125, Ru-106)
dört ile yedi günlük yatış, personel maruziyeti ve iki ayrı ameliyat gerektiren yapısını,
**tek anestezi seansında** tamamlanan HDR episkleral brakiterapi ile değiştirmek.

Sklera fiksasyonu korunur. Bu, stereotaktik radyocerrahi ve protona göre temel avantajdır:
plak tümörle birlikte hareket eder, göz ve baş hareketi doz dağılımını bozmaz, immobilizasyon
ve görüntü kılavuzluğu gerekmez.

## Zorunlu gereksinimler

| No | Gereksinim | Gerekçe |
|----|-----------|---------|
| G1 | Dikim, ışınlama ve çıkarım tek genel anestezi seansında, hasta yer değiştirmeden tamamlanır | Projenin varlık nedeni; iki seans olacaksa LDR'ye üstünlüğü kalmaz |
| G2 | Işınlama süresi tipik tümörde 30 dakikayı, en kalın tümörde 60 dakikayı aşmaz | Anestezi süresi ve ameliyathane işgali |
| G3 | Tedavi ameliyathanede, mobil koruma ile yapılabilir | G1'in sonucu; bunkere taşıma tek seans akışını bozar |
| G4 | Aplikatör mevcut plaklarla aynı cerrahi teknikle skleraya dikilir | Cerrahi öğrenme eğrisi sıfıra yakın olmalı |
| G5 | Plak sırtı orbita, optik sinir ve karşı gözü koruyacak kadar zayıflatma sağlar | Yüksek enerjili kaynaklar bunu sağlayamadığı için elenmiştir |
| G6 | Mevcut HDR afterloader ile, cihazın kanal ve kablo standardında çalışır | Yeni afterloader satın alınmaz |
| G7 | Tümör apeks yüksekliği 2 ile 10 mm arasındaki lezyonlar tedavi edilebilir | Mevcut plak endikasyon aralığı |
| G8 | Aplikatör pozisyonu ameliyat sırasında ultrason ile doğrulanabilir | Metal sırt transilüminasyona izin vermez |

## Kaynak seçimi kararı

| Kaynak | Ortalama foton enerjisi | Yarı ömür | Kurşunda HVL, yaklaşık | Karar |
|--------|------------------------|-----------|------------------------|-------|
| Ir-192 | ~380 keV | 74 gün | ~3 mm | Elendi: G3 ve G5 sağlanamaz. Prototip dozimetrisi için kullanılabilir |
| Se-75 | ~215 keV | 120 gün | ~1 mm | Elendi: koruma için 2 ile 3 mm tungsten gerekir, plak kalınlaşır |
| **Yb-169** | **~93 keV** | **32 gün** | **~0,5 mm** | **Seçildi**: 1,5 mm altın/tungsten ile koruma sağlanır, ameliyathanede uygulanabilir, kalın tümörde çalışır |
| Tm-170 | ~84 keV | 128 gün | ~0,5 mm | Elendi: gama verimi çok düşük, gereken aktivite pratik değil |
| Elektronik, 50 kV | ~30 keV etkin | Yok | ~0,05 mm | Elendi: 5 ile 6 mm üzeri tümörde sklera dozu tolere edilemez, cihaz erişimi belirsiz |

Yb-169'un bedeli kısa yarı ömür ve ticari HDR kaynağının bulunmamasıdır. Bkz. belge 01.

## Fraksiyonasyon kararı

Tek fraksiyon. Gerekçe G1'dir. Radyobiyolojik sonuçları ve buna karşı alınan önlemler
belge 03'te ele alınmıştır. Özetle: apeks dozu SRS serilerinin tek fraksiyon dozlarıyla
örtüşür ve emsali vardır; sklera dozu ise plak geometrisine özgü asıl risktir ve bu yüzden
ilk hastalarda doz kademeli artırılır.

## Kapsam dışı

- Afterloader cihazının kendisi ve yazılımı
- Yb-169 kaynağının üretim süreci (yalnızca kaynağın karşılaması gereken şartlar yazılır)
