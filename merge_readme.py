import json

# JSON રિપોર્ટ વાંચીએ
with open("civilizational_mapping_report.json", "r") as f:
    data = json.load(f)

# જૂની README વાંચીએ
try:
    with open("README.md", "r") as rm:
        old_readme = rm.read()
except FileNotFoundError:
    old_readme = "# Quantum-Civilizational-Engine"

# નવો સિવિલાઈઝેશનલ રિપોર્ટ સેક્શન બનાવીએ
new_section = f"""

---

## 🌌 Civilizational Mapping & Quantum Execution Report (Job: {data.get("job_id")})

- **Engine / Initiative:** {data.get("engine")}
- **IBM Quantum Backend:** `{data.get("backend")}`
- **Total Shots Executed:** `{data.get("total_shots")}`

### 📊 Top Quantum States & Mapping
| Civilizational Node | 14-Qubit Bitstring | Count | Probability | Entropy Score |
| :--- | :--- | :--- | :--- | :--- |
"""

for node in data.get("top_civilizational_states", []):
    new_section += f"| **{node['node']}** | `{node['bitstring']}` | {node['count']} | {node['probability']} | {node['entropy_score']} |\n"

new_section += """
### 📉 Visualization: Quantum Probability Distribution
![Quantum Histogram](quantum_histogram.png)
"""

# જો જૂની README માં આ સેક્શન પહેલેથી ન હોય તો જ ઉમેરીએ
if "Civilizational Mapping & Quantum Execution Report" not in old_readme:
    final_content = old_readme + new_section
else:
    final_content = old_readme  # જો પહેલેથી હોય તો એ જ રાખીએ

# README.md માં સેવ કરીએ
with open("README.md", "w") as rm:
    rm.write(final_content)

print("Successfully merged old README with new civilizational report!")
