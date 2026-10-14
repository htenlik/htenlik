"""Generate the XP Explorer-style project section for the htenlik profile README.

Outputs SVGs into <repo>/assets/explorer/ and prints the README snippet.
Usage: python3 scripts/generate_explorer.py   (run from anywhere; edit PROJECTS below)
"""
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "explorer"
OUT.mkdir(parents=True, exist_ok=True)

W = 840
FONT = "Tahoma, Verdana, 'Segoe UI', sans-serif"

LANG = {
    "PHP": "#4F5D95", "Java": "#b07219", "TypeScript": "#3178c6",
    "Kotlin": "#A97BFF", "C++": "#f34b7d", "Python": "#3572A5",
}

# ---------------------------------------------------------------- icons (72x72)
ICONS = {}

ICONS["chart"] = """
<path d="M14 6h34l12 12v48H14z" fill="#fff" stroke="#5a6f8c" stroke-width="2"/>
<path d="M48 6v12h12" fill="#dfe8f5" stroke="#5a6f8c" stroke-width="2"/>
<rect x="21" y="40" width="7" height="16" fill="#3a7bd5"/>
<rect x="31" y="31" width="7" height="25" fill="#f39c1f"/>
<rect x="41" y="36" width="7" height="20" fill="#3a7bd5"/>
<path d="M20 25c5-6 8 4 13-2s7 3 12-1" fill="none" stroke="#16821f" stroke-width="2.5" stroke-linecap="round"/>
<path d="M19 60h34" stroke="#9aa9bd" stroke-width="2"/>
"""

ICONS["model"] = """
<rect x="26" y="7" width="20" height="14" rx="3" fill="#1268dc" stroke="#0a3f8f" stroke-width="1.5"/>
<rect x="8" y="34" width="20" height="14" rx="3" fill="#58c23d" stroke="#16821f" stroke-width="1.5"/>
<rect x="44" y="34" width="20" height="14" rx="3" fill="#58c23d" stroke="#16821f" stroke-width="1.5"/>
<path d="M36 21v7M18 34v-6h36v6" fill="none" stroke="#5a6f8c" stroke-width="2"/>
<circle cx="47" cy="54" r="10" fill="#fff8d6" stroke="#5a6f8c" stroke-width="3"/>
<path d="M54 61l9 9" stroke="#5a6f8c" stroke-width="5" stroke-linecap="round"/>
<path d="M42 54l4 4 6-7" fill="none" stroke="#16821f" stroke-width="2.5" stroke-linecap="round"/>
"""

ICONS["clipboard"] = """
<rect x="13" y="10" width="46" height="56" rx="4" fill="#c58b4c" stroke="#7a4d1f" stroke-width="2"/>
<rect x="18" y="16" width="36" height="45" fill="#fff" stroke="#9aa9bd"/>
<rect x="26" y="5" width="20" height="10" rx="3" fill="#cfd7e2" stroke="#5a6f8c" stroke-width="2"/>
<path d="M22 27l3 3 5-6M22 39l3 3 5-6" fill="none" stroke="#16821f" stroke-width="2.5" stroke-linecap="round"/>
<path d="M33 28h16M33 40h16M33 52h12" stroke="#7b8ba2" stroke-width="2.5"/>
<rect x="22" y="48" width="7" height="7" fill="none" stroke="#7b8ba2" stroke-width="2"/>
"""

ICONS["map"] = """
<path d="M8 16l18-7 20 7 18-7v47l-18 7-20-7-18 7z" fill="#b9e3a1" stroke="#3d7d2d" stroke-width="2"/>
<path d="M26 9v47M46 16v47" stroke="#3d7d2d" stroke-width="1.5" opacity=".6"/>
<path d="M8 40c12-6 22 6 34 0s15-4 22-2" fill="none" stroke="#3a8ad8" stroke-width="4" opacity=".8"/>
<path d="M36 50s-12-13-12-22a12 12 0 0124 0c0 9-12 22-12 22z" fill="#e13c2f" stroke="#8f1d14" stroke-width="2"/>
<circle cx="36" cy="28" r="4.5" fill="#fff"/>
"""

