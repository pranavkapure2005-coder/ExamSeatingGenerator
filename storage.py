
import csv
import json
import os


DATA_DIR = "data"

STUDENTS_FILE = os.path.join(DATA_DIR, "students.csv")
ROOMS_FILE = os.path.join(DATA_DIR, "rooms.csv")
SEATING_FILE = os.path.join(DATA_DIR, "seating.json")


def initialize_storage():
    """Create the data folder and required files if missing."""
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["roll_no", "name", "branch"]
            )
            writer.writeheader()

    if not os.path.exists(ROOMS_FILE):
        with open(ROOMS_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["room_no", "rows", "columns"]
            )
            writer.writeheader()

    if not os.path.exists(SEATING_FILE):
        with open(SEATING_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def save_students(students):
    """Save a list of Student objects to CSV."""
    with open(STUDENTS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["roll_no", "name", "branch"]
        )
        writer.writeheader()

        for student in students:
            writer.writerow(student.to_dict())


def load_students():
    """Load student records from CSV."""
    with open(STUDENTS_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_rooms(rooms):
    """Save a list of Room objects to CSV."""
    with open(ROOMS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["room_no", "rows", "columns"]
        )
        writer.writeheader()

        for room in rooms:
            writer.writerow(room.to_dict())

def load_rooms():
    """Load room records from CSV and convert dimensions to integers."""
    with open(ROOMS_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rooms = []

        for row in reader:
            rooms.append({
                "room_no": row["room_no"].strip(),
                "rows": int(row["rows"]),
                "columns": int(row["columns"])
            })

        return rooms



def save_seating(allocation):
    """Save seating allocation data to JSON."""
    with open(SEATING_FILE, "w", encoding="utf-8") as file:
        json.dump(allocation, file, indent=4)


def load_seating():
    """Load seating allocation data from JSON."""
    with open(SEATING_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    initialize_storage()
    print("Storage initialized successfully.")

    print("Students:", load_students())
    print("Rooms:", load_rooms())
    print("Seating:", load_seating())

