# Exercise 29 - E-Commerce Product System

Built around one three-line method that needs no object at all:

```python
Product.is_valid_price(1299)    # True    <- no product has been created
Product.is_valid_price(0)       # False
Product.is_valid_price(True)    # False
```

---

## Project objective

Exercise 26 introduced three kinds of method and 27 and 28 used two of them. This
exercise is about the third.

`is_valid_price(price)` reads no attribute of any product and no attribute of the
class. It takes a number and answers a question about that number. That is the
whole test for `@staticmethod`, and it has a practical consequence: `__init__`
can call it **before** the object exists, which is exactly when a price needs
checking.

```python
def __init__(self, product_id, name, price, category, stock=0):
    if not self.is_valid_price(price):
        raise ValueError(...)
    ...
    self.price = float(price)      # only reached if the price is good
```

Five products are built, two more are refused, and neither of the refused two is
counted - because the exception is raised before `Product.total_products += 1`.

---

## Project structure

```
29_ecommerce_product_system/
├── README.md
├── product.py             THE CLASS - 2 static, 9 instance, 2 class methods
├── main.py                5 products, sales, restocks, refusals
├── sample_output.txt      captured from a real run
└── static_methods.png
```

---

## How to execute the program

```bash
python main.py             # the application
python product.py          # the class's own self-test
```

or from the repo root:

```bash
python .\01_python_basics\29_ecommerce_product_system\main.py
```

No installation and no external packages. **Requires Python 3.7+** -
dictionaries keep their insertion order from 3.7, which the output relies on.
Verified on Python 3.12.10.

---

## The class

### Attributes - the five the assignment asks for, plus a tally

| Attribute | Example | Kind |
|---|---|---|
| `product_id` | `"P101"` | instance |
| `name` | `"Laptop"` | instance |
| `price` | `58990.0` | instance |
| `category` | `"Electronics"` | instance |
| `stock` | `12` | instance |
| `units_sold` | `2` | instance |
| `total_products`, `store_name` | `5`, `"Nova Cart"` | **class** |
| `CURRENCY`, `GST_RATE`, `LOW_STOCK`, `CATEGORIES` | `"INR"`, `0.18`, `5`, a tuple | **class** |

### The three methods the assignment names

| Method | Returns |
|---|---|
| `display_product()` | `None` - it prints |
| `update_stock(change)` | the new stock level |
| `calculate_total_price(quantity, include_tax=True)` | what the order costs |

Plus `sell()`, `restock()`, `apply_discount()`, `in_stock()`, `is_low_stock()` and
`stock_value()`.

### The static methods

```python
@staticmethod
def is_valid_price(price):      # the one the assignment names

@staticmethod
def is_valid_quantity(quantity)
```

Both are callable three ways, and all three run the same code:

```python
Product.is_valid_price(1299)     # on the class          <- the useful one
laptop.is_valid_price(1299)      # through an object     <- works, but odd
Product.is_valid_price           # the plain function
```

---

## Which kind of method, and why

| Method | Kind | Because it needs |
|---|---|---|
| `is_valid_price(price)` | `@staticmethod` | only the argument |
| `is_valid_quantity(q)` | `@staticmethod` | only the argument |
| `calculate_total_price(q)` | instance | **this** product's price |
| `update_stock(change)` | instance | **this** product's stock |
| `get_total_products()` | `@classmethod` | the class's counter |
| `set_store_name(name)` | `@classmethod` | the class's shared name |

That single question - *what does this method actually need?* - decides every
one of them. It is a better rule than "make it static if it does not use `self`",
because `calculate_total_price()` could be written to take a price as an argument
and would then be static, and worse.

### Why it is not a plain function outside the class

`is_valid_price()` **could** be a module-level function. Keeping it in `Product`
says what it is a rule *about*. It travels with the class, it shows up in
`help(Product)`, and a subclass could tighten it. Exercise 24 made the same
argument about a package: the boundary is the point.

---

## `calculate_total_price(quantity, include_tax=True)`

```
qty         subtotal      with GST
----------------------------------
1          58,990.00     69,608.20
2         117,980.00    139,216.40
5         294,950.00    348,041.00
```

`include_tax` has a default, so the common call is the short one and the
exception has to be spelled out - the default-argument rule from exercise 19.
`GST_RATE` is a class variable, so changing the rate is one line and reaches every
product.

---

## Stock, and the order the checks run in

`update_stock(change)` takes a **signed** change, so one method covers both
directions and there is one place where "stock must never go negative" is
enforced:

```python
new_level = self.stock + change
if new_level < 0:
    raise ValueError(f"cannot remove {-change} of {self.name}: only {self.stock} in stock")
self.stock = new_level
```

`sell()` then reads:

```python
total = self.calculate_total_price(quantity)   # raises on a bad quantity
self.update_stock(-quantity)                   # raises if there are not enough
self.units_sold += quantity
return total
```

Both things that can fail happen before either number moves. A refused sale leaves
stock, `units_sold` and the price untouched - the same "refuse before you change"
rule as exercise 27's `withdraw()`.

