import csv
import json
from collections import defaultdict

print("Initializing Day 2 Network Extraction Check...")

# 1. Read our Accused data and group cases by suspect name
suspect_case_map = defaultdict(list)

with open('Accused_Mock.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['AccusedName']
        case_id = row['CaseMasterID']
        suspect_case_map[name].append(case_id)

# 2. Filter out suspects who are repeat offenders (linked to more than 1 case)
repeat_offenders = {name: cases for name, cases in suspect_case_map.items() if len(cases) > 1}

# 3. Format this hidden network into our clean JSON Front-End Contract
contract_json = {
    "nodes": [],
    "edges": []
}

added_nodes = set()
edge_counter = 1

for name, cases in repeat_offenders.items():
    # Add the suspect node
    suspect_node_id = f"Accused_{name.replace(' ', '_')}"
    if suspect_node_id not in added_nodes:
        contract_json["nodes"].append({
            "id": suspect_node_id,
            "label": f"Suspect: {name}",
            "type": "Accused"
        })
        added_nodes.add(suspect_node_id)
        
    for case_id in cases:
        case_node_id = f"Case_{case_id}"
        # Add the case node
        if case_node_id not in added_nodes:
            contract_json["nodes"].append({
                "id": case_node_id,
                "label": f"FIR Case ID: {case_id}",
                "type": "Case"
            })
            added_nodes.add(case_node_id)
            
        # Add the edge connecting them
        contract_json["edges"].append({
            "id": f"e_{edge_counter}",
            "source": suspect_node_id,
            "target": case_node_id,
            "relationship": "Repeated Offender Link"
        })
        edge_counter += 1

# 4. Save the generated network layout to a JSON file
with open('extracted_network.json', 'w', encoding='utf-8') as json_file:
    json.dump(contract_json, json_file, indent=2)

print(f"Success! Detected {len(repeat_offenders)} repeat offender networks.")
print("Formatted structural network data saved to 'extracted_network.json'.")