"""
Question 9 - A Function That Counts the Vowels in a String
===========================================================
All the logic sits inside the function: the loop, the vowel test and
the counter.

    for char in text:              <- a string is iterable
        if char.lower() in "aeiou":
            count += 1

WHY .lower() MATTERS: 'A' and 'a' are different characters to Python.
Without lowering each character first, "APPLE" would report 0 vowels,
because the vowel string holds only lowercase letters.

The function RETURNS the count rather than printing it, so the caller
can add it up, compare it, or store it.
"""


def count_vowels(text):
    """Return the number of vowels in a string, ignoring case."""
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count


def list_vowels(text):
    """Return a list of the vowel characters found in a string."""
    vowels = "aeiou"
    found = []
    for char in text:
        if char.lower() in vowels:
            found.append(char)
    return found


print("=" * 55)
print("COUNTING VOWELS")
print("=" * 55)

tests = ["Programming", "Python", "APPLE", "rhythm", "AEIOU", "Hello World", ""]

for text in tests:
    print(f"   count_vowels({repr(text):<15}) = {count_vowels(text)}")

print()
print("   'rhythm' has 0 vowels. The empty string also gives 0.")
print("   'APPLE' gives 2 - proof that .lower() is doing its job.")
print()

print("=" * 55)
print("WHICH VOWELS WERE FOUND")
print("=" * 55)

for text in ["Programming", "Education", "Hello World"]:
    print(f"   {text:<15} -> {count_vowels(text)} vowels {list_vowels(text)}")

print()

print("=" * 55)
print("A VERSION THAT SHOWS ITS WORKING")
print("=" * 55)


def count_vowels_verbose(text):
    """Return the vowel count, printing the decision for each character."""
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
            print(f"      '{char}' -> VOWEL      (count = {count})")
        else:
            print(f"      '{char}' -> not a vowel")
    return count


print("   count_vowels_verbose('Python')")
print("   RESULT:", count_vowels_verbose("Python"))
print()

print("=" * 55)
print("WHY .lower() IS NEEDED")
print("=" * 55)


def count_vowels_broken(text):
    """Deliberately wrong: no .lower(), so uppercase vowels are missed."""
    count = 0
    for char in text:
        if char in "aeiou":
            count += 1
    return count


for text in ["APPLE", "Education", "AEIOU"]:
    print(f"   {text:<12} correct: {count_vowels(text)}   "
          f"without .lower(): {count_vowels_broken(text)}")
print()
print("   Uppercase vowels never match a lowercase vowel string.")
