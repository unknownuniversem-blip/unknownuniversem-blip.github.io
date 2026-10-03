import urllib.request
import json
import ssl

GITHUB_USER = "unknownuniversem-blip"

# Comprehensive dictionary mapping each tool to its unique icon, badge, and description
CATALOG = {
    "wa-direct": {
        "icon": "💬", "title": "WhatsApp Direct Chat", "badge": "MESSAGING",
        "desc": "Open WhatsApp chats instantly without saving unknown numbers to your phone contacts."
    },
    "upi-qr-standee": {
        "icon": "💳", "title": "UPI QR Standee Maker", "badge": "BUSINESS",
        "desc": "Create printable countertop UPI QR payment displays with shop details and logos."
    },
    "typing-speed-finger-test": {
        "icon": "⏱️️", "title": "Finger Typing Speed Test", "badge": "SKILLS",
        "desc": "Test net words per minute (WPM), accuracy, and finger placement with live visual feedback."
    },
    "typer-racer-world": {
        "icon": "🏎️", "title": "Type Racer World", "badge": "GAMING",
        "desc": "Interactive competitive speed typing challenges against clock benchmarks."
    },
    "type-arcade": {
        "icon": "🕹️", "title": "Type Arcade", "badge": "GAMING",
        "desc": "Gamified typing practice challenges to build rapid finger muscle memory."
    },
    "signature-maker-studio": {
        "icon": "✍️", "title": "Signature Maker Studio", "badge": "SIGNATURE",
        "desc": "Draw, smooth, transparentize, and export digital signatures for online forms and documents."
    },
    "sarkari-alert-ai": {
        "icon": "📢", "title": "Sarkari Alert AI", "badge": "GOVT JOBS",
        "desc": "Real-time government job alerts, age cutoff calculators, and recruitment notices."
    },
    "pdf-smart-tools": {
        "icon": "📄", "title": "PDF Smart Tools", "badge": "DOCUMENTS",
        "desc": "Merge, compress, and split PDF documents client-side with complete file privacy."
    },
    "passport-photo-grid": {
        "icon": "🪪", "title": "Passport Photo Grid Maker", "badge": "PRINTING",
        "desc": "Arrange passport size photos into 4x6 or A4 printable grid layouts with cut lines."
    },
    "panchang-choghadiya": {
        "icon": "🕉️", "title": "Panchang & Choghadiya", "badge": "CALENDAR",
        "desc": "Calculate live Shubh Muhurat, Rahu Kaal, Yamaganda, and daily Tithi by location."
    },
    "open-astrologer": {
        "icon": "🔮", "title": "Open Astrologer", "badge": "ASTROLOGY",
        "desc": "Algorithmic Vedic Kundli generator and planetary position chart calculations."
    },
    "loan-emi-calculator": {
        "icon": "📊", "title": "Loan EMI Calculator", "badge": "FINANCE",
        "desc": "Instant loan EMI calculation with detailed amortization table and interest breakdown."
    },
    "land-converter": {
        "icon": "📐", "title": "Bigha & Land Unit Converter", "badge": "LAND UTILITY",
        "desc": "Convert regional land units including Bigha, Biswa, Guntha, Acre, and Square Yards."
    },
    "krutidev-unicode-converter": {
        "icon": "⌨️", "title": "Krutidev to Unicode Converter", "badge": "HINDI TYPING",
        "desc": "Bidirectional conversion between Krutidev and standard Unicode (Mangal) Hindi fonts."
    },
    "hindi-typing-tutor": {
        "icon": "🇮🇳", "title": "Hindi Typing Tutor", "badge": "HINDI PRACTICE",
        "desc": "Structured typing lessons for Remington Gail, Krutidev, and Mangal Inscript layouts."
    },
    "gst-quick-calc": {
        "icon": "🧾", "title": "GST Quick Calculator", "badge": "TAX & ACCOUNTS",
        "desc": "Fast forward and reverse GST calculation across standard 5%, 12%, 18%, and 28% slabs."
    },
    "exam-resizer": {
        "icon": "📷", "title": "Sarkari Photo & Signature Resizer", "badge": "SARKARI EXAMS",
        "desc": "Strict 20KB–50KB dimension cropping for SSC, UPSC, State PSC, and Railway applications."
    },
    "commerce-accounts-hub": {
        "icon": "📚", "title": "BalanceSheet OS (Class 12)", "badge": "CBSE COMMERCE",
        "desc": "Complete DK Goel Class 12 practical problems with step-by-step journals and ledger working notes."
    },
    "age-eligibility-calc": {
        "icon": "📅", "title": "Exam Age Eligibility Calculator", "badge": "ELIGIBILITY",
        "desc": "Calculate exact age as of cutoff dates specified in competitive exam notifications."
    },
    "smartbanker-ai": {
        "icon": "🏦", "title": "SmartBanker AI", "badge": "BANKING EXAMS",
        "desc": "Banking awareness study modules, mock test questions, and exam readiness assistant."
    },
    "math-workout-app": {
        "icon": "⚡", "title": "Math Speed Sprint", "badge": "MATH SPEED",
        "desc": "Rapid mental arithmetic drills and speed calculations for Banking, SSC, and CSAT exams."
    }
}

cards_html = ""
for slug, meta in CATALOG.items():
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
  <title>Digital Utility Suite — {len(CATALOG)} Free Web Tools</title>
  
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
      padding: 50px 10px 25px;
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
      margin-bottom: 12px;
    }}
    h1 {{
      color: #ffffff;
      font-size: 2.5rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
    }}
    h1 span.bolt {{ color: #fbbf24; }}
    p.sub {{
      color: #94a3b8;
      font-size: 1.05rem;
      margin-top: 8px;
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
      font-size: 30px;
      line-height: 1;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 50px;
      height: 50px;
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
    }}
    .tool-desc {{
      font-size: 0.88rem;
      color: #94a3b8;
      line-height: 1.5;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="hero-badge">Direct Access Network</div>
      <h1><span class="bolt">⚡</span> Digital Utility Suite</h1>
      <p class="sub">Explore all {len(CATALOG)} free student, career, exam, and web utilities.</p>
    </header>

    <div class="grid-tools">
      {cards_html}
    </div>
  </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(hub_html)

print("Generated clean index.html with distinct icons and descriptions for all 21 tools.")
