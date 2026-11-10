# 🏥 CareFlow — Clinical Pathway Process Mining

## 🌐 Live Dashboard
**[Open CareFlow Analytics Dashboard]https://careflow-clinical-pathway-process-minning.streamlit.app/
**

## 📌 Project Overview
CareFlow is a Data Analytics project that analyzes synthetic hospital patient journey data to identify process patterns, repeated activities, and patient journey duration.

## 🎯 Objectives
- Analyze patient clinical pathways.
- Identify repeated activities and process bottlenecks.
- Calculate patient journey duration.
- Visualize hospital operational insights.

## 🛠️ Technologies Used
- Python
- Pandas
- Matplotlib
- NetworkX
- Seaborn
- SQL / SQLite
- FastAPI
- Streamlit
- Power BI

## 📊 Dataset
- Total Patients: 100
- Total Events: 613
- Unique Activities: 6

Activities:
1. Registration
2. Triage
3. Doctor
4. Laboratory
5. Treatment
6. Discharge

*Note: The dataset contains synthetic educational data, not real patient records.*

## 🚀 Project Features
- Patient event data generation and validation.
- Process mining and patient journey analysis.
- Activity frequency analysis.
- Repeated activity identification.
- SQLite database integration.
- FastAPI endpoints for patient and analytics data.
- Interactive Streamlit dashboard.
- Power BI dashboard.

## 📁 Project Structure
```text
CareFlow/
├── app.py
├── careflow.db
├── data/
│   └── patient_event_log.csv
├── dashboard/
│   └── CareFlow_Dashboard.pbix
├── docs/
│   └── methodology.md
├── outputs/
│   ├── activity_summary.csv
│   ├── event_analysis.csv
│   ├── patient_journeys.csv
│   ├── process_map.png
│   └── repeated_activities.csv
├── src/
│   ├── api.py
│   ├── database.py
│   ├── analyze_events.py
│   ├── generate_data.py
│   ├── process_map.py
│   └── validate_data.py
└── requirements.txt
```

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize database:

```bash
python src/database.py
```

Start API:

```bash
python -m uvicorn src.api:app --reload
```

Start dashboard in another terminal:

```bash
streamlit run app.py
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## 👩‍💻 Developer
**Mounika Chinthati**

Data Analytics | Python | SQL | Power BI
