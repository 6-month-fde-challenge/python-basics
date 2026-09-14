"""
product.py - the Product class
===============================
One product in a small shop: an id, a name, a price, a category and however many
are on the shelf.

    from product import Product

    Product.is_valid_price(1299)     # True    <- no product needed
    Product.is_valid_price(0)        # False

    laptop = Product("P101", "Laptop", 58_990, "Electronics", 12)
    laptop.calculate_total_price(2)  # 139,216.40  (2 x 58,990 + 18% GST)
    laptop.sell(2)                   # 10 left

The exercise is built around `is_valid_price`, which is a **static** method: it
answers a question about a number, and a number is all it needs.
"""


class Product:
    """One line in a catalogue."""

    # ---------------------------------------------------------------- class
    total_products = 0
    store_name = "Nova Cart"
    CURRENCY = "INR"
    GST_RATE = 0.18
    LOW_STOCK = 5
    CATEGORIES = ("Electronics", "Home", "Grocery", "Fashion", "Stationery")

    # ------------------------------------------------------------ construct

    def __init__(self, product_id, name, price, category, stock=0):
        if not self.is_valid_price(price):
            raise ValueError(f"price must be greater than zero, got {price!r}")
        if not self.is_valid_quantity(stock):
            raise ValueError(f"stock must be a whole number of 0 or more, got {stock!r}")
        if category not in self.CATEGORIES:
            raise ValueError(
                f"unknown category {category!r} (known: {', '.join(self.CATEGORIES)})"
            )

        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.category = category
        self.stock = int(stock)
        self.units_sold = 0

        Product.total_products += 1

    # --------------------------------------------------------------- static
    # Neither of these touches self or cls. They judge a value, and the value
    # is passed in - so they are static methods, callable without a product.

    @staticmethod
    def is_valid_price(price):
        """True when price is a number greater than zero, False otherwise.

        bool is checked first: True is an int in Python, and a price of True
        would otherwise be accepted and stored as 1.0.
        """
        if isinstance(price, bool):
            return False
        if not isinstance(price, (int, float)):
            return False
        return price > 0

    @staticmethod
    def is_valid_quantity(quantity):
        """True when quantity is a whole number of zero or more."""
        if isinstance(quantity, bool):
            return False
        if not isinstance(quantity, int):
            return False
        return quantity >= 0

    # ------------------------------------------------------------- instance

    def calculate_total_price(self, quantity, include_tax=True):
        """What `quantity` of this product costs, with GST unless asked not to."""
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError(f"quantity must be a whole number above zero, got {quantity!r}")

        subtotal = self.price * quantity
        if include_tax:
            subtotal *= (1 + self.GST_RATE)
        return round(subtotal, 2)

    def update_stock(self, change):
        """Move the stock level by `change`, which may be negative.

        Refuses to go below zero, so a sale of more than is on the shelf fails
        instead of leaving a negative stock count.
        """
        if isinstance(change, bool) or not isinstance(change, int):
            raise ValueError(f"stock change must be a whole number, got {change!r}")
        if change == 0:
            raise ValueError("stock change of 0 does nothing")

        new_level = self.stock + change
        if new_level < 0:
            raise ValueError(
                f"cannot remove {-change} of {self.name}: only {self.stock} in stock"
            )

        self.stock = new_level
        return self.stock

    def sell(self, quantity):
        """Sell `quantity` units. Returns what the customer pays."""
        if not self.is_valid_quantity(quantity) or quantity == 0:
            raise ValueError(f"quantity must be a whole number above zero, got {quantity!r}")

        total = self.calculate_total_price(quantity)   # raises before any change
        self.update_stock(-quantity)                   # raises if there are not enough
        self.units_sold += quantity
        return total

    def restock(self, quantity):
        """Put `quantity` more on the shelf."""
        if not self.is_valid_quantity(quantity) or quantity == 0:
            raise ValueError(f"quantity must be a whole number above zero, got {quantity!r}")
        return self.update_stock(quantity)

    def in_stock(self):
        return self.stock > 0

    def is_low_stock(self):
        return 0 < self.stock <= self.LOW_STOCK

    def stock_value(self):
        """What the shelf is worth, before tax."""
        return round(self.price * self.stock, 2)

    def apply_discount(self, percent):
        """Cut the price by a percentage. Refuses anything that is not a price."""
        if isinstance(percent, bool) or not isinstance(percent, (int, float)):
            raise ValueError(f"discount must be a number, got {percent!r}")
        if not 0 < percent < 100:
            raise ValueError(f"discount must be between 0 and 100, got {percent}")

        new_price = round(self.price * (1 - percent / 100), 2)
        if not self.is_valid_price(new_price):
            raise ValueError(f"a discount of {percent}% would make the price {new_price}")

        self.price = new_price
        return self.price

    def display_product(self):
        """Print the product as a block. The only method here that prints."""
        if self.stock == 0:
            status = "OUT OF STOCK"
        elif self.is_low_stock():
            status = f"LOW ({self.stock} left)"
        else:
            status = f"{self.stock} in stock"

        print(f"    {self.name}  ({self.product_id})")
        print(f"      category   : {self.category}")
        print(f"      price      : {self.CURRENCY} {self.price:>10,.2f}")
        print(f"      with GST   : {self.CURRENCY} "
              f"{self.calculate_total_price(1):>10,.2f}")
        print(f"      stock      : {status}")
        print(f"      sold       : {self.units_sold}")
        print(f"      shelf value: {self.CURRENCY} {self.stock_value():>10,.2f}")

    # ---------------------------------------------------------------- class

    @classmethod
    def get_total_products(cls):
        return cls.total_products

    @classmethod
    def set_store_name(cls, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("store name must be a non-empty string")
        cls.store_name = name.strip()
        return cls.store_name

    # -------------------------------------------------------------- dunders

    def __repr__(self):
        return (f"Product({self.product_id!r}, {self.name!r}, {self.price!r}, "
                f"{self.category!r}, {self.stock!r})")


if __name__ == "__main__":
    print("Product.is_valid_price(1299)   ->", Product.is_valid_price(1299))
    print("Product.is_valid_price(0)      ->", Product.is_valid_price(0))
    print()
    demo = Product("P000", "Test Item", 100, "Home", 10)
    print("sell(3) costs", demo.sell(3))
    demo.display_product()
