# Exercise 20 - Advanced Functions

`*args`, `**kwargs`, recursion, lambda functions, scope, and functions working
together.

## Project organisation

Twelve questions across thirteen files. Each program is self-contained and runs on
its own:

```bash
python 01_args_sum.py
```

or from the repo root:

```bash
python .\01_python_basics\20_advanced_functions\01_args_sum.py
```

The mini calculator (Q12) is deliberately split into **two** files, because it is
the one question with two distinct jobs:

| File | Responsibility |
|------|----------------|
| `operations.py` | The maths — `add`, `subtract`, `multiply`, `divide`, `power`, `modulus`. Pure functions: no input, no printing. |
| `12_mini_calculator.py` | The interface — menu, input validation, output. Imports `operations`. |

`python operations.py` runs a self-test of the maths alone; `python
12_mini_calculator.py` runs the calculator. That is what the `if __name__ ==
"__main__"` block at the bottom of each file controls.

---

## Questions and approach

### Q1 — Total of any number of values (`*args`)
**File:** `01_args_sum.py`

`*args` collects every extra positional argument into a **tuple**, so one function
handles `total(10, 20)` and `total(10, 20, 30, 40, 50)` alike. A `for` loop then
accumulates the values. Also shows `total(*prices)`, where the star **unpacks** an
existing list into separate arguments.

```
total(10, 20)             -> 30
total(10, 20, 30, 40, 50) -> 150
total()                   -> 0
```

### Q2 — Largest supplied number (`*args`)
**File:** `02_args_largest.py`

`*args` plus the champion pattern: assume `args[0]` is the winner, then replace it
whenever a bigger value appears. Starting from `args[0]` rather than `0` matters —
with all-negative inputs, starting at 0 returns 0, a value never passed in. An
empty call returns `None` rather than raising `IndexError`.

```
largest(10, 45, 3, 78, 22)  -> 78
largest(-5, -12, -3, -40)   -> -3
largest()                   -> None
```

### Q3 — `create_profile(**kwargs)`
**File:** `03_kwargs_profile.py`

`**kwargs` collects keyword arguments into a **dictionary**, so `.items()` walks the
supplied attributes. This suits a profile precisely because there is no fixed field
list — one user gives a phone number, another gives a course. Also demonstrates
`*args` and `**kwargs` in the same signature, and `create_profile(**details)`
unpacking a dictionary.

```
create_profile(name="Rahul", age=22)
   Name              : Rahul
   Age               : 22
```

### Q4 — A function that accepts another function
**File:** `04_function_as_argument.py`

Functions are **first-class objects** — they can be stored and passed like any
value. `calculate(add, 10, 20)` passes the function itself; note the **absence of
brackets**, since `add(10, 20)` would pass the number `30` instead. Also stores
functions in a list and a dictionary, and returns one from a function.

```
calculate(add, 10, 20)      -> 30
calculate(multiply, 10, 20) -> 200
```

### Q5 — Lambda for the square of a number
**File:** `05_lambda_square.py`

`square = lambda n: n ** 2`. A lambda holds **one expression** whose value is
returned automatically — no `return`, no loops, no multi-line blocks. `type()`
confirms a lambda and a `def` produce the same kind of object. Ends with a genuine
use case: `sorted(students, key=lambda pair: pair[1])`.

### Q6 — `lambda` with `map()`
**File:** `06_lambda_map.py`

`map()` **transforms** — one output per input, so the length never changes.
Demonstrates that the returned map object is **lazy** and is consumed after one
pass.

```
[1, 2, 3, 4, 5, 6]  ->  [1, 4, 9, 16, 25, 36]
```

### Q7 — `lambda` with `filter()`
**File:** `07_lambda_filter.py`

`filter()` **selects** — it keeps items whose predicate returns `True`, so the
output is usually shorter. Run side by side with `map()` on the same list to make
the contrast concrete.

```
[1..10]  --map(square)-->    10 items
[1..10]  --filter(even)-->    5 items  ->  [2, 4, 6, 8, 10]
```

### Q8 — Recursive factorial
**File:** `08_recursive_factorial.py`

Base case `n <= 1` returns 1; recursive case returns `n * factorial(n - 1)`.
Includes a **traced version** printing an indented call stack, and a demonstration
of `RecursionError` when the base case is removed.

```
5! = 120     (trace shows 5 calls down, then 1 -> 2 -> 6 -> 24 -> 120 back up)
```

### Q9 — Recursive sum 1 + 2 + … + n
**File:** `09_recursive_sum.py`

Structurally identical to Q8 — only the operator changes, from `*` to `+`. Traced,
and verified against both a loop and the formula `n(n+1)/2`.

```
sum_to(5) = 15
```

### Q10 — Recursive Fibonacci
**File:** `10_recursive_fibonacci.py`

Needs **two** base cases (`n == 0` and `n == 1`), because the recursive case reaches
back two steps. Makes **two** recursive calls per level, so the calls form a
branching tree rather than a line — and the same values are recomputed repeatedly.
The program counts the calls to show how badly this scales.

```
fib(10) = 55       177 calls
fib(20) = 6765     21,891 calls
fib(30) = 832040   2,692,537 calls
```

### Q11 — Local and global scope
**File:** `11_scope_demo.py`

Six demonstrations, each triggering the real behaviour rather than describing it:
reading a global works; a local dies with its function (`NameError`); assigning
inside a function creates a **new local** and leaves the global untouched; `global`
changes it for real; and reading a name before assigning it in the same function
raises `UnboundLocalError`.

```
counter before = 100  ->  assignment inside function  ->  still 100
counter before = 100  ->  with `global counter`       ->  now 555
```

### Q12 — Mini calculator
**Files:** `operations.py` + `12_mini_calculator.py`

Each operation is its own function in `operations.py`; `main()` in the calculator
drives a `while True` menu. Instead of an if/elif chain, a **dictionary maps each
menu choice to a function object** — the same idea as Q4, so adding an operation
means adding one dictionary entry.

Validated: non-numeric input, division by zero (the maths functions return `None`
and the menu reports it), and invalid menu choices.

```
1 -> 10, 20   ->  RESULT: 10.0 + 20.0 = 30.0
4 -> 10, 0    ->  ERROR: cannot use / with a second number of zero.
```

---

## Sample runs

```bash
python operations.py            # self-test of the maths module alone
python 12_mini_calculator.py    # the interactive calculator
python 08_recursive_factorial.py  # includes the full call-stack trace
```

or from the repo root:

```bash
python .\01_python_basics\20_advanced_functions\operations.py
python .\01_python_basics\20_advanced_functions\12_mini_calculator.py
python .\01_python_basics\20_advanced_functions\08_recursive_factorial.py
```
