
from storage import initialize_storage, load_rooms, load_students, load_seating
from services.seating_manager import SeatingManager

class ReportManager:
    def __init__(self):
        initialize_storage()

    def load_report_data(self):
        """Load the latest saved data whenever a report is requested."""
        self.rooms = load_rooms()
        self.students = load_students()
        self.allocation = load_seating()

    def room_wise_chart(self):
        self.load_report_data()

        if not self.rooms:
            print("\nNo rooms are registered.")
            return

        print("\n========== ROOM-WISE SEATING CHART ==========")

        for room in self.rooms:
            room_no = room["room_no"]
            rows = int(room["rows"])
            columns = int(room["columns"])

            # Map each occupied seat to its student's name and roll number.
            occupied = {}

            for item in self.allocation:
                if item["room_no"].casefold() == room_no.casefold():
                    key = (int(item["row"]), int(item["seat"]))
                    occupied[key] = (
                        f"{item['name']} ({item['roll_no']})"
                    )

            print(f"\nRoom: {room_no}")
            print("-" * 60)

            for row in range(1, rows + 1):
                seats = []

                for seat in range(1, columns + 1):
                    student = occupied.get((row, seat), "EMPTY")
                    seats.append(f"Seat {seat}: {student}")

                print(f"Row {row} | " + " | ".join(seats))

            print("-" * 60)

    def student_wise_report(self):
        self.load_report_data()

        roll_no = input("Enter student roll number: ").strip()

        student = None
        for record in self.students:
            if record["roll_no"].casefold() == roll_no.casefold():
                student = record
                break

        if student is None:
            print("Student not found in the student records.")
            return

        assignment = None
        for item in self.allocation:
            if item["roll_no"].casefold() == roll_no.casefold():
                assignment = item
                break

        print("\n========== STUDENT SEATING REPORT ==========")
        print("Roll Number:", student["roll_no"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])

        if assignment is None:
            print("Seating status: Not assigned")
        else:
            print("Room Number:", assignment["room_no"])
            print("Row Number:", assignment["row"])
            print("Seat Number:", assignment["seat"])

    def room_occupancy_report(self):
        self.load_report_data()

        print("\n========== ROOM OCCUPANCY REPORT ==========")

        if not self.rooms:
            print("No rooms are registered.")
            return

        for room in self.rooms:
            room_no = room["room_no"]
            capacity = int(room["rows"]) * int(room["columns"])

            occupied = sum(
                1 for item in self.allocation
                if item["room_no"].casefold() == room_no.casefold()
            )

            empty = capacity - occupied

            print(f"\nRoom: {room_no}")
            print("Total capacity:", capacity)
            print("Occupied seats:", occupied)
            print("Empty seats:", empty)

    def overall_summary(self):
        self.load_report_data()

        total_capacity = sum(
            int(room["rows"]) * int(room["columns"])
            for room in self.rooms
        )

        assigned_students = len(self.allocation)
        empty_seats = total_capacity - assigned_students

        print("\n========== OVERALL SEATING SUMMARY ==========")
        print("Registered students:", len(self.students))
        print("Students assigned seats:", assigned_students)
        print("Total rooms:", len(self.rooms))
        print("Total seating capacity:", total_capacity)
        print("Occupied seats:", assigned_students)
        print("Empty seats:", empty_seats)

    def reports_menu(self):
        while True:
            print("\n========== SEATING REPORTS ==========")
            print("1. Room-wise seating chart")
            print("2. Student-wise seating report")
            print("3. Room occupancy and empty seats")
            print("4. Overall seating summary")
            print("5. Back to main menu")

            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                self.room_wise_chart()
            elif choice == "2":
                self.student_wise_report()
            elif choice == "3":
                self.room_occupancy_report()
            elif choice == "4":
                self.overall_summary()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    manager = ReportManager()
    manager.reports_menu()
