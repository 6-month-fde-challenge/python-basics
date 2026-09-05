# Exercise 21 - Combined Final Project

Loops, while loops and functions brought together into twelve practical
mini-programs.

---

## Project objective

The three earlier modules each taught one idea in isolation — `for` loops, `while`
loops, and functions. This project combines all three into applications that
actually do something: a bank, an inventory system, a quiz, a shopping cart, an
expense tracker.

The shift in this project is **structure**. Earlier exercises were single scripts. Here
each program is built from small named functions with a `main()` that coordinates
them, input is validated instead of trusted, and edge cases are handled rather than
assumed away.

---

## Project structure

```
21_combined_final_project/
├── README.md
├── requirements.txt
├── exercise_01/   Student Result Management System
│   ├── main.py
│   └── sample_output.txt
├── exercise_02/   Banking Application
├── exercise_03/   Inventory Management
├── exercise_04/   Quiz Application
├── exercise_05/   Number Analysis Tool
├── exercise_06/   Employee Salary Analyzer
├── exercise_07/   Shopping Cart
├── exercise_08/   Password Strength Checker
├── exercise_09/   Prime Number Analyzer
├── exercise_10/   Expense Tracker
├── exercise_11/   Mini Authentication System
└── exercise_12/   Python Utility Application
```

Each `exercise_XX/` folder contains `main.py` and a `sample_output.txt` captured from a
real run.

---

## How to execute the programs

No installation is required — the project uses only the Python standard library.

```bash
python exercise_01/main.py
```

or from the repo root:

```bash
python .\01_python_basics\21_combined_final_project\exercise_01\main.py
```

or from inside the exercise folder:

```bash
cd exercise_01
python main.py
```

**Requires Python 3.6+** (f-strings). Verified on Python 3.12.

---

## Programs completed

| # | Program | What it does | Type |
|---|---------|--------------|------|
| 01 | Student Result Management | Marks → total, percentage, grade, pass/fail | Interactive |
| 02 | Banking Application | Balance, deposit, withdraw, transaction history | Menu-driven |
| 03 | Inventory Management | Add, display, search, update quantity, total value | Menu-driven |
| 04 | Quiz Application | 5 Python questions, score, percentage, answer review | Interactive |
| 05 | Number Analysis Tool | 8 statistics in one pass, no `min`/`max`/`sum` | Runs standalone |
| 06 | Employee Salary Analyzer | Payroll, average, highest, lowest, above-average staff | Runs standalone |
| 07 | Shopping Cart | Add, remove, view, bill with GST | Menu-driven |
| 08 | Password Strength Checker | 5 rules → score out of 5 and a strength rating | Runs standalone |
| 09 | Prime Number Analyzer | Primes in a range: list, count, sum, largest | Interactive |
| 10 | Expense Tracker | Add, view, total, highest expense | Menu-driven |
| 11 | Mini Authentication System | Login limit, dashboard, logout, retry | Menu-driven |
| 12 | Python Utility Application | **8 utilities** in one menu | Menu-driven |

### Verified results

```
exercise_01   Rahul: 88+92+76+65+95 = 416/500 -> 83.20% -> Grade A -> PASS
exercise_05   [12,-5,8,0,33,-17,4,25,-8,41] -> largest 41, smallest -17,
          total 93, average 9.30, even 5, odd 5, +6 / -3 / zero 1
exercise_09   Range 1-100 -> 25 primes, sum 1060, largest 97, density 25.0%
exercise_07   Laptop x1 + Mouse x2 -> subtotal 56400.00, GST 18% -> 66552.00
```

---

## Concepts used

**Loops**
- `for` over lists, dictionaries, strings and `range()`
- `while` for menus, input validation and retry logic
- Nested loops (exercise_11 has a login loop inside an application loop)
- `break` to leave early, `continue` to skip one pass
- `enumerate()` for numbered output

**Functions**
- One function per job, with a docstring on every one
- Return values rather than printing, so results can be reused
- Default arguments, and functions calling other functions
- A dictionary mapping menu choices to function objects (exercise_12), replacing a long
  `if/elif` chain
- `global` where an operation must update shared state (exercises 02, 07)

**Data structures**
- Lists of dictionaries for tabular data (exercises 03, 06, 10)
- Dictionaries for lookups — catalogues, credentials, menu routing

**Techniques written by hand rather than with built-ins**
- Accumulator pattern instead of `sum()`
- Champion pattern instead of `max()` / `min()`
- Divisor loop stopping at √n for prime testing
- Two-pointer comparison for palindromes

**Error handling**
- `try/except ValueError` on every numeric input
- Guards for divide-by-zero, empty lists, blank names, negative amounts,
  overdrafts, and unknown products
- Invalid menu choices redisplay the menu instead of crashing or exiting

---

## Why `for` or `while` was selected

| Situation | Loop | Reason |
|---|---|---|
| Walking a known list of subjects, questions, employees | `for` | The count is known before the loop starts |
| Menus (exercises 02, 03, 07, 10, 11, 12) | `while` | The user decides when to stop — a **condition**, not a count |
| Input validation and retries | `while` | Nobody knows how many times a user will mistype |
| Login attempts (exercise_11) | `while` with a limit | Two exits: success (`break`) or attempts exhausted |
| Prime testing | `while divisor * divisor <= n` | The number of divisors to test depends on the value |

The dividing line: **`for` is count-controlled, `while` is condition-controlled.**

In every menu-driven program, `running = False` is the **only** line that ends the
application. Invalid input, declined transactions and unknown menu choices all
deliberately leave the flag alone and loop back to the menu.

---

## Learning / outcomes

1. **Returning beats printing.** A function that prints can be used one way. A
   function that returns can be totalled, compared, filtered or passed on. Exercise 05
   returns a dictionary of eight statistics precisely so the caller can do anything
   with them.

2. **One pass, not eight.** The first version of the number analyzer looped eight
   times, once per statistic. Each statistic only needs to see one number at a
   time, so they all collapse into a single loop.

3. **Seed a champion with real data, never zero.** Starting `largest = 0` looks
   harmless until every value is negative — then the answer is 0, a number not even
   in the list. Starting with `numbers[0]` is always safe.

4. **Validation is most of the work.** The maths in these programs is short. Most
   of the code is making sure bad input cannot corrupt the state — which is what
   separates a script from an application.

5. **Menus are just three lines of loop.** `running = True`, `while running:`,
   `running = False`. Everything else is routing.

6. **Edge cases are where the bugs live.** An empty list, a zero divisor, `0!`,
   the number 1 in a prime test, removing more units than the cart holds — each of
   these needed explicit handling.

### Challenges faced

- **The average is not the midpoint.** In exercise 06, only 3 of 8 employees earn above
  the average, because a few large salaries pull it upward. The report prints the
  count so this is visible rather than surprising.
- **Duplicate cart lines.** Adding a product already in the cart originally created
  a second line. Fixed by checking membership first and increasing the quantity.
- **A `while` loop that never runs.** `count_digits(0)` returned 0 because `0 > 0`
  is False, so the body never executed — but 0 has one digit. Handled before the loop.
- **Shared state across functions.** Exercises 02 and 07 need several functions to
  update one balance or cart, which is what `global` is for — though passing state
  in and returning it is the cleaner long-term habit.

---

## YouTube demonstration link

<your-youtube-video-link>

---

## Submission links

- **GitHub Repository:** `<your-public-github-repository-link>`
- **YouTube Explanation:** `<your-youtube-video-link>`
