# Exercise 02 - String Cleaning Challenge

## What this exercise is about

Taking one messy string - `"   Welcome To Python Programming Class   "`, padded with
stray spaces - and running ten different string methods over it: trimming, changing
case, replacing text, testing how it starts and ends, counting, searching and
splitting.

The idea that ties them together is **immutability**. Strings cannot be changed. Every
method here returns a *brand new string* and leaves the original exactly as it was,
which is why each result has to be stored in its own variable. The program reprints
the original at the end to prove it survived untouched.

## Operations covered

`strip()` · `lower()` · `upper()` · `title()` · `replace()` · `startswith()` ·
`endswith()` · `count()` · `find()` · `split()`

## Key results

```
strip()      -> 'Welcome To Python Programming Class'   (41 chars -> 35)
replace()    -> Welcome To Advanced Python Programming Class
count('o')   -> 4        (case-sensitive)
find('Programming') -> 18
split()      -> ['Welcome', 'To', 'Python', 'Programming', 'Class']
```

## Worth knowing

- `strip()` trims **only the ends**. Spaces between words survive.
- `find()` returns **-1** when the text is absent - it does not raise an error.
- `split()` is the only one that changes the data *type*: string becomes list.

## Run it

```bash
python 02_string_cleaning.py
```

or from the repo root:

```bash
python .\01_python_basics\02_string_cleaning\02_string_cleaning.py
```
