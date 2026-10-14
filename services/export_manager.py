import csv
import os

from services.seating_manager import SeatingManager
from storage import initialize_storage, load_seating, load_rooms


REPORTS_DIR = "reports"


class ExportManager:
    def __init__(self):
        initialize_storage()
        os.makedirs(REPORTS_DIR, exist_ok=True)
        self.seating_manager = SeatingManager()

    def _validate_seating_data(self, allocation):
        """Validate seating assignments before exporting."""

        if not isinstance(allocation, list):
            print("Error: Seating data must be a list.")
            return False

        required_fields = {
            "roll_no", "name", "branch",
            "room_no", "row", "seat"
        }

        for item in allocation:
            if not isinstance(item, dict):
                print("Error: Invalid seating assignment.")
                return False

            if not required_fields.issubset(item):
                print("Error: Seating assignment has missing fields.")
                return False

            for field in ("roll_no", "name", "branch", "room_no"):
                value = item[field]

                if not isinstance(value, str) or not value.strip():
                    print(f"Error: Invalid {field} in seating data.")
                    return False

            for field in ("row", "seat"):
                value = item[field]

                if type(value) is not int or value < 1:
                    print(f"Error: Invalid {field} number.")
                    return False

        if not allocation:
            return True

        if not self.seating_manager.validate_allocation(allocation):
            print("Error: Seating validation failed. Report not exported.")
            return False

        return True

    def export_seating_csv(self):
        """Export validated student seating assignments to CSV."""

        try:
            allocation = load_seating()

            if not allocation:
                print("No seating assignments available to export.")
                return False

            if not self._validate_seating_data(allocation):
                return False

            file_path = os.path.join(
                REPORTS_DIR, "seating_assignments.csv"
            )

            fieldnames = [
                "roll_no", "name", "branch",
                "room_no", "row", "seat"
            ]

            with open(
                file_path, "w", newline="", encoding="utf-8"
            ) as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(
                    {field: item[field] for field in fieldnames}
                    for item in allocation
                )

            print("Seating report exported successfully.")
            print("File location:", os.path.abspath(file_path))
            return True

        except (
            OSError, ValueError, KeyError,
            TypeError, AttributeError
        ) as error:
            print("Could not export seating report:", error)
            return False

    def export_room_summary_csv(self):
        """Export room occupancy information to CSV."""

        try:
            rooms = load_rooms()
            allocation = load_seating()

            if not isinstance(rooms, list):
                print("Error: Room data must be a list.")
                return False

            if not isinstance(allocation, list):
                print("Error: Seating data must be a list.")
                return False

            if not self._validate_seating_data(allocation):
                return False

           

            room_ids = set()

            for room in rooms:
                if not isinstance(room, dict):
                    print("Error: Invalid room record.")
                    return False

                if not {"room_no", "rows", "columns"}.issubset(room):
                    print("Error: Room record has missing fields.")
                    return False

                room_no = room["room_no"]

                if not isinstance(room_no, str) or not room_no.strip():
                    print("Error: Invalid room number.")
                    return False

                room_key = room_no.strip().casefold()

                if room_key in room_ids:
                    print("Error: Duplicate room number.")
                    return False

                room_ids.add(room_key)

                for field in ("rows", "columns"):
                    value = room[field]

                    if type(value) is not int or value < 1:
                        print(f"Error: Invalid room {field}.")
                        return False

            file_path = os.path.join(
                REPORTS_DIR, "room_occupancy.csv"
            )

            fieldnames = [
                "room_no", "rows", "columns",
                "capacity", "occupied_seats", "empty_seats"
            ]

            with open(
                file_path, "w", newline="", encoding="utf-8"
            ) as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for room in rooms:
                    room_no = room["room_no"].strip()
                    rows = room["rows"]
                    columns = room["columns"]
                    capacity = rows * columns

                    # Count actual assignments for this room.
                    occupied = sum(
                        1
                        for item in allocation
                        if item["room_no"].strip().casefold()
                        == room_no.casefold()
                    )

                    if occupied > capacity:
                        print(
                            f"Error: Room {room_no} has more "
                            "assignments than its capacity."
                        )
                        return False

                    writer.writerow({
                        "room_no": room_no,
                        "rows": rows,
                        "columns": columns,
                        "capacity": capacity,
                        "occupied_seats": occupied,
                        "empty_seats": capacity - occupied,
                    })

                  

            print("Room summary exported successfully.")
            print("File location:", os.path.abspath(file_path))
            return True

        except (
            OSError, ValueError, KeyError,
            TypeError, AttributeError
        ) as error:
            print("Could not export room summary:", error)
            return False

    def export_menu(self):
        """Display the report export menu."""

        while True:
            print("\n========== EXPORT REPORTS ==========")
            print("1. Export student seating assignments")
            print("2. Export room occupancy summary")
            print("3. Export both reports")
            print("4. Return to main menu")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                self.export_seating_csv()
            elif choice == "2":
                self.export_room_summary_csv()
            elif choice == "3":
                seating_success = self.export_seating_csv()
                room_success = self.export_room_summary_csv()

                if seating_success and room_success:
                    print("Both reports exported successfully.")
                else:
                    print("One or more reports could not be exported.")
            elif choice == "4":
                break
            else:
                print("Invalid choice. Enter 1-4.")


if __name__ == "__main__":
    manager = ExportManager()
    manager.export_menu()