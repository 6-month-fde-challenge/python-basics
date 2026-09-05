# Exercise 19 - Function Fundamentals

Reusable programming using custom functions, arguments, parameters, return values,
scope and default arguments.

Twelve independent programs. Each runs on its own:

```bash
python 01_add.py
```

or from the repo root:

```bash
python .\01_python_basics\19_function_fundamentals\01_add.py
```

**Every function here has a docstring** — 34 functions, verified.
All problem-solving logic lives **inside** the functions; the code outside only
supplies test values and displays what comes back.

Most files also include a `_verbose` variant of the main function that prints its
working step by step, so the logic is visible while it runs.

---

## Questions and approach

### Q1 — `def add(a, b)`
**File:** `01_add.py`

The vocabulary in four lines: **definition**, **docstring**, **return**, **call**.
`a` and `b` are **parameters** (the placeholders in the definition); `10` and `20`
are **arguments** (the actual values at call time). Shows the returned value being
stored, reused in more maths, and nested inside itself.

```
add(10, 20)                  -> 30
add(add(1, 2), add(3, 4))    -> 10
```

### Q2 — Four arithmetic functions
**File:** `02_arithmetic_functions.py`

One function per operation — each takes two parameters and **returns**. None of
them print, because printing is the caller's decision. `divide()` guards against a
zero divisor and returns a message instead of raising `ZeroDivisionError`.

```
add(20, 4) = 24    subtract(20, 4) = 16
multiply(20, 4) = 80    divide(20, 4) = 5.0    divide(20, 0) = Error: cannot divide by zero
```

### Q3 — Even or odd
**File:** `03_even_or_odd.py`

Two versions, because they return different **kinds** of answer:
`check_even_odd()` returns a **string** for displaying; `is_even()` returns a
**boolean** for deciding. The boolean version is then used to split a list — which
a string version could not do cleanly.

```
check_even_odd(10) -> Even     is_even(10) -> True
```

### Q4 — Largest of three without `max()`
**File:** `04_largest_of_three.py`

Two approaches: direct `if/elif` comparison, and the **champion pattern** (assume
the first wins, then challenge it). The champion pattern is preferred because it
scales to any number of values unchanged. Starting from `a` rather than `0` is what
makes the all-negative case work.

```
largest_of_three(10, 25, 7)   -> 25
largest_of_three(-5, -12, -3) -> -3
```

### Q5 — Factorial
**File:** `05_factorial.py`

Accumulator inside the function, starting at **1, not 0** — multiplying by zero
destroys everything. Handles `0!` (defined as 1) and negatives (returns `None`).
The program runs the buggy zero-start version to show 5! coming out as 0.

```
5! = 120     0! = 1     factorial(-5) = None
```

### Q6 — Prime check
**File:** `06_prime_check.py`

Returns a **boolean**. Rejects anything below 2 up front (1 is not prime), then
tests divisors while `divisor * divisor <= number` — divisors come in pairs, so
past the square root the same pairs just repeat. The boolean return is then used to
collect all 25 primes below 100.

```
is_prime(29) -> True     is_prime(91) -> False  (91 = 7 x 13)
```

### Q7 — `calculate_discount(price, discount=10)`
**File:** `07_calculate_discount.py`

`price` is required; `discount` has a **default**, so supplying it is optional.
Parameters with defaults must come **after** those without, or Python cannot tell
which slot a lone argument fills. The same call is shown four ways — fully
positional, mixed, fully keyword, and with the keywords reordered.

```
calculate_discount(1000)      -> 900.0   (default 10% used)
calculate_discount(1000, 25)  -> 750.0   (default overridden)
calculate_discount()          -> TypeError: price is required
```

### Q8 — Sum a list without `sum()`
**File:** `08_list_sum.py`

Accumulator declared **outside** the loop — inside, it would reset every pass. An
empty list correctly returns 0 because the loop body never runs. `list_average()`
then **calls** `list_sum()` rather than repeating the loop, which is the whole point
of writing functions.

```
list_sum([10, 20, 30, 40, 50]) -> 150     list_sum([]) -> 0
```

### Q9 — Count vowels
**File:** `09_count_vowels.py`

Loops the string character by character. `char.lower()` is essential — the program
runs a version without it to show `"APPLE"` reporting **0** vowels instead of 2.

```
count_vowels("Programming") -> 3      count_vowels("rhythm") -> 0
```

### Q10 — Palindrome check
**File:** `10_palindrome.py`

**Two-pointer** technique: one index at the front, one at the back, moving inward
until they meet. The first mismatch returns `False` immediately, so only half the
characters are ever compared. A helper `clean_text()` strips spaces and lowercases,
so sentences work too.

```
is_palindrome("madam")             -> True
is_palindrome("Never odd or even") -> True
is_palindrome("python")            -> False  (fails on the first comparison)
```

### Q11 — Student profile, positional and keyword arguments
**File:** `11_student_profile.py`

Returns a formatted profile string, called four ways: all positional, all keyword,
keywords in a scrambled order, and mixed. The sharpest demonstration is the
**swapped positional call** — `student_profile(22, "Rahul", "Python")` raises **no
error at all** and silently produces `22 (Rahul) is studying Python.` Keyword
arguments make that mistake impossible.

### Q12 — `print()` versus `return`
**File:** `12_print_vs_return.py`

Six demonstrations of why `return` matters:

1. On screen both look identical — both display 30.
2. Capturing the result reveals the truth: the printing function gives back
   **`None`**, of type `NoneType`.
3. `add_and_return(10, 20) * 2` works; doubling the printed one raises `TypeError`.
4. Returned values can be **chained**; printed ones cannot.
5. A shopping cart: the returning version adds up to a total, the printing version
   cannot.
6. `return` also **exits the function immediately**, so `check_age()` needs no
   `elif`.

```
printed  = add_and_print(10, 20)   -> None   (type NoneType)
returned = add_and_return(10, 20)  -> 30     (type int)
```

---

## Notes on the constraints

- The problem-solving logic is **inside** the functions. Code at module level only
  calls them and prints results.
- Every function has a docstring (34 in total).
- Q4 solves the problem without `max()`, and Q8 without `sum()`. `sum()` appears
  once at the end of Q8 purely to print a `match: True` verification line.
- All twelve programs run without user input, so they can be demonstrated
  straight through.
