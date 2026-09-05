"""
Question 5 - A Lambda Function for the Square of a Number
==========================================================
A LAMBDA is a small function written on one line, with no name and no
`return` keyword.

    def square(n):              square = lambda n: n ** 2
        return n ** 2

Both create a function that takes n and gives back n squared.

THE STRUCTURE:
    lambda  n  :  n ** 2
      |     |        |
      |     |        the expression - its value is returned automatically
      |     the parameter(s)
      the keyword

LIMITS OF A LAMBDA
   - it can hold only ONE expression, not several statements
   - it cannot contain a loop or a multi-line if block
   - there is no `return` - the expression's value IS the return value

WHEN TO USE ONE: when a tiny function is needed for a moment, usually as
an argument to map(), filter() or sorted(). For anything longer, `def` is
clearer and can carry a docstring.
"""

# --- The lambda ------------------------------------------------------------
square = lambda n: n ** 2

print("=" * 55)
print("A LAMBDA FOR SQUARING")
print("=" * 55)
print("square = lambda n: n ** 2")
print()
print("square(5)  =", square(5))
print("square(9)  =", square(9))
print("square(12) =", square(12))
print("square(-4) =", square(-4), " <- a negative squared is positive")
print("square(0)  =", square(0))
print()


# --- The equivalent def ----------------------------------------------------
def square_def(n):
    """Return n squared."""
    return n ** 2


print("=" * 55)
print("THE SAME THING WRITTEN WITH def")
print("=" * 55)
print("square(7)     =", square(7))
print("square_def(7) =", square_def(7))
print("Identical results:", square(7) == square_def(7))
print()
print("type(square)     =", type(square).__name__)
print("type(square_def) =", type(square_def).__name__)
print("Both are functions - a lambda is not a different kind of thing.")
print()

# --- A table of squares ----------------------------------------------------
print("=" * 55)
print("SQUARES FROM 1 TO 10")
print("=" * 55)
for n in range(1, 11):
    print(f"   {n:>3} squared = {square(n)}")
print()

# --- Lambdas with more than one parameter ----------------------------------
print("=" * 55)
print("LAMBDAS CAN TAKE MORE THAN ONE PARAMETER")
print("=" * 55)

add = lambda a, b: a + b
cube = lambda n: n ** 3
is_even = lambda n: n % 2 == 0
bigger = lambda a, b: a if a > b else b

print("add(10, 20)    =", add(10, 20))
print("cube(3)        =", cube(3))
print("is_even(8)     =", is_even(8))
print("is_even(7)     =", is_even(7))
print("bigger(15, 42) =", bigger(15, 42))
print()

# --- Where lambdas are genuinely useful ------------------------------------
print("=" * 55)
print("WHERE A LAMBDA IS ACTUALLY WORTH USING")
print("=" * 55)

students = [("Rahul", 78), ("Priya", 92), ("Aman", 65), ("Sneha", 88)]
print("Students        :", students)

by_marks = sorted(students, key=lambda pair: pair[1], reverse=True)
print("Sorted by marks :", by_marks)
print()
print("The lambda tells sorted() WHICH part of each tuple to sort on.")
print("Writing a whole def for that one line would be heavier than needed.")
