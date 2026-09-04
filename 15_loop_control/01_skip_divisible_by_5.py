"""
Question 1 - Print 1 to 100, Skipping Multiples of 5, Using continue
=====================================================================
Concept: the `continue` statement.

`continue` does NOT end the loop. It abandons the CURRENT pass only and
jumps straight back to the top for the next number. Any code written
below `continue` is skipped for that one number.

    for n in range(1, 101):
        if n % 5 == 0:
            continue        <- jump to the next n, do not print
        print(n)            <- only reached when n is NOT a multiple of 5

The test  n % 5 == 0  means "the remainder after dividing by 5 is zero",
which is the definition of "divisible by 5".
"""

print("Numbers from 1 to 100, skipping every multiple of 5")
print("=" * 60)

printed = 0
skipped = 0

for n in range(1, 101):
    if n % 5 == 0:
        skipped += 1
        continue                     # skip 5, 10, 15, 20 ... 100
    print(n, end="  ")
    printed += 1

print()
print("=" * 60)
print("Numbers printed :", printed)
print("Numbers skipped :", skipped, "(the multiples of 5)")
print("Total checked   :", printed + skipped)
print()

# --- Showing the decision for the first 20 numbers -------------------------
print("What the loop decides for the first 20 numbers:")
for n in range(1, 21):
    if n % 5 == 0:
        print(f"   {n:>3}  ->  {n} % 5 = 0   -> continue (skipped)")
        continue
    print(f"   {n:>3}  ->  {n} % 5 = {n % 5}   -> printed")
