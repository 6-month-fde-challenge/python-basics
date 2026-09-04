# Exercise 14 - Real-World Loops

Applying loops to realistic data-processing and problem-solving scenarios.

Every program is **independently executable**. Run any one on its own:

```bash
python 01_total_transactions.py
```

or from the repo root:

```bash
python .\01_python_basics\14_real_world_loops\01_total_transactions.py
```

**Requires Python 3.6+** (f-strings). No external packages needed.

---

## Programs at a glance

| # | File | Problem | Loop technique |
|---|------|---------|----------------|
| 1 | `01_total_transactions.py` | Total transaction value without `sum()` | Accumulator |
| 2 | `02_highest_lowest_transaction.py` | Highest & lowest without `max()`/`min()` | Champion tracking |
| 3 | `03_average_temperature.py` | Average temperature | Accumulator + division |
| 4 | `04_marks_analysis.py` | Count students per grade band | Multiple counters + `if`/`elif` |
| 5 | `05_login_system.py` | Login, max 3 attempts | `while` + counter + `break` |
| 6 | `06_expensive_products.py` | Products costing over ₹2,000 | Loop over `dict.items()` + filter |
| 7 | `07_accept_ten_numbers.py` | Accept 10 numbers from the user | Loop + `input()` + `append()` |
| 8 | `08_character_frequency.py` | Character frequency without `Counter` | Building a dict in a loop |
| 9 | `09_second_largest.py` | Second largest without `sort()` | Tracking two champions |
| 10 | `10_palindrome_check.py` | Palindrome check using loops | Two-pointer technique |
| 11 | `11_number_pattern.py` | Number pattern `1` / `12` / `123` … | Nested loops |
| 12 | `12_atm_simulation.py` | Menu-driven ATM | `while True` + `break`, split into functions |

---

## Questions and approach

### Q1 — Total transaction value without `sum()`
**File:** `01_total_transactions.py`

The **accumulator** pattern: `total = 0` declared *outside* the loop, then `total += amount`
on each pass. Declaring it inside would reset it every time and leave only the last value.

```
[1200, 450, 800, 1500, 2300, 700, 100]  ->  7050
```

### Q2 — Highest and lowest without `max()` / `min()`
**File:** `02_highest_lowest_transaction.py`

The **champion** pattern: assume the first element wins, then challenge it against every
other. Seeding from `transactions[0]` rather than `0` is deliberate — with all-negative
data, starting at 0 would report a value that is not in the list.

```
Highest 2300   Lowest 100   Range 2200
```

### Q3 — Average temperature
**File:** `03_average_temperature.py`

Accumulator for the total, then divide by the count. Also reports how many days sat above
and below the average.

```
[32, 35, 28, 40, 38, 31, 42]  ->  total 246, average 35.14
```

### Q4 — Count students per grade band
**File:** `04_marks_analysis.py`

Four counters driven by `if / elif / else`. **`elif` is load-bearing here** — 92 satisfies
`>= 90`, `>= 75` *and* `>= 50`, so separate `if`s would count that student three times.
The "Total counted: 7 of 7" line is the proof that each student landed in exactly one band.

```
90+ : 2    75-89 : 2    50-74 : 2    below 50 : 1
```

### Q5 — Login system, maximum 3 attempts
**File:** `05_login_system.py` · **interactive**

A `while` loop with **two exits**: `break` on the correct password, or the condition
`attempts < MAX_ATTEMPTS` turning False. A plain `while True` would let someone guess
forever, which is exactly what a login system must prevent.

### Q6 — Products costing more than ₹2,000
**File:** `06_expensive_products.py`

Loops a dictionary with `.items()`, which yields the key and value together. **Watch the
boundary:** "more than 2000" means `> 2000`, not `>=`. Headphones cost exactly ₹2,000 and
are correctly excluded — the program prints the True/False test for every product so this
is visible rather than hidden.

```
Matched: Laptop (55000), Phone (30000)  ->  2 of 5
```

### Q7 — Accept 10 numbers from the user
**File:** `07_accept_ten_numbers.py` · **interactive**

`input()` always returns a string, so `int()` is required before any arithmetic. A
`try/except ValueError` catches typos and re-asks for that number rather than crashing,
so the count of 10 valid entries is still honoured.

### Q8 — Character frequency without `Counter`
**File:** `08_character_frequency.py`

The whole algorithm is one `if/else`: seen before → `+= 1`; brand new → start at `1`. The
program narrates each character so the dictionary is visibly built up.

```
"banana"  ->  b: 1, a: 3, n: 2
```

### Q9 — Second largest without `sort()`
**File:** `09_second_largest.py`

Tracks **two** champions at once. The order of the two lines matters: the old largest must
be pushed down into second *before* largest is overwritten, or it is lost. Values equal to
the largest are skipped, so the answer is the second-largest **distinct** value.

```
[45, 88, 12, 99, 67, 99, 23]  ->  largest 99, second largest 88
```

Edge case handled: when every value is identical, there is no second largest, and the
program says so instead of returning a wrong number.

### Q10 — Palindrome check using loops
**File:** `10_palindrome_check.py` · **interactive**

**Two-pointer** technique — one index at the front, one at the back, moving inward until
they meet. The first mismatch returns immediately, so only half the characters are ever
compared. The `text[::-1]` shortcut is deliberately avoided. Spaces and capitals are
stripped first, so sentences work too.

### Q11 — Number pattern
**File:** `11_number_pattern.py`

**Nested loops.** The outer loop controls the rows, the inner controls what goes on each
row — and the inner loop's length *depends on* the outer counter, which is what makes a
triangle instead of a rectangle. `print(x, end="")` keeps a row on one line; a bare
`print()` ends it.

### Q12 — Menu-driven ATM
**File:** `12_atm_simulation.py` · **interactive**

`while True` plus `break`, organised into six functions rather than one block.
`deposit()` and `withdraw()` share `get_amount()` for validation, so the "must be a
number, must be positive" rules are written once. A failed validation returns early, so
the balance is **never** touched on invalid input.

---

## Interactive programs

Programs 5, 7, 10 and 12 read from the keyboard.

**`05_login_system.py`** — username `admin`, password `python123`
- Success: enter the correct password on any of the 3 attempts
- Failure: enter a wrong password 3 times → account locked

**`12_atm_simulation.py`** — starting balance ₹5,000
- Options: 1 check balance · 2 deposit · 3 withdraw · 4 exit
- Rejects: non-numeric amounts, amounts ≤ 0, withdrawals over the balance, invalid menu choices
- Prints a session summary of all transactions on exit

---

## Notes on the constraints

- `sum()`, `max()`, `min()` and `sort()` are **not** used to solve problems 1, 2 and 9.
  Programs 1 and 2 call them once at the end purely to *verify* the loop's answer.
- `collections.Counter` is not used in problem 8.
- Problem 10 avoids the `text[::-1]` shortcut and compares characters with a loop.
- Problem 6 uses `price > 2000`, not `>=`. Headphones cost exactly ₹2,000 and are
  correctly **excluded**.
