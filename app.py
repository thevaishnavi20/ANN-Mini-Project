import streamlit as st

st.set_page_config(
    page_title="Campus Placement Analytics - Home",
    layout="wide",
    page_icon="🎓",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    [data-testid="stSidebar"] { display: none; }
    .main { padding: 0; }
    body { background-color: #0a1628; }
    .stApp { background-color: #0a1628; }
    .hero-section {
        background: linear-gradient(135deg, #0a1628 0%, #1a2f5e 50%, #0d2144 100%);
        padding: 8rem 2rem;
        text-align: center;
        color: white;
        border-bottom: 3px solid #c9a84c;
    }
    .hero-title {
        font-size: 4.5rem;
        font-weight: bold;
        color: #c9a84c;
        margin-bottom: 1.5rem;
        line-height: 1.2;
        text-shadow: 0 2px 10px rgba(201,168,76,0.3);
    }
    .hero-subtitle { font-size: 1.8rem; margin-bottom: 3rem; opacity: 0.9; color: #e8d5a3; }
    .features-section {
        background: #0d1f3c;
        padding: 5rem 2rem;
    }
    .features-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        color: #c9a84c;
        margin-bottom: 3rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #1a2f5e 0%, #0d2144 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        border: 1px solid #c9a84c;
        height: 100%;
    }
    .feature-icon { font-size: 4rem; margin-bottom: 1rem; }
    .feature-title { font-size: 1.5rem; font-weight: bold; color: #c9a84c; margin-bottom: 1rem; }
    .feature-desc { font-size: 1rem; color: #b0c4de; }
    .footer {
        background: #060e1f;
        padding: 2rem;
        text-align: center;
        color: #c9a84c;
        font-size: 1rem;
        border-top: 1px solid #c9a84c;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #c9a84c, #f0d080);
        color: #0a1628;
        font-weight: bold;
        font-size: 1.2rem;
        border: none;
        border-radius: 50px;
        padding: 0.8rem 2rem;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #f0d080, #c9a84c);
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">🎓 Campus Placement Analytics</h1>
    <p class="hero-subtitle">Predict Student Placement Success with Data-Driven Insights</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    get_started = st.button("🚀 Get Started", use_container_width=True)

if get_started:
    st.switch_page("pages/1_Dashboard.py")

st.markdown("""<div class="features-section">
<h2 class="features-title">Why Choose Our Platform?</h2>
</div>""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Advanced Analytics</div>
        <div class="feature-desc">Comprehensive data visualization with interactive charts and real-time insights</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">AI Predictions</div>
        <div class="feature-desc">Machine learning powered placement probability predictions with high accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <div class="feature-title">Skill Gap Analysis</div>
        <div class="feature-desc">Identify strengths and weaknesses with detailed performance metrics</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer">Made with ❤️ using Streamlit | Campus Placement Analytics © 2024</div>', unsafe_allow_html=True)
