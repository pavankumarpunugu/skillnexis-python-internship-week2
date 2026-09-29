"""
SkillNexis Python Programming Internship - Week 2
Assignment 2: Word Counter from Text File

Features:
- Count words
- Count lines
- Count characters

The program creates a sample text file if the specified file does not exist.
"""

from pathlib import Path


def count_file_content(filename):
    path = Path(filename)

    if not path.exists():
        print(f"File '{filename}' not found.")
        return

    try:
        text = path.read_text(encoding="utf-8")

        lines = text.splitlines()
        words = text.split()
        characters = len(text)

        print("\n--- File Statistics ---")
        print(f"File       : {filename}")
        print(f"Words      : {len(words)}")
        print(f"Lines      : {len(lines)}")
        print(f"Characters : {characters}")

    except OSError as error:
        print(f"Unable to read file: {error}")


def create_sample_file(filename):
    sample_text = (
        "Python is a powerful programming language.\n"
        "File handling is useful for storing data permanently.\n"
        "This is a sample text file for the Word Counter assignment.\n"
    )

    try:
        Path(filename).write_text(sample_text, encoding="utf-8")
        print(f"Sample file '{filename}' created.")
    except OSError as error:
        print(f"Unable to create sample file: {error}")


def main():
    filename = input("Enter text file name: ").strip()

    if not filename:
        print("File name cannot be empty.")
        return

    if not Path(filename).exists():
        create_sample_file(filename)

    count_file_content(filename)


if __name__ == "__main__":
    main()
