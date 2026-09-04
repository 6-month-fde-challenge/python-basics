"""
Exercise 21 - Create a Student Marks List
=========================================
Concepts practised: indexing, negative indexing, slicing, len(), max(),
                    min(), sum(), sort(), append(), extend(), remove(),
                    count(), index()

IMPORTANT: list methods change the list IN PLACE and return None.
That is why we write   marks.sort()   and NOT   marks = marks.sort()
The second version would replace the whole list with None.

Because operations 9 to 13 modify the list, the marks are printed after
every change so you can watch the list evolve.
"""

# ---------------------------------------------------------------------------
# The original list
# ---------------------------------------------------------------------------

marks = [78, 85, 90, 67, 88, 92, 76]


# ---------------------------------------------------------------------------
# 1. Print the complete list
# ---------------------------------------------------------------------------
print("1.  Complete list        :", marks)
print()


# ---------------------------------------------------------------------------
# 2. First element -> index 0
# ---------------------------------------------------------------------------
print("2.  First element  [0]   :", marks[0])


# ---------------------------------------------------------------------------
# 3. Last element -> index -1 works no matter how long the list is
# ---------------------------------------------------------------------------
print("3.  Last element   [-1]  :", marks[-1])
print("    (marks[6] gives the same answer, but -1 keeps working")
print("     even after the list grows or shrinks.)")
print()


# ---------------------------------------------------------------------------
# 4. Elements from index 2 to 5
#    Slicing is [start:stop] and the STOP IS EXCLUDED.
#    To INCLUDE index 5, the stop must be 6.
# ---------------------------------------------------------------------------
print("4.  Index 2 to 5 [2:6]   :", marks[2:6], "<- indexes 2, 3, 4, 5")
print("    Compare [2:5]        :", marks[2:5], "<- stops BEFORE 5, so index 5 is missing")
print()
print("    Position map:")
for position, mark in enumerate(marks):
    marker = "  <- included in [2:6]" if 2 <= position <= 5 else ""
    print(f"       index {position} -> {mark}{marker}")
print()


# ---------------------------------------------------------------------------
# 5. Number of elements
# ---------------------------------------------------------------------------
print("5.  Number of elements   :", len(marks))


# ---------------------------------------------------------------------------
# 6, 7, 8. Maximum, minimum and total
# ---------------------------------------------------------------------------
print("6.  Maximum marks        :", max(marks))
print("7.  Minimum marks        :", min(marks))
print("8.  Total marks          :", sum(marks))
print("    Average              :", round(sum(marks) / len(marks), 2))
print()


# ===========================================================================
# FROM HERE ON THE LIST IS MODIFIED
# ===========================================================================

print("=" * 58)
print("OPERATIONS THAT CHANGE THE LIST")
print("=" * 58)
print("Before any changes :", marks)
print()


# ---------------------------------------------------------------------------
# 9. Sort in ascending order (smallest first) - changes the list in place
# ---------------------------------------------------------------------------
marks.sort()
print("9.  After sort()                 :", marks, "<- ascending")


# ---------------------------------------------------------------------------
# 10. Sort in descending order (largest first)
# ---------------------------------------------------------------------------
marks.sort(reverse=True)
print("10. After sort(reverse=True)     :", marks, "<- descending")
print()


# ---------------------------------------------------------------------------
# 11. Add 95 - append() adds ONE item to the end
# ---------------------------------------------------------------------------
marks.append(95)
print("11. After append(95)             :", marks)
print("    Length is now                :", len(marks))


# ---------------------------------------------------------------------------
# 12. Add [81, 84] - extend() adds EACH ITEM SEPARATELY
#     append([81, 84]) would put the LIST INSIDE the list as one item.
# ---------------------------------------------------------------------------
marks.extend([81, 84])
print("12. After extend([81, 84])       :", marks)
print("    Length is now                :", len(marks), "<- grew by 2, not by 1")
print()


# ---------------------------------------------------------------------------
# 13. Remove 67 - remove() deletes BY VALUE, not by position
#     Only the FIRST match is removed, and a missing value raises ValueError.
# ---------------------------------------------------------------------------
marks.remove(67)
print("13. After remove(67)             :", marks)
print("    Length is now                :", len(marks))
print()


# ---------------------------------------------------------------------------
# 14. Count how many times 90 occurs
# ---------------------------------------------------------------------------
print("14. Count of 90                  :", marks.count(90))


# ---------------------------------------------------------------------------
# 15. Find the index of 88
#     NOTE: this is its position in the CURRENT list. Sorting moved it -
#     88 was at index 4 in the original list.
# ---------------------------------------------------------------------------
print("15. Index of 88                  :", marks.index(88))
print("    (88 was at index 4 before the list was sorted.)")
print()


# ---------------------------------------------------------------------------
# The final list
# ---------------------------------------------------------------------------
print("=" * 58)
print("FINAL STATE")
print("=" * 58)
print("Final list    :", marks)
print("Length        :", len(marks))
print("Highest mark  :", max(marks))
print("Lowest mark   :", min(marks))
print("Total         :", sum(marks))
print("Average       :", round(sum(marks) / len(marks), 2))
print()


# ===========================================================================
# EXTRA - append() vs extend(), a common point of confusion
# ===========================================================================

print("=" * 58)
print("EXTRA : append() vs extend()")
print("=" * 58)

demo_append = [78, 85]
demo_extend = [78, 85]
new_marks = [81, 84]

demo_append.append(new_marks)     # adds the LIST as ONE item -> nested
demo_extend.extend(new_marks)     # adds each item SEPARATELY -> flat

print("Starting list        :", [78, 85])
print("append([81, 84]) ->", demo_append, "| length:", len(demo_append))
print("extend([81, 84]) ->", demo_extend, "| length:", len(demo_extend))
print()
print("append adds ONE item - here that item is a whole list, so you get")
print("a list nested inside a list. extend adds each item separately.")
print()

# ---------------------------------------------------------------------------
# EXTRA - sorted() returns a NEW list instead of changing the original
# ---------------------------------------------------------------------------
print("=" * 58)
print("EXTRA : sort() vs sorted()")
print("=" * 58)

original = [78, 85, 90, 67]
new_sorted = sorted(original)     # returns a new list, leaves original alone

print("original         :", original, "<- unchanged")
print("sorted(original) :", new_sorted, "<- a brand new sorted list")
print()
original.sort()                   # changes the original in place
print("after original.sort() :", original, "<- the original itself changed")
print()
print("Use sort()   when you want to reorder the list you have.")
print("Use sorted() when you need a sorted copy and must keep the original.")
