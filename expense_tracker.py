FILE_NAME = "expenses.txt"


def load_expenses():
    expenses = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|", 2)
                if len(parts) == 3:
                    try:
                        amount = float(parts[0])
                    except ValueError:
                        continue
                    expenses.append({
                        "amount": amount,
                        "category": parts[1],
                        "description": parts[2]
                    })
    except FileNotFoundError:
        pass
    return expenses


def save_expenses(expenses):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for expense in expenses:
            file.write(
                f"{expense['amount']}|{expense['category']}|"
                f"{expense['description']}\n"
            )


def add_expense(expenses):
    try:
        amount = float(input("Enter amount (₹): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    category = input("Enter category (Food, Travel, etc.): ").strip()
    description = input("Enter description: ").strip()
    if not category or not description:
        print("Category and description cannot be empty.")
        return

    # The | symbol separates fields in the text file.
    category = category.replace("|", "/").title()
    description = description.replace("|", "/")
    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n{:<10} {:<18} {}".format("Amount", "Category", "Description"))
    print("-" * 55)
    for expense in expenses:
        print("₹{:<9.2f} {:<18} {}".format(
            expense["amount"], expense["category"], expense["description"]
        ))


def show_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total expenses: ₹{total:.2f}")


def category_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return

    totals = {}
    for expense in expenses:
        category = expense["category"]
        if category in totals:
            totals[category] += expense["amount"]
        else:
            totals[category] = expense["amount"]

    print("\nExpense summary by category:")
    for category, amount in totals.items():
        print(f"{category}: ₹{amount:.2f}")


def search_expenses(expenses):
    search_category = input("Enter category to search: ").strip().lower()
    found = False
    for expense in expenses:
        if expense["category"].lower() == search_category:
            print(
                f"₹{expense['amount']:.2f} - "
                f"{expense['category']} - {expense['description']}"
            )
            found = True
    if not found:
        print("No expenses found in that category.")


def main():
    expenses = load_expenses()
    while True:
        print("\n====== PERSONAL EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Expenses")
        print("4. Category Summary")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            search_expenses(expenses)
        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1 to 6.")


main()
