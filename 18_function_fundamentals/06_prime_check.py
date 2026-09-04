"""
Question 6 - A Function That Checks Whether a Number Is Prime
==============================================================
A PRIME number has exactly two divisors: 1 and itself.

    7  is prime      - nothing from 2 to 6 divides it
    9  is not prime  - 3 divides it
    1  is NOT prime  - it has only one divisor, not two
    2  IS prime      - the only even prime

THE ALGORITHM (entirely inside the function)
    numbers below 2 are rejected immediately
    then test each possible divisor from 2 upwards
    the first divisor found proves it is not prime -> return False
    if the loop finishes with no divisor -> return True

WHY THE LOOP STOPS AT THE SQUARE ROOT
Divisors come in pairs. For 36: 2x18, 3x12, 4x9, 6x6, and after 6 the
same pairs simply repeat in reverse. So there is nothing new to find
above the square root, and testing further is wasted work.

The function returns a BOOLEAN, which lets the caller use it in an if,
in a filter, or in a loop that collects primes.
"""


def is_prime(number):
    """Return True if the number is prime, otherwise False."""
    if number < 2:
        return False                   # 0, 1 and negatives are not prime

    divisor = 2
    while divisor * divisor <= number:  # same as divisor <= sqrt(number)
        if number % divisor == 0:
            return False               # found a divisor -> not prime
        divisor += 1

    return True                        # no divisor found -> prime


print("=" * 50)
print("TESTING INDIVIDUAL NUMBERS")
print("=" * 50)

for n in [-7, 0, 1, 2, 3, 4, 9, 17, 25, 29, 51, 91, 97, 100]:
    if is_prime(n):
        print(f"   {n:>4} -> PRIME")
    else:
        print(f"   {n:>4} -> not prime")

print()
print("   Edge cases: 1 is NOT prime, 2 IS prime.")
print("   51 looks prime but is 3 x 17. 91 looks prime but is 7 x 13.")
print()

print("=" * 50)
print("A VERSION THAT SHOWS ITS WORKING")
print("=" * 50)


def is_prime_verbose(number):
    """Return True if the number is prime, printing every division tested."""
    if number < 2:
        print(f"      {number} is below 2 -> not prime")
        return False

    divisor = 2
    while divisor * divisor <= number:
        remainder = number % divisor
        if remainder == 0:
            print(f"      {number} % {divisor} = 0  -> divisible -> NOT prime")
            print(f"      because {number} = {divisor} x {number // divisor}")
            return False
        print(f"      {number} % {divisor} = {remainder}  -> not a divisor")
        divisor += 1

    print(f"      no divisor found -> {number} is PRIME")
    return True


print("   is_prime_verbose(29)")
print("   RESULT:", is_prime_verbose(29))
print()
print("   is_prime_verbose(91)")
print("   RESULT:", is_prime_verbose(91))
print()

print("=" * 50)
print("USING THE FUNCTION TO COLLECT ALL PRIMES BELOW 100")
print("=" * 50)

primes = []
for n in range(1, 100):
    if is_prime(n):
        primes.append(n)

print("  ", primes)
print("   Count :", len(primes))
print()
print("   This is why returning True/False is better than printing:")
print("   the answer can be used to build a list.")
