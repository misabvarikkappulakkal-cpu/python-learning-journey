import csv
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "expenses.csv")


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])


def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("Invalid amount!")
        return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("✅ Expense added successfully!")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)

            print("\n{:<12} {:<10} {:<15} {}".format(
                "Date", "Amount", "Category", "Description"))
            print("-" * 60)

            for row in reader:
                print("{:<12} ₹{:<9} {:<15} {}".format(
                    row[0], row[1], row[2], row[3]))

    except FileNotFoundError:
        print("No expenses found.")


def total_expenses():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                total += float(row[1])

        print(f"\n💰 Total Expenses: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expenses found.")


def search_category():
    category = input("Enter category: ").strip()

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[2].lower() == category.lower():
                print(
                    f"{row[0]} | ₹{row[1]} | {row[2]} | {row[3]}")
                found = True

    if not found:
        print("No matching expenses found.")


def highest_expense():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)

            expenses = list(reader)

            if not expenses:
                print("No expenses available.")
                return

            highest = max(expenses, key=lambda x: float(x[1]))

            print("\n🏆 Highest Expense")
            print(f"Date       : {highest[0]}")
            print(f"Amount     : ₹{highest[1]}")
            print(f"Category   : {highest[2]}")
            print(f"Description: {highest[3]}")

    except FileNotFoundError:
        print("No expenses found.")


def category_report():
    report = {}

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                category = row[2]
                amount = float(row[1])

                report[category] = report.get(category, 0) + amount

        print("\n📊 Category Report")
        print("-" * 25)

        for category, total in report.items():
            print(f"{category:<15} ₹{total:.2f}")

    except FileNotFoundError:
        print("No expenses found.")


initialize_file()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Search Category")
    print("5. Highest Expense")
    print("6. Category Report")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        search_category()

    elif choice == "5":
        highest_expense()

    elif choice == "6":
        category_report()

    elif choice == "7":
        print("👋 Goodbye!")
        break

    else:
        print("Invalid choice.")