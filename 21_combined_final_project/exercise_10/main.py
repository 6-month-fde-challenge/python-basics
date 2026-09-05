"""
Exercise 10 - Expense Tracker
=============================
Lets the user record expenses repeatedly and analyse them.

    1. Add expense    2. View expenses    3. Calculate total
    4. Highest expense                    5. Exit

DATA STRUCTURE
A list of dictionaries, one per expense:

    expenses = [{"name": "Groceries", "amount": 2400.0}, ...]

FUNCTIONS
    add_expense()       - record a name and an amount, both validated
    view_expenses()     - print the list with each item's share of the total
    calculate_total()   - add every amount, without sum()
    highest_expense()   - the champion pattern, without max()
    lowest_expense()    - the same, in reverse
    main()              - the while loop driving the menu

WHY while FOR THE MENU
The user decides how many expenses to record - it could be two or twenty.
The application must stay open until they explicitly choose Exit, which is
a condition rather than a count.

ERROR HANDLING
    blank expense names, non-numeric amounts, and amounts of zero or less
    are all rejected without ending the session or corrupting the data.

SAMPLE INPUT / OUTPUT
    Add "Groceries" 2400, "Rent" 12000, "Fuel" 1800
    Total            : Rs.16200.00
    Highest expense  : Rent (Rs.12000.00) - 74.1% of all spending
    Average expense  : Rs.5400.00
"""

# Each expense is a dictionary; all of them live in this list
expenses = []


def show_menu():
    """Display the expense tracker menu."""
    print()
    print("=" * 48)
    print("              EXPENSE TRACKER")
    print("=" * 48)
    print(f"   Expenses recorded : {len(expenses)}")
    if len(expenses) > 0:
        print(f"   Running total     : Rs.{calculate_total():.2f}")
    print("   " + "-" * 42)
    print("   1. Add expense")
    print("   2. View expenses")
    print("   3. Calculate total")
    print("   4. Find highest expense")
    print("   5. Exit")
    print("=" * 48)


def add_expense():
    """Record one new expense after validating the name and the amount."""
    name = input("   Expense name : ").strip()

    if name == "":
        print("      ERROR: the expense name cannot be blank.")
        return

    entry = input("   Amount       : Rs.")

    try:
        amount = float(entry)
    except ValueError:
        print(f"      ERROR: '{entry}' is not a valid number.")
        return

    if amount <= 0:
        print(f"      ERROR: the amount must be greater than zero (you entered {amount}).")
        return

    expenses.append({"name": name, "amount": amount})

    print()
    print(f"   ADDED: {name} - Rs.{amount:.2f}")
    print(f"   You have now recorded {len(expenses)} expense(s), "
          f"totalling Rs.{calculate_total():.2f}")


def calculate_total():
    """Return the total of every expense, calculated without sum()."""
    total = 0.0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_average():
    """Return the average expense, or 0 if none have been recorded."""
    if len(expenses) == 0:
        return 0.0
    return calculate_total() / len(expenses)


def highest_expense():
    """
    Return the largest expense, without using max().

    Returns None when no expenses have been recorded.
    """
    if len(expenses) == 0:
        return None

    biggest = expenses[0]
    for expense in expenses:
        if expense["amount"] > biggest["amount"]:
            biggest = expense
    return biggest


def lowest_expense():
    """Return the smallest expense, or None if there are none."""
    if len(expenses) == 0:
        return None

    smallest = expenses[0]
    for expense in expenses:
        if expense["amount"] < smallest["amount"]:
            smallest = expense
    return smallest


def view_expenses():
    """Display every recorded expense with its share of the total."""
    print()
    print("   RECORDED EXPENSES")
    print("   " + "-" * 50)

    if len(expenses) == 0:
        print("   No expenses have been recorded yet.")
        print("   " + "-" * 50)
        return

    total = calculate_total()

    print(f"   {'#':<4}{'EXPENSE':<22}{'AMOUNT':>12}{'SHARE':>10}")
    print("   " + "-" * 50)

    for index, expense in enumerate(expenses, start=1):
        share = (expense["amount"] / total) * 100
        print(f"   {index:<4}{expense['name']:<22}"
              f"{expense['amount']:>12.2f}{share:>9.1f}%")

    print("   " + "-" * 50)
    print(f"   {'TOTAL':<26}{total:>12.2f}{'100.0%':>10}")


def show_total():
    """Display the total, average, highest and lowest expenses."""
    print()
    print("   EXPENSE SUMMARY")
    print("   " + "-" * 44)

    if len(expenses) == 0:
        print("   No expenses recorded, so the total is Rs.0.00")
        return

    biggest = highest_expense()
    smallest = lowest_expense()

    print(f"   {'Number of expenses':<24}: {len(expenses)}")
    print(f"   {'TOTAL SPENT':<24}: Rs.{calculate_total():.2f}")
    print(f"   {'Average expense':<24}: Rs.{calculate_average():.2f}")
    print(f"   {'Highest expense':<24}: Rs.{biggest['amount']:.2f} ({biggest['name']})")
    print(f"   {'Lowest expense':<24}: Rs.{smallest['amount']:.2f} ({smallest['name']})")
    print("   " + "-" * 44)


def show_highest():
    """Display the single largest expense in detail."""
    print()
    print("   HIGHEST EXPENSE")
    print("   " + "-" * 44)

    biggest = highest_expense()

    if biggest is None:
        print("   No expenses have been recorded yet.")
        return

    total = calculate_total()
    share = (biggest["amount"] / total) * 100

    print(f"   Name   : {biggest['name']}")
    print(f"   Amount : Rs.{biggest['amount']:.2f}")
    print(f"   Share  : {share:.1f}% of all spending (Rs.{total:.2f})")

    if share > 50:
        print()
        print("   This single expense is more than half of everything spent.")


def main():
    """Run the expense tracker until the user chooses Exit."""
    print("Expense Tracker starting...")

    # INITIALIZATION
    running = True

    # CONDITION : keep tracking until the user chooses Exit
    while running:
        show_menu()
        choice = input("   Choose an option (1-5) : ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            show_highest()
        elif choice == "5":
            # UPDATE / TERMINATION
            running = False
            print()
            print("=" * 48)
            print("              FINAL SUMMARY")
            print("=" * 48)
            if len(expenses) == 0:
                print("   No expenses were recorded this session.")
            else:
                print(f"   Expenses recorded : {len(expenses)}")
                print(f"   Total spent       : Rs.{calculate_total():.2f}")
                print(f"   Average expense   : Rs.{calculate_average():.2f}")
                print(f"   Highest expense   : {highest_expense()['name']}"
                      f" (Rs.{highest_expense()['amount']:.2f})")
            print("   Goodbye!")
            print("=" * 48)
        else:
            print()
            print(f"   INVALID OPTION: '{choice}'. Please choose 1 to 5.")


if __name__ == "__main__":
    main()
