
from services.room_manager import RoomManager

manager = RoomManager()

print("\n===== ROOM MANAGEMENT TEST =====")

# Use a unique test room number.
room_no = "TEST_ROOM_901"

# Clean up a previous test record if it exists.
if manager.find_room(room_no):
    manager.delete_room(room_no)

# Test adding a room.
assert manager.add_room(room_no, 5, 6) is True

# Test capacity calculation.
room = manager.find_room(room_no)
assert room.calculate_capacity() == 30

# Test duplicate prevention.
assert manager.add_room(room_no, 2, 2) is False

# Test invalid dimensions.
assert manager.add_room("TEST_INVALID_901", 0, 5) is False

# Test searching.
assert manager.search_room(room_no) is not None

# Test updating capacity.
assert manager.update_room(room_no, 4, 5) is True
assert manager.find_room(room_no).calculate_capacity() == 20

# Test persistence by loading a fresh manager.
manager2 = RoomManager()
assert manager2.find_room(room_no) is not None
assert manager2.find_room(room_no).calculate_capacity() == 20

# Remove the test record.
assert manager2.delete_room(room_no) is True

print("\nAll room management tests passed.")
