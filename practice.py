
# A list stores multiple student records.
students = [
    {"roll_no": "101", "name": "Amit", "branch": "AIDS"},
    {"roll_no": "102", "name": "Priya", "branch": "COMP"},
    {"roll_no": "103", "name": "Rahul", "branch": "IT"}
]

# Display every student.
for student in students:
    print(student["roll_no"], student["name"], student["branch"])

# Search for a student by roll number.
search_roll = input("Enter roll number to search: ").strip()

found = False

for student in students:
    if student["roll_no"] == search_roll:
        print("Student found:", student)
        found = True
        break

if not found:
    print("Student not found.")
