"""
Exercise 09 - Prime Number Analyzer
===================================
Takes a range from the user and reports every prime it contains.

    find_primes()    - the list of primes in the range
    count_primes()   - how many there are
    sum_of_primes()  - their total, without using sum()
    largest_prime()  - the biggest one found, without using max()

WHAT MAKES A NUMBER PRIME
Exactly two divisors: 1 and itself.
    1  is NOT prime - it has only one divisor
    2  IS prime     - the only even prime
    91 is NOT prime - it is 7 x 13, which is easy to miss

WHY THE DIVISOR LOOP STOPS AT THE SQUARE ROOT
Divisors come in pairs. For 36: 2x18, 3x12, 4x9, 6x6 - and past 6 the same
pairs repeat in reverse. So nothing new can be found above the square root,
and testing further is wasted work. The condition `divisor * divisor <= n`
expresses this without needing a square-root function.

LOOPS USED
    while - to validate the range input (retries unknown) and inside
            is_prime() (the number of divisors to test depends on the value)
    for   - to walk the range once its bounds are known

SAMPLE INPUT / OUTPUT
    Start: 1    End: 50
    Primes found  : 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
    Count         : 15
    Sum           : 328
    Largest prime : 47
"""


def is_prime(number):
    """Return True if the number is prime, otherwise False."""
    # 0, 1 and every negative number are not prime
    if number < 2:
        return False

    # Test divisors from 2 up to the square root of the number
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False          # a divisor exists, so it is not prime
        divisor += 1

    return True                   # no divisor found


def find_primes(start, end):
    """Return a list of every prime number between start and end inclusive."""
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes


def count_primes(primes):
    """Return how many primes were found."""
    return len(primes)


def sum_of_primes(primes):
    """Return the total of all the primes, calculated without sum()."""
    total = 0
    for prime in primes:
        total += prime
    return total


def largest_prime(primes):
    """
    Return the largest prime in the list, without using max().

    Returns None if the list is empty.
    """
    if len(primes) == 0:
        return None

    biggest = primes[0]
    for prime in primes:
        if prime > biggest:
            biggest = prime
    return biggest


def smallest_prime(primes):
    """Return the smallest prime in the list, or None if there are none."""
    if len(primes) == 0:
        return None

    smallest = primes[0]
    for prime in primes:
        if prime < smallest:
            smallest = prime
    return smallest


def get_range_value(prompt):
    """
    Ask for one end of the range and return it as an integer.

    Keeps asking until a valid whole number is entered.
    """
    # while: the number of retries depends on how often the user mistypes
    while True:
        entry = input(prompt)
        try:
            return int(entry)
        except ValueError:
            print(f"      ERROR: '{entry}' is not a whole number. Try again.")


def display_report(start, end, primes):
    """Print the full prime analysis for a range."""
    print()
    print("=" * 56)
    print(f"        PRIME ANALYSIS FOR {start} TO {end}")
    print("=" * 56)

    if len(primes) == 0:
        print(f"   No prime numbers exist between {start} and {end}.")
        print("=" * 56)
        return

    print("   PRIMES FOUND")
    print("   " + "-" * 50)

    position = 0
    for prime in primes:
        print(f"{prime:>6}", end="")
        position += 1
        if position % 8 == 0:      # eight per line keeps it readable
            print()
    if position % 8 != 0:
        print()

    print("   " + "-" * 50)
    print(f"   {'Numbers checked':<22}: {end - start + 1}")
    print(f"   {'Primes found':<22}: {count_primes(primes)}")
    print(f"   {'Sum of primes':<22}: {sum_of_primes(primes)}")
    print(f"   {'Largest prime':<22}: {largest_prime(primes)}")
    print(f"   {'Smallest prime':<22}: {smallest_prime(primes)}")

    density = (count_primes(primes) / (end - start + 1)) * 100
    print(f"   {'Density':<22}: {density:.1f}% of the range is prime")
    print("=" * 56)


def main():
    """Run the prime analyzer on a built-in range, then a user-supplied one."""
    print("=" * 56)
    print("              PRIME NUMBER ANALYZER")
    print("=" * 56)

    # --- A built-in example so the program demonstrates itself -------------
    print("   Example run for the range 1 to 50:")
    display_report(1, 50, find_primes(1, 50))

    # --- Now the user's own range ------------------------------------------
    print()
    print("=" * 56)
    print("              ANALYSE YOUR OWN RANGE")
    print("=" * 56)

    start = get_range_value("   Enter the START of the range : ")
    end = get_range_value("   Enter the END of the range   : ")

    # Swap them rather than refusing, if they were entered the wrong way round
    if start > end:
        print(f"   Note: {start} is greater than {end}, so the values were swapped.")
        start, end = end, start

    primes = find_primes(start, end)
    display_report(start, end, primes)


if __name__ == "__main__":
    main()
