"""
Exercise 05 - Nested List Challenge
===================================
Concepts practised: nested lists, double indexing [row][column],
                    item assignment, append()

CONSTRAINT: no loops. Every value is reached by direct indexing.

HOW NESTED INDEXING WORKS
-------------------------
`students` is a LIST OF LISTS - think of it as a table.

                   [0]        [1]              [2]
                   name       age              course
students[0]  ->   "Rahul"      21             "Python"
students[1]  ->   "Priya"      22             "Data Science"
students[2]  ->   "Aman"       20             "Machine Learning"

The FIRST index picks the ROW (which student).
The SECOND index picks the COLUMN (which detail of that student).
So students[1][2] means: row 1 -> Priya, then item 2 -> "Data Science".
"""

# ---------------------------------------------------------------------------
# Create the nested list
# ---------------------------------------------------------------------------

students = [
    ["Rahul", 21, "Python"],
    ["Priya", 22, "Data Science"],
    ["Aman", 20, "Machine Learning"]
]


# ---------------------------------------------------------------------------
# 1. Print the complete list
# ---------------------------------------------------------------------------
print("1. Complete nested list :")
print("  ", students)
print("   Number of students   :", len(students))
print()


# ---------------------------------------------------------------------------
# 2. Rahul's name -> row 0, item 0
# ---------------------------------------------------------------------------
print("2. Rahul's name         :", students[0][0])


# ---------------------------------------------------------------------------
# 3. Priya's age -> row 1, item 1
# ---------------------------------------------------------------------------
print("3. Priya's age          :", students[1][1])


# ---------------------------------------------------------------------------
# 4. Aman's course -> row 2, item 2
# ---------------------------------------------------------------------------
print("4. Aman's course        :", students[2][2])


# ---------------------------------------------------------------------------
# 5. Priya's COMPLETE record -> only ONE index, so we get the whole inner list
# ---------------------------------------------------------------------------
print("5. Priya's full record  :", students[1])
print("   Type of students[1]  :", type(students[1]), "<- still a list")
print("   Type of students[1][0]:", type(students[1][0]), "<- now a string")
print()


# ---------------------------------------------------------------------------
# 6. Change Rahul's course to "AI"
#    Lists are MUTABLE, so we can assign straight into a position.
# ---------------------------------------------------------------------------
print("6. Rahul's course before:", students[0][2])
students[0][2] = "AI"
print("   Rahul's course after :", students[0][2])
print()


# ---------------------------------------------------------------------------
# 7. Add another student record manually using append()
#    append() adds ONE new item - here that item is a whole list (a new row).
# ---------------------------------------------------------------------------
students.append(["Sneha", 23, "Web Development"])
print("7. New student added    :", students[3])
print("   Students count now   :", len(students))
print()


# ---------------------------------------------------------------------------
# 8. Print the updated nested list
# ---------------------------------------------------------------------------
print("8. Updated nested list  :")
print("  ", students)
print()

# Printed row by row (still no loops - just four direct index lookups)
print("   Row 0 :", students[0])
print("   Row 1 :", students[1])
print("   Row 2 :", students[2])
print("   Row 3 :", students[3])


# ---------------------------------------------------------------------------
# EXTRA - negative indexing works exactly the same way on nested lists
# ---------------------------------------------------------------------------
print()
print("EXTRA (negative indexing):")
print("   Last student record  :", students[-1])
print("   Last student's course:", students[-1][-1])