---

## What the shop refuses

| Call | Result |
|---|---|
| `notebook.sell(5)` with 2 in stock | `ValueError: cannot remove 5 of Notebook: only 2 in stock` |
| `notebook.sell(2)` with 2 in stock | **allowed** - stock goes to 0 |
| `notebook.sell(-2)` | `ValueError: quantity must be a whole number above zero` |
| `notebook.sell(1.5)` | `ValueError: … got 1.5` |
| `notebook.update_stock(0)` | `ValueError: stock change of 0 does nothing` |
| `laptop.apply_discount(100)` | `ValueError: discount must be between 0 and 100` |
| `Product("P999", "Freebie", 0, "Home", 1)` | `ValueError: price must be greater than zero, got 0` |
| `Product("P998", "Anvil", 500, "Hardware", 1)` | `ValueError: unknown category 'Hardware' (known: …)` |

Three details:

- **`True` is not a price.** `bool` subclasses `int`, so `True > 0` is `True` and
  a price of `True` would be stored as `1.00`. `is_valid_price()` checks `bool`
  before it checks anything else - the same trap as exercises 24, 26 and 27.
- **`2.5` is not a quantity.** `is_valid_quantity()` insists on `int`, not any
  number, because half a notebook does not leave the shelf.
- **A 100% discount is refused**, not because the maths fails, but because it
  would leave `price = 0.0`, which `is_valid_price()` would reject on the next
  product. `apply_discount()` runs the new price back through
  `is_valid_price()` before storing it, so one rule governs prices however they
  arrive.

---

## Verified run

`python main.py` produces six sections in 162 lines:

```
1. A static method needs no object   7 prices judged with 0 products in existence
2. Five products                     the catalogue
3. calculate_total_price()           1, 2 and 5 laptops, with and without GST
4. Buying                            5 sales, 152,100.82, stock down by exactly what sold
5. What the shop refuses             8 refusals, then the exact-stock sale
6. Restock, discount, display        a 15% cut, three product blocks, a best seller
```

---

## Concepts used

**Static methods** - `@staticmethod`, called on the class before any object
exists, used by `__init__` to validate its own arguments, and reused by
`apply_discount()` so one rule governs every price

**Choosing the method kind** - instance / class / static decided by what the
method needs, with the table above as the working rule

**Class variables** - `total_products`, `store_name`, `GST_RATE`, `LOW_STOCK`, and
`CATEGORIES` as a tuple so the list of valid categories cannot be edited by
accident

**Class methods** - `get_total_products()` and `set_store_name()`

**Instance methods** - a signed `update_stock()` with one guard; `sell()` and
`restock()` as thin wrappers over it; `display_product()` as the only method that
prints

**Validation** - refuse before mutating, the bool-before-int order, `int` rather
than "any number" for a count, boundaries tested from both sides, and error
messages that name the product and both numbers

**Carried forward** - default arguments (exercise 19), the accumulator and
champion patterns instead of `sum()` and `max()` (exercise 18), `try`/`except
ValueError` around every refusal (exercise 23), and the module self-test
(exercise 24)

---

## Learning / outcomes

1. **`@staticmethod` is the answer to "this needs nothing from the object".**
   Not "it happens not to use `self`" - genuinely needs nothing, which is why it
   can run inside `__init__` before there is an object to need.

2. **Validation belongs where the value enters, and only there.** Price is
   checked in `__init__` and in `apply_discount()`, both through the same static
   method. There is one rule about prices, written once.

3. **A signed `update_stock()` beats `add_stock()` and `remove_stock()`.** One
   method, one guard, one place where stock can go wrong.

4. **Order the failures first.** `sell()` prices the order and checks the stock
   before changing either. A method that mutates and then validates needs a
   rollback, and nobody writes the rollback.

5. **A count is an `int`, not a number.** Accepting `2.5` because it is numeric
   produces a stock level of `1.5` and a bug that appears three screens later.

### Challenges faced

- **`is_valid_price(True)` returned `True`.** `True > 0` is perfectly valid
  Python. A product priced at `True` was built and displayed as `INR 1.00`.
- **`sell(1.5)` left 2.5 notebooks on the shelf.** The first `update_stock()`
  accepted any number. Stock counts are now `int` or nothing.
- **A failed sale still charged the customer.** An early `sell()` computed the
  total *after* calling `update_stock()`, so a sale that was refused for stock had
  already returned a price on the previous line. Both checks moved above the
  first assignment.
- **`apply_discount(100)` set the price to 0.00.** The discount maths was right
  and the result was a product the constructor would have refused. The new price
  now goes back through `is_valid_price()`.
- **`float` drift in the shelf value.** Repeated `price * stock` on discounted
  prices produced figures like `25287.499999999996`. Every stored money value is
  rounded to two decimals at the point it is stored.

---

## YouTube demonstration link

<your-youtube-video-link>

---

## Submission links

- **GitHub Repository:** `<your-public-github-repository-link>`
- **YouTube Explanation:** `<your-youtube-video-link>`
