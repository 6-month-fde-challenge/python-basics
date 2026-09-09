"""
calculator_tools - a reusable calculator package
================================================
THIS FILE IS WHAT MAKES THE FOLDER A PACKAGE. Without it,
`calculator_tools/` is just a directory that happens to hold .py files.

THE FOUR WORDS THIS EXERCISE IS ABOUT

    function   add(2, 3)              one named block of code
    module     arithmetic.py          one FILE of functions
    package    calculator_tools/      a FOLDER of modules, with this file
    import     the statement that finds one of them and names it

THREE WAYS TO REACH THE SAME FUNCTION

    import calculator_tools
    calculator_tools.arithmetic.add(2, 3)        # package.module.function

    from calculator_tools import arithmetic
    arithmetic.add(2, 3)                         # module, then function

    from calculator_tools import add
    add(2, 3)                                    # re-exported below

THE DOT
    Every import inside this package starts with a dot:

        from .arithmetic import add       # "arithmetic, next to me"

    Without it, Python searches sys.path instead and would not find a
    file sitting next to this one.

IMPORT ORDER IS DEPENDENCY ORDER
    exceptions.py  imports nothing of ours
    arithmetic.py  imports exceptions
    statistics.py  imports arithmetic
    converter.py   imports arithmetic
    __init__.py    imports all four

    Nothing imports upwards, so there are no circular imports.

USAGE
    from calculator_tools import calculate, average, convert_temperature

    calculate("+", 2, 3)                  ->   5.0
    average([88, 92, 76])                 ->  85.33
    convert_temperature(100, "c", "f")    -> 212.0
"""
from .arithmetic import (
    OPERATIONS,
    add,
    calculate,
    divide,
    modulus,
    multiply,
    percent_of,
    percentage,
    power,
    subtract,
)
from .converter import convert_length, convert_temperature, convert_weight
from .exceptions import (
    CalculatorError,
    DivisionByZeroError,
    InvalidOperationError,
    InvalidValueError,
)
from .statistics import average, total

__version__ = "1.0"

# `from calculator_tools import *` imports exactly these names. Being
# explicit makes the public surface a decision rather than an accident.
__all__ = [
    "add", "subtract", "multiply", "divide", "modulus", "power",
    "calculate", "OPERATIONS",
    "percentage", "percent_of",
    "total", "average",
    "convert_temperature", "convert_length", "convert_weight",
    "CalculatorError", "InvalidOperationError", "InvalidValueError",
    "DivisionByZeroError",
]
