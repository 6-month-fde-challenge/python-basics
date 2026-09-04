# Exercise 10 - Nested Dictionaries

## What this exercise is about

An employee record where one of the values is itself a dictionary. Ten operations read
and modify it at both levels, all by direct key access and no loops.

## The mental model

```
employee ---> "name"       : "Amit"
         ---> "department" : "Engineering"
         ---> "skills"     : ---> "language" : "Python"
                             ---> "database" : "PostgreSQL"
                             ---> "cloud"    : "AWS"
         ---> "salary"     : 80000
```

Three values are plain data; **one value is another dictionary**. That is all nesting
means.

## Compared with the nested list in Exercise 05

```
students[1][2]                    -> addressed by POSITION
employee["skills"]["language"]    -> addressed by KEY NAME
```

Same two-step shape. The upgrade is readability: `["price"]` says what it holds,
`[2]` does not - and reordering the data breaks the position but not the key.

## The proof that there are two layers

- `employee["skills"]` -> a **dict**
- `employee["skills"]["cloud"]` -> a **str**

One key gives a container, the second reaches inside it.

## The rule that makes updating and adding identical

`dict[key] = value` - if the key **exists** the value is replaced; if it does **not**,
the key is created. Nothing in the code distinguishes the two cases. This works the
same one level down: `employee["skills"]["framework"] = "Django"` grows the inner
dictionary from three skills to four.

## Safe access

| | Missing key |
|---|---|
| `employee["bonus"]` | **`KeyError`** |
| `employee.get("bonus")` | `None` |
| `employee.get("bonus", 0)` | your default |

Use `[]` when the key must exist; `.get()` for optional fields.

## Run it

```bash
python 10_nested_dictionary.py
```

or from the repo root:

```bash
python .\01_python_basics\10_nested_dictionary\10_nested_dictionary.py
```
