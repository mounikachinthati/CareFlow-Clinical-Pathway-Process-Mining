import streamlit as st
import pandas as pd
import random

# Generate 500 patients data on the fly so no CSV file is needed
def generate_data():
    depts = ['General Medicine', 'Surgery', 'Orthopedics', 'Cardiology', 'Gynecology']
    pathways = ['Respiratory Infection', 'Fracture', 'Cardiovascular', 'Diabetes', 'Gastrointestinal']
    data = []
    for i in range(1, 501):
        data.append({
            "PatientID": f"P{i:03d}",
            "Department": random.choice(depts),
            "Pathway": random.choice(pathways),
            "LengthOfStay": round(random.uniform(3.0, 8.0), 1),
            "IsCompliant": random.choice(['Yes', 'No', 'Yes', 'Yes']), # more Yes
            "Readmitted": random.choice(['Yes', 'No', 'No', 'No', 'No']), # less Yes
            "Cost": random.randint(3000, 7000)
        })
    return pd.DataFrame(data)

df = generate_data()

# --- Custom CSS to match your image exactly ---
st.set_page_config(page_title="CareFlow Dashboard", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    /* Main background */
    .stApp { background-color: #F4F7F9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* Hide Streamlit default stuff */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding-top: 1rem; padding-bottom: 1rem; max-width: 95%; }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] { background-color: #0B192C !important; }
    [data-testid="stSidebar"] * { color: #FFFFFF !important; font-family: 'Segoe UI', sans-serif; }
    
    /* Metric Cards Styling */
    div[data-testid="metric-container"] {
        background-color: white;
        border-radius: 8px;
        padding: 15px 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        border-left: 4px solid #2563EB;
    }
    div[data-testid="metric-container"] label { color: #64748B !important; font-weight: 600; font-size: 14px;}
    div[data-testid="metric-container"] div[data-testid="stMetricValue"] { color: #0F172A; font-size: 28px; font-weight: bold; }
    
    /* Custom Cards for Process Flow */
    .process-card {
        background-color: white; padding: 20px; border-radius: 10px; text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05); border-top: 3px solid #2563EB;
    }
    .process-card h3 { margin: 0; color: #2563EB; font-size: 24px; }
    .process-card p { margin: 5px 0 0 0; color: #64748B; font-size: 14px; }
    
    /* Headers */
    h1, h2, h3 { color: #0F172A; font-weight: 700; }
    h3 { font-size: 18px; border-bottom: 2px solid #E2E8F0; padding-bottom: 10px; margin-bottom: 15px;}
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.markdown("<h2>🏥 CareFlow</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:12px; color:#94A3B8;'>Clinical Pathway Process Mining</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

page = st.sidebar.radio("Navigation", ["Overview", "Process Mining"])
st.sidebar.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size:12px; color:#94A3B8;'>Data Period<br>01 Jan 2025 - 30 Sep 2025</p>", unsafe_allow_html=True)

# --- KPI Calculations ---
total_patients = len(df)
avg_los = df['LengthOfStay'].mean()
total_time = avg_los * 4.4 # fake calc for display
readmit_rate = (len(df[df['Readmitted'] == 'Yes']) / total_patients) * 100

if page == "Overview":
    # Header area
    col_head1, col_head2 = st.columns([3, 1])
    with col_head1:
        st.markdown("<h1>Executive Dashboard</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#64748B;'>Key insights into patient flow, operational performance and clinical efficiency</p>", unsafe_allow_html=True)
    
    # KPI Row
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Patients", f"{total_patients:,}", "↑ 8.4%")
    c2.metric("Avg. Length of Stay", f"{avg_los:.1f} Days", "↓ 12.5%")
    c3.metric("Total Process Time", f"{total_time:.1f} Hours", "↓ 15.8%")
    c4.metric("Readmission Rate", f"{readmit_rate:.1f}%", "↓ 2.1%")
    c5.metric("Patient Satisfaction", "92%", "↑ 4.7%")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Middle Row: Process Flow & Pie Chart placeholder
    col_mid1, col_mid2 = st.columns([1.5, 1])
    
    with col_mid1:
        st.markdown("<div style='background:white; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.05);'><h3>Patient Flow Through Clinical Pathway</h3>", unsafe_allow_html=True)
        f1, f2, f3, f4 = st.columns(4)
        f1.markdown("<div class='process-card'><h3>12,482</h3><p>Admission (100%)</p></div>", unsafe_allow_html=True)
        f2.markdown("<div class='process-card'><h3>11,856</h3><p>Diagnosis (95%)</p></div>", unsafe_allow_html=True)
        f3.markdown("<div class='process-card'><h3>10,982</h3><p>Treatment (88%)</p></div>", unsafe_allow_html=True)
        f4.markdown("<div class='process-card'><h3>10,421</h3><p>Discharge (83%)</p></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("<div style='background:white; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.05);'><h3>Process Performance</h3>", unsafe_allow_html=True)
        perf_data = pd.DataFrame({
            "Stage": ["Admission", "Diagnosis", "Treatment", "Discharge"],
            "Avg. Time (Hours)": [2.1, 4.3, 7.8, 4.4],
            "vs Target": ["↓ 18%", "↓ 22%", "↓ 15%", "↓ 20%"],
            "Trend": ["～～", "～～", "～～", "～～"]
        })
        st.dataframe(perf_data, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_mid2:
        st.markdown("<div style='background:white; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.05);'><h3>Patient Volume by Department</h3>", unsafe_allow_html=True)
        dept_counts = df['Department'].value_counts()
        # Streamlit native bar chart looks better inside the box
        st.bar_chart(dept_counts, color="#2563EB")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("<div style='background:white; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.05);'><h3>Top 5 Diagnoses</h3>", unsafe_allow_html=True)
        path_counts = df['Pathway'].value_counts().head(5)
        st.bar_chart(path_counts, color="#F59E0B")
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "Process Mining":
    st.markdown("<h1>Process Mining & Patient Flow Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748B;'>Visualizing actual vs. ideal process, bottlenecks and opportunities for improvement</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("<div style='background:white; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.05);'><h3>Process Flow (Actual vs. Ideal)</h3>", unsafe_allow_html=True)
        st.info("Admission (2.1h) ➡ Diagnosis (4.3h) ➡ Treatment (7.8h) ➡ Discharge (4.4h)")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("<div style='background:white; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.05);'><h3>Patient Pathway Variations</h3>", unsafe_allow_html=True)
        variations = pd.DataFrame({"Count": [42.3, 18.7, 12.4, 9.8, 16.8]}, index=["Admission → Diagnostics → Treatment → Discharge", "Admission → Diagnostics → Re-admission", "Admission → Treatment → Diagnostics", "Admission → Treatment → Discharge", "Others"])
        st.bar_chart(variations, color="#2563EB")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div style='background:white; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.05);'><h3>Bottleneck Analysis</h3>", unsafe_allow_html=True)
        b_data = pd.DataFrame({
            "Process Step": ["Waiting for Diagnostics", "Consultation Scheduling", "Lab Results", "Treatment Approval"],
            "Avg. Wait Time": ["2.8 h", "1.6 h", "1.2 h", "0.9 h"],
            "Status": ["🔴 High", "🟠 Medium", "🟢 Low", "🟢 Low"]
        })
        st.dataframe(b_data, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("<div style='background:white; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.05);'><h3>Recommendations</h3>", unsafe_allow_html=True)
        st.success("1. Reduce diagnostic waiting time by 20%.")
        st.warning("2. Improve consultation scheduling.")
        st.markdown("</div>", unsafe_allow_html=True)