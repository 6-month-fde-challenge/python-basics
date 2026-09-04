"""
Question 4 - Student Marks Analysis
===================================
Concept: multiple counters + if / elif / else.

Count how many students fall into each grade band:
    90 and above   -> Excellent
    75 to 89       -> Good
    50 to 74       -> Average
    below 50       -> Fail

WHY elif AND NOT SEPARATE ifs?
Once a mark matches a band, the remaining bands must NOT be tested.
elif stops the chain, so every student is counted EXACTLY ONCE.
"""

marks = [78, 92, 45, 67, 88, 53, 99]

print("Student marks :", marks)
print("Total students:", len(marks))
print()

# Four separate counters, all starting at 0
excellent = 0        # 90+
good = 0             # 75 - 89
average = 0          # 50 - 74
fail = 0             # below 50

print("Placing each student into a band:")
for mark in marks:
    if mark >= 90:
        excellent += 1
        band = "90+        (Excellent)"
    elif mark >= 75:                 # already known to be below 90
        good += 1
        band = "75-89      (Good)"
    elif mark >= 50:                 # already known to be below 75
        average += 1
        band = "50-74      (Average)"
    else:                            # everything left is below 50
        fail += 1
        band = "below 50   (Fail)"
    print(f"   {mark:>3} -> {band}")

print()
print("=" * 40)
print("MARKS ANALYSIS REPORT")
print("=" * 40)
print(f"90 and above : {excellent} student(s)")
print(f"75 to 89     : {good} student(s)")
print(f"50 to 74     : {average} student(s)")
print(f"Below 50     : {fail} student(s)")
print("-" * 40)
print(f"Total counted: {excellent + good + average + fail} of {len(marks)}")
print()

# A simple text bar chart so the distribution is visible
print("Distribution:")
print("  90+      |", "*" * excellent)
print("  75-89    |", "*" * good)
print("  50-74    |", "*" * average)
print("  below 50 |", "*" * fail)
