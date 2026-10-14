import csv
import os
import unittest
from unittest.mock import patch

from services.export_manager import ExportManager


class TestExportManager(unittest.TestCase):

    def setUp(self):
        self.test_dir = "test_reports"
        os.makedirs(self.test_dir, exist_ok=True)

        self.manager = ExportManager()

        self.seating_file = os.path.join(
            self.test_dir, "seating_assignments.csv"
        )
        self.room_file = os.path.join(
            self.test_dir, "room_occupancy.csv"
        )

    def tearDown(self):
        for path in (self.seating_file, self.room_file):
            if os.path.exists(path):
                os.remove(path)

        if os.path.isdir(self.test_dir):
            os.rmdir(self.test_dir)

    def test_seating_csv_headers_and_rows(self):
        sample_data = [
            {
                "roll_no": "101",
                "name": "Amit",
                "branch": "AIDS",
                "room_no": "R1",
                "row": 1,
                "seat": 1,
            },
            {
                "roll_no": "102",
                "name": "Neha",
                "branch": "AIDS",
                "room_no": "R1",
                "row": 1,
                "seat": 2,
            },
        ]

        with (
            patch(
                "services.export_manager.load_seating",
                return_value=sample_data,
            ),
            patch(
                "services.export_manager.REPORTS_DIR",
                self.test_dir,
            ),
            patch.object(
                self.manager.seating_manager,
                "validate_allocation",
                return_value=True,
            ),
            patch("builtins.print"),
        ):
            result = self.manager.export_seating_csv()

        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.seating_file))

        with open(
            self.seating_file, newline="", encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            headers = reader.fieldnames

        self.assertEqual(
            headers,
            ["roll_no", "name", "branch", "room_no", "row", "seat"],
        )
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["name"], "Amit")
        self.assertEqual(rows[1]["roll_no"], "102")

    def test_room_summary_csv(self):
        sample_rooms = [
            {"room_no": "R1", "rows": 2, "columns": 3}
        ]

        sample_allocation = [
            {
                "roll_no": "101",
                "name": "Amit",
                "branch": "AIDS",
                "room_no": "R1",
                "row": 1,
                "seat": 1,
            },
            {
                "roll_no": "102",
                "name": "Neha",
                "branch": "AIDS",
                "room_no": "R1",
                "row": 1,
                "seat": 2,
            },
        ]

        with (
            patch(
                "services.export_manager.load_rooms",
                return_value=sample_rooms,
            ),
            patch(
                "services.export_manager.load_seating",
                return_value=sample_allocation,
            ),
            patch(
                "services.export_manager.REPORTS_DIR",
                self.test_dir,
            ),
            patch.object(
                self.manager.seating_manager,
                "validate_allocation",
                return_value=True,
            ),
            patch("builtins.print"),
        ):
            result = self.manager.export_room_summary_csv()

        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.room_file))

        with open(
            self.room_file, newline="", encoding="utf-8"
        ) as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["room_no"], "R1")
        self.assertEqual(rows[0]["capacity"], "6")
        self.assertEqual(rows[0]["occupied_seats"], "2")
        self.assertEqual(rows[0]["empty_seats"], "4")

    def test_invalid_data_does_not_overwrite_existing_report(self):
        original_content = "existing report must remain unchanged"

        with open(
            self.seating_file, "w", encoding="utf-8"
        ) as file:
            file.write(original_content)

        invalid_data = [
            {"roll_no": "101", "room_no": "R1"}
        ]

        with (
            patch(
                "services.export_manager.load_seating",
                return_value=invalid_data,
            ),
            patch(
                "services.export_manager.REPORTS_DIR",
                self.test_dir,
            ),
            patch("builtins.print"),
        ):
            result = self.manager.export_seating_csv()

        self.assertFalse(result)

        with open(
            self.seating_file, "r", encoding="utf-8"
        ) as file:
            content = file.read()

        self.assertEqual(content, original_content)


if __name__ == "__main__":
    unittest.main(verbosity=2)