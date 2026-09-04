"""
Question 1 - Total of Any Number of Values Using *args
=======================================================
Concept: *args = "any number of positional arguments".

A normal function has a fixed number of parameters:
    def add(a, b):        <- exactly two, always

*args removes that limit. Python collects every extra positional
argument into a TUPLE named args:

    def total(*args):
        args is (10, 20, 30)   when called as total(10, 20, 30)

THE STAR IS THE FEATURE, NOT THE NAME. Writing *numbers works exactly
the same way. "args" is only a naming convention.

Because args is a tuple, a plain for loop walks through it.
"""


def total(*args):
    """Return the total of every value passed in."""
    print("   Inside the function, args =", args)
    print("   Type of args              =", type(args).__name__)
    print("   Number of values received =", len(args))

    running = 0
    for value in args:
        running += value
    return running


print("=" * 55)
print("*args ACCEPTS ANY NUMBER OF VALUES")
print("=" * 55)

print("\ntotal(10, 20)")
print("   Result:", total(10, 20))

print("\ntotal(10, 20, 30, 40, 50)")
print("   Result:", total(10, 20, 30, 40, 50))

print("\ntotal(5)")
print("   Result:", total(5))

print("\ntotal()   <- no arguments at all")
print("   Result:", total())
print("   An empty tuple gives 0, because the loop never runs.")

print()

# --- Mixing a normal parameter with *args ----------------------------------
print("=" * 55)
print("A NORMAL PARAMETER PLUS *args")
print("=" * 55)


def total_with_label(label, *args):
    """The first argument fills `label`; everything after it goes into args."""
    running = 0
    for value in args:
        running += value
    return label + " = " + str(running)


print(total_with_label("Cart total", 250, 100, 75))
print(total_with_label("Marks total", 88, 92, 79, 95))
print("The first value always fills `label`. *args must come LAST.")
print()

# --- Unpacking an existing list into *args ---------------------------------
print("=" * 55)
print("PASSING A LIST INTO *args WITH THE STAR OPERATOR")
print("=" * 55)

prices = [199, 499, 89, 1250]
print("prices =", prices)
print("total(prices)   -> would send ONE argument (the whole list) and fail on +")
print("total(*prices)  -> the star UNPACKS the list into separate arguments")
print("   Result:", total(*prices))
