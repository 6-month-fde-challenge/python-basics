"""
Question 8 - Count the Frequency of Every Character WITHOUT Counter
====================================================================
Concept: building a dictionary inside a loop.

THE PATTERN (this is the whole program):
    for each character:
        if we have seen it before -> add 1 to its count
        if it is brand new        -> start its count at 1

Example expected for "banana":
    b -> 1
    a -> 3
    n -> 2
"""

text = "banana"

print("Input string :", text)
print("Length       :", len(text))
print()

frequency = {}                    # empty dictionary: character -> how many times

print("Walking through the string one character at a time:")
for char in text:
    if char in frequency:         # already seen -> increase the count
        frequency[char] += 1
        print(f"   '{char}' seen again -> count is now {frequency[char]}")
    else:                         # first time -> create the key with value 1
        frequency[char] = 1
        print(f"   '{char}' is NEW      -> count starts at 1")

print()
print("=" * 30)
print("CHARACTER FREQUENCY")
print("=" * 30)
for char, count in frequency.items():
    print(f"   {char} -> {count}")

print()
print("As a dictionary :", frequency)
print("Unique characters:", len(frequency))
print()

# --- A second example with spaces and mixed case ---------------------------
print("=" * 45)
print("SECOND EXAMPLE - a full sentence")
print("=" * 45)

sentence = "Python Programming"
print("Input :", sentence)

freq2 = {}
for char in sentence:
    if char == " ":               # skip spaces so they do not clutter the report
        continue
    char = char.lower()           # treat 'P' and 'p' as the same character
    if char in freq2:
        freq2[char] += 1
    else:
        freq2[char] = 1

print("Result (spaces ignored, case ignored):")
for char, count in freq2.items():
    print(f"   {char} -> {count}")

# Which characters were repeated?
print()
print("Characters that appear more than once:")
for char, count in freq2.items():
    if count > 1:
        print(f"   {char} -> {count} times")
