
from services.seating_manager import SeatingManager

manager = SeatingManager()

print("\n===== SEATING ALGORITHM TEST =====")

# Test 1: Generate a seating plan using saved records.
success = manager.generate_seating()

if success:
    # Test 2: Verify every student has a unique assignment.
    roll_numbers = [
        item["roll_no"].casefold()
        for item in manager.allocation
    ]

    assert len(roll_numbers) == len(set(roll_numbers))

    # Test 3: Verify no seat is assigned twice.
    seats = [
        (
            item["room_no"].casefold(),
            item["row"],
            item["seat"]
        )
        for item in manager.allocation
    ]

    assert len(seats) == len(set(seats))

    # Test 4: Verify every seat is within its room's dimensions.
    assert manager.validate_allocation(manager.allocation)

    # Test 5: Load the saved allocation into a fresh manager.
    manager2 = SeatingManager()
    assert manager2.load_saved_allocation()

    assert len(manager2.allocation) == len(manager.allocation)

    print("\nAll seating tests passed.")

else:
    print(
        "\nAllocation was not generated. "
        "Check student records, room capacity, and saved files."
    )
