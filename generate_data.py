import csv
import random
from datetime import datetime, timedelta
from faker import Faker

# Initialize the Faker library for realistic random data generation
fake = Faker('en_IN')  # Uses Indian locales for names/addresses if needed

print("Initializing Day 1 KSP Data Simulation...")

# 1. Define how many mock cases we want to generate today
NUM_CASES = 500

# 2. Open a CSV file to write our simulated CaseMaster table
with open('CaseMaster_Mock.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the exact headers based on the official KSP Database Schema
    writer.writerow([
        'CaseMasterID', 'CrimeNo', 'CaseNo', 'CrimeRegistered_Date', 
        'latitude', 'longitude', 'BriefFacts'
    ])
    
    # 3. Loop to generate individual case records
    for i in range(1, NUM_CASES + 1):
        case_master_id = i
        
        # Simulate the structured KSP CrimeNo format (Category + Dist + PS + Year + Serial)
        year = "2026"
        crime_no = f"104430006{year}{str(i).zfill(5)}"
        case_no = f"{year}{str(i).zfill(5)}"
        
        # Generate random incident registration dates over the last year
        start_date = datetime(2025, 1, 1)
        random_days = random.randint(0, 500)
        crime_registered_date = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
        
        # Generate realistic GPS coordinates bound to the Karnataka region
        # Karnataka roughly spans Latitude: 11.5°N to 18.5°N, Longitude: 74.0°E to 78.5°E
        latitude = round(random.uniform(11.5, 18.5), 6)
        longitude = round(random.uniform(74.0, 78.5), 6)
        
        # Create a realistic short text description for the case summary
        crime_types = ["House burglary night-time", "Chain snatching near transit station", "Two-wheeler theft", "Commercial shop shoplifting"]
        chosen_crime = random.choice(crime_types)
        brief_facts = f"An incident of {chosen_crime} was reported. {fake.sentence(nb_words=10)}"
        
        # Write the row into our simulated table
        writer.writerow([
            case_master_id, crime_no, case_no, crime_registered_date, 
            latitude, longitude, brief_facts
        ])

print(f"Success! Generated {NUM_CASES} records inside 'CaseMaster_Mock.csv'.")