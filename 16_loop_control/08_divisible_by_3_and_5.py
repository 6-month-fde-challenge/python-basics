"""
Question 8 - Numbers Between 1 and 200 Divisible by BOTH 3 and 5
=================================================================
Concept: a loop with a compound condition using `and`.

    n % 3 == 0 and n % 5 == 0

BOTH tests must be True. Using `or` instead would be a completely
different question - it would return every multiple of 3 as well as
every multiple of 5.

A number divisible by both 3 and 5 is a multiple of 15, so the answer
is the 15-times table up to 200.
"""

print("Numbers between 1 and 200 divisible by BOTH 3 and 5")
print("=" * 55)

results = []

for n in range(1, 201):
    if n % 3 == 0 and n % 5 == 0:
        results.append(n)
        print(f"   {n:>3}   ({n} % 3 = 0  and  {n} % 5 = 0)")

print("=" * 55)
print("All matches :", results)
print("How many    :", len(results))
print("Their total :", sum(results))
print()

# --- Why 'and' matters, compared with 'or' ---------------------------------
print("=" * 55)
print("WHY 'and' AND NOT 'or'")
print("=" * 55)

only_3 = 0
only_5 = 0
both = 0

for n in range(1, 201):
    if n % 3 == 0 and n % 5 == 0:
        both += 1
    elif n % 3 == 0:
        only_3 += 1
    elif n % 5 == 0:
        only_5 += 1

print("Divisible by 3 ONLY      :", only_3)
print("Divisible by 5 ONLY      :", only_5)
print("Divisible by BOTH (and)  :", both, "<- the answer to this question")
print("Divisible by EITHER (or) :", only_3 + only_5 + both, "<- a different question")
print()
print("Every match is a multiple of 3 x 5 = 15:")
for n in results:
    print(f"   {n:>3} = 15 x {n // 15}")
