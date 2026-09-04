"""
Question 10 - A Function That Checks for a Palindrome
======================================================
A palindrome reads the same forwards and backwards: madam, level, racecar.

THE TECHNIQUE - TWO POINTERS
    one pointer starts at the FRONT (index 0)
    one starts at the BACK  (the last index)
    compare them, then move both inwards
    the first mismatch proves it is not a palindrome -> return False
    if they meet in the middle with no mismatch      -> return True

The comparison stops as soon as the pointers meet, so only half the
characters are ever compared.

CLEANING FIRST: spaces are removed and everything is lowered, so
"Never odd or even" is recognised as a palindrome.

The function RETURNS True or False rather than printing, so the caller
can use it in an if or to filter a list.
"""


def clean_text(text):
    """Return the text in lowercase with all spaces removed."""
    cleaned = ""
    for char in text:
        if char != " ":
            cleaned += char.lower()
    return cleaned


def is_palindrome(text):
    """Return True if the text reads the same forwards and backwards."""
    cleaned = clean_text(text)

    left = 0                           # front pointer
    right = len(cleaned) - 1           # back pointer

    while left < right:                # stop when they meet in the middle
        if cleaned[left] != cleaned[right]:
            return False               # mismatch -> not a palindrome
        left += 1
        right -= 1

    return True                        # never mismatched -> palindrome


print("=" * 55)
print("TESTING WORDS")
print("=" * 55)

words = ["madam", "level", "racecar", "noon", "python", "banana", "hello", "a", ""]

for word in words:
    if is_palindrome(word):
        print(f"   {repr(word):<12} -> YES, a palindrome")
    else:
        print(f"   {repr(word):<12} -> no")

print()
print("   A single character is always a palindrome, and so is an empty")
print("   string - the while loop never runs, so no mismatch is possible.")
print()

print("=" * 55)
print("SENTENCES (spaces and capitals ignored)")
print("=" * 55)

sentences = [
    "Never odd or even",
    "Was it a car or a cat I saw",
    "Madam In Eden Im Adam",
    "Python is fun",
]

for sentence in sentences:
    verdict = "palindrome" if is_palindrome(sentence) else "not a palindrome"
    print(f"   {sentence:<30} -> {verdict}")
    print(f"      cleaned to: {clean_text(sentence)}")

print()

print("=" * 55)
print("A VERSION THAT SHOWS ITS WORKING")
print("=" * 55)


def is_palindrome_verbose(text):
    """Return True if text is a palindrome, printing each comparison."""
    cleaned = clean_text(text)
    print(f"      cleaned text: '{cleaned}'")

    left = 0
    right = len(cleaned) - 1

    while left < right:
        print(f"      compare '{cleaned[left]}' (index {left}) "
              f"with '{cleaned[right]}' (index {right})", end="")
        if cleaned[left] != cleaned[right]:
            print("  -> MISMATCH, stop")
            return False
        print("  -> match")
        left += 1
        right -= 1

    print("      pointers met in the middle with no mismatch")
    return True


print("   is_palindrome_verbose('madam')")
print("   RESULT:", is_palindrome_verbose("madam"))
print()
print("   is_palindrome_verbose('python')")
print("   RESULT:", is_palindrome_verbose("python"))
print()
print("   Notice 'python' stops at the very first comparison - the two")
print("   pointers do not need to travel any further to know the answer.")
