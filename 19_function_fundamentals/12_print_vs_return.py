"""
Question 12 - print() versus return
====================================
This is the single most important idea about functions, and the one most
often confused.

    print()  SHOWS a value to the person watching the screen.
             The program itself cannot use what was printed.

    return   HANDS a value back to the code that called the function.
             The program CAN use it - store it, calculate with it, pass it on.

A function with no `return` statement automatically returns None. So a
printing function LOOKS like it works, right up to the moment you try to
use its answer.

RULE OF THUMB: a function should RETURN its result and let the caller
decide whether to print it. That is what keeps a function reusable.
"""


def add_and_print(a, b):
    """Print the sum of two numbers. Returns nothing."""
    print("      The sum is", a + b)


def add_and_return(a, b):
    """Return the sum of two numbers."""
    return a + b


print("=" * 60)
print("1. ON SCREEN THEY LOOK IDENTICAL")
print("=" * 60)

print("   add_and_print(10, 20)")
add_and_print(10, 20)

print("   print(add_and_return(10, 20))")
print("      The sum is", add_and_return(10, 20))
print()
print("   Both display 30, so far with no visible difference.")
print()

print("=" * 60)
print("2. THE DIFFERENCE APPEARS WHEN YOU CAPTURE THE RESULT")
print("=" * 60)

printed = add_and_print(10, 20)
returned = add_and_return(10, 20)

print("   value from add_and_print  ->", printed, "  <- None! Nothing came back.")
print("   value from add_and_return ->", returned, "    <- the real number")
print()
print("   type of the first  :", type(printed).__name__)
print("   type of the second :", type(returned).__name__)
print()

print("=" * 60)
print("3. ONLY A RETURNED VALUE CAN BE USED")
print("=" * 60)

print("   Doubling the returned value:", add_and_return(10, 20) * 2)

try:
    doubled = add_and_print(10, 20) * 2
except TypeError as error:
    print("   Doubling the printed value -> TypeError:", error)
    print("   None cannot be multiplied. The 30 was shown, then lost forever.")
print()

print("=" * 60)
print("4. RETURNED VALUES CAN BE CHAINED")
print("=" * 60)

print("   add_and_return(add_and_return(1, 2), add_and_return(3, 4))")
print("   =", add_and_return(add_and_return(1, 2), add_and_return(3, 4)))
print()
print("   The same nesting with add_and_print would fail, because each")
print("   inner call hands back None instead of a number.")
print()

print("=" * 60)
print("5. A REAL EXAMPLE - WHY IT ACTUALLY MATTERS")
print("=" * 60)


def line_total_print(quantity, unit_price):
    """Print the total for one cart line. Returns nothing."""
    print("      Line total:", quantity * unit_price)


def line_total_return(quantity, unit_price):
    """Return the total for one cart line."""
    return quantity * unit_price


cart = [(2, 250), (1, 1200), (3, 99)]

print("   Using the RETURNING version, the lines can be added up:")
cart_total = 0
for quantity, price in cart:
    line = line_total_return(quantity, price)
    print("      " + str(quantity) + " x " + str(price) + " = " + str(line))
    cart_total += line
print("      CART TOTAL =", cart_total)
print()

print("   Using the PRINTING version, each line appears but nothing adds up:")
for quantity, price in cart:
    line_total_print(quantity, price)
print("      CART TOTAL = impossible - every call returned None")
print()

print("=" * 60)
print("6. return ALSO ENDS THE FUNCTION IMMEDIATELY")
print("=" * 60)


def check_age(age):
    """Return an age category. Lines after a matching return never run."""
    if age < 0:
        return "Invalid age"
    if age < 18:
        return "Minor"
    if age < 60:
        return "Adult"
    return "Senior"


for age in [-5, 10, 25, 70]:
    print("   check_age(" + str(age).rjust(3) + ") ->", check_age(age))

print()
print("   As soon as one return runs, the function stops - so no elif is")
print("   needed here. That early exit is a second job return quietly does.")
print()

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
   print()  -> shows a value to a human. The program cannot reuse it,
               and the function itself gives back None.

   return   -> hands a value back to the calling code, which can store it,
               calculate with it, or pass it to another function. It also
               ends the function on the spot.

   WRITE FUNCTIONS THAT RETURN, and let the caller decide what to print.
   A function that only prints can be used in exactly one way. A function
   that returns can be used in any way the caller needs.
""")
