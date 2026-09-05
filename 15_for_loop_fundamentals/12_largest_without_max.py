"""
Question 12 - Find the Largest Number WITHOUT max()
====================================================
Concept: the "champion" pattern.

    assume the FIRST item is the winner
    compare it against every other item
    whenever something bigger appears, IT becomes the winner

WHY START WITH numbers[0] AND NOT 0?
Starting at 0 looks harmless but is a real bug: if every number in the
list is negative, nothing is above 0, and the program would wrongly
answer 0 - a value that is not even in the list. Starting with the
first actual element is always safe.

Sample input : [12, 7, 9, 20, 33, 42, 8, 15]
Sample output: 42
"""

numbers = [12, 7, 9, 20, 33, 42, 8, 15]

print("Numbers :", numbers)
print()

# Assume the first number is the largest
largest = numbers[0]
print("Starting assumption: largest =", largest, "(the first element)")
print()

print("Comparing each number against the current champion:")
for n in numbers:
    if n > largest:
        print(f"   {n:>3} is bigger than {largest} -> {n} becomes the new largest")
        largest = n
    else:
        print(f"   {n:>3} is not bigger than {largest} -> no change")

print()
print("=" * 45)
print("LARGEST NUMBER :", largest)
print("=" * 45)
print()

# Verification (max() used ONLY to prove the loop is correct)
print("Check with max() :", max(numbers), "-> match:", largest == max(numbers))
print()

# --- The same pattern finds the smallest ------------------------------------
print("=" * 45)
print("THE SAME PATTERN FINDS THE SMALLEST")
print("=" * 45)

smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n

print("Smallest number :", smallest)
print("Largest number  :", largest)
print("Range           :", largest - smallest)
print()

# --- Why starting at 0 is a bug --------------------------------------------
print("=" * 45)
print("WHY STARTING AT 0 IS A BUG")
print("=" * 45)

negatives = [-5, -12, -3, -40, -8]
print("Test list (all negative) :", negatives)

# The wrong way
wrong = 0
for n in negatives:
    if n > wrong:
        wrong = n

# The right way
right = negatives[0]
for n in negatives:
    if n > right:
        right = n

print("   Starting at 0             -> answer", wrong, "  <- WRONG, 0 is not in the list")
print("   Starting at negatives[0]  -> answer", right, " <- correct")
