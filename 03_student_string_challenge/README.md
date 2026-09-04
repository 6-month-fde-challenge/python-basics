# Exercise 03 - String Indexing and Slicing

## What this exercise is about

Reaching into the string `"python programming for data science"` by **position** rather
than by method. Thirteen operations pull out single characters, ranges of characters,
and a fully reversed copy - then apply the familiar case and search methods for
comparison.

The core skill is **slicing**: `[start : stop : step]`, where the stop is always
excluded and a negative step walks backwards.

## Key results

```
[0]      -> 'p'                              first character
[-1]     -> 'e'                              last character, length-independent
[0:6]    -> 'python'                         6 characters, indexes 0-5
[-7:]    -> 'science'                        last seven
[::-1]   -> 'ecneics atad rof gnimmargorp nohtyp'
count('a')          -> 3
find('programming') -> 7
```

## Worth knowing

- The **stop is excluded**: `[0:6]` gives six characters, not seven. This is the
  single most common slicing mistake.
- `[::-1]` reverses **characters**, not words - which is why the output reads
  backwards rather than reordering the sentence.
- Operation 8 (`lower()`) produces output identical to the input, because the string
  is already lowercase. That is correct, not a skipped step.

## Run it

```bash
python 03_student_string_challenge.py
```

or from the repo root:

```bash
python .\01_python_basics\03_student_string_challenge\03_student_string_challenge.py
```
