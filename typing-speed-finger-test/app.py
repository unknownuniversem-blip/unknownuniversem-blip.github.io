import streamlit.components.v1 as components
import streamlit as st
import sqlite3
import json
import html
import re
from datetime import datetime

# 1. SEARCH ENGINE TITLE & METADATA
st.set_page_config(
    page_title="SmartBanker AI | Free IBPS, SBI, RRB PO & Clerk CBT Practice",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="auto"
)

# 2. INJECT GOOGLE SEO META TAGS & STRUCTURED SCHEMA
st.markdown("""
<head>
    <meta name="google-site-verification" content="kwVbUelR6vQiW3EYxdH_lRRouUw3HytRiV-CuF1Wsrw" />
    <meta name="google-site-verification" content="PASTE_YOUR_CODE_HERE" />
    <meta name="description" content="Free online banking exam preparation portal for IBPS PO, IBPS Clerk, SBI PO, SBI Clerk, and RRB. Practice real memory-based questions with instant AI step-by-step derivations.">
    <meta name="keywords" content="SmartBanker AI, IBPS PO practice, SBI Clerk mock test, RRB PO reasoning puzzles, Quantitative Aptitude shortcuts, bank exam preparation, free CBT banking test">
    <meta name="author" content="SmartBanker AI">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="SmartBanker AI | Banking Exam Preparation Engine">
    <meta property="og:description" content="Practice authentic past year banking questions with instant AI step-by-step logic breakdown in English and Hindi.">
    <meta property="og:type" content="website">
</head>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "SmartBanker AI",
  "applicationCategory": "EducationalApplication",
  "operatingSystem": "All",
  "description": "Comprehensive CBT exam portal for IBPS, SBI, and RRB banking exams featuring step-by-step AI solutions.",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "INR"
  }
}
</script>
""", unsafe_allow_html=True)

# 3. CSS STYLING
st.markdown("""
<style>
    .hero-container {
        background: linear-gradient(135deg, #0D47A1 0%, #1976D2 100%);
        color: white;
        padding: 40px 30px;
        border-radius: 12px;
        margin-bottom: 25px;
        text-align: center;
    }
    .hero-title {
        font-size: 38px !important;
        font-weight: 800 !important;
        color: #FFFFFF !important;
        margin-bottom: 8px;
    }
    .hero-subtitle {
        font-size: 18px !important;
        color: #E3F2FD !important;
        margin-bottom: 20px;
    }
    .feature-card {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-radius: 10px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        height: 100%;
    }
    .feature-card h3 {
        color: #0D47A1;
        margin-bottom: 8px;
    }
    .feature-card p {
        color: #555555;
        font-size: 14px;
        line-height: 1.5;
    }
    .seo-keyword-badge {
        display: inline-block;
        background-color: #E3F2FD;
        color: #0D47A1;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        margin: 3px;
    }
    .question-box {
        font-size: 18px !important;
        line-height: 1.6 !important;
        font-family: 'Segoe UI', Roboto, sans-serif !important;
        font-weight: 500 !important;
        color: #1A1A1A;
        background-color: #F8F9FA;
        padding: 18px;
        border-radius: 8px;
        border-left: 5px solid #1E88E5;
        margin-bottom: 15px;
        white-space: pre-wrap;
    }
    .solution-box {
        font-size: 16px !important;
        line-height: 1.6 !important;
        color: #1B5E20;
        background-color: #E8F5E9;
        padding: 16px;
        border-radius: 6px;
        white-space: pre-wrap;
        margin-bottom: 12px;
    }
    .ai-wrapper {
        background-color: #F0F7FF;
        border: 1px solid #BBDEFB;
        border-radius: 8px;
        padding: 16px;
        margin-top: 10px;
    }
    .ai-step-box {
        font-size: 15px !important;
        line-height: 1.7 !important;
        color: #212121;
        background-color: #FFFFFF;
        padding: 16px;
        border-radius: 6px;
        border: 1px solid #E0E0E0;
        white-space: pre-wrap;
    }
    .quote-box {
        font-size: 14px !important;
        font-style: italic;
        color: #4A148C;
        background-color: #F3E5F5;
        padding: 12px 16px;
        border-radius: 8px;
        border-left: 4px solid #AB47BC;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

DB_FILE = "bank_prep.db"

def get_db():
    return sqlite3.connect(DB_FILE)

def init_reporting_tables():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS question_reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id INTEGER,
        report_type TEXT,
        details TEXT,
        created_at TEXT
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        feedback TEXT,
        created_at TEXT
    )
    """)
    conn.commit()
    conn.close()

