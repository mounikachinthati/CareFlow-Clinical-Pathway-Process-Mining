
import streamlit as st
import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="CareFlow Analytics",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 CareFlow — Clinical Pathway Analytics")
st.caption("Patient journey and hospital process analysis")

try:
    analytics = requests.get(
        f"{API_URL}/analytics",
        timeout=10
    )
    analytics.raise_for_status()
    data = analytics.json()

    patients_response = requests.get(
        f"{API_URL}/patients",
        timeout=10
    )
    patients_response.raise_for_status()
    patients = patients_response.json()["patients"]

except requests.RequestException:
    st.error("Cannot connect to CareFlow API. Start the FastAPI server first.")
    st.stop()

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Patients", data["total_patients"])
col2.metric("Total Events", data["total_events"])
col3.metric("Unique Activities", len(data["activity_summary"]))

st.divider()

# Activity Analysis
st.subheader("Patient Activity Analysis")

activity_df = pd.DataFrame(data["activity_summary"])

st.bar_chart(
    activity_df.set_index("Activity")["frequency"],
    color="#2196F3"
)

# Patient Search
st.divider()
st.subheader("Patient Journey Explorer")

selected_patient = st.selectbox(
    "Select Patient Case ID",
    patients
)

if selected_patient:
    response = requests.get(
        f"{API_URL}/patients/{selected_patient}",
        timeout=10
    )

    if response.status_code == 200:
        journey_df = pd.DataFrame(response.json())

        st.write(f"Journey details for {selected_patient}")
        st.dataframe(journey_df, use_container_width=True)

        st.write("Activity Sequence")
        st.write(" → ".join(journey_df["Activity"].tolist()))

st.success("CareFlow dashboard connected to the API.")
