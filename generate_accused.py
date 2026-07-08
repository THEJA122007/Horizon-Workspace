import csv
import random
from faker import Faker

fake = Faker('en_IN')

print("Initializing Day 2: Relational Suspect Graph Generation...")

# 1. Create a pool of core "repeat offenders" to inject hidden criminal networks
core_criminals = [
    {"name": "Jagdish Shetty", "age": 34, "gender": 1},  # 1 = Male lookup
    {"name": "Anand Gowda", "age": 28, "gender": 1},
    {"name": "Syed Imran", "age": 41, "gender": 1},
    {"name": "Rupa Das", "age": 25, "gender": 2}         # 2 = Female lookup
]

# 2. Open a new CSV file to write our Accused table rows
with open('Accused_Mock.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the exact headers based on the official KSP Database Schema
    writer.writerow(['AccusedMasterID', 'CaseMasterID', 'AccusedName', 'AgeYear', 'GenderID', 'PersonID'])
    
    accused_id_counter = 1
    
    # 3. Read the 50 cases we created yesterday so we match the exact CaseMasterIDs
    for case_id in range(1, 51):
        
        # Decide how many suspects this specific case has (1 to 3)
        num_suspects_in_case = random.randint(1, 3)
        
        for position in range(1, num_suspects_in_case + 1):
            # Form an explicit logical connection: 
            # 30% chance a case involves one of our core repeat offenders (creating the graph network)
            if random.random() < 0.30:
                core_suspect = random.choice(core_criminals)
                name = core_suspect["name"]
                age = core_suspect["age"]
                gender = core_suspect["gender"]
            else:
                # 70% chance it's a completely new unique suspect
                name = fake.name()
                age = random.randint(18, 70)
                gender = random.choice([1, 2]) # Male or Female lookup values
            
            # Formats position identifier like A1, A2, A3 based on your ER design doc
            person_sort_id = f"A{position}" 
            
            # Write the row linking this suspect straight to the CaseMasterID
            writer.writerow([accused_id_counter, case_id, name, age, gender, person_sort_id])
            accused_id_counter += 1

print(f"Success! Generated {accused_id_counter - 1} accused records linked relationally inside 'Accused_Mock.csv'.")