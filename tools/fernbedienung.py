# -*- coding: utf-8 -*-
INK, CREAM, LINE, TEAL, SAGE = "#123A4E", "#FFFDF9", "#E7DFCF", "#2F8F86", "#A9BFB7"

def bau(hervor=()):
    h = set(hervor)
    o = []
    def fill(i):  return INK if i in h else "none"
    def ink(i):   return CREAM if i in h else INK
    def pill(i, x, y, w, ht, label="", fs=13, weight="600"):
        r = ht/2
        o.append(f'<rect id="{i}" x="{x}" y="{y}" width="{w}" height="{ht}" rx="{r}" fill="{fill(i)}" stroke="{INK}" stroke-width="1.6"/>')
        if label:
            o.append(f'<text x="{x+w/2}" y="{y+ht/2+fs*0.36}" text-anchor="middle" font-family="Inter,sans-serif" font-weight="{weight}" font-size="{fs}" fill="{ink(i)}">{label}</text>')
    def lab(x, y, t, fs=7.5, anchor="start", col=INK):
        o.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Inter,sans-serif" font-weight="600" font-size="{fs}" letter-spacing="0.4" fill="{col}">{t}</text>')

    o.append(f'<rect x="8" y="8" width="284" height="1044" rx="30" fill="{CREAM}" stroke="{INK}" stroke-width="2.6"/>')

    # Kopf
    pill("input", 30, 30, 40, 20)
    o.append(f'<g transform="translate(43 34)"><rect x="0" y="1.5" width="9" height="9" rx="1.6" fill="none" stroke="{ink("input")}" stroke-width="1.4"/><path d="M10.5 6h5M13 3.5 15.5 6 13 8.5" fill="none" stroke="{ink("input")}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></g>')
    pill("oval", 80, 30, 110, 20)
    o.append(f'<circle id="power" cx="248" cy="42" r="21" fill="{TEAL if "power" in h else "none"}" stroke="{INK}" stroke-width="2"/>')
    o.append(f'<g transform="translate(248 42)"><path d="M0 -9 V-1" stroke="{CREAM if "power" in h else INK}" stroke-width="2" stroke-linecap="round"/><path d="M-6 -6 A 8.5 8.5 0 1 0 6 -6" fill="none" stroke="{CREAM if "power" in h else INK}" stroke-width="2" stroke-linecap="round"/></g>')
    lab(30, 68, "DIGITAL/", fs=10); lab(30, 79, "ANALOG", fs=10)
    lab(248, 76, "SYNC MENU", fs=10, anchor="middle")
    pill("digital", 30, 84, 40, 20)
    pill("sync", 228, 84, 40, 20)

    # Zifferntasten
    zahlen = [("1","2","3"), ("4","5","6"), ("7","8","9"), ("EXIT","0","TXT")]
    for zi, reihe in enumerate(zahlen):
        for si, t in enumerate(reihe):
            x = 26 + si*84
            y = 116 + zi*44
            pill(f"k{t}", x, y, 72, 34, t, fs=17 if len(t) < 3 else 11)

    # Farbtasten
    for fi, (fid, farbe) in enumerate((("rot","#D14343"),("gruen","#3E9E5E"),("gelb","#E3C044"),("blau","#9FB8DD"))):
        o.append(f'<rect x="{26+fi*62}" y="300" width="54" height="16" rx="8" fill="{farbe}" stroke="{INK}" stroke-width="1.4"/>')

    pill("nx", 96, 326, 108, 30, "NX", fs=16)
    pill("info", 105, 370, 90, 18)
    o.append(f'<g transform="translate(150 379)" font-family="Inter,sans-serif" font-size="8" font-weight="600" fill="{INK}"><text x="-14" y="3" text-anchor="middle">i+</text><text x="12" y="3" text-anchor="middle">?</text></g>')
    o.append(f'<g stroke="{INK}" stroke-width="1.8" stroke-linecap="round"><path d="M238 374 h20M238 379 h20M238 384 h20"/></g>')

    # Steuerkreuz
    cx, cy = 150, 470
    o.append(f'<circle cx="{cx}" cy="{cy}" r="78" fill="none" stroke="{INK}" stroke-width="2"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="50" fill="none" stroke="{INK}" stroke-width="1.4" opacity="0.45"/>')
    for pid, dx, dy, rot in (("hoch",0,-38,0), ("runter",0,38,180), ("links",-38,0,270), ("rechts",38,0,90)):
        f = INK if pid in h else "none"
        c = CREAM if pid in h else INK
        o.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="13" fill="{f}"/>')
        o.append(f'<g transform="translate({cx+dx} {cy+dy}) rotate({rot})"><path d="M0 -5 L5 3 L-5 3 Z" fill="{c}"/></g>')
    o.append(f'<circle id="ok" cx="{cx}" cy="{cy}" r="26" fill="{fill("ok")}" stroke="{INK}" stroke-width="2"/>')
    o.append(f'<g stroke="{ink("ok")}" stroke-width="2" stroke-linecap="round"><path d="M{cx-9} {cy} h18M{cx} {cy-9} v18"/></g>')
    # Die vier Tasten liegen im Ring zwischen innerem und aeusserem Kreis
    for t, x, y, rot in (("SLEEP", 105, 426, -45), ("GUIDE", 195, 426, 45),
                         ("RETURN", 104, 517, 45), ("OPTIONS", 196, 517, -45)):
        o.append(f'<text transform="translate({x} {y}) rotate({rot})" text-anchor="middle" '
                 f'font-family="Inter,sans-serif" font-weight="600" font-size="8.5" letter-spacing="0.3" fill="{INK}">{t}</text>')
    o.append(f'<rect id="home" x="104" y="556" width="92" height="26" rx="13" fill="{SAGE if "home" in h else CREAM}" stroke="{INK}" stroke-width="1.8"/>')
    o.append(f'<text x="150" y="574" text-anchor="middle" font-family="Inter,sans-serif" font-weight="600" font-size="13" fill="{INK}">HOME</text>')

    # Lautstärke und Programm
    o.append(f'<path d="M49 620 L75 602 L75 620 Z" fill="none" stroke="{INK}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
    lab(238, 614, "PROG", fs=11, anchor="middle")
    for bid, x, y, t in (("vol+",26,626,"+"), ("vol-",26,674,"−"), ("prog+",202,626,"+"), ("prog-",202,674,"−")):
        pill(bid, x, y, 72, 42, t, fs=22, weight="400")
    pill("jump", 122, 630, 56, 20)
    o.append(f'<g transform="translate(150 640)" fill="none" stroke="{INK}" stroke-width="1.5" stroke-linecap="round"><path d="M-7 -2 a7 7 0 1 1 2 5"/><path d="M-8 -5 v4 h4"/></g>')
    pill("mute", 122, 672, 56, 20)
    o.append(f'<g transform="translate(150 682)" fill="none" stroke="{INK}" stroke-width="1.5" stroke-linecap="round"><path d="M-9 -3 h4 l4 -4 v14 l-4 -4 h-4 z"/><path d="M3 -3 l7 7M10 -3 l-7 7"/></g>')
    lab(28, 730, "AUDIO", fs=9); lab(272, 730, "TITLE LIST", fs=9, anchor="end")
    o.append(f'<rect x="138" y="722" width="24" height="12" rx="2.5" fill="none" stroke="{INK}" stroke-width="1.5"/><path d="M142 730 h8M154 730 h4" stroke="{INK}" stroke-width="1.5" stroke-linecap="round"/>')
    pill("audio", 26, 738, 72, 16); pill("sub", 122, 738, 56, 16); pill("title", 202, 738, 72, 16)

    # Wiedergabe
    def sym(x, y, art):
        g = f'<g transform="translate({x} {y})" fill="{INK}">'
        if art == "rew":   g += '<path d="M0 -6 L-8 0 L0 6 Z"/><path d="M9 -6 L1 0 L9 6 Z"/>'
        elif art == "ff":  g += '<path d="M0 -6 L8 0 L0 6 Z"/><path d="M-9 -6 L-1 0 L-9 6 Z"/>'
        elif art == "play":g += '<path d="M-5 -7 L8 0 L-5 7 Z"/>'
        elif art == "prev":g += '<rect x="-10" y="-6" width="2.6" height="12"/><path d="M8 -6 L-2 0 L8 6 Z"/>'
        elif art == "next":g += '<rect x="7.4" y="-6" width="2.6" height="12"/><path d="M-8 -6 L2 0 L-8 6 Z"/>'
        elif art == "pause":g+= '<rect x="-6" y="-6" width="4" height="12"/><rect x="2" y="-6" width="4" height="12"/>'
        elif art == "stop":g += '<rect x="-6" y="-6" width="12" height="12" rx="1"/>'
        elif art == "rec": g = f'<g transform="translate({x} {y})" fill="#D14343"><circle r="7"/>'
        elif art == "grid":g = (f'<g transform="translate({x} {y})" fill="none" stroke="{INK}" stroke-width="1.6">'
                                '<rect x="-9" y="-7" width="18" height="14" rx="2"/><path d="M-9 -2h18M-9 3h18M-3 -7v14M3 -7v14"/>')
        return g + '</g>'
    for ri, (arten, y) in enumerate(((("rew","play","ff"), 772), (("prev","pause","next"), 812), (("rec","stop","grid"), 852))):
        for si, art in enumerate(arten):
            x = 26 + si*88
            pill(f"pb{art}", x, y, 72, 28)
            o.append(sym(x+36, y+14, art))
    lab(30, 848, "REC", fs=8, col="#D14343")

    o.append(f'<path d="M100 968 H200" stroke="{INK}" stroke-width="1.4" opacity="0.5"/>')
    o.append(f'<text x="150" y="994" text-anchor="middle" font-family="Inter,sans-serif" font-weight="600" font-size="13" fill="{INK}">TV</text>')
    o.append(f'<text x="150" y="1014" text-anchor="middle" font-family="\'IBM Plex Mono\',monospace" font-size="10" letter-spacing="0.5" fill="#7C8B93">RMT-TX102D</text>')

    inner = "\n  ".join(o)
    return (f'<svg viewBox="0 0 300 1060" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-label="Fernbedienung Sony RMT-TX102D">\n  {inner}\n</svg>\n')

if __name__ == "__main__":
    import sys, io
    io.open(sys.argv[1], "w", encoding="utf-8").write(bau(sys.argv[2:]))

# Aufruf:  python3 tools/fernbedienung.py assets/ziel.svg [taste ...]
# Tasten:  input power ok hoch runter links rechts home vol+ vol- prog+ prog-
#          k1..k9 kEXIT k0 kTXT nx mute jump audio sub title pbplay pbstop ...
