"""
Exercise 12 - Python Utility Application
========================================
A single menu-driven application bundling SEVEN utilities:

    1. Calculator                5. Number Analyzer
    2. Palindrome Checker        6. Password Strength Checker
    3. Prime Checker             7. Vowel & Character Counter
    4. Factorial Calculator      8. Multiplication Table
    9. Exit

STRUCTURE
Every utility is its own function, so each can be read and tested alone.
main() only routes the user's choice to the right one - it contains no
calculation logic itself.

WHY while FOR THE MENU
The user decides how many utilities to run and in what order. The
application must stay open until Exit is chosen, which is a condition and
not a count. `running = False` is the only line that ends it.

ERROR HANDLING
Every utility validates its own input and returns to the menu on bad data,
rather than crashing the whole application.

SAMPLE INPUT / OUTPUT
    Option 3, number 97   -> 97 is a PRIME number
    Option 4, number 6    -> 6! = 720
    Option 2, text madam  -> 'madam' IS a palindrome
"""

SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"


# ---------------------------------------------------------------------------
# Shared input helpers
# ---------------------------------------------------------------------------

def get_number(prompt, whole_number=False):
    """
    Ask for a number and return it, or None if the input is invalid.

    whole_number - require an integer rather than a decimal.
    """
    entry = input(prompt)
    try:
        return int(entry) if whole_number else float(entry)
    except ValueError:
        kind = "whole number" if whole_number else "number"
        print(f"      ERROR: '{entry}' is not a valid {kind}.")
        return None


# ---------------------------------------------------------------------------
# Utility 1 - Calculator
# ---------------------------------------------------------------------------

def utility_calculator():
    """Add, subtract, multiply, divide, power or modulus two numbers."""
    print()
    print("   --- CALCULATOR ---")
    print("   Operations: +  -  *  /  **  %")

    a = get_number("   First number  : ")
    if a is None:
        return

    operator = input("   Operator       : ").strip()

    b = get_number("   Second number : ")
    if b is None:
        return

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "**":
        result = a ** b
    elif operator in ("/", "%"):
        if b == 0:
            print(f"      ERROR: cannot use '{operator}' with a second number of zero.")
            return
        result = a / b if operator == "/" else a % b
    else:
        print(f"      ERROR: '{operator}' is not a supported operator.")
        return

    print()
    print(f"   RESULT: {a} {operator} {b} = {result}")


# ---------------------------------------------------------------------------
# Utility 2 - Palindrome Checker
# ---------------------------------------------------------------------------

def utility_palindrome():
    """Check whether a word or sentence reads the same in both directions."""
    print()
    print("   --- PALINDROME CHECKER ---")

    text = input("   Enter a word or sentence : ").strip()

    if text == "":
        print("      ERROR: nothing was entered.")
        return

    # Clean the text: drop spaces and ignore capitals
    cleaned = ""
    for char in text:
        if char != " ":
            cleaned += char.lower()

    # Two-pointer comparison, moving inwards from both ends
    left = 0
    right = len(cleaned) - 1
    palindrome = True

    while left < right:
        if cleaned[left] != cleaned[right]:
            palindrome = False
            break
        left += 1
        right -= 1

    print()
    print(f"   Cleaned text : '{cleaned}'")
    if palindrome:
        print(f"   RESULT: '{text}' IS a palindrome.")
    else:
        print(f"   RESULT: '{text}' is NOT a palindrome.")


# ---------------------------------------------------------------------------
# Utility 3 - Prime Checker
# ---------------------------------------------------------------------------

def is_prime(number):
    """Return True if the number is prime, otherwise False."""
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def utility_prime():
    """Check whether a number is prime, showing a divisor if it is not."""
    print()
    print("   --- PRIME CHECKER ---")

    number = get_number("   Enter a whole number : ", whole_number=True)
    if number is None:
        return

    print()
    if is_prime(number):
        print(f"   RESULT: {number} is a PRIME number.")
        print("   It has exactly two divisors: 1 and itself.")
    else:
        print(f"   RESULT: {number} is NOT a prime number.")
        if number < 2:
            print("   Numbers below 2 are not prime by definition.")
        else:
            # Show the first divisor as evidence
            divisor = 2
            while divisor * divisor <= number:
                if number % divisor == 0:
                    print(f"   It divides evenly: {number} = "
                          f"{divisor} x {number // divisor}")
                    break
                divisor += 1


# ---------------------------------------------------------------------------
# Utility 4 - Factorial Calculator
# ---------------------------------------------------------------------------

def utility_factorial():
    """Calculate the factorial of a number using a loop."""
    print()
    print("   --- FACTORIAL CALCULATOR ---")

    number = get_number("   Enter a whole number : ", whole_number=True)
    if number is None:
        return

    if number < 0:
        print("      ERROR: factorial is not defined for negative numbers.")
        return

    if number > 500:
        print("      ERROR: please choose 500 or less - larger values are unwieldy.")
        return

    # A product must start at 1, because anything multiplied by 0 is 0
    result = 1
    i = 1
    while i <= number:
        result *= i
        i += 1

    print()
    print(f"   RESULT: {number}! = {result}")

    if 0 < number <= 10:
        working = ""
        i = 1
        while i <= number:
            working += str(i)
            if i < number:
                working += " x "
            i += 1
        print(f"   Working: {working} = {result}")


# ---------------------------------------------------------------------------
# Utility 5 - Number Analyzer
# ---------------------------------------------------------------------------

