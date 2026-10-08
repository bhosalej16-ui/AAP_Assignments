import csv
import json

csv_file = "input.csv"
json_file = "output.json"

with open(csv_file, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    records = []

    for row in reader:
        records.append(row)

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2)

print("Conversion completed successfully!")
print("JSON file saved as:", json_file)