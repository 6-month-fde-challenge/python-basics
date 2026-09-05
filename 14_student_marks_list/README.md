# Exercise 14 - Student Marks List

## What this exercise is about

Fifteen list operations applied in sequence to a set of exam marks - reading values by
position, slicing a range out of the middle, computing statistics, sorting both ways,
growing the list two different ways, removing a value, and searching it.

Operations 9 to 13 **modify** the list, so the program prints it after every change.
The order of the operations genuinely matters, and the output makes that visible.

## How the list evolves

```
[78, 85, 90, 67, 88, 92, 76]      original                    7 items
[67, 76, 78, 85, 88, 90, 92]      sort()                      7
[92, 90, 88, 85, 78, 76, 67]      sort(reverse=True)          7
... append(95)                                                8
... extend([81, 84])                                          10   <- grew by TWO
... remove(67)                                                 9
```

## Read-only results

```
marks[0]   -> 78          marks[-1]  -> 76
marks[2:6] -> [90, 67, 88, 92]
len 7   max 92   min 67   sum 576   average 82.29
```

## Two things worth explaining

**"Index 2 to 5" is ambiguous.** `marks[2:6]` includes index 5; `marks[2:5]` stops
before it. The program prints both alongside a position map, so either reading is
defensible.

**`index(88)` returns 2, not 4.** Sorting moved it. It was at index 4 in the original
list. Any position looked up after a sort refers to the *current* arrangement.

## `append()` versus `extend()`

Both are shown back to back, which is the point:

```
append([81, 84]) -> [78, 85, [81, 84]]   length 3   <- a list INSIDE the list
extend([81, 84]) -> [78, 85, 81, 84]     length 4   <- four separate marks
```

`append()` always adds **exactly one item**. `extend()` unpacks and adds each element.

## Bonus: `sort()` versus `sorted()`

`sort()` reorders the list you have and returns `None`. `sorted()` returns a **new**
sorted list and leaves the original alone. Use the second when the original order is
still needed.

## Run it

```bash
python 14_student_marks_list.py
```

or from the repo root:

```bash
python .\01_python_basics\14_student_marks_list\14_student_marks_list.py
```
