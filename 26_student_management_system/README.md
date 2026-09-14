# Exercise 26 - Student Management System

The first class in the course. Everything before this exercise stored a student
in a dictionary; this one gives the student a **type**.

```python
aarav = Student("Aarav Sharma", "aarav@example.com", "S101", "Python")
aarav.update_marks("Python", 88)
aarav.average_marks()            #  88.0
Student.get_total_students()     #  1
```

---

## Project objective

Exercise 12 built a student out of a dictionary and exercise 13 built a list of
them. Both worked. Both had the same problem: the data and the code that
understood the data lived in different places, and nothing stopped a caller
writing `student["marks"] = "eighty"`.

A class closes that gap. `Student` holds the five fields the assignment names -
name, email, student ID, course and marks - **and** the four operations that make
sense on them. A mark can now only get in through `update_marks()`, which is
where the validation is.

```
12   a dict of fields                     data
13   a list of dicts                      data, in bulk
26   a class with methods                 data + the code that owns it   <- here
```

---

## Project structure

```
26_student_management_system/
├── README.md
├── 00_concepts.py          class, object, __init__, self, class var, classmethod
├── student.py              THE CLASS - 5 attributes, 6 instance methods, 3 class-level
├── main.py                 builds 5 students and demonstrates all of it
├── sample_output.txt       captured from a real run
└── classes_objects.png
```

---

## How to execute the program

```bash
python 00_concepts.py     # the six ideas, standalone
python main.py            # the application
python student.py         # the class's own self-test
```

or from the repo root:

```bash
python .\01_python_basics\26_student_management_system\main.py
```

No installation and no external packages. **Requires Python 3.7+** -
dictionaries keep their insertion order from 3.7, which the output relies on.
Verified on Python 3.12.10.

---

## Start with `00_concepts.py`

It imports nothing from the application, runs on its own, and prints real output
for each of the six ideas the class is built from:

| # | Concept | What it shows |
|---|---|---|
| 1 | class and object | `Dog()` twice gives two objects; `first is second` is `False` |
| 2 | `__init__` | runs at build time; `self.x = ...` is what creates an attribute |
| 3 | `self` | `rocky.speak()` **is** `Dog.speak(rocky)` |
| 4 | class variable | one shared copy - and the assignment trap that hides it |
| 5 | `@classmethod` | `cls` is the class; `Dog.get_count()` needs no dog |
| 6 | the three method kinds | instance / class / static, side by side |

---

## The class

### Attributes - the five the assignment asks for

| Attribute | Example | Set where |
|---|---|---|
| `name` | `"Aarav Sharma"` | `__init__` |
| `email` | `"aarav@example.com"` | `__init__` |
| `student_id` | `"S101"` | `__init__` |
| `course` | `"Python"` | `__init__` |
| `marks` | `{"Python": 88, "Maths": 92}` | `__init__`, then `update_marks()` |

`marks` is a dictionary rather than a list because a bare `[88, 92, 76]` cannot
answer "what did they get in Maths?" - and exercise 10 already made the case for
keys over positions.

### Instance methods - one object at a time

| Method | Returns | Notes |
|---|---|---|
| `update_marks(subject, score)` | the previous score, or `None` | the only door marks come in through |
| `average_marks()` | `float` | `0.0` for a student with no marks, not a crash |
| `highest_subject()` | `(subject, score)` or `None` | the champion pattern from exercise 18 |
| `grade()` | `"A+"` … `"F"` | reads `GRADE_BANDS` |
| `has_passed()` | `bool` | every subject at or above `PASS_MARK` |
| `display_details()` | `None` | the **only** method that prints |

Everything except `display_details()` returns instead of printing, which is the
rule from exercise 19 - a method that prints can only ever be used for printing.

### Class variables - one copy, shared by everybody

```python
total_students = 0
institute = "Nova Institute of Technology"
PASS_MARK = 40
MAX_MARK = 100
GRADE_BANDS = ((90, "A+"), (80, "A"), ...)
```

`total_students` is the counter the assignment asks for. It is incremented in
`__init__`, so it counts objects that were actually built and cannot be fooled -
section 6 of `main.py` quietly creates a sixth student to test the validation, and
the closing count says 6.

### Class methods - asked of the class

```python
@classmethod
def get_total_students(cls):
    return cls.total_students
```

`Student.get_total_students()` needs no student. Asking one student how many
students exist would be a strange question, which is exactly the signal that a
method should take `cls` rather than `self`.

`set_institute(name)` is the second one, and it changes the institute for every
student at once, because it assigns to `cls.institute` - the single shared copy.

### One static method

`is_valid_email(email)` needs neither the object nor the class, only its
argument, so it is a `@staticmethod`. Exercise 29 is built around that decision.

---

## `Student.count` versus `self.count` - the bug that does not raise

The counter says:

```python
Student.total_students += 1        # correct
```

not:

```python
self.total_students += 1           # silently counts nothing
```

