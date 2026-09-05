# Exercise 18 - while Loops

Condition-controlled iteration, and where `while` is more appropriate than `for`.

Twelve independent programs:

```bash
python 01_print_1_to_100.py
```

or from the repo root:

```bash
python .\01_python_basics\18_while_loops\01_print_1_to_100.py
```

## The three-part rule

Every major `while` loop here is commented with the same three
labels, because getting any one of them wrong is what causes an infinite loop:

```python
# INITIALIZATION : the counter is created BEFORE the loop
n = 1

# CONDITION : the test at the top; while True, the loop runs
while n <= 100:
    print(n)

    # UPDATE / TERMINATION : n moves towards failing the condition.
    # Remove this line and the program hangs forever.
    n += 1
```

A `for` loop hides all three inside `range()`. A `while` loop makes you write them
yourself — which is exactly why it can express things `for` cannot.

**No accidental infinite loops:** every program was run under a hard timeout to
confirm it terminates. The interactive ones were driven through all their paths,
including invalid input.

---

## Questions and approach

### Q1 — Print 1 to 100
**File:** `01_print_1_to_100.py` · no input

Counter starts at 1, condition `n <= 100`, update `n += 1`. Also shows what an
accidental infinite loop looks like, and that the update step need not be 1.

### Q2 — Print 100 down to 1
**File:** `02_print_100_to_1.py` · no input

Counting down flips two of the three parts: start at 100, condition `n >= 1`,
update `n -= 1`. **The classic bug** is writing `n += 1` out of habit — the counter
then runs *away* from the condition and the loop never ends. Includes a rocket
countdown.

### Q3 — Even numbers 1 to 100
**File:** `03_even_numbers.py` · no input

Two methods. Method 1 steps by 1 and filters with `if n % 2 == 0`. Method 2 starts
at 2 and steps by 2, so every value is already even — half the passes and no
condition inside the body. The filter has been moved into the **update** step.

### Q4 — Sum of digits
**File:** `04_sum_of_digits.py` · no input

`number % 10` takes the last digit, `number //= 10` removes it. Each pass peels one
digit off the right; when the number hits 0 the loop ends by itself.

```
5832 -> 2, then 3, then 8, then 5  ->  18
```

### Q5 — Reverse an integer
**File:** `05_reverse_integer.py` · no input

Same peeling loop, but each digit is used to **build** a new number:
`reversed_number = reversed_number * 10 + digit`. Multiplying by 10 shifts what has
already been collected left, freeing the units column for the new digit.

```
12345 -> 5 -> 54 -> 543 -> 5432 -> 54321
```

Note `1000` reverses to `1` — leading zeros do not exist in a number.

### Q6 — Count the digits
**File:** `06_count_digits.py` · no input

The same loop with a plain counter. **The edge case is 0**: `0 > 0` is False, so the
loop never runs and the count would be 0 — but 0 has one digit. Handled before the
loop. A good reminder that a `while` loop can run **zero times**, since its
condition is tested *before* the first pass.

### Q7 — Factorial
**File:** `07_factorial_while.py` · no input

Two accumulators at once: `i` drives the loop, `result` collects the product. The
product starts at **1, not 0** — the program runs the broken zero-start version to
show 5! coming out as 0. Honest note in the file: `for` is genuinely the better
choice here, since the pass count is known.

### Q8 — Sum numbers until the user enters 0
**File:** `08_sum_until_zero.py` · **interactive**

The clearest case for `while`. `0` is a **sentinel value** — an input whose only job
is to signal "stop", and which is not added to the total. Invalid text is rejected
without ending the loop.

```
10, 25, 5, 0  ->  Sum: 40   Average: 13.33
```

### Q9 — Password checker
**File:** `09_password_checker.py` · **interactive** · password `python123`

Keeps asking until the password matches. Termination happens the moment the
condition `entered != CORRECT_PASSWORD` becomes False. Also documents a safer
version with an attempt limit, since unlimited attempts is a real security problem.

### Q10 — Guessing game
**File:** `10_guessing_game.py` · **interactive** · secret number `42`

Loops on a `found` flag, giving too-high/too-low hints. Includes the halving
strategy: each guess halves the remaining range, so any number in 1–100 is found in
at most 7 guesses.

### Q11 — Menu-driven calculator
**File:** `11_menu_calculator.py` · **interactive**

`1 Add · 2 Subtract · 3 Multiply · 4 Divide · 5 Exit`. The menu redisplays after
every action. `running = False` on option 5 is the **only** line that ends the
program. Validated: non-numeric input, division by zero, invalid menu choices —
none of which end the loop.

### Q12 — ATM menu
**File:** `12_atm_menu.py` · **interactive** · starting balance ₹5,000

`1 Check balance · 2 Deposit · 3 Withdraw · 4 Mini statement · 5 Exit`. Contains a
**nested** `while` loop for printing the statement, also fully commented. Validated:
non-numeric amounts, amounts ≤ 0, withdrawals over the balance, invalid menu
choices. Prints a session summary on exit.

---

## Why `while` rather than `for`

| Question | Number of passes | Right loop |
|---|---|---|
| Q1, Q2, Q3, Q7 | known in advance | `for` would be cleaner — `while` used to show the three parts |
| Q4, Q5, Q6 | depends on the **data** (how many digits) | **`while`** |
| Q8, Q9, Q10, Q11, Q12 | depends on the **user**, at run time | **`while`** |

The dividing line: `for` is **count-controlled**, `while` is **condition-controlled**.
When nobody can say up front how many passes are needed, only a condition works.
