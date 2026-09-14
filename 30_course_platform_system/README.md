# Exercise 30 - Course and PremiumCourse

Two classes, two methods with the same names in both, and no duplicated code:

```
Course
   |
PremiumCourse
```

```python
basics = Course("Python Basics", "V. Krishnan", 6, 4_999)
pro    = PremiumCourse("Python Pro", "V. Krishnan", 12, 14_999,
                       mentor_support=True, live_sessions=16)

basics.calculate_discount()    # 10
pro.calculate_discount()       # 38.0   =  super()'s 25  + 5 mentor + 8 sessions
```

---

## Project objective

Exercise 28 introduced inheritance. This one is about the half of it that is easy
to get wrong: **overriding a method without throwing away the parent's version**.

Both `calculate_discount()` and `show_course_details()` are defined in both
classes. In both cases the child's first line is a call to `super()`, and
everything after it is an addition:

```python
def calculate_discount(self):
    discount = super().calculate_discount()     # the platform-wide rules
    if self.mentor_support:
        discount += self.MENTOR_BONUS           # what being premium adds
    discount += self.live_sessions * self.LIVE_SESSION_BONUS
    return round(min(discount, self.MAX_DISCOUNT), 2)
```

The long-course bonus is written once, in `Course`. Change it there and premium
courses move with it. A `PremiumCourse` that re-implemented the whole calculation
would look identical today and be wrong on the first pricing change.

This is how a small online learning platform actually models a catalogue: one
class for what every course has, one subclass per tier, and the pricing rules in
one place each.

---

## Project structure

```
30_course_platform_system/
├── README.md
├── course.py              THE CLASSES - Course, and PremiumCourse(Course)
├── main.py                6 courses, discounts, enrolments, refusals
├── sample_output.txt      captured from a real run
└── method_overriding.png
```

---

## How to execute the program

```bash
python main.py             # the application
python course.py           # the module's own self-test
```

or from the repo root:

```bash
python .\01_python_basics\30_course_platform_system\main.py
```

No installation and no external packages. **Requires Python 3.7+** -
dictionaries keep their insertion order from 3.7, which the output relies on.
Verified on Python 3.12.10.

---

## The two classes

### `Course` - the parent

| | |
|---|---|
| **Attributes** | `name`, `instructor`, `duration_weeks`, `price`, `enrolled` |
| **The two methods the assignment names** | `show_course_details()`, `calculate_discount()` |
| **Other instance methods** | `course_type()`, `discount_amount()`, `final_price()`, `price_per_week()`, `enrol()`, `revenue()` |
| **Class variables** | `total_courses`, `platform`, `CURRENCY`, `BASE_DISCOUNT`, `LONG_COURSE_WEEKS`, `LONG_COURSE_BONUS`, `MAX_DISCOUNT` |
| **Class methods** | `get_course_count()`, `set_platform()` |
| **Static method** | `is_valid_price()` |

### `PremiumCourse(Course)` - the child

| | |
|---|---|
| **Adds** | `mentor_support`, `live_sessions` |
| **Adds** | `cost_per_session()`, `add_live_sessions()` |
| **Overrides** | `__init__`, `course_type()`, `calculate_discount()`, `show_course_details()`, `BASE_DISCOUNT` |
| **Inherits unchanged** | `discount_amount`, `final_price`, `price_per_week`, `enrol`, `revenue`, `is_valid_price`, `get_course_count`, `set_platform`, `__repr__` |

---

## `calculate_discount()` returns a percentage, not a price

That is a deliberate choice and the reason the override is three lines long.

If the parent returned a **price**, the child could only discount the already
discounted number, or ignore it and recompute from scratch. Returning a
**percentage** makes the parent's answer something the child can add to:

```
super().calculate_discount()   =    25%   (base 20 + long-course 5)
+ mentor                       =     5%
+ 16 live sessions x 0.5%      =   8.0%
--------------------------------------------
pro.calculate_discount()       =  38.0%
```

`discount_amount()` and `final_price()` then turn the percentage into money, once,
in the parent, for both classes.

### The cap is real

```
before  Python Pro: 38.0%
pro.add_live_sessions(60)
after   Python Pro: 60%   (capped at 60%)
```

`min(discount, self.MAX_DISCOUNT)` appears in both versions of the method, so
neither the base rules nor the premium bonuses can price a course below the
floor. Without it, a long enough premium course discounts past 100% and the shop
starts paying learners to enrol.

---

## `BASE_DISCOUNT` - overriding data instead of code

```python
class Course:
    BASE_DISCOUNT = 10

class PremiumCourse(Course):
    BASE_DISCOUNT = 20
```

`Course.calculate_discount()` reads `self.BASE_DISCOUNT`. When `super()` runs it
on a premium course, `self` is still the premium object, so the lookup finds
`20` - the parent's method, running the child's number:

| course | class | `BASE_DISCOUNT` | total |
|---|---|---|---|
| Python Basics | `Course` | 10 | 10% |
| Data Structures (10 weeks) | `Course` | 10 | 15% |
| Python Pro (12 weeks, mentor, 16 live) | `PremiumCourse` | 20 | 38% |
| Analytics Career Track (16 weeks, mentor, 24 live) | `PremiumCourse` | 20 | 42% |

