# Exercise 23 - Fault-Tolerant Student Result Processor

Fourteen student records go in. Seven of them are broken. All fourteen are accounted
for, seven results come out, and the program never stops.

---

## Project objective

Exercise 22 was about **recording** what happened. This one is about **surviving** it.

The rule the whole exercise turns on: *instead of stopping when an error occurs, log
the error and continue processing the remaining students.* A batch job that dies on
row 4 of 200 is worse than useless — it has done a quarter of the work and told you
almost nothing about why it stopped.

Six things can be wrong with a record, and each gets its own exception class rather
than a shared `ValueError` with a different message string. That is the difference
between an error you can *branch on* and an error you have to *read*.

---

## Project structure

```
23_student_result_processor/
├── README.md
├── 00_concepts.py       READ FIRST - exception handling, demonstrated
├── main.py              load, process every row, report - holds the continue-on-error loop
├── student_ops.py       reading and validating records from the CSV
├── result_calc.py       total, percentage, grade, pass/fail - pure arithmetic
├── exceptions.py        the six exception classes
├── logger_config.py     where log records go
├── sample_output.txt    captured from a real run
├── data/
│   └── students.csv     14 records, 7 of them deliberately broken
└── logs/
    ├── application.log  DEBUG and above - the full processing trace
    └── error.log        ERROR and above - the rejected records alone
```

Four modules for four jobs, exactly as the assignment asks: **student operations,
result calculation, exception definitions, logging configuration.**

---

## How to execute the program

No installation is required — `csv` and `logging` are both standard library.

```bash
python 00_concepts.py              # READ FIRST - the concepts, standalone
python main.py                     # process data/students.csv
python main.py path/to/other.csv   # process a different file
python result_calc.py              # self-test the arithmetic alone
```

or from the repo root:

```bash
python .\01_python_basics\23_student_result_processor\main.py
```

**Requires Python 3.6+.** Verified on Python 3.12.10.

---

## The exception hierarchy

```
Exception
 └── StudentDataError                base for everything below
      ├── MissingStudentInfoError        no roll number, or no name
      ├── InvalidMarksError              not a number at all
      │    └── MarksOutOfRangeError      a number, but not 0-100
      ├── SubjectCountError              not exactly 5 subjects
      └── ResultCalculationError         the arithmetic itself failed
```

Two inheritance decisions do the real work:

**Everything descends from `StudentDataError`.** That is what lets `main.py` say "any
problem with this student, skip them" in one clause — while still letting a genuine
bug (a typo in a variable name, say) fall through to the `except Exception` below it
and be logged as `CRITICAL` with a traceback. A bare `except Exception` would have
hidden the bug among the bad data.

**`MarksOutOfRangeError` descends from `InvalidMarksError`.** 105 and `"abc"` are both
unusable marks; one is unusable in a more specific way. So the keyboard loop, which
only cares "were the marks usable?", catches `InvalidMarksError` and gets both:

```python
except InvalidMarksError as error:      # catches MarksOutOfRangeError too
    print(f"      -> {error.message}. Try again (0-100).")
```

The classes carry **fields, not just text**. `InvalidMarksError` holds `.subject`,
`.value` and `.reason`; `StudentDataError` holds `.roll`, so `__str__` can prefix every
message with `[roll 105]` without a single caller having to remember to add it.

```python
raise MarksOutOfRangeError("Maths", 101.0, roll="105")
# -> [roll 105] Invalid marks for Maths: 101.0 (outside the valid range 0-100)
```

---

## The one loop that matters

```python
for position, row in enumerate(rows, start=1):
    try:
        student = student_ops.build_student(row)
        result  = result_calc.process(student)

    except StudentDataError as error:          # our own errors: bad data
        log.error("SKIPPED %s - %s: %s", label, type(error).__name__, error.message)
        skipped.append(...)
        continue

    except Exception as error:                 # not ours: a defect
        log.critical("SKIPPED %s - unexpected %s", label, ..., exc_info=True)
        skipped.append(...)
        continue

    else:
        results.append(result)

    finally:
        log.debug("Finished with %s", label)
```

`continue` **is** the fault tolerance. Everything else — the exception classes, the two
log files, the summary table — exists to make that one line safe to rely on.

The four clauses each earn their place:

| Clause | Handles | Level |
|---|---|---|
| `except StudentDataError` | the six things we predicted | `ERROR` |
| `except Exception` | the things we did not | `CRITICAL` + traceback |
| `else` | the success path, kept visibly separate | — |
| `finally` | runs on all three, so the trace has no gaps | `DEBUG` |

