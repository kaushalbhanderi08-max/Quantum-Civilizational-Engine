import json

# JSON રિપોર્ટ વાંચીએ
with open("civilizational_mapping_report.json", "r") as f:
    data = json.load(f)

# સાદી ભાષામાં Markdown કન્ટેન્ટ બનાવીએ
readme_content = f"""# Quantum-Civilizational-Engine 🌌⚙️

Welcome to the **Quantum-Civilizational-Engine** repository! This project bridges physical quantum computing hardware with long-term civilizational modeling frameworks.

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
    readme_content += f"| **{node['node']}** | `{node['bitstring']}` | {node['count']} | {node['probability']} | {node['entropy_score']} |\n"

readme_content += """
---

## 📉 Visualization: Quantum Probability Distribution
Here is the execution histogram representing the top frequency states captured from `ibm_kingston`:

![Quantum Histogram](quantum_histogram.png)

---
*Maintained by Enter The Futures Pvt Ltd.*
"""

# README.md માં લખી દઈએ
with open("README.md", "w") as rm:
    rm.write(readme_content)

print("Successfully updated README.md with clean civilizational report and graph!")
