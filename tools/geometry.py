#!/usr/bin/env python3
"""
Yb-169 HDR episkleral aplikatör: geometri ve kaba doz oranı hesabı.

Bu betik tasarım kararlarını beslemek için yaklaşık sayılar üretir.
Klinik doz hesabı için DEĞİLDİR; Monte Carlo ve film doğrulaması şarttır.

Model:
- Sklera dış yüzeyi küre, yarıçap R_SCLERA (mm). Plak iç yüzeyi aynı yarıçapta.
- Bekleme (dwell) pozisyonları sklera yüzeyinden DWELL_OFFSET kadar dışarıda,
  yarıçapı R_SCLERA + DWELL_OFFSET olan küre kabuğu üzerinde, paralel kirişler
  boyunca dizilir.
- Doz: nokta kaynak, ters kare + Yb-169 için yaklaşık radyal doz fonksiyonu.
  Anizotropi ve plak saçılması ihmal edildi. Sırt koruması ihmal edildi
  (koruma yalnızca plak arkasını etkiler, tümör tarafını değil).
- Tüm bekleme sürelerinin eşit olduğu "düz" plan hesaplanır; optimizasyonla
  sklera/apeks oranı bir miktar iyileşir.
"""
import math
import sys

R_SCLERA = 12.3       # mm, COMS ile uyumlu iç eğrilik yarıçapı
# Not: Varian kablosu için kanal yayı 17 mm yarıçaplıdır; uçlardaki <=0,6 mm sapma bu
# kaba modelde ihmal edilmiştir (bkz. spec/02).
DWELL_OFFSET = 1.5    # mm, bekleme pozisyonu ile sklera arasındaki mesafe
DWELL_STEP = 2.5      # mm, bekleme pozisyonu aralığı
CHANNEL_PITCH = 3.0   # mm, komşu kanallar arasındaki mesafe
EDGE_MARGIN = 1.5     # mm, plak kenarından kanal merkezine
TIP_DEAD = 2.0        # mm, kanal kör ucunda kaynağın ulaşamadığı boşluk

# Yb-169 radyal doz fonksiyonu için kaba yaklaşım (literatür, g(r) 1 cm'de 1)
# 0.5 cm'de ~0.98, 1 cm'de 1.0, 2 cm'de ~1.04 (yumuşak spektrumda saçılma birikimi)
def g_r(r_mm):
    r = max(r_mm, 0.5) / 10.0
    return 1.0 + 0.05 * math.log(r) if r < 1 else 1.0 + 0.04 * math.log(r)

def dose_rate(rel, d_mm):
    """Nokta kaynak, keyfi birim. d: mesafe (mm)."""
    d = max(d_mm, 0.5)
    return rel * g_r(d) / (d * d)

