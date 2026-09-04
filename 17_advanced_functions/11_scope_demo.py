"""
Question 11 - Local and Global Variable Scope
==============================================
SCOPE is the part of a program where a variable can be seen.

    GLOBAL - created outside every function; visible everywhere
    LOCAL  - created inside a function; visible ONLY inside that function
             and destroyed the moment the function finishes

THE RULE PYTHON FOLLOWS WHEN READING A NAME (the LEGB rule):
    Local      -> is it defined in this function?
    Enclosing  -> is it in a surrounding function?
    Global     -> is it at the top level of the file?
    Built-in   -> is it a Python built-in like len or print?
The first match wins.

THE RULE WHEN ASSIGNING IS DIFFERENT AND CATCHES EVERYONE:
Assigning to a name inside a function makes it LOCAL by default, even if
a global of the same name exists. The `global` keyword is how you say
"no, I mean the outer one".
"""

# A GLOBAL variable - defined outside every function
counter = 100
message = "I am global"

print("=" * 60)
print("1. READING A GLOBAL FROM INSIDE A FUNCTION - allowed")
print("=" * 60)


def read_global():
    """Reading a global needs no special keyword."""
    print("   Inside the function, message =", message)


print("   Outside the function, message =", message)
read_global()
print("   Reading works because Python looks outward when a name is not local.")
print()


print("=" * 60)
print("2. A LOCAL VARIABLE CANNOT BE SEEN FROM OUTSIDE")
print("=" * 60)


def make_local():
    """Create a variable that exists only while this function runs."""
    local_message = "I am local"
    print("   Inside the function, local_message =", local_message)


make_local()
try:
    print(local_message)
except NameError as error:
    print("   Outside the function -> NameError:", error)
    print("   The variable was destroyed when the function finished.")
print()


print("=" * 60)
print("3. ASSIGNING INSIDE A FUNCTION CREATES A **NEW LOCAL**")
print("=" * 60)


def try_to_change():
    """This does NOT change the global - it makes a local of the same name."""
    counter = 999                      # a brand new LOCAL named counter
    print("   Inside the function, counter =", counter)


print("   Before calling      :", counter)
try_to_change()
print("   After calling       :", counter, " <- unchanged!")
print("   The function built its own local `counter` and threw it away.")
print("   This is called SHADOWING - the local hides the global by name only.")
print()


print("=" * 60)
print("4. THE `global` KEYWORD ACTUALLY CHANGES THE GLOBAL")
print("=" * 60)


def really_change():
    """`global` tells Python to use the outer variable, not make a new one."""
    global counter
    counter = 555
    print("   Inside the function, counter =", counter)


print("   Before calling      :", counter)
really_change()
print("   After calling       :", counter, " <- changed for real")
print()


print("=" * 60)
print("5. THE CLASSIC ERROR - READING BEFORE ASSIGNING")
print("=" * 60)

total = 50


def broken():
    """Looks like it reads the global, but the assignment makes it local."""
    print(total)                       # error happens here
    total = total + 1


try:
    broken()
except UnboundLocalError as error:
    print("   UnboundLocalError:", error)
    print()
    print("   WHY: Python scans the whole function BEFORE running it. It sees")
    print("   `total = ...` on the last line, decides total is LOCAL for the")
    print("   entire function, and then the print on line 1 asks for a local")
    print("   that has not been given a value yet.")
    print("   THE FIX: add `global total` as the first line of the function.")
print()


print("=" * 60)
print("6. A PRACTICAL EXAMPLE - A RUNNING SCORE")
print("=" * 60)

score = 0                              # global game score


def add_points(points):
    """Add to the global score."""
    global score
    score += points
    print(f"   +{points} points -> score is now {score}")


def preview_points(points):
    """Calculate a hypothetical score WITHOUT touching the global."""
    new_score = score + points         # a local; the global is only read
    print(f"   If we added {points}, the score would be {new_score}")
    return new_score


print("   Starting score:", score)
add_points(10)
add_points(25)
preview_points(100)
print("   Actual score after the preview:", score, " <- the preview changed nothing")
print()


print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
   READING  a global inside a function      -> always allowed
   ASSIGNING to a name inside a function    -> creates a LOCAL by default
   `global name`                            -> assignment affects the global
   A local variable                         -> dies when the function ends

   GOOD PRACTICE: prefer passing values in as arguments and returning
   results, rather than reaching out to globals. Globals can be changed
   from anywhere, which makes bugs hard to find. `global` is used here to
   demonstrate the concept, not because it is the best design.
""")
