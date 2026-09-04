"""
Question 4 - Largest of Three Numbers WITHOUT max()
====================================================
max() is not used - the comparison logic is written by hand, inside the
function, which is the whole point here.

TWO WAYS TO WRITE IT
   Method 1 - nested if/elif comparing all three directly
   Method 2 - the "champion" pattern: assume the first is biggest, then
              challenge it against the other two

Method 2 is better because it scales. Comparing three numbers by hand is
manageable; comparing ten by hand would be unreadable, while the champion
pattern stays the same length.

NOTE ON TIES: >= versus > only matters when two values are equal, and
either way the returned NUMBER is correct.
"""


def largest_of_three(a, b, c):
    """Return the largest of three numbers using direct comparison."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def largest_champion(a, b, c):
    """Return the largest of three numbers using the champion pattern."""
    biggest = a                      # assume the first one wins
    if b > biggest:
        biggest = b
    if c > biggest:
        biggest = c
    return biggest


print("=" * 55)
print("METHOD 1 - direct comparison")
print("=" * 55)

tests = [
    (10, 25, 7),
    (100, 45, 60),
    (3, 8, 99),
    (-5, -12, -3),
    (7, 7, 7),
    (50, 50, 20),
]

for a, b, c in tests:
    print(f"   largest_of_three({a:>4}, {b:>4}, {c:>4}) = {largest_of_three(a, b, c)}")

print()
print("=" * 55)
print("METHOD 2 - the champion pattern")
print("=" * 55)

for a, b, c in tests:
    print(f"   largest_champion({a:>4}, {b:>4}, {c:>4}) = {largest_champion(a, b, c)}")

print()
print("=" * 55)
print("BOTH METHODS AGREE")
print("=" * 55)
agree = True
for a, b, c in tests:
    if largest_of_three(a, b, c) != largest_champion(a, b, c):
        agree = False
print("   Same answer on every test case :", agree)
print()

print("=" * 55)
print("THE CHAMPION PATTERN, STEP BY STEP")
print("=" * 55)


def largest_verbose(a, b, c):
    """Return the largest of three numbers, printing each comparison."""
    biggest = a
    print(f"      start: biggest = {a} (the first number)")

    if b > biggest:
        print(f"      {b} beats {biggest} -> biggest becomes {b}")
        biggest = b
    else:
        print(f"      {b} does not beat {biggest}")

    if c > biggest:
        print(f"      {c} beats {biggest} -> biggest becomes {c}")
        biggest = c
    else:
        print(f"      {c} does not beat {biggest}")

    return biggest


print("   largest_verbose(10, 25, 7)")
print("   RESULT:", largest_verbose(10, 25, 7))
print()
print("   largest_verbose(-5, -12, -3)")
print("   RESULT:", largest_verbose(-5, -12, -3))
print()
print("   Starting from `a` rather than 0 is what makes the negative case work.")
