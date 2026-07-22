import json
import base64
import zlib
import numpy as np

result_file = "job-d9flvokinv1c73arhv60-result.json"

try:
    with open(result_file, "r") as f:
        data = json.load(f)
    
    pub_results = data.get("__value__", {}).get("pub_results", [])
    if pub_results:
        bit_array_obj = pub_results[0]["__value__"]["data"]["__value__"]["fields"]["c"]["__value__"]
        
        num_bits = bit_array_obj.get("num_bits")
        encoded_str = bit_array_obj.get("array", {}).get("__value__")
        
        # ડીકોડ અને ડીકોમ્પ્રెస్ કરો
        decoded_data = zlib.decompress(base64.b64decode(encoded_str))
        
        # બાઇટ્સને ન્યૂપાઇ એરેમાં રૂપાંતરિત કરો (uint64 અથવા uint32)
        # Qiskit BitArray સામાન્ય રીતે 64-bit integers તરીકે સ્ટોર કરે છે
        arr = np.frombuffer(decoded_data, dtype=np.uint64)
        
        print("=== Step 7: Final Counts & Probabilities ===")
        print(f"Total Number of Bits: {num_bits}")
        print(f"Total Shot Integers Read: {len(arr)}")
        
        # સેમ્પલ બિટસ્ટ્રિંગ્સ અને તેના કાઉન્ટ્સ ગણીએ
        counts = {}
        for val in arr:
            # ૧૪-બિટ ફોર્મેટમાં બાયનરી સ્ટ્રિંગ બનાવીએ
            b_str = format(val, f'0{num_bits}b')
            # રિવર્સ કરીએ કારણ કે Qiskit લિટલ-એન્ડિયન (Little-Endian) ફોર્મેટ વાપરે છે
            b_str_rev = b_str[::-1]
            counts[b_str_rev] = counts.get(b_str_rev, 0) + 1
            
        total_shots = sum(counts.values())
        print(f"Total Shots Computed: {total_shots}")
        print("\nTop 5 Quantum States (Bitstring : Count : Probability):")
        
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        for b_str, cnt in sorted_counts[:5]:
            prob = cnt / total_shots
            print(f"  {b_str} : {cnt} : {prob:.4f}")
            
    else:
        print("No pub results found.")

except Exception as e:
    print(f"Error computing final counts: {e}")
