
from models.student import Student
from storage import (
    initialize_storage,
    save_students,
    load_students
)


class StudentManager:
    def __init__(self):
        initialize_storage()
        self.students = []
        self.load_data()

    def load_data(self):
        """Load CSV records and convert them into Student objects."""
        records = load_students()

        self.students = [
            Student(
                record["roll_no"],
                record["name"],
                record["branch"]
            )
            for record in records
        ]

    def find_student(self, roll_no):
        """Find a student using a case-insensitive roll number."""
        roll_no = roll_no.strip().casefold()

        for student in self.students:
            if student.roll_no.casefold() == roll_no:
                return student

        return None

    def add_student(self, roll_no, name, branch):
        """Create and persist a student record."""
        roll_no = roll_no.strip()
        name = name.strip()
        branch = branch.strip()

        if not roll_no or not name or not branch:
            print("Error: All fields are required.")
            return False

        if self.find_student(roll_no):
            print("Error: Roll number already exists.")
            return False

        student = Student(roll_no, name, branch)
        self.students.append(student)
        save_students(self.students)

        print("Student added successfully.")
        return True

    def view_students(self):
        """Display all registered students."""
        if not self.students:
            print("No students registered.")
            return

        print("\n" + "-" * 55)
        print(f"{'Roll Number':<15}{'Name':<25}{'Branch':<15}")
        print("-" * 55)

        for student in self.students:
            print(
                f"{student.roll_no:<15}"
                f"{student.name:<25}"
                f"{student.branch:<15}"
            )

        print("-" * 55)
        print("Total students:", len(self.students))

    def search_student(self, roll_no):
        """Search for a student by roll number."""
        student = self.find_student(roll_no)

        if student is None:
            print("Student not found.")
            return None

        student.display_details()
        return student

    def update_student(self, roll_no, new_name, new_branch):
        """Update a student's name and branch."""
        student = self.find_student(roll_no)

        if student is None:
            print("Error: Student not found.")
            return False

        new_name = new_name.strip()
        new_branch = new_branch.strip()

        if not new_name or not new_branch:
            print("Error: Name and branch cannot be empty.")
            return False

        student.name = new_name
        student.branch = new_branch

        save_students(self.students)

        print("Student updated successfully.")
        return True

    def delete_student(self, roll_no):
        """Delete a student and persist the change."""
        student = self.find_student(roll_no)

        if student is None:
            print("Error: Student not found.")
            return False

        self.students.remove(student)
        save_students(self.students)

        print("Student deleted successfully.")
        return True


if __name__ == "__main__":
    manager = StudentManager()

    print("\n===== STUDENT MANAGEMENT TEST =====")

    manager.add_student("TEST101", "Test Student", "AIDS")
    manager.view_students()

    manager.search_student("TEST101")

    manager.update_student(
        "TEST101",
        "Updated Student",
        "COMP"
    )
    manager.search_student("TEST101")

    manager.delete_student("TEST101")
    manager.search_student("TEST101")
