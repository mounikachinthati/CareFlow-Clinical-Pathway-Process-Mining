# CareFlow — Clinical Pathway Process Mining

A data analytics project that examines patient event logs to understand clinical activity sequences, patient journey duration, repeated activities, and workflow patterns.

> **Data note:** This project uses synthetic data for educational analysis. It does not contain real patient records or measure actual hospital performance.

## Project Objectives

- Analyze the sequence of activities in patient journeys.
- Summarize the frequency of clinical activities.
- Calculate patient journey duration.
- Identify repeated activities within patient cases.
- Visualize workflow transitions using a process map.
- Present key metrics through a Power BI dashboard.

## Technologies Used

- **Python** — analysis and validation
- **Pandas** — data cleaning and transformation
- **Matplotlib and NetworkX** — process-map visualization
- **Power BI** — interactive dashboard development
- **Git and GitHub** — version control

## Project Structure

```text
CareFlow/
├── data/
│   └── patient_event_log.csv
├── src/
│   ├── generate_data.py
│   ├── analyze_events.py
│   ├── process_map.py
│   └── validate_data.py
├── outputs/
│   ├── activity_summary.csv
│   ├── event_analysis.csv
│   ├── patient_journeys.csv
│   ├── process_map.png
│   └── repeated_activities.csv
├── dashboard/
│   └── CareFlow_Dashboard.pbix
├── docs/
│   └── methodology.md
└── README.md
```

## Dataset

The synthetic event log contains the following fields:

| Column | Description |
|---|---|
| `Case_ID` | Identifier for a patient journey |
| `Activity` | Clinical activity recorded |
| `Timestamp` | Date and time of the event |

## Analysis Workflow

1. Load the event log.
2. Validate required columns, missing values, timestamps, and duplicate rows.
3. Summarize activity frequencies.
4. Calculate patient journey durations.
5. Identify repeated activities.
6. Analyze transitions between consecutive activities.
7. Generate a process map.
8. Explore results in the Power BI dashboard.

## Initial Results

| Metric | Result |
|---|---:|
| Patient cases | 100 |
| Event records | 613 |
| Average journey duration | 127.12 minutes |
| Missing values in required columns | 0 |
| Invalid timestamps | 0 |
| Duplicate event rows | 0 |
| Repeated Doctor activity records | 13 |

These results describe the current synthetic dataset. Repeated activities are patterns to investigate, not proof of a clinical problem or delay.

## How to Run

Run commands from the project root directory.

### 1. Install dependencies

```bash
pip install pandas matplotlib networkx
```

### 2. Validate the event log

```bash
python src/validate_data.py
```

### 3. Run the analysis

```bash
python src/analyze_events.py
```

### 4. Generate the process map

```bash
python src/process_map.py
```

Open `dashboard/CareFlow_Dashboard.pbix` using Microsoft Power BI Desktop to view the dashboard.

**Note:** Run `src/generate_data.py` only if you intend to regenerate the synthetic dataset.

## Limitations

- The dataset is synthetic and may not represent real clinical workflows.
- Repeated activities require context before their operational significance can be determined.
- The findings should not be used to make clinical decisions.

## Future Improvements

- Add more automated data-quality checks.
- Improve process-flow and duration analysis.
- Refine dashboard layout and KPI explanations.
- Add further tests and reproducible documentation.

## Project Status

The project includes synthetic event data, Python analysis scripts, output files, a process-map image, and a Power BI dashboard. Further validation and documentation can improve reproducibility and presentation.
