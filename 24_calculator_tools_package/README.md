# Exercise 24 - Build Your Own `calculator_tools` Python Package

Four words, one exercise: **function, module, package, import.**

```python
from calculator_tools import calculate, average, convert_temperature

calculate("+", 2, 3)                 #   5.0
average([88, 92, 76, 65, 95])        #  83.2
convert_temperature(100, "c", "f")   # 212.0
```

---

## Project objective

Exercises 22 and 23 were built from loose **modules** — several `.py` files in a folder,
importing each other by filename. This one builds a **package**: a folder with an
`__init__.py` that turns five files into one importable thing.

`main.py` is deliberately **outside** the package and imports it, the way any other
program would. That boundary is the exercise — `calculator_tools/` could be copied into
a different project unchanged.

It is also where exercise 20 ends up. That folder held `operations.py` with `add`,
`subtract`, `multiply`, `divide`, `power` and `modulus`, imported by one script next to
it. Same six functions, promoted:

```
20   one module,  imported by one script      "a module"
22   six modules, imported by main.py         "modules in an application"
24   a package,   imported by main.py         "a package"          <- here
25   a package,   doing irreversible work     "a package in anger"
```

---

## Project structure

```
24_calculator_tools_package/
├── README.md
├── main.py                     a separate program that IMPORTS the package
├── sample_output.txt           captured from a real run
├── packages.png
└── calculator_tools/           <- THE PACKAGE
    ├── __init__.py                 the front door: what the package offers
    ├── exceptions.py               4 error classes
    ├── arithmetic.py               6 operations + 2 percentage functions
    ├── statistics.py               total and average
    └── converter.py                temperature, length, weight
```

---

## How to execute the program

```bash
python main.py
```

or from the repo root:

```bash
python .\01_python_basics\24_calculator_tools_package\main.py
```

No installation is required — the package imports nothing outside itself.
**Requires Python 3.6+.** Verified on Python 3.12.10.

---

## Function, module, package, import

| Word | Example | What it is |
|---|---|---|
| **function** | `add(2, 3)` | one named block of code |
| **module** | `arithmetic.py` | one **file** of functions |
| **package** | `calculator_tools/` | a **folder** of modules, with an `__init__.py` |
| **import** | `from x import y` | the statement that finds one and names it |

`main.py` section 1 proves it rather than asserting it:

```
calculator_tools             module      the PACKAGE
calculator_tools.arithmetic  module      a MODULE in it
arithmetic.add               function    a FUNCTION in that
```

### Three routes to the same function

All three appear in `main.py`, and all three run identical code:

```python
import calculator_tools
calculator_tools.arithmetic.add(2, 3)          # package.module.function

from calculator_tools import arithmetic
arithmetic.add(2, 3)                           # module, then function

from calculator_tools import add
add(2, 3)                                      # re-exported by __init__.py
```

The third works **only** because `__init__.py` contains `from .arithmetic import add`.
That is what a front door is: a caller never has to know which module a function is in.

### The dot — relative imports

Every import *inside* the package starts with a dot:

```python
from .arithmetic import require_number     # "arithmetic, next to me"
```

Without it, Python searches `sys.path` and would not find a file sitting next to this
one.

**Import order is dependency order:** `exceptions.py` imports nothing of ours,
`arithmetic.py` imports `exceptions`, `statistics.py` and `converter.py` import
`arithmetic`, and `__init__.py` imports all four. Nothing imports upwards, so there are
no circular imports — the usual reason a package will not import at all.

### `__all__`

```python
__all__ = ["add", "subtract", ..., "convert_temperature", ...]
```

`from calculator_tools import *` imports exactly these. Being explicit makes the public
surface a **decision** rather than an accident of which names happen to exist.

---

## The `statistics.py` shadowing case

Python ships a `statistics` module. This package contains
`calculator_tools/statistics.py`. **Both exist at once and they do not clash**, because
a package is a namespace:

```python
import statistics                        # -> the standard library
from calculator_tools import statistics  # -> ours
from .statistics import average          # -> ours, from inside the package
```

