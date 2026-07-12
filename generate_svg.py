#!/usr/bin/env python3
"""Genera dark.svg y light.svg para el profile README de SGGaray.
Estilo terminal GRC, tipografia JetBrains Mono (fallback monospace).
Uso: python3 generate_svg.py
"""

LINES = [
    ("cmd",    "sebastian@grc ~ % ./profile.sh --live"),
    ("blank",  ""),
    ("kv", ("Subject",    "Sebastian Garay")),
    ("kv", ("Role",       "GRC Analyst (Jr) - Human Risk & Shadow AI")),
    ("kv", ("Origin",     "Buenos Aires, AR")),
    ("kv", ("Education",  "Lic. Ciberdefensa (UNDEF) - Psic. Social (AMVA)")),
    ("kv", ("Frameworks", "ISO 27001 - NIST CSF 2.0 - COBIT 2019")),
    ("kv", ("Focus",      "VIDA Model - Behavioral Security - Shadow AI Gov.")),
    ("kv", ("Status",     "Building - Learning - Shipping")),
    ("blank",  ""),
    ("sep",    "Contact"),
    ("kv", ("Mail",       "garaysebastiang@gmail.com")),
    ("kv", ("Portfolio",  "sggaray.vercel.app")),
    ("kv", ("LinkedIn",   "linkedin.com/in/sebastian-garay")),
    ("blank",  ""),
]

THEMES = {
    "dark": {
        "bg": "#0d1117", "frame": "#30363d", "title": "#8b949e",
        "key": "#7ee787", "val": "#c9d1d9", "cmd": "#79c0ff",
        "sep": "#f2cc60", "dim": "#6e7681", "dots": ["#ff5f56", "#ffbd2e", "#27c93f"],
    },
    "light": {
        "bg": "#ffffff", "frame": "#d0d7de", "title": "#57606a",
        "key": "#116329", "val": "#24292f", "cmd": "#0550ae",
        "sep": "#953800", "dim": "#8c959f", "dots": ["#ff5f56", "#ffbd2e", "#27c93f"],
    },
}

W, LH, PAD_X, PAD_TOP = 780, 26, 32, 64
KEY_W = 12  # chars reserved for key column

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def build(theme):
    t = THEMES[theme]
    h = PAD_TOP + LH * len(LINES) + 28
    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" font-family="JetBrains Mono, SFMono-Regular, Consolas, monospace" font-size="14">')
    out.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{h-1}" rx="10" fill="{t["bg"]}" stroke="{t["frame"]}"/>')
    # title bar
    for i, c in enumerate(t["dots"]):
        out.append(f'<circle cx="{24 + i*20}" cy="24" r="6" fill="{c}"/>')
    out.append(f'<text x="{W/2}" y="28" text-anchor="middle" fill="{t["title"]}">sebas@grc: profile.sh</text>')
    out.append(f'<line x1="0" y1="42" x2="{W}" y2="42" stroke="{t["frame"]}"/>')

    y = PAD_TOP
    for kind, data in LINES:
        if kind == "blank":
            y += LH
            continue
        if kind == "cmd":
            out.append(f'<text x="{PAD_X}" y="{y}" fill="{t["cmd"]}">{esc(data)}</text>')
        elif kind == "sep":
            bar = "-" * 8
            out.append(f'<text x="{PAD_X}" y="{y}" fill="{t["sep"]}">{bar} {esc(data)} {bar}</text>')
        elif kind == "dim":
            out.append(f'<text x="{PAD_X}" y="{y}" fill="{t["dim"]}">{esc(data)}</text>')
        elif kind == "kv":
            key, val = data
            dots = "." * max(1, KEY_W - len(key))
            out.append(f'<text x="{PAD_X}" y="{y}">'
                       f'<tspan fill="{t["key"]}" font-weight="bold">{esc(key)}</tspan>'
                       f'<tspan fill="{t["dim"]}"> {dots} </tspan>'
                       f'<tspan fill="{t["val"]}">{esc(val)}</tspan></text>')
        y += LH
    out.append("</svg>")
    return "\n".join(out)

if __name__ == "__main__":
    for theme in THEMES:
        path = f"{theme}.svg"
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(theme))
        print(f"wrote {path}")
