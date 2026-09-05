"""
Exercise 02 - Banking Application
=================================
A menu-driven bank account with a transaction history.

    1. Check balance   2. Deposit   3. Withdraw
    4. Transaction history          5. Exit

FUNCTIONS
    show_menu()          - display the options
    get_amount()         - ask for an amount and validate it
    check_balance()      - option 1
    deposit()            - option 2
    withdraw()           - option 3
    transaction_history()- option 4
    main()               - the while loop driving the menu

WHY while FOR THE MENU
Nobody knows how many transactions a customer will make. The application
must stay open until they explicitly choose Exit, which is a CONDITION,
not a count. `running = False` on option 5 is the only line that ends it.

ERROR HANDLING
    non-numeric amounts, amounts of zero or less, and withdrawals larger
    than the balance are all rejected without ending the session.

SAMPLE INPUT / OUTPUT
    Option 2, amount 2000  -> SUCCESS, balance Rs.7000.00
    Option 3, amount 99999 -> DECLINED: insufficient funds
    Option 4              -> lists both transactions with running balances
"""

# Account state, shared by the operation functions
balance = 5000.0
transactions = []


def show_menu():
    """Display the banking menu and the current balance."""
    print()
    print("=" * 46)
    print("            PYTHON BANK")
    print("=" * 46)
    print(f"   Balance : Rs.{balance:.2f}")
    print("   " + "-" * 40)
    print("   1. Check balance")
    print("   2. Deposit")
    print("   3. Withdraw")
    print("   4. Transaction history")
    print("   5. Exit")
    print("=" * 46)


def get_amount(action):
    """
    Ask for an amount and return it as a float.

    Returns None when the input is not a number or is not positive, so the
    caller can abandon the operation without changing the balance.
    """
    entry = input(f"   Enter amount to {action} : Rs.")

    try:
        amount = float(entry)
    except ValueError:
        print(f"      ERROR: '{entry}' is not a valid number.")
        return None

    if amount <= 0:
        print(f"      ERROR: the amount must be greater than zero (you entered {amount}).")
        return None

    return amount


def record(kind, amount):
    """Add one entry to the transaction history."""
    transactions.append({
        "type": kind,
        "amount": amount,
        "balance_after": balance,
    })


def check_balance():
    """Display the current account balance."""
    print()
    print(f"   Your available balance is Rs.{balance:.2f}")


def deposit():
    """Add money to the account after validating the amount."""
    global balance

    amount = get_amount("deposit")
    if amount is None:
        return

    balance += amount
    record("Deposit", amount)
    print()
    print(f"   SUCCESS: Rs.{amount:.2f} deposited.")
    print(f"   New balance: Rs.{balance:.2f}")


def withdraw():
    """Remove money from the account, never allowing an overdraft."""
    global balance

    amount = get_amount("withdraw")
    if amount is None:
        return

    if amount > balance:
        print()
        print("   DECLINED: insufficient funds.")
        print(f"   Requested Rs.{amount:.2f}, available Rs.{balance:.2f}")
        print(f"   Short by Rs.{amount - balance:.2f}")
        return

    balance -= amount
    record("Withdrawal", amount)
    print()
    print(f"   SUCCESS: Rs.{amount:.2f} withdrawn.")
    print(f"   Remaining balance: Rs.{balance:.2f}")


def transaction_history():
    """Display every transaction made during this session."""
    print()
    print("   TRANSACTION HISTORY")
    print("   " + "-" * 44)

    if len(transactions) == 0:
        print("   No transactions have been made this session.")
        print("   " + "-" * 44)
        return

    print(f"   {'#':<4}{'TYPE':<14}{'AMOUNT':>12}{'BALANCE':>14}")
    print("   " + "-" * 44)

    # for: the list length is known at this point
    for index, entry in enumerate(transactions, start=1):
        sign = "+" if entry["type"] == "Deposit" else "-"
        print(f"   {index:<4}{entry['type']:<14}"
              f"{sign + 'Rs.' + format(entry['amount'], '.2f'):>12}"
              f"{'Rs.' + format(entry['balance_after'], '.2f'):>14}")

    print("   " + "-" * 44)
    print(f"   {len(transactions)} transaction(s)")


def main():
    """Run the banking application menu until the user exits."""
    print("Welcome to Python Bank.")

    # INITIALIZATION : the flag that keeps the application open
    running = True

    # CONDITION : keep serving while the customer has not chosen Exit
    while running:
        show_menu()
        choice = input("   Choose an option (1-5) : ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            # UPDATE / TERMINATION : the only line that ends the application
            running = False
            print()
            print("=" * 46)
            print(f"   Final balance : Rs.{balance:.2f}")
            print(f"   Transactions  : {len(transactions)}")
            print("   Thank you for banking with us. Goodbye!")
            print("=" * 46)
        else:
            print()
            print(f"   INVALID OPTION: '{choice}'. Please choose 1 to 5.")


if __name__ == "__main__":
    main()