ICONS["weather"] = """
<g stroke="#f39c1f" stroke-width="3" stroke-linecap="round">
  <path d="M27 4v7M27 43v-3M8 23h7M46 23h-3M13 9l5 5M41 9l-5 5M13 37l5-5"/>
</g>
<circle cx="27" cy="23" r="11" fill="#ffd23f" stroke="#f39c1f" stroke-width="2"/>
<path d="M22 60h34a11 11 0 000-22 15 15 0 00-28 3 10 10 0 00-6 19z" fill="#fff" stroke="#5a8fc7" stroke-width="2.5"/>
<path d="M27 66l-2 4M37 66l-2 4M47 66l-2 4" stroke="#3a8ad8" stroke-width="2.5" stroke-linecap="round"/>
"""

ICONS["database"] = """
<defs><linearGradient id="dbg" x2="1"><stop stop-color="#1d5fbf"/><stop offset=".5" stop-color="#5fa2f0"/><stop offset="1" stop-color="#1d5fbf"/></linearGradient></defs>
<path d="M12 14v40c0 5 11 9 24 9s24-4 24-9V14" fill="url(#dbg)" stroke="#0a3f8f" stroke-width="2"/>
<ellipse cx="36" cy="14" rx="24" ry="8" fill="#9fcbff" stroke="#0a3f8f" stroke-width="2"/>
<path d="M12 28c0 5 11 9 24 9s24-4 24-9M12 41c0 5 11 9 24 9s24-4 24-9" fill="none" stroke="#0a3f8f" stroke-width="2"/>
<rect x="38" y="50" width="30" height="17" rx="3" fill="#f34b7d" stroke="#8f1d40" stroke-width="1.5"/>
<text x="53" y="63" text-anchor="middle" font-family="Consolas, 'DejaVu Sans Mono', monospace" font-size="12" font-weight="bold" fill="#fff">C++</text>
"""


def _torus():
    s = []
    pts = [12 + i * 16 for i in range(4)]
    for y in pts:
        s.append(f'<path d="M4 {y}H68" stroke="#7b8ba2" stroke-width="2"/>')
    for x in pts:
        s.append(f'<path d="M{x} 4V68" stroke="#7b8ba2" stroke-width="2"/>')
    s.append('<path d="M60 12q8 0 8 -6M12 60q-8 0 -8 6" fill="none" stroke="#3a7bd5" stroke-width="2" stroke-dasharray="3 2"/>')
    for x in pts:
        for y in pts:
            root = (x, y) == (pts[0], pts[0])
            agg = (x == pts[0] or y == pts[0]) and not root
            fill = "#f39c1f" if root else ("#58c23d" if agg else "#1268dc")
            s.append(f'<circle cx="{x}" cy="{y}" r="{6.5 if root else 5}" fill="{fill}" stroke="#fff" stroke-width="1.5"/>')
    return "\n".join(s)


ICONS["torus"] = _torus()

ICONS["p2p"] = """
<path d="M22 22L50 22M22 22L36 50M50 22L36 50" stroke="#3a7bd5" stroke-width="3" stroke-dasharray="5 3"/>
<g>
  <rect x="7" y="10" width="28" height="20" rx="2" fill="#dce8ee" stroke="#244c64" stroke-width="2"/><rect x="11" y="14" width="20" height="12" fill="#3b91c7"/><rect x="14" y="31" width="14" height="4" rx="1" fill="#9fb2c2"/>
  <rect x="37" y="10" width="28" height="20" rx="2" fill="#dce8ee" stroke="#244c64" stroke-width="2"/><rect x="41" y="14" width="20" height="12" fill="#3b91c7"/><rect x="44" y="31" width="14" height="4" rx="1" fill="#9fb2c2"/>
  <rect x="22" y="40" width="28" height="20" rx="2" fill="#dce8ee" stroke="#244c64" stroke-width="2"/><rect x="26" y="44" width="20" height="12" fill="#58c23d"/><rect x="29" y="61" width="14" height="4" rx="1" fill="#9fb2c2"/>
</g>
<path d="M36 46v7M32 50l4 4 4-4" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
"""

