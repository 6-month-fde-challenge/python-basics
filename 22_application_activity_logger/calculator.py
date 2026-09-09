"""
calculator.py - the Calculate activity
======================================
Six operations, and the exception handling that keeps a bad sum from
taking the whole application down with it.

THE THREE THINGS THAT CAN GO WRONG, AND THEIR LEVELS
    the user types "abc"      ValueError       -> WARNING (their mistake)
    the user divides by zero  ZeroDivisionError-> ERROR   (op failed)
    anything else at all      Exception        -> CRITICAL(we did not
                                                  see this coming)

`log.exception(...)` is used in the last branch instead of `log.error`.
It logs at ERROR level AND appends the full traceback, which is the
difference between a log that says "something failed" and a log you can
actually debug from. Here it is wrapped by an explicit CRITICAL call so
the severity matches an unexpected failure.
"""
from logger_config import get_logger

log = get_logger("calculator")

# Menu choice -> (symbol, function). A dictionary replaces a long
# if/elif chain: adding an operation is one new line.
OPERATIONS = {
    "1": ("+", lambda a, b: a + b),
    "2": ("-", lambda a, b: a - b),
    "3": ("*", lambda a, b: a * b),
    "4": ("/", lambda a, b: a / b),
    "5": ("%", lambda a, b: a % b),
    "6": ("**", lambda a, b: a ** b),
}


def read_number(prompt):
    """
    Ask for a number until a valid one arrives.

    A ValueError here is the user's typo, not a fault - so it is WARNING,
    and the loop simply asks again.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            log.warning("Non-numeric input rejected: %r", raw)
            print("   Please type a number, for example 12 or 3.5")
        else:
            log.debug("Parsed %r as %s", raw, value)
            return value


def calculate(a, symbol, operation, b):
    """
    Apply one operation and return its result, or None if it failed.

    Returning None rather than raising means the menu keeps running: an
    error in one operation must not terminate the application.
    """
    log.debug("Calculating %s %s %s", a, symbol, b)
    try:
        result = operation(a, b)

    except ZeroDivisionError:
        # A real failure of this operation - the answer does not exist.
        log.error("Division by zero attempted: %s %s %s", a, symbol, b)
        print("   Cannot divide by zero.")
        return None

    except OverflowError:
        # 9e300 ** 5 - the maths is valid, the float cannot hold it.
        log.error("Result too large to represent: %s %s %s", a, symbol, b)
        print("   That result is too large for Python to store.")
        return None

    except Exception:
        # Nothing above matched, so this is a bug rather than bad input.
        log.critical("Unexpected failure in calculate()", exc_info=True)
        print("   Unexpected failure - the error has been logged.")
        return None

    else:
        # `else` runs only when NO exception was raised, which keeps the
        # success path visibly separate from the failure paths.
        log.info("Calculation completed: %s %s %s = %s", a, symbol, b, result)
        return result

    finally:
        # `finally` runs on every path - success, handled error, or an
        # exception on its way out. Good place for "the attempt ended".
        log.debug("calculate() finished for operator %r", symbol)


def run():
    """The Calculate activity as the menu sees it."""
    print()
    print("   OPERATIONS")
    for key, (symbol, _) in OPERATIONS.items():
        print(f"      {key}. {symbol}")

    choice = input("   Choose an operation : ").strip()
    if choice not in OPERATIONS:
        log.warning("Unknown operation choice: %r", choice)
        print("   That is not one of the operations.")
        return None

    symbol, operation = OPERATIONS[choice]
    a = read_number("   First number       : ")
    b = read_number("   Second number      : ")

    result = calculate(a, symbol, operation, b)
    if result is not None:
        print(f"   RESULT: {a} {symbol} {b} = {result}")
    return result
