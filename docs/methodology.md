\# CareFlow — Clinical Pathway Process Mining



\## 1. Project Objective

The objective of CareFlow is to analyze patient event logs, understand the sequence of clinical activities, measure patient journey duration, and identify repeated activities in a simulated clinical workflow.



\## 2. Dataset

The project uses a synthetic patient event log containing 613 event records across 100 patient cases.



The main columns are:

\- `Case\_ID`: identifier for a patient journey.

\- `Activity`: clinical activity recorded in the journey.

\- `Timestamp`: date and time when the activity occurred.



\## 3. Tools Used

\- Python

\- Pandas for data processing and analysis

\- Matplotlib and NetworkX for process-map visualization

\- Power BI for dashboard development

\- Git and GitHub for version control



\## 4. Methodology

1\. Load the patient event log into Python.

2\. Inspect the dataset structure and check for missing values.

3\. Organize events by patient case and timestamp.

4\. Summarize the frequency of clinical activities.

5\. Calculate the duration of each patient journey.

6\. Identify repeated activities within patient journeys.

7\. Examine transitions between consecutive activities.

8\. Visualize the workflow using a process map.

9\. Present key metrics and activity patterns in a Power BI dashboard.



\## 5. Initial Findings

\- Total patient cases: 100.

\- Total event records: 613.

\- Average journey duration: approximately 127.12 minutes.

\- Repeated Doctor activity records: 13.



\## 6. Limitations

The dataset is synthetic and intended for educational analysis. The results do not represent actual hospital performance or establish clinical causes of delays. Repeated activities may require further investigation before drawing operational conclusions.



\## 7. Future Improvements

\- Add automated data-quality validation.

\- Improve process-flow and duration analysis.

\- Document dashboard KPI definitions.

\- Add reproducible instructions for running the analysis.



