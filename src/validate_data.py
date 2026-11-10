
import pandas as pd
from pathlib import Path

# Locate the project root and dataset
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_ROOT / "data" / "patient_event_log.csv"


def validate_event_log():

    print("========== DATA VALIDATION ==========")

    # Check whether the dataset exists
    if not DATA_FILE.exists():
        print(f"FAIL: Dataset not found: {DATA_FILE}")
        return False

    try:
        df = pd.read_csv(DATA_FILE)
    except (pd.errors.EmptyDataError, pd.errors.ParserError, OSError) as error:
        print("FAIL: Unable to read dataset:", error)
        return False

    # Check required columns
    required_columns = ["Case_ID", "Activity", "Timestamp"]

    missing_columns = [
        col for col in required_columns if col not in df.columns
    ]

    if missing_columns:
        print("FAIL: Missing required columns:", missing_columns)
        return False

    # Check for an empty dataset
    if df.empty:
        print("FAIL: The event log is empty.")
        return False

    # Treat blank strings as missing values
    df[required_columns] = df[required_columns].replace(
        r"^\s*$", pd.NA, regex=True
    )

    # Display dataset information
    print("Total event records:", len(df))
    print("Unique patient cases:", df["Case_ID"].nunique())

    # Check missing values
    missing_values = df[required_columns].isnull().sum()
    print("\nMissing values:\n", missing_values)

    # Check invalid timestamps
    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"], errors="coerce"
    )

    invalid_timestamps = df["Timestamp"].isnull().sum()
    print("\nInvalid timestamps:", invalid_timestamps)

    # Check duplicate event rows
    duplicate_rows = df.duplicated().sum()
    print("Duplicate event rows:", duplicate_rows)

    # Determine validation status
    has_missing_values = missing_values.sum() > 0

    if has_missing_values or invalid_timestamps > 0 or duplicate_rows > 0:
        print("\nVALIDATION RESULT: FAIL")
        return False

    print("\nVALIDATION RESULT: PASS")
    print("Data validation completed successfully.")

    return True


if __name__ == "__main__":
    validate_event_log()
