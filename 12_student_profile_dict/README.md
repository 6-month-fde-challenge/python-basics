# Exercise 12 - Dictionary Methods

## What this exercise is about

A student record used as a workbench for the seven dictionary methods that matter
most. Twelve operations cover reading, bulk updating, deleting, safe access and
copying.

## The seven methods, grouped by job

| Job | Methods |
|---|---|
| **Look at** the whole dictionary | `keys()`, `values()`, `items()` |
| **Read** one value safely | `get()` |
| **Change** the dictionary | `update()`, `pop()` |
| **Duplicate** it | `copy()` |

## `get()` versus `[]`

Both return `Rahul` for `"name"`. The difference only appears on a key that is not
there:

```
student["city"]                ->  KeyError   (crashes)
student.get("city")            ->  None
student.get("city", "Unknown") ->  Unknown
```

## `update()` - the bulk version

One call did three things: updated `marks` (92 to 95) and `city` (Bangalore to
Hyderabad) because those keys existed, and **created** `grade` because it did not.
Same rule as `[] =`, applied to many keys at once.

## `copy()` - the part carrying the most weight

Three things the program demonstrates:

1. `student.copy()` makes a real duplicate - `student is student_copy` prints `False`.
2. Editing the copy leaves the original completely untouched.
3. **The contrast:** `alias = student` is *not* a copy. It is a second **name for the
   same dictionary**, so `alias["name"] = "CHANGED"` changed the original too.

Then the honest caveat: `copy()` is **shallow**. Top-level values are independent, but
a dictionary nested *inside* stays shared. For that you need `copy.deepcopy()`.

## Run it

```bash
python 12_student_profile_dict.py
```

or from the repo root:

```bash
python .\01_python_basics\12_student_profile_dict\12_student_profile_dict.py
```
