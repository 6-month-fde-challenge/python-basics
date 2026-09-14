# Exercise 31 - Vehicle Rental System

One parent with **two** children, which is the first hierarchy in the course wide
enough to have siblings.

```
Vehicle
   |
   +---- Car     (seats)
   |
   +---- Bike    (engine_cc)
```

```python
Vehicle.is_valid_duration(3)     # True     <- no vehicle exists yet
Vehicle.is_valid_duration(0)     # False

swift   = Car("KA01AB1234", "Maruti", "Swift", 1_800, seats=5)
classic = Bike("KA05CD5678", "Royal Enfield", "Classic 350", 700, engine_cc=349)

swift.calculate_rent(7)          # 13,090.00   base, less 10%, plus insurance
classic.calculate_rent(7)        #  4,510.00   base, less 10%, plus a helmet
```

---

## Project objective

Exercises 28 and 30 each had one child. This one has two, and the interesting
property is what they do **not** share with each other.

`Car` and `Bike` never mention each other. Neither imports the other, neither
checks what the other is, and adding a third child - a van, a scooter - would
touch neither file nor either class. Everything they have in common they got from
`Vehicle`:

- the weekly discount, written once;
- `is_valid_duration()`, one rule about rental days for all three classes;
- the counter, the agency name and `__repr__`;
- `rent_out()`, `return_vehicle()` and `display_details()`.

The alternative - one `Vehicle` class with a `kind` attribute and
`if self.kind == "car"` scattered through it - works until the fourth kind of
vehicle, and then every one of those `if`s has to be found.

---

## Project structure

```
31_vehicle_rental_system/
├── README.md
├── vehicle.py             THE CLASSES - Vehicle, Car(Vehicle), Bike(Vehicle)
├── main.py                2 cars, 2 bikes, bookings, refusals
├── sample_output.txt      captured from a real run
└── class_hierarchy.png
```

---

## How to execute the program

```bash
python main.py             # the application
python vehicle.py          # the module's own self-test
```

or from the repo root:

```bash
python .\01_python_basics\31_vehicle_rental_system\main.py
```

No installation and no external packages. **Requires Python 3.7+** -
dictionaries keep their insertion order from 3.7, which the output relies on.
Verified on Python 3.12.10.

---

## The three classes

### `Vehicle` - the parent

| | |
|---|---|
| **Attributes** | `vehicle_number`, `brand`, `model`, `rent_per_day`, `days_hired`, `on_hire` |
| **Instance methods** | `calculate_rent()`, `rent_out()`, `return_vehicle()`, `display_details()`, `vehicle_type()`, `extras_for()` |
| **Static method** | `is_valid_duration(days)` - the one the assignment asks for |
| **Class variables** | `total_vehicles`, `agency`, `CURRENCY`, `MIN_DAYS`, `MAX_DAYS`, `WEEKLY_DAYS`, `WEEKLY_DISCOUNT` |
| **Class methods** | `get_total_vehicles()`, `set_agency()` |

### `Car(Vehicle)` and `Bike(Vehicle)` - the children

| | `Car` | `Bike` |
|---|---|---|
| **Adds** | `seats` | `engine_cc` |
| **Own class variables** | `INSURANCE_PER_DAY`, `LARGE_CAR_SEATS` | `HELMET_CHARGE`, `HIGH_CC` |
| **Overrides** | `__init__`, `vehicle_type()`, `extras_for()`, `calculate_rent()`, `display_details()` | the same five |
| **Own validation** | 2 to 9 seats | 50cc to 2000cc |

Each override is two or three lines, and every one of them starts with `super()`.

---

## The static method

```python
@staticmethod
def is_valid_duration(days):
    if isinstance(days, bool):
        return False
    if not isinstance(days, int):
        return False
    return Vehicle.MIN_DAYS <= days <= Vehicle.MAX_DAYS
```

It needs neither a vehicle nor the class, so it is static - and that is what lets
`main.py` call it before a single vehicle has been built:

