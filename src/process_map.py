
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from pathlib import Path

# Locate project folders
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "patient_event_log.csv"
OUTPUT_FOLDER = PROJECT_ROOT / "outputs"
OUTPUT_FILE = OUTPUT_FOLDER / "process_map.png"


def generate_process_map():

    print("========== CAREFLOW PROCESS MAP ==========")

    # Check dataset availability
    if not INPUT_FILE.exists():
        print("ERROR: Dataset not found:", INPUT_FILE)
        return

    try:
        df = pd.read_csv(INPUT_FILE)

        # Validate required columns
        required_columns = ["Case_ID", "Activity", "Timestamp"]

        if not all(col in df.columns for col in required_columns):
            print("ERROR: Required columns are missing.")
            return

        if df.empty or df[required_columns].isnull().any().any():
            print("ERROR: Dataset is empty or contains missing values.")
            return

        # Convert timestamps
        df["Timestamp"] = pd.to_datetime(
            df["Timestamp"], errors="coerce"
        )

        if df["Timestamp"].isnull().any():
            print("ERROR: Invalid timestamps found.")
            return

        # Sort activities for each patient
        df = df.sort_values(
            ["Case_ID", "Timestamp"]
        )

        # Identify consecutive activity transitions
        df["Next_Activity"] = (
            df.groupby("Case_ID")["Activity"].shift(-1)
        )

        transitions = df.dropna(
            subset=["Next_Activity"]
        )

        transition_counts = transitions.groupby(
            ["Activity", "Next_Activity"]
        ).size().reset_index(name="Frequency")

        # Create directed process graph
        G = nx.DiGraph()

        for _, row in transition_counts.iterrows():
            G.add_edge(
                row["Activity"],
                row["Next_Activity"],
                weight=int(row["Frequency"])
            )

        if G.number_of_edges() == 0:
            print("ERROR: No activity transitions found.")
            return

        # Generate process map
        OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

        plt.figure(figsize=(12, 8))

        pos = nx.spring_layout(
            G, seed=42, k=1.5
        )

        edge_labels = nx.get_edge_attributes(G, "weight")

        nx.draw_networkx_nodes(
            G, pos,
            node_size=3000,
            node_color="lightblue",
            edgecolors="black"
        )

        nx.draw_networkx_labels(
            G, pos,
            font_size=9,
            font_weight="bold"
        )

        nx.draw_networkx_edges(
            G, pos,
            arrows=True,
            arrowsize=20,
            width=2,
            edge_color="gray",
            connectionstyle="arc3,rad=0.08"
        )

        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=edge_labels,
            font_size=9
        )

        plt.title(
            "CareFlow - Clinical Process Map",
            fontsize=15,
            fontweight="bold"
        )

        plt.axis("off")
        plt.tight_layout()

        try:
            plt.savefig(
                str(OUTPUT_FILE),
                format="png",
                dpi=300,
                bbox_inches="tight"
            )
        finally:
            plt.close()

        # Display transition results
        print("\n========== ACTIVITY TRANSITIONS ==========")
        print(transition_counts.to_string(index=False))

        print("\nProcess map generated successfully!")
        print("Saved to:", OUTPUT_FILE)

    except (OSError, pd.errors.ParserError, pd.errors.EmptyDataError) as error:
        print("ERROR: Unable to generate process map:", error)


if __name__ == "__main__":
    generate_process_map()
