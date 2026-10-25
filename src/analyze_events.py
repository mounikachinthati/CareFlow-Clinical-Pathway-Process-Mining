
import pandas as pd
from pathlib import Path

# Locate project folders
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "patient_event_log.csv"
OUTPUT_FOLDER = PROJECT_ROOT / "outputs"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Load event data
df = pd.read_csv(INPUT_FILE, parse_dates=["Timestamp"])

# Basic data checks
print("========== DATA OVERVIEW ==========")
print("Total event records:", len(df))
print("Total patients:", df["Case_ID"].nunique())
print("Missing values:\n", df.isnull().sum())

# Sort events chronologically for each patient
df = df.sort_values(
    ["Case_ID", "Timestamp"]
).reset_index(drop=True)

# Calculate time from the previous event for each patient
df["Previous_Activity"] = (
    df.groupby("Case_ID")["Activity"].shift(1)
)

df["Previous_Timestamp"] = (
    df.groupby("Case_ID")["Timestamp"].shift(1)
)

df["Interval_Minutes"] = (
    df["Timestamp"] - df["Previous_Timestamp"]
).dt.total_seconds() / 60

# Calculate total journey duration per patient
journeys = df.groupby("Case_ID").agg(
    Start_Time=("Timestamp", "min"),
    End_Time=("Timestamp", "max"),
    Total_Events=("Activity", "count")
).reset_index()

journeys["Journey_Minutes"] = (
    journeys["End_Time"] - journeys["Start_Time"]
).dt.total_seconds() / 60

# Activity frequency
activity_summary = df.groupby("Activity").agg(
    Event_Count=("Activity", "size"),
    Patients=("Case_ID", "nunique"),
    Average_Interval_After_Minutes=("Interval_Minutes", "mean")
).reset_index()

# Identify repeated activities within a patient journey
df["Activity_Visit_Number"] = (
    df.groupby(["Case_ID", "Activity"]).cumcount() + 1
)

repeated = df[df["Activity_Visit_Number"] > 1].copy()

# Save analysis results
df.to_csv(OUTPUT_FOLDER / "event_analysis.csv", index=False)
journeys.to_csv(OUTPUT_FOLDER / "patient_journeys.csv", index=False)
activity_summary.to_csv(
    OUTPUT_FOLDER / "activity_summary.csv", index=False
)
repeated.to_csv(OUTPUT_FOLDER / "repeated_activities.csv", index=False)

# Display key findings
print("\n========== PATIENT JOURNEY SUMMARY ==========")
print("Average journey duration (minutes):",
      round(journeys["Journey_Minutes"].mean(), 2))
print("Longest journey (minutes):",
      round(journeys["Journey_Minutes"].max(), 2))
print("Shortest journey (minutes):",
      round(journeys["Journey_Minutes"].min(), 2))

print("\n========== ACTIVITY SUMMARY ==========")
print(activity_summary.round(2).to_string(index=False))

print("\n========== REPEATED ACTIVITIES ==========")
print("Repeated activity events:", len(repeated))
print(repeated[["Case_ID", "Activity", "Timestamp"]]
      .head(10).to_string(index=False))

print("\nAnalysis complete! Results saved in:", OUTPUT_FOLDER)
