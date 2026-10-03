import urllib.request
import json
import ssl

GITHUB_USER = "unknownuniversem-blip"

# Tool-specific metadata dictionary: icon, badge, category description
TOOL_META = {
    "wa-direct": {
        "icon": "💬",
        "title": "WhatsApp Direct Chat",
        "badge": "MESSAGING",
        "desc": "Open WhatsApp chats instantly without saving unknown phone numbers to contacts."
    },
    "upi-qr-standee": {
        "icon": "💳",
        "title": "UPI QR Standee Maker",
        "badge": "BUSINESS",
        "desc": "Generate custom, printable tabletop QR payment standees for retail shops and billing counters."
    },
    "typing-speed-finger-test": {
        "icon": "⏱️",
        "title": "Finger Speed Typing Test",
        "badge": "TESTING",
        "desc": "Real-time WPM, accuracy, and finger placement assessment for keyboard tests."
    },
    "typer-racer-world": {
        "icon": "🏎️",
        "title": "Type Racer World",
        "badge": "GAMING",
        "desc": "Interactive multi-track typing race challenge to boost word speed under time pressure."
    },
    "type-arcade": {
        "icon": "🕹️",
        "title": "Type Arcade",
        "badge": "ARCADE",
        "desc": "Gamified typing practice challenges to train muscle memory and rapid finger response."
    },
    "signature-maker-studio": {
        "icon": "✍️",
        "title": "Signature Maker Studio",
        "badge": "SIGNATURE",
        "desc": "Draw, smooth, transparentize, and download official digital signatures for online forms."
    },
    "exam-resizer": {
        "icon": "📷",
        "title": "Sarkari Photo & Sign Resizer",
        "badge": "SARKARI EXAMS",
        "desc": "Instant strict 20KB-50KB dimension cropping for SSC, UPSC, IBPS, and State exam portals."
    },
    "sarkari-alert-ai": {
        "icon": "📢",
        "title": "Sarkari Alert AI",
        "badge": "GOVT JOBS",
        "desc": "Automated recruitment notifications, eligibility filters, and exam timetable alerts."
    },
    "commerce-accounts-hub": {
        "icon": "📚",
        "title": "BalanceSheet OS",
        "badge": "CBSE CLASS 12",
        "desc": "Complete DK Goel Class 12 practical problems with step-by-step journals and ledger working notes."
    },
    "krutidev-unicode-converter": {
        "icon": "⌨️️",
        "title": "Krutidev to Unicode Converter",
        "badge": "HINDI TYPING",
        "desc": "Instant bidirectional font engine for official government typing examinations."
    },
    "hindi-typing-tutor": {
        "icon": "🇮🇳",
        "title": "Hindi Typing Tutor",
        "badge": "HINDI SKILLS",
        "desc": "Structured finger layout lessons for Remington Gail, Krutidev, and Mangal Inscript layouts."
    },
    "pdf-smart-tools": {
        "icon": "📄",
        "title": "PDF Smart Tools",
        "badge": "DOCUMENTS",
        "desc": "Merge, split, and compress PDF documents entirely in your browser with zero data uploads."
    },
    "loan-emi-calculator": {
        "icon": "📊",
        "title": "Loan EMI Calculator",
        "badge": "FINANCE",
        "desc": "Interactive loan amortization schedules with principal vs. interest payment breakdowns."
    },
    "panchang-choghadiya": {
        "icon": "🕉️",
        "title": "Panchang & Choghadiya",
        "badge": "CALENDAR",
        "desc": "Real-time daily Shubh Muhurat, Rahu Kaal, and Tithi calculations based on coordinates."
    },
    "age-eligibility-calc": {
        "icon": "📅",
        "title": "Age Eligibility Calculator",
        "badge": "CUTOFF CHECK",
        "desc": "Exact age calculation as of cutoff dates specified in competitive exam notifications."
    },
    "passport-photo-grid": {
        "icon": "🪪",
        "title": "Passport Photo Grid Maker",
        "badge": "PRINTING",
        "desc": "Arrange 4x6 or A4 printable grids of standard passport-size photos with cutting guides."
    },
    "gst-quick-calc": {
        "icon": "🧾",
        "title": "GST Quick Calculator",
        "badge": "ACCOUNTS",
        "desc": "Fast forward and reverse GST breakdowns across 5%, 12%, 18%, and 28% slabs."
    },
    "smartbanker-ai": {
        "icon": "🏦",
        "title": "SmartBanker AI",
        "badge": "BANKING",
        "desc": "Automated financial planning algorithms and loan eligibility pre-qualification analysis."
    },
    "land-converter": {
        "icon": "📐",
        "title": "Bigha & Land Unit Converter",
        "badge": "LAND UTILITY",
        "desc": "Convert regional land units including Bigha, Biswa, Acre, Hectare, and Square Yards."
    },
    "open-astrologer": {
        "icon": "🔮",
        "title": "Open Astrologer",
        "badge": "ASTROLOGY",
        "desc": "Algorithmic Kundli generator and planetary position calculator based on birth details."
    }
}