| `days` | result | why |
|---|---|---|
| `1`, `3`, `7`, `90` | `True` | whole days inside the range |
| `0`, `-2` | `False` | a hire has to last at least a day |
| `91` | `False` | above `MAX_DAYS` |
| `2.5` | `False` | half a day is not a rental day |
| `True` | `False` | `bool` subclasses `int`; a hire of `True` would be a hire of 1 |
| `"3"` | `False` | not a number at all |

All three classes share it - `Car.is_valid_duration(7)` and
`Bike.is_valid_duration(7)` run the same function - so there is one answer to
"is this a legal hire?" rather than three that can drift apart.

---

## `calculate_rent(days)` - three definitions, one discount

```python
# Vehicle
def calculate_rent(self, days):
    if not self.is_valid_duration(days):
        raise ValueError(...)
    rent = self.rent_per_day * days
    if days >= self.WEEKLY_DAYS:
        rent *= (1 - self.WEEKLY_DISCOUNT / 100)
    return round(rent, 2)

# Car                                   # Bike
def calculate_rent(self, days):         def calculate_rent(self, days):
    return round(super().calculate_rent(days) + self.extras_for(days), 2)
```

Both children are the same one line. The difference is in `extras_for()`:

| | `extras_for(days)` | scales with the hire? |
|---|---|---|
| `Vehicle` | `0.0` | - |
| `Car` | `INSURANCE_PER_DAY * days` | **yes** |
| `Bike` | `HELMET_CHARGE` | no - charged once |

That is the point of splitting it out. `calculate_rent()` is identical in both
children, so the thing that actually differs is named and isolated.

```
vehicle                         1 day     3 days     7 days    14 days
----------------------------------------------------------------------
Maruti Swift                 2,050.00   6,150.00  13,090.00  26,180.00
Toyota Innova                3,450.00  10,350.00  21,910.00  43,820.00
Royal Enfield Classic 350      800.00   2,200.00   4,510.00   8,920.00
Honda Activa                   450.00   1,150.00   2,305.00   4,510.00
```

```
Where a 7-day Swift hire comes from:
  super().calculate_rent(7)  =  11,340.00   (7 x 1,800.00, less 10%)
  + insurance 7 x 250.00     =   1,750.00
  ----------------------------------------
  swift.calculate_rent(7)    =  13,090.00
```

The weekly discount is written **once**. Change `WEEKLY_DISCOUNT` in `Vehicle` and
all four rows of that table move together.

---

## `vehicle_type()` - a child overriding a method the parent calls

`Vehicle.display_details()` prints `self.vehicle_type()`, and both children
override it:

```python
# Car
return "Large Car" if self.seats >= self.LARGE_CAR_SEATS else "Car"

# Bike
return "High-capacity Bike" if self.engine_cc >= self.HIGH_CC else "Bike"
```

So the parent's own method prints "Large Car" for the Innova without `Vehicle`
knowing that seats exist. The forecourt table in `main.py` calls
`v.vehicle_type()` on every vehicle in one loop and never asks what class it is.

---

## Refusing before changing - twice

**`rent_out()`** prices the hire before it marks the vehicle as out:

```python
total = self.calculate_rent(days)   # raises on a bad duration, first
self.on_hire = True
self.days_hired += days
```

**`Car.__init__` and `Bike.__init__`** validate their own argument *before*
calling `super().__init__`, because `super().__init__` increments the counter:

```python
if not 2 <= seats <= 9:
    raise ValueError(...)
super().__init__(vehicle_number, brand, model, rent_per_day)
```

The run proves both: nine deliberately bad calls, three of them constructions, and
`Vehicle.get_total_vehicles()` is still 4.

| Call | Result |
|---|---|
| `swift.calculate_rent(0)` | `ValueError: rental duration must be a whole number of days between 1 and 90, got 0` |
| `swift.calculate_rent(2.5)` | `ValueError: … got 2.5` |
| `swift.calculate_rent(120)` | `ValueError: … got 120` |
| `swift.calculate_rent(1)` and `(90)` | **allowed** - both boundaries |
| `Car(..., seats=1)` | `ValueError: seats must be between 2 and 9, got 1` |
| `Bike(..., engine_cc=30)` | `ValueError: engine capacity must be between 50cc and 2000cc, got 30` |
| `Bike(..., rent_per_day=0)` | `ValueError: rent per day must be above zero, got 0` - from the **parent** |
| `swift.rent_out(2)` while out | `ValueError: KA01AB1234 is already out on hire` |

