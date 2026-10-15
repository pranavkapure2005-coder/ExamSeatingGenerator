<<<<<<< HEAD
# Exam Seating Arrangement Generator

A Python-based application that manages student records, exam rooms, seating allocation, and seating reports. It uses object-oriented programming and CSV/JSON files for data persistence.

## Features

- **Student Management:** Add, view, search, update, and delete student records.
- **Room Management:** Create, view, update, and delete exam rooms.
- **Automatic Seating Allocation:** Assign students to available seats.
- **Capacity Validation:** Check whether available rooms can accommodate registered students.
- **Seat Validation:** Prevent duplicate student assignments and duplicate seat allocation.
- **Data Persistence:** Store student, room, and seating data in CSV and JSON files.
- **Seating Reports:** View room-wise seating charts, student-wise assignments, and occupancy summaries.
- **CSV Export:** Export seating assignments and room occupancy reports.
- **Automated Testing:** Test core functionality, seating allocation, and report exports.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- CSV and JSON
- Python `unittest`
- File handling and exception handling

## Project Structure

```text
ExamSeatingGenerator/
├── main.py
├── utils.py
├── storage.py
├── models/
│   ├── student.py
│   └── room.py
├── services/
│   ├── student_manager.py
│   ├── room_manager.py
│   ├── seating_manager.py
│   ├── report_manager.py
│   └── export_manager.py
├── data/
│   ├── students.csv
│   ├── rooms.csv
│   └── seating.json
├── reports/
├── test_project.py
├── test_storage.py
├── test_room_manager.py
├── test_seating.py
├── test_export_manager.py
└── README.md
```

## Requirements

- Python 3.11 or compatible Python 3 version
- Windows, macOS, or Linux

No third-party packages are required if the project uses only Python's standard library.

## Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the environment on Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Start the application:

   ```bash
   python main.py
   ```

## How to Use

1. Launch the application.
2. Add student records with unique roll numbers.
3. Add exam rooms and define their row and column counts.
4. Generate the seating arrangement.
5. View seating charts and reports.
6. Export seating assignments or room occupancy summaries to CSV.

## Run Tests

Run the export tests:

```bash
python -m unittest test_export_manager -v
```

Run test discovery for the project:

```bash
python -m unittest discover -v
```

## Output Files

- `data/students.csv` — student records
- `data/rooms.csv` — exam room details
- `data/seating.json` — saved seating allocation
- `reports/seating_assignments.csv` — exported seating assignments
- `reports/room_occupancy.csv` — exported room occupancy summary

## Future Enhancements

- Graphical user interface or web dashboard
- PDF seating chart generation
- Student search by roll number
- Room-wise printable reports
- More comprehensive validation and automated tests
- Role-based access for administrators

## Disclaimer

This project is an educational software project intended to demonstrate Python programming, file handling, object-oriented design, validation, and automated testing.
=======
# ExamSeatingGenerator
>>>>>>> cfee54db86398b5b728f6a384825a99eb80234f2
