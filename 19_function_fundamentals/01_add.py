"""
Question 1 - def add(a, b)
===========================
THE VOCABULARY, all visible in these few lines:

    def add(a, b):            <- FUNCTION DEFINITION
        (docstring here)      <- DOCSTRING (describes what it does)
        return a + b          <- RETURN statement (sends a value back)

    add(10, 20)               <- FUNCTION CALL

    a and b   are PARAMETERS - the names in the definition
    10 and 20 are ARGUMENTS  - the actual values passed in at call time

A PARAMETER is the placeholder; an ARGUMENT is what fills it.
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


print("=" * 50)
print("THE add() FUNCTION")
print("=" * 50)

print("add(10, 20)      =", add(10, 20))
print("add(5, 7)        =", add(5, 7))
print("add(-3, 8)       =", add(-3, 8))
print("add(2.5, 1.5)    =", add(2.5, 1.5))
print("add(100, 0)      =", add(100, 0))
print()

# --- The value comes back, so it can be used elsewhere ---------------------
print("=" * 50)
print("THE RETURNED VALUE CAN BE USED LIKE ANY OTHER VALUE")
print("=" * 50)

result = add(10, 20)
print("Stored in a variable :", result)
print("Used in more maths   :", add(10, 20) * 2)
print("Nested inside itself :", add(add(1, 2), add(3, 4)), " <- (1+2) + (3+4)")
print("Used in a condition  :", "big" if add(50, 60) > 100 else "small")
print()

# --- Parameters versus arguments -------------------------------------------
print("=" * 50)
print("PARAMETER vs ARGUMENT")
print("=" * 50)
print("def add(a, b)   -> 'a' and 'b' are PARAMETERS (the placeholders)")
print("add(10, 20)     -> 10 and 20 are ARGUMENTS  (the real values)")
print("On this call, a becomes 10 and b becomes 20.")
print()
print("The docstring is readable from code too:")
print("   add.__doc__ ->", add.__doc__)
