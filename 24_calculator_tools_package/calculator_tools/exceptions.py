"""
calculator_tools.exceptions - the errors this package raises
============================================================
One base class and three specific ones. Deliberately small: exercises 23
and 25 each build a six-class hierarchy, and repeating that here would
teach nothing new. Four classes is enough to show the shape.

THE HIERARCHY
    Exception
     └── CalculatorError                 base - one except catches all
          ├── InvalidOperationError          the operation/unit is unknown
          ├── InvalidValueError              the value cannot be used
          └── DivisionByZeroError            dividing by zero

`InvalidOperationError` is the class the assignment names. It covers the
"unsupported operation" case in both senses the package needs it:

    calculate("nonsense", 2, 3)          -> unknown operator
    convert_length(5, "m", "parsecs")    -> unknown unit

WHY A CLASS AND NOT A MESSAGE
    `raise ValueError("bad operator")` works, and then every caller has
    to read the message string to find out what went wrong. A class
    carries that meaning in its TYPE, so code can branch on it - and the
    exception can hold structured fields (which operator, what was
    supported) instead of one flattened sentence.

WHY WRAP ZeroDivisionError AT ALL
    Python already raises ZeroDivisionError, so DivisionByZeroError may
    look redundant. It is not: it makes the package's errors ONE family.
    A caller writes `except CalculatorError` and is covered for every
    failure this package can produce, instead of that clause plus a
    separate `except ZeroDivisionError` that it has to remember exists.
    The original is kept on `.cause` so nothing is lost.
"""


class CalculatorError(Exception):
    """
    Base class for every error raised by calculator_tools.

    Subclassing this rather than Exception directly is what lets a caller
    write one `except CalculatorError` and still let a genuine bug - a
    typo in a variable name, say - travel up as the AttributeError it is.
    """

    def __init__(self, message, operation=None):
        # Passing the message up to Exception is what makes str(error)
        # and the traceback show something useful.
        super().__init__(message)
        self.message = message
        self.operation = operation      # which function was asked, if known

    def __str__(self):
        if self.operation:
            return f"{self.message} (in {self.operation})"
        return self.message


class InvalidOperationError(CalculatorError):
    """
    Raised when an operation or a unit is not one this package supports.

    This is the custom exception the assignment requires. It carries what
    WAS asked for and what IS supported, so the message can be helpful
    rather than just negative:

        InvalidOperationError: unsupported operation 'nonsense'
        (supported: add, divide, modulus, multiply, power, subtract)
    """

    def __init__(self, requested, supported=(), kind="operation",
                 operation=None):
        known = ", ".join(sorted(str(s) for s in supported))
        message = f"unsupported {kind} {requested!r}"
        if known:
            message += f" (supported: {known})"
        super().__init__(message, operation)
        self.requested = requested
        self.supported = tuple(supported)
        self.kind = kind


class InvalidValueError(CalculatorError):
    """
    Raised when a value cannot be used - wrong type, or out of domain.

    Covers two of the four cases the assignment lists, because from the
    caller's side they are the same problem:

        "twelve"          -> not a number at all      (incorrect type)
        -40 kelvin        -> a number, but impossible (invalid value)

    `.value` keeps the offending input and `.reason` says which of the
    two it was, so one class can report both without losing the
    distinction.
    """

    def __init__(self, value, reason="not a number", operation=None):
        super().__init__(f"invalid value {value!r}: {reason}", operation)
        self.value = value
        self.reason = reason


class DivisionByZeroError(CalculatorError):
    """
    Raised instead of letting a bare ZeroDivisionError escape.

    The original exception is kept on `.cause`, so the OS-level - here
    interpreter-level - detail is still available to anyone who wants it.
    Dropping it is the usual mistake when wrapping an exception: the new
    type is clearer and the reason disappears.
    """

    def __init__(self, message="cannot divide by zero", operation=None,
                 cause=None):
        super().__init__(message, operation)
        self.cause = cause
