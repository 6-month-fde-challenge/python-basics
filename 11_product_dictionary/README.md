# Exercise 11 - Product Dictionary

## What this exercise is about

Modelling a real-world object - a laptop - as a dictionary of named attributes, then
putting it through twelve operations: reading fields, updating them, adding new ones,
deleting one, and inspecting the dictionary three different ways. A second product (a
mobile phone) is then built to show that two records of the same "kind" need not share
the same fields.

A dictionary suits a product because a laptop is not a *sequence* of things, it is one
thing with named parts. `laptop["price"]` documents itself; `laptop[2]` does not.

## The rule behind updating and adding

`laptop[key] = value` - key **exists** means update, key **new** means create. Price
and RAM were updates, processor and GPU were additions, and nothing in the code
distinguishes them. The flip side: a **typo silently creates a junk key** rather than
raising an error.

## Deleting

| | Deletes | Returns the value | Missing key |
|---|---|---|---|
| `pop("available")` | yes | **yes** | `KeyError` |
| `pop("x", default)` | yes | yes | your default |
| `del laptop["gpu"]` | yes | **no** | `KeyError` |

## The three views, and what each is for

- `keys()` - the **names** of the details: "what do I know about this product?"
- `values()` - the **data**: "what are the answers?"
- `items()` - **both paired**, as `(key, value)` **tuples**

The program proves that last claim with `type()`. That pairing is why `items()` is the
one used with loops later. All three return **view objects**, not lists - wrap in
`list()` for a real list.

## The closing idea

`products = [laptop, mobile]` - a **list of dictionaries**, which is how essentially
every real catalogue, API response and database result is shaped. Exercise 13 builds on
this directly.

## Run it

```bash
python 11_product_dictionary.py
```

or from the repo root:

```bash
python .\01_python_basics\11_product_dictionary\11_product_dictionary.py
```
