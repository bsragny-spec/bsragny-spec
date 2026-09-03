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
FILLET = 1.5   # dış kenar yuvarlatma yarıçapı

def layout(D, notched=False):
    return G.plaque_layout(D, notched=notched)

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
    # giriş: her kanal anterior kenardan KENDİ altın ağzıyla çıkar, kendi kateteri ve kablosu vardır
    # (kabuktan önce çizilir; ağız kabukla tek parça görünür)
    NOZ_OD, NOZ_L, CAT_OD, CAT_L = 2.4, 3.0, 2.0, 9.0
    for c in ch:
        x0 = ox + c["x"] * S; y_rim = oy - c["y_start"] * S - 1.0 * S
        e.append(f'<rect x="{x0 - NOZ_OD/2*S:.1f}" y="{y_rim:.1f}" width="{NOZ_OD*S:.1f}" height="{(NOZ_L + 1.0)*S:.1f}" rx="{0.6*S:.1f}" fill="#e6c96a" stroke="#8a6d1a" stroke-width="1.0"/>')
        yc0 = y_rim + (NOZ_L + 1.0) * S
        e.append(f'<path d="M {x0:.1f} {yc0:.1f} C {x0:.1f} {yc0 + 4*S:.1f} {x0 + c["x"]*0.15*S:.1f} {yc0 + 6*S:.1f} {x0 + c["x"]*0.25*S:.1f} {yc0 + CAT_L*S:.1f}" stroke="#2b4c5e" stroke-width="{CAT_OD*S:.1f}" fill="none" stroke-linecap="round"/>')
        e.append(f'<path d="M {x0:.1f} {yc0:.1f} C {x0:.1f} {yc0 + 4*S:.1f} {x0 + c["x"]*0.15*S:.1f} {yc0 + 6*S:.1f} {x0 + c["x"]*0.25*S:.1f} {yc0 + CAT_L*S:.1f}" stroke="#dfe7ec" stroke-width="{(CAT_OD - 0.5)*S:.1f}" fill="none" stroke-linecap="round"/>')
        e.append(f'<circle cx="{x0:.1f}" cy="{y_rim + (NOZ_L + 0.4)*S:.1f}" r="{CH_ID/2*S:.1f}" fill="#fff" stroke="#2b4c5e" stroke-width="0.5"/>')
    if full:
        yl = oy + (r + NOZ_L + CAT_L + 1.5) * S
        e.append(f'<text x="{ox:.1f}" y="{yl:.1f}" text-anchor="middle" font-size="{max(9, 0.8*S):.0f}" fill="#555">kanal başına altın ağız Ø {NOZ_OD} × {NOZ_L:.0f} mm ve ayrı kateter Ø {CAT_OD} mm</text>')
    # kabuk ve kenar
    if notched:
        e.append(f'<path d="{notched_outline(r, ox, oy, S)}" fill="#efdca0" stroke="#8a6d1a" stroke-width="1.4"/>')     # yuvarlatılmış kenar bandı
        e.append(f'<path d="{notched_outline(r, ox, oy, S, FILLET)}" fill="#e6c96a" stroke="#c9ad4f" stroke-width="0.6"/>')  # düz sırt
        e.append(f'<path d="{notched_outline(r, ox, oy, S, RIM)}" fill="#eef4f7" stroke="#8a6d1a" stroke-width="0.7" opacity="0.92"/>')
    else:
        e.append(f'<circle cx="{ox}" cy="{oy}" r="{r*S:.1f}" fill="#efdca0" stroke="#8a6d1a" stroke-width="1.4"/>')
        e.append(f'<circle cx="{ox}" cy="{oy}" r="{(r-FILLET)*S:.1f}" fill="#e6c96a" stroke="#c9ad4f" stroke-width="0.6"/>')
        e.append(f'<circle cx="{ox}" cy="{oy}" r="{(r-RIM)*S:.1f}" fill="#eef4f7" stroke="#8a6d1a" stroke-width="0.7" opacity="0.92"/>')
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
    """Kanal eksenine dik kesit. (ox, cy): küre merkezi (px). Kenar duvarı plak eksenine
    paralel (eksenel izdüşüm): sırt, taban ile aynı izdüşüme sahiptir."""
    e = []
    r = D / 2
    z = lambda R, x: math.sqrt(max(R * R - x * x, 0.0))
    px = lambda x, R: (ox + x * S, cy - z(R, x) * S)
    def band(Ra, Rb, xa, xb, fill, stroke, sw=1.0):
        # Ra iç yay, Rb dış yay; x aralığı [xa, xb]; duvarlar dikey
        a0, a1 = px(xa, Ra), px(xb, Ra); b0, b1 = px(xa, Rb), px(xb, Rb)
        return (f'<path d="M {b0[0]:.1f} {b0[1]:.1f} A {Rb*S:.1f} {Rb*S:.1f} 0 0 1 {b1[0]:.1f} {b1[1]:.1f} '
                f'L {a1[0]:.1f} {a1[1]:.1f} A {Ra*S:.1f} {Ra*S:.1f} 0 0 0 {a0[0]:.1f} {a0[1]:.1f} Z" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    # göz ve sklera
    e.append(f'<circle cx="{ox}" cy="{cy}" r="{(R_SCL-1)*S:.1f}" fill="#fdf3e7"/>')
    xw = min(r + 4.0, R_SCL - 1.5)
    e.append(band(R_SCL - 1, R_SCL, -xw, xw, "#e8dcc8", "#8a7a60", 0.8))
    # katmanlar (eksenel, dik duvarlı)
    R1 = R_SCL; R2 = R1 + T_SPACER; R3 = R2 + T_CHAN; R4 = R3 + T_SHIELD
    e.append(band(R1, R2, -(r - RIM), r - RIM, "#d9ecf5", "#4a7c96", 0.8))
    e.append(band(R2, R3, -(r - RIM), r - RIM, "#eef4f7", "#4a7c96", 0.8))
    # altın sırt: dış köşeler FILLET ile yuvarlatılmış
    f = FILLET
    p1 = px(-r, R3); p2 = px(r, R3); w3 = px(r, R4); p3 = (w3[0], w3[1] + f * S); p4 = px(r - f, R4)
    p5 = px(-(r - f), R4); w6 = px(-r, R4); p6 = (w6[0], w6[1] + f * S)
    e.append(f'<path d="M {p1[0]:.1f} {p1[1]:.1f} A {R3*S:.1f} {R3*S:.1f} 0 0 1 {p2[0]:.1f} {p2[1]:.1f} '
             f'L {p3[0]:.1f} {p3[1]:.1f} A {f*S:.1f} {f*S:.1f} 0 0 0 {p4[0]:.1f} {p4[1]:.1f} '
             f'A {R4*S:.1f} {R4*S:.1f} 0 0 0 {p5[0]:.1f} {p5[1]:.1f} A {f*S:.1f} {f*S:.1f} 0 0 0 {p6[0]:.1f} {p6[1]:.1f} Z" '
             f'fill="#e6c96a" stroke="#8a6d1a" stroke-width="1.2"/>')
    # kenar kalkanı: 0,5 mm, dikey, sklera temasından R3'e
    for sgn in (-1, 1):
        xa, xb = sgn * r, sgn * (r - RIM)
        q = [px(xa, R3), px(xa, R1), px(xb, R1), px(xb, R3)]
        e.append('<path d="M ' + ' L '.join(f'{x:.1f} {y:.1f}' for x, y in q) + ' Z" fill="#e6c96a" stroke="#8a6d1a" stroke-width="1"/>')
    # kanallar: y=0 düzlemini kestikleri x
    Rd = R_SCL + OFF
    for c in layout(D, notched):
        if c["y_tube_end"] <= 0: continue
        x, y = px(c["x"], Rd)
        e.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{CH_OD/2*S:.1f}" fill="#b8c7d1" stroke="#2b4c5e" stroke-width="0.7"/>')
        e.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{CH_ID/2*S:.1f}" fill="#fff"/>')
    x, y = px(0, Rd)
    e.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{0.35*S:.1f}" fill="#c0392b"/>')
    # kalınlık ölçüleri: merkezde ve kenarda
    xl = ox + (r + 2.5) * S
    ya, yb = cy - R4 * S, cy - R1 * S
    e.append(f'<line x1="{xl:.1f}" y1="{ya:.1f}" x2="{xl:.1f}" y2="{yb:.1f}" stroke="#333" stroke-width="0.7"/>')
    e.append(f'<line x1="{xl-3}" y1="{ya:.1f}" x2="{xl+3}" y2="{ya:.1f}" stroke="#333" stroke-width="0.7"/>')
    e.append(f'<line x1="{xl-3}" y1="{yb:.1f}" x2="{xl+3}" y2="{yb:.1f}" stroke="#333" stroke-width="0.7"/>')
    e.append(f'<text x="{xl + 0.5*S:.1f}" y="{(ya+yb)/2 + 3:.1f}" text-anchor="start" font-size="{max(9, 0.8*S):.0f}">{R4-R1:.2f} mm merkez</text>')
    edge_h = z(R4, r) - z(R1, r)
    e.append(f'<text x="{xl + 0.5*S:.1f}" y="{(ya+yb)/2 + 3 + 1.2*S:.1f}" text-anchor="start" font-size="{max(9, 0.8*S):.0f}">{edge_h:.1f} mm kenar</text>')
    sag = R_SCL - z(R_SCL, r)
    th = math.asin(min(r / R_SCL, 1.0))
    return "\n".join(e), dict(sag=sag, th=math.degrees(th), edge_h=edge_h)

def svg_wrap(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'font-family="Arial, Helvetica, sans-serif" font-size="11">\n<title>{title}</title>\n'
            f'<rect width="{w}" height="{h}" fill="#ffffff"/>\n{body}\n</svg>\n')

def single(D, notched=False):
    S = 10
    W, H = 640, 640
    ttl = f"{D} mm {'çentikli ' if notched else ''}plak"
    body = [f'<text x="{W/2}" y="24" text-anchor="middle" font-size="15" font-weight="bold">Yb-169 HDR episkleral aplikatör, {ttl} (ölçek 10 px = 1 mm)</text>']
    tv, info = top_view(D, S, 200, 190, notched=notched)
    body.append(tv)
    sc, sinfo = section(D, S, 450, 300, notched=notched)
    body.append(sc)
    body.append(f'<text x="200" y="{190 + (D/2 + 15.8) * S:.0f}" text-anchor="middle" font-size="11" fill="#555">Üstten görünüş, anterior (kanal ağızları) altta</text>')
    body.append(f'<text x="450" y="{300 - (R_SCL + 6.0) * S:.0f}" text-anchor="middle" font-size="11" fill="#555">Kesit, kanal eksenine dik; duvar eksene paralel</text>')
    y = 452
    xs_txt = ", ".join(f"{c['x']:+.1f}" for c in layout(D, notched))
    rows = [
        (f"Çap {D} mm, çentikli: jukstapapiller tümör, taban ≤ {D-4} mm, posterior kenarı disk kenarında; bir boy büyük seçilir" if notched
         else f"Çap {D} mm, tümör tabanı ≤ {D-4} mm için"),
        (f"Kanal: {info['n']} paralel kör kiriş, x = {xs_txt} mm; {info['n_trunc']} tanesi çentikte kısaltılmış; iç çap {CH_ID} mm" if notched
         else f"Kanal: {info['n']} paralel kör kiriş, x = {xs_txt} mm (LP ile seçildi), iç çap {CH_ID} mm"),
        f"Bekleme pozisyonu: {info['n_dw']} adet, adım {G.DWELL_STEP} mm, kör uç ölü boşluğu {G.TIP_DEAD} mm",
        f"En uzun kanal yayı {info['arc']:.1f} mm; eğrilik yalnızca küreden ({R_SCL+OFF} mm); eksen skleradan {OFF} mm",
        f"Katmanlar: ara katman {T_SPACER} mm, kanal katmanı {T_CHAN} mm, altın sırt {T_SHIELD} mm; kenar kalkanı {RIM} mm; dış kenar {FILLET} mm yuvarlatılmış",
        f"Kubbe derinliği (sagitta) {sinfo['sag']:.1f} mm, yarım açı {sinfo['th']:.0f}°; iç eğrilik yarıçapı {R_SCL} mm; kenar duvar yüksekliği {sinfo['edge_h']:.1f} mm",
        "Sütür deliği 3 adet, Ø 0,8 mm. Her kanal kendi altın ağzından çıkar; kanal başına ayrı kateter, ayrı transfer tüpü.",
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
        l1 = f"{D} mm {'çentikli' if notched else ''}: {info['n']} kanal, {info['n_dw']} dwell"
        l2 = (f"{info['n_trunc']} kısa + {info['n']-info['n_trunc']} yan kanal" if notched
              else f"ayrı ağız ve kateter, taban ≤ {D-4} mm")
        yl = cy + 105 + (D/2 + 12.5) * S
        body.append(f'<text x="{cx}" y="{yl:.0f}" text-anchor="middle" font-size="9.5" fill="#333">{l1}</text>')
        body.append(f'<text x="{cx}" y="{yl+12:.0f}" text-anchor="middle" font-size="9.5" fill="#555">{l2}</text>')
    body.append(f'<text x="{W/2}" y="{H-12}" text-anchor="middle" font-size="10" fill="#777">Her boy için üstten görünüş (posterior üstte, kanal ağızları anteriorda) ve kanal eksenine dik kesit. Şematik, taslak v0.1.</text>')
    return svg_wrap(W, H, "\n".join(body), "Plak ailesi")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "figures")
    os.makedirs(out, exist_ok=True)
    print(f"{'Çap':>4} {'Kanal':>5} {'Aralık':>7} {'Dwell':>5} {'Yay':>7} {'Sagitta':>8} {'Yarım açı':>9}")
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
