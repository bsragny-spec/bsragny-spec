#!/usr/bin/env python3
"""
Plak ailesi çizimleri (12, 14, 16, 18, 20, 22 mm): üstten görünüş + kesit, SVG.
Kanal yerleşimi geometry.py kurallarıyla aynıdır.
Çıktı: figures/plak-XXmm.svg (her boy) ve figures/plak-ailesi.svg (tek sayfa).
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import geometry as G

SIZES = (12, 14, 16, 18, 20, 22)
R_SCL = G.R_SCLERA          # 12.3
OFF = G.DWELL_OFFSET        # 1.5
T_SPACER, T_CHAN, T_SHIELD = 0.85, 1.90, 1.50
CH_ID, CH_OD = 1.2, 1.6
RIM = 0.5

def layout(D):
    return G.plaque_layout(D)

def top_view(D, S, ox, oy, full=True):
    """Üstten görünüş. S: px/mm. (ox,oy): plak merkezi."""
    e = []
    r = D / 2
    ch = layout(D)
    pitch = ch[0]["pitch"]
    # kabuk ve kenar
    e.append(f'<circle cx="{ox}" cy="{oy}" r="{r*S:.1f}" fill="#e6c96a" stroke="#8a6d1a" stroke-width="1.4"/>')
    e.append(f'<circle cx="{ox}" cy="{oy}" r="{(r-RIM)*S:.1f}" fill="#eef4f7" stroke="#8a6d1a" stroke-width="0.7"/>')
    # sütür delikleri: 2 posterior 45°, 1 anterior sol
    for ang in (45, 135, 200):
        a = math.radians(ang)
        e.append(f'<circle cx="{ox + (r-0.9)*S*math.cos(a):.1f}" cy="{oy - (r-0.9)*S*math.sin(a):.1f}" r="{0.4*S:.1f}" fill="#fff" stroke="#8a6d1a" stroke-width="0.8"/>')
    # kanallar (anterior = alt)
    half = r - G.EDGE_MARGIN
    for c in ch:
        x = c["x"]; chalf = c["chord"] / 2
        x0 = ox + x * S
        y_top = oy - chalf * S          # kör uç tarafı (posterior, üst)
        y_bot = oy + chalf * S          # giriş tarafı (anterior, alt)
        e.append(f'<rect x="{x0 - CH_OD/2*S:.1f}" y="{y_top:.1f}" width="{CH_OD*S:.1f}" height="{(y_bot-y_top):.1f}" rx="{CH_OD/2*S:.1f}" fill="#b8c7d1" stroke="#2b4c5e" stroke-width="0.8"/>')
        e.append(f'<rect x="{x0 - CH_ID/2*S:.1f}" y="{y_top + 0.2*S:.1f}" width="{CH_ID*S:.1f}" height="{(y_bot-y_top-0.2*S):.1f}" rx="{CH_ID/2*S:.1f}" fill="#fff"/>')
        # ölü boşluk
        e.append(f'<rect x="{x0 - CH_ID/2*S:.1f}" y="{y_top + 0.2*S:.1f}" width="{CH_ID*S:.1f}" height="{G.TIP_DEAD*S:.1f}" rx="{CH_ID/2*S:.1f}" fill="#f3d1cc"/>')
        # bekleme pozisyonları
        for (dx, dy, dz) in c["dwells"]:
            e.append(f'<circle cx="{ox + dx*S:.1f}" cy="{oy - dy*S:.1f}" r="{0.28*S:.1f}" fill="#c0392b"/>')
        # bloğa bağlantı
        e.append(f'<line x1="{x0:.1f}" y1="{y_bot:.1f}" x2="{x0:.1f}" y2="{oy + (r+1.0)*S:.1f}" stroke="#2b4c5e" stroke-width="0.8"/>')
    # giriş bloğu
    bw = (ch[-1]["x"] - ch[0]["x"] + 3.0) * S; bh = 2.2 * S
    e.append(f'<rect x="{ox - bw/2:.1f}" y="{oy + (r+1.0)*S:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="{0.4*S:.1f}" fill="#9fb3c0" stroke="#2b4c5e" stroke-width="1"/>')
    for i, c in enumerate(ch):
        cx = ox + c["x"] * S; cy = oy + (r + 2.1) * S
        e.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{0.45*S:.1f}" fill="#fff" stroke="#2b4c5e" stroke-width="0.7"/>')
        if full:
            e.append(f'<text x="{cx:.1f}" y="{cy + 0.3*S:.1f}" text-anchor="middle" font-size="{0.7*S:.0f}" fill="#2b4c5e">{i+1}</text>')
    # tek kılıf
    y0 = oy + (r + 3.2) * S
    e.append(f'<path d="M {ox} {y0:.1f} C {ox} {y0 + 3*S:.1f} {ox + 2*S:.1f} {y0 + 4*S:.1f} {ox + 4*S:.1f} {y0 + 6*S:.1f}" stroke="#2b4c5e" stroke-width="{0.8*S:.1f}" fill="none" stroke-linecap="round"/>')
    e.append(f'<path d="M {ox} {y0:.1f} C {ox} {y0 + 3*S:.1f} {ox + 2*S:.1f} {y0 + 4*S:.1f} {ox + 4*S:.1f} {y0 + 6*S:.1f}" stroke="#dfe7ec" stroke-width="{0.45*S:.1f}" fill="none" stroke-linecap="round"/>')
    # çap ölçüsü
    yd = oy - (r + 1.6) * S
    e.append(f'<line x1="{ox - r*S:.1f}" y1="{yd:.1f}" x2="{ox + r*S:.1f}" y2="{yd:.1f}" stroke="#333" stroke-width="0.7"/>')
    e.append(f'<line x1="{ox - r*S:.1f}" y1="{yd-0.5*S:.1f}" x2="{ox - r*S:.1f}" y2="{yd+0.5*S:.1f}" stroke="#333" stroke-width="0.7"/>')
    e.append(f'<line x1="{ox + r*S:.1f}" y1="{yd-0.5*S:.1f}" x2="{ox + r*S:.1f}" y2="{yd+0.5*S:.1f}" stroke="#333" stroke-width="0.7"/>')
    e.append(f'<text x="{ox}" y="{yd - 0.4*S:.1f}" text-anchor="middle" font-size="{max(10, 0.95*S):.0f}" font-weight="bold">Ø {D} mm</text>')
    n_dw = sum(len(c["dwells"]) for c in ch)
    return "\n".join(e), dict(n=len(ch), pitch=pitch, n_dw=n_dw, arc=max(c["arc"] for c in ch))

def section(D, S, ox, cy, label=True):
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
    for c in layout(D):
        a = math.asin(c["x"] / Rd)
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

def single(D):
    S = 10
    W, H = 640, 640
    body = [f'<text x="{W/2}" y="24" text-anchor="middle" font-size="15" font-weight="bold">Yb-169 HDR episkleral aplikatör, {D} mm plak (ölçek 10 px = 1 mm)</text>']
    tv, info = top_view(D, S, 200, 190)
    body.append(tv)
    sc, sinfo = section(D, S, 470, 300)
    body.append(sc)
    body.append(f'<text x="200" y="{190 + (D/2 + 11.5) * S:.0f}" text-anchor="middle" font-size="11" fill="#555">Üstten görünüş, anterior (giriş bloğu) altta</text>')
    body.append(f'<text x="470" y="{300 - (R_SCL + 4.5) * S:.0f}" text-anchor="middle" font-size="11" fill="#555">Kesit, kanal eksenine dik</text>')
    y = 470
    rows = [
        f"Çap {D} mm, tümör tabanı ≤ {D-4} mm için",
        f"Kanal: {info['n']} paralel kör kiriş, aralık {info['pitch']:.2f} mm, iç çap {CH_ID} mm",
        f"Bekleme pozisyonu: {info['n_dw']} adet, adım {G.DWELL_STEP} mm, kör uç ölü boşluğu {G.TIP_DEAD} mm",
        f"En uzun kanal yayı {info['arc']:.1f} mm; eksen skleradan {OFF} mm, küre yarıçapı {R_SCL+OFF} mm",
        f"Katmanlar: ara katman {T_SPACER} mm, kanal katmanı {T_CHAN} mm, altın sırt {T_SHIELD} mm; kenar kalkanı {RIM} mm tam yükseklik",
        f"Kubbe derinliği (sagitta) {sinfo['sag']:.1f} mm, yarım açı {sinfo['th']:.0f}°; iç eğrilik yarıçapı {R_SCL} mm",
        "Sütür deliği 3 adet, Ø 0,8 mm. Tek giriş bloğu, tek kilitli konektör, tek kılıf.",
    ]
    for i, t in enumerate(rows):
        body.append(f'<text x="40" y="{y + i*18}" font-size="11" fill="#222">{t}</text>')
    body.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="10" fill="#777">Şematik tasarım çizimi, taslak v0.1. Üretim çizimi değildir; toleranslar belge 02.</text>')
    return svg_wrap(W, H, "\n".join(body), f"{D} mm plak"), info, sinfo

def family():
    S = 6
    cols, cw, chh = 3, 330, 400
    W, H = cols * cw + 40, 2 * chh + 70
    body = [f'<text x="{W/2}" y="26" text-anchor="middle" font-size="16" font-weight="bold">Yb-169 HDR episkleral aplikatör ailesi, 12 ile 22 mm (ölçek 6 px = 1 mm)</text>']
    for i, D in enumerate(SIZES):
        cx = 20 + (i % cols) * cw + cw / 2
        cy = 60 + (i // cols) * chh
        tv, info = top_view(D, S, cx, cy + 105, full=False)
        body.append(tv)
        sc, sinfo = section(D, S, cx, cy + 370)
        body.append(sc)
        body.append(f'<text x="{cx}" y="{cy + 105 + (D/2 + 10) * S:.0f}" text-anchor="middle" font-size="10" fill="#333">'
                    f"{info['n']} kanal, aralık {info['pitch']:.2f} mm, {info['n_dw']} dwell, taban ≤ {D-4} mm</text>")
    body.append(f'<text x="{W/2}" y="{H-12}" text-anchor="middle" font-size="10" fill="#777">Her boy için üstten görünüş ve kanal eksenine dik kesit. Şematik, taslak v0.1.</text>')
    return svg_wrap(W, H, "\n".join(body), "Plak ailesi 12 ile 22 mm")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "figures")
    os.makedirs(out, exist_ok=True)
    print(f"{'Çap':>4} {'Kanal':>5} {'Aralık':>7} {'Dwell':>5} {'Yay':>7} {'Sagitta':>8} {'Yarım açı':>9}")
    for D in SIZES:
        svg, info, sinfo = single(D)
        open(os.path.join(out, f"plak-{D}mm.svg"), "w").write(svg)
        print(f"{D:>4} {info['n']:>5} {info['pitch']:>7.2f} {info['n_dw']:>5} {info['arc']:>6.1f} {sinfo['sag']:>7.1f} {sinfo['th']:>8.0f}°")
    open(os.path.join(out, "plak-ailesi.svg"), "w").write(family())
    print("yazıldı:", out)