ICONS["shield"] = """
<path d="M30 5l22 8v18c0 16-10 26-22 32C18 57 8 47 8 31V13z" fill="#1268dc" stroke="#0a3f8f" stroke-width="2"/>
<path d="M30 11l16 6v14c0 12-7 20-16 25z" fill="#5fa2f0"/>
<path d="M16 30h7l3-6 4 12 3-6h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linejoin="round"/>
<circle cx="50" cy="48" r="11" fill="#fff8d6" stroke="#5a6f8c" stroke-width="3"/>
<path d="M58 56l8 8" stroke="#5a6f8c" stroke-width="5" stroke-linecap="round"/>
<path d="M45 48h10M50 43v10" stroke="#e13c2f" stroke-width="2.5"/>
"""

FOLDER_SM = """<path d="M0 3a2 2 0 012-2h5l2 2h9a2 2 0 012 2v10a2 2 0 01-2 2H2a2 2 0 01-2-2z" fill="#f5c64c" stroke="#b07d14" stroke-width="1.2"/><path d="M0 7h20" stroke="#fff3c4" stroke-width="1"/>"""

# ---------------------------------------------------------------- data
PROJECTS = [
    dict(slug="01-jotform-sign-analytics", icon="chart", title="Jotform Sign Analytics",
         meta="Professional / Analytics  ·  Jotform internship, 3-person team",
         desc="REST aggregation pipelines, field-friction scoring and AI document insights.",
         lang="PHP", button="Open", url="https://github.com/htenlik/jutform-hackathon"),
    dict(slug="02-oss-qmet", icon="model", title="OSS-QMET",
         meta="Professional / Research  ·  Hacettepe DREAM project",
         desc="Visual quality-model builder with DSL parsing for open-source software.",
         lang="Java", button="Open", url="https://github.com/htenlik/open-source-software"),
    dict(slug="03-internship-workflow", icon="clipboard", title="Internship Workflow Management System",
         meta="Full Stack / Workflow  ·  React · Spring Boot · PostgreSQL",
         desc="Four-role approval workflow with PDF reports, JWT and OTP verification.",
         lang="Java", button="Open", url="https://github.com/htenlik/Internship-Workflow-Management-System"),
    dict(slug="04-tasinmaz", icon="map", title="Taşınmaz Yönetim Sistemi",
         meta="Full Stack / GIS  ·  Angular · ASP.NET Core · EF Core",
         desc="Real-estate management with location hierarchy, audit logs and maps.",
         lang="TypeScript", button="Open", url="https://github.com/htenlik/Tasinmaz-Management-System"),
    dict(slug="05-hava-weather", icon="weather", title="Hava — Weather App",
         meta="Mobile / Android  ·  Kotlin · Jetpack Compose · KAMP+",
         desc="Offline cache, device location, localization and 60 unit tests in CI.",
         lang="Kotlin", button="Open", url="https://github.com/htenlik/weather-app"),
    dict(slug="06-minidb", icon="database", title="MiniDB++",
         meta="Systems / Databases  ·  C++20 from scratch",
         desc="B+ tree, SQL engine, LRU-K buffer pool, WAL and crash recovery over TCP.",
         lang="C++", button="Open", url="https://github.com/htenlik/minidb_cpp"),
    dict(slug="07-mpi-gather-torus", icon="torus", title="MPI_Gather on 2D Torus",
         meta="Systems / Parallel Computing  ·  OMNeT++ simulation",
         desc="Topology-aware gather: 46.9% fewer hops, 88.2% less root load at 256 nodes.",
         lang="C++", button="Open", url="https://github.com/htenlik/MPIGatherTorus"),
    dict(slug="08-p2p-file-sharing", icon="p2p", title="P2P File Sharing",
         meta="Systems / Networking  ·  Python sockets",
         desc="Central peer discovery and parallel byte-range downloads between peers.",
         lang="Python", button="Open", url="https://github.com/htenlik/P2P-File-Sharing"),
    dict(slug="09-ai-incident-dashboard", icon="shield", title="AI Incident Evidence Dashboard",
         meta="Research / AI Safety  ·  Apart Research sprint",
         desc="Claim-level evidence timeline of the OpenAI–Hugging Face incident.",
         lang="TypeScript", button="Open", url="https://github.com/htenlik/apart-incident-dashboard"),
]