Writing `Course.BASE_DISCOUNT` inside the method would have hard-wired 10 and
made the child's value decorative - the same mistake exercise 28's `BONUS_RATE`
warns about.

---

## `show_course_details()` - nine lines, then twelve

```python
def show_course_details(self):
    super().show_course_details()          # the parent's nine
    print(f"      mentor     : ...")
    print(f"      live        : ...")
    print(f"      per session: ...")
```

The parent's block already prints `self.course_type()`, which the child
overrides - so the parent's own code prints "Premium Course" without knowing that
premium courses exist. That is the whole idea behind putting `course_type()` in
`Course` at all.

---

## The counter, and the order of checks in `__init__`

```python
Course.total_courses += 1        # in Course.__init__, so it counts both classes
```

`PremiumCourse.__init__` does its own two checks **before** calling
`super().__init__`:

```python
if not isinstance(mentor_support, bool):
    raise ValueError(...)
...
super().__init__(name, instructor, duration_weeks, price)
```

The reason is the counter. `super().__init__` increments it, so validating
afterwards would count a course that is about to be rejected. The run proves it:
five deliberately bad constructions, and `Course.get_course_count()` is still 6.

| Call | Raised by | Result |
|---|---|---|
| `Course("Free", "X", 4, 0)` | parent | `price must be greater than zero, got 0` |
| `Course("Instant", "X", 0, 999)` | parent | `duration must be at least 1 week, got 0` |
| `Course("Odd", "X", 2.5, 999)` | parent | `duration must be a whole number of weeks, got 2.5` |
| `PremiumCourse(..., live_sessions=-3)` | **child** | `live_sessions must not be negative, got -3` |
| `PremiumCourse(..., mentor_support="yes")` | **child** | `mentor_support must be True or False, got 'yes'` |

`PremiumCourse` never wrote a price check or a duration check. It inherited both.

---

## Verified run

`python main.py` produces six sections in 166 lines:

```
1. Two classes, six courses       0 -> 6; the counter lives in Course
2. calculate_discount()           a discount table; BASE_DISCOUNT twice
3. What super() returned          25 + 5 + 8 = 38, then the 60% cap biting
4. show_course_details()          nine lines, then twelve
5. One loop over both classes     enrolments, revenue, a top earner
6. Class variable / class method  one platform name, one counter, 5 refusals
```

---

## Concepts used

**Inheritance** - `class PremiumCourse(Course)`, and a child that adds two
attributes and two methods to a working class

**Overriding** - `calculate_discount()`, `show_course_details()`, `course_type()`
and `__init__` all redefined; `BASE_DISCOUNT` overridden as data

**`super()`** - used as a **value**, not a formality: the child's discount starts
from the parent's answer, and the child's detail block starts from the parent's
output

**Class variables** - `total_courses` counting both classes from one place;
`platform` shared and renamed once; `MAX_DISCOUNT` as a floor both versions of the
method respect

**Class methods** - `get_course_count()` as the assignment asks, and
`set_platform()` assigning to `Course.platform` so children see it

**Static method** - `is_valid_price()`, reused from exercise 29

**Ordering** - the child validating before `super().__init__` so a refused object
is not counted

**Carried forward** - the accumulator and champion patterns (exercise 18),
default and keyword arguments (exercise 19), `try`/`except ValueError`
(exercise 23), and the module self-test (exercise 24)

---

## Learning / outcomes

1. **Override by extending, not by replacing.** `super().calculate_discount()` on
   the first line is the difference between two pricing rules and two copies of
   one pricing rule.

2. **Return a number the child can build on.** Had `calculate_discount()` returned
   a price, the override would have had to recompute everything. A percentage is
   composable; a total is not.

3. **`self.CONSTANT` beats `ClassName.CONSTANT` inside a method.** The first lets
   a subclass change the answer with one line of data; the second silently ignores
   it.

4. **A parent can call a method the child overrides.**
   `Course.show_course_details()` prints `self.course_type()` and gets "Premium
   Course" - the parent using behaviour it does not know about.

5. **Where you put `super().__init__()` is a decision, not a habit.** Anything
   with a side effect - a counter, a registry, a log line - makes the order of the
   child's checks and the parent's call matter.

### Challenges faced

- **Premium courses were discounted at 15%.** The first
  `PremiumCourse.calculate_discount()` was a copy of the parent's body with two
  lines added, and it hard-coded `10` instead of reading `BASE_DISCOUNT`. The
  override looked right in isolation and only the table exposed it.
- **A 90-week premium course had a negative price.** Without `MAX_DISCOUNT`, the
  bonuses stacked past 100%.
- **A rejected premium course was counted.** `super().__init__` ran first, bumped
  `total_courses`, and *then* the `live_sessions` check raised. The catalogue said
  seven courses and printed six.
- **`live_sessions=True` scheduled one session.** `bool` is an `int`, so the whole
  number check passed. The `bool` test had to come first - the same trap as
  exercises 26 to 29.
- **`cost_per_session()` divided by zero.** A premium course with mentor support
  and no live sessions is legitimate, and the first version had no guard for it.

---

## YouTube demonstration link

<your-youtube-video-link>

---

## Submission links

- **GitHub Repository:** `<your-public-github-repository-link>`
- **YouTube Explanation:** `<your-youtube-video-link>`
