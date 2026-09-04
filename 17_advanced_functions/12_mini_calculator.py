"""
Question 12 - Mini Calculator
==============================
Every mathematical operation is a SEPARATE FUNCTION, and a MAIN FUNCTION
controls the program.

PROJECT ORGANISATION (two files, two jobs)
    operations.py         -> the maths: add, subtract, multiply, divide,
                             power, modulus. No printing, no input.
    12_mini_calculator.py -> this file: the menu, the input, the output.

Why split them? The maths functions can then be tested, reused or replaced
without touching the menu, and the menu can be redesigned without any risk
to the maths. Run `python operations.py` on its own to see its self-test.

HOW THE MENU CHOOSES AN OPERATION
Instead of a long if/elif chain, a DICTIONARY maps each menu choice to a
FUNCTION OBJECT:

    OPERATIONS = {"1": ("Addition", operations.add), ...}

Adding a new operation then means adding one dictionary entry - no new
branches. This is the same "functions are objects" idea as Question 4.
"""

import operations

# Menu choice -> (label, symbol, the function to call)
OPERATIONS = {
    "1": ("Addition", "+", operations.add),
    "2": ("Subtraction", "-", operations.subtract),
    "3": ("Multiplication", "*", operations.multiply),
    "4": ("Division", "/", operations.divide),
    "5": ("Power", "**", operations.power),
    "6": ("Modulus", "%", operations.modulus),
}


def show_menu():
    """Display the list of available operations."""
    print()
    print("=" * 40)
    print("          MINI CALCULATOR")
    print("=" * 40)
    for key, (label, symbol, _) in OPERATIONS.items():
        print(f"   {key}. {label:<16} ({symbol})")
    print("   7. Exit")
    print("=" * 40)


def get_number(prompt):
    """
    Ask for one number and return it as a float.

    Returns None when the text typed is not a number, so the caller can
    abandon the calculation instead of crashing.
    """
    entry = input(prompt)
    try:
        return float(entry)
    except ValueError:
        print("   INVALID: '" + entry + "' is not a number.")
        return None


def run_operation(choice):
    """Collect two numbers, run the chosen operation and show the result."""
    label, symbol, function = OPERATIONS[choice]

    print()
    print(f"   --- {label} ---")

    a = get_number("   Enter the first number  : ")
    if a is None:
        return

    b = get_number("   Enter the second number : ")
    if b is None:
        return

    result = function(a, b)            # the function from the dictionary is called here

    print()
    if result is None:
        # divide() and modulus() return None when the second number is zero
        print(f"   ERROR: cannot use {symbol} with a second number of zero.")
    else:
        print(f"   RESULT: {a} {symbol} {b} = {result}")


def main():
    """The main function - it controls the whole program."""
    print("Welcome to the mini calculator.")

    while True:
        show_menu()
        choice = input("Choose an option (1-7) : ").strip()

        if choice == "7":
            print()
            print("Goodbye!")
            break
        elif choice in OPERATIONS:
            run_operation(choice)
        else:
            print()
            print(f"   INVALID OPTION: '{choice}'. Please choose 1 to 7.")


# Start the program only when this file is run directly
if __name__ == "__main__":
    main()