TABS = ["All Projects", "Professional", "Full Stack", "Systems", "Research"]


def svg(h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" '
            f'role="img" aria-label="{escape(label)}">\n<title>{escape(label)}</title>\n{body}\n</svg>\n')


def xp_button(x, y, w, h, text, primary=False):
    fill = "url(#btn)"
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="#003c74" stroke-width="1"/>'
            f'<rect x="{x+1.5}" y="{y+1.5}" width="{w-3}" height="{h-3}" rx="3" fill="none" stroke="#fff" stroke-opacity=".8"/>'
            f'<text x="{x + w/2}" y="{y + h/2 + 5}" text-anchor="middle" font-family="{FONT}" font-size="14" '
            f'font-weight="{"bold" if primary else "normal"}" fill="#1b1b1b">{escape(text)}</text>')


BTN_GRAD = ('<linearGradient id="btn" x2="0" y2="1"><stop stop-color="#ffffff"/>'
            '<stop offset=".85" stop-color="#ece9d8"/><stop offset="1" stop-color="#d6d0bd"/></linearGradient>')


# ---------------------------------------------------------------- header
def header():
    h = 196
    tabs = []
    x = 14
    widths = [150, 146, 136, 120, 124]
    for i, (name, tw) in enumerate(zip(TABS, widths)):
        sel = i == 0
        fill = "url(#tabsel)" if sel else "#e8effb"
        stroke = "#0a3f9f" if sel else "#9db5e0"
        col = "#fff" if sel else "#1b1b1b"
        tabs.append(
            f'<rect x="{x}" y="146" width="{tw}" height="38" rx="2" fill="{fill}" stroke="{stroke}"/>'
            f'<g transform="translate({x+12} 156)">{FOLDER_SM}</g>'
            f'<text x="{x+40}" y="170" font-family="{FONT}" font-size="14" fill="{col}">{name}</text>')
        x += tw + 8
    menu = []
    mx = 18
    for item in ["File", "Edit", "View", "Favorites", "Tools", "Help"]:
        tw = int(7.6 * len(item)) + 6
        menu.append(f'<text x="{mx}" y="60" font-family="{FONT}" font-size="14" fill="#1b1b1b">{item}</text>'
                    f'<path d="M{mx} 63h8" stroke="#1b1b1b"/>')
        mx += tw + 14
    body = f"""
<defs>
  <linearGradient id="title" x2="0" y2="1"><stop stop-color="#3d95ff"/><stop offset=".12" stop-color="#2a7cf0"/><stop offset=".55" stop-color="#0a5bd8"/><stop offset="1" stop-color="#0646ad"/></linearGradient>
  <linearGradient id="band" x2="0" y2="1"><stop stop-color="#7aa5ea"/><stop offset="1" stop-color="#5585d8"/></linearGradient>
  <linearGradient id="tabsel" x2="0" y2="1"><stop stop-color="#3a78e0"/><stop offset="1" stop-color="#1c55c0"/></linearGradient>
  <linearGradient id="go" x2="0" y2="1"><stop stop-color="#6fd34e"/><stop offset="1" stop-color="#249a23"/></linearGradient>
  <linearGradient id="close" x2="0" y2="1"><stop stop-color="#f08a72"/><stop offset="1" stop-color="#c3361c"/></linearGradient>
  <linearGradient id="ctl" x2="0" y2="1"><stop stop-color="#5a9cff"/><stop offset="1" stop-color="#1c5fd6"/></linearGradient>
  {BTN_GRAD}
</defs>
<rect x="1" y="1" width="{W-2}" height="{h-2}" rx="9" fill="#ece9d8" stroke="#0a3f9f" stroke-width="2"/>
<path d="M2 10a8 8 0 018-8h{W-20}a8 8 0 018 8v26H2z" fill="url(#title)"/>
<path d="M10 3h{W-20}" stroke="#8cc0ff" stroke-width="1.5" opacity=".7"/>
<g transform="translate(14 10) scale(.95)">{FOLDER_SM}</g>
<text x="44" y="26" font-family="{FONT}" font-size="15" font-weight="bold" fill="#fff" stroke="#0a3070" stroke-width=".4">My Projects</text>
<g transform="translate({W-92} 8)">
  <rect width="24" height="22" rx="3" fill="url(#ctl)" stroke="#fff"/><path d="M6 15h10" stroke="#fff" stroke-width="3"/>
  <rect x="28" width="24" height="22" rx="3" fill="url(#ctl)" stroke="#fff"/><rect x="34" y="5" width="12" height="11" fill="none" stroke="#fff" stroke-width="2"/>
  <rect x="56" width="24" height="22" rx="3" fill="url(#close)" stroke="#fff"/><path d="M62 5l12 12M74 5L62 17" stroke="#fff" stroke-width="2.6"/>
</g>
{''.join(menu)}
<path d="M2 70h{W-4}" stroke="#d4d0c8"/>
<g>
  <circle cx="30" cy="91" r="12" fill="url(#go)" stroke="#1a6e1a"/><path d="M36 91H24m5-5l-5 5 5 5" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="48" y="96" font-family="{FONT}" font-size="14" fill="#1b1b1b">Back</text>
  <circle cx="104" cy="91" r="12" fill="#c9c6b8" stroke="#8d8a7c"/><path d="M98 91h12m-5-5l5 5-5 5" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
  <g transform="translate(130 82)">{FOLDER_SM}<path d="M10 14V7m-3 3l3-3 3 3" fill="none" stroke="#2a7a1a" stroke-width="2"/></g>
  <path d="M164 78v26" stroke="#c4c0b0"/>
  <circle cx="186" cy="89" r="6" fill="none" stroke="#3a6fbf" stroke-width="2.5"/><path d="M190 93l5 5" stroke="#3a6fbf" stroke-width="3" stroke-linecap="round"/>
  <text x="202" y="96" font-family="{FONT}" font-size="14" fill="#1b1b1b">Search</text>
  <g transform="translate(266 82)">{FOLDER_SM}</g>
  <text x="292" y="96" font-family="{FONT}" font-size="14" fill="#1b1b1b">Folders</text>
  <text x="{W-20}" y="96" text-anchor="end" font-family="{FONT}" font-size="13" fill="#4d4d4d">{len(PROJECTS)} objects</text>
</g>
<path d="M2 110h{W-4}" stroke="#d4d0c8"/>
<text x="16" y="131" font-family="{FONT}" font-size="13" fill="#6d6d6d">Address</text>
<rect x="76" y="116" width="{W-160}" height="24" fill="#fff" stroke="#7f9db9"/>
<g transform="translate(84 120) scale(.85)">{FOLDER_SM}</g>
<text x="108" y="133" font-family="{FONT}" font-size="13" fill="#1b1b1b">C:\\Users\\Huseyin\\Projects\\All Projects</text>
<rect x="{W-76}" y="116" width="58" height="24" rx="2" fill="#ece9d8" stroke="#a5a294"/>
<rect x="{W-72}" y="120" width="16" height="16" rx="3" fill="url(#go)"/><path d="M{W-68} 128h8m-3-3l3 3-3 3" fill="none" stroke="#fff" stroke-width="2"/>
<text x="{W-50}" y="133" font-family="{FONT}" font-size="13" fill="#1b1b1b">Go</text>
<rect x="2" y="140" width="{W-4}" height="{h-142}" rx="0" fill="url(#band)"/>
<path d="M2 140h{W-4}" stroke="#3a64b8"/>
<path d="M2 {h-10}v1a8 8 0 008 8h{W-20}a8 8 0 008-8v-1" fill="url(#band)"/>
{''.join(tabs)}
<rect x="1" y="1" width="{W-2}" height="{h-2}" rx="9" fill="none" stroke="#0a3f9f" stroke-width="2"/>
"""
    return svg(h, body, "My Projects — Windows XP style file explorer")