def plaque_layout(diameter):
    """Paralel kiriş kanalları ve bekleme pozisyonlarını üretir.
    Koordinatlar plak tabanı düzleminde (x,y), z sklera normalinde.
    Küre üzerine projeksiyon: z = sqrt(Rd^2 - x^2 - y^2) - Rd + ... """
    Rd = R_SCLERA + DWELL_OFFSET
    half = diameter / 2.0 - EDGE_MARGIN
    # tek sayıda kanal, en dış kanal kenar payının 1 mm içinde
    n_ch = 2 * int((half - 1.0) / CHANNEL_PITCH + 0.5) + 1
    pitch = 2 * (half - 1.0) / (n_ch - 1) if n_ch > 1 else 0.0
    xs = [(-(n_ch - 1) / 2.0 + i) * pitch for i in range(n_ch)]
    channels = []
    for x in xs:
        chord_half = math.sqrt(half * half - x * x)
        # kanal girişi y=-chord_half tarafında; kör uç y=+chord_half - TIP_DEAD
        y_end = chord_half - TIP_DEAD
        y_start = -chord_half + 0.5
        n = int((y_end - y_start) // DWELL_STEP) + 1
        ys = [y_start + i * DWELL_STEP for i in range(n)]
        dwells = []
        for y in ys:
            rr = x * x + y * y
            z = math.sqrt(max(Rd * Rd - rr, 0.0))  # küre merkezinden yükseklik
            dwells.append((x, y, z))
        # kanal boyunca eğrilik yarıçapı: küre kabuğunda kiriş -> Rd*... yaklaşık Rd
        arc_len = 2 * Rd * math.asin(min(chord_half / Rd, 1.0))
        channels.append({"x": x, "chord": 2 * chord_half, "arc": arc_len,
                         "pitch": pitch, "dwells": dwells})
    return channels

def evaluate(diameter, tumor_heights=(3, 5, 8, 10)):
    ch = plaque_layout(diameter)
    dwells = [d for c in ch for d in c["dwells"]]
    Rs = R_SCLERA
    # Sklera merkezi noktası: küre üzerinde (0,0,Rs). Apeks: (0,0,Rs - h) (içe doğru)
    def dose_at(pt):
        return sum(dose_rate(1.0, math.dist(pt, dw)) for dw in dwells)
    d_sclera = dose_at((0, 0, Rs))
    # sklera altındaki en sıcak nokta: bir bekleme pozisyonunun tam altı
    hot = max(dose_at((dw[0], dw[1], math.sqrt(max(Rs*Rs - dw[0]**2 - dw[1]**2, 0))))
              for dw in dwells)
    out = {"diameter": diameter, "n_channels": len(ch), "n_dwells": len(dwells),
           "arc_max": max(c["arc"] for c in ch), "pitch": ch[0]["pitch"], "sclera_center": d_sclera,
           "sclera_hot": hot, "apex": {}}
    for h in tumor_heights:
        da = dose_at((0, 0, Rs - h))
        out["apex"][h] = {"ratio_center": d_sclera / da, "ratio_hot": hot / da,
                          "abs": da}
    return out

def dwell_time_estimate(diameter, h, activity_ci, apex_dose_gy):
    """Yb-169 için toplam bekleme süresi kaba tahmini (dakika).
    1 Ci Yb-169 için 1 cm'de suda doz hızı ~18 Gy/h varsayımı."""
    res = evaluate(diameter, (h,))
    ch = plaque_layout(diameter)
    n = sum(len(c["dwells"]) for c in ch)
    # her bekleme kendi süresinde katkı verir: eşit süre t için apeks dozu =
    # t * sum(rate_i); rate_i birimi (1/mm^2) -> 1 cm = 100 mm^2 normalizasyonu
    gy_per_min_per_ci_at_1cm = 18.0 / 60.0
    apex_rate_sum = res["apex"][h]["abs"] * 100.0  # (1 cm)^2 normalizasyonu
    t_each = apex_dose_gy / (apex_rate_sum * gy_per_min_per_ci_at_1cm * activity_ci)
    return t_each * n, n

if __name__ == "__main__":
    print("Yb-169 HDR episkleral aplikatör, kaba geometri/doz tablosu")
    print(f"R_sklera={R_SCLERA} mm, dwell offset={DWELL_OFFSET} mm, "
          f"kanal aralığı={CHANNEL_PITCH} mm, dwell adımı={DWELL_STEP} mm\n")
    for off in (1.0, 1.5, 2.0):
        DWELL_OFFSET = off
        print(f"--- dwell offset = {off} mm ---")
        print(f"{'Çap':>4} {'Kanal':>5} {'Aralık':>6} {'Dwell':>5} {'Yay(max)':>9} | "
              f"{'h=3':>11} {'h=5':>11} {'h=8':>11} {'h=10':>11}")
        print(" " * 36 + "| sklera/apeks oranı (merkez / sıcak nokta)")
        for dia in (12, 14, 16, 18, 20, 22):
            r = evaluate(dia)
            cells = []
            for h in (3, 5, 8, 10):
                a = r["apex"][h]
                cells.append(f"{a['ratio_center']:4.1f}/{a['ratio_hot']:4.1f}")
            print(f"{dia:>4} {r['n_channels']:>5} {r['pitch']:>6.2f} {r['n_dwells']:>5} "
                  f"{r['arc_max']:>8.1f}mm | " + " ".join(f"{c:>11}" for c in cells))
        print()
    DWELL_OFFSET = 1.5
    print("\nToplam bekleme süresi tahmini, 25 Gy apeks, 16 mm plak:")
    for h in (3, 5, 8):
        for act in (8, 4, 2):
            t, n = dwell_time_estimate(16, h, act, 25.0)
            print(f"  h={h} mm, {act} Ci: {t:5.1f} dk ({n} dwell)")
    # kiriş sagittası: düz kanal ile küre arasındaki sapma
    print("\nDüz kiriş ile küre yüzeyi arasındaki sapma (sagitta), Rd=13.3 mm:")
    for chord in (8, 10, 12, 14, 16):
        c = chord / 2
        print(f"  kiriş {chord} mm: {13.3 - math.sqrt(13.3**2 - c*c):.2f} mm")
