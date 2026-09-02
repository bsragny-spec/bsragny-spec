#!/usr/bin/env python3
"""
Kanal düzeni karşılaştırması ve bekleme süresi optimizasyonu.

Prensipler (kullanıcı kararı):
  - Plak çapı = tümör tabanı en geniş çapı + 4 mm
  - Kenar tam yükseklikte altın kalkanla kapalı
  - Plağa tek giriş; içeride kanal düzeni en iyi olanı

Model, geometry.py ile aynı basitleştirmelerle: nokta kaynak, ters kare × g(r),
küre göz. Tümör: iç sklera üzerine oturan elipsoid kubbe (taban çapı b, apeks h).
Amaç: tümör yüzeyinin her noktası >= reçete dozu iken sklera maksimumunu en aza indir
(doğrusal programlama, bekleme süreleri >= 0).
"""
import math, sys
import numpy as np
from scipy.optimize import linprog

R_OUT = 12.3      # dış sklera (plak temas yüzeyi)
R_IN = 11.3       # iç sklera (tümör tabanı)
OFFSET = 1.5      # bekleme ekseni skleradan yükseklik
R_D = R_OUT + OFFSET
STEP = 2.5        # bekleme adımı (mm)
TIP_DEAD = 2.0
EDGE = 1.5        # plak kenarından kanal eksenine en az mesafe

def g_r(d):
    r = max(d, 0.5) / 10.0
    return 1.0 + (0.05 if r < 1 else 0.04) * math.log(r)

def kernel(p, q):
    d = max(np.linalg.norm(p - q), 0.5)
    return g_r(d) / (d * d)

def on_sphere(x, y, R):
    """Plak taban düzlemindeki (x,y) noktasını R yarıçaplı küreye izdüşür."""
    z = math.sqrt(max(R * R - x * x - y * y, 0.0))
    return np.array([x, y, z])

# ---------- kanal düzenleri ----------
def chords(D, n):
    half = D / 2 - EDGE
    pitch = 2 * (half - 1.0) / (n - 1) if n > 1 else 0.0
    xs = [(-(n - 1) / 2 + i) * pitch for i in range(n)]
    dw, bend = [], R_D
    for x in xs:
        c = math.sqrt(max(half * half - x * x, 0))
        y0, y1 = -c + 0.5, c - TIP_DEAD
        k = int((y1 - y0) // STEP) + 1
        for i in range(k):
            dw.append(on_sphere(x, y0 + i * STEP, R_D))
    return np.array(dw), bend, f"{n} paralel kiriş"

def single_chord(D):
    return chords(D, 1)[0], R_D, "tek çap kirişi"

def c_ring(D, r=None, center=True):
    half = D / 2 - EDGE
    r = half - 0.5 if r is None else r
    circ = 2 * math.pi * r
    k = int((circ - TIP_DEAD - 1.0) // STEP) + 1
    dw = [on_sphere(r * math.cos(2 * math.pi * i * STEP / circ + math.pi / 2),
                    r * math.sin(2 * math.pi * i * STEP / circ + math.pi / 2), R_D)
          for i in range(k)]
    bend = 1 / math.sqrt(1 / r ** 2 + 1 / R_D ** 2)
    name = f"C halkası r={r:.1f}"
    if center:
        dw.append(on_sphere(0, 0, R_D)); name += " + merkez"
    return np.array(dw), bend, name

def concentric(D):
    half = D / 2 - EDGE
    rings = [half - 0.5]
    r = half - 0.5 - 2.75
    while r > 1.5:
        rings.append(r); r -= 2.75
    dw, bend = [np.array(on_sphere(0, 0, R_D))], None
    for r in rings:
        d, b, _ = c_ring(D, r, center=False)
        dw.extend(d); bend = b if bend is None else min(bend, b)
    return np.array(dw), bend, f"eş merkezli {len(rings)} halka + merkez"

# ---------- hedef ve risk noktaları ----------
def tumor_points(b, h, n_rho=7, n_az=12):
    pts = []
    for i in range(n_rho + 1):
        rho = (b / 2) * i / n_rho
        hh = h * math.sqrt(max(1 - (rho / (b / 2)) ** 2, 0))
        phi = rho / R_IN
        rr = R_IN - hh
        for j in range(n_az):
            az = 2 * math.pi * j / n_az
            pts.append([rr * math.sin(phi) * math.cos(az), rr * math.sin(phi) * math.sin(az), rr * math.cos(phi)])
    return np.array(pts)

def sclera_points(D, n=9):
    pts = []
    half = D / 2
    for x in np.linspace(-half + 1, half - 1, n):
        for y in np.linspace(-half + 1, half - 1, n):
            if x * x + y * y <= (half - 1) ** 2:
                pts.append(on_sphere(x, y, R_OUT))
    return np.array(pts)

def evaluate(dw, tp, sp):
    A_t = np.array([[kernel(p, q) for q in dw] for p in tp])
    A_s = np.array([[kernel(p, q) for q in dw] for p in sp])
    n = len(dw)
    # eşit süre
    w = np.ones(n)
    eq = (A_s @ w).max() / (A_t @ w).min()
    # LP: min t ; A_t w >= 1 ; A_s w <= t ; w >= 0
    c = np.zeros(n + 1); c[-1] = 1
    A_ub = np.vstack([np.hstack([-A_t, np.zeros((len(tp), 1))]),
                      np.hstack([A_s, -np.ones((len(sp), 1))])])
    b_ub = np.hstack([-np.ones(len(tp)), np.zeros(len(sp))])
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0, None)] * n + [(0, None)], method="highs")
    if not res.success:
        return eq, None, None
    w = res.x[:n]
    opt = (A_s @ w).max() / (A_t @ w).min()
    return eq, opt, w.sum()

