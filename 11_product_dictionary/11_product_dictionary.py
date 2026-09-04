"""
Exercise 11 - Build a Product Dictionary
========================================
Concepts practised: dictionary creation, key access, updating values,
                    adding keys, pop(), keys(), values(), items()

A dictionary is the natural way to describe ONE REAL-WORLD THING,
because every piece of information gets a NAME instead of a number.
"""

# ---------------------------------------------------------------------------
# Create the laptop dictionary
# ---------------------------------------------------------------------------

laptop = {
    "brand": "Dell",
    "model": "XPS 15",
    "price": 120000,
    "ram": "16GB",
    "storage": "512GB SSD",
    "available": True
}


# ---------------------------------------------------------------------------
# 1. Display the complete product
# ---------------------------------------------------------------------------
print("1. Complete product :")
print("  ", laptop)
print("   Number of details :", len(laptop))
print()


# ---------------------------------------------------------------------------
# 2, 3, 4. Access individual values by their key
# ---------------------------------------------------------------------------
print("2. Brand            :", laptop["brand"])
print("3. Model            :", laptop["model"])
print("4. Price            :", laptop["price"], "->", type(laptop["price"]))
print()


# ===========================================================================
# UPDATING AND ADDING
# ===========================================================================

print("=" * 62)
print("UPDATING AND ADDING")
print("=" * 62)
print("The syntax is the SAME for both:  laptop[key] = value")
print("Key already there -> it is UPDATED.  Key not there -> it is CREATED.")
print()

# --- 5. Change the price (key exists -> update) ----------------------------
print("5. Price before     :", laptop["price"])
laptop["price"] = 110000
print("   Price after      :", laptop["price"], "(discounted)")

# --- 6. Add processor information (key is new -> create) -------------------
laptop["processor"] = "Intel Core i7"
print("6. Processor added  :", laptop["processor"])

# --- 7. Add GPU information (key is new -> create) -------------------------
laptop["gpu"] = "NVIDIA RTX 4050"
print("7. GPU added        :", laptop["gpu"])

# --- 8. Change RAM to 32GB (key exists -> update) --------------------------
print("8. RAM before       :", laptop["ram"])
laptop["ram"] = "32GB"
print("   RAM after        :", laptop["ram"])
print()
print("   Product so far   :", laptop)
print()


# ===========================================================================
# REMOVING A KEY
# ===========================================================================

print("=" * 62)
print("REMOVING A KEY")
print("=" * 62)

# --- 9. Remove "available" using pop()
#        pop() deletes the key AND RETURNS its value, so nothing is wasted.
print("9. Keys before pop() :", list(laptop.keys()))
removed_value = laptop.pop("available")
print("   pop('available') returned :", removed_value)
print("   Keys after  pop() :", list(laptop.keys()))
print("   'available' in laptop ->", "available" in laptop)
print()
print("   Other ways to delete:")
print("     del laptop['gpu']    -> deletes, but returns nothing")
print("     laptop.pop('x')      -> KeyError if the key is missing")
print("     laptop.pop('x', None)-> safe, gives None instead of crashing")
print("     Example:", laptop.pop("warranty", "key not found"))
print()


# ===========================================================================
# THE THREE VIEW METHODS
# ===========================================================================

print("=" * 62)
print("keys() / values() / items()")
print("=" * 62)

# --- 10. All keys - the NAMES of the details --------------------------------
print("10. All keys   :", laptop.keys())
print("    As a list  :", list(laptop.keys()))

# --- 11. All values - the ACTUAL data ---------------------------------------
print("11. All values :", laptop.values())
print("    As a list  :", list(laptop.values()))

# --- 12. All items - key and value TOGETHER as (key, value) tuples ----------
print("12. All items  :", laptop.items())
print("    As a list  :", list(laptop.items()))
print("    Each item is a tuple, e.g.", list(laptop.items())[0],
      "->", type(list(laptop.items())[0]))
print()


# ===========================================================================
# 13. A SECOND PRODUCT - A MOBILE PHONE
# ===========================================================================

print("=" * 62)
print("SECOND PRODUCT : MOBILE PHONE")
print("=" * 62)

mobile = {
    "brand": "Samsung",
    "model": "Galaxy S24 Ultra",
    "price": 129999,
    "ram": "12GB",
    "storage": "256GB",
    "camera": "200MP",
    "battery": "5000mAh",
    "available": True
}

print("Complete product :")
print("  ", mobile)
print()
print("Brand            :", mobile["brand"])
print("Model            :", mobile["model"])
print("Price            :", mobile["price"])
print("Camera           :", mobile["camera"])
print("Battery          :", mobile["battery"])
print("In stock?        :", mobile["available"])
print()
print("All keys         :", list(mobile.keys()))
print("All values       :", list(mobile.values()))


# ===========================================================================
# COMPARING THE TWO PRODUCTS (no loops - direct key access)
# ===========================================================================

print()
print("=" * 62)
print("COMPARING THE TWO PRODUCTS")
print("=" * 62)
print("Laptop :", laptop["brand"], laptop["model"], "- Rs.", laptop["price"])
print("Mobile :", mobile["brand"], mobile["model"], "- Rs.", mobile["price"])
print("Price difference :  Rs.", abs(laptop["price"] - mobile["price"]))
print("Cheaper product  : ", laptop["model"] if laptop["price"] < mobile["price"] else mobile["model"])

# Both products stored together in one list of dictionaries
products = [laptop, mobile]
print()
print("Both products in one list :")
print("   Product 1 :", products[0]["brand"], products[0]["model"])
print("   Product 2 :", products[1]["brand"], products[1]["model"])
print("   Total products in catalogue :", len(products))
