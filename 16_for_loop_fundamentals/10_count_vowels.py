"""
Question 10 - Count the Vowels in a User-Provided String
=========================================================
Concept: looping over a STRING character by character.

A string is ITERABLE - a for loop walks through it one character at a
time, so no index or range() is needed:

    for char in text:      -> gives 'P', 'y', 't', 'h', 'o', 'n' ...

WHY .lower() MATTERS: 'A' and 'a' are different characters to Python.
Without lowering the text first, "APPLE" would report 0 vowels because
the vowel list holds only lowercase letters.

Sample input : Programming
Sample output: 3 vowels (o, a, i)
"""

VOWELS = "aeiou"

print("=" * 50)
print("VOWEL COUNTER")
print("=" * 50)

text = input("Enter a string : ")

count = 0
found = []

print()
print("Checking each character:")
for char in text:
    if char.lower() in VOWELS:        # lower() so 'A' matches 'a'
        count += 1
        found.append(char)
        print(f"   '{char}' -> VOWEL     (count is now {count})")
    else:
        print(f"   '{char}' -> not a vowel")

print()
print("=" * 50)
print("RESULT")
print("=" * 50)
print("Input string   :", text)
print("Total characters:", len(text))
print("VOWEL COUNT    :", count)
print("Vowels found   :", found)
print("Consonants etc :", len(text) - count)
print()

# --- How many of each vowel ------------------------------------------------
print("Breakdown by vowel:")
for vowel in VOWELS:
    vowel_total = 0
    for char in text:
        if char.lower() == vowel:
            vowel_total += 1
    print(f"   {vowel} -> {vowel_total}")

print()

# --- Why .lower() is needed ------------------------------------------------
print("=" * 50)
print("WHY .lower() IS NEEDED")
print("=" * 50)

sample = "APPLE"
with_lower = 0
without_lower = 0

for char in sample:
    if char.lower() in VOWELS:
        with_lower += 1
    if char in VOWELS:                # no .lower() - the wrong way
        without_lower += 1

print(f"Testing '{sample}':")
print("   with .lower()    ->", with_lower, "vowels (correct: A and E)")
print("   without .lower() ->", without_lower, "vowels (wrong - uppercase never matches)")
