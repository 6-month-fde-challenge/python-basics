# Exercise 27 - Bank Account System

Exercise 26 showed what a class variable **is**. This one is built around what a
class variable is *for*: one bank name, stored once, changed once, seen by every
account.

```python
acc = BankAccount("Aarav Sharma", "AC1001", 25_000)
acc.deposit(5_000)                        #  30000.0
acc.withdraw(99_000)                      #  InsufficientFundsError
BankAccount.rename_bank("Nova Federal")   #  every account, one call
```

---

## Project objective

Money is the thing a program is least allowed to get wrong, so the assignment's
one hard rule - **a user cannot withdraw more than is available** - is the spine
of the exercise. Everything else hangs off it:

- the check runs **before** the subtraction, so a refused withdrawal changes
  nothing at all;
- a refusal is an **exception**, not a `False` return, because a caller who
  ignores `False` silently loses money and a caller who ignores an exception
  cannot;
- `transfer_to()` calls `withdraw()` first for exactly that reason - the wrong
  order would credit the other account with money that was never taken out.

The class variables are the second half. `bank_name` is not copied into each
account, so renaming the bank is one assignment rather than a loop over every
customer.

---

## Project structure

```
27_bank_account_system/
├── README.md
├── account.py              BankAccount + 3 exception classes
├── main.py                 opens 4 accounts and demonstrates all of it
├── sample_output.txt       captured from a real run
└── class_variables.png
```

---

## How to execute the program

```bash
python main.py              # the application
python account.py           # the class's own self-test
```

or from the repo root:

```bash
python .\01_python_basics\27_bank_account_system\main.py
```

No installation and no external packages. **Requires Python 3.7+** -
dictionaries keep their insertion order from 3.7, which the output relies on.
Verified on Python 3.12.10.

---

## The class

### Attributes

| Attribute | Example | Kind |
|---|---|---|
| `holder_name` | `"Aarav Sharma"` | instance |
| `account_number` | `"AC1001"` | instance |
| `balance` | `25000.0` | instance |
| `history` | `[("OPEN", 25000.0, 25000.0), …]` | instance |
| `bank_name` | `"Nova Bank"` | **class** |
| `total_accounts` | `4` | **class** |
| `MIN_BALANCE`, `WITHDRAWAL_LIMIT` | `0.0`, `50000.0` | **class** |

### The four methods the assignment names

| Method | Returns | Raises |
|---|---|---|
| `deposit(amount)` | the new balance | `InvalidAmountError` |
| `withdraw(amount)` | the new balance | `InvalidAmountError`, `InsufficientFundsError` |
| `check_balance()` | the balance | - |
| `display_account_details()` | `None` - it prints | - |

Plus `transfer_to(other, amount)`, which is the only method that touches two
objects.

### Class methods

```python
@classmethod
def rename_bank(cls, new_name):
    cls.bank_name = new_name.strip()
```

One assignment, and all four accounts report the new name - because none of them
ever had a copy. `get_total_accounts()` is the bonus counter, and
`open_salary_account(holder, number)` is a **second constructor**: it returns
`cls(holder, number, 1000.0)`, so `main.py` never has to know that a salary
account opens with a credit.

---

## Why the counter says `BankAccount.total_accounts += 1`

```python
BankAccount.total_accounts += 1        # correct
self.total_accounts += 1               # counts nothing, raises nothing
```

The second form reads the class variable, adds 1, and assigns the result **to the
object** - creating an instance variable that hides the class variable. Every
account then reports `1` and `BankAccount.total_accounts` stays at `0`.

Section 6 of `main.py` demonstrates the same shadowing deliberately:

```
meera.bank_name = 'Rogue Bank'
meera.bank_name        -> Rogue Bank
BankAccount.bank_name  -> Nova Federal Bank
aarav.bank_name        -> Nova Federal Bank
del meera.bank_name    -> Nova Federal Bank   (the shared one is back)
```

Reading goes object → class. Writing stops at the object.

---

## The validation

Everything numeric goes through one static helper before it is used:

```python
@staticmethod
def _clean_amount(amount, allow_zero=False):
```

It is a `@staticmethod` because it needs neither the account nor the class - only
the value. `deposit()`, `withdraw()` and `__init__` all call it, so there is one
place where an amount is judged rather than three.

| Call | Result |
|---|---|
| `kabir.withdraw(9_999)` on 3,000 | `InsufficientFundsError: cannot withdraw 9,999.00 from a balance of 3,000.00 (short by 6,999.00)` |
| `kabir.withdraw(3_001)` on 3,000 | `InsufficientFundsError: … (short by 1.00)` |
| `kabir.withdraw(3_000)` on 3,000 | **allowed** - the balance goes to 0.00 |
| `kabir.withdraw(-500)` | `InvalidAmountError: must not be negative` |
| `kabir.deposit(0)` | `InvalidAmountError: must be greater than zero` |
| `kabir.deposit("2000")` | `InvalidAmountError: must be a number` |
| `kabir.deposit(True)` | `InvalidAmountError: must be a number` |
| `kabir.withdraw(60_000)` | `InvalidAmountError: above the per-transaction limit of 50,000.00` |

Three details worth pointing at:

