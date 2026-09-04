"""
Question 10 - Count Positive, Negative and Zero Values
=======================================================
Concept: three counters driven by if / elif / else.

The three categories are MUTUALLY EXCLUSIVE - a number is positive OR
negative OR zero, never two at once. That is exactly what if/elif/else
expresses: the first matching branch wins and the rest are skipped.

WATCH THE ZERO. Zero is neither positive nor negative, so it must have
its own branch. Writing  if n >= 0  would wrongly count 0 as positive.
"""

numbers = [10, -4, 8, -2, 0, 15, -9, 21]

print("Numbers :", numbers)
print("Count   :", len(numbers))
print()

positive = 0
negative = 0
zero = 0

print("Classifying each number:")
for n in numbers:
    if n > 0:
        positive += 1
        label = "POSITIVE"
    elif n < 0:
        negative += 1
        label = "NEGATIVE"
    else:                              # the only value left is exactly 0
        zero += 1
        label = "ZERO"
    print(f"   {n:>4} -> {label}")

print()
print("=" * 35)
print("RESULT")
print("=" * 35)
print("Positive numbers :", positive)
print("Negative numbers :", negative)
print("Zeros            :", zero)
print("-" * 35)
print("Total counted    :", positive + negative + zero, "of", len(numbers))
print()

# --- Visual summary --------------------------------------------------------
print("Distribution:")
print("  Positive |", "+" * positive)
print("  Negative |", "-" * negative)
print("  Zero     |", "0" * zero)
print()

# --- Why zero needs its own branch -----------------------------------------
print("=" * 45)
print("WHY ZERO NEEDS ITS OWN BRANCH")
print("=" * 45)

wrong_positive = 0
for n in numbers:
    if n >= 0:                         # deliberately wrong: >= instead of >
        wrong_positive += 1

print("Using  n > 0   (correct) -> positive count =", positive)
print("Using  n >= 0  (wrong)   -> positive count =", wrong_positive)
print("The wrong version counts 0 as positive, giving one too many.")
