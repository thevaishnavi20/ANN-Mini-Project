import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Campus Placement Analytics",
    layout="wide",
    page_icon="🎓",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp { background-color: #0a1628; color: #e8d5a3; }
    [data-testid="stSidebar"] {
        background-color: #0d1f3c;
        border-right: 2px solid #c9a84c;
    }
    [data-testid="stSidebar"] * { color: #e8d5a3 !important; }
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #c9a84c;
        text-align: center;
        padding: 1rem 0;
        text-shadow: 0 2px 10px rgba(201,168,76,0.3);
    }
    h3 { color: #c9a84c !important; }
    .stMetric { background-color: #1a2f5e; border-radius: 10px; padding: 1rem; border: 1px solid #c9a84c; }
    [data-testid="stMetricValue"] { color: #c9a84c !important; }
    [data-testid="stMetricLabel"] { color: #b0c4de !important; }
    .stDataFrame { border: 1px solid #c9a84c; border-radius: 8px; }
    div.stButton > button {
        background: linear-gradient(135deg, #c9a84c, #f0d080);
        color: #0a1628;
        font-weight: bold;
        border: none;
        border-radius: 8px;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #f0d080, #c9a84c);
    }
    .stSelectbox > div { background-color: #1a2f5e; border: 1px solid #c9a84c; }
    hr { border-color: #c9a84c; }
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("data/campus_placement_cleaned_final_ANN.csv")

df = load_data()

# ---------------- TITLE ----------------
st.markdown('<h1 class="main-header">🎓 Campus Placement Analytics</h1>', unsafe_allow_html=True)
st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.header("🔎 Filter Data")
filter_col = st.sidebar.selectbox("Select column", df.columns)
selected_values = st.sidebar.multiselect("Select values", df[filter_col].unique())

if selected_values:
    df_filtered = df[df[filter_col].isin(selected_values)]
else:
    df_filtered = df.copy()

# ---------------- KEY METRICS ----------------
st.markdown("### 📊 Key Metrics")

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("📚 Total Students", df_filtered.shape[0], delta="Active")
with c2:
    placed = df_filtered[df_filtered['PlacementStatus'] == 'placed'].shape[0] if 'PlacementStatus' in df_filtered.columns else 0
    st.metric("✅ Placed", placed)
with c3:
    avg_score = df_filtered.select_dtypes(include=np.number).mean().mean()
    st.metric("📈 Avg Score", f"{avg_score:.1f}")
with c4:
    st.metric("🔍 Filtered By", filter_col[:15])

# ---------------- DATASET PREVIEW ----------------
st.markdown("### 📋 Dataset Preview")
st.dataframe(df_filtered.head(10), use_container_width=True)

# ---------------- SKILL GAP ANALYSIS ----------------
st.markdown("### 📊 Skill Gap Analysis")

skill_cols = ['Technical_Skills_Score', 'SoftSkillsRating', 'AptitudeTestScore']
available_skills = [col for col in skill_cols if col in df_filtered.columns]

if available_skills:
    skill_avg = df_filtered[available_skills].mean()
    skill_target = pd.Series([80, 4.5, 75], index=['Technical_Skills_Score', 'SoftSkillsRating', 'AptitudeTestScore'])

    skill_gap_data = pd.DataFrame({
        'Skill': available_skills,
        'Current Avg': [skill_avg[s] for s in available_skills],
        'Target': [skill_target[s] if s in skill_target.index else 80 for s in available_skills]
    })

    fig = go.Figure()
    fig.add_trace(go.Bar(name='Current', x=skill_gap_data['Skill'], y=skill_gap_data['Current Avg'], marker_color='#c9a84c'))
    fig.add_trace(go.Bar(name='Target', x=skill_gap_data['Skill'], y=skill_gap_data['Target'], marker_color='#1a2f5e'))
    fig.update_layout(barmode='group', title='Skill Gap Analysis', height=400,
                      paper_bgcolor='#0a1628', plot_bgcolor='#0d1f3c',
                      font_color='#e8d5a3', title_font_color='#c9a84c')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Skill data not available")

# ---------------- TIMELINE OF PLACEMENT DRIVES ----------------
st.markdown("### 📅 Timeline of Placement Drives")

timeline_data = pd.DataFrame({
    'Company': ['TCS', 'Infosys', 'Wipro', 'Accenture', 'Cognizant', 'HCL'],
    'Date': pd.date_range(start='2024-01-15', periods=6, freq='15D'),
    'Students_Placed': [45, 38, 52, 30, 41, 35]
})

fig = px.scatter(timeline_data, x='Date', y='Students_Placed', size='Students_Placed',
                 color='Company', title='Placement Drive Timeline',
                 hover_data=['Company', 'Students_Placed'],
                 color_discrete_sequence=['#c9a84c', '#f0d080', '#b0c4de', '#4a7fc1', '#1a2f5e', '#e8d5a3'])
fig.update_layout(height=400, paper_bgcolor='#0a1628', plot_bgcolor='#0d1f3c',
                  font_color='#e8d5a3', title_font_color='#c9a84c')
st.plotly_chart(fig, use_container_width=True)

# ---------------- VISUALIZATIONS ----------------
st.markdown("### 📈 Data Visualizations")

col1, col2 = st.columns(2)

with col1:
    numeric_cols = df_filtered.select_dtypes(include=np.number).columns
    num_col = st.selectbox("Select numeric column", numeric_cols)

    fig = px.histogram(df_filtered, x=num_col, nbins=30,
                       title=f"Distribution of {num_col}",
                       color_discrete_sequence=['#c9a84c'])
    fig.update_layout(showlegend=False, height=400, paper_bgcolor='#0a1628',
                      plot_bgcolor='#0d1f3c', font_color='#e8d5a3', title_font_color='#c9a84c')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.box(df_filtered, y=num_col,
                 title=f"Box Plot of {num_col}",
                 color_discrete_sequence=['#f0d080'])
    fig.update_layout(showlegend=False, height=400, paper_bgcolor='#0a1628',
                      plot_bgcolor='#0d1f3c', font_color='#e8d5a3', title_font_color='#c9a84c')
    st.plotly_chart(fig, use_container_width=True)

# ---------------- PLACEMENT PREDICTION ----------------
st.markdown("---")
st.markdown("### 🎯 Placement Prediction")

col1, col2 = st.columns([1, 2])

with col1:
    if len(df_filtered) > 0:
        student_options = ["-- Select a Student --"] + list(df_filtered['StudentID'])
        selected_student = st.selectbox("Select Student Name", student_options)
    else:
        selected_student = None
        st.warning("⚠️ No students available in filtered data")

    if selected_student and selected_student != "-- Select a Student --":
        student = df_filtered[df_filtered['StudentID'] == selected_student].iloc[0]
        features = ["Internships", "Projects", "Workshops/Certifications", "AptitudeTestScore",
                    "SoftSkillsRating", "ExtracurricularActivities", "PlacementTraining",
                    "SSC_Marks", "HSC_Marks", "Technical_Skills_Score"]
        available_features = [f for f in features if f in student.index]
        display_df = pd.DataFrame({"Feature": available_features, "Value": [student[f] for f in available_features]})
        st.dataframe(display_df, use_container_width=True, height=400)

with col2:
    if selected_student and selected_student != "-- Select a Student --":
        student = df_filtered[df_filtered['StudentID'] == selected_student].iloc[0]
        available_features = [f for f in ["Internships", "Projects", "Workshops/Certifications", "AptitudeTestScore",
                                           "SoftSkillsRating", "ExtracurricularActivities", "PlacementTraining",
                                           "SSC_Marks", "HSC_Marks", "Technical_Skills_Score"] if f in student.index]
        fig = go.Figure(go.Bar(
            x=[student[f] for f in available_features if pd.api.types.is_numeric_dtype(type(student[f]))],
            y=[f for f in available_features if pd.api.types.is_numeric_dtype(type(student[f]))],
            orientation='h',
            marker=dict(color='#c9a84c')
        ))
        fig.update_layout(title="Student Profile", height=400, xaxis_title="Score", yaxis_title="Features",
                          paper_bgcolor='#0a1628', plot_bgcolor='#0d1f3c',
                          font_color='#e8d5a3', title_font_color='#c9a84c')
        st.plotly_chart(fig, use_container_width=True)

# ---------------- PREDICTION LOGIC ----------------
def predict_placement(row):
    score = 0
    if row["Internships"] > 0: score += 15
    if row["Projects"] >= 2: score += 15
    if row["Workshops/Certifications"] >= 1: score += 10
    if row["AptitudeTestScore"] >= 70: score += 15
    if row["SoftSkillsRating"] >= 4: score += 10
    if row["Technical_Skills_Score"] >= 60: score += 15
    if row["PlacementTraining"] == "Yes": score += 10
    return min(score, 100)

predict_btn = st.button("🔮 Predict Placement", use_container_width=True)

if predict_btn:
    if not selected_student or selected_student == "-- Select a Student --" or len(df_filtered) == 0:
        st.warning("⚠️ Please select a student name from the dropdown above to predict placement")
    else:
        student = df_filtered[df_filtered['StudentID'] == selected_student].iloc[0]
        confidence = predict_placement(student)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=confidence,
                title={'text': "Placement Confidence", 'font': {'color': '#c9a84c'}},
                gauge={'axis': {'range': [None, 100]},
                       'bar': {'color': "#c9a84c"},
                       'steps': [
                           {'range': [0, 40], 'color': "#0d1f3c"},
                           {'range': [40, 70], 'color': "#1a2f5e"},
                           {'range': [70, 100], 'color': "#2a4a8e"}],
                       'threshold': {'line': {'color': "#f0d080", 'width': 4}, 'thickness': 0.75, 'value': 60}}
            ))
            fig.update_layout(height=300, paper_bgcolor='#0a1628', font_color='#e8d5a3')
            st.plotly_chart(fig, use_container_width=True)

            if confidence >= 60:
                st.success(f"✅ Likely PLACED (Confidence: {confidence:.0f}%)")
            else:
                st.error(f"❌ Likely NOT PLACED (Confidence: {confidence:.0f}%)")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("<div style='text-align: center; color: #c9a84c;'>Made with ❤️ using Streamlit | Campus Placement Analytics © 2024</div>", unsafe_allow_html=True)
