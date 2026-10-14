
from models.room import Room
from storage import (
    initialize_storage,
    save_rooms,
    load_rooms
)


class RoomManager:
    def __init__(self):
        initialize_storage()
        self.rooms = []
        self.load_data()

    def load_data(self):
        """Load CSV records and convert them into Room objects."""
        records = load_rooms()

        self.rooms = [
            Room(
                record["room_no"],
                int(record["rows"]),
                int(record["columns"])
            )
            for record in records
        ]

    def find_room(self, room_no):
        """Find a room using a case-insensitive room number."""
        room_no = room_no.strip().casefold()

        for room in self.rooms:
            if room.room_no.casefold() == room_no:
                return room

        return None

    def add_room(self, room_no, rows, columns):
        """Add a room after validating its details."""
        room_no = room_no.strip()

        if not room_no:
            print("Error: Room number is required.")
            return False

        if self.find_room(room_no):
            print("Error: Room number already exists.")
            return False

        try:
            rows = int(rows)
            columns = int(columns)
        except (ValueError, TypeError):
            print("Error: Rows and columns must be integers.")
            return False

        if rows <= 0 or columns <= 0:
            print("Error: Rows and columns must be positive.")
            return False

        room = Room(room_no, rows, columns)
        self.rooms.append(room)
        save_rooms(self.rooms)

        print("Room added successfully.")
        print("Total capacity:", room.calculate_capacity())
        return True

    def view_rooms(self):
        """Display all registered rooms."""
        if not self.rooms:
            print("No rooms registered.")
            return

        print("\n" + "-" * 65)
        print(
            f"{'Room Number':<15}"
            f"{'Rows':<10}"
            f"{'Columns':<10}"
            f"{'Capacity':<12}"
        )
        print("-" * 65)

        total_capacity = 0

        for room in self.rooms:
            capacity = room.calculate_capacity()
            total_capacity += capacity

            print(
                f"{room.room_no:<15}"
                f"{room.rows:<10}"
                f"{room.columns:<10}"
                f"{capacity:<12}"
            )

        print("-" * 65)
        print("Total rooms:", len(self.rooms))
        print("Total seating capacity:", total_capacity)

    def search_room(self, room_no):
        """Search for a room by room number."""
        room = self.find_room(room_no)

        if room is None:
            print("Room not found.")
            return None

        room.display_details()
        return room

    def update_room(self, room_no, new_rows, new_columns):
        """Update the dimensions of an existing room."""
        room = self.find_room(room_no)

        if room is None:
            print("Error: Room not found.")
            return False

        try:
            new_rows = int(new_rows)
            new_columns = int(new_columns)
        except (ValueError, TypeError):
            print("Error: Rows and columns must be integers.")
            return False

        if new_rows <= 0 or new_columns <= 0:
            print("Error: Rows and columns must be positive.")
            return False

        room.rows = new_rows
        room.columns = new_columns

        save_rooms(self.rooms)

        print("Room updated successfully.")
        print("New capacity:", room.calculate_capacity())
        return True

    def delete_room(self, room_no):
        """Delete a room and persist the change."""
        room = self.find_room(room_no)

        if room is None:
            print("Error: Room not found.")
            return False

        self.rooms.remove(room)
        save_rooms(self.rooms)

        print("Room deleted successfully.")
        return True


if __name__ == "__main__":
    manager = RoomManager()
    manager.view_rooms()
