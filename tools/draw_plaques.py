#!/usr/bin/env python3
"""
Plak ailesi çizimleri (12, 14, 16, 18, 20, 22 mm): üstten görünüş + kesit, SVG.
Kanal yerleşimi geometry.py kurallarıyla aynıdır.
Çıktı: figures/plak-XXmm.svg (her boy) ve figures/plak-ailesi.svg (tek sayfa).
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import geometry as G

SIZES = (12, 14, 16, 18, 20)
NOTCHED = (16, 18, 20)      # çentikli sürümler (14 mm'de yan kanallara yer kalmaz)
R_SCL = G.R_SCLERA          # 12.3
OFF = G.DWELL_OFFSET        # 1.5
T_SPACER, T_CHAN, T_SHIELD = 0.85, 1.90, 1.50
CH_ID, CH_OD = 1.2, 1.6
RIM = 0.5

def layout(D, notched=False):
    return G.fan_layout(D, notched=notched)

def notched_outline(r, ox, oy, S, inset=0.0):
    """U çentikli plak dış hattı (posterior = üst). inset: kenar kalkanı iç hattı için."""
    R = (r - inset)
    nr = G.NOTCH_R + inset            # çentik yarıçapı iç hatta büyür
    cy_n = G.notch_center_y(2 * r)    # çentik yarım daire merkezi (merkezden posterior)
    # çentik kolları dış çemberi kestiği nokta: x = ±nr, y = sqrt(R^2 - nr^2)
    if nr >= R:
        return None
    yk = math.sqrt(R * R - nr * nr)
    # piksel: +y posterior = yukarı (oy - y*S)
    P = lambda x, y: f"{ox + x*S:.1f} {oy - y*S:.1f}"
    d = (f"M {P(nr, yk)} A {R*S:.1f} {R*S:.1f} 0 1 1 {P(-nr, yk)} "      # büyük yay (saat yönü tersi, sol kola)
         f"L {P(-nr, cy_n)} A {nr*S:.1f} {nr*S:.1f} 0 0 0 {P(nr, cy_n)} Z")  # çentik yarım dairesi
    return d

def top_view(D, S, ox, oy, full=True, notched=False):
    """Üstten görünüş. S: px/mm. (ox,oy): plak merkezi."""
    e = []
    r = D / 2
    ch = layout(D, notched)
    pitch = ch[0]["pitch"]
    # giriş sapı: kabukla tek parça (kabuktan önce çizilir), kenara teğet, yassı; ucunda lümenler, sonra yuvarlak kılıf
    n = len(ch); W = n * G.FAN_PITCH0 + 1.6; Ls = 4.0
    y_rim = oy + (r - 1.0) * S
    e.append(f'<rect x="{ox - W/2*S:.1f}" y="{y_rim:.1f}" width="{W*S:.1f}" height="{(Ls + 1.0)*S:.1f}" rx="{1.0*S:.1f}" fill="#e6c96a" stroke="#8a6d1a" stroke-width="1.2"/>')
    y0 = y_rim + (Ls + 1.0) * S
    e.append(f'<rect x="{ox - 2.4*S:.1f}" y="{y0 - 0.2*S:.1f}" width="{4.8*S:.1f}" height="{5.0*S:.1f}" rx="{2.4*S:.1f}" fill="#dfe7ec" stroke="#2b4c5e" stroke-width="0.9"/>')
    for c in ch:
        cx = ox + c["x"] * S; cy = y_rim + (Ls + 0.1) * S
        e.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{CH_ID/2*S:.1f}" fill="#fff" stroke="#2b4c5e" stroke-width="0.6"/>')
    if full:
        e.append(f'<text x="{ox + (W/2 + 0.8)*S:.1f}" y="{y_rim + 2.6*S:.1f}" font-size="{max(9, 0.8*S):.0f}" fill="#555">sap {W:.1f} × 2 mm</text>')
        e.append(f'<text x="{ox + (W/2 + 0.8)*S:.1f}" y="{y_rim + 3.8*S:.1f}" font-size="{max(9, 0.8*S):.0f}" fill="#555">kabukla tek parça</text>')
        e.append(f'<text x="{ox + 2.9*S:.1f}" y="{y0 + 2.8*S:.1f}" font-size="{max(9, 0.8*S):.0f}" fill="#555">kılıf Ø 4,8 mm</text>')
    # kabuk ve kenar
    if notched:
        e.append(f'<path d="{notched_outline(r, ox, oy, S)}" fill="#e6c96a" stroke="#8a6d1a" stroke-width="1.4"/>')
        e.append(f'<path d="{notched_outline(r, ox, oy, S, RIM)}" fill="#eef4f7" stroke="#8a6d1a" stroke-width="0.7"/>')
    else:
        e.append(f'<circle cx="{ox}" cy="{oy}" r="{r*S:.1f}" fill="#e6c96a" stroke="#8a6d1a" stroke-width="1.4"/>')
        e.append(f'<circle cx="{ox}" cy="{oy}" r="{(r-RIM)*S:.1f}" fill="#eef4f7" stroke="#8a6d1a" stroke-width="0.7"/>')
    # sütür delikleri: yuvarlakta 2 posterior 45°, 1 anterior sol; çentiklide 2 lateral, 1 anterior
    for ang in ((10, 170, 200) if notched else (45, 135, 200)):
        a = math.radians(ang)
        e.append(f'<circle cx="{ox + (r-0.9)*S*math.cos(a):.1f}" cy="{oy - (r-0.9)*S*math.sin(a):.1f}" r="{0.4*S:.1f}" fill="#fff" stroke="#8a6d1a" stroke-width="0.8"/>')
    # kanallar: anterior kenardaki dar giriş sırasından açılan düz ışınlar
    for c in ch:
        (xa, ya), (xb, yb) = c["start"], c["end"]
        Xa, Ya, Xb, Yb = ox + xa * S, oy - ya * S, ox + xb * S, oy - yb * S
        L = math.hypot(Xb - Xa, Yb - Ya); ang = math.degrees(math.atan2(Yb - Ya, Xb - Xa))
        tr = f'transform="translate({Xa:.1f},{Ya:.1f}) rotate({ang:.2f})"'
        e.append(f'<rect x="{-0.3*S:.1f}" y="{-CH_OD/2*S:.1f}" width="{L + 0.3*S:.1f}" height="{CH_OD*S:.1f}" rx="{CH_OD/2*S:.1f}" fill="#b8c7d1" stroke="#2b4c5e" stroke-width="0.8" {tr}/>')
        e.append(f'<rect x="{-0.3*S:.1f}" y="{-CH_ID/2*S:.1f}" width="{L + 0.1*S:.1f}" height="{CH_ID*S:.1f}" rx="{CH_ID/2*S:.1f}" fill="#fff" {tr}/>')
        e.append(f'<rect x="{L - G.TIP_DEAD*S - 0.2*S:.1f}" y="{-CH_ID/2*S:.1f}" width="{G.TIP_DEAD*S:.1f}" height="{CH_ID*S:.1f}" rx="{CH_ID/2*S:.1f}" fill="#f3d1cc" {tr}/>')
        for (dx, dy, dz) in c["dwells"]:
            e.append(f'<circle cx="{ox + dx*S:.1f}" cy="{oy - dy*S:.1f}" r="{0.28*S:.1f}" fill="#c0392b"/>')
    # çap ölçüsü
    yd = oy - (r + 1.6) * S
    e.append(f'<line x1="{ox - r*S:.1f}" y1="{yd:.1f}" x2="{ox + r*S:.1f}" y2="{yd:.1f}" stroke="#333" stroke-width="0.7"/>')
    e.append(f'<line x1="{ox - r*S:.1f}" y1="{yd-0.5*S:.1f}" x2="{ox - r*S:.1f}" y2="{yd+0.5*S:.1f}" stroke="#333" stroke-width="0.7"/>')
    e.append(f'<line x1="{ox + r*S:.1f}" y1="{yd-0.5*S:.1f}" x2="{ox + r*S:.1f}" y2="{yd+0.5*S:.1f}" stroke="#333" stroke-width="0.7"/>')
    e.append(f'<text x="{ox}" y="{yd - 0.4*S:.1f}" text-anchor="middle" font-size="{max(10, 0.95*S):.0f}" font-weight="bold">Ø {D} mm</text>')
    n_dw = sum(len(c["dwells"]) for c in ch)
    if notched and full:
        # çentik ölçüleri
        ncy = G.notch_center_y(D)
        e.append(f'<line x1="{ox + G.NOTCH_R*S*0.6:.1f}" y1="{oy - (ncy - 1.0)*S:.1f}" x2="{ox + (r + 1.5)*S:.1f}" y2="{oy - (r - 0.5)*S:.1f}" stroke="#7a3c3c" stroke-width="0.7"/>')
        e.append(f'<text x="{ox + (r + 1.7)*S:.1f}" y="{oy - (r - 0.5)*S:.1f}" text-anchor="start" font-size="{max(9, 0.8*S):.0f}" fill="#7a3c3c">çentik {G.NOTCH_W:.0f} mm</text>')
        e.append(f'<text x="{ox + (r + 1.7)*S:.1f}" y="{oy - (r - 0.5)*S + 12:.1f}" text-anchor="start" font-size="{max(9, 0.8*S):.0f}" fill="#7a3c3c">sinir ekseni merkezden {G.notch_center_y(D):.0f} mm</text>')
        e.append(f'<text x="{ox + (r + 1.7)*S:.1f}" y="{oy - (r - 0.5)*S + 24:.1f}" text-anchor="start" font-size="{max(9, 0.8*S):.0f}" fill="#7a3c3c">dip merkezden {ncy - G.NOTCH_R:.0f} mm</text>')
    return "\n".join(e), dict(n=len(ch), pitch=pitch, n_dw=n_dw, arc=max(c["arc"] for c in ch),
                             n_trunc=sum(1 for c in ch if c["truncated"]))

def section(D, S, ox, cy, label=True, notched=False):
    """Kanal eksenine dik kesit. (ox, cy): küre merkezi (px)."""
    e = []
    r = D / 2
    th = math.asin(min(r / R_SCL, 1.0))
    def pt(R, a):
        return ox + R * S * math.sin(a), cy - R * S * math.cos(a)
    def sector(R1, R2, fill, stroke, sw=1.0):
        x1l, y1l = pt(R1, -th); x1r, y1r = pt(R1, th); x2r, y2r = pt(R2, th); x2l, y2l = pt(R2, -th)
        return (f'<path d="M {x1l:.1f} {y1l:.1f} A {R1*S:.1f} {R1*S:.1f} 0 0 1 {x1r:.1f} {y1r:.1f} '
                f'L {x2r:.1f} {y2r:.1f} A {R2*S:.1f} {R2*S:.1f} 0 0 0 {x2l:.1f} {y2l:.1f} Z" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    # göz ve sklera
    e.append(f'<circle cx="{ox}" cy="{cy}" r="{(R_SCL-1)*S:.1f}" fill="#fdf3e7"/>')
    thw = min(th + 0.35, math.pi / 2)
    x1l, y1l = pt(R_SCL, -thw); x1r, y1r = pt(R_SCL, thw); x2r, y2r = pt(R_SCL-1, thw); x2l, y2l = pt(R_SCL-1, -thw)
    e.append(f'<path d="M {x1l:.1f} {y1l:.1f} A {R_SCL*S:.1f} {R_SCL*S:.1f} 0 0 1 {x1r:.1f} {y1r:.1f} L {x2r:.1f} {y2r:.1f} A {(R_SCL-1)*S:.1f} {(R_SCL-1)*S:.1f} 0 0 0 {x2l:.1f} {y2l:.1f} Z" fill="#e8dcc8" stroke="#8a7a60" stroke-width="0.8"/>')
    # katmanlar
    R1 = R_SCL; R2 = R1 + T_SPACER; R3 = R2 + T_CHAN; R4 = R3 + T_SHIELD
    e.append(sector(R1, R2, "#d9ecf5", "#4a7c96", 0.8))
    e.append(sector(R2, R3, "#eef4f7", "#4a7c96", 0.8))
    e.append(sector(R3, R4, "#e6c96a", "#8a6d1a", 1.2))
    # kenar kalkanı: tam yükseklik, 0,5 mm
    for sgn in (-1, 1):
        a_out = sgn * th; a_in = sgn * math.asin(min((r - RIM) / R_SCL, 1.0))
        xa, ya = pt(R4, a_out); xb, yb = pt(R1, a_out); xc, yc = pt(R1, a_in); xd, yd = pt(R4, a_in)
        e.append(f'<path d="M {xa:.1f} {ya:.1f} L {xb:.1f} {yb:.1f} L {xc:.1f} {yc:.1f} L {xd:.1f} {yd:.1f} Z" fill="#e6c96a" stroke="#8a6d1a" stroke-width="1"/>')
    # kanallar
    Rd = R_SCL + OFF
    for c in layout(D, notched):
        (xa, ya), (xb, yb) = c["start"], c["end"]
        if ya >= 0 or yb <= 0: continue
        xc = xa + (0 - ya) / (yb - ya) * (xb - xa)
        a = math.asin(max(min(xc / Rd, 1), -1))
        x, y = pt(Rd, a)
        e.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{CH_OD/2*S:.1f}" fill="#b8c7d1" stroke="#2b4c5e" stroke-width="0.7"/>')
        e.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{CH_ID/2*S:.1f}" fill="#fff"/>')
    x, y = pt(Rd, 0)
    e.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{0.35*S:.1f}" fill="#c0392b"/>')
    # kalınlık ölçüsü
    xl = ox + (r + 2.5) * S
    ya = cy - R4 * S; yb = cy - R1 * S
    e.append(f'<line x1="{xl:.1f}" y1="{ya:.1f}" x2="{xl:.1f}" y2="{yb:.1f}" stroke="#333" stroke-width="0.7"/>')
    e.append(f'<line x1="{xl-3}" y1="{ya:.1f}" x2="{xl+3}" y2="{ya:.1f}" stroke="#333" stroke-width="0.7"/>')
    e.append(f'<line x1="{xl-3}" y1="{yb:.1f}" x2="{xl+3}" y2="{yb:.1f}" stroke="#333" stroke-width="0.7"/>')
    e.append(f'<text x="{xl + 0.5*S:.1f}" y="{(ya+yb)/2 + 3:.1f}" text-anchor="start" font-size="{max(9, 0.8*S):.0f}">{R4-R1:.2f} mm</text>')
    # kubbe derinliği (sagitta)
    sag = R_SCL - R_SCL * math.cos(th)
    return "\n".join(e), dict(sag=sag, th=math.degrees(th))

def svg_wrap(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'font-family="Arial, Helvetica, sans-serif" font-size="11">\n<title>{title}</title>\n'
            f'<rect width="{w}" height="{h}" fill="#ffffff"/>\n{body}\n</svg>\n')

def single(D, notched=False):
    S = 10
    W, H = 640, 600
    ttl = f"{D} mm {'çentikli ' if notched else ''}plak"
    body = [f'<text x="{W/2}" y="24" text-anchor="middle" font-size="15" font-weight="bold">Yb-169 HDR episkleral aplikatör, {ttl} (ölçek 10 px = 1 mm)</text>']
    tv, info = top_view(D, S, 200, 190, notched=notched)
    body.append(tv)
    sc, sinfo = section(D, S, 470, 300, notched=notched)
    body.append(sc)
    body.append(f'<text x="200" y="{190 + (D/2 + 12.5) * S:.0f}" text-anchor="middle" font-size="11" fill="#555">Üstten görünüş, anterior (giriş sapı) altta</text>')
    body.append(f'<text x="470" y="{300 - (R_SCL + 6.0) * S:.0f}" text-anchor="middle" font-size="11" fill="#555">Kesit, kanal eksenine dik</text>')
    y = 440
    rows = [
        (f"Çap {D} mm, çentikli: jukstapapiller tümör, taban ≤ {D-4} mm, posterior kenarı disk kenarında; bir boy büyük seçilir" if notched
         else f"Çap {D} mm, tümör tabanı ≤ {D-4} mm için"),
        (f"Kanal: {info['n']} yelpaze ışını, ±45°, giriş sırası aralığı {G.FAN_PITCH0} mm; {info['n_trunc']} tanesi çentikte kısaltılmış; iç çap {CH_ID} mm" if notched
         else f"Kanal: {info['n']} yelpaze ışını, ±45°, giriş sırası aralığı {G.FAN_PITCH0} mm, iç çap {CH_ID} mm"),
        f"Bekleme pozisyonu: {info['n_dw']} adet, adım {G.DWELL_STEP} mm, kör uç ölü boşluğu {G.TIP_DEAD} mm",
        f"En uzun kanal {info['arc']:.1f} mm; düzlemde düz, eğrilik yalnızca küreden ({R_SCL+OFF} mm); eksen skleradan {OFF} mm",
        f"Katmanlar: ara katman {T_SPACER} mm, kanal katmanı {T_CHAN} mm, altın sırt {T_SHIELD} mm; kenar kalkanı {RIM} mm tam yükseklik",
        f"Kubbe derinliği (sagitta) {sinfo['sag']:.1f} mm, yarım açı {sinfo['th']:.0f}°; iç eğrilik yarıçapı {R_SCL} mm",
        "Sütür deliği 3 adet, Ø 0,8 mm. Kabukla tek parça yassı sap, ucunda tek kilitli konektör ve Ø 4,5 mm kılıf.",
    ] + ([f"Çentik: U biçimli, genişlik {G.NOTCH_W:.0f} mm, sinir ekseni plak merkezinden {G.notch_center_y(D):.0f} mm (kenardan {G.NOTCH_INSET:.0f} mm içeride), dip merkezden {G.notch_center_y(D)-G.NOTCH_R:.0f} mm; kalkan çentiği izler"] if notched else [])
    for i, t in enumerate(rows):
        body.append(f'<text x="30" y="{y + i*17}" font-size="10.5" fill="#222">{t}</text>')
    body.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="10" fill="#777">Şematik tasarım çizimi, taslak v0.1. Üretim çizimi değildir; toleranslar belge 02.</text>')
    return svg_wrap(W, H, "\n".join(body), ttl), info, sinfo

def family():
    S = 6
    cols, cw, chh = 4, 250, 400
    items = [(D, False) for D in SIZES] + [(D, True) for D in NOTCHED]
    rows = math.ceil(len(items) / cols)
    W, H = cols * cw + 40, rows * chh + 70
    body = [f'<text x="{W/2}" y="26" text-anchor="middle" font-size="16" font-weight="bold">Yb-169 HDR episkleral aplikatör ailesi: yuvarlak 12 ile 20 mm, çentikli 16 ile 20 mm (ölçek 6 px = 1 mm)</text>']
    for i, (D, notched) in enumerate(items):
        cx = 20 + (i % cols) * cw + cw / 2
        cy = 60 + (i // cols) * chh
        tv, info = top_view(D, S, cx, cy + 105, full=False, notched=notched)
        body.append(tv)
        sc, sinfo = section(D, S, cx, cy + 370, notched=notched)
        body.append(sc)
        l1 = f"{D} mm {'çentikli' if notched else ''}: {info['n']} ışın, {info['n_dw']} dwell"
        l2 = (f"{info['n_trunc']} kısa + {info['n']-info['n_trunc']} yan ışın" if notched
              else f"yelpaze ±45°, taban ≤ {D-4} mm")
        if notched and D >= 20: l2 += ", ±55°"
        yl = cy + 105 + (D/2 + 11.5) * S
        body.append(f'<text x="{cx}" y="{yl:.0f}" text-anchor="middle" font-size="9.5" fill="#333">{l1}</text>')
        body.append(f'<text x="{cx}" y="{yl+12:.0f}" text-anchor="middle" font-size="9.5" fill="#555">{l2}</text>')
    body.append(f'<text x="{W/2}" y="{H-12}" text-anchor="middle" font-size="10" fill="#777">Her boy için üstten görünüş (posterior üstte, giriş sapı anteriorda) ve kanal eksenine dik kesit. Şematik, taslak v0.1.</text>')
    return svg_wrap(W, H, "\n".join(body), "Plak ailesi")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "figures")
    os.makedirs(out, exist_ok=True)
    print(f"{'Çap':>4} {'Işın':>5} {'Giriş':>7} {'Dwell':>5} {'Uzun':>7} {'Sagitta':>8} {'Yarım açı':>9}")
    for D in SIZES:
        svg, info, sinfo = single(D)
        open(os.path.join(out, f"plak-{D}mm.svg"), "w").write(svg)
        print(f"{D:>4} {info['n']:>5} {info['pitch']:>7.2f} {info['n_dw']:>5} {info['arc']:>6.1f} {sinfo['sag']:>7.1f} {sinfo['th']:>8.0f}°")
    for D in NOTCHED:
        svg, info, sinfo = single(D, notched=True)
        open(os.path.join(out, f"plak-{D}mm-centik.svg"), "w").write(svg)
        print(f"{D:>4}N {info['n']:>4} {info['pitch']:>7.2f} {info['n_dw']:>5} {info['arc']:>6.1f}   ({info['n_trunc']} kısa kanal)")
    open(os.path.join(out, "plak-ailesi.svg"), "w").write(family())
    print("yazıldı:", out)
