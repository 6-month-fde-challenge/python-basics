"""
Question 7 - calculate_discount(price, discount=10)
====================================================
A DEFAULT ARGUMENT is a value written into the definition itself:

    def calculate_discount(price, discount=10):
                                  ^^^^^^^^^^^
    price    has no default -> it MUST be supplied on every call
    discount has a default  -> supplying it is OPTIONAL

    calculate_discount(1000)      -> discount is 10 (the default is used)
    calculate_discount(1000, 25)  -> discount is 25 (the default is replaced)

THE RULE ON ORDER: parameters WITH defaults must come AFTER those without.
Writing def f(discount=10, price) is a SyntaxError, because Python could
not tell which value a single argument was meant to fill.

WHY DEFAULTS ARE USEFUL: the common case stays short, while the unusual
case is still possible. Without a default, every caller would have to
type 10 even when 10 is what they always want.
"""


def calculate_discount(price, discount=10):
    """Return the price after applying a discount percentage (default 10%)."""
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price


def discount_details(price, discount=10):
    """Return the discount amount and final price as a tuple."""
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return discount_amount, final_price


print("=" * 55)
print("USING THE DEFAULT (no discount supplied)")
print("=" * 55)

print("   calculate_discount(1000)  =", calculate_discount(1000))
print("   calculate_discount(2500)  =", calculate_discount(2500))
print("   calculate_discount(499)   =", calculate_discount(499))
print("   In each case discount was 10, taken from the definition.")
print()

print("=" * 55)
print("OVERRIDING THE DEFAULT")
print("=" * 55)

print("   calculate_discount(1000, 25) =", calculate_discount(1000, 25))
print("   calculate_discount(1000, 50) =", calculate_discount(1000, 50))
print("   calculate_discount(1000, 0)  =", calculate_discount(1000, 0),
      " <- 0% off, so nothing changes")
print()

print("=" * 55)
print("THE SAME CALL WRITTEN THREE WAYS")
print("=" * 55)
print("   calculate_discount(1000, 25)            ->",
      calculate_discount(1000, 25), " (both positional)")
print("   calculate_discount(1000, discount=25)   ->",
      calculate_discount(1000, discount=25), " (one keyword)")
print("   calculate_discount(price=1000, discount=25) ->",
      calculate_discount(price=1000, discount=25), " (both keyword)")
print("   calculate_discount(discount=25, price=1000) ->",
      calculate_discount(discount=25, price=1000), " (keywords can be reordered)")
print()
print("   Positional arguments are matched BY POSITION, so their order is fixed.")
print("   Keyword arguments are matched BY NAME, so their order does not matter.")
print()

print("=" * 55)
print("A FULL DISCOUNT TABLE")
print("=" * 55)
print(f"   {'PRICE':<10}{'DISCOUNT':<12}{'YOU SAVE':<12}{'YOU PAY':<10}")
print("   " + "-" * 44)

for price, percent in [(1000, 10), (1000, 25), (2500, 15), (799, 5), (15000, 30)]:
    saved, final = discount_details(price, percent)
    print(f"   {price:<10}{str(percent) + '%':<12}{saved:<12.2f}{final:<10.2f}")

print()
print("=" * 55)
print("WHAT HAPPENS WITHOUT THE REQUIRED ARGUMENT")
print("=" * 55)

try:
    calculate_discount()
except TypeError as error:
    print("   calculate_discount() -> TypeError:", error)
    print("   `price` has no default, so it can never be left out.")