def run(b, h):
    D = b + 4
    tp, sp = tumor_points(b, h), sclera_points(D)
    layouts = [single_chord(D), chords(D, 3), chords(D, 5), chords(D, 7),
               c_ring(D), concentric(D)]
    print(f"\nTümör tabanı {b} mm, apeks {h} mm  ->  plak {D} mm")
    print(f"{'Düzen':<30}{'Dwell':>6}{'Bükülme R':>11}{'Sklera/Rx eşit':>16}{'Sklera/Rx opt.':>16}{'Süre (göreli)':>15}")
    base_time = None
    for dw, bend, name in layouts:
        eq, opt, T = evaluate(dw, tp, sp)
        feas = "" if bend >= 12 else "  (kablo ile olmaz)"
        if T is not None and base_time is None: base_time = T
        tstr = f"{T / base_time:.2f}" if T else "-"
        ostr = f"{opt:.1f}" if opt else "-"
        print(f"{name:<30}{len(dw):>6}{bend:>9.1f}mm{eq:>16.1f}{ostr:>16}{tstr:>15}{feas}")

def tumor_points_offset(b, h, yc, n_rho=7, n_az=12):
    """Tümör merkezi plak ekseninden yc kadar kaymış (küre üzerinde y yönünde)."""
    pts = tumor_points(b, h, n_rho, n_az)
    out = []
    ang = yc / R_IN
    for x, y, z in pts:
        # y-z düzleminde ang kadar döndür
        y2 = y * math.cos(ang) + z * math.sin(ang)
        z2 = -y * math.sin(ang) + z * math.cos(ang)
        out.append([x, y2, z2])
    return np.array(out)

def run_notched(D, h):
    """Jukstapapiller tümör: taban çapı D-4, posterior kenarı çentik dibinde (y=+5)."""
    import geometry as G
    b = D - 4
    yc = (G.NOTCH_CY - G.NOTCH_R) - b / 2.0   # tümör posterior kenarı çentik dibinde
    tp = tumor_points_offset(b, h, yc)
    sp = sclera_points(D)
    disc = np.array([on_sphere(0, 0, R_IN)])
    disc = tumor_points_offset(0.01, 0.0, G.NOTCH_CY)[:1]  # disk merkezi: çentik merkezi, iç sklera
    print(f"\nÇentikli karşılaştırma: plak {D} mm, tümör tabanı {b} mm, apeks {h} mm, tümör merkezi y={yc:+.1f} mm, disk y=+{G.NOTCH_CY:.0f} mm")
    print(f"{'Düzen':<34}{'Dwell':>6}{'Sklera/Rx opt.':>16}{'Disk/Rx opt.':>14}")
    for notched in (False, True):
        ch = G.plaque_layout(D, notched=notched)
        dw = np.array([d for c in ch for d in c["dwells"]])
        A_t = np.array([[kernel(p, q) for q in dw] for p in tp])
        A_s = np.array([[kernel(p, q) for q in dw] for p in sp])
        A_d = np.array([[kernel(p, q) for q in dw] for p in disc])
        n = len(dw)
        c = np.zeros(n + 1); c[-1] = 1
        A_ub = np.vstack([np.hstack([-A_t, np.zeros((len(tp), 1))]),
                          np.hstack([A_s, -np.ones((len(sp), 1))])])
        b_ub = np.hstack([-np.ones(len(tp)), np.zeros(len(sp))])
        res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0, None)] * (n + 1), method="highs")
        w = res.x[:n]
        rx = (A_t @ w).min()
        name = ("çentikli, " if notched else "yuvarlak (sinir yok sayılır), ") + f"{len(ch)} kanal"
        print(f"{name:<34}{n:>6}{(A_s @ w).max() / rx:>16.1f}{(A_d @ w).max() / rx:>14.2f}")

if __name__ == "__main__":
    for b, h in ((8, 3), (12, 5), (12, 8), (16, 5)):
        run(b, h)
    for D, h in ((16, 5), (20, 5)):
        run_notched(D, h)
    print("\nSklera/Rx: plak altındaki en yüksek dış sklera dozu / tümör yüzeyindeki en düşük doz (reçete).")
    print("Süre: aynı reçete için toplam bekleme süresi, ilk satıra göre. Bükülme R < 12 mm kablo sürücülü kaynakla uygulanamaz.")
