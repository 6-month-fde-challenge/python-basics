"""
Question 12 - ATM Simulation
============================
A menu-driven ATM the user can operate repeatedly until they choose to exit.

    1. Check balance
    2. Deposit money
    3. Withdraw money
    4. Exit

STRUCTURE (organised into functions rather than one long block)
----------------------------------------------------------------
Each job is a separate function, so each can be read and tested alone:

    show_menu()          -> displays the options
    get_amount()         -> asks for an amount and validates it
    check_balance()      -> option 1
    deposit()            -> option 2
    withdraw()           -> option 3
    main()               -> the while loop that ties it all together

THE LOOP: a `while True` keeps the menu coming back after every action.
It ends only when the user chooses 4, which triggers `break`.

VALIDATION RULES ENFORCED BELOW
    - the amount must be a number
    - the amount must be greater than zero
    - a withdrawal cannot exceed the available balance
"""

# ---------------------------------------------------------------------------
# Account state
# ---------------------------------------------------------------------------

balance = 5000.0                  # the account starts with this much
transaction_history = []          # every successful action is recorded here


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def show_menu():
    """Display the ATM menu."""
    print()
    print("=" * 40)
    print("           ATM MAIN MENU")
    print("=" * 40)
    print("   1. Check balance")
    print("   2. Deposit money")
    print("   3. Withdraw money")
    print("   4. Exit")
    print("=" * 40)


def get_amount(action):
    """
    Ask the user for an amount and validate it.
    Returns the amount as a float, or None if the input was invalid.
    """
    entry = input(f"Enter amount to {action} : Rs.")

    # Rule 1 - it must actually be a number
    try:
        amount = float(entry)
    except ValueError:
        print(f"   INVALID: '{entry}' is not a number.")
        return None

    # Rule 2 - it must be positive
    if amount <= 0:
        print(f"   INVALID: amount must be greater than zero (you entered {amount}).")
        return None

    return amount


def check_balance():
    """Option 1 - show the current balance."""
    print()
    print(f"   Your current balance is Rs.{balance:.2f}")


def deposit():
    """Option 2 - add money to the account."""
    global balance

    amount = get_amount("deposit")
    if amount is None:
        return                                  # invalid input, nothing changes

    balance += amount
    transaction_history.append(f"Deposit    +Rs.{amount:.2f}")
    print()
    print(f"   SUCCESS: Rs.{amount:.2f} deposited.")
    print(f"   New balance: Rs.{balance:.2f}")


def withdraw():
    """Option 3 - take money out, but never more than the balance."""
    global balance

    amount = get_amount("withdraw")
    if amount is None:
        return                                  # invalid input, nothing changes

    # Rule 3 - you cannot withdraw more than you have
    if amount > balance:
        print()
        print(f"   DECLINED: insufficient funds.")
        print(f"   You asked for Rs.{amount:.2f} but only have Rs.{balance:.2f}.")
        print(f"   Short by Rs.{amount - balance:.2f}")
        return

    balance -= amount
    transaction_history.append(f"Withdrawal -Rs.{amount:.2f}")
    print()
    print(f"   SUCCESS: Rs.{amount:.2f} withdrawn.")
    print(f"   Remaining balance: Rs.{balance:.2f}")


def show_summary():
    """Printed once, when the user exits."""
    print()
    print("=" * 40)
    print("        SESSION SUMMARY")
    print("=" * 40)
    if transaction_history:
        print("Transactions this session:")
        for record in transaction_history:
            print("   ", record)
    else:
        print("No transactions were made this session.")
    print("-" * 40)
    print(f"Final balance : Rs.{balance:.2f}")
    print("Thank you for using our ATM. Goodbye!")
    print("=" * 40)


# ---------------------------------------------------------------------------
# The main program loop
# ---------------------------------------------------------------------------

def main():
    print("=" * 40)
    print("      WELCOME TO PYTHON BANK ATM")
    print("=" * 40)

    while True:                              # keep showing the menu forever...
        show_menu()
        choice = input("Choose an option (1-4) : ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            show_summary()
            break                            # ...until the user chooses 4
        else:
            print()
            print(f"   INVALID OPTION: '{choice}'. Please enter 1, 2, 3 or 4.")


# Only run main() when this file is executed directly
if __name__ == "__main__":
    main()