The `try` wraps **one iteration**, not the loop. That is the whole trick: put the
`try` outside the `for` and the first bad row still ends the run.

---

## Validation rules

| Check | Raises | Example row |
|---|---|---|
| roll number present | `MissingStudentInfoError` | `,Anonymous Student,70,...` |
| name present | `MissingStudentInfoError` | `103,,55,62,71,48,66` |
| mark parses as a number | `InvalidMarksError` | `104,Aman Verma,45,abc,...` |
| mark is not blank | `InvalidMarksError` | `110,Arjun Das,,,,,` |
| mark within 0-100 | `MarksOutOfRangeError` | `105,...,101,...` and `106,...,-5,...` |
| exactly 5 subjects | `SubjectCountError` | `107,Divya Iyer,90,85,77,68` |
| divisor is non-zero | `ResultCalculationError` | 0 subjects to divide by |

Surrounding whitespace on a name is stripped rather than refused — a padded name is
still a name. Everything else in the table is refused, logged, and skipped.

---

## The result rules

```
total       the five marks added up                       0 - 500
percentage  total / (5 * 100) * 100                       0 - 100
grade       A+ >=90   A >=80   B >=70   C >=60   D >=50   E >=40   F below 40
pass        percentage >= 40  AND  every subject >= 33
```

The second pass condition is the interesting one. **Rohit Kulkarni scores 95, 90, 88,
30, 85 — an average of 77.6%, a clear pass — and fails**, because 30 in English is
below the subject minimum. Averaging hides a failed subject, so the per-subject check
runs separately and the report says which subject:

```
112    Rohit Kulkarni    388/500   77.60%      B  FAIL
       -> English below the subject minimum of 33
```

`calculate_percentage()` guards its own division:

```python
try:
    percentage = (total / (subject_count * MAX_PER_SUBJECT)) * 100
except ZeroDivisionError:
    raise ResultCalculationError("Cannot calculate a percentage from 0 subjects",
                                 roll) from None
```

`from None` suppresses the "During handling of the above exception..." chain, because
the `ZeroDivisionError` is an implementation detail — the caller wants the error that
names a student.

---

## Verified run

```
Records read        : 14
Processed           : 7
Skipped (logged)    : 7
Passed / Failed     : 5 / 2
Class average       : 71.47%
Highest             : Neha Gupta (100.00%)
```

`error.log` after that run — seven skipped records, one per line:

```
ERROR | SKIPPED 103    - MissingStudentInfoError: Missing student information: 'name' is empty
ERROR | SKIPPED 104    - InvalidMarksError:       Invalid marks for Physics: 'abc' (not a number)
ERROR | SKIPPED 105    - MarksOutOfRangeError:    Invalid marks for Maths: 101.0 (outside 0-100)
ERROR | SKIPPED 106    - MarksOutOfRangeError:    Invalid marks for Maths: -5.0 (outside 0-100)
ERROR | SKIPPED 107    - SubjectCountError:       Expected 5 subject marks, found 4
ERROR | SKIPPED 110    - InvalidMarksError:       Invalid marks for Maths: '' (no value given)
ERROR | SKIPPED row 13 - MissingStudentInfoError: Missing student information: 'roll' is empty
```

85 records in `application.log`: 1 `CRITICAL`, 7 `ERROR`, 16 `INFO`, 61 `DEBUG` - and no
`WARNING`, because nothing in this data set is repairable: every problem is either fine
or fatal to that one record.

**The one failure that does stop the program** is a missing data file — logged
`CRITICAL`, exit code 1. There is no point being fault-tolerant when there is nothing
to process:

```
[CRITICAL] Data file not found: data/not_here.csv - nothing to process
```

`python result_calc.py` self-tests the arithmetic with no CSV and no menu in the way,
including the division guard:

```
Clear pass                           416   83.20%  A   PASS
Clear fail                           173   34.60%  F   FAIL
High average, one subject failed     388   77.60%  B   FAIL   <- English below 33
Perfect                              500  100.00%  A+  PASS
Exactly on the pass line             200   40.00%  E   PASS
division guard   -> ResultCalculationError: [roll EMPTY] Cannot calculate a percentage from 0 subjects
```

---

## Concepts used

**Custom exceptions**
- A base class per application, subclasses per failure mode
- Subclassing a subclass (`MarksOutOfRangeError` from `InvalidMarksError`) so one
  `except` can be broad or narrow as the caller needs
