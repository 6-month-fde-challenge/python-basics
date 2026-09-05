"""
Question 7 - Accept 10 Numbers From the User and Store Them in a List
======================================================================
Concept: for loop with range() + input() + append().

range(10) produces 0,1,2...9 -> exactly 10 passes.
We display i+1 so the user sees "Number 1" instead of "Number 0".

input() ALWAYS returns a string, so int() is needed before the value
can be used in maths. A try/except keeps a typing mistake from
crashing the whole program.
"""

TOTAL = 10

print("=" * 45)
print(f"   ENTER {TOTAL} NUMBERS")
print("=" * 45)

numbers = []                      # start with an empty list

count = 0
while count < TOTAL:
    entry = input(f"Enter number {count + 1} of {TOTAL} : ")
    try:
        value = int(entry)
    except ValueError:
        print(f"   '{entry}' is not a whole number. Please try again.")
        continue                  # skip the rest and ask for this number again
    numbers.append(value)         # add the valid number to the list
    count += 1

print()
print("=" * 45)
print("RESULTS")
print("=" * 45)
print("Numbers you entered :", numbers)
print("How many stored     :", len(numbers))

# A few facts about the collected numbers, all found with loops
total = 0
largest = numbers[0]
smallest = numbers[0]
even_count = 0
odd_count = 0

for n in numbers:
    total += n
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Sum                 :", total)
print("Average             :", round(total / len(numbers), 2))
print("Largest             :", largest)
print("Smallest            :", smallest)
print("Even numbers        :", even_count)
print("Odd numbers         :", odd_count)
