
import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "careflow.db"
CSV_PATH = BASE_DIR / "data" / "patient_event_log.csv"

def initialize_database():
    df = pd.read_csv(CSV_PATH)

    connection = sqlite3.connect(DB_PATH)

    df.to_sql(
        "patient_events",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()
    print("CareFlow database created successfully!")
    print(f"Records imported: {len(df)}")

if __name__ == "__main__":
    initialize_database()
