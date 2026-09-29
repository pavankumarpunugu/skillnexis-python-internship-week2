"""
SkillNexis Python Programming Internship - Week 2
Assignment 1: Contact Book using Dictionary

Features:
- Add contact
- Search contact
- Update contact
- Delete contact
"""

def add_contact(contacts):
    name = input("Enter contact name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully.")


def search_contact(contacts):
    name = input("Enter contact name to search: ").strip()

    if name in contacts:
        contact = contacts[name]
        print("\nContact Found")
        print(f"Name  : {name}")
        print(f"Phone : {contact['phone']}")
        print(f"Email : {contact['email']}")
    else:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter contact name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact updated successfully.")


def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def display_contacts(contacts):
    if not contacts:
        print("Contact book is empty.")
        return

    print("\n--- All Contacts ---")
    for name, details in contacts.items():
        print(f"Name: {name} | Phone: {details['phone']} | Email: {details['email']}")


def main():
    contacts = {}

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            display_contacts(contacts)
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
