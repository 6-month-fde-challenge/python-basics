"""
Question 1 - Print Numbers From 1 to 100 Using a for Loop
==========================================================
Concept: range(start, stop) and the for loop.

    range(1, 101)  ->  1, 2, 3 ... 100

THE MOST COMMON MISTAKE: writing range(1, 100).
The STOP value is always EXCLUDED, so range(1, 100) ends at 99.
To reach 100 the stop must be 101.

Sample output: 1 2 3 4 5 ... 98 99 100
"""

print("Numbers from 1 to 100")
print("=" * 60)

for n in range(1, 101):
    print(n, end="  ")

print()
print("=" * 60)
print("Count of numbers printed :", len(range(1, 101)))
print()

# --- Proof that the stop value is excluded ---------------------------------
print("Why the stop value is 101 and not 100:")
print("   range(1, 100) gives 1 to", list(range(1, 100))[-1], "  <- misses 100")
print("   range(1, 101) gives 1 to", list(range(1, 101))[-1], " <- correct")
print()

# --- The three forms of range() --------------------------------------------
print("The three ways to write range():")
print("   range(5)         ->", list(range(5)), "         (stop only, starts at 0)")
print("   range(1, 6)      ->", list(range(1, 6)), "      (start and stop)")
print("   range(1, 11, 2)  ->", list(range(1, 11, 2)), " (start, stop and step)")
print()

# --- Printed 10 per line for readability -----------------------------------
print("The same numbers, 10 per line:")
for n in range(1, 101):
    print(f"{n:>4}", end="")
    if n % 10 == 0:
        print()
