"""
main.py - a separate program that IMPORTS calculator_tools
==========================================================
main.py is not part of the package. It sits next to it and imports it,
exactly as any other program would. That line is the assignment:

    from calculator_tools import calculate, average

Everything below is a demonstration that the import worked and that the
package behaves - including when it is given nonsense.

    python main.py
"""

# The imports are part of the demonstration - three styles, on purpose.
import calculator_tools                                  # the package
from calculator_tools import arithmetic, converter, statistics   # its modules
from calculator_tools import average, calculate          # its functions

from calculator_tools.exceptions import CalculatorError

LINE = "=" * 62


def title(number, text):
    print()
    print(LINE)
    print(f"  {number}. {text}")
    print(LINE)


def show(call, value):
    print(f"    {call:<38} = {value:,.2f}".rstrip("0").rstrip("."))


# ---------------------------------------------------------------- 1

def demo_1_function_module_package():
    title(1, "Function, module, package, import")

    print("    The same function, three ways:")
    print()
    show("calculator_tools.arithmetic.add(2, 3)",
         calculator_tools.arithmetic.add(2, 3))
    show("arithmetic.add(2, 3)", arithmetic.add(2, 3))
    show("calculator_tools.add(2, 3)", calculator_tools.add(2, 3))

    print()
    print("    And what each name actually is:")
    print()
    print(f"      calculator_tools             {type(calculator_tools).__name__}"
          f"      the PACKAGE")
    print(f"      calculator_tools.arithmetic  {type(arithmetic).__name__}"
          f"      a MODULE in it")
    print(f"      arithmetic.add               "
          f"{type(arithmetic.add).__name__}    a FUNCTION in that")


# ---------------------------------------------------------------- 2

def demo_2_arithmetic_and_percentage():
    title(2, "Arithmetic and percentages")

    for symbol in ["+", "-", "*", "/", "%", "**"]:
        show(f"calculate({symbol!r}, 12, 4)", calculate(symbol, 12, 4))

    print()
    show("percentage(416, 500)", arithmetic.percentage(416, 500))
    show("percent_of(18, 1000)", arithmetic.percent_of(18, 1000))


# ---------------------------------------------------------------- 3

def demo_3_averages():
    title(3, "Averages")

    marks = [88, 92, 76, 65, 95]
    print(f"    marks = {marks}")
    print()
    show("total(marks)", statistics.total(marks))
    show("average(marks)", average(marks))


# ---------------------------------------------------------------- 4

def demo_4_conversion():
    title(4, "Temperature and unit conversion")

    show("convert_temperature(100, 'c', 'f')",
         converter.convert_temperature(100, "c", "f"))
    show("convert_temperature(0, 'c', 'f')",
         converter.convert_temperature(0, "c", "f"))
    show("convert_temperature(212, 'f', 'c')",
         converter.convert_temperature(212, "f", "c"))
    print("    0 C -> 32 F, so temperature needs an offset, not just a")
    print("    factor. That is why it is not in the unit table.")

    print()
    show("convert_length(5, 'km', 'mi')",
         converter.convert_length(5, "km", "mi"))
    show("convert_weight(70, 'kg', 'lb')",
         converter.convert_weight(70, "kg", "lb"))


# ---------------------------------------------------------------- 5

def demo_5_errors():
    title(5, "Error handling")

    cases = [
        ("divide by zero", lambda: calculate("/", 10, 0)),
        ("not a number", lambda: calculate("+", "twelve", 3)),
        ("unknown operation", lambda: calculate("nonsense", 1, 2)),
        ("unknown unit", lambda: converter.convert_length(5, "m", "parsecs")),
        ("below absolute zero",
         lambda: converter.convert_temperature(-300, "c", "f")),
        ("empty list", lambda: average([])),
    ]

    for label, call in cases:
        try:
            call()
        except CalculatorError as error:
            print(f"    {label:<22} {type(error).__name__}")
            print(f"    {'':<22}   {error}")

    print()
    print("    All six are subclasses of CalculatorError, so one clause")
    print("    catches every error this package can raise:")
    print()
    print("        except CalculatorError as error:")
    print("            print(error)")


def main():
    print()
    print(LINE)
    print("  EXERCISE 24 - calculator_tools")
    print("  A package, imported by a program that is not part of it")
    print(LINE)

    demo_1_function_module_package()
    demo_2_arithmetic_and_percentage()
    demo_3_averages()
    demo_4_conversion()
    demo_5_errors()

    print()
    print(LINE)
    print("  Every function above lives in calculator_tools/.")
    print("  This file only imported them and printed the results.")
    print(LINE)
    print()


if __name__ == "__main__":
    main()
