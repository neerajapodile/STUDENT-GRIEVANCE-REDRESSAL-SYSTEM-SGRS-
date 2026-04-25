import json
import csv

records = [
    {"ID": "101", "Name": "Lucky", "Issue": "Fees"},
    {"ID": "102", "Name": "Ravi", "Issue": "Exam"}
]

with open("grievance.json", "w") as f:
    json.dump(records, f)

with open("grievance.json", "r") as f:
    data = json.load(f)

print(data)

with open("grievance.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Issue"])

    for r in records:
        writer.writerow([r["ID"], r["Name"], r["Issue"]])

print("CSV File Created")
