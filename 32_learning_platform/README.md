# Exercise 32 - Learning Platform

The last exercise of the module, and the one that uses all of it: a class
hierarchy, a class that owns the hierarchy, five exception classes, and a package
that `main.py` only imports.

```
User
  |
  +---- Student    (course, completed assignments)
  |
  +---- Mentor     (expertise, students assigned)
```

```python
from platform_app import LearningPlatform

site  = LearningPlatform("Nova Learn")
aarav = site.register_student("Aarav Sharma", "aarav@example.com", "Python Basics")
guide = site.register_mentor("V. Krishnan", "krishnan@example.com", "Python, Backend")

site.assign_mentor(aarav.user_id, guide.user_id)
site.submit_assignment(aarav.user_id, "Loops and conditionals")
site.report()
```

---

## Project objective

Exercises 26 to 31 each isolated one idea. This one puts them in the same program
and adds the piece none of them needed: **a class that is not part of the
hierarchy at all.**

`Student` and `Mentor` are *kinds of* `User` - that is inheritance.
`LearningPlatform` *has* users - that is composition. It holds a dictionary of
them, refuses a duplicate email, finds one by id, and knows nothing about how a
student stores assignments.

Getting that split right is the difference between a design that survives a third
kind of user and one that does not.

### Every requirement, and where it is

| Requirement | Where |
|---|---|
| Inheritance | `Student(User)`, `Mentor(User)` in `users.py` |
| Constructors | `__init__` in all three, both children calling `super().__init__` |
| At least one class variable | `User.total_users`, `User.platform_name`, `ID_PREFIX`, `_sequence`, `REQUIRED_ASSIGNMENTS`, `MAX_STUDENTS` |
| At least one class method | `get_total_users()`, `set_platform_name()`, `_new_id()` |
| At least one static method | `User.is_valid_email()` |
| Multiple objects | 5 students, 2 mentors, 1 platform |
| Instance methods | `assign_course()`, `submit_assignment()`, `assign_student()`, `display_details()`, … |
| Registering students | `LearningPlatform.register_student()` |
| Assigning a course | `LearningPlatform.assign_course()` |
| Submitting an assignment | `LearningPlatform.submit_assignment()` |
| Displaying student information | `Student.display_details()` |
| Displaying mentor information | `Mentor.display_details()` |
| Counting total users | `User.get_total_users()` **and** `site.total_users()` - see below |

---

## Project structure

```
32_learning_platform/
├── README.md
├── main.py                      a program that IMPORTS the package
├── sample_output.txt            captured from a real run
├── oop_project.png
└── platform_app/                <- THE PACKAGE
    ├── __init__.py                  the front door: what the package offers
    ├── exceptions.py                5 error classes
    ├── users.py                     User, Student(User), Mentor(User)
    └── registry.py                  LearningPlatform - owns the users
```

Import order is dependency order, so there are no circular imports:

```
exceptions   imports nothing of ours
users        imports exceptions
registry     imports exceptions and users
__init__     imports all three
```

That is exercise 24's rule, reused.

---

## How to execute the program

```bash
python main.py
```

or from the repo root:

```bash
python .\01_python_basics\32_learning_platform\main.py
```

No installation and no external packages. **Requires Python 3.7+** -
dictionaries keep their insertion order from 3.7, which the output relies on.
Verified on Python 3.12.10.

---

## The hierarchy

### `User` - what every account has

| | |
|---|---|
| **Attributes** | `name`, `email`, `user_id` |
| **Instance methods** | `role()`, `display_details()` |
| **Class variables** | `total_users`, `platform_name`, `ID_PREFIX`, `_sequence` |
| **Class methods** | `get_total_users()`, `set_platform_name()`, `_new_id()` |
| **Static method** | `is_valid_email()` |

### `Student(User)`

| | |
|---|---|
| **Adds** | `course`, `completed_assignments`, `mentor` |
| **Adds** | `assign_course()`, `submit_assignment()`, `completed_count()`, `progress()`, `has_finished()` |
| **Overrides** | `__init__`, `role()`, `display_details()`, `ID_PREFIX`, `_sequence` |

### `Mentor(User)`

| | |
|---|---|
| **Adds** | `expertise`, `students` |
| **Adds** | `assign_student()`, `student_count()`, `is_full()`, `average_progress()` |
| **Overrides** | `__init__`, `role()`, `display_details()`, `ID_PREFIX`, `_sequence` |

