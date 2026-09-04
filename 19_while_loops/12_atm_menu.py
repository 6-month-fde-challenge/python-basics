"""
Question 12 - ATM Menu Using while
===================================
    1. Check balance    2. Deposit      3. Withdraw
    4. Mini statement   5. Exit

The application keeps running until the user explicitly chooses Exit.

WHY while: a cash machine cannot know how many transactions someone will
make. It must stay available until they walk away - a condition, never a
count. This is the textbook use of condition-controlled iteration.

THE THREE PARTS
    INITIALIZATION : `running = True` and the account state, before the loop
    CONDITION      : `while running:`
    UPDATE         : `running = False` on option 5

VALIDATION ENFORCED
    the amount must be a number
    the amount must be greater than zero
    a withdrawal can never exceed the balance
    an invalid menu choice reshows the menu instead of crashing
"""


def show_menu(balance):
    """Display the ATM menu along with the current balance."""
    print()
    print("=" * 44)
    print("            PYTHON BANK ATM")
    print("=" * 44)
    print(f"   Available balance : Rs.{balance:.2f}")
    print("   " + "-" * 38)
    print("   1. Check balance")
    print("   2. Deposit money")
    print("   3. Withdraw money")
    print("   4. Mini statement")
    print("   5. Exit")
    print("=" * 44)


def get_amount(action):
    """Ask for an amount and return it as a float, or None if invalid."""
    entry = input(f"   Enter amount to {action} : Rs.")

    try:
        amount = float(entry)
    except ValueError:
        print(f"      INVALID: '{entry}' is not a number.")
        return None

    if amount <= 0:
        print(f"      INVALID: the amount must be more than zero (you entered {amount}).")
        return None

    return amount


# INITIALIZATION : the account state and the loop flag, all set before the loop
balance = 5000.0
history = []
running = True

print("Welcome. Please choose an option.")

# CONDITION : the machine stays available while `running` is True
while running:
    show_menu(balance)
    choice = input("   Choose an option (1-5) : ").strip()

    if choice == "1":
        print()
        print(f"   Your balance is Rs.{balance:.2f}")

    elif choice == "2":
        amount = get_amount("deposit")
        if amount is not None:
            balance += amount
            history.append(f"Deposit     +Rs.{amount:.2f}")
            print()
            print(f"   SUCCESS: Rs.{amount:.2f} deposited.")
            print(f"   New balance: Rs.{balance:.2f}")

    elif choice == "3":
        amount = get_amount("withdraw")
        if amount is not None:
            if amount > balance:
                print()
                print("   DECLINED: insufficient funds.")
                print(f"   You asked for Rs.{amount:.2f} but hold Rs.{balance:.2f}.")
                print(f"   Short by Rs.{amount - balance:.2f}")
            else:
                balance -= amount
                history.append(f"Withdrawal  -Rs.{amount:.2f}")
                print()
                print(f"   SUCCESS: Rs.{amount:.2f} withdrawn.")
                print(f"   Remaining balance: Rs.{balance:.2f}")

    elif choice == "4":
        print()
        print("   MINI STATEMENT")
        print("   " + "-" * 34)
        if len(history) == 0:
            print("   No transactions this session.")
        else:
            # INITIALIZATION : index for walking the history list
            i = 0
            # CONDITION : while there are entries left to print
            while i < len(history):
                print(f"   {i + 1}. {history[i]}")
                # UPDATE : move to the next entry
                i += 1
        print("   " + "-" * 34)
        print(f"   Current balance: Rs.{balance:.2f}")

    elif choice == "5":
        # UPDATE / TERMINATION : this is the only line that ends the program.
        # Without it the while condition stays True and the ATM never closes.
        running = False
        print()
        print("=" * 44)
        print("            SESSION SUMMARY")
        print("=" * 44)
        if len(history) == 0:
            print("   No transactions were made.")
        else:
            print("   Transactions this session:")
            for record in history:
                print("      " + record)
        print("   " + "-" * 38)
        print(f"   Final balance : Rs.{balance:.2f}")
        print("   Thank you for banking with us. Goodbye!")
        print("=" * 44)

    else:
        # An invalid choice must NOT end the loop
        print()
        print(f"   INVALID OPTION: '{choice}'. Please choose 1 to 5.")
