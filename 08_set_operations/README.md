# Exercise 08 - Set Operations

## What this exercise is about

Two sets of students - one learning Python, one learning Java - compared and modified
using all seven core set operations. The program answers the kind of questions a real
enrolment system would ask: who is on both courses, who is only on one, who is
enrolled anywhere at all.

## The split that organises everything

| Family | Methods | Behaviour |
|---|---|---|
| **Comparing** | `union`, `intersection`, `difference`, `symmetric_difference` | return a **new set**; originals untouched |
| **Changing** | `add`, `remove`, `discard` | modify **in place**; return `None` |

The program reprints both original sets after all four comparisons to prove they
survived.

## The four comparisons as a Venn diagram

| Operation | Operator | Answers | Result |
|---|---|---|---|
| `union()` | `\|` | either course | 7 students |
| `intersection()` | `&` | both courses | Karan, Priya |
| `difference()` | `-` | Python only | Aman, Neha, Rahul |
| `symmetric_difference()` | `^` | exactly one course | 5 students |

`difference()` is the only **directional** one: `python - java` and `java - python`
give completely different answers. And the arithmetic is not a coincidence -
**7 (union) − 2 (intersection) = 5 (symmetric difference)** is the definition.

## `remove()` versus `discard()`

Identical when the item exists. The difference only appears when it does not:

```
remove("Vikram")   ->  KeyError    (crashes)
discard("Vikram")  ->  runs quietly
```

Use `remove()` when the item *must* be there - a crash correctly tells you the data is
wrong. Use `discard()` when you only care that it is gone. Choosing `discard()`
everywhere to avoid errors hides genuine bugs.

## Run it

```bash
python 08_set_operations.py
```

or from the repo root:

```bash
python .\01_python_basics\08_set_operations\08_set_operations.py
```
