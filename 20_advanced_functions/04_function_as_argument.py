"""
Question 4 - A Function That Accepts Another Function
======================================================
Concept: functions are FIRST-CLASS OBJECTS in Python.

That means a function can be stored in a variable, put in a list, and
passed to another function - exactly like an int or a string.

    calculate(add, 10, 20)

Notice there are NO BRACKETS after `add`. That is the whole idea:

    add      -> the function ITSELF (an object that can be passed around)
    add(2,3) -> CALLS the function and gives back the RESULT, 5

If you wrote calculate(add(10, 20), 10, 20) you would be passing the
number 30, not the function.

A function passed into another function is often called a CALLBACK.
"""


# --- The individual operations ---------------------------------------------

def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """Return a / b, or a message when b is zero."""
    if b == 0:
        return "cannot divide by zero"
    return a / b


# --- The function that accepts a function ----------------------------------

def calculate(operation, a, b):
    """
    Run whichever operation was handed in.

    `operation` holds a FUNCTION, so operation(a, b) calls it.
    """
    print(f"   operation received : {operation.__name__}")
    print(f"   type of operation  : {type(operation).__name__}")
    result = operation(a, b)               # the callback is called here
    return result


print("=" * 55)
print("PASSING A FUNCTION AS AN ARGUMENT")
print("=" * 55)

print("\ncalculate(add, 10, 20)")
print("   Result:", calculate(add, 10, 20))

print("\ncalculate(subtract, 10, 20)")
print("   Result:", calculate(subtract, 10, 20))

print("\ncalculate(multiply, 10, 20)")
print("   Result:", calculate(multiply, 10, 20))

print("\ncalculate(divide, 10, 20)")
print("   Result:", calculate(divide, 10, 20))

print("\ncalculate(divide, 10, 0)")
print("   Result:", calculate(divide, 10, 0))

print()

# --- The difference between a function and a function call -----------------
print("=" * 55)
print("add   vs   add(10, 20)")
print("=" * 55)
print("add          ->", add, "  <- the function object itself")
print("add(10, 20)  ->", add(10, 20), "  <- the result of calling it")
print("Brackets mean 'run it now'. No brackets means 'hand over the function'.")
print()

# --- Storing functions in a list and a dictionary --------------------------
print("=" * 55)
print("FUNCTIONS STORED IN A LIST AND A DICTIONARY")
print("=" * 55)

operations = [add, subtract, multiply, divide]
print("A list of functions:")
for operation in operations:
    print(f"   {operation.__name__:<10} (10, 20) = {operation(10, 20)}")

print()
operation_map = {"+": add, "-": subtract, "*": multiply, "/": divide}
print("A dictionary mapping symbols to functions:")
for symbol, operation in operation_map.items():
    print(f"   10 {symbol} 20 = {operation(10, 20)}")

print()
print("This dictionary trick replaces a long if/elif chain - the calculator")
print("in Question 12 uses exactly this idea.")
print()

# --- A function can also RETURN a function ---------------------------------
print("=" * 55)
print("A FUNCTION CAN ALSO RETURN A FUNCTION")
print("=" * 55)


def pick_operation(symbol):
    """Return the function matching the symbol."""
    if symbol == "+":
        return add
    if symbol == "-":
        return subtract
    return multiply


chosen = pick_operation("+")               # `chosen` now HOLDS the add function
print("chosen = pick_operation('+')")
print("chosen is now:", chosen.__name__)
print("chosen(7, 3) =", chosen(7, 3))
