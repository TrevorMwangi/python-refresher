import csv
import json

def csv_to_json(csv_file, json_file):

    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]

    with open(json_file, mode='w') as file:
        json.dump(data, file, indent=4)

    print(f"CSV to JSON conversion completed!! {json_file}")

csv_to_json('Instagram.csv', 'data.json')