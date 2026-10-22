# Student Management System

A simple command-line Student Management System written in Python. It stores student names, IDs, and grades during the program session and provides options to manage student records.

## Features

- Add a student with a name, ID, and grade
- View all recorded students
- Search for a student by name or ID
- Update a student's ID and grade
- Delete a student by name or ID
- Display a message when a student is not found
- Interactive menu for navigating the program

## Technologies Used

- Python
- Lists and tuples
- Functions
- `while` loops and `for` loops
- Conditional statements
- `enumerate()`
- User input and output

## Requirements

- Python 3

## How to Run

1. Save the Python script as `student_management.py`.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python student_management.py
   ```

   If your system uses `python3` to launch Python, run `python3 student_management.py` instead.

## Data Storage

Student records are kept in a Python list while the program is running. The records are not saved to a file or database, so they will be lost when the program exits.

## Future Improvements

- Save student records to a file or database
- Validate student IDs and grades
- Improve input validation and error handling
- Add sorting or grade statistics