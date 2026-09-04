# Exercise 07 - Removing Duplicates with Sets

## What this exercise is about

Taking a list with repeated values and stripping it down to unique entries in a single
call - no loops, no comparisons. Two examples are worked through: a list of numbers,
and an attendance list of student names.

A set is not "a function that removes duplicates". It is a container **physically
incapable** of holding the same value twice, so the duplicates are never accepted in
the first place.

## Key results

```
[10, 20, 30, 20, 40, 10, 50, 30, 60]   9 items -> 6 unique, 3 removed
9 attendance entries                    -> 5 students, 4 removed (Priya appeared 3x)
```

## Why sets are useful

1. **One line replaces an algorithm.** Without a set you would need a loop, a second
   list, and an `if x not in result` check on every item.
2. **Membership testing is fast.** `"Priya" in students` uses hashing to jump straight
   to the answer; a list has to walk item by item.
3. **Comparison operators lists do not have** - `&` (in both), `|` (in either),
   `-` (in the first only).

## What a set costs you

| You lose | Consequence |
|---|---|
| Order | `[10, 20, 30, ...]` came back as `{40, 10, 50, ...}` |
| Indexing | `unique_set[0]` raises `TypeError` |
| Counts | You can no longer tell that 20 appeared twice |

That last one matters most - which is why the program counts the duplicates
**before** converting. `sorted(set(data))` is the practical pattern: unique *and*
back in order.

## Run it

```bash
python 07_remove_duplicates_sets.py
```

or from the repo root:

```bash
python .\01_python_basics\07_remove_duplicates_sets\07_remove_duplicates_sets.py
```

The names set may print in a different order each run - Python randomises string
hashing per process. That is live proof that sets have no reliable order.
