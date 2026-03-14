import csv
import json

CSV_FILE = "data/students.csv"
JSON_FILE = "data/students.json"


def read_students():
    students = []
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print("CSV file not found")
    return students


def write_students(students):
    with open(CSV_FILE, "w", newline="") as file:
        fieldnames = ["id", "name", "age", "course"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)


def export_to_json(students):
    with open(JSON_FILE, "w") as file:
        json.dump(students, file, indent=4)

    print("Data exported to JSON successfully")