- **The boundary is tested in both directions.** Withdrawing one rupee more than
  the balance is refused; withdrawing exactly the balance is allowed. An
  off-by-one in that comparison is the classic bug here, and it is invisible
  unless the exact-balance case is actually run.
- **`True` is refused.** `bool` subclasses `int`, so `float(True)` is `1.0` and a
  deposit of `True` would quietly credit one rupee. The bool test comes first, or
  it never runs - the same trap as exercise 24 and exercise 26.
- **A negative deposit is not a withdrawal.** Without the `< 0` check,
  `deposit(-5000)` would drain the account through the method that is supposed to
  fill it, bypassing the balance check entirely.

### Three exception classes

```
Exception
 └── BankError                  base - one except clause catches all
      ├── InsufficientFundsError    .requested  .available  .short_by
      └── InvalidAmountError        .amount     .reason
```

`InsufficientFundsError` carries the three numbers rather than one flattened
string, so a caller can decide what to do - offer an overdraft, suggest the
maximum, or just print the message. That is the lesson from exercise 23, applied
to a class.

---

## `transfer_to()` - why the order of two lines matters

```python
def transfer_to(self, other, amount):
    self.withdraw(amount)      # raises here if it cannot be afforded
    other.deposit(amount)
    return self.balance, other.balance
```

If those two lines were swapped, a transfer of 40,000 from a balance of 14,000
would credit the other account **first** and then raise - leaving 40,000 that
never existed sitting in Diya's account. Section 4 runs exactly that case and
prints the balances either side of it:

```
InsufficientFundsError: cannot withdraw 40,000.00 from a balance of 14,000.00 (short by 26,000.00)
balances before (14000.0, 14000.0)
balances after  (14000.0, 14000.0)
```

The failing step has to be the first step.

---

## Verified run

`python main.py` produces six sections in 149 lines:

```
1. Opening accounts               0 -> 4 accounts, one built by a class method
2. deposit / withdraw / balance   five calls, five new balances
3. The validation                 seven refusals, then the exact-balance case
4. transfer_to()                  4,000 moves; 40,000 does not move at all
5. display_account_details()      each account's own history list
6. Class variable / class method  one rename, four accounts, and the trap
```

---

## Concepts used

**Class variables** - `bank_name` and `total_accounts` as one shared copy each,
`MIN_BALANCE` and `WITHDRAWAL_LIMIT` as shared constants, and the `self.x += 1`
shadowing trap shown on purpose

**Class methods** - `@classmethod` with `cls`; `rename_bank()` assigning to
`cls.bank_name`; `get_total_accounts()`; and `open_salary_account()` as a second
constructor that calls `cls(...)`

**Static methods** - `_clean_amount()` needs neither the object nor the class

**Instance methods** - `deposit`, `withdraw`, `check_balance`, `transfer_to`, and
one method that exists to print

**Custom exceptions** (exercise 23) - a base class, two subclasses, extra
attributes on the exception instead of one long message, and `except BankError`
catching both

**Validation** - one helper called from three places; the bool-before-int order;
testing a boundary from both sides; refusing before mutating

**Encapsulation in practice** - `balance` is only ever changed by two methods, so
there are exactly two places where the rules about money live

---

## Learning / outcomes

1. **A class variable is the right answer when the data belongs to the bank, not
   to the customer.** Copying `bank_name` into 10,000 accounts would mean 10,000
   updates and one chance to miss some.

2. **Refuse before you change.** `withdraw()` checks the balance and *then*
   subtracts. Any method that mutates first and validates second has a state to
   roll back, and no rollback was written.

3. **An exception beats a `False` return when the caller might not look.**
   `if not acc.withdraw(9999):` is easy to forget; a raised
   `InsufficientFundsError` is not.

4. **The order of two correct lines can still be a bug.** `transfer_to()` is
   three lines and only one arrangement of them is safe.

5. **A second constructor is a class method.** `open_salary_account()` returns
   `cls(...)`, which keeps the "salary accounts start at 1,000" rule inside the
   class where the rest of the rules are.

### Challenges faced

- **The counter reported 1 for every account.** The first `__init__` said
  `self.total_accounts += 1`. Four accounts, four private counters, and
  `BankAccount.total_accounts` still 0.
- **`deposit(-5000)` emptied the account.** The first version only checked for
  non-numbers. A negative deposit walked straight past the withdrawal rules and
  did a withdrawal's job.
- **`withdraw(3000)` on a balance of 3,000 was refused.** The comparison was
  `amount >= self.balance`. Nobody could ever empty their own account, and the
  test that would have caught it - the exact-balance case - was not in the demo
  until it was written on purpose.
- **A failed transfer created money.** `transfer_to()` originally credited first.
  A transfer of 40,000 from 14,000 left the second account 40,000 richer before
  the exception arrived.
- **Floating point drift in the balance.** Repeated deposits of `1599.50` left
  balances like `9999.999999999998`. Every arithmetic result is now rounded to two
  decimals when it is stored, not only when it is printed.

---

## YouTube demonstration link

<your-youtube-video-link>

---

## Submission links

- **GitHub Repository:** `<your-public-github-repository-link>`
- **YouTube Explanation:** `<your-youtube-video-link>`