# ---------------------------------------------------------------- rows
def row(p):
    h = 104
    lang_col = LANG[p["lang"]]
    title = escape(p["title"])
    # rough underline width (Tahoma bold 17px ≈ 9.6px/char; Verdana a bit wider)
    ul = int(len(p["title"]) * 9.4)
    body = f"""
<defs>{BTN_GRAD}
  <linearGradient id="hl" x2="1"><stop stop-color="#e6effd"/><stop offset="1" stop-color="#ffffff"/></linearGradient>
</defs>
<rect x="1" y="1" width="{W-2}" height="{h-2}" rx="6" fill="url(#hl)" stroke="#9db5e0"/>
<rect x="1" y="1" width="5" height="{h-2}" rx="2" fill="#2f6fd6"/>
<rect x="20" y="14" width="76" height="76" fill="#fff" stroke="#a0a0a0"/>
<g transform="translate(22 16)">{ICONS[p['icon']]}</g>
<text x="114" y="38" font-family="{FONT}" font-size="17" font-weight="bold" fill="#0b46c4" text-decoration="underline">{title}</text>
<text x="114" y="62" font-family="{FONT}" font-size="13" fill="#6b6b6b">{escape(p['meta'])}</text>
<text x="114" y="84" font-family="{FONT}" font-size="13.5" fill="#222">{escape(p['desc'])}</text>
<circle cx="{W-112}" cy="33" r="5.5" fill="{lang_col}"/>
<text x="{W-101}" y="38" font-family="{FONT}" font-size="13" fill="#4d4d4d">{p['lang']}</text>
{xp_button(W-114, 54, 92, 30, p['button'] + '  ›', primary=p['button'] == 'Live')}
"""
    return svg(h, body, f"{p['title']} — {p['desc']}")


