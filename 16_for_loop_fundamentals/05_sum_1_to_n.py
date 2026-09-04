"""
Question 5 - Sum of Numbers From 1 to n Using a Loop
=====================================================
Concept: the ACCUMULATOR pattern.

    total = 0                 <- start OUTSIDE the loop
    for i in range(1, n + 1):
        total += i            <- grow it on every pass

WHY total = 0 MUST BE OUTSIDE THE LOOP:
if it were inside, it would reset to 0 on every pass and the final
answer would just be the last number.

Sample input : 10
Sample output: 55      (1+2+3+4+5+6+7+8+9+10)
"""

print("=" * 45)
print("SUM OF NUMBERS FROM 1 TO n")
print("=" * 45)

entry = input("Enter a value for n : ")

try:
    n = int(entry)
except ValueError:
    print("'" + entry + "' is not a valid whole number.")
    raise SystemExit

if n < 1:
    print("Please enter a number of 1 or more.")
    raise SystemExit

# The accumulator starts at 0, OUTSIDE the loop
total = 0

print()
print("Adding one number at a time:")
for i in range(1, n + 1):             # n + 1 so that n itself is included
    total += i
    if n <= 20:                       # only show every step for small n
        print(f"   + {i:>3}  ->  running total = {total}")

print()
print("=" * 45)
print(f"SUM OF 1 TO {n} = {total}")
print("=" * 45)
print()

# --- Checking the answer with the mathematical formula ---------------------
formula = n * (n + 1) // 2
print("Verification using the formula n x (n + 1) / 2:")
print(f"   {n} x {n + 1} / 2 = {formula}")
print("   Loop answer    :", total)
print("   Formula answer :", formula)
print("   They match     :", total == formula)
