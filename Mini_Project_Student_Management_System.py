"""
SkillNexis Python Programming Internship - Week 2 Mini Project
Project: Student Management System

Features:
- Store student data in a CSV file
- Add students
- Search students
- Delete students
- Display all students
- Permanently save changes to CSV
"""

import csv
from pathlib import Path


FILE_NAME = "students.csv"
FIELDNAMES = ["roll_number", "name", "marks"]


def initialize_file():
    """Create the CSV file with headers if it does not exist."""
    path = Path(FILE_NAME)

    if not path.exists():
        try:
            with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
        except OSError as error:
            print(f"Unable to create CSV file: {error}")


def load_students():
    """Load student records from the CSV file."""
    initialize_file()
    students = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    except OSError as error:
        print(f"Unable to read CSV file: {error}")

    return students


def save_students(students):
    """Save all student records permanently to the CSV file."""
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(students)

        return True

    except OSError as error:
        print(f"Unable to save students: {error}")
        return False


def add_student():
    """Add a new student to the CSV file."""
    students = load_students()

    roll_number = input("Enter roll number: ").strip()

    if not roll_number:
        print("Roll number cannot be empty.")
        return

    if any(student["roll_number"] == roll_number for student in students):
        print("A student with this roll number already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    marks = input("Enter marks: ").strip()

    try:
        marks_value = float(marks)

        if marks_value < 0 or marks_value > 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Marks must be a valid number.")
        return

    student = {
        "roll_number": roll_number,
        "name": name,
        "marks": f"{marks_value:g}"
    }

    students.append(student)

    if save_students(students):
        print("Student added and saved successfully.")


def search_student():
    """Search for a student using roll number."""
    students = load_students()
    roll_number = input("Enter roll number to search: ").strip()

    for student in students:
        if student["roll_number"] == roll_number:
            print("\n--- Student Found ---")
            print(f"Roll Number : {student['roll_number']}")
            print(f"Name        : {student['name']}")
            print(f"Marks       : {student['marks']}")
            return

    print("Student not found.")


def delete_student():
    """Delete a student using roll number."""
    students = load_students()
    roll_number = input("Enter roll number to delete: ").strip()

    updated_students = [
        student
        for student in students
        if student["roll_number"] != roll_number
    ]

    if len(updated_students) == len(students):
        print("Student not found.")
        return

    if save_students(updated_students):
        print("Student deleted and changes saved permanently.")


def display_students():
    """Display all students."""
    students = load_students()

    if not students:
        print("No student records available.")
        return

    print("\n" + "=" * 55)
    print("                 STUDENT RECORDS")
    print("=" * 55)
    print(f"{'Roll No.':<12}{'Name':<25}{'Marks':<10}")
    print("-" * 55)

    for student in students:
        print(
            f"{student['roll_number']:<12}"
            f"{student['name']:<25}"
            f"{student['marks']:<10}"
        )

    print("=" * 55)


def student_management_system():
    """Main menu for the Student Management System."""
    initialize_file()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Thank you for using Student Management System.")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    student_management_system()
