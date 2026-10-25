import pandas as pd
from pathlib import Path

DATA_FILE = Path("data/patient_event_log.csv")

def validate_event_log():
    if not DATA_FILE.exists():
        print(f"ERROR: File not found: {DATA_FILE}")
        return

    df = pd.read_csv(DATA_FILE)

    required_columns = ["Case_ID", "Activity", "Timestamp"]
    missing_columns = [
        col for col in required_columns if col not in df.columns
    ]

    if missing_columns:
        print("ERROR: Missing columns:", missing_columns)
        return

    print("Total event records:", len(df))
    print("Unique patient cases:", df["Case_ID"].nunique())
    print("Missing values:\n", df[required_columns].isnull().sum())

    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"], errors="coerce"
    )

    print("Invalid timestamps:", df["Timestamp"].isnull().sum())
    print("Duplicate event rows:", df.duplicated().sum())

    if df.empty:
        print("WARNING: The event log is empty.")
    else:
        print("Data validation completed.")

if __name__ == "__main__":
    validate_event_log()