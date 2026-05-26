passwords = {}

while True:
    print("\n==== PASSWORD MANAGER ====")
    print("1. View Accounts")
    print("2. Add Account")
    print("3. Search Account")
    print("4. Delete Account")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # View Accounts
    if choice == "1":

        if len(passwords) == 0:
            print("No accounts saved.")

        else:
            print("\nSaved Accounts:")

            for account in passwords:
                print("-", account)

    # Add Account
    elif choice == "2":

        account = input("Enter account name: ")
        password = input("Enter password: ")

        passwords[account] = password

        print("Account saved successfully!")

    # Search Account
    elif choice == "3":

        account = input("Enter account name to search: ")

        if account in passwords:
            print("Password:", passwords[account])

        else:
            print("Account not found.")

    # Delete Account
    elif choice == "4":

        account = input("Enter account name to delete: ")

        if account in passwords:
            del passwords[account]
            print("Account deleted.")

        else:
            print("Account not found.")

    # Exit
    elif choice == "5":

        print("Exiting Password Manager...")
        break

    else:
        print("Invalid choice.")