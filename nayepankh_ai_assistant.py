import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NayePankh AI Assistant",
    page_icon="🕊️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@700&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #F7F9FC;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #1A3C5E 0%, #0D2137 100%);
    color: white;
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stTextInput label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #E8F0F7 !important;
}
[data-testid="stSidebar"] .stMarkdown { color: #CBD8E6; }

/* ── Hero header ── */
.hero {
    background: linear-gradient(135deg, #1A3C5E 0%, #2E6DA4 100%);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    color: white;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    margin: 0 0 0.3rem 0;
    color: white;
}
.hero p { margin: 0; color: #B8D4ED; font-size: 0.95rem; }

/* ── Tab pills ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 6px;
    background: transparent;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 8px 20px;
    font-weight: 500;
    background: white;
    border: 1px solid #D6E4F0;
    color: #1A3C5E;
}
.stTabs [aria-selected="true"] {
    background: #2E6DA4 !important;
    color: white !important;
    border-color: #2E6DA4 !important;
}

/* ── Cards ── */
.card {
    background: white;
    border-radius: 12px;
    padding: 1.4rem;
    border: 1px solid #E2EBF4;
    margin-bottom: 1rem;
    box-shadow: 0 2px 8px rgba(26,60,94,0.06);
}
.card-title {
    font-weight: 600;
    color: #1A3C5E;
    margin-bottom: 0.5rem;
    font-size: 0.95rem;
}

/* ── Chat bubbles ── */
.user-bubble {
    background: #2E6DA4;
    color: white;
    padding: 0.75rem 1rem;
    border-radius: 16px 16px 4px 16px;
    margin: 0.4rem 0 0.4rem 20%;
    font-size: 0.92rem;
}
.bot-bubble {
    background: white;
    color: #1A3C5E;
    padding: 0.75rem 1rem;
    border-radius: 16px 16px 16px 4px;
    margin: 0.4rem 20% 0.4rem 0;
    font-size: 0.92rem;
    border: 1px solid #D6E4F0;
}

/* ── Buttons ── */
.stButton > button {
    background: #2E6DA4;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 500;
    padding: 0.5rem 1.5rem;
    transition: background 0.2s;
}
.stButton > button:hover { background: #1A3C5E; color: white; }

/* ── Text areas & inputs ── */
.stTextArea textarea, .stTextInput input {
    border-radius: 8px !important;
    border: 1px solid #D6E4F0 !important;
    font-family: 'Inter', sans-serif !important;
}

/* ── Info boxes ── */
.tip-box {
    background: #EBF4FF;
    border-left: 4px solid #2E6DA4;
    padding: 0.75rem 1rem;
    border-radius: 0 8px 8px 0;
    font-size: 0.88rem;
    color: #1A3C5E;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🕊️ NayePankh AI")
    st.markdown("---")

    if GROQ_API_KEY:
        st.success("✅ API Key loaded")
    else:
        st.error("❌ GROQ_API_KEY not found in .env")

    st.markdown("---")
    st.markdown("**About NayePankh Foundation**")
    st.markdown(
        "NayePankh Foundation empowers underprivileged youth through education, "
        "internships, and skill development programs across India."
    )
    st.markdown("---")
    st.markdown(
        "<small>Built with ❤️ using Groq + Streamlit<br>"
        "Project by Kavya Kamatham</small>",
        unsafe_allow_html=True,
    )

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>🕊️ NayePankh AI Assistant</h1>
  <p>Empowering the foundation with AI · Volunteer Support · Campaign Generator · FAQ Bot</p>
</div>
""", unsafe_allow_html=True)

# ── Groq client (lazy) ────────────────────────────────────────────────────────
def get_client():
    if not GROQ_API_KEY:
        st.error("❌ GROQ_API_KEY not found. Please add it to your .env file.")
        st.stop()
    return Groq(api_key=GROQ_API_KEY)

def groq_chat(messages, system_prompt, temperature=0.7):
    client = get_client()
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "system", "content": system_prompt}] + messages,
        temperature=temperature,
        max_tokens=1024,
    )
    return response.choices[0].message.content

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🤖 Volunteer Chatbot", "✍️ Campaign Generator", "❓ FAQ Assistant"])

# ═════════════════════════════════════════════════════════════════
# TAB 1 — VOLUNTEER CHATBOT (AI Agent)
# ═════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("""
    <div class="card">
      <div class="card-title">AI Volunteer Assistant</div>
      Ask anything about NayePankh internships, programs, volunteer opportunities, 
      or how to get involved. The AI agent answers on behalf of the foundation.
    </div>
    """, unsafe_allow_html=True)

    CHATBOT_SYSTEM = """You are the official AI Assistant for NayePankh Foundation, 
an NGO that empowers underprivileged youth in India through education, skill development, 
internships, and awareness campaigns.

Answer questions helpfully and warmly about:
- NayePankh internship programs (Technical, Design, Content, etc.)
- Volunteer opportunities and how to join
- The foundation's mission and impact
- How to donate or support
- Application processes and eligibility
- Certificates and benefits for interns/volunteers

If you don't know specific details, give general helpful guidance and encourage 
the person to visit nayepankh.in or contact the foundation directly.
Always be encouraging, warm, and aligned with the NGO's mission of youth empowerment.
Keep responses concise (2-4 short paragraphs max)."""

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Render chat history
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-bubble">🧑 {msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-bubble">🕊️ {msg["content"]}</div>', unsafe_allow_html=True)

    # Input
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input(
            "Your question",
            placeholder="e.g. How do I apply for the AI internship?",
            label_visibility="collapsed",
        )
        col1, col2 = st.columns([5, 1])
        with col2:
            submitted = st.form_submit_button("Send 💬")

    if submitted and user_input.strip():
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.spinner("Thinking..."):
            reply = groq_chat(st.session_state.chat_history, CHATBOT_SYSTEM)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.rerun()

    if st.session_state.chat_history:
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

    st.markdown("""
    <div class="tip-box">
    💡 <b>Try asking:</b> "What internships are available?", 
    "How do I get a certificate?", "What is NayePankh Foundation?"
    </div>
    """, unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════
# TAB 2 — CAMPAIGN CONTENT GENERATOR (AI)
# ═════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("""
    <div class="card">
      <div class="card-title">✍️ AI Campaign Content Generator</div>
      Generate social media posts, email campaigns, and awareness messages 
      for NayePankh Foundation — instantly with AI.
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        content_type = st.selectbox(
            "Content Type",
            ["Instagram Post", "Twitter/X Post", "LinkedIn Post",
             "WhatsApp Message", "Email Campaign", "Awareness Slogan"],
        )
    with col_b:
        tone = st.selectbox(
            "Tone",
            ["Inspiring & Motivational", "Informative", "Urgent & Action-Oriented",
             "Warm & Personal", "Professional"],
        )

    topic = st.text_area(
        "Campaign Topic / Details",
        placeholder="e.g. We're launching a new technical internship program for college students in Hyderabad. Applications open July 2025.",
        height=100,
    )

    include_hashtags = st.checkbox("Include hashtags", value=True)
    include_emoji = st.checkbox("Include emojis", value=True)

    if st.button("🚀 Generate Content"):
        if not topic.strip():
            st.error("Please enter a campaign topic.")
        else:
            extras = []
            if include_hashtags:
                extras.append("relevant hashtags")
            if include_emoji:
                extras.append("appropriate emojis")
            extras_str = f"Include {', '.join(extras)}. " if extras else ""

            prompt = f"""Create a {content_type} for NayePankh Foundation.
Topic: {topic}
Tone: {tone}
{extras_str}
NayePankh Foundation is an NGO empowering underprivileged youth in India through 
education, internships, and skill development.
Make the content compelling, authentic, and aligned with NGO values.
Format it ready to post — no extra explanation needed."""

            with st.spinner("Generating content..."):
                result = groq_chat(
                    [{"role": "user", "content": prompt}],
                    "You are a creative content writer specializing in NGO social media and campaigns. "
                    "Write authentic, impactful content that drives engagement and supports the mission.",
                    temperature=0.85,
                )

            st.markdown("### 📋 Generated Content")
            st.markdown(
                f'<div class="card" style="white-space:pre-wrap;">{result}</div>',
                unsafe_allow_html=True,
            )
            st.download_button(
                "⬇️ Download as .txt",
                data=result,
                file_name=f"nayepankh_{content_type.lower().replace('/', '_').replace(' ', '_')}.txt",
                mime="text/plain",
            )


# ═════════════════════════════════════════════════════════════════
# TAB 3 — FAQ ASSISTANT (AI)
# ═════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("""
    <div class="card">
      <div class="card-title">❓ Smart FAQ Assistant</div>
      Get instant answers about NayePankh programs, eligibility, 
      certificates, timelines, and more.
    </div>
    """, unsafe_allow_html=True)

    # Quick FAQ buttons
    st.markdown("**Quick Questions:**")
    quick_qs = [
        "Who can apply for internships?",
        "Is this internship paid?",
        "How long is the internship?",
        "What certificate will I receive?",
        "How do I contact NayePankh?",
    ]
    cols = st.columns(3)
    for i, q in enumerate(quick_qs):
        with cols[i % 3]:
            if st.button(q, key=f"faq_{i}"):
                st.session_state["faq_question"] = q

    faq_question = st.text_input(
        "Or type your own question",
        value=st.session_state.get("faq_question", ""),
        placeholder="e.g. Can I do multiple internship roles?",
    )

    if st.button("Get Answer 🔍") and faq_question.strip():
        FAQ_SYSTEM = """You are a knowledgeable assistant for NayePankh Foundation FAQ.
Answer questions clearly and concisely about:
- Internship programs: duration (typically 1 month), roles available, eligibility (any college student)
- Certificates: provided upon completion with tasks submitted
- Process: apply via form → selection task → onboarding via WhatsApp
- Roles available: Full Stack, AI, ML, Python, Data Analytics, Vibe Coder, UI/UX, and more
- Cost: completely free, unpaid but gives experience and certificate
- Contact: via their official website nayepankh.in
- Mission: empowering underprivileged youth through skill development

Give a friendly, helpful, concise answer in 2-3 sentences. Be warm and encouraging."""

        with st.spinner("Finding answer..."):
            answer = groq_chat(
                [{"role": "user", "content": faq_question}],
                FAQ_SYSTEM,
                temperature=0.4,
            )

        st.markdown("### 💬 Answer")
        st.markdown(
            f'<div class="card">'
            f'<div class="card-title">Q: {faq_question}</div>'
            f'{answer}'
            f'</div>',
            unsafe_allow_html=True,
        )
        # Clear the quick question state
        if "faq_question" in st.session_state:
            del st.session_state["faq_question"]