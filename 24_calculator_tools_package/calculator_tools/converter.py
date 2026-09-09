"""
calculator_tools.converter - temperature and unit conversion
=============================================================
Temperature is not like the others, and that is the interesting part.

    length, weight    a SCALE change.  1 km = 1000 m, so multiply.
    temperature       a scale AND an OFFSET.  0 C is not 0 F, so
                      multiplying alone gives 0 F instead of 32 F.

That is why temperature gets its own function and the units share a
table.
"""
from .arithmetic import require_number
from .exceptions import InvalidOperationError, InvalidValueError

SCALES = {"c": -273.15, "f": -459.67, "k": 0.0}     # the coldest each can go


def convert_temperature(value, from_scale, to_scale):
    """
    Convert between Celsius, Fahrenheit and Kelvin.

    Everything routes through Celsius, so there are three ways in and
    three ways out instead of nine separate formulas.
    """
    number = require_number(value, "convert_temperature")

    source = str(from_scale).strip().lower()[:1]
    target = str(to_scale).strip().lower()[:1]

    for scale in (source, target):
        if scale not in SCALES:
            raise InvalidOperationError(scale, sorted(SCALES),
                                        "temperature scale",
                                        "convert_temperature")

    if number < SCALES[source]:
        raise InvalidValueError(number, "below absolute zero",
                                "convert_temperature")

    # step 1: into Celsius
    if source == "f":
        celsius = (number - 32) * 5 / 9
    elif source == "k":
        celsius = number - 273.15
    else:
        celsius = number

    # step 2: out of Celsius
    if target == "f":
        return celsius * 9 / 5 + 32
    if target == "k":
        return celsius + 273.15
    return celsius


# unit -> how many BASE units it is worth (metres, then grams).
# One number per unit, not one per PAIR of units, so adding a unit is
# one new line rather than a whole new row and column.
LENGTH = {"cm": 0.01, "m": 1.0, "km": 1000.0, "in": 0.0254,
          "ft": 0.3048, "mi": 1609.344}
WEIGHT = {"g": 1.0, "kg": 1000.0, "lb": 453.59237, "oz": 28.349523125}

UNITS = {"length": LENGTH, "weight": WEIGHT}


def convert(value, from_unit, to_unit, category):
    """
    Convert between two units of the same category.

    Two steps through the base unit is the whole implementation:
        metres = value * LENGTH[from_unit]
        result = metres / LENGTH[to_unit]
    """
    if category not in UNITS:
        raise InvalidOperationError(category, sorted(UNITS), "category",
                                    "convert")

    table = UNITS[category]
    number = require_number(value, f"convert_{category}")

    source = str(from_unit).strip().lower()
    target = str(to_unit).strip().lower()

    for unit in (source, target):
        if unit not in table:
            raise InvalidOperationError(unit, sorted(table),
                                        f"{category} unit",
                                        f"convert_{category}")

    return number * table[source] / table[target]


def convert_length(value, from_unit, to_unit):
    """Convert between cm, m, km, in, ft and mi."""
    return convert(value, from_unit, to_unit, "length")


def convert_weight(value, from_unit, to_unit):
    """Convert between g, kg, lb and oz."""
    return convert(value, from_unit, to_unit, "weight")
