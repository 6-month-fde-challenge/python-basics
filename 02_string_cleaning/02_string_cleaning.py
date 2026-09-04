"""
Exercise 02 - String Cleaning Challenge
=======================================
Concepts practised: strip(), lower(), upper(), title(), replace(),
                    startswith(), endswith(), count(), find(), split()

IMPORTANT IDEA: strings in Python are IMMUTABLE.
Every method below RETURNS A NEW STRING - the original `message` never changes.
That is why each result is stored in its own variable.
"""

# ---------------------------------------------------------------------------
# The original string (note the extra spaces at the start and the end)
# ---------------------------------------------------------------------------

message = "   Welcome To Python Programming Class   "

print("Original string :", repr(message))   # repr() shows the spaces clearly
print("Original length :", len(message))
print()


# ---------------------------------------------------------------------------
# 1. strip() - remove the extra spaces from both ends
# ---------------------------------------------------------------------------
cleaned = message.strip()
print("1. strip()      :", repr(cleaned))
print("   new length   :", len(cleaned))


# ---------------------------------------------------------------------------
# 2. lower() - convert everything to lowercase
# ---------------------------------------------------------------------------
lower_text = cleaned.lower()
print("2. lower()      :", lower_text)


# ---------------------------------------------------------------------------
# 3. upper() - convert everything to uppercase
# ---------------------------------------------------------------------------
upper_text = cleaned.upper()
print("3. upper()      :", upper_text)


# ---------------------------------------------------------------------------
# 4. title() - capitalise the first letter of every word
# ---------------------------------------------------------------------------
title_text = cleaned.title()
print("4. title()      :", title_text)


# ---------------------------------------------------------------------------
# 5. replace() - swap "Python" for "Advanced Python"
# ---------------------------------------------------------------------------
replaced_text = cleaned.replace("Python", "Advanced Python")
print("5. replace()    :", replaced_text)


# ---------------------------------------------------------------------------
# 6. startswith() - does the sentence begin with "Welcome"?
# ---------------------------------------------------------------------------
starts_with_welcome = cleaned.startswith("Welcome")
print("6. startswith('Welcome') :", starts_with_welcome)


# ---------------------------------------------------------------------------
# 7. endswith() - does the sentence end with "Class"?
# ---------------------------------------------------------------------------
ends_with_class = cleaned.endswith("Class")
print("7. endswith('Class')     :", ends_with_class)


# ---------------------------------------------------------------------------
# 8. count() - how many times does the letter "o" appear?
#    NOTE: count() is case sensitive, so "O" would be counted separately.
# ---------------------------------------------------------------------------
count_o = cleaned.count("o")
print("8. count('o')            :", count_o)


# ---------------------------------------------------------------------------
# 9. find() - at which index does the word "Programming" start?
#    find() returns -1 when the text is not present (it does NOT crash).
# ---------------------------------------------------------------------------
position = cleaned.find("Programming")
print("9. find('Programming')   :", position)
print("   find('Java') ->", cleaned.find("Java"), "(-1 means 'not found')")


# ---------------------------------------------------------------------------
# 10. split() - break the sentence into a list of words
#     With no argument it splits on whitespace.
# ---------------------------------------------------------------------------
words = cleaned.split()
print("10. split()              :", words)
print("    number of words      :", len(words))


# ---------------------------------------------------------------------------
# Proof that the original string was never modified
# ---------------------------------------------------------------------------
print()
print("Original is still :", repr(message))
