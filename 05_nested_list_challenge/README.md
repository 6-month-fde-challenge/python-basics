# Exercise 05 - Nested Lists

## What this exercise is about

Working with a list whose items are themselves lists - three student records, each
holding a name, an age and a course. Every value is reached by **direct indexing**;
loops are deliberately not used, which forces the addressing itself to be understood.

## The mental model

A nested list is a table. The first index picks the **row**, the second picks the
**column**.

```
                   [0]        [1]     [2]
                   name       age     course
students[0]  ->   "Rahul"      21     "Python"
students[1]  ->   "Priya"      22     "Data Science"
students[2]  ->   "Aman"       20     "Machine Learning"
```

`students[1][2]` is not one special operation - it is two ordinary ones. `students[1]`
hands back the whole inner list, then `[2]` is applied to *that result*.

## The clearest proof

- `students[1]` -> a **list**: `['Priya', 22, 'Data Science']`
- `students[1][0]` -> a **str**: `'Priya'`

One index gives you a container; the second reaches inside it.

## Also covered

- **Modifying** one cell: `students[0][2] = "AI"` - the row count stays at 3.
- **Adding** a whole row: `students.append([...])` - the table grows to 4.
- Negative indexing: `students[-1][-1]` is the last student's course.

## Run it

```bash
python 05_nested_list_challenge.py
```

or from the repo root:

```bash
python .\01_python_basics\05_nested_list_challenge\05_nested_list_challenge.py
```
