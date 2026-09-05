"""
Question 7 - Print Only the Numbers Divisible by 3
===================================================
Concept: looping over a LIST with a filter condition.

    n % 3 == 0   means "dividing by 3 leaves no remainder"

Note the difference from Questions 2 and 3: there we looped over a
range() of generated numbers. Here we loop over an EXISTING LIST, so
range() is not needed at all - the for loop takes the items directly.

Sample output: 12, 9, 33, 42, 15
"""

numbers = [12, 7, 9, 20, 33, 42, 8, 15]

print("Original list :", numbers)
print("Count         :", len(numbers))
print()

print("Testing each number:")
matches = []

for n in numbers:
    if n % 3 == 0:
        matches.append(n)
        print(f"   {n:>3}  ->  {n} % 3 = 0   -> DIVISIBLE by 3")
    else:
        print(f"   {n:>3}  ->  {n} % 3 = {n % 3}   -> not divisible")

print()
print("=" * 45)
print("NUMBERS DIVISIBLE BY 3")
print("=" * 45)
for n in matches:
    print("   ", n)

print()
print("As a list  :", matches)
print("How many   :", len(matches), "out of", len(numbers))
print("Their total:", sum(matches))
print()

# --- Showing the division for each match -----------------------------------
print("Proof:")
for n in matches:
    print(f"   {n} = 3 x {n // 3}")