def utility_number_analyzer():
    """Report statistics for a list of numbers, without min/max/sum."""
    print()
    print("   --- NUMBER ANALYZER ---")

    entry = input("   Enter numbers separated by spaces : ")

    numbers = []
    for piece in entry.split():
        try:
            numbers.append(float(piece))
        except ValueError:
            print(f"      Skipping '{piece}' - not a number.")

    if len(numbers) == 0:
        print("      ERROR: no valid numbers were entered.")
        return

    # A single pass collects every statistic
    largest = numbers[0]
    smallest = numbers[0]
    total = 0.0
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    for number in numbers:
        total += number
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1

    print()
    print(f"   Count    : {len(numbers)}")
    print(f"   Largest  : {largest}")
    print(f"   Smallest : {smallest}")
    print(f"   Total    : {total}")
    print(f"   Average  : {total / len(numbers):.2f}")
    print(f"   Even     : {even_count}    Odd      : {odd_count}")
    print(f"   Positive : {positive_count}    Negative : {negative_count}")


# ---------------------------------------------------------------------------
# Utility 6 - Password Strength Checker
# ---------------------------------------------------------------------------

def utility_password_checker():
    """Score a password against five strength rules."""
    print()
    print("   --- PASSWORD STRENGTH CHECKER ---")

    password = input("   Enter a password : ")

    if password == "":
        print("      ERROR: nothing was entered.")
        return

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in SPECIAL_CHARACTERS:
            has_special = True

    long_enough = len(password) >= 8

    checks = {
        "At least 8 characters": long_enough,
        "Uppercase letter": has_upper,
        "Lowercase letter": has_lower,
        "Number": has_digit,
        "Special character": has_special,
    }

    score = 0
    for passed in checks.values():
        if passed:
            score += 1

    if score == 5:
        strength = "VERY STRONG"
    elif score == 4:
        strength = "STRONG"
    elif score == 3:
        strength = "MEDIUM"
    elif score == 2:
        strength = "WEAK"
    else:
        strength = "VERY WEAK"

    print()
    for rule, passed in checks.items():
        print(f"   [{'PASS' if passed else 'FAIL'}]  {rule}")
    print(f"   SCORE    : {score} / 5")
    print(f"   STRENGTH : {strength}")


# ---------------------------------------------------------------------------
# Utility 7 - Vowel and Character Counter
# ---------------------------------------------------------------------------

def utility_vowel_counter():
    """Count vowels, consonants, digits and spaces in a string."""
    print()
    print("   --- VOWEL AND CHARACTER COUNTER ---")

    text = input("   Enter some text : ")

    if text == "":
        print("      ERROR: nothing was entered.")
        return

    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0
    others = 0

    for char in text:
        if char == " ":
            spaces += 1
        elif char.isdigit():
            digits += 1
        elif char.isalpha():
            if char.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
        else:
            others += 1

    print()
    print(f"   Total characters : {len(text)}")
    print(f"   Vowels           : {vowels}")
    print(f"   Consonants       : {consonants}")
    print(f"   Digits           : {digits}")
    print(f"   Spaces           : {spaces}")
    print(f"   Other characters : {others}")


# ---------------------------------------------------------------------------
# Utility 8 - Multiplication Table
# ---------------------------------------------------------------------------

def utility_multiplication_table():
    """Print the multiplication table of a number up to a chosen limit."""
    print()
    print("   --- MULTIPLICATION TABLE ---")

    number = get_number("   Table of        : ", whole_number=True)
    if number is None:
        return

    limit = get_number("   Up to (e.g. 10) : ", whole_number=True)
    if limit is None:
        return

    if limit < 1 or limit > 100:
        print("      ERROR: please choose a limit between 1 and 100.")
        return

    print()
    i = 1
    while i <= limit:
        print(f"   {number} x {i:>3} = {number * i}")
        i += 1


# ---------------------------------------------------------------------------
# The menu
# ---------------------------------------------------------------------------

def show_menu():
    """Display the list of available utilities."""
    print()
    print("=" * 50)
    print("           PYTHON UTILITY APPLICATION")
    print("=" * 50)
    print("   1. Calculator")
    print("   2. Palindrome Checker")
    print("   3. Prime Checker")
    print("   4. Factorial Calculator")
    print("   5. Number Analyzer")
    print("   6. Password Strength Checker")
    print("   7. Vowel & Character Counter")
    print("   8. Multiplication Table")
    print("   9. Exit")
    print("=" * 50)


def main():
    """Run the utility application until the user chooses Exit."""
    print("Welcome to the Python Utility Application.")

    # Each menu choice maps to the function that handles it, which keeps
    # main() free of any calculation logic.
    utilities = {
        "1": utility_calculator,
        "2": utility_palindrome,
        "3": utility_prime,
        "4": utility_factorial,
        "5": utility_number_analyzer,
        "6": utility_password_checker,
        "7": utility_vowel_counter,
        "8": utility_multiplication_table,
    }

    # INITIALIZATION
    running = True
    used = 0

    # CONDITION : keep the application open until Exit is chosen
    while running:
        show_menu()
        choice = input("   Choose a utility (1-9) : ").strip()

        if choice == "9":
            # UPDATE / TERMINATION
            running = False
            print()
            print("=" * 50)
            print(f"   Utilities used this session : {used}")
            print("   Thank you for using the utility application. Goodbye!")
            print("=" * 50)
        elif choice in utilities:
            utilities[choice]()      # call the chosen utility function
            used += 1
        else:
            print()
            print(f"   INVALID OPTION: '{choice}'. Please choose 1 to 9.")


if __name__ == "__main__":
    main()