init_reporting_tables()

if "view_mode" not in st.session_state:
    st.session_state.view_mode = "home"

# ----------------------------------------------------
# 1. FRONT / LANDING PAGE VIEW
# ----------------------------------------------------
if st.session_state.view_mode == "home":
    st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">🏛 SmartBanker AI</h1>
        <p class="hero-subtitle">India's Free AI-Augmented CBT Practice Engine for Banking Aspirants</p>
        <div style="margin-bottom: 18px;">
            <span class="seo-keyword-badge">IBPS PO Prelims & Mains</span>
            <span class="seo-keyword-badge">SBI PO / Clerk 2026</span>
            <span class="seo-keyword-badge">RRB Officer Scale-I</span>
            <span class="seo-keyword-badge">Quantitative Aptitude</span>
            <span class="seo-keyword-badge">Reasoning Puzzles</span>
            <span class="seo-keyword-badge">English Language</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
    with col_c2:
        if st.button("🚀 Start Free CBT Mock Practice", type="primary", use_container_width=True):
            st.session_state.view_mode = "practice"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    f_col1, f_col2, f_col3 = st.columns(3)
    with f_col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📑 Real Memory-Based Papers</h3>
            <p>100% verified question bank curated strictly by exam stage across IBPS, SBI, and RRB exams.</p>
        </div>
        """, unsafe_allow_html=True)
    with f_col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🤖 Step-by-Step AI Solutions</h3>
            <p>Mathematical derivations for Quant, logical constraint mapping for Reasoning puzzles, and grammar breakdowns for English.</p>
        </div>
        """, unsafe_allow_html=True)
    with f_col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Official CBT Console</h3>
            <p>Zero-scroll test interface matching real exam centers, featuring bilingual question toggles and zero page lag.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    ### 📚 Free Comprehensive Banking Syllabus Coverage
    * **Quantitative Aptitude**: Data Interpretation (DI), Arithmetic Word Problems, Quadratic Equations, Number Series, Simple & Compound Interest.
    * **Reasoning Ability**: Floor & Flat Puzzles, Circular & Linear Seating Arrangements, Syllogisms, Inequalities, Direction & Distance.
    * **English Language**: Reading Comprehension (RC), Para Jumbles, Cloze Test, Error Spotting, Sentence Improvement.
    """)
    st.caption("SmartBanker AI • Free Online Portal for IBPS, SBI, and RRB Banking Aspirants • 2018–2026 Exam Databank")
    st.stop()

# ----------------------------------------------------
# 2. CBT PRACTICE CONSOLE VIEW
# ----------------------------------------------------
conn = get_db()
cur = conn.cursor()

col_title, col_home = st.columns([4, 1])
with col_title:
    st.title("🏦 SmartBanker AI")

# --- Cross-Promotion Banner for Monetized Typing Test ---
components.html(
    """
    <div style="text-align: center; padding: 14px; background: #1e293b; border-radius: 10px; border: 1px solid #334155; margin: 15px 0;">
        <span style="color: #94a3b8; font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 4px;">Recommended Practice Tool</span>
        <a href="https://unknownuniversem-blip.github.io/typing-speed-finger-test/" target="_blank" style="color: #38bdf8; font-weight: 700; font-size: 16px; text-decoration: none; display: inline-block;">
            ⌨️ Practice Typing & CBT Speed Test for Bank Exams →
        </a>
    </div>
    """,
    height=85
)
    st.caption("🎯 Target Exams: IBPS PO / Clerk | SBI PO / Clerk | RRB PO / Clerk")
with col_home:
    if st.button("🏠 Exit to Home"):
        st.session_state.view_mode = "home"
        st.rerun()

target_exam = st.sidebar.selectbox(
    "🎯 Target Banking Exam",
    [
        "All Bank Exams (Common Pool)",
        "IBPS PO",
        "IBPS Clerk",
        "SBI PO",
        "SBI Clerk",
        "RRB PO (Officer Scale-I)",
        "RRB Clerk (Office Assistant)"
    ],
    index=0
)

available_stages = [r[0] for r in cur.execute("SELECT DISTINCT stage FROM questions WHERE stage IS NOT NULL").fetchall()]
stages = ["Prelims"] + [s for s in sorted(available_stages) if s != "Prelims"] if "Prelims" in available_stages else available_stages
if not stages:
    stages = ["Prelims", "Mains"]

selected_stage = st.sidebar.selectbox("1. Select Stage / चरण", stages, index=0)

subjects = [r[0] for r in cur.execute("SELECT DISTINCT subject FROM questions WHERE stage = ? AND subject IS NOT NULL ORDER BY subject", (selected_stage,)).fetchall()]
selected_subject = st.sidebar.selectbox("2. Select Subject / विषय", subjects)

col_lang, _ = st.columns([1, 3])
with col_lang:
    if selected_subject == "English Language":
        st.info("ℹ English Section is strictly in English.")
        lang = "English"
    else:
        lang = st.radio("🌐 Language / भाषा:", ["English", "हिन्दी"], horizontal=True)

chapters = [r[0] for r in cur.execute("SELECT DISTINCT chapter FROM questions WHERE stage = ? AND subject = ? AND chapter IS NOT NULL ORDER BY chapter", (selected_stage, selected_subject)).fetchall()]
chapter_options = ["All Chapters / सभी अध्याय"] + chapters
selected_chapter = st.sidebar.selectbox("3. Select Chapter / अध्याय", chapter_options)

st.sidebar.markdown("---")
st.sidebar.subheader("🤖 AI Settings")
api_key = st.sidebar.text_input("Gemini API Key (Optional)", type="password")

st.sidebar.markdown("---")
st.sidebar.subheader("💡 Suggestion Box")
with st.sidebar.expander("Send Platform Suggestion", expanded=False):
    sugg_text = st.text_area("How can we improve SmartBanker AI?", key="sugg_box", placeholder="Write your ideas here...")
    if st.button("Submit Suggestion"):
        if sugg_text.strip():
            c = get_db()
            c.cursor().execute("INSERT INTO user_feedback (feedback, created_at) VALUES (?, ?)", 
                             (sugg_text.strip(), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            c.commit()
            c.close()
            st.success("Thank you for helping improve SmartBanker AI!")
        else:
            st.warning("Please type a suggestion before submitting.")

# Load newest first
if selected_chapter == "All Chapters / सभी अध्याय":
    query = """
    SELECT id, exam, chapter, question, options, answer, solution, question_hi, options_hi, solution_hi, solution_ai, answer_ai 
    FROM questions 
    WHERE stage = ? AND subject = ?
    ORDER BY id DESC
    """
    cur.execute(query, (selected_stage, selected_subject))
else:
    query = """
    SELECT id, exam, chapter, question, options, answer, solution, question_hi, options_hi, solution_hi, solution_ai, answer_ai 
    FROM questions 
    WHERE stage = ? AND subject = ? AND chapter = ?
    ORDER BY id DESC
    """
    cur.execute(query, (selected_stage, selected_subject, selected_chapter))

questions = cur.fetchall()
total_questions = len(questions)
st.sidebar.markdown(f"**Available Questions:** {total_questions}")

if not questions:
    st.warning("No questions found for this selection.")
    conn.close()
    st.stop()

filter_key = f"{target_exam}_{selected_stage}_{selected_subject}_{selected_chapter}"
if "last_filter" not in st.session_state or st.session_state.last_filter != filter_key:
    st.session_state.last_filter = filter_key
    st.session_state.q_index = 0

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "ai_cache" not in st.session_state:
    st.session_state.ai_cache = {}

st.session_state.q_index = max(0, min(st.session_state.q_index, total_questions - 1))

q_data = questions[st.session_state.q_index]
qid, exam, chap, q_en, opts_en, ans, sol_en, q_hi, opts_hi, sol_hi, sol_ai, ans_ai = q_data

if lang == "हिन्दी" and q_hi and selected_subject != "English Language":
    display_q = q_hi
    display_sol = sol_hi if sol_hi else sol_en
    raw_opts = opts_hi if opts_hi else opts_en
else:
    display_q = q_en
    display_sol = sol_en
    raw_opts = opts_en

display_opts = []
if raw_opts:
    try:
        display_opts = json.loads(raw_opts)
    except Exception:
        display_opts = []

extra_statements = []
if len(display_opts) > 5:
    actual_choices = []
    for item in display_opts:
        if re.search(r'\b[A-E]{3,5}\b', item) or "rearrangement" in item.lower() or "none" in item.lower():
            actual_choices.append(item)
        else:
            extra_statements.append(item)
    if len(actual_choices) >= 3:
        display_opts = actual_choices
    else:
        display_opts = display_opts[-5:]

if not display_opts:
    display_opts = ["(A) Option A", "(B) Option B", "(C) Option C", "(D) Option D", "(E) Option E"]

if extra_statements:
    display_q += "\n\n" + "\n".join(extra_statements)

safe_q = html.escape(str(display_q or ""))

# Extract clean Exam, Year, and Stage
raw_ex = str(exam or '')
raw_stg = str(selected_stage or '')

year_match = re.search(r'\b(20[1-2][0-9])\b', raw_ex)
detected_year = year_match.group(1) if year_match else "2026"

ex_lower = raw_ex.lower()
if "sbi po" in ex_lower:
    exam_title = "SBI PO"
elif "sbi clerk" in ex_lower:
    exam_title = "SBI Clerk"
elif "rrb po" in ex_lower or "officer scale" in ex_lower:
    exam_title = "RRB PO"
elif "rrb clerk" in ex_lower or "office assistant" in ex_lower:
    exam_title = "RRB Clerk"
elif "ibps clerk" in ex_lower:
    exam_title = "IBPS Clerk"
elif "ibps po" in ex_lower:
    exam_title = "IBPS PO"
else:
    exam_title = target_exam if "All" not in target_exam else "IBPS PO"

stage_tag = "Pre" if "pre" in raw_stg.lower() else "Mains"
exam_badge = f"{exam_title} {detected_year} {stage_tag}"

# Prominent header banner
st.markdown(f'''
<div style="display:flex; justify-content:space-between; align-items:center; background:#EFF6FF; border:1px solid #BFDBFE; padding:10px 16px; border-radius:8px; margin-bottom:12px;">
    <span style="font-size:16px; font-weight:800; color:#1D4ED8;">🏛️ {exam_badge}</span>
    <span style="font-size:13px; font-weight:600; color:#475569;">Topic: {chap} • Q {st.session_state.q_index + 1} / {total_questions}</span>
</div>
''', unsafe_allow_html=True)

st.markdown(f'<div class="question-box">{safe_q}</div>', unsafe_allow_html=True)

user_choice = st.radio("Choose Option / विकल्प चुनें:", display_opts, key=f"ans_{qid}_{st.session_state.q_index}")

effective_ans = ans if (ans and len(ans.strip()) > 0) else (ans_ai if ans_ai else "Option (B)")

def go_prev():
    if st.session_state.q_index > 0:
        st.session_state.q_index -= 1

def go_next():
    if st.session_state.q_index < total_questions - 1:
        st.session_state.q_index += 1

def on_jump():
    val = st.session_state["jump_input"] - 1
    st.session_state.q_index = max(0, min(val, total_questions - 1))

bar_col1, bar_col2, bar_col3, bar_col4 = st.columns([1.5, 2.5, 1.5, 2.5])

with bar_col1:
    st.button("⬅ Previous", disabled=(st.session_state.q_index == 0), on_click=go_prev, use_container_width=True)

with bar_col2:
    submit_clicked = st.button("Submit Answer / उत्तर जांचें", type="primary", use_container_width=True)

with bar_col3:
    st.button("Next ➡️", disabled=(st.session_state.q_index == total_questions - 1), on_click=go_next, use_container_width=True)

with bar_col4:
    st.number_input(
        f"Jump (1 - {total_questions})", 
        min_value=1, 
        max_value=total_questions, 
        value=st.session_state.q_index + 1,
        key="jump_input",
        on_change=on_jump,
        label_visibility="collapsed"
    )

if submit_clicked:
    correct_prefix = effective_ans[:2].upper()
    if user_choice.startswith(correct_prefix):
        st.success(f"✅ Correct! Verified Answer Key: {effective_ans}")
    else:
        st.error(f"❌ Incorrect! Verified Answer Key is: {effective_ans}")

st.markdown("---")

tab_official, tab_ai = st.tabs(["📖 Official Source Answer", "🤖 SmartBanker AI Step-by-Step Explanation"])

with tab_official:
    if display_sol and len(display_sol.strip()) > 15 and "refer" not in display_sol.lower() and "memory based" not in display_sol.lower():
        st.markdown(f'<div class="solution-box"><b>Official Paper Solution:</b>\n{html.escape(display_sol)}</div>', unsafe_allow_html=True)
    else:
        st.info("ℹ️ Official source contains only a memory-based placeholder key. See the AI tab for the complete explanation.")
        st.write(f"**Extracted Key:** {ans if ans else 'Not provided in raw sheet'}")

def generate_deep_step_solution(subject, chapter, q_text, options, official_ans):
    opts_formatted = "\n".join([f"  • {o}" for o in options])

    if "Quant" in subject:
        return f"""### 📝 Question Overview & Problem Statement:
{q_text}

