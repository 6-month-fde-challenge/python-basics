"""
Question 7 - Multiplication Tables from 1 to 10 Using Nested Loops
===================================================================
Concept: nested loops where BOTH loops have a fixed length.

    OUTER loop -> which TABLE we are printing   (1 to 10)
    INNER loop -> which ROW of that table       (1 to 10)

The inner loop runs completely for EVERY single pass of the outer loop,
so the total number of lines is 10 x 10 = 100 multiplications.

This is the defining feature of a nested loop: the inner loop restarts
from the beginning each time the outer loop advances by one.
"""

print("=" * 50)
print("MULTIPLICATION TABLES 1 TO 10")
print("=" * 50)

for table in range(1, 11):                # outer: table number
    print()
    print(f"--- Table of {table} ---")
    for row in range(1, 11):              # inner: 1 to 10, restarts every table
        print(f"   {table} x {row:>2} = {table * row}")

print()
print("Total multiplications performed :", 10 * 10)
print()


# --- The same data as a compact grid ---------------------------------------
print("=" * 50)
print("THE SAME TABLES AS A GRID")
print("=" * 50)

# Column headings
print("     ", end="")
for col in range(1, 11):
    print(f"{col:>5}", end="")
print()
print("     " + "-" * 50)

# One row per table
for table in range(1, 11):
    print(f"{table:>3} |", end="")
    for col in range(1, 11):
        print(f"{table * col:>5}", end="")
    print()

print()
print("Reading the grid: find the row, then the column, and the")
print("cell where they meet is the answer - row 7, column 8 is", 7 * 8)
