# Exercise 13 - Mini E-Commerce Dataset

## What this exercise is about

The payoff for everything from Exercise 05 onward: combining a list and a dictionary into
the single most common data shape in real programming - a **list of dictionaries**.
Three products are stored, read, modified and extended, all without loops.

## Why the combination works

- A **list** holds many items in order, reached by **position** - but cannot say what
  each item *is*.
- A **dictionary** describes one thing with named details - but holds only one product.

Together they form a table:

```
                 "name"     "price"   "brand"     <- KEYS = the columns
products[0]  ->  "Laptop"    70000    "Dell"      <- one dict = one row
products[1]  ->  "Phone"     40000    "Samsung"
products[2]  ->  "Tablet"    30000    "Apple"
```

Any value has the address **`products[index]["key"]`** - index for *which* product,
key for *which* detail.

## The three layers, proved with `type()`

| Expression | Type | Meaning |
|---|---|---|
| `products` | `list` | the whole catalogue |
| `products[1]` | `dict` | one product |
| `products[1]["name"]` | `str` | one detail of one product |

## Two ways to grow it, and the difference matters

- `products[1]["rating"] = 4.5` adds a **column to one row** - still 3 products.
- `products.append({...})` adds a **whole new row** - now 4 products.

Note that after the first, product 1 has four keys while product 0 still has three.
**Rows in a list of dictionaries need not share the same keys** - real catalogues are
exactly like this.

## Why this matters in practice

This structure is what every JSON API returns, what every database query gives back,
and what pandas turns into a DataFrame. It is the default shape of real data.

## Run it

```bash
python 13_ecommerce_dataset.py
```

or from the repo root:

```bash
python .\01_python_basics\13_ecommerce_dataset\13_ecommerce_dataset.py
```
