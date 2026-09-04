# Exercise 04 - Data Type Laboratory

## What this exercise is about

A tour of every core Python data type, followed by type conversion. Sixteen variables
are created - two examples of each of the eight types - and `type()` is called on all
of them. Then seven conversions are performed, each printing the value **and** its
type both before and after, so the change is visible rather than asserted.

## The eight types, organised by what actually separates them

| | Ordered? | Changeable? | Duplicates? |
|---|---|---|---|
| **list** `[]` | yes | yes | yes |
| **tuple** `()` | yes | **no** | yes |
| **set** `{}` | **no** | yes | **no** |
| **dict** `{k: v}` | yes | yes | keys unique |

Plus the four scalar types: `int`, `float`, `str`, `bool`.

## Conversions demonstrated

`int("100")` · `float("45.67")` · `str(500)` · `bool(1)` · `list((1,2,3))` ·
`tuple([1,2,3])` · `set([1,2,2,3])`

They fall into three groups:

1. **Parsing text into a number** - `"100" + "100"` is `"100100"`, but `100 + 100` is
   `200`.
2. **Unlocking or locking a container** - list ↔ tuple, same items, different
   permissions.
3. **Losing information** - `set([1,2,2,3])` is the only conversion that *destroys*
   data. Four items in, three out, and converting back will not restore the missing 2.

## Worth knowing

- `bool()` follows a fixed rule: `0`, `0.0`, `""`, `[]`, `()`, `{}` and `None` are
  falsy; **everything else** is `True`.
- Not every conversion is possible. The program ends by triggering a real
  `ValueError` from `int("hello")` inside a `try/except`.

## Run it

```bash
python 04_data_type_laboratory.py
```

or from the repo root:

```bash
python .\01_python_basics\04_data_type_laboratory\04_data_type_laboratory.py
```