In Python 3, `import statistics` always searches `sys.path`, so reaching a sibling file
needs the dot. That is why every import inside the package is relative.

| | Safe? | Why |
|---|---|---|
| `calculator_tools/statistics.py` | **yes** | inside a package; the dot reaches siblings |
| a loose `statistics.py` next to `main.py` | **no** | found first, breaks `import statistics` for the whole program |

Exercise 22 walked into the second case with a module called `logging.py`. Same trap.

---

## What the package provides

**Arithmetic** — `add`, `subtract`, `multiply`, `divide`, `modulus`, `power`, plus
`calculate(op, a, b)` which takes a name or a symbol:

```
calculate('+',  12, 4)  = 16        calculate('%',  12, 4) = 0
calculate('/',  12, 4)  = 3         calculate('**', 12, 4) = 20,736
```

`OPERATIONS` is a dictionary of name → function, and it is the **only** list of
supported operators — which keeps the error message correct when one is added.

**Percentages** — `percentage(416, 500)` → `83.2`, `percent_of(18, 1000)` → `180`.

**Averages** — `total` and `average`, which is what "average calculation" asks for.
Written with the accumulator pattern from exercise 18 rather than `sum()`, for the same
reason that exercise did it.

**Temperature** — `convert_temperature(value, from, to)` between C, F and K. Everything
routes through Celsius, so there are three ways in and three ways out instead of nine
formulas.

**Units** — `convert_length` and `convert_weight`, both one call into a shared
table-driven `convert()`.

### Why temperature is not in the unit table

| | Kind of conversion | Method |
|---|---|---|
| length, weight | **scale** | multiply by a factor |
| temperature | **scale *and* offset** | multiply, then add |

`0 °C` is not `0 °F`, so a factor alone turns 0 °C into 0 °F instead of 32 °F. Forcing
temperature into the factor table is the classic mistake here.

The table records how many **base** units each unit is worth — metres, grams — so every
conversion is two steps through the base:

```
5 km  ->  5000 m  ->  5000 / 1609.344  ->  3.11 mi
```

One number per unit instead of one per **pair** of units. Adding a unit is one new line.

---

## Error handling

Four classes:

```
Exception
 └── CalculatorError                 base - one except clause catches all
      ├── InvalidOperationError          the operation or unit is unknown
      ├── InvalidValueError              the value cannot be used
      └── DivisionByZeroError            dividing by zero
```

`InvalidOperationError` is the class the assignment names, and it covers "unsupported
operation" in both senses the package needs — an unknown operator and an unknown unit.
It carries what *was* asked and what *is* supported, so the message helps:

```
unsupported operation 'nonsense'
(supported: add, divide, modulus, multiply, power, subtract)
```

The six cases in `main.py` section 5, all caught by one `except CalculatorError`:

| Case | Raises |
|---|---|
| `calculate("/", 10, 0)` | `DivisionByZeroError` |
| `calculate("+", "twelve", 3)` | `InvalidValueError` — incorrect type |
| `calculate("nonsense", 1, 2)` | `InvalidOperationError` |
| `convert_length(5, "m", "parsecs")` | `InvalidOperationError` |
| `convert_temperature(-300, "c", "f")` | `InvalidValueError` — below absolute zero |
| `average([])` | `InvalidValueError` — empty list |

Three details worth pointing at:

- **`True` is rejected.** In Python `bool` subclasses `int`, so `float(True)` is `1.0`.
  A calculator that accepts `add(True, 5) == 6` is guessing, not validating — which is
  why the bool check comes *first*, before the `float()` attempt.
- **`0 ** -1` is a division by zero** in disguise, and does not raise on its own.
- **`average("123")` is refused.** A string is iterable, so without a check it would be
  read as the three numbers 1, 2 and 3.

### Raising, not returning `None`

Exercise 20's `operations.py` returned `None` when asked to divide by zero. This module
raises, because of what happens *next*:

```python
result = divide_returning_none(10, 0)   # -> None
print(result + 1)                       # TypeError, later, naming neither
                                        # the division nor the zero
```

