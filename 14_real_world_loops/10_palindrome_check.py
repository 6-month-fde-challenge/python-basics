"""
Question 10 - Check Whether a String Is a Palindrome USING LOOPS
================================================================
A palindrome reads the same forwards and backwards: madam, level, racecar.

Concept: the TWO-POINTER technique.
    one pointer starts at the FRONT  (index 0)
    one pointer starts at the BACK   (index -1)
    compare them, then move both inwards
    the moment two characters differ -> NOT a palindrome, stop early

The shortcut  text == text[::-1]  is deliberately avoided - the point
here is to do the comparison character by character with a loop.
"""


def is_palindrome(text):
    """Return True if text is a palindrome, checked character by character."""
    # Clean the text first: ignore case and spaces
    cleaned = ""
    for char in text:
        if char != " ":
            cleaned += char.lower()

    left = 0                          # front pointer
    right = len(cleaned) - 1          # back pointer

    while left < right:               # stop when the pointers meet in the middle
        if cleaned[left] != cleaned[right]:
            return False              # mismatch found -> stop immediately
        left += 1                     # move front pointer forwards
        right -= 1                    # move back pointer backwards

    return True                       # never mismatched -> palindrome


# --- A detailed, step-by-step demonstration on one word --------------------
word = "madam"
print("=" * 50)
print("STEP BY STEP :", word)
print("=" * 50)

left = 0
right = len(word) - 1
result = True

while left < right:
    print(f"   compare '{word[left]}' (index {left}) with '{word[right]}' (index {right})", end="")
    if word[left] == word[right]:
        print("  -> match")
    else:
        print("  -> MISMATCH, stop here")
        result = False
        break
    left += 1
    right -= 1

print()
print(f"'{word}' is a palindrome :", result)
print()


# --- Test several words ----------------------------------------------------
print("=" * 50)
print("TESTING MANY WORDS")
print("=" * 50)

test_words = ["madam", "level", "racecar", "python", "banana", "noon", "hello"]

for w in test_words:
    if is_palindrome(w):
        print(f"   {w:<10} -> YES, it is a palindrome")
    else:
        print(f"   {w:<10} -> No, it is not")

print()

# --- Sentences work too, because spaces and case are ignored ---------------
print("=" * 50)
print("SENTENCES")
print("=" * 50)
sentences = ["Never odd or even", "Was it a car or a cat I saw", "Python is fun"]
for s in sentences:
    print(f"   '{s}'")
    print(f"      -> {'palindrome' if is_palindrome(s) else 'not a palindrome'}")

print()

# --- Try your own ----------------------------------------------------------
user_text = input("Enter a word or sentence to check : ")
if is_palindrome(user_text):
    print(f"'{user_text}' IS a palindrome.")
else:
    print(f"'{user_text}' is NOT a palindrome.")