- `super().__init__(message)` so `str(error)` and the traceback are useful
- Extra attributes on the exception (`.subject`, `.value`, `.roll`) instead of one
  flattened message string
- Overriding `__str__` to prefix the roll number in one place
- `raise ... from None` to hide an implementation-detail exception chain

**Exception handling**
- `try` / `except` / `else` / `finally` with all four clauses doing distinct work
- The `try` inside the loop, not around it
- Ordering: our own base class first, `Exception` after it
- Re-raising in `load_rows()` so a missing file reaches a caller that can stop

**Modules**
- Four modules with four jobs and no circular imports — `exceptions.py` imports
  nothing, `logger_config.py` imports nothing of ours, the rest import those two
- `result_calc.py` is pure: no input, no printing, no skip decisions, so
  `python result_calc.py` can test the maths alone via `if __name__ == "__main__"`

**Standard library**
- `csv.DictReader`, which yields dictionaries keyed by the header row and gives `None`
  for columns a short row does not have — which is exactly what makes
  `SubjectCountError` detectable
- `logging` with two file handlers at two thresholds
- `enumerate(rows, start=1)` so a row with no roll number can still be named

---

## Learning / outcomes

1. **An exception class is a decision you can act on; a message string is one you have
   to parse.** `except MarksOutOfRangeError` is code. `if "range" in str(error)` is a
   guess that breaks the moment somebody rewords the message.

2. **The `try` goes inside the loop.** This is the entire assignment in one line of
   placement. Outside the loop, `continue` cannot exist and the first bad row is the
   last row.

3. **Catch your own base class, then `Exception`.** Two clauses, two meanings: the
   first is bad *data* and expected, the second is a bad *program* and is not. Logging
   them at the same level would hide real bugs among ordinary noise.

4. **Not every problem deserves a rejection.** A padded name and a duplicate roll are
   warnings, not errors — the record still works. Deciding which problems are fatal is
   a design choice, and the log is where that choice becomes visible to everyone else.

5. **Averages lie.** 77.6% looks like a comfortable pass until you notice the 30 in
   English. Two independent conditions, reported separately, beat one number.

6. **A skipped record must still be counted.** The first version silently dropped
   keyboard entries that were refused, so the summary said "0 skipped" while the log
   said otherwise. A report that disagrees with the log is worse than no report.

### Challenges faced

- **`except Exception` swallowed a real bug.** An early version caught everything in
  one clause, so a misspelled dictionary key looked exactly like a bad CSV row and got
  quietly "skipped" 16 times. Splitting the clause by exception type made it visible
  immediately, as a `CRITICAL` with a traceback.
- **`float("")` and `float(None)` raise different exceptions.** `ValueError` for the
  first, `TypeError` for the second. Both are caught, because a CSV gives you `""` and
  a short row gives you `None`.
- **A row with four marks still produced a percentage.** Dividing by
  `len(marks) * 100` quietly rescaled the total, so 320/400 read as a perfectly
  plausible 80%. `SubjectCountError` refuses the record instead of reporting a number
  nobody can reproduce.
- **The chained traceback was noise.** Without `from None`, the log showed the
  `ZeroDivisionError` *and* the `ResultCalculationError`, and the useful one was
  second.
- **`csv.DictReader` and the header row.** The header is lower case, the display names
  are not, so `row.get(subject.lower())` bridges the two. Getting this wrong made
  every subject look missing at once.

---

## `00_concepts.py` - the basics, before the application

A plain top-to-bottom script - **no functions**, nothing clever. Read it from the first
line to the last:

| # | Shows |
|---|---|
| 1 | without try/except the loop stops on item 3 |
| 2 | `try` / `except` - it carries on, and knows what it skipped |
| 3 | `try` / `except` / `else` / `finally`, and what runs when |
| 4 | `raise`, and your own exception class |
| 5 | the `try` goes **inside** the loop |

```bash
python 00_concepts.py
```

Section 5 is the one to put on camera - the same loop with one line moved:

```
try OUTSIDE the loop -> 2 of 5 done  [88.0, 92.0]
try INSIDE  the loop -> 4 of 5 done  [88.0, 92.0, 65.0, 95.0]
```

---

## YouTube demonstration link

<your-youtube-video-link>

---

## Submission links

- **GitHub Repository:** `<your-public-github-repository-link>`
- **YouTube Explanation:** `<your-youtube-video-link>`
