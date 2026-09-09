"""
calculator_tools.arithmetic - the operations, and percentages
=============================================================
Where exercise 20's `operations.py` ended up: the same six functions,
now inside a package.

One difference worth noticing. That version returned None when asked to
divide by zero; this one raises. None is a value, so `divide(10, 0) + 1`
would fail later, somewhere else, naming neither the division nor the
zero. Raising puts the error where the mistake is.
"""
from .exceptions import DivisionByZeroError, InvalidOperationError, \
    InvalidValueError


def require_number(value, operation=None):
    """
    Return `value` as a float, or raise InvalidValueError.

    The bool check comes first on purpose: in Python `bool` is a
    subclass of `int`, so float(True) is 1.0 and a calculator that
    accepts add(True, 5) == 6 is guessing, not validating.
    """
    if isinstance(value, bool):
        raise InvalidValueError(value, "a boolean is not a number", operation)

    try:
        return float(value)
    except (TypeError, ValueError):
        # float("abc") raises ValueError; float(None) raises TypeError.
        raise InvalidValueError(value, "not a number", operation) from None


def add(a, b):
    """Return a + b."""
    return require_number(a, "add") + require_number(b, "add")


def subtract(a, b):
    """Return a - b."""
    return require_number(a, "subtract") - require_number(b, "subtract")


def multiply(a, b):
    """Return a * b."""
    return require_number(a, "multiply") * require_number(b, "multiply")


def divide(a, b):
    """Return a / b, or raise DivisionByZeroError."""
    a = require_number(a, "divide")
    b = require_number(b, "divide")

    try:
        return a / b
    except ZeroDivisionError as error:
        # Re-raised as one of ours, so a caller's `except CalculatorError`
        # covers this too. The original is kept on .cause.
        raise DivisionByZeroError(f"cannot divide {a:g} by zero",
                                  "divide", error) from error


def modulus(a, b):
    """Return the remainder of a / b."""
    a = require_number(a, "modulus")
    b = require_number(b, "modulus")

    try:
        return a % b
    except ZeroDivisionError as error:
        raise DivisionByZeroError("cannot take a remainder modulo zero",
                                  "modulus", error) from error


def power(a, b):
    """Return a to the power of b."""
    a = require_number(a, "power")
    b = require_number(b, "power")

    if a == 0 and b < 0:
        # 0 ** -1 is 1/0 - a division by zero in disguise.
        raise DivisionByZeroError("0 to a negative power is 1/0", "power")

    return a ** b


# Name -> function. This dictionary is also the only list of supported
# operations, so the error message below cannot go out of date.
OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "modulus": modulus,
    "power": power,
}

SYMBOLS = {"+": "add", "-": "subtract", "*": "multiply",
           "/": "divide", "%": "modulus", "**": "power"}


def calculate(operation, a, b):
    """
    Apply an operation chosen by name or symbol: calculate("+", 2, 3).

    An unknown operation is not a bad value and not a division by zero -
    it is a request the package cannot honour, so it gets its own class.
    """
    key = SYMBOLS.get(operation, operation)

    if key not in OPERATIONS:
        raise InvalidOperationError(operation, sorted(OPERATIONS),
                                    "operation", "calculate")

    # Functions are objects, so this looks one up and calls it instead
    # of routing through a long if/elif chain.
    return OPERATIONS[key](a, b)


def percentage(part, whole):
    """Return what percent `part` is of `whole`. percentage(45, 60) -> 75.0"""
    part = require_number(part, "percentage")
    whole = require_number(whole, "percentage")

    if whole == 0:
        raise DivisionByZeroError("a percentage of zero is undefined",
                                  "percentage")
    return (part / whole) * 100


def percent_of(percent, value):
    """Return `percent` percent of `value`. percent_of(18, 1000) -> 180.0"""
    percent = require_number(percent, "percent_of")
    value = require_number(value, "percent_of")
    return (percent / 100) * value
