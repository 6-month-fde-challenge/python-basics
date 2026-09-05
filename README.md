# Python Basics

Twenty-one practical Python exercises covering the language fundamentals — data
types, sequences, loops and functions. Each lives in its own folder with a README
explaining what it covers.

Every program is self-contained and runs on its own:

```bash
python 01_developer_profile/01_developer_profile.py
```

**Requires Python 3.6+** (f-strings are used throughout). Verified on Python 3.12.
No external packages are needed anywhere in this module.

---

## Part 1 - Data types and data structures (exercises 01-14)

Single-file exercises. Several of these deliberately forbid loops, so every value is
reached by direct indexing or key access.

| # | Folder | Topic |
|---|--------|-------|
| 01 | [01_developer_profile](01_developer_profile/) | Variables and `type()` |
| 02 | [02_string_cleaning](02_string_cleaning/) | String methods and immutability |
| 03 | [03_student_string_challenge](03_student_string_challenge/) | Indexing and slicing |
| 04 | [04_data_type_laboratory](04_data_type_laboratory/) | All 8 types + type casting |
| 05 | [05_nested_list_challenge](05_nested_list_challenge/) | Nested lists, `[row][column]` |
| 06 | [06_shopping_cart](06_shopping_cart/) | List methods, `copy()` vs aliasing |
| 07 | [07_remove_duplicates_sets](07_remove_duplicates_sets/) | Sets for deduplication |
| 08 | [08_set_operations](08_set_operations/) | Union, intersection, difference |
| 09 | [09_tuple_challenge](09_tuple_challenge/) | Tuples and immutability |
| 10 | [10_nested_dictionary](10_nested_dictionary/) | Nested dicts, `[key][key]` |
| 11 | [11_product_dictionary](11_product_dictionary/) | Modelling an object as a dict |
| 12 | [12_student_profile_dict](12_student_profile_dict/) | The 7 dictionary methods |
| 13 | [13_ecommerce_dataset](13_ecommerce_dataset/) | List of dictionaries |
| 14 | [14_student_marks_list](14_student_marks_list/) | 15 list operations in sequence |

## Part 2 - Loops (exercises 15-18)

Multi-program sets. Each has its own README with per-question notes.

| # | Folder | Topic |
|---|--------|-------|
| 15 | [15_for_loop_fundamentals](15_for_loop_fundamentals/) | `for` fundamentals, `range()` |
| 16 | [16_loop_control](16_loop_control/) | `break`, `continue`, `for-else`, `enumerate()` |
| 17 | [17_while_loops](17_while_loops/) | `while`, menus, digit peeling |
| 18 | [18_real_world_loops](18_real_world_loops/) | Real-world data processing |

## Part 3 - Functions (exercises 19-20)

| # | Folder | Topic |
|---|--------|-------|
| 19 | [19_function_fundamentals](19_function_fundamentals/) | Parameters, arguments, `return`, defaults |
| 20 | [20_advanced_functions](20_advanced_functions/) | `*args`, `**kwargs`, lambda, recursion, scope |

## Part 4 - Final combined project (exercise 21)

| # | Folder | Topic |
|---|--------|-------|
| 21 | [21_combined_final_project](21_combined_final_project/) | 12 mini-applications combining everything above |

---

## A note on the numbering

Folder numbers are the **learning order**: reading them 01 through 21, top to bottom,
gives the sensible sequence. Data types and data structures first, then loops, then
functions, then the combined project that uses all of them.

---

## Concepts covered across the module

**Data types** - `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, `dict`, type
casting, mutability versus immutability

**Sequences** - indexing, negative indexing, slicing with `[start:stop:step]`, nesting

**Loops** - `for` over ranges and collections, `while` for condition-controlled
iteration, `break`, `continue`, `for-else`, `enumerate()`, nested loops

**Functions** - definition and call, parameters versus arguments, `return` versus
`print()`, default arguments, positional versus keyword arguments, `*args`,
`**kwargs`, lambda, `map()`, `filter()`, recursion, local and global scope

**Patterns written by hand** rather than with built-ins - the accumulator (instead of
`sum()`), the champion (instead of `max()` / `min()`), two-pointer comparison, digit
peeling with `% 10` and `// 10`, divisor testing up to the square root

**Practice** - input validation with `try/except`, guarding edge cases (empty lists,
zero divisors, `0!`, the number 1 in a prime test), menu-driven applications, and
docstrings on every function from exercise 19 onward.

---

## About this module

This is **module 01** of the [6-month FDE challenge](https://github.com/6-month-fde-challenge).
Each module of the challenge lives in its own repository under that organisation.
