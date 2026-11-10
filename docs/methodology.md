# CareFlow — Clinical Pathway Process Mining

## 1. Project Objective

CareFlow is a Data Analytics project that examines synthetic patient event logs to understand clinical activity sequences, patient journey duration, repeated activities, and workflow transitions.

The objective is to identify patterns in a simulated clinical pathway and present useful analytical insights through Python and Power BI.

## 2. Dataset Description

The project uses a synthetic dataset containing:

- **Total patient cases:** 100
- **Total event records:** 613

The dataset contains the following columns:

| Column | Description |
|---|---|
| `Case_ID` | Unique identifier for a patient journey |
| `Activity` | Clinical activity recorded |
| `Timestamp` | Date and time of the event |

The dataset is created for educational and analytical purposes. It does not contain real patient information.

## 3. Technologies Used

- **Python:** Data processing and analysis
- **Pandas:** Data manipulation and transformation
- **Matplotlib:** Visualization
- **NetworkX:** Process-flow visualization
- **Power BI:** Interactive dashboard and KPI presentation
- **Git and GitHub:** Version control and project management

## 4. Project Methodology

1. Load the patient event log into Python.
2. Inspect the dataset structure and required columns.
3. Validate missing values, invalid timestamps, and duplicate records.
4. Organize events by patient case and timestamp.
5. Calculate clinical activity frequencies.
6. Calculate individual patient journey durations.
7. Identify repeated activities within patient cases.
8. Analyze transitions between consecutive activities.
9. Generate a process map to visualize workflow patterns.
10. Present key findings through a Power BI dashboard.

## 5. Data Validation

The validation process checks:

- Required columns are available.
- Missing values are identified.
- Timestamps are valid.
- Duplicate event records are identified.

Initial validation results:

| Validation Check | Result |
|---|---:|
| Total event records | 613 |
| Unique patient cases | 100 |
| Missing values | 0 |
| Invalid timestamps | 0 |
| Duplicate event rows | 0 |

## 6. Initial Analytical Findings

| Metric | Result |
|---|---:|
| Total patient cases | 100 |
| Total event records | 613 |
| Average journey duration | 127.12 minutes |
| Longest journey | 194 minutes |
| Shortest journey | 69 minutes |
| Repeated Doctor activity records | 13 |

The analysis also identifies transitions between consecutive activities. For example, 13 cases contain a Laboratory-to-Doctor transition in the current dataset.

These are patterns in synthetic data, not evidence of actual clinical delays or problems.

## 7. Analysis Workflow

The Python scripts are organized by responsibility:

- `generate_data.py` — Generates synthetic patient event data.
- `validate_data.py` — Performs data-quality checks.
- `analyze_events.py` — Calculates activity summaries, journey durations, and repeated activities.
- `process_map.py` — Generates the clinical process-flow visualization.

The generated CSV files and process map are stored in the `outputs/` directory. The Power BI dashboard presents selected metrics and visualizations.

## 8. Limitations

- The dataset is synthetic and does not represent real hospital operations.
- Repeated activities require additional context before their significance can be interpreted.
- Time differences between events are not necessarily actual clinical waiting times.
- The findings must not be used for clinical decisions.

## 9. Future Enhancements

- Add more automated data-quality checks.
- Improve process-flow and patient journey analysis.
- Document Power BI KPI definitions.
- Add additional analytical tests.
- Improve dashboard explanations and presentation.

## 10. Project Status

The project currently includes synthetic event data, Python validation and analysis scripts, generated analytical outputs, a process map, and a Power BI dashboard.

Further testing, documentation, and dashboard refinement will support reproducibility and final evaluation.