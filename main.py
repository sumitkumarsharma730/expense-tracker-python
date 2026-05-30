# 🧾 Mini Project – Expense Tracker

"""
    Question / Problem Statement: Create a console-based Expense Tracker
    program in Python that allows the user to record daily expenses and view
    summaries like total spending. Use only the concepts learned till Chapter 6
    (loops, conditionals, lists, dictionaries, and basic input/output).
"""


"""
    Project Details / Description:

    You are required to build a simple personal finance management tool.
    The program should allow the user to:
    ● Add an expense with details like date, category, description, and amount.
    ● View all recorded expenses in a clean format.
    ● Calculate total spending so far.
    ● Exit the program gracefully when the user chooses to.

    All tasks must be implemented using loops, if-else, lists, and dictionaries
    only. No user-defined functions or file handling should be used.
"""

"""
    Sample Output:
    Welcome to Expense Tracker 💸

    ======= MENU =======
    1️⃣Add Expense
    2️⃣View All Expenses
    3️⃣View Total Spending
    4️⃣Exit
    =====================

    Enter your choice (1-4): 1

    Enter date (DD-MM-YYYY): 05-11-2025
    Enter category (Food, Travel, Shopping, etc): Food
    Enter short description: Lunch
    Enter amount (₹): 150
    ✅ Expense added successfully!

    ======= MENU =======
    1️⃣Add Expense
    2️⃣View All Expenses
    3️⃣View Total Spending
    4️⃣Exit
    =====================

    Enter your choice (1-4): 3

    💰 Total Spending = ₹150
"""

# 🧾 Expense Tracker Project

# Display welcome message
print("Welcome to Expense Tracker 💸")

# Create an empty list to store all expenses
expenses = []

# Infinite loop to keep showing the menu
while True:

    # Display menu options
    print("\n======= MENU =======")
    print("1️⃣ Add Expense")
    print("2️⃣ View All Expenses")
    print("3️⃣ View Total Spending")
    print("4️⃣ Exit")
    print("=====================")

    # Take user's choice as input
    choice = input("\nEnter your choice (1-4): ")

    # ==========================================
    # OPTION 1 : ADD EXPENSE
    # ==========================================
    if choice == "1":

        # Take expense details from user
        date = input("\nEnter date (DD-MM-YYYY): ")
        category = input("Enter category (Food, Travel, Shopping, etc): ")
        description = input("Enter short description: ")
        amount = float(input("Enter amount (₹): "))

        # Store all details in a dictionary
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        # Add dictionary into expenses list
        expenses.append(expense)

        # Success message
        print("✅ Expense added successfully!")

    # ==========================================
    # OPTION 2 : VIEW ALL EXPENSES
    # ==========================================
    elif choice == "2":

        # Check if list is empty
        if len(expenses) == 0:
            print("\nNo expenses recorded yet.")

        else:
            print("\n📋 All Recorded Expenses:")

            # Loop through each expense
            for index, expense in enumerate(expenses, start=1):

                print(
                    f"{index}. "
                    f"Date: {expense['date']} | "
                    f"Category: {expense['category']} | "
                    f"Description: {expense['description']} | "
                    f"Amount: ₹{expense['amount']}"
                )

    # ==========================================
    # OPTION 3 : VIEW TOTAL SPENDING
    # ==========================================
    elif choice == "3":

        # Variable to store total amount
        total_spending = 0

        # Add all expense amounts
        for expense in expenses:
            total_spending += expense["amount"]

        # Display total spending
        print(f"\n💰 Total Spending = ₹{total_spending}")

    # ==========================================
    # OPTION 4 : EXIT PROGRAM
    # ==========================================
    elif choice == "4":

        print("\nThank you for using Expense Tracker. Goodbye! 👋")

        # Break loop and stop program
        break

    # ==========================================
    # INVALID CHOICE
    # ==========================================
    else:
        print("\n❌ Invalid choice. Please enter a number between 1 and 4.")