# Fetch all repositories dynamically from GitHub API
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(
    f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100&sort=updated",
    headers={"User-Agent": "Mozilla/5.0"}
)

try:
    with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
        repos = json.loads(resp.read().decode('utf-8'))
except Exception as e:
    print(f"Error querying GitHub API: {e}")
    exit(1)

exclude = ["github-profile", f"{GITHUB_USER}.github.io", GITHUB_USER]
active_repos = [r for r in repos if r["name"] not in exclude]

cards_html = ""
for r in active_repos:
    slug = r["name"]
    meta = TOOL_META.get(slug, {
        "icon": "⚡",
        "title": slug.replace("-", " ").title(),
        "badge": "UTILITY",
        "desc": r.get("description") or f"Free high-speed {slug.replace('-', ' ')} tool."
    })
    
    url = f"https://{GITHUB_USER}.github.io/{slug}/"
    cards_html += f"""
      <a class="tool-card" href="{url}" target="_blank">
        <div class="card-top">
          <span class="tool-icon">{meta['icon']}</span>
          <span class="badge">{meta['badge']}</span>
        </div>
        <div class="tool-title">{meta['title']}</div>
        <div class="tool-desc">{meta['desc']}</div>
      </a>"""

hub_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Digital Utility Suite — Free Student & Daily Tools</title>
  
  <!-- Custom SVG Favicon (replaces browser earth/globe icon) -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
  
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #070c18;
      color: #f1f5f9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, sans-serif;
      padding: 0 20px 60px;
    }}
    header {{
      text-align: center;
      padding: 60px 10px 30px;
      max-width: 800px;
      margin: 0 auto;
    }}
    .hero-badge {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      background: rgba(14, 165, 233, 0.15);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 4px 14px;
      border-radius: 99px;
      margin-bottom: 14px;
    }}
    h1 {{
      color: #ffffff;
      font-size: 2.6rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
    }}
    h1 span.bolt {{ color: #fbbf24; }}
    p.sub {{
      color: #94a3b8;
      font-size: 1.05rem;
      line-height: 1.5;
    }}
    .container {{
      max-width: 1200px;
      margin: 0 auto;
    }}
    .grid-tools {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 18px;
      margin-top: 30px;
    }}
    .tool-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 14px;
      padding: 22px;
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      transition: all 0.2s ease;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }}
    .tool-card:hover {{
      border-color: #38bdf8;
      transform: translateY(-4px);
      box-shadow: 0 10px 24px rgba(14, 165, 233, 0.15);
      background: #131d35;
    }}
    .card-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
    }}
    .tool-icon {{
      font-size: 32px;
      line-height: 1;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 52px;
      height: 52px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
    }}
    .badge {{
      font-size: 10px;
      font-weight: 700;
      background: #0284c7;
      color: #ffffff;
      padding: 3px 10px;
      border-radius: 99px;
      letter-spacing: 0.04em;
    }}
    .tool-title {{
      font-weight: 700;
      color: #ffffff;
      font-size: 1.15rem;
      margin-bottom: 8px;
      line-height: 1.3;
    }}
    .tool-desc {{
      font-size: 0.88rem;
      color: #94a3b8;
      line-height: 1.5;
      flex-grow: 1;
    }}
    footer {{
      text-align: center;
      margin-top: 60px;
      color: #64748b;
      font-size: 0.85rem;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="hero-badge">Direct Access Network</div>
      <h1><span class="bolt">⚡</span> Digital Utility Suite</h1>
      <p class="sub">Instant, client-side tools designed for speed and zero data collection. No installations, paywalls, or account registrations.</p>
    </header>

    <div class="grid-tools">
      {cards_html}
    </div>

    <footer>
      Maintained under open-source client-side distribution.
    </footer>
  </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(hub_html)

print("Generated custom index.html with icons, custom favicon, and tailored tool metadata.")