---

## `_new_id()` - one class method, two counters

```python
@classmethod
def _new_id(cls):
    cls._sequence += 1
    return f"{cls.ID_PREFIX}{cls._sequence:03d}"
```

Written once in `User`, and it produces `S001…S005` for students and `M001…M002`
for mentors, because `cls` is whichever class was called:

```
Student.ID_PREFIX / _sequence  -> S / 5
Mentor.ID_PREFIX  / _sequence  -> M / 2
User.ID_PREFIX    / _sequence  -> U / 0   <- never used, never moved
```

The mechanism is the class-variable shadowing that exercises 26 and 27 warned
about, this time put to work. `cls._sequence += 1` **reads** `User._sequence`
(if the subclass has none) and **assigns** to the subclass - so each subclass
quietly gets a counter of its own. `Student` and `Mentor` both declare
`_sequence = 0` so that is a decision in the source rather than an accident of
the first call.

---

## Inheritance and composition, side by side

```python
class Student(User):                 # a student IS a user
    ...

class LearningPlatform:              # a platform HAS users
    def __init__(self, name):
        self.users = {}
```

`LearningPlatform` is the only class in the project that is not part of the
hierarchy, and it is the one that holds everything:

- `register_student()` / `register_mentor()` build the object and store it;
- `_register()` is shared by both and is the only place a duplicate email is
  refused;
- `find()` turns a `KeyError` into an `UnknownUserError` with `raise … from None`;
- `students()` and `mentors()` filter the same dictionary with `isinstance()`;
- `report()` loops over every user and asks `isinstance()` **once**, to choose
  which detail column to print.

The alternative - making `LearningPlatform` a subclass of something, or giving
`User` a list of all users - couples the container to the contents and makes the
counting question below unanswerable.

---

## Two counts, on purpose

```
User.total_users            -> 9
site.total_users()          -> 8
```

They answer different questions and both are right:

```
7 registered in section 1
+1 'No Course', registered in section 6 and never given a course
+1 'Someone Else', built and then refused for a duplicate email
```

`User.total_users` is a class variable incremented in `User.__init__`, so it
counts every `User` object whose constructor **finished** - including one that was
built and then rejected by the platform a moment later. `site.total_users()` is
`len(self.users)`, so it counts what the platform actually kept.

This is worth noticing rather than hiding: a class variable counts objects, a
container counts membership, and picking the wrong one is how a dashboard ends up
reporting a user who does not exist.

---

## `display_details()` in three classes

```python
# User            # Student                       # Mentor
                  def display_details(self):      def display_details(self):
4 lines               super().display_details()       super().display_details()
                      ... course, mentor,             ... expertise, students,
                          assignments                     capacity
```

The parent's four lines include `self.role()`, which both children override. So
`User.display_details()` prints "Mentor" without `User` ever learning that mentors
exist - the same trick as exercises 30 and 31.

---

## Five exception classes, one `except`

```
Exception
 └── PlatformError                base - one clause catches all
      ├── ValidationError             .field  .value  .reason
      ├── DuplicateUserError          .email  .existing_id
      ├── UnknownUserError            .user_id
      └── MentorFullError             .mentor .limit
```

`main.py` section 6 runs eight different failures through one handler:

| Case | Raises |
|---|---|
| a duplicate email | `DuplicateUserError: aarav@example.com is already registered as S001` |
| a malformed email | `ValidationError: email 'nope' is not usable: must look like name@example.com` |
| a blank name | `ValidationError: name '   ' is not usable: must be a non-empty string` |
| an unknown id | `UnknownUserError: no user with id 'S999'` |
| a course for a mentor | `ValidationError: user 'M001' is not usable: is not a student` |
| an assignment before a course | `ValidationError: … the student is not on a course yet` |
| the same assignment twice | `ValidationError: … has already been submitted` |
| a fourth student for a full mentor | `MentorFullError: V. Krishnan already has 3 students, which is the maximum` |

Each carries its own attributes rather than one flattened string, so a caller can
act on the failure instead of parsing the message:

```python
except MentorFullError as error:
    error.mentor.name     # 'V. Krishnan'
    error.limit           # 3
```

That is exercise 23's lesson, applied to a hierarchy.

---

## Verified run

`python main.py` produces seven sections in 192 lines:

