
import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "careflow.db"

app = FastAPI(
    title="CareFlow API",
    description="Clinical Pathway Process Mining API",
    version="1.0"
)


def get_connection():
    return sqlite3.connect(DB_PATH)


@app.get("/")
def home():
    return {
        "message": "Welcome to CareFlow API",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/patients")
def get_patients():
    connection = get_connection()
    connection.row_factory = sqlite3.Row

    rows = connection.execute("""
        SELECT DISTINCT Case_ID
        FROM patient_events
        ORDER BY Case_ID
    """).fetchall()

    connection.close()

    return {
        "total_patients": len(rows),
        "patients": [row["Case_ID"] for row in rows]
    }


@app.get("/patients/{case_id}")
def get_patient(case_id: str):
    connection = get_connection()
    connection.row_factory = sqlite3.Row

    rows = connection.execute("""
        SELECT Case_ID, Activity, Timestamp
        FROM patient_events
        WHERE Case_ID = ?
        ORDER BY Timestamp
    """, (case_id,)).fetchall()

    connection.close()

    if not rows:
        raise HTTPException(status_code=404, detail="Patient not found")

    return [dict(row) for row in rows]


@app.get("/analytics")
def get_analytics():
    connection = get_connection()
    connection.row_factory = sqlite3.Row

    total_events = connection.execute(
        "SELECT COUNT(*) FROM patient_events"
    ).fetchone()[0]

    total_patients = connection.execute(
        "SELECT COUNT(DISTINCT Case_ID) FROM patient_events"
    ).fetchone()[0]

    activities = connection.execute("""
        SELECT Activity, COUNT(*) AS frequency
        FROM patient_events
        GROUP BY Activity
        ORDER BY frequency DESC
    """).fetchall()

    connection.close()

    return {
        "total_patients": total_patients,
        "total_events": total_events,
        "activity_summary": [dict(row) for row in activities]
    }

