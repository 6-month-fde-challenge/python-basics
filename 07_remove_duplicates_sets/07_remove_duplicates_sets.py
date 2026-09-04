"""
Exercise 07 - Remove Duplicate Data Using Sets
==============================================
Concepts practised: set(), list(), len(), duplicate removal, set operations

CONSTRAINT: no loops. set() does all the work in a single step.

THE CORE IDEA
-------------
A SET is an unordered collection that CANNOT contain duplicates.
So converting a list to a set is the fastest way to remove duplicates -
you do not have to compare anything yourself, Python does it for you.
"""

# ===========================================================================
# EXAMPLE 1 - DUPLICATE NUMBERS
# ===========================================================================

numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60]


# ---------------------------------------------------------------------------
# 1. Print the original list
# ---------------------------------------------------------------------------
print("1. Original list        :", numbers)


# ---------------------------------------------------------------------------
# 2. Convert the list into a set - duplicates vanish automatically
# ---------------------------------------------------------------------------
unique_set = set(numbers)
print("2. Converted to a set   :", unique_set)
print("   Type                 :", type(unique_set))


# ---------------------------------------------------------------------------
# 3. Observe WHICH duplicates disappeared
#    Each of these appeared twice in the list, so one copy of each was dropped.
# ---------------------------------------------------------------------------
print("3. Duplicates in the original list:")
print("   10 appeared", numbers.count(10), "times -> kept once")
print("   20 appeared", numbers.count(20), "times -> kept once")
print("   30 appeared", numbers.count(30), "times -> kept once")
print("   40 appeared", numbers.count(40), "time  -> unchanged")
print("   50 appeared", numbers.count(50), "time  -> unchanged")
print("   60 appeared", numbers.count(60), "time  -> unchanged")
print("   3 extra copies were removed in total.")


# ---------------------------------------------------------------------------
# 4. Convert the set back into a list
#    We usually convert back because lists are ordered and can be indexed.
# ---------------------------------------------------------------------------
unique_list = list(unique_set)
print("4. Back to a list       :", unique_list)
print("   Type                 :", type(unique_list))
print("   Sorted neatly        :", sorted(unique_set), "<- sorted() fixes the lost order")


# ---------------------------------------------------------------------------
# 5 & 6. Count the original elements vs the unique elements
# ---------------------------------------------------------------------------
print("5. Original element count :", len(numbers))
print("6. Unique element count   :", len(unique_set))
print("   Duplicates removed     :", len(numbers) - len(unique_set))


# ===========================================================================
# EXAMPLE 2 - DUPLICATE STUDENT NAMES
# ===========================================================================

print()
print("=" * 60)
print("EXAMPLE 2 : DUPLICATE STUDENT NAMES")
print("=" * 60)

students = ["Rahul", "Priya", "Aman", "Priya", "Sneha", "Rahul", "Aman", "Kiran", "Priya"]

print("Original attendance list :", students)
print("Total entries            :", len(students))

unique_students = set(students)
print("After set() conversion   :", unique_students)
print("Unique students          :", len(unique_students))
print("Duplicate entries removed:", len(students) - len(unique_students))

# Back to a clean, alphabetically ordered list
final_student_list = sorted(unique_students)
print("Final clean name list    :", final_student_list)

# Which names were repeated? (still no loops)
print()
print("How many times each name appeared:")
print("   Rahul :", students.count("Rahul"))
print("   Priya :", students.count("Priya"))
print("   Aman  :", students.count("Aman"))
print("   Sneha :", students.count("Sneha"))
print("   Kiran :", students.count("Kiran"))


# ===========================================================================
# WHY SETS ARE USEFUL WITH DUPLICATE DATA
# ===========================================================================

print()
print("=" * 60)
print("WHY SETS ARE USEFUL")
print("=" * 60)

# Reason 1 - one line of code instead of manual comparison
print("1. ONE LINE: set(numbers) removes every duplicate. No loops, no if-checks.")

# Reason 2 - membership testing is extremely fast
print("2. FAST SEARCH: 'is Priya present?' ->", "Priya" in unique_students)
print("   A set finds this instantly using hashing; a long list must scan item by item.")

# Reason 3 - built-in comparison tools that lists do not have
morning_batch = {"Rahul", "Priya", "Aman"}
evening_batch = {"Priya", "Kiran", "Sneha"}
print("3. COMPARISON TOOLS a list cannot do so easily:")
print("   morning batch        :", morning_batch)
print("   evening batch        :", evening_batch)
print("   in BOTH  (intersection) :", morning_batch & evening_batch)
print("   in EITHER (union)       :", morning_batch | evening_batch)
print("   morning ONLY (difference):", morning_batch - evening_batch)

# The trade-off - what you give up
print()
print("THE TRADE-OFF - what a set costs you:")
print("   a) ORDER IS LOST     : original", numbers, "-> set", unique_set)
print("   b) NO INDEXING       : unique_set[0] would raise a TypeError")
print("   c) COUNTS ARE LOST   : you can no longer tell 20 appeared twice")
print("   Fix: keep the original list too, then use sorted(set(...)) when you")
print("   need clean, unique, ordered data.")