# ---------------------------------------------------------------- status bar
def footer():
    h = 40
    body = f"""
<defs><linearGradient id="sb" x2="0" y2="1"><stop stop-color="#f3f1e6"/><stop offset="1" stop-color="#e3dfcd"/></linearGradient></defs>
<rect x="1" y="1" width="{W-2}" height="{h-2}" rx="6" fill="url(#sb)" stroke="#a5a294"/>
<text x="16" y="25" font-family="{FONT}" font-size="13" fill="#333">{len(PROJECTS)} object(s)</text>
<path d="M120 8v24M560 8v24" stroke="#c4c0b0"/>
<text x="136" y="25" font-family="{FONT}" font-size="13" fill="#333">Screenshots &amp; case studies → htenlik.com</text>
<g transform="translate(578 9)">
  <circle cx="11" cy="11" r="10" fill="#3a8ad8" stroke="#0a3f8f"/>
  <path d="M1 11h20M11 1c-5 6-5 14 0 20M11 1c5 6 5 14 0 20" fill="none" stroke="#fff" stroke-width="1.3"/>
</g>
<text x="606" y="25" font-family="{FONT}" font-size="13" fill="#333">Internet</text>
<path d="M{W-24} {h-10}l10-10M{W-19} {h-10}l5-5" stroke="#a5a294" stroke-width="1.5"/>
"""
    return svg(h, body, "Status bar — 9 objects, more on htenlik.com")


(OUT / "00-header.svg").write_text(header(), encoding="utf-8")
for p in PROJECTS:
    (OUT / f"{p['slug']}.svg").write_text(row(p), encoding="utf-8")
(OUT / "99-statusbar.svg").write_text(footer(), encoding="utf-8")

lines = ['<a href="https://htenlik.com/#projects"><img src="assets/explorer/00-header.svg" width="100%" alt="My Projects — explorer window"/></a>']
for p in PROJECTS:
    lines.append(f'<a href="{p["url"]}"><img src="assets/explorer/{p["slug"]}.svg" width="100%" alt="{escape(p["title"])}"/></a>')
lines.append('<a href="https://htenlik.com/#projects"><img src="assets/explorer/99-statusbar.svg" width="100%" alt="More on htenlik.com"/></a>')
print("\n".join(lines))
