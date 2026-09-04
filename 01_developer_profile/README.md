# Exercise 01 - Developer Profile with Variables

## What this exercise is about

The starting point of the whole course: storing information in named variables and
finding out what Python thinks each one is. Eight facts about a developer are stored
in separate variables, printed, and then passed through `type()` so the data type of
each is visible.

The real lesson is that Python is **dynamically typed** - you never declare a type.
The value you assign decides it, and `type()` reports what Python worked out.

## What it stores

| Variable                                            | Example        | Type      |
| --------------------------------------------------- | -------------- | --------- |
| `name`, `city`, `company`, `learning_topic` | text           | `str`   |
| `age`                                             | 24             | `int`   |
| `years_of_experience`, `expected_salary`        | 1.5, 750000.00 | `float` |
| `likes_python`                                    | True           | `bool`  |

## Concepts

Variables, assignment, `str` / `int` / `float` / `bool`, `print()`, `type()`.

## Run it

```bash
python 01_developer_profile.py
```

or from the repo root:

```bash
python .\01_python_basics\01_developer_profile\01_developer_profile.py
```

## Note

The personal details near the top are placeholders. Replace them with your own -
the program behaves identically either way.
