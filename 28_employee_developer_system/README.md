# Exercise 28 - Employee and Developer, with Inheritance

Two classes, one of them 47 lines long, both of them complete employees.

```
Employee
   |
Developer
```

```python
rahul = Developer("E103", "Rahul Verma", 92_000, "Engineering", "Python", 6)

rahul.annual_salary()      # 1,104,000.0   <- Employee's code
rahul.code("fix a bug")    # "Rahul Verma is writing Python..."  <- Developer's
rahul.display_details()    # Developer's, which calls Employee's first
```

---

## Project objective

Exercises 26 and 27 each wrote one class. This one writes a second class that
**starts where the first one finished**.

`Developer` defines six things: `__init__`, `role()`, `display_details()`,
`is_senior()`, `code()` and `_clean_experience()`. It gets everything else -
`annual_salary()`, `bonus()`, `give_raise()`, the salary validation, the company
name, the employee counter, `__repr__` - from `Employee`, without a line of it
being repeated.

The alternative is a `Developer` class that copies all of `Employee` and adds two
fields. It works on the first day and drifts out of step on every day after it,
because a fix in one copy is not a fix in the other.

---

## Project structure

```
28_employee_developer_system/
├── README.md
├── 00_concepts.py          inherit, add, override, super(), isinstance
├── employee.py             THE CLASSES - Employee, and Developer(Employee)
├── main.py                 builds 5 people and demonstrates all of it
├── sample_output.txt       captured from a real run
└── inheritance.png
```

---

## How to execute the program

```bash
python 00_concepts.py     # the five ideas, standalone
python main.py            # the application
python employee.py        # the module's own self-test
```

or from the repo root:

```bash
python .\01_python_basics\28_employee_developer_system\main.py
```

No installation and no external packages. **Requires Python 3.7+** -
dictionaries keep their insertion order from 3.7, which the output relies on.
Verified on Python 3.12.10.

---

## Start with `00_concepts.py`

| # | Concept | What it shows |
|---|---|---|
| 1 | `class Dog(Animal)` | a child with an empty body already has `__init__` and `eat()` |
| 2 | adding | `Dog.fetch()` exists; `Animal.fetch()` is an `AttributeError` |
| 3 | overriding | three classes, one method name, three answers - and the MRO |
| 4 | `super()` | the parent's half of `__init__`, and what breaks when it is skipped |
| 5 | `isinstance` | a `Dog` **is** an `Animal`; `type()` says otherwise and is the wrong question |

---

## The two classes

### `Employee` - the parent

| | |
|---|---|
| **Attributes** | `employee_id`, `name`, `salary`, `department` |
| **Instance methods** | `annual_salary()`, `bonus()`, `give_raise()`, `role()`, `display_details()` |
| **Class variables** | `company`, `total_employees`, `CURRENCY`, `BONUS_RATE` |
| **Class methods** | `get_total_employees()`, `set_company()` |
| **Static method** | `_clean_salary()` |

### `Developer(Employee)` - the child

| | |
|---|---|
| **Adds** | `language`, `experience` |
| **Adds** | `is_senior()`, `code(task)` |
| **Overrides** | `__init__`, `role()`, `display_details()`, `BONUS_RATE` |
| **Inherits unchanged** | `annual_salary`, `bonus`, `give_raise`, `_clean_salary`, `get_total_employees`, `set_company`, `company`, `CURRENCY`, `__repr__` |

---

## `super()` - the two places it earns its keep

### In `__init__`

```python
def __init__(self, employee_id, name, salary, department, language, experience):
    super().__init__(employee_id, name, salary, department)
    self.language = language
    self.experience = self._clean_experience(experience)
```

The parent sets the four common fields, validates the salary **and** increments
the counter. `Developer` never has to know that a counter exists - which is why
`Employee.get_total_employees()` says 5 after two employees and three
developers are built, not 2.

Skipping `super().__init__()` is the classic mistake, and
`00_concepts.py` section 4 runs it on purpose: the object is built happily, and
the missing attribute only shows up later as an `AttributeError` in a method that
had nothing to do with it.

### In `display_details()`

```python
def display_details(self):
    super().display_details()          # the parent's six lines
    print(f"      language   : {self.language}")
    print(f"      experience : {self.experience:.0f} years")
    print(f"      senior     : {self.is_senior()}")
```

**Extend, do not replace.** Copying the parent's six `print()` calls would look
identical today. The difference appears the first time `Employee` gains a field.

---

## Overriding without rewriting: `BONUS_RATE`

`bonus()` is written once, in `Employee`, and never overridden:

```python
def bonus(self):
    return round(self.annual_salary() * self.BONUS_RATE, 2)
```

