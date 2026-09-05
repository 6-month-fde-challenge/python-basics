"""
Question 2 - Largest Supplied Number Using *args
=================================================
Concept: *args combined with the "champion" pattern.

    assume the first value is the winner
    compare it against every other value
    whenever a bigger one appears, it becomes the winner

WHY args[0] AND NOT 0 AS THE STARTING POINT?
If every value were negative, nothing would beat 0 and the function
would return 0 - a number that was never passed in. Starting with the
first real value is always safe.

EDGE CASE: what if no arguments are given at all? args[0] would raise
an IndexError, so the function checks the length first and returns None.
"""


def largest(*args):
    """Return the biggest value passed in, or None if nothing was passed."""
    if len(args) == 0:                     # guard against an empty call
        return None

    biggest = args[0]                      # assume the first is the winner
    for value in args:
        if value > biggest:
            biggest = value
    return biggest


print("=" * 55)
print("FINDING THE LARGEST VALUE")
print("=" * 55)

print("largest(10, 45, 3, 78, 22)   ->", largest(10, 45, 3, 78, 22))
print("largest(5, 9)                ->", largest(5, 9))
print("largest(100)                 ->", largest(100))
print("largest(-5, -12, -3, -40)    ->", largest(-5, -12, -3, -40))
print("largest()                    ->", largest(), "  <- nothing passed in")
print()

# --- A version that shows its working --------------------------------------
print("=" * 55)
print("THE SAME LOGIC, STEP BY STEP")
print("=" * 55)


def largest_verbose(*args):
    """Same as largest(), but prints every comparison."""
    if len(args) == 0:
        print("   No values supplied.")
        return None

    print("   Values received :", args)
    biggest = args[0]
    print("   Starting assumption: biggest =", biggest)

    for value in args:
        if value > biggest:
            print(f"      {value} beats {biggest} -> new biggest")
            biggest = value
        else:
            print(f"      {value} does not beat {biggest}")
    return biggest


print("\nlargest_verbose(10, 45, 3, 78, 22)")
print("   RESULT:", largest_verbose(10, 45, 3, 78, 22))
print()

# --- Why starting at 0 would be a bug --------------------------------------
print("=" * 55)
print("WHY STARTING AT 0 WOULD BE A BUG")
print("=" * 55)


def largest_buggy(*args):
    """Deliberately wrong: starts the champion at 0."""
    biggest = 0
    for value in args:
        if value > biggest:
            biggest = value
    return biggest


print("With all-negative values (-5, -12, -3, -40):")
print("   Correct version :", largest(-5, -12, -3, -40))
print("   Buggy version   :", largest_buggy(-5, -12, -3, -40), " <- 0 was never passed in")
