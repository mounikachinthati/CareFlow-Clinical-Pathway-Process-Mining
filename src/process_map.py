
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from pathlib import Path

# Project paths
ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = ROOT / "data" / "patient_event_log.csv"
OUTPUT_FILE = ROOT / "outputs" / "process_map.png"

# Load and sort the event log
df = pd.read_csv(INPUT_FILE, parse_dates=["Timestamp"])
df = df.sort_values(["Case_ID", "Timestamp"])

# Find each patient's next activity
df["Next_Activity"] = (
    df.groupby("Case_ID")["Activity"].shift(-1)
)

# Count transitions between activities
transitions = (
    df.dropna(subset=["Next_Activity"])
    .groupby(["Activity", "Next_Activity"])
    .size()
    .reset_index(name="Frequency")
)

# Create a directed process graph
G = nx.DiGraph()

for _, row in transitions.iterrows():
    G.add_edge(
        row["Activity"],
        row["Next_Activity"],
        weight=int(row["Frequency"])
    )

# Arrange activities in a readable layout
positions = {
    "Registration": (0, 1),
    "Triage": (1.5, 1),
    "Doctor": (3, 1),
    "Laboratory": (4.5, 1.7),
    "Treatment": (4.5, 0.3),
    "Discharge": (6, 1)
}

plt.figure(figsize=(13, 7))

nx.draw_networkx_nodes(
    G, positions,
    node_size=3200,
    node_color="lightblue",
    edgecolors="steelblue"
)

nx.draw_networkx_labels(
    G, positions,
    font_size=9,
    font_weight="bold"
)

# Thicker edges indicate more frequent transitions
edge_widths = [
    1 + G[u][v]["weight"] / 20
    for u, v in G.edges()
]

nx.draw_networkx_edges(
    G, positions,
    width=edge_widths,
    edge_color="gray",
    arrows=True,
    arrowsize=18,
    connectionstyle="arc3,rad=0.08",
    min_source_margin=22,
    min_target_margin=22
)

edge_labels = {
    (u, v): G[u][v]["weight"]
    for u, v in G.edges()
}

nx.draw_networkx_edge_labels(
    G, positions,
    edge_labels=edge_labels,
    font_size=8,
    label_pos=0.5
)

plt.title(
    "CareFlow: Patient Activity Process Map",
    fontsize=16,
    fontweight="bold"
)
plt.text(
    0.5, -0.08,
    "Edge labels = number of observed transitions",
    transform=plt.gca().transAxes,
    ha="center"
)

plt.axis("off")
plt.tight_layout()

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUTPUT_FILE, dpi=200, bbox_inches="tight")
plt.close()

print("Process map created successfully!")
print("Saved to:", OUTPUT_FILE)
print("\nMost frequent transitions:")
print(
    transitions.sort_values("Frequency", ascending=False)
    .head(10)
    .to_string(index=False)
)
