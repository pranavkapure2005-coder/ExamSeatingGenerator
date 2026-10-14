
class Room:
    def __init__(self, room_no, rows, columns):
        if rows <= 0 or columns <= 0:
            raise ValueError("Rows and columns must be positive.")

        self.room_no = room_no
        self.rows = rows
        self.columns = columns

    def calculate_capacity(self):
        return self.rows * self.columns

    def display_details(self):
        print("Room Number:", self.room_no)
        print("Rows:", self.rows)
        print("Columns:", self.columns)
        print("Total Capacity:", self.calculate_capacity())

    def to_dict(self):
        return {
            "room_no": self.room_no,
            "rows": self.rows,
            "columns": self.columns
        }


if __name__ == "__main__":
    room1 = Room("A101", 5, 6)
    room2 = Room("A102", 4, 5)

    room1.display_details()
    print("-" * 25)
    room2.display_details()
