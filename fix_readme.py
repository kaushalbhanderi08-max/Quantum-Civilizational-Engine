import json

with open("civilizational_mapping_report.json", "r") as f:
    data = json.load(f)

# સંપૂર્ણ અને અસલ README કન્ટેન્ટ
complete_readme = f"""# Quantum-Civilizational-Engine 🌌⚙️

Welcome to the **Quantum-Civilizational-Engine** repository! This project bridges physical quantum computing hardware with long-term civilizational modeling frameworks.

---

## 📊 Latest Execution Summary
- **Engine / Initiative:** {data.get("engine")}
- **IBM Quantum Backend:** `{data.get("backend")}`
- **Job ID:** `{data.get("job_id")}`
- **Total Shots Executed:** `{data.get("total_shots")}`

---

## 📈 Quantum State & Civilizational Mapping Report
Below are the top quantum states extracted from our 14-qubit circuit telemetry, mapped to our civilizational nodes along with their probability and entropy scores:

| Civilizational Node | 14-Qubit Bitstring (Sampled) | Count | Probability | Entropy Score |
| :--- | :--- | :--- | :--- | :--- |
"""

for node in data.get("top_civilizational_states", []):
    complete_readme += f"| **{node['node']}** | `{node['bitstring']}` | {node['count']} | {node['probability']} | {node['entropy_score']} |\n"

complete_readme += """
---

## 📉 Visualization: Quantum Probability Distribution
Here is the execution histogram representing the top frequency states captured from `ibm_kingston`:

![Quantum Histogram](quantum_histogram.png)

---
*Maintained by Enter The Futures Pvt Ltd.*
"""

# README.md માં સેવ કરીએ
with open("README.md", "w") as rm:
    rm.write(complete_readme)

print("Successfully fixed README.md with full content!")
