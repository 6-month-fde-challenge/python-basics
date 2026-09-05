# Exercise 16 - Loop Control

Intermediate loop control: `for`, `break`, `continue`, `for-else`, `range()`,
`enumerate()` and nested loops.

Every program is independently executable:

```bash
python 01_skip_divisible_by_5.py
```

or from the repo root:

```bash
python .\01_python_basics\16_loop_control\01_skip_divisible_by_5.py
```

---

## Questions and approach

### Q1 — Print 1–100, skipping multiples of 5 (`continue`)
**File:** `01_skip_divisible_by_5.py`

Loop over `range(1, 101)`. When `n % 5 == 0`, call `continue`, which abandons only
the current pass and jumps to the next number — the `print()` below it is never
reached for that value. 80 numbers print, 20 are skipped.

### Q2 — Stop at the first number divisible by both 7 and 11 (`break`)
**File:** `02_stop_at_7_and_11.py`

Same `range(1, 101)`, but the condition uses `and`: `n % 7 == 0 and n % 11 == 0`.
When it matches, `break` ends the whole loop immediately. The answer is **77**
(= 7 × 11), found after 77 checks — `break` saves the remaining 23.

**Contrast with Q1:** `continue` skips one item and keeps looping; `break` stops
the loop entirely.

### Q3 — Search a list using `for-else`
**File:** `03_search_for_else.py`

A `for` loop compares each element to the user's number. On a match it prints
`"Number Found"` and calls `break`. The `else` block attached to the `for` prints
`"Number Not Found"`.

**The rule:** a `for-else` block runs **only if the loop finished without hitting
`break`**. It does not mean "otherwise" — a better name would be "no-break". This
removes the need for a `found = False` flag variable.

### Q4 — Numbered names using `enumerate()`
**File:** `04_enumerate_names.py`

`enumerate(names, start=1)` yields `(index, value)` tuples, unpacked by the loop
into two variables. `start=1` is the key detail: `enumerate()` defaults to 0, but
the required output begins at `1 Aman`. The manual-counter alternative is shown
alongside for comparison.

### Q5 — Increasing star pattern
**File:** `05_increasing_star_pattern.py`

Nested loops. The outer loop controls the **rows**, the inner loop the **stars per
row**, and the inner loop's length depends on the outer counter — `range(row)`, so
row 3 prints 3 stars. `print("*", end="")` keeps the row on one line; a bare
`print()` ends it.

### Q6 — Decreasing star pattern
**File:** `06_decreasing_star_pattern.py`

Identical to Q5 except the outer loop counts **down**: `range(5, 0, -1)` → 5, 4, 3,
2, 1. The stop value is `0`, not `1`, because `range()` always excludes its stop —
using `range(5, 1, -1)` would lose the final row.

### Q7 — Multiplication tables 1–10
**File:** `07_multiplication_tables.py`

Two nested loops, both fixed at `range(1, 11)`. The outer picks the table, the
inner the row. The inner loop restarts completely on every outer pass, producing
10 × 10 = 100 multiplications. Also rendered as a 10×10 grid.

### Q8 — Numbers 1–200 divisible by both 3 and 5
**File:** `08_divisible_by_3_and_5.py`

One loop with a compound `and` condition. Both remainders must be zero, which makes
every match a multiple of 15 — **13 numbers**, from 15 to 195. The program also
counts the `or` case to show how different that question would be.

### Q9 — Unique elements without `set()`
**File:** `09_unique_without_set.py`

The "check before you add" pattern: build an empty list, then for each element
`if item not in unique: unique.append(item)`. Doing it manually rather than with
`set()` has a real advantage — it **preserves the original order**, which `set()`
does not.

### Q10 — Count positives, negatives and zeros
**File:** `10_count_pos_neg_zero.py`

Three counters with `if / elif / else`. The categories are mutually exclusive, so
`elif` guarantees each number is counted exactly once. **Zero needs its own
branch** — using `n >= 0` would wrongly classify it as positive, which the program
demonstrates side by side. Result: 4 positive, 3 negative, 1 zero.

### Q11 — Prime check using a loop
**File:** `11_prime_check.py`

Test every divisor from 2 upward; the first one that divides evenly proves the
number is not prime, so the loop stops there. If none is found, it is prime.

Two details: numbers below 2 are rejected up front (1 is **not** prime), and the
loop only runs to `int(n ** 0.5) + 1` — divisors come in pairs, so past the square
root the pairs just repeat in reverse.

### Q12 — All primes between 1 and 100
**File:** `12_primes_1_to_100.py`

Nested loops plus `for-else`: the outer loop walks the candidates, the inner loop
hunts for a divisor. If the inner loop `break`s, the `else` is skipped; if it
completes, the `else` runs and the number is recorded as prime. No flag variable
needed. Result: **25 primes**, from 2 to 97.

---

## Notes on the constraints

- No shortcut bypasses the technique being practised: Q9 does not use `set()`, and
  Q11/Q12 determine primality with an actual divisor loop.
- Q2 (`break`), Q1 (`continue`), Q3 (`for-else`), Q5/Q6/Q7/Q12 (nested loops) and
  Q4 (`enumerate`) each demonstrate their named feature directly.
- Programs 3 and 11 read one value from the keyboard; the rest run unattended.
