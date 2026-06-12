import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "students.csv")


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll No", "Name", "Age", "Course"])


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, age, course])

    print("Student added successfully!")


def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def search_student():
    roll = input("Enter Roll Number to Search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            if row[0] == roll:
                print("\nStudent Found:")
                print(f"Roll No: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Age: {row[2]}")
                print(f"Course: {row[3]}")
                return

    print("Student not found.")


def update_student():
    roll = input("Enter Roll Number to Update: ")

    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    updated = False

    for row in rows[1:]:
        if row[0] == roll:
            row[1] = input("New Name: ")
            row[2] = input("New Age: ")
            row[3] = input("New Course: ")
            updated = True

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if updated:
        print("Student updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    new_rows = [rows[0]]

    deleted = False

    for row in rows[1:]:
        if row[0] != roll:
            new_rows.append(row)
        else:
            deleted = True

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)

    if deleted:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def main():
    initialize_file()

    while True:
        print("\n===== STUDENT DATABASE SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()