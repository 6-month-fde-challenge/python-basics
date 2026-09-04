# Exercise 09 - Tuples and Immutability

## What this exercise is about

A tuple of programming languages put through eleven operations - indexing, slicing,
counting, searching - and then the question it is really built around: how do you
"add" an item to something that cannot be changed?

The answer is that you do not. You convert it to a list, edit that, and build a
**new** tuple from the result. Three separate objects. The program reprints the
original tuple afterwards, still six items long, to prove it was never touched.

## Three proofs of immutability

1. **Assignment is refused.** `technologies[1] = "Ruby"` raises
   `TypeError: 'tuple' object does not support item assignment`. The program triggers
   the real error inside a `try/except`.
2. **The methods do not exist.** A tuple has **2** methods (`count`, `index`); a list
   has **11**. There is no `append`, no `remove`, no `sort` - Python never gave tuples
   any way to change.
3. **Rebinding is not mutating.** `sample = ("A","B")` then `sample = ("A","B","C")`
   *looks* like editing. It is not - the first tuple was never altered, the **name**
   was pointed at a new one. Immutability is a property of the object, not the name.

## So why use a tuple?

- **Safety** - fixed data like `(latitude, longitude)` cannot be corrupted by accident.
- **Speed** - lighter and faster than a list.
- **Hashability** - a tuple can be a dictionary key or set member; a list raises
  `unhashable type: list`. The program uses coordinates as dict keys to show this.

## The trap

`("Python")` is a **string** - the brackets are just grouping. `("Python",)` is a
tuple. It is the **comma** that makes a tuple, not the brackets.

## Run it

```bash
python 09_tuple_challenge.py
```

or from the repo root:

```bash
python .\01_python_basics\09_tuple_challenge\09_tuple_challenge.py
```
