"""
Question 11 - Menu-Driven Calculator
=====================================
    1. Add        2. Subtract     3. Multiply
    4. Divide     5. Exit

The menu reappears after every operation and stops only when the user
chooses 5.

WHY while: a menu has no known number of passes. The user might do one
calculation or fifty. The loop must keep running until they explicitly
choose to leave - which is a condition, not a count.

THE THREE PARTS IN A MENU LOOP
    INITIALIZATION : `running = True` before the loop
    CONDITION      : `while running:`
    UPDATE         : `running = False` when option 5 is chosen

That single assignment is what prevents an infinite loop. Without it the
program could never be exited.
"""


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """Return a / b, or None if b is zero."""
    if b == 0:
        return None
    return a / b


def show_menu():
    """Display the calculator menu."""
    print()
    print("=" * 40)
    print("         MENU-DRIVEN CALCULATOR")
    print("=" * 40)
    print("   1. Add")
    print("   2. Subtract")
    print("   3. Multiply")
    print("   4. Divide")
    print("   5. Exit")
    print("=" * 40)


def get_number(prompt):
    """Ask for a number and return it as a float, or None if invalid."""
    entry = input(prompt)
    try:
        return float(entry)
    except ValueError:
        print("      INVALID: '" + entry + "' is not a number.")
        return None


print("Welcome to the calculator.")

# INITIALIZATION : the flag that keeps the menu alive, set before the loop
running = True
calculations = 0

# CONDITION : keep showing the menu while `running` is True
while running:
    show_menu()
    choice = input("   Choose an option (1-5) : ").strip()

    # UPDATE / TERMINATION : option 5 sets the flag False, which makes the
    # condition above False on the next check and ends the program.
    if choice == "5":
        running = False
        print()
        print("   Exiting the calculator.")
        print("   Calculations performed this session:", calculations)
        print("   Goodbye!")

    elif choice in ("1", "2", "3", "4"):
        a = get_number("   Enter the first number  : ")
        if a is None:
            continue                       # back to the menu, nothing lost

        b = get_number("   Enter the second number : ")
        if b is None:
            continue

        if choice == "1":
            print(f"   RESULT: {a} + {b} = {add(a, b)}")
            calculations += 1
        elif choice == "2":
            print(f"   RESULT: {a} - {b} = {subtract(a, b)}")
            calculations += 1
        elif choice == "3":
            print(f"   RESULT: {a} * {b} = {multiply(a, b)}")
            calculations += 1
        else:
            result = divide(a, b)
            if result is None:
                print("   ERROR: cannot divide by zero.")
            else:
                print(f"   RESULT: {a} / {b} = {result}")
                calculations += 1

    else:
        # An invalid choice must NOT end the loop - it just reshows the menu
        print(f"   INVALID OPTION: '{choice}'. Please choose 1 to 5.")
