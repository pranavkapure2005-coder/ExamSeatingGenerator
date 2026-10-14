
from utils import (
    get_non_empty_input,
    get_positive_integer,
    get_menu_choice,
    get_yes_no,
)
from services.export_manager import ExportManager
from services.student_manager import StudentManager
from services.room_manager import RoomManager
from services.seating_manager import SeatingManager
from services.report_manager import ReportManager


def display_menu():
    print("\n" + "=" * 45)
    print("   EXAM SEATING ARRANGEMENT GENERATOR")
    print("=" * 45)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Manage Exam Rooms")
    print("7. Generate Seating Arrangement")
    print("8. View Seating Report")
    print("9. Export Reports to CSV")
    print("10. Exit")
    print("=" * 45)


def room_menu(manager):
    while True:
        print("\n===== ROOM MANAGEMENT =====")
        print("1. Add Room")
        print("2. View Rooms")
        print("3. Search Room")
        print("4. Update Room")
        print("5. Delete Room")
        print("6. Return to Main Menu")

        choice = get_menu_choice(
          "Enter your choice (1-6): ",
          ["1", "2", "3", "4", "5", "6"]
        )

        if choice == "1":
            room_no = get_non_empty_input("Enter room number: ")
            rows = get_positive_integer("Enter number of rows: ")
            columns = get_positive_integer("Enter number of columns: ")
            manager.add_room(room_no, rows, columns)

        elif choice == "2":
            manager.view_rooms()

        elif choice == "3":
            room_no = get_non_empty_input(
                "Enter room number to search: "
            )
            manager.search_room(room_no)

        elif choice == "4":
            room_no = get_non_empty_input(
                "Enter room number to update: "
            )
            rows = get_positive_integer("Enter new number of rows: ")
            columns = get_positive_integer(
                "Enter new number of columns: "
            )
            manager.update_room(room_no, rows, columns)

        elif choice == "5":
            room_no = get_non_empty_input(
                "Enter room number to delete: "
            )

            if get_yes_no(f"Delete room {room_no}? (yes/no): "):
                manager.delete_room(room_no)
            else:
                print("Deletion cancelled.")

        elif choice == "6":
            break


def main():
    # Initialize all managers before displaying the menu.
    student_manager = StudentManager()
    room_manager = RoomManager()
    seating_manager = SeatingManager()
    report_manager = ReportManager()

    while True:
        display_menu()

        choice = get_menu_choice(
            "Enter your choice (1-10): ",
            ["1", "2", "3", "4", "5", "6", "7", "8", "9","10"],
        )

        if choice == "1":
            roll_no = get_non_empty_input("Enter roll number: ")
            name = get_non_empty_input("Enter student name: ")
            branch = get_non_empty_input("Enter branch: ")

            student_manager.add_student(roll_no, name, branch)

        elif choice == "2":
            student_manager.view_students()

        elif choice == "3":
            roll_no = get_non_empty_input(
                "Enter roll number to search: "
            )
            student_manager.search_student(roll_no)

        elif choice == "4":
            roll_no = get_non_empty_input(
                "Enter roll number to update: "
            )
            name = get_non_empty_input("Enter new name: ")
            branch = get_non_empty_input("Enter new branch: ")

            student_manager.update_student(
                roll_no, name, branch
            )

        elif choice == "5":
            roll_no = get_non_empty_input(
                "Enter roll number to delete: "
            )

            if get_yes_no(f"Delete student {roll_no}? (yes/no): "):
                student_manager.delete_student(roll_no)
            else:
                print("Deletion cancelled.")

        elif choice == "6":
            room_menu(room_manager)

        elif choice == "7":
            if get_yes_no(
                "Generate a new seating plan? (yes/no): "
            ):
                seating_manager.generate_seating()
            else:
                print("Allocation cancelled.")

        elif choice == "8":
            report_manager.reports_menu()

        elif choice == "9":
            export_manager.export_menu()

        elif choice == "10":
          print("Exiting application.")
        break

export_manager = ExportManager()
if __name__ == "__main__":
    main()
