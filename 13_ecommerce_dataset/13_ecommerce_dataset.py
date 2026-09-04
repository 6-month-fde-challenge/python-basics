"""
Exercise 13 - Create a Mini E-Commerce Dataset
==============================================
Concepts practised: list of dictionaries, indexing + keys together,
                    updating values, adding keys, append()

CONSTRAINT: no loops. Everything is reached by direct access.

THE COMBINATION - this is the most important structure in real programming
--------------------------------------------------------------------------
A LIST gives you MANY items, kept in ORDER, reached by POSITION.
A DICTIONARY describes ONE item, with NAMED details, reached by KEY.

Put them together and you get a TABLE - a list of dictionaries:

                 "name"     "price"   "brand"      <- KEYS (the columns)
products[0]  ->  "Laptop"    70000    "Dell"       <- one dictionary (a row)
products[1]  ->  "Phone"     40000    "Samsung"    <- one dictionary (a row)
products[2]  ->  "Tablet"    30000    "Apple"      <- one dictionary (a row)
     ^
     INDEX picks WHICH product      KEY picks WHICH detail

So the address of any single piece of data is:  products[index]["key"]
This is exactly the shape of every real product catalogue, API response
and database result you will ever work with.
"""

# ---------------------------------------------------------------------------
# Create the dataset - a LIST containing three DICTIONARIES
# ---------------------------------------------------------------------------

products = [
    {
        "name": "Laptop",
        "price": 70000,
        "brand": "Dell"
    },
    {
        "name": "Phone",
        "price": 40000,
        "brand": "Samsung"
    },
    {
        "name": "Tablet",
        "price": 30000,
        "brand": "Apple"
    }
]


# ---------------------------------------------------------------------------
# 1. Print all products
# ---------------------------------------------------------------------------
print("1. Complete dataset :")
print("  ", products)
print("   Number of products :", len(products))
print("   Type of 'products' :", type(products), "<- the outer container is a LIST")
print()


# ---------------------------------------------------------------------------
# 2. Print the first product -> ONE index gives the whole dictionary
# ---------------------------------------------------------------------------
print("2. First product    :", products[0])
print("   Type              :", type(products[0]), "<- each item is a DICTIONARY")
print()


# ---------------------------------------------------------------------------
# 3. Second product's price -> index 1 picks the product, "price" picks the detail
# ---------------------------------------------------------------------------
print("3. Second product's price :", products[1]["price"])
print("   Type                    :", type(products[1]["price"]), "<- now a plain value")


# ---------------------------------------------------------------------------
# 4. Third product's brand -> index 2, then the "brand" key
# ---------------------------------------------------------------------------
print("4. Third product's brand  :", products[2]["brand"])
print()


# ===========================================================================
# CHANGING THE DATASET
# ===========================================================================

print("=" * 64)
print("CHANGING THE DATASET")
print("=" * 64)

# --- 5. Change the first product's price -----------------------------------
print("5. Laptop price before :", products[0]["price"])
products[0]["price"] = 65000
print("   Laptop price after  :", products[0]["price"], "(price drop)")
print("   Row 0 is now        :", products[0])
print()

# --- 6. Add a "rating" to the SECOND product only --------------------------
#     Note: only products[1] gets this key. The other rows are unaffected.
print("6. Phone before adding rating :", products[1])
products[1]["rating"] = 4.5
print("   Phone after  adding rating :", products[1])
print("   Rating value               :", products[1]["rating"], type(products[1]["rating"]))
print("   Laptop still has keys      :", list(products[0].keys()),
      "<- unchanged, no rating")
print()

# --- 7. Add another product - append() adds ONE new dictionary (a new row) --
print("7. Products before append :", len(products))
products.append({
    "name": "Smartwatch",
    "price": 25000,
    "brand": "Boat"
})
print("   Products after  append :", len(products))
print("   New product [3]        :", products[3])
print()


# ---------------------------------------------------------------------------
# 8. Print the final dataset
# ---------------------------------------------------------------------------
print("=" * 64)
print("8. FINAL DATASET")
print("=" * 64)
print(products)
print()

# Displayed row by row - still no loops, just four direct lookups
print("Row 0 :", products[0])
print("Row 1 :", products[1])
print("Row 2 :", products[2])
print("Row 3 :", products[3])
print()

# Displayed as a neat table using index + key together
print("A readable table (index picks the row, key picks the column):")
print(f"{'NAME':<12}{'PRICE':<10}{'BRAND':<10}")
print("-" * 32)
print(f"{products[0]['name']:<12}{products[0]['price']:<10}{products[0]['brand']:<10}")
print(f"{products[1]['name']:<12}{products[1]['price']:<10}{products[1]['brand']:<10}")
print(f"{products[2]['name']:<12}{products[2]['price']:<10}{products[2]['brand']:<10}")
print(f"{products[3]['name']:<12}{products[3]['price']:<10}{products[3]['brand']:<10}")


# ===========================================================================
# PUTTING INDEXING, KEYS AND VALUES TOGETHER
# ===========================================================================

print()
print("=" * 64)
print("HOW THE PIECES COMBINE")
print("=" * 64)

print("products            ->", type(products), "the whole catalogue")
print("products[1]         ->", type(products[1]), "one product")
print("products[1]['name'] ->", type(products[1]["name"]), "one detail of one product")
print()
print("Reading it left to right:")
print("   products[1]          gives", products[1])
print("   ...then ['name']     gives", products[1]["name"])
print()

# Keys and values of a single row
print("Keys of product 1 (the detail NAMES) :", list(products[1].keys()))
print("Values of product 1 (the DATA)       :", list(products[1].values()))
print("Items of product 1 (paired together) :", list(products[1].items()))
print()

# Negative indexing works exactly the same way
print("Negative indexing:")
print("   Last product          :", products[-1])
print("   Last product's brand  :", products[-1]["brand"])
print()

# Slicing the list returns a smaller list of dictionaries
print("Slicing the list:")
print("   First two products    :", products[:2])
print("   Type of the slice     :", type(products[:2]), "<- still a list of dicts")
print()

# Simple calculations using direct access
total = products[0]["price"] + products[1]["price"] + products[2]["price"] + products[3]["price"]
print("Cart total (all four prices added) : Rs.", total)
print("Average price                      : Rs.", round(total / len(products), 2))
print("Most expensive of the four         : Rs.", max(products[0]["price"], products[1]["price"],
                                                      products[2]["price"], products[3]["price"]))
