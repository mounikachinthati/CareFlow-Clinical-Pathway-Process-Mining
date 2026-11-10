
import pandas as pd
import random
from pathlib import Path
from datetime import datetime, timedelta

# Ensure reproducible synthetic data
random.seed(42)

# Define clinical activities
activities = [
    "Registration",
    "Triage",
    "Doctor",
    "Laboratory",
    "Treatment",
    "Discharge"
]


def generate_patient_data():

    print("========== CAREFLOW DATA GENERATION ==========")

    rows = []
    start_date = datetime(2026, 10, 1, 8, 0)

    # Generate 100 synthetic patient journeys
    for patient_num in range(1, 101):

        case_id = f"P{patient_num:03d}"

        current_time = start_date + timedelta(
            minutes=random.randint(0, 480)
        )

        patient_activities = activities.copy()

        # Introduce occasional repeated Doctor visits
        if random.random() < 0.20:
            patient_activities.insert(4, "Doctor")

        for activity in patient_activities:

            rows.append({
                "Case_ID": case_id,
                "Activity": activity,
                "Timestamp": current_time
            })

            # Simulate time until the next activity
            current_time += timedelta(
                minutes=random.randint(5, 45)
            )

    # Create DataFrame
    df = pd.DataFrame(rows)

    # Sort patient events chronologically
    df = df.sort_values(
        ["Case_ID", "Timestamp"]
    ).reset_index(drop=True)

    # Validate generated data
    required_columns = ["Case_ID", "Activity", "Timestamp"]

    if df.empty or df[required_columns].isnull().any().any():
        print("ERROR: Generated dataset is invalid.")
        return

    # Save dataset
    project_root = Path(__file__).resolve().parent.parent

    output_file = (
        project_root / "data" / "patient_event_log.csv"
    )

    output_file.parent.mkdir(
        parents=True, exist_ok=True
    )

    df.to_csv(output_file, index=False)

    # Display generation summary
    print("Patient event dataset created successfully!")
    print("Total event records:", len(df))
    print("Total patients:", df["Case_ID"].nunique())
    print("Total clinical activities:", df["Activity"].nunique())
    print("Missing values:", df[required_columns].isnull().sum().sum())

    print("\nFirst 10 records:")
    print(df.head(10).to_string(index=False))

    print("\nDataset saved to:", output_file)


if __name__ == "__main__":
    generate_patient_data()
