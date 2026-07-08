import csv
import json
from collections import defaultdict

print(" Spatiotemporal Crime Hotspot Analyzer...")

# 1. Initialize a structure to group cases by their approximate location grid
hotspot_map = defaultdict(list)

with open('CaseMaster_Mock.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        case_id = row['CaseMasterID']
        lat = float(row['latitude'])
        lon = float(row['longitude'])
        date_str = row['CrimeRegistered_Date']
        
        # Round coordinates to group close incidents together (approx 1.1km grid)
        grid_lat = round(lat, 2)
        grid_lon = round(lon, 2)
        grid_key = (grid_lat, grid_lon)
        
        hotspot_map[grid_key].append({
            "case_id": case_id,
            "date": date_str,
            "coords": [lat, lon]
        })

# 2. Filter out grids that contain multiple incidents and sort by density
sorted_hotspots = sorted(
    [(grid, cases) for grid, cases in hotspot_map.items() if len(cases) > 1],
    key=lambda x: len(x[1]),
    reverse=True
)

# 3. Format into a clean payload structure for the Frontend Lead's map layer
map_contract_json = {
    "generated_at": "2026-07-08",
    "total_hotspots_detected": len(sorted_hotspots),
    "hotspots": []
}

for rank, (grid, cases) in enumerate(sorted_hotspots[:10], start=1):  # Increased to top 10 zones
    avg_lat = sum(c['coords'][0] for c in cases) / len(cases)
    avg_lon = sum(c['coords'][1] for c in cases) / len(cases)
    
    map_contract_json["hotspots"].append({
        "rank": rank,
        "cluster_center": [round(avg_lat, 6), round(avg_lon, 6)],
        "intensity_score": len(cases),
        "associated_case_ids": [c['case_id'] for c in cases]
    })

# 4. EXPORT FILE: Save the processed structural layer to disk as a JSON file
with open('hotspots_layer.json', 'w', encoding='utf-8') as json_file:
    json.dump(map_contract_json, json_file, indent=2)

print("\n--- Top Proactive Patrol Target Zones Exported Successfully ---")
print(f"Detected and tracked {len(sorted_hotspots)} unique coordinate clusters.")
print("Saved geo-coordinates contract file as: 'hotspots_layer.json'")