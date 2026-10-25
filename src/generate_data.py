
import pandas as pd
import random
from pathlib import Path
from datetime import datetime, timedelta

random.seed(42)

# Activities in the hospital emergency department
activities = [
    "Registration",
    "Triage",
    "Doctor",
    "Laboratory",
    "Treatment",
    "Discharge"
]

rows = []
start_date = datetime(2026, 10, 1, 8, 0)

# Generate synthetic patient journeys
for patient_num in range(1, 101):
    case_id = f"P{patient_num:03d}"
    current_time = start_date + timedelta(
        minutes=random.randint(0, 480)
    )

    patient_activities = activities.copy()

    # Introduce occasional repeated activities
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

df = pd.DataFrame(rows)

# Sort events by patient and time
df = df.sort_values(
    ["Case_ID", "Timestamp"]
).reset_index(drop=True)

# Save CSV in the project's data folder
project_root = Path(__file__).resolve().parent.parent
output_file = project_root / "data" / "patient_event_log.csv"

output_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_file, index=False)

print("Patient event dataset created successfully!")
print("Total event records:", len(df))
print("Total patients:", df["Case_ID"].nunique())
print("Saved to:", output_file)
print("\nFirst 10 records:")
print(df.head(10).to_string(index=False))
