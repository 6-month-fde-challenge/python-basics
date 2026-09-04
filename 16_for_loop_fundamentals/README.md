# Exercise 16 - for Loop Fundamentals

Building fundamentals in iteration using `for`, `range()`, strings, lists, tuples,
sets and dictionaries.

## About this exercise

Twelve independent programs, each solving one question. Every file is
self-contained and runs on its own:

```bash
python 01_print_1_to_100.py
```

or from the repo root:

```bash
python .\01_python_basics\16_for_loop_fundamentals\01_print_1_to_100.py
```

Each program prints its working step by step rather than just the final answer, so
the logic is visible while it runs. Important logic is explained in comments inside
every file.

**Requires:** Python 3.6 or newer (the programs use f-strings).

---

## Questions, approach and sample output

### Q1 — Print numbers 1 to 100
**File:** `01_print_1_to_100.py` · no input

`for n in range(1, 101)`. The stop value is **101, not 100**, because `range()`
always excludes its stop — `range(1, 100)` would end at 99.

```
Numbers from 1 to 100
1  2  3  4  5  ...  98  99  100
Count of numbers printed : 100
```

### Q2 — Print all even numbers 1 to 100
**File:** `02_even_numbers.py` · no input

Two methods shown. Method 1 tests every number with `if n % 2 == 0`. Method 2 uses
`range(2, 101, 2)` so the step produces only even numbers — half the work, same
answer.

```
2  4  6  8  10  ...  96  98  100
Even numbers found : 50
```

### Q3 — Print all odd numbers 1 to 100
**File:** `03_odd_numbers.py` · no input

The mirror of Q2: test `n % 2 == 1`, or step with `range(1, 101, 2)`.

```
1  3  5  7  9  ...  95  97  99
Odd numbers found : 50
```

### Q4 — Multiplication table of n, from 1 to 20
**File:** `04_multiplication_table.py` · **input:** an integer

Loop `range(1, 21)` and print `n * i`. `input()` returns a **string**, so `int()`
is required first — otherwise `"7" * 3` would give `"777"` instead of `21`.

```
Input : 7

   7 x  1 = 7
   7 x  2 = 14
   ...
   7 x 20 = 140
```

### Q5 — Sum of numbers from 1 to n
**File:** `05_sum_1_to_n.py` · **input:** an integer

Accumulator pattern: `total = 0` **outside** the loop, then `total += i` inside. If
the accumulator were declared inside, it would reset on every pass. Verified
against the formula `n × (n + 1) / 2`.

```
Input : 10

SUM OF 1 TO 10 = 55
Formula check: 10 x 11 / 2 = 55  -> match: True
```

### Q6 — Factorial without a built-in function
**File:** `06_factorial.py` · **input:** a non-negative integer

Accumulator again, but **multiplying**. The critical difference from a sum: the
accumulator starts at **1, not 0** — anything multiplied by 0 stays 0. `0!` is
defined as 1.

```
Input : 5

   x 1 -> 1     x 2 -> 2     x 3 -> 6     x 4 -> 24     x 5 -> 120
5! = 120
Working: 5! = 1 x 2 x 3 x 4 x 5 = 120
```

### Q7 — Numbers divisible by 3 from a list
**File:** `07_divisible_by_3.py` · no input

Loop the list directly — no `range()` needed, since the `for` takes items straight
from the list — and filter with `n % 3 == 0`.

```
Input  : [12, 7, 9, 20, 33, 42, 8, 15]
Output : [12, 9, 33, 42, 15]      (5 of 8, total 111)
```

### Q8 — Every language with its length
**File:** `08_language_lengths.py` · no input

Loop the list and call `len()` on each string. Note that `len()` answers two
different questions: on a **list** it counts items, on a **string** it counts
characters.

```
   Python       -> 6 characters
   Java         -> 4 characters
   C++          -> 3 characters
   JavaScript   -> 10 characters
   Go           -> 2 characters
```

### Q9 — Print every key and value of a dictionary
**File:** `09_iterate_dictionary.py` · no input

`.items()` yields a `(key, value)` **tuple** each pass, unpacked into two loop
variables. All three looping styles are shown — keys only, values only, and both.

```
   name -> Rahul
   age -> 22
   course -> Data Science
   city -> Bangalore
```

### Q10 — Count vowels in a user-provided string
**File:** `10_count_vowels.py` · **input:** any string

A string is iterable, so `for char in text` walks it character by character.
`char.lower()` is essential — without it, `"APPLE"` would report 0 vowels because
the vowel list is lowercase.

```
Input : Programming

VOWEL COUNT  : 3
Vowels found : ['o', 'a', 'i']
```

### Q11 — Reverse a string using a loop
**File:** `11_reverse_string.py` · **input:** any string

`[::-1]` and `reversed()` are **not** used. Instead each character is placed in
**front** of what has been built so far: `reversed_text = char + reversed_text`.
Every new character pushes the earlier ones right, which reverses the order. A
second method walking backwards by index is shown for comparison.

```
Input : Python

   'P' -> "P"    'y' -> "yP"    't' -> "tyP"    'h' -> "htyP" ...
Reversed : nohtyP
```

### Q12 — Largest number without `max()`
**File:** `12_largest_without_max.py` · no input

Champion pattern: assume `numbers[0]` is the largest, then replace it whenever a
bigger value appears. Starting from `numbers[0]` rather than `0` matters — with an
all-negative list, starting at 0 returns 0, a value not even in the list. The
program demonstrates that bug.

```
Input  : [12, 7, 9, 20, 33, 42, 8, 15]
Output : LARGEST NUMBER : 42
```

---

## Notes on the constraints

- Q6 computes the factorial with a loop; `math.factorial` is not used.
- Q11 uses neither `[::-1]` nor `reversed()`.
- Q12 solves the problem with a loop. `max()` appears once at the end **only** to
  print a `match: True` verification line.
- Programs 4, 5, 6, 10 and 11 read one value from the keyboard; the other seven run
  unattended.