`Developer` changes one line - `BONUS_RATE = 0.08` - and the same inherited
method starts paying developers 8% instead of 5%:

```
Anita Desai         816,000.00 x 5% =    40,800.00
Rahul Verma       1,200,000.00 x 8% =    96,000.00
```

This works because `self.BONUS_RATE` is looked up on the object's class first and
only then on the parent - the same rule that makes method overriding work, applied
to data. Writing `Employee.BONUS_RATE` there instead would have hard-wired 5% and
broken it.

---

## `role()` and the MRO

```
Employee.__mro__   Employee -> object
Developer.__mro__  Developer -> Employee -> object
```

`role()` exists in both classes. Python walks that list left to right and stops at
the first match, so `rahul.role()` finds `Developer.role()` and
`anita.role()` falls through to `Employee.role()`. There is no magic beyond the
order of that list.

---

## `isinstance()` and what it buys

```python
isinstance(rahul, Developer)     # True
isinstance(rahul, Employee)      # True     <- a Developer IS an Employee
isinstance(anita, Developer)     # False    <- not the other way
type(rahul) is Employee          # False    <- type() ignores inheritance
```

The second line is the point of the whole exercise. Because it is `True`, one loop
handles the whole payroll:

```python
for person in staff:
    total += person.annual_salary()
```

Five calls, one definition, no `if` on the type. `isinstance()` appears exactly
once in `main.py` - to decide whether to print the language - and that is the only
place the difference matters.

---

## Verified run

`python main.py` produces six sections in 155 lines:

```
1. Two classes, five objects       the counter says 5, incremented in Employee
2. What Developer got for free     annual_salary, give_raise, company, CURRENCY
3. display_details()               the same six lines, plus three
4. Overriding                      role() twice, BONUS_RATE twice, bonus() once
5. isinstance()                    one loop over both classes, payroll 5,202,000
6. One counter, one company        set_company() reaches Developer too
```

---

## Concepts used

**Inheritance** - `class Developer(Employee)`, what a child gets without asking,
and that it goes one way only

**`super()`** - in `__init__` to reuse the parent's construction and counting, and
in `display_details()` to extend rather than replace the parent's output

**Overriding** - `role()` and `display_details()` redefined; `BONUS_RATE`
overridden as **data** so an inherited method changes behaviour without changing

**The MRO** - `__mro__` as the list Python walks, and why the child always wins

**`isinstance` / `issubclass` / `type`** - the "is a" question, and why `type()`
usually answers the wrong one

**Class variables across a hierarchy** - one `total_employees`, read by both
classes; `set_company()` assigning to `Employee.company` so children see it too

**Carried forward** - `@staticmethod` for the validators (exercise 26 and 27),
the bool-before-int check on every number, `__repr__` written once with
`type(self).__name__` so both classes print their own name, and the module
self-test under `if __name__ == "__main__"` (exercise 24)

---

## Learning / outcomes

1. **Inheritance is about the code you do not write.** `Developer` is 47 lines and
   behaves like a full employee because the other 83 lines exist once, one class
   up.

2. **`super()` in `__init__` is not a formality.** It is what sets four attributes
   and increments the counter. Forget it and the object is built with pieces
   missing, and the error surfaces somewhere else entirely.

3. **Extend the parent's method, do not copy it.** `super().display_details()`
   keeps one copy of six `print()` calls; duplicating them creates two that must
   be kept in step by hand.

4. **Overriding data is as useful as overriding methods.** One line -
   `BONUS_RATE = 0.08` - changes what an inherited method computes, without
   touching the method.

5. **`isinstance()` is what makes a mixed list a single list.** Once a
   `Developer` counts as an `Employee`, the payroll loop stops caring which is
   which.

### Challenges faced

- **The counter said 2.** `Developer.__init__` set its own four attributes
  directly instead of calling `super().__init__`, so
  `Employee.total_employees += 1` never ran for a developer. The count was quietly
  wrong, and nothing raised.
- **`rahul.bonus()` paid 5%.** `bonus()` was written as
  `self.annual_salary() * Employee.BONUS_RATE`. Naming the class instead of `self`
  pinned the rate to the parent and made `Developer.BONUS_RATE` decorative.
- **`display_details()` was copied.** The first `Developer.display_details()`
  reprinted all six of the parent's lines. Adding `company` to `Employee` updated
  one of the two blocks, and the bug was a missing line rather than a traceback.
- **`type(person) == Employee` skipped every developer.** An early payroll loop
  filtered on `type()`. `isinstance()` was the fix, and the reason the concepts
  file spends a section on the difference.

---

## YouTube demonstration link

<your-youtube-video-link>

---

## Submission links

- **GitHub Repository:** `<your-public-github-repository-link>`
- **YouTube Explanation:** `<your-youtube-video-link>`
