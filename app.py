
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="CareFlow Analytics",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 CareFlow — Clinical Pathway Analytics")
st.caption("Patient Journey and Hospital Process Analysis")

# Load project dataset directly
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "patient_event_log.csv"

df = pd.read_csv(CSV_PATH)
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Calculate KPIs
total_patients = df["Case_ID"].nunique()
total_events = len(df)
total_activities = df["Activity"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Patients", total_patients)
col2.metric("Total Events", total_events)
col3.metric("Unique Activities", total_activities)

st.divider()

# Activity analysis
st.subheader("Patient Activity Analysis")

activity_summary = (
    df["Activity"]
    .value_counts()
    .reset_index()
)
activity_summary.columns = ["Activity", "Frequency"]

st.bar_chart(
    activity_summary.set_index("Activity")
)

# Patient journey explorer
st.divider()
st.subheader("Patient Journey Explorer")

patients = sorted(df["Case_ID"].unique())

selected_patient = st.selectbox(
    "Select Patient Case ID",
    patients
)

journey = df[df["Case_ID"] == selected_patient].sort_values("Timestamp")

st.dataframe(journey, use_container_width=True)

st.subheader("Activity Sequence")
st.write(" → ".join(journey["Activity"].tolist()))

st.success("CareFlow Analytics dashboard loaded successfully!")