---

## Verified run

`python main.py` produces six sections in 173 lines:

```
1. is_valid_duration()        10 durations judged with 0 vehicles in existence
2. One parent, two children   4 vehicles, issubclass(Car, Bike) is False
3. calculate_rent(days)       a 4x4 price table, then where two of the cells came from
4. Renting the fleet out      4 bookings, 37,310.00, and a double-hire refused
5. What the agency refuses    9 refusals, then both boundaries accepted
6. display_details()          7 shared lines + 2, one agency rename, one loop
```

---

## Concepts used

**Inheritance with siblings** - one parent, two children, neither child aware of
the other; `issubclass(Car, Bike)` is `False` and that is the point

**Static methods** - `is_valid_duration()` as the assignment requires, shared by
all three classes and callable before any object exists

**Overriding** - `calculate_rent()`, `extras_for()`, `vehicle_type()`,
`display_details()` and `__init__` in both children, every one of them starting
from `super()`

**Template-method shape** - `calculate_rent()` is identical in both children
because the difference was pushed into `extras_for()`, which is the only method
either child really had to write

**Class variables** - one `total_vehicles` for the whole hierarchy; `agency`
renamed once and read by three classes; per-class constants (`INSURANCE_PER_DAY`,
`HELMET_CHARGE`) that live with the class they belong to

**Class methods** - `get_total_vehicles()`, `set_agency()`

**Ordering and validation** - children validating before `super().__init__`;
`rent_out()` pricing before mutating; both ends of the day range tested; the
bool-before-int check

**Carried forward** - the accumulator and champion patterns (exercise 18),
keyword arguments for `seats=` and `engine_cc=` (exercise 19), `try`/`except
ValueError` (exercise 23), and the module self-test (exercise 24)

---

## Learning / outcomes

1. **Two children beat one class with a `kind` field.** The `if` statements that
   a `kind` attribute would need are replaced by two small classes that do not
   have to be looked at together.

2. **Siblings should not know about each other.** `Car` and `Bike` share a parent
   and nothing else. A third vehicle type is a new class and no edits.

3. **Push the difference down, not the whole method.** `calculate_rent()` is one
   identical line in both children because `extras_for()` holds the part that
   actually varies. Overriding the whole calculation would have duplicated the
   weekly discount twice over.

4. **A parent can safely call a method its children override.**
   `display_details()` prints `self.vehicle_type()` and gets the child's answer.

5. **Static means "needs nothing", and that is a practical property.**
   `is_valid_duration()` is called on the class, inside `calculate_rent()`, and by
   `main.py` before any vehicle exists - three callers, one rule.

### Challenges faced

- **The weekly discount was applied twice to a car.** The first
  `Car.calculate_rent()` was a copy of the parent's body with insurance added,
  and when the parent later gained the discount, cars got it once from the copy
  and once from `super()`. Replacing the copy with a single `super()` call fixed
  it and shortened the method to one line.
- **A bike was charged for a helmet every day.** `extras_for()` started as one
  method that multiplied by `days` for both children. A helmet is a one-off, and
  the only way to see it was the 14-day column of the price table.
- **`calculate_rent(True)` returned a one-day hire.** `isinstance(True, int)` is
  `True`, so the range check passed - the same trap as exercises 26 to 30.
- **A refused bike was counted.** `Bike.__init__` called `super().__init__` first
  and validated `engine_cc` afterwards, so a 30cc bike incremented
  `total_vehicles` on its way to raising.
- **The Innova rented while it was already out.** `rent_out()` had no
  `on_hire` check at first, so the same vehicle could be booked twice and
  `days_hired` grew for a vehicle that was not on the forecourt.

---

## YouTube demonstration link

<your-youtube-video-link>

---

## Submission links

- **GitHub Repository:** `<your-public-github-repository-link>`
- **YouTube Explanation:** `<your-youtube-video-link>`
