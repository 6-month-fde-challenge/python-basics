# Exercise 06 - Shopping Cart with List Methods

## What this exercise is about

A cart of five products put through eleven list operations in sequence - adding,
inserting, removing, searching, copying, reversing and sorting. The cart is printed
after every single step, so the effect of each method is visible as it happens.

The rule underneath all of it: **list methods change the list in place and return
`None`.** So it is `cart.sort()`, never `cart = cart.sort()` - the second replaces
your cart with `None`.

## The methods, grouped by what they do

**Adding** - three methods, three behaviours
| Method | Adds | Where |
|---|---|---|
| `append(x)` | exactly one item | at the end |
| `extend([a, b])` | each item separately | at the end |
| `insert(i, x)` | one item | at position `i`, shifting the rest right |

**Removing** - the difference is *what* versus *where*
| Method | You specify | Returns |
|---|---|---|
| `remove("Mouse")` | the **value** | nothing |
| `pop()` | the **position** (default last) | **the removed item** |
| `clear()` | nothing | empties the list |

**Reordering** - `reverse()` flips the current order; `sort()` arranges A-Z. They are
not the same thing.

**Copying** - `cart.copy()` makes an independent duplicate. `cart_copy = cart` does
**not** - it creates a second name for the same list, and editing either changes both.
The program proves the difference two ways.

## Run it

```bash
python 06_shopping_cart.py
```

or from the repo root:

```bash
python .\01_python_basics\06_shopping_cart\06_shopping_cart.py
```

## Worth knowing

`index("Monitor")` returns 3, the same as its original position - but only by
coincidence. `insert()` pushed it right, then `remove()` pulled it back.
