"""
Question 11 - Determine Whether a Number Is Prime Using a Loop
===============================================================
A PRIME number has exactly two divisors: 1 and itself.
    7  is prime     -> nothing between 2 and 6 divides it
    9  is not prime -> 3 divides it
    1  is NOT prime -> it has only one divisor, not two
    2  IS prime     -> the only even prime

THE ALGORITHM
    assume the number is prime
    test every possible divisor from 2 upwards
    the moment one divides evenly -> it is NOT prime -> break out
    if no divisor was ever found  -> it is prime

WHY STOP AT THE SQUARE ROOT?
Divisors come in pairs. For 36: 2x18, 3x12, 4x9, 6x6, 9x4, 12x3, 18x2.
After the square root (6) the same pairs simply repeat in reverse, so
there is nothing new to find. Testing only up to int(n ** 0.5) + 1 gives
exactly the same answer with far fewer checks.
"""


def is_prime(n):
    """Return True if n is a prime number."""
    # Rule 1: 0, 1 and every negative number are not prime
    if n < 2:
        return False

    # Rule 2: test every possible divisor from 2 up to the square root
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False               # found a divisor -> not prime
        divisor += 1

    return True                        # no divisor found -> prime


def check_with_working(number):
    """Run the prime test on one number, printing every step."""
    print("=" * 55)
    print("STEP BY STEP CHECK : is", number, "prime?")
    print("=" * 55)

    if number < 2:
        print("  ", number, "is less than 2 -> NOT prime")
        return False

    limit = int(number ** 0.5) + 1
    print("   Testing divisors from 2 up to", limit - 1)

    for divisor in range(2, limit):
        remainder = number % divisor
        if remainder == 0:
            print(f"   {number} % {divisor} = 0   -> {divisor} divides it -> NOT prime, stop")
            print()
            print("RESULT:", number, "is NOT prime")
            print("        because", number, "=", divisor, "x", number // divisor)
            return False
        print(f"   {number} % {divisor} = {remainder}   -> not a divisor, keep testing")

    print()
    print("RESULT:", number, "is PRIME (no divisor was ever found)")
    return True


# --- A number that IS prime ------------------------------------------------
check_with_working(29)
print()

# --- A tricky number that looks prime but is not ---------------------------
check_with_working(91)
print()

# --- Test a range of values, including the edge cases ----------------------
print("=" * 55)
print("TESTING MANY NUMBERS")
print("=" * 55)

for n in [-5, 0, 1, 2, 3, 4, 9, 17, 25, 29, 91, 97, 100]:
    if is_prime(n):
        print(f"   {n:>4} -> PRIME")
    else:
        print(f"   {n:>4} -> not prime")

print()
print("Note the edge cases: 1 is NOT prime, and 2 IS prime.")
print()

# --- Let the user try ------------------------------------------------------
entry = input("Enter a number to test : ")
try:
    user_number = int(entry)
except ValueError:
    print("'" + entry + "' is not a valid whole number.")
else:
    if is_prime(user_number):
        print(user_number, "IS a prime number.")
    else:
        print(user_number, "is NOT a prime number.")
