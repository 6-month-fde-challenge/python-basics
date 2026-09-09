"""
calculator_tools.statistics - the average of a list of numbers
==============================================================
The assignment asks for average calculation, so that is what is here.
Written with the accumulator pattern from exercise 18 rather than sum(),
for the same reason that exercise did it: the point is to see the loop.

THIS FILE SHARES ITS NAME WITH A STANDARD LIBRARY MODULE - ON PURPOSE.
Python ships `statistics`. This is `calculator_tools/statistics.py`.
Both exist and they do not clash, because a package is a namespace:

    import statistics                        -> the standard library
    from calculator_tools import statistics  -> this file
    from .statistics import average          -> this file, from inside

In Python 3 a plain `import x` always searches sys.path, so reaching a
file next to you needs the dot. That is why every import in this package
is relative - and it is only safe because this is a package. A loose
statistics.py sitting next to main.py would be found first and would
break `import statistics` for the whole program.
"""
from .arithmetic import require_number
from .exceptions import DivisionByZeroError, InvalidValueError


def clean(values, operation=None):
    """
    Check a list and return it as a list of floats.

    Done once, here, so every function below can assume it is looking
    at numbers.
    """
    if isinstance(values, str):
        # "123" is iterable, so without this a string would be read as
        # the three numbers 1, 2 and 3.
        raise InvalidValueError(values, "a string is not a list of numbers",
                                operation)

    numbers = [require_number(item, operation) for item in values]

    if not numbers:
        raise InvalidValueError(values, "the list is empty", operation)

    return numbers


def total(values):
    """Return the sum, using the accumulator pattern."""
    running = 0.0
    for number in clean(values, "total"):
        running += number
    return running


def average(values):
    """Return the mean. An empty list is refused by clean()."""
    numbers = clean(values, "average")

    if not numbers:
        raise DivisionByZeroError("cannot average an empty list", "average")
    return total(numbers) / len(numbers)
