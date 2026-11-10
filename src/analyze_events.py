
import pandas as pd
from pathlib import Path

# Locate project folders
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "patient_event_log.csv"
OUTPUT_FOLDER = PROJECT_ROOT / "outputs"


def analyze_events():

    print("========== CAREFLOW DATA ANALYSIS ==========")

    # Check dataset availability
    if not INPUT_FILE.exists():
        print("ERROR: Dataset not found:", INPUT_FILE)
        return

    try:
        df = pd.read_csv(INPUT_FILE)

        # Check required columns
        required_columns = ["Case_ID", "Activity", "Timestamp"]

        missing_columns = [
            col for col in required_columns if col not in df.columns
        ]

        if missing_columns:
            print("ERROR: Missing columns:", missing_columns)
            return

        if df.empty:
            print("ERROR: Dataset is empty.")
            return

        # Check missing and blank values
        df[required_columns] = df[required_columns].replace(
            r"^\s*$", pd.NA, regex=True
        )

        if df[required_columns].isnull().any().any():
            print("ERROR: Dataset contains missing values.")
            print(df[required_columns].isnull().sum())
            return

        # Convert timestamps
        df["Timestamp"] = pd.to_datetime(
            df["Timestamp"], errors="coerce"
        )

        if df["Timestamp"].isnull().any():
            print("ERROR: Invalid timestamps found.")
            return

        # Sort events chronologically
        df = df.sort_values(
            ["Case_ID", "Timestamp"]
        ).reset_index(drop=True)

        # Previous activity information
        df["Previous_Activity"] = (
            df.groupby("Case_ID")["Activity"].shift(1)
        )

        df["Previous_Timestamp"] = (
            df.groupby("Case_ID")["Timestamp"].shift(1)
        )

        df["Interval_Minutes"] = (
            df["Timestamp"] - df["Previous_Timestamp"]
        ).dt.total_seconds() / 60

        # Next activity information
        df["Next_Activity"] = (
            df.groupby("Case_ID")["Activity"].shift(-1)
        )

        df["Next_Timestamp"] = (
            df.groupby("Case_ID")["Timestamp"].shift(-1)
        )

        df["Next_Interval_Minutes"] = (
            df["Next_Timestamp"] - df["Timestamp"]
        ).dt.total_seconds() / 60

        # Calculate patient journey duration
        journeys = df.groupby("Case_ID").agg(
            Start_Time=("Timestamp", "min"),
            End_Time=("Timestamp", "max"),
            Total_Events=("Activity", "count")
        ).reset_index()

        journeys["Journey_Minutes"] = (
            journeys["End_Time"] - journeys["Start_Time"]
        ).dt.total_seconds() / 60

        # Activity frequency and average interval after activity
        activity_summary = df.groupby("Activity").agg(
            Event_Count=("Activity", "size"),
            Patients=("Case_ID", "nunique"),
            Average_Interval_After_Minutes=(
                "Next_Interval_Minutes", "mean"
            )
        ).reset_index()

        # Identify repeated activities
        df["Activity_Visit_Number"] = (
            df.groupby(["Case_ID", "Activity"]).cumcount() + 1
        )

        repeated = df[
            df["Activity_Visit_Number"] > 1
        ].copy()

        # Create output folder
        OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

        # Save analysis results
        df.to_csv(
            OUTPUT_FOLDER / "event_analysis.csv", index=False
        )

        journeys.to_csv(
            OUTPUT_FOLDER / "patient_journeys.csv", index=False
        )

        activity_summary.to_csv(
            OUTPUT_FOLDER / "activity_summary.csv", index=False
        )

        repeated.to_csv(
            OUTPUT_FOLDER / "repeated_activities.csv", index=False
        )

        # Display data overview
        print("\n========== DATA OVERVIEW ==========")
        print("Total event records:", len(df))
        print("Total patients:", df["Case_ID"].nunique())

        # Display journey summary
        print("\n========== PATIENT JOURNEY SUMMARY ==========")
        print(
            "Average journey duration (minutes):",
            round(journeys["Journey_Minutes"].mean(), 2)
        )
        print(
            "Longest journey (minutes):",
            round(journeys["Journey_Minutes"].max(), 2)
        )
        print(
            "Shortest journey (minutes):",
            round(journeys["Journey_Minutes"].min(), 2)
        )

        # Display activity summary
        print("\n========== ACTIVITY SUMMARY ==========")
        print(activity_summary.round(2).to_string(index=False))

        # Display repeated activities
        print("\n========== REPEATED ACTIVITIES ==========")
        print("Repeated activity events:", len(repeated))

        print(
            repeated[
                ["Case_ID", "Activity", "Timestamp"]
            ].head(10).to_string(index=False)
        )

        print("\nAnalysis completed successfully!")
        print("Results saved in:", OUTPUT_FOLDER)

    except (OSError, pd.errors.ParserError, pd.errors.EmptyDataError) as error:
        print("ERROR: Unable to process dataset:", error)


if __name__ == "__main__":
    analyze_events()