The second one *reads* the class variable (0), adds 1, and then **assigns the
result to the object** - creating a brand-new instance variable that shadows the
class variable. Every student ends up with their own `total_students = 1`, the
class variable stays at 0, and nothing raises.

`00_concepts.py` section 4 shows the same shadowing with `rocky.species`.

---

## Validation

`update_marks()` is the only way a score enters the object, so it is the only
place that has to check one:

| Call | Result |
|---|---|
| `update_marks("Python", 120)` | `ValueError: score for 'Python' must be between 0 and 100, got 120` |
| `update_marks("Python", -5)` | `ValueError: … got -5` |
| `update_marks("Python", "eighty")` | `ValueError: score for 'Python' must be a number, got 'eighty'` |
| `update_marks("Python", True)` | `ValueError: … got True` |
| `update_marks("   ", 50)` | `ValueError: subject must be a non-empty string` |

**`True` is rejected first, on purpose.** `bool` is a subclass of `int`, so
`isinstance(True, int)` is `True` and a score of `True` would be stored, averaged
as `1`, and quietly wrong. The bool check has to come *before* the number check
or it never runs - the same trap exercise 24 hit in `require_number()`.

### The copied dictionary

```python
self.marks = {}
if marks:
    for subject, score in marks.items():
        self.update_marks(subject, score)
```

The dictionary passed in is not kept. Every value is fed back through
`update_marks()`, which validates it and stores it in a **new** dictionary. Two
things follow: bad marks cannot sneak in through the constructor, and two
students built from the same `defaults` dict do not share one dictionary - the
aliasing trap from exercise 06.

---

## Verified run

`python main.py` produces six sections in 150 lines:

```
1. One class, five objects        0 students, then 5, from one class
2. display_details()              five blocks, including one with no marks
3. update_marks()                 Meera re-sits JavaScript: 33 -> 68, FAIL -> PASS
4. average_marks()                a table, a class average of 77.60, a top student
5. class variable / class method  one counter, one institute, changed once
6. Validation                     five refusals and a static method
```

---

## Concepts used

**Classes and objects** - `class` as a blueprint, calling the class to build an
object, `type()` on an object, two objects of the same class being independent

**`__init__`** - the constructor, never called by hand; `self.x = value` as the
thing that creates an attribute; optional arguments with a default

**`self`** - the object the method was called on, and why `rocky.speak()` is
`Dog.speak(rocky)`

**Instance methods** - returning values rather than printing; one method that
prints, on purpose; guarding the empty case in every method that reads `marks`

**Class variables** - a shared counter, a shared name, and shared constants
(`PASS_MARK`, `MAX_MARK`, `GRADE_BANDS`); the `self.x += 1` shadowing trap

**Class methods** - `@classmethod`, `cls`, and choosing `cls` over `self` when the
answer does not depend on any one object

**Static methods** - `@staticmethod` for a helper that needs neither

**Carried forward** - the accumulator and champion patterns instead of `sum()`
and `max()` (exercise 18), `try`/`except ValueError` around bad input
(exercise 23), the module self-test under `if __name__ == "__main__"`
(exercise 24), and copying a mutable argument instead of storing it
(exercise 06)

---

## Learning / outcomes

1. **A class is a dictionary that knows the rules about itself.** The fields are
   the same five as exercise 12. What is new is that no caller can write a mark
   of 120, because the only way in runs a check.

2. **`self` is not magic, it is the first parameter.** Once `rocky.speak()` is
   read as `Dog.speak(rocky)`, every question about `self` answers itself.

3. **Ask "what does this method need?" to pick its kind.** `average_marks()`
   needs one student. `get_total_students()` needs the class. `is_valid_email()`
   needs neither. That question decides `self`, `cls` or `@staticmethod` every
   time, and it is a better rule than "put it wherever it fits".

4. **A class variable is one object shared by every instance.** That is what
   makes the counter work, and it is also what makes `self.total_students += 1`
   a bug rather than a shortcut.

5. **Validate at the edge, once.** `update_marks()` is the only door, so it is
   the only place that checks. `__init__` reuses it rather than repeating it.

### Challenges faced

- **The counter counted nothing.** The first `__init__` said
  `self.total_students += 1`. Every student reported 1 and
  `Student.get_total_students()` reported 0. Nothing raised - the assignment had
  created an instance variable that hid the class variable.
- **`average_marks()` crashed on a new student.** Rohan is built with no marks at
  all, and `total / len(self.marks)` was a `ZeroDivisionError` the first time the
  demo ran. Every method that reads `marks` now checks it is not empty first.
- **Two students shared one marks dictionary.** An early `__init__` did
  `self.marks = marks or {}`. Building two students from the same literal dict
  gave them one dictionary between them, and updating one updated both - exercise
  06's aliasing trap, wearing a class.
- **`update_marks("Python", True)` scored 1.** `isinstance(True, int)` is `True`,
  so the number check passed. The bool test had to move above it.

---

## YouTube demonstration link

<your-youtube-video-link>

---

## Submission links

- **GitHub Repository:** `<your-public-github-repository-link>`
- **YouTube Explanation:** `<your-youtube-video-link>`
