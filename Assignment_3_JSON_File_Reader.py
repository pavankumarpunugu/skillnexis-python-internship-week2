"""
SkillNexis Python Programming Internship - Week 2
Assignment 3: JSON File Reader

Features:
- Load JSON data from a file
- Print formatted JSON output
"""

import json
from pathlib import Path


def create_sample_json(filename):
    sample_data = {
        "students": [
            {
                "roll_number": 101,
                "name": "Pavan",
                "marks": 85
            },
            {
                "roll_number": 102,
                "name": "Rahul",
                "marks": 78
            }
        ]
    }

    try:
        Path(filename).write_text(
            json.dumps(sample_data, indent=4),
            encoding="utf-8"
        )
        print(f"Sample JSON file '{filename}' created.")
    except OSError as error:
        print(f"Unable to create file: {error}")


def read_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("\n--- Formatted JSON Output ---")
        print(json.dumps(data, indent=4))

    except FileNotFoundError:
        print("JSON file not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except OSError as error:
        print(f"Unable to read file: {error}")


def main():
    filename = input("Enter JSON file name: ").strip()

    if not filename:
        print("File name cannot be empty.")
        return

    if not Path(filename).exists():
        create_sample_json(filename)

    read_json_file(filename)


if __name__ == "__main__":
    main()