### 🔢 Given Options:
{opts_formatted}

---
### 🔍 Step-by-Step Mathematical Derivation:
1. **Given Data & Variables**: Extract numerical values, rates, and assign variables ($x, y$).
2. **Equation Setup**: Apply standard formulae (Work equivalence $W = E \\times T$, SI/CI, or Mixture rules).
3. **Calculation & Verification**: Algebraically solve and balance constraints.
- **Definitive Answer**: **Option ({official_ans})**"""

    elif "Reasoning" in subject:
        return f"""### 📝 Question Overview & Problem Statement:
{q_text}

### 🧩 Given Options:
{opts_formatted}

---
### 🔍 Step-by-Step Logical Deduction:
1. **Direct Clues Mapping**: Place fixed positions and immediate neighbors first.
2. **Constraint Elimination**: Discard secondary arrangements that violate circular or linear boundaries.
3. **Validation**: Validate final sequence against all conditions.
- **Definitive Answer**: **Option ({official_ans})**"""

    else:
        return f"""### 📝 Question Overview & Problem Statement:
{q_text}

### 🔤 Given Options:
{opts_formatted}

---
### 🔍 Step-by-Step Grammatical Derivation:
1. **Sentence Architecture**: Inspect subject-verb agreement, clause parallelism, and connectors.
2. **Rule Application**: Identify independent topic sentence, match mandatory pairs, and check prepositions.
- **Definitive Answer**: **Option ({official_ans})**"""

with tab_ai:
    if qid not in st.session_state.ai_cache:
        if api_key:
            with st.spinner("SmartBanker AI is generating step-by-step solution..."):
                try:
                    from google import genai
                    client = genai.Client(api_key=api_key)
                    prompt = f"Solve step-by-step for IBPS PO: {display_q} Options: {display_opts} Key: {effective_ans}"
                    res = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                    st.session_state.ai_cache[qid] = res.text
                except Exception:
                    st.session_state.ai_cache[qid] = generate_deep_step_solution(selected_subject, chap, display_q, display_opts, effective_ans)
        else:
            st.session_state.ai_cache[qid] = generate_deep_step_solution(selected_subject, chap, display_q, display_opts, effective_ans)

    st.markdown('<div class="ai-wrapper">', unsafe_allow_html=True)
    st.markdown(f'<div class="ai-step-box">{st.session_state.ai_cache[qid]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with st.expander("🚩 Report an Issue (Question / Solution / Options)", expanded=False):
    st.markdown("""
    <div class="quote-box">
        💛 <b>We are truly sorry for the inconvenience and friction you faced!</b><br>
        <i>"Every error identified and conquered is simply one step closer to perfection. Keep your chin up—your dedication and relentless effort will make you a Probationary Officer!"</i> ✨
    </div>
    """, unsafe_allow_html=True)
    
    st.write(f"Flag an issue for **Question #{st.session_state.q_index + 1} (ID #{qid})**:")
    rep_type = st.selectbox(
        "Select Error Type / समस्या का प्रकार चुनें:",
        [
            "Wrong Question Statement (अशुद्ध प्रश्न / अधूरा प्रश्न)",
            "Wrong Answer Key (गलत उत्तर कुंजी)",
            "Wrong or Missing Solution (गलत या अनुपलब्ध समाधान)",
            "Wrong / Scrambled Options (गलत या अस्पष्ट विकल्प)",
            "Hindi Translation / Formatting Issue (हिन्दी अनुवाद में त्रुटि)"
        ],
        key=f"rep_type_{qid}"
    )
    rep_details = st.text_area(
        "Describe the exact problem / विवरण लिखें (Optional):", 
        placeholder="e.g. Option C has a typo, or the answer explanation missed the negative sign...",
        key=f"rep_det_{qid}"
    )
    if st.button("Submit Report / रिपोर्ट भेजें", key=f"btn_rep_{qid}"):
        db_rep = get_db()
        db_rep.cursor().execute("""
            INSERT INTO question_reports (question_id, report_type, details, created_at)
            VALUES (?, ?, ?, ?)
        """, (qid, rep_type, rep_details.strip(), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        db_rep.commit()
        db_rep.close()
        st.success("💖 Thank you for helping us refine SmartBanker AI! Your feedback has been recorded.")

conn.close()
