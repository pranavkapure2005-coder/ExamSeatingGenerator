
from models.student import Student
from models.room import Room

from storage import (
    initialize_storage,
    save_students,
    load_students,
    save_rooms,
    load_rooms,
    save_seating,
    load_seating
)


initialize_storage()

# Create test objects.
students = [
    Student("101", "Amit", "AIDS"),
    Student("102", "Priya", "COMP")
]

rooms = [
    Room("A101", 5, 6),
    Room("A102", 4, 5)
]

# Save records.
save_students(students)
save_rooms(rooms)

# Load records.
print("Loaded students:")
for student in load_students():
    print(student)

print("\nLoaded rooms:")
for room in load_rooms():
    print(room)

# Save a sample seating allocation.
allocation = [
    {
        "roll_no": "101",
        "room_no": "A101",
        "row": 1,
        "seat": 1
    },
    {
        "roll_no": "102",
        "room_no": "A101",
        "row": 1,
        "seat": 2
    }
]

save_seating(allocation)

print("\nLoaded seating:")
print(load_seating())
