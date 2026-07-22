import json
import base64
import zlib
import numpy as np
import matplotlib.pyplot as plt

result_file = "job-d9flvokinv1c73arhv60-result.json"

try:
    with open(result_file, "r") as f:
        data = json.load(f)
    
    pub_results = data.get("__value__", {}).get("pub_results", [])
    if pub_results:
        bit_array_obj = pub_results[0]["__value__"]["data"]["__value__"]["fields"]["c"]["__value__"]
        num_bits = bit_array_obj.get("num_bits")
        encoded_str = bit_array_obj.get("array", {}).get("__value__")
        
        # ડીકોડિંગ
        decoded_data = zlib.decompress(base64.b64decode(encoded_str))
        arr = np.frombuffer(decoded_data, dtype=np.uint64)
        
        counts = {}
        for val in arr:
            b_str = format(val, f'0{num_bits}b')[::-1]
            counts[b_str] = counts.get(b_str, 0) + 1
            
        # 1. વિઝ્યુઅલાઈઝેશન ગ્રાફ સેવ કરીએ
        top_states = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]
        states = [x[0][:6] + "..." for x in top_states]  # ટૂંકી નજર માટે
        frequencies = [x[1] for x in top_states]
        
        plt.figure(figsize=(10, 5))
        plt.bar(states, frequencies, color='#1f77b4')
        plt.xlabel('Quantum States (14-Qubit Bitstrings)')
        plt.ylabel('Counts / Frequency')
        plt.title('IBM Quantum (ibm_kingston) Job: d9flvokinv1c73arhv60')
        plt.xticks(rotation=15)
        plt.tight_layout()
        plt.savefig('quantum_histogram.png')
        print("Successfully generated 'quantum_histogram.png'!")
        
        # 2. સિવિલાઈઝેશનલ એન્જિન ડેટા મેપિંગ રિપોર્ટ જનરેટ કરીએ
        civilizational_report = {
            "engine": "Quantum-Civilizational-Engine",
            "backend": "ibm_kingston",
            "job_id": "d9flvokinv1c73arhv60",
            "total_shots": sum(counts.values()),
            "top_civilizational_states": []
        }
        
        for idx, (st, cnt) in enumerate(top_states):
            prob = cnt / sum(counts.values())
            # સિવિલાઈઝેશનલ મેટ્રિક્સ મેપિંગ ફોર્મ્યુલા
            civilizational_index = f"Civ-Node-{idx+1}"
            civilizational_report["top_civilizational_states"].append({
                "node": civilizational_index,
                "bitstring": st,
                "count": cnt,
                "probability": round(prob, 4),
                "entropy_score": round(prob * np.log2(1/prob if prob > 0 else 1), 4)
            })
            
        with open("civilizational_mapping_report.json", "w") as rf:
            json.dump(civilizational_report, rf, indent=4)
        print("Successfully generated 'civilizational_mapping_report.json'!")

except Exception as e:
    print(f"Error: {e}")