`None` is a value, so the failure surfaces somewhere else entirely. That was fine for a
script that printed the answer; it is wrong for a library whose answer gets used.

---

## Verified run

`python main.py` produces five sections in 78 lines:

```
1. Function, module, package, import   three routes, all -> 5
2. Arithmetic and percentages          6 operations, 2 percentage functions
3. Averages                            total 416, average 83.2
4. Temperature and unit conversion     100 C -> 212 F, 5 km -> 3.11 mi
5. Error handling                       6 cases, all caught by one base class
```

---

## Concepts used

**Packages**
- `__init__.py`, and what it adds over a plain folder of modules
- Relative imports — `from .arithmetic import ...` — and why every internal import uses one
- Absolute imports in Python 3, and the `statistics.py` shadowing case
- `__all__` and `__version__`
- Re-exporting a package's public surface from its front door
- Dependency order as import order, so there are no circular imports
- The application (`main.py`) living outside the package it uses

**Custom exceptions**
- A base class, three subclasses under it
- `InvalidOperationError`, as the assignment requires
- Extra attributes on the exception (`.requested`, `.supported`, `.value`, `.reason`)
  instead of one flattened message string
- `raise ... from error` to keep the original, `from None` to hide a detail
- Wrapping `ZeroDivisionError` so the package's errors are one family

**Functions**
- `OPERATIONS` as a dictionary of name → function object, so `calculate()` is a lookup
  rather than an `if`/`elif` chain
- Validation extracted into `require_number()` and `clean()`, called at the top, so
  every function body below can be one line
- The accumulator pattern instead of `sum()`

---

## Learning / outcomes

1. **A package is a boundary, not a folder.** The useful question is not "how do I write
   `__init__.py`" but "what is inside the boundary and what is outside". `print()` is
   outside; arithmetic is inside.

2. **The dot is the difference between a module and a package.**
   `from .arithmetic import add` says "next to me"; `import arithmetic` says "somewhere
   on `sys.path`". Once that clicks, `statistics.py` shadowing a standard library module
   stops being frightening.

3. **`__init__.py` is an interface, not a formality.** An empty one works. A useful one
   lets a caller write `from calculator_tools import average` without knowing that
   `average` lives in `statistics.py` — and keep writing it after it moves.

4. **A library raises; an application catches.** `arithmetic.divide()` raises, `main.py`
   catches. Returning `None` from a library moves the error somewhere it cannot be
   explained.

5. **Validate once, at the edge.** `require_number()` runs before any arithmetic, so
   nothing below it can be reached with a string — which is what lets the function
   bodies be one line each.

### Challenges faced

- **`float(True)` is `1.0`.** The first `require_number()` accepted booleans, so
  `add(True, 5)` returned `6.0`. `bool` is a subclass of `int`, so every numeric check
  passes — the bool test has to come *first*, or it never runs.
- **`except ... as error` deletes its own name.** An earlier `main.py` recorded the
  exception type inside each handler and printed the message *after* the try/except, and
  got `UnboundLocalError`. Python 3 unbinds the name at the end of the except block, so
  anything wanted afterwards has to be copied out inside the handler.
- **`"123"` is a perfectly good iterable.** `average("123")` originally returned `2.0`,
  having read the string as 1, 2 and 3. `clean()` now rejects `str` first.
- **The first version was too big.** It had 36 functions across six modules — `mode`,
  `variance`, `standard_deviation`, `spread`, `median`, `minimum`, `maximum`,
  `floor_divide`, `percentage_change`, `apply_discount`, a data-size converter and a
  `__main__.py` with a `python -m` entry point. All of it worked and none of it was
  asked for, and it made the package take twenty minutes to explain instead of five.
  Cut to the five things the assignment actually names: arithmetic, percentage, average,
  temperature and unit conversion.

---

## YouTube demonstration link

<your-youtube-video-link>

---

## Submission links

- **GitHub Repository:** `<your-public-github-repository-link>`
- **YouTube Explanation:** `<your-youtube-video-link>`
