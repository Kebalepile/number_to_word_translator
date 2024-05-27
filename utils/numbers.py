"""Create a *.json file with numbers 1 to 1000"""
import json

def create_numbers_file():
    # Step 1: Generate the list of numbers from 1 to 1000
    numbers = list(range(1, 1001))

    # Step 2: Convert the list to JSON format
    numbers_json = json.dumps(numbers, indent=4)

    # Step 3: Save the JSON data to a file
    with open('numbers.json', 'w') as json_file:
        json_file.write(numbers_json)

    print("JSON file with numbers from 1 to 1000 has been created successfully.")
