"""
Exercise 08 - Password Strength Checker
=======================================
Checks a password against five rules and returns a meaningful strength
rating rather than a bare True/False.

    THE FIVE RULES
        at least 8 characters
        at least one uppercase letter    (A-Z)
        at least one lowercase letter    (a-z)
        at least one digit               (0-9)
        at least one special character   (!@#$ etc.)

FUNCTIONS
    has_uppercase()        - rule 2
    has_lowercase()        - rule 3
    has_digit()            - rule 4
    has_special_char()     - rule 5
    check_password()       - run all five and return a full report
    display_report()       - print the checklist, rating and suggestions

WHY EACH RULE IS ITS OWN FUNCTION
Each returns True or False and can be read, tested and reused on its own.
check_password() then combines them, so the scoring logic sits in one place
and the rules sit in another.

THE RATING
    5 of 5 rules -> Very Strong
    4 of 5       -> Strong
    3 of 5       -> Medium
    2 of 5       -> Weak
    0-1 of 5     -> Very Weak

SAMPLE INPUT / OUTPUT
    "python"       -> 1/5  Very Weak
    "Python123"    -> 4/5  Strong      (missing a special character)
    "Python@123"   -> 5/5  Very Strong
"""

SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
MINIMUM_LENGTH = 8


def has_minimum_length(password):
    """Return True if the password is at least MINIMUM_LENGTH characters."""
    return len(password) >= MINIMUM_LENGTH


def has_uppercase(password):
    """Return True if the password contains at least one uppercase letter."""
    for char in password:
        if char.isupper():
            return True
    return False


def has_lowercase(password):
    """Return True if the password contains at least one lowercase letter."""
    for char in password:
        if char.islower():
            return True
    return False


def has_digit(password):
    """Return True if the password contains at least one digit."""
    for char in password:
        if char.isdigit():
            return True
    return False


def has_special_char(password):
    """Return True if the password contains at least one special character."""
    for char in password:
        if char in SPECIAL_CHARACTERS:
            return True
    return False


def rate_strength(score):
    """Return a strength label for a score out of five."""
    if score == 5:
        return "VERY STRONG"
    elif score == 4:
        return "STRONG"
    elif score == 3:
        return "MEDIUM"
    elif score == 2:
        return "WEAK"
    return "VERY WEAK"


def check_password(password):
    """
    Check a password against all five rules.

    Returns a dictionary holding each rule's result, the score out of five,
    the strength label, and a list of suggestions for whatever failed.
    """
    checks = {
        f"At least {MINIMUM_LENGTH} characters": has_minimum_length(password),
        "Contains an uppercase letter": has_uppercase(password),
        "Contains a lowercase letter": has_lowercase(password),
        "Contains a number": has_digit(password),
        "Contains a special character": has_special_char(password),
    }

    # Count how many rules passed, without using sum()
    score = 0
    for passed in checks.values():
        if passed:
            score += 1

    # Build advice for whatever failed
    suggestions = []
    if not checks[f"At least {MINIMUM_LENGTH} characters"]:
        short_by = MINIMUM_LENGTH - len(password)
        suggestions.append(f"Add {short_by} more character(s).")
    if not checks["Contains an uppercase letter"]:
        suggestions.append("Add a capital letter, for example A or M.")
    if not checks["Contains a lowercase letter"]:
        suggestions.append("Add a small letter, for example a or m.")
    if not checks["Contains a number"]:
        suggestions.append("Add a digit, for example 7.")
    if not checks["Contains a special character"]:
        suggestions.append("Add a special character, for example @ or #.")

    return {
        "password": password,
        "length": len(password),
        "checks": checks,
        "score": score,
        "strength": rate_strength(score),
        "suggestions": suggestions,
        "accepted": score == 5,
    }


def display_report(result):
    """Print the full password strength report."""
    print()
    print("=" * 54)
    print(f"   PASSWORD : {result['password']}")
    print(f"   LENGTH   : {result['length']} characters")
    print("=" * 54)

    for rule, passed in result["checks"].items():
        mark = "PASS" if passed else "FAIL"
        print(f"   [{mark}]  {rule}")

    print("   " + "-" * 48)
    bar = "#" * result["score"] + "." * (5 - result["score"])
    print(f"   SCORE    : {result['score']} / 5   [{bar}]")
    print(f"   STRENGTH : {result['strength']}")

    if result["accepted"]:
        print("   RESULT   : Accepted - this password meets every rule.")
    else:
        print("   RESULT   : Rejected - improve the following:")
        for suggestion in result["suggestions"]:
            print(f"      - {suggestion}")

    print("=" * 54)


def main():
    """Check a set of example passwords, then anything the user enters."""
    print("=" * 54)
    print("            PASSWORD STRENGTH CHECKER")
    print("=" * 54)

    examples = [
        "python",
        "PYTHON123",
        "Python12",
        "Python123",
        "Python@123",
        "P@1a",
        "correct horse battery staple",
    ]

    for password in examples:
        display_report(check_password(password))

    # --- Let the user test their own ---------------------------------------
    print()
    print("=" * 54)
    print("            TEST YOUR OWN PASSWORD")
    print("=" * 54)

    user_password = input("   Enter a password to check : ")

    if user_password == "":
        print("   Nothing entered - skipping.")
    else:
        display_report(check_password(user_password))


if __name__ == "__main__":
    main()
