"""
Exercise 03 - Student Information String Challenge
==================================================
Concepts practised: indexing, negative indexing, slicing, reverse slicing,
                    upper(), lower(), title(), count(), find(), replace(), split()

KEY IDEA 1 - Indexing starts at 0.
             The first character is [0], the second is [1], and so on.
KEY IDEA 2 - Negative indexes count backwards from the end: [-1] is the last one.
KEY IDEA 3 - Slicing is [start : stop : step] and the STOP is EXCLUDED.
"""

# ---------------------------------------------------------------------------
# The string we will work on
# ---------------------------------------------------------------------------

student = "python programming for data science"


# ---------------------------------------------------------------------------
# 1. Print the complete string
# ---------------------------------------------------------------------------
print("1.  Complete string      :", student)
print("    Total characters     :", len(student))


# ---------------------------------------------------------------------------
# 2. First character -> index 0
# ---------------------------------------------------------------------------
print("2.  First character      :", student[0])


# ---------------------------------------------------------------------------
# 3. Last character -> index -1 (works no matter how long the string is)
# ---------------------------------------------------------------------------
print("3.  Last character       :", student[-1])


# ---------------------------------------------------------------------------
# 4. First 6 characters -> slice from 0 up to (but NOT including) 6
# ---------------------------------------------------------------------------
print("4.  First 6 characters   :", student[0:6])


# ---------------------------------------------------------------------------
# 5. Last 7 characters -> start 7 places from the end and run to the end
# ---------------------------------------------------------------------------
print("5.  Last 7 characters    :", student[-7:])


# ---------------------------------------------------------------------------
# 6. Reverse the string using slicing
#    [::-1] means "take every character, but step backwards by 1"
# ---------------------------------------------------------------------------
print("6.  Reversed string      :", student[::-1])


# ---------------------------------------------------------------------------
# 7. Uppercase
# ---------------------------------------------------------------------------
print("7.  Uppercase            :", student.upper())


# ---------------------------------------------------------------------------
# 8. Lowercase (already lowercase, so the output looks unchanged)
# ---------------------------------------------------------------------------
print("8.  Lowercase            :", student.lower())


# ---------------------------------------------------------------------------
# 9. Title case - first letter of every word capitalised
# ---------------------------------------------------------------------------
print("9.  Title case           :", student.title())


# ---------------------------------------------------------------------------
# 10. Count how many times "a" appears (count() is case sensitive)
# ---------------------------------------------------------------------------
print("10. Count of 'a'         :", student.count("a"))


# ---------------------------------------------------------------------------
# 11. Find the starting index of the word "programming"
#     find() returns -1 instead of crashing when the word is missing
# ---------------------------------------------------------------------------
print("11. Position of 'programming' :", student.find("programming"))


# ---------------------------------------------------------------------------
# 12. Replace "data science" with "artificial intelligence"
#     replace() returns a NEW string - `student` itself is not changed
# ---------------------------------------------------------------------------
updated = student.replace("data science", "artificial intelligence")
print("12. After replace()      :", updated)


# ---------------------------------------------------------------------------
# 13. Split the sentence into a list of individual words
# ---------------------------------------------------------------------------
words = student.split()
print("13. Split into words     :", words)
print("    Number of words      :", len(words))


# ---------------------------------------------------------------------------
# Proof that the original string is unchanged (strings are immutable)
# ---------------------------------------------------------------------------
print()
print("Original string is still :", student)
