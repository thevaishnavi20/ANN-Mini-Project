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
    .hero-section {
        background: linear-gradient(135deg, #a4133c 0%, #ff4d6d 100%);
        padding: 8rem 2rem;
        text-align: center;
        color: white;
    }
    .hero-title { font-size: 4.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2; }
    .hero-subtitle { font-size: 1.8rem; margin-bottom: 3rem; opacity: 0.95; }
    .feature-card {
        background: linear-gradient(135deg, #ffccd5 0%, #ff8fa3 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        height: 100%;
    }
    .feature-icon { font-size: 4rem; margin-bottom: 1rem; }
    .feature-title { font-size: 1.8rem; font-weight: bold; color: #a4133c; margin-bottom: 1rem; }
    .feature-desc { font-size: 1.1rem; color: #333; }
    .footer { background: #f8f9fa; padding: 2rem; text-align: center; color: #c9184a; font-size: 1.1rem; }
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
    get_started = st.button("🚀 Get Started", use_container_width=True, type="primary")

if get_started:
    st.switch_page("pages/1_Dashboard.py")

st.markdown("<br><br>", unsafe_allow_html=True)

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
