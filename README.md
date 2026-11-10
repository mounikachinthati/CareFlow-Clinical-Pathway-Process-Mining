# CareFlow — Clinical Pathway Process Mining

## Project Overview

CareFlow is a **Data Analytics project** that uses process mining and data analysis techniques to understand patient journey workflows in a clinical environment.

The project analyzes patient event logs to identify activity frequency, patient journey duration, repeated clinical activities, and process transitions. The findings help demonstrate how healthcare workflows can be examined using data analytics.

**Note:** This project uses synthetic educational data and does not represent real hospital or patient records.

## Project Objectives

- Analyze patient event log data.
- Understand the sequence of clinical activities.
- Calculate patient journey duration.
- Identify repeated clinical activities.
- Analyze transitions between clinical activities.
- Visualize process patterns using Python and Power BI.
- Generate insights from the analyzed data.

## Technologies Used

- Python
- Pandas
- Matplotlib
- NetworkX
- Power BI
- Power Query
- CSV

## Project Structure

```text
CareFlow-Clinical-Pathway-Process-Mining/
│
├── data/
│   └── patient_event_log.csv
│
├── src/
│   ├── generate_data.py
│   ├── validate_data.py
│   ├── analyze_events.py
│   └── process_map.py
│
├── outputs/
│   ├── activity_summary.csv
│   ├── event_analysis.csv
│   ├── patient_journeys.csv
│   ├── repeated_activities.csv
│   └── process_map.png
│
├── dashboard/
│   └── CareFlow_Dashboard.pbix
│
├── docs/
│   └── methodology.md
│
├── requirements.txt
├── README.md
└── dummy.py
```

## Dataset Description

The project uses a synthetic patient event log containing **613 event records across 100 patient cases**.

| Column | Description |
|---|---|
| Case_ID | Unique patient case identifier |
| Activity | Clinical activity performed |
| Timestamp | Date and time of the activity |

### Clinical Activities

- Registration
- Triage
- Doctor
- Laboratory
- Treatment
- Discharge

## Methodology

The project follows these steps:

1. **Data Generation:** Generate synthetic patient event records.
2. **Data Validation:** Check missing values, duplicate records, and invalid timestamps.
3. **Data Cleaning:** Prepare the event log for analysis.
4. **Exploratory Data Analysis:** Examine activity frequencies and patient journeys.
5. **Process Mining:** Identify transitions between consecutive clinical activities.
6. **Visualization:** Create process maps and Power BI dashboard visualizations.
7. **Insight Generation:** Interpret workflow patterns and repeated activities.

## Data Validation Results

The validation script was executed successfully.

| Validation Check | Result |
|---|---:|
| Total event records | 613 |
| Unique patient cases | 100 |
| Missing values | 0 |
| Invalid timestamps | 0 |
| Duplicate event rows | 0 |

## Key Analytical Findings

| Metric | Result |
|---|---:|
| Total Patients | 100 |
| Total Event Records | 613 |
| Average Journey Duration | 127.12 minutes |
| Longest Journey | 194 minutes |
| Shortest Journey | 69 minutes |
| Repeated Activity Events | 13 |

### Activity Frequency

| Activity | Event Count |
|---|---:|
| Registration | 100 |
| Triage | 100 |
| Doctor | 113 |
| Laboratory | 100 |
| Treatment | 100 |
| Discharge | 100 |

### Process Transition Findings

The analysis identified the following transitions:

- Registration → Triage: 100
- Triage → Doctor: 100
- Doctor → Laboratory: 100
- Laboratory → Treatment: 87
- Laboratory → Doctor: 13
- Doctor → Treatment: 13
- Treatment → Discharge: 100

The repeated activity analysis identified 13 additional Doctor activity events.

**Interpretation:** These results describe patterns in the synthetic dataset. They should not be interpreted as real clinical waiting times or actual hospital performance.

## Power BI Dashboard

The Power BI dashboard presents key project findings through visualizations, including:

- Total Patients
- Total Event Records
- Average Journey Duration
- Clinical Activity Frequency
- Repeated Clinical Activities
- Patient Journey Duration by Case ID

The dashboard file is available at:

`dashboard/CareFlow_Dashboard.pbix`

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/mounikachinthati/CareFlow-Clinical-Pathway-Process-Mining.git
```

### 2. Open the Project Folder

```bash
cd CareFlow-Clinical-Pathway-Process-Mining
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Validate the Dataset

```bash
python src/validate_data.py
```

### 5. Run Data Analysis

```bash
python src/analyze_events.py
```

### 6. Generate the Process Map

```bash
python src/process_map.py
```

### 7. View the Dashboard

Open `dashboard/CareFlow_Dashboard.pbix` using Power BI Desktop.

## Project Limitations

- The dataset is synthetic and intended for educational purposes.
- The analysis is based on the available event log fields.
- The calculated journey duration represents elapsed time between the first and last recorded activities.
- The project does not connect to a live hospital information system.
- The findings should not be treated as real-world medical or operational conclusions.

## Future Enhancements

- Analyze larger and more diverse event logs.
- Add additional process performance metrics.
- Improve interactive Power BI dashboard filtering.
- Explore bottleneck and process deviation analysis.
- Extend the analysis with additional process mining techniques.

## Project Status

The project includes synthetic event data, data validation, Python-based analysis, process map generation, analytical output files, methodology documentation, and a Power BI dashboard.

**Project Domain:** Data Analytics | Healthcare Process Mining

**GitHub Repository:**  
https://github.com/mounikachinthati/CareFlow-Clinical-Pathway-Process-Mining