```
1. Registering users            7 users, ids generated by one class method
2. Course and mentor            a course assigned, 5 students paired to 2 mentors
3. Submitting assignments       15 assignments; one student finishes at 100%
4. Displaying                   a student block and a mentor block
5. The whole platform           one table over two classes, mentor averages
6. What the platform refuses    8 failures, one except clause
7. Class variable / method      one rename across three classes, two counts
```

---

## Concepts used

**Inheritance** - `Student(User)`, `Mentor(User)`, siblings that never mention
each other, and a parent method that calls an overridden one

**Composition** - `LearningPlatform` **has** users rather than being one, and the
dictionary it holds is the only list of members

**Constructors** - `__init__` in four classes; both children calling
`super().__init__`; `Mentor` validating its own argument first; per-object
mutable state (`completed_assignments`, `students`) built inside `__init__` so
two objects never share one list

**Class variables** - `total_users` counting the whole hierarchy, `platform_name`
renamed once and seen by three classes, `ID_PREFIX` and `_sequence` overridden per
subclass, `REQUIRED_ASSIGNMENTS` and `MAX_STUDENTS` as per-class rules

**Class methods** - `get_total_users()`, `set_platform_name()`, and `_new_id()`
using `cls` to produce different ids for different subclasses

**Static methods** - `is_valid_email()`, called by `__init__` before the object
exists and by `main.py` before any user exists

**Packages** (exercise 24) - `__init__.py` as a front door, `__all__`, relative
imports, dependency order as import order, and `main.py` living outside the
package it uses

**Custom exceptions** (exercise 23) - one base, four subclasses, attributes on the
exception, `raise … from None` to hide a `KeyError` that would only confuse

**Carried forward** - the accumulator and champion patterns (exercise 18),
`enumerate()` (exercise 16), default and keyword arguments (exercise 19), dict and
list handling (exercises 06 to 13), and the aliasing trap avoided by building each
list inside `__init__` (exercise 06)

---

## Learning / outcomes

1. **"Is a" is inheritance; "has a" is composition.** A student is a user, so
   `Student` subclasses `User`. A platform has users, so `LearningPlatform` holds
   a dictionary. Trying to express the second as inheritance is the most common
   way an OOP design goes wrong early.

2. **`cls` is what makes one class method behave differently per subclass.**
   `_new_id()` is four lines and produces two independent id series, because
   `cls` is `Student` for a student and `Mentor` for a mentor.

3. **Two counters can both be correct.** `User.total_users` counts objects built;
   `site.total_users()` counts users registered. Knowing which question is being
   asked is the whole job.

4. **A hierarchy of exceptions turns eight failures into one handler.** The
   caller writes `except PlatformError` and still has `.mentor`, `.limit`,
   `.existing_id` available when it wants to do something specific.

5. **Mutable state belongs in `__init__`, never in the class body.**
   `completed_assignments = []` as a class variable would have given every
   student on the platform the same list. Building it per object is one line and
   the difference between a working platform and a very confusing bug.

### Challenges faced

- **Every student shared one list of assignments.** The first `Student` declared
  `completed_assignments = []` in the class body. One submission appeared on all
  five students - exercise 06's aliasing trap, promoted to a class variable, and
  the reason `main.py` prints the `is` comparison between two students' lists.
- **Every user got the id `U001`.** `_new_id()` was written as a
  `@staticmethod` reading `User._sequence`, so there was one counter and one
  prefix. Making it a `@classmethod` and giving each subclass its own `_sequence`
  fixed both at once.
- **A duplicate registration still incremented the counter.** It still does - and
  once the reason was understood, the right fix was to explain the two counts
  rather than to hide one. `User.__init__` genuinely finished; the platform simply
  refused to keep the object.
- **`find()` raised `KeyError` from inside `UnknownUserError`.** Without
  `from None`, the traceback showed "During handling of the above exception,
  another exception occurred" and two errors for one mistake.
- **`assign_mentor()` linked one side only.** An early version appended the
  student to `mentor.students` and left `student.mentor` as `None`, so a student
  page said "no mentor" while the mentor's page listed them. Both sides are now
  set in `Mentor.assign_student()`, which is the one place that knows about the
  link.
- **A mentor could be given the same student twice.** The capacity check passed,
  because two entries for one student are still two entries. `assign_student()`
  now checks membership before the count.

---

## YouTube demonstration link

<your-youtube-video-link>

---

## Submission links

- **GitHub Repository:** `<your-public-github-repository-link>`
- **YouTube Explanation:** `<your-youtube-video-link>`
