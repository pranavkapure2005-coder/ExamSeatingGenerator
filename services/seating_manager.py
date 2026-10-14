
from services.student_manager import StudentManager
from services.room_manager import RoomManager
from storage import save_seating, load_seating



class SeatingManager:
    def __init__(self):
        self.student_manager = StudentManager()
        self.room_manager = RoomManager()
        self.allocation = []

    def generate_seating(self):
        """Allocate students to unique seats and save the plan."""

        students = self.student_manager.students
        rooms = self.room_manager.rooms

        # Step 1: Validate available data.
        if not students:
            print("Error: No students registered.")
            return False

        if not rooms:
            print("Error: No rooms registered.")
            return False

        # Step 2: Calculate total capacity.
        total_capacity = sum(
            room.calculate_capacity()
            for room in rooms
        )

        student_count = len(students)

        print("\n===== CAPACITY CHECK =====")
        print("Total students:", student_count)
        print("Total seats:", total_capacity)

        # Step 3: Stop if capacity is insufficient.
        if student_count > total_capacity:
            print("Error: Insufficient seating capacity.")
            print("Additional seats needed:", student_count - total_capacity)
            return False

        # Step 4: Prepare allocation in memory.
        new_allocation = []
        student_index = 0

        # Step 5: Fill each room row by row.
        for room in rooms:
            for row in range(1, room.rows + 1):
                for seat in range(1, room.columns + 1):

                    # Stop when all students have been assigned.
                    if student_index >= student_count:
                        break

                    student = students[student_index]

                    assignment = {
                        "roll_no": student.roll_no,
                        "name": student.name,
                        "branch": student.branch,
                        "room_no": room.room_no,
                        "row": row,
                        "seat": seat
                    }

                    new_allocation.append(assignment)
                    student_index += 1

                if student_index >= student_count:
                    break

            if student_index >= student_count:
                break

        # Step 6: Verify the new allocation before saving.
        if not self.validate_allocation(new_allocation):
            print("Error: Allocation validation failed.")
            return False

        # Step 7: Save first; only update in-memory state on success.
        try:
            save_seating(new_allocation)
        except OSError as error:
            print("Error saving seating plan:", error)
            return False

        self.allocation = new_allocation

        print("\nSeating arrangement generated successfully.")
        print("Students assigned:", len(new_allocation))
        print("Unoccupied seats:", total_capacity - len(new_allocation))

        return True

    def validate_allocation(self, allocation):
        """Check student uniqueness, seat uniqueness, and room bounds."""

        valid_students = {
            student.roll_no.casefold()
            for student in self.student_manager.students
        }

        room_lookup = {
            room.room_no.casefold(): room
            for room in self.room_manager.rooms
        }

        assigned_students = set()
        occupied_seats = set()

        for item in allocation:
            roll_no = item["roll_no"].casefold()
            room_no = item["room_no"].casefold()
            row = item["row"]
            seat = item["seat"]

            # Each assigned student must be registered.
            if roll_no not in valid_students:
                return False

            # No student may be assigned twice.
            if roll_no in assigned_students:
                return False

            # Each assignment must refer to a registered room.
            if room_no not in room_lookup:
                return False

            room = room_lookup[room_no]

            # Check seat coordinates.
            if not (1 <= row <= room.rows):
                return False

            if not (1 <= seat <= room.columns):
                return False

            seat_key = (room_no, row, seat)

            # No two students can occupy the same seat.
            if seat_key in occupied_seats:
                return False

            assigned_students.add(roll_no)
            occupied_seats.add(seat_key)

        return True

    def load_saved_allocation(self):
        """Load and validate a previously saved seating plan."""

        try:
            allocation = load_seating()
        except (OSError, ValueError) as error:
            print("Could not load seating plan:", error)
            return False

        if not isinstance(allocation, list):
            print("Error: Seating file must contain a list.")
            return False

        if not self.validate_allocation(allocation):
            print("Error: Saved seating plan is invalid.")
            return False

        self.allocation = allocation
        print("Saved seating plan loaded successfully.")
        return True

    def view_allocation(self):
        """Display the current seating allocation."""

        if not self.allocation:
            print("No seating allocation loaded or generated.")
            return

        print("\n===== SEATING ALLOCATION =====")

        for item in self.allocation:
            print(
                f"Roll: {item['roll_no']} | "
                f"Name: {item['name']} | "
                f"Room: {item['room_no']} | "
                f"Row: {item['row']} | "
                f"Seat: {item['seat']}"
            )


if __name__ == "__main__":
    manager = SeatingManager()
    manager.generate_seating()
    manager.view_allocation()
