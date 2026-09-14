"""
vehicle.py - Vehicle, and its two children
===========================================
One parent, two children, and neither child knows the other exists.

    Vehicle
       |
       +---- Car     (seats)
       |
       +---- Bike    (engine_cc)

    from vehicle import Vehicle, Car, Bike

    Vehicle.is_valid_duration(3)     # True    <- no vehicle needed
    Vehicle.is_valid_duration(0)     # False

    swift = Car("KA01AB1234", "Maruti", "Swift", 1_800, seats=5)
    swift.calculate_rent(4)          # base rent, plus what a car adds

`calculate_rent(days)` is defined in all three classes. Both children start with
`super().calculate_rent(days)` and add to it, so the weekly discount is written
once and applies to everything on the forecourt.
"""


class Vehicle:
    """Anything the agency rents out."""

    # ---------------------------------------------------------------- class
    total_vehicles = 0                # every vehicle, of every kind
    agency = "Nova Rentals"
    CURRENCY = "INR"
    MIN_DAYS = 1
    MAX_DAYS = 90
    WEEKLY_DAYS = 7
    WEEKLY_DISCOUNT = 10              # percent, for a hire of a week or more

    # ------------------------------------------------------------ construct

    def __init__(self, vehicle_number, brand, model, rent_per_day):
        if not isinstance(vehicle_number, str) or not vehicle_number.strip():
            raise ValueError("vehicle number must be a non-empty string")
        if isinstance(rent_per_day, bool) or not isinstance(rent_per_day, (int, float)):
            raise ValueError(f"rent per day must be a number, got {rent_per_day!r}")
        if rent_per_day <= 0:
            raise ValueError(f"rent per day must be above zero, got {rent_per_day}")

        self.vehicle_number = vehicle_number.strip().upper()
        self.brand = brand
        self.model = model
        self.rent_per_day = float(rent_per_day)
        self.days_hired = 0               # running total, this vehicle only
        self.on_hire = False

        Vehicle.total_vehicles += 1       # the class, so both children count here

    # --------------------------------------------------------------- static

    @staticmethod
    def is_valid_duration(days):
        """True when `days` is a whole number of days the agency will accept.

        Takes neither the vehicle nor the class - only the number - so it is a
        static method, and it can be called before any vehicle exists.
        """
        if isinstance(days, bool):
            return False                       # True is an int; a hire of True is not
        if not isinstance(days, int):
            return False                       # half a day is not a rental day
        return Vehicle.MIN_DAYS <= days <= Vehicle.MAX_DAYS

    # ------------------------------------------------------------- instance

    def vehicle_type(self):
        """Overridden by both children."""
        return "Vehicle"

    def extras_for(self, days):
        """What this kind of vehicle adds on top of the base rent. 0 here."""
        return 0.0

    def calculate_rent(self, days):
        """Base rent for `days`, with the weekly discount if it applies.

        Both children call this first and add their own charges to the result,
        so the discount rule lives in exactly one place.
        """
        if not self.is_valid_duration(days):
            raise ValueError(
                f"rental duration must be a whole number of days between "
                f"{self.MIN_DAYS} and {self.MAX_DAYS}, got {days!r}"
            )

        rent = self.rent_per_day * days
        if days >= self.WEEKLY_DAYS:
            rent *= (1 - self.WEEKLY_DISCOUNT / 100)
        return round(rent, 2)

    def rent_out(self, days):
        """Hire the vehicle out for `days`. Returns what is owed."""
        if self.on_hire:
            raise ValueError(f"{self.vehicle_number} is already out on hire")

        total = self.calculate_rent(days)   # raises on a bad duration, first
        self.on_hire = True
        self.days_hired += days
        return total

    def return_vehicle(self):
        """Bring it back. Returns True if it was actually out."""
        was_out, self.on_hire = self.on_hire, False
        return was_out

    def display_details(self):
        """Print the vehicle. Both children extend this rather than replacing it."""
        print(f"    {self.brand} {self.model}  ({self.vehicle_number})")
        print(f"      type       : {self.vehicle_type()}")
        print(f"      agency     : {self.agency}")
        print(f"      per day    : {self.CURRENCY} {self.rent_per_day:>9,.2f}")
        print(f"      3 days     : {self.CURRENCY} {self.calculate_rent(3):>9,.2f}")
        print(f"      7 days     : {self.CURRENCY} {self.calculate_rent(7):>9,.2f}"
              f"   (weekly rate)")
        print(f"      status     : {'out on hire' if self.on_hire else 'available'}")
        print(f"      days hired : {self.days_hired}")

    # ---------------------------------------------------------------- class

    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles

    @classmethod
    def set_agency(cls, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("agency name must be a non-empty string")
        Vehicle.agency = name.strip()
        return Vehicle.agency

    # -------------------------------------------------------------- dunders

    def __repr__(self):
        return (f"{type(self).__name__}({self.vehicle_number!r}, {self.brand!r}, "
                f"{self.model!r}, {self.rent_per_day!r})")


class Car(Vehicle):
    """A car. Has seats, and a per-day insurance charge."""

    INSURANCE_PER_DAY = 250.0
    LARGE_CAR_SEATS = 7

    def __init__(self, vehicle_number, brand, model, rent_per_day, seats):
        if isinstance(seats, bool) or not isinstance(seats, int):
            raise ValueError(f"seats must be a whole number, got {seats!r}")
        if not 2 <= seats <= 9:
            raise ValueError(f"seats must be between 2 and 9, got {seats}")

        super().__init__(vehicle_number, brand, model, rent_per_day)
        self.seats = seats

    def vehicle_type(self):
        return "Large Car" if self.seats >= self.LARGE_CAR_SEATS else "Car"

    def extras_for(self, days):
        """Insurance is charged per day, so it scales with the hire."""
        return round(self.INSURANCE_PER_DAY * days, 2)

    def calculate_rent(self, days):
        """The base rent, plus insurance for every day."""
        return round(super().calculate_rent(days) + self.extras_for(days), 2)

    def display_details(self):
        super().display_details()
        print(f"      seats      : {self.seats}")
        print(f"      insurance  : {self.CURRENCY} {self.INSURANCE_PER_DAY:>9,.2f}"
              f" / day")


class Bike(Vehicle):
    """A motorcycle. Has an engine size, and a one-off helmet charge."""

    HELMET_CHARGE = 100.0
    HIGH_CC = 350

    def __init__(self, vehicle_number, brand, model, rent_per_day, engine_cc):
        if isinstance(engine_cc, bool) or not isinstance(engine_cc, int):
            raise ValueError(f"engine capacity must be a whole number, got {engine_cc!r}")
        if not 50 <= engine_cc <= 2000:
            raise ValueError(f"engine capacity must be between 50cc and 2000cc, got {engine_cc}")

        super().__init__(vehicle_number, brand, model, rent_per_day)
        self.engine_cc = engine_cc

    def vehicle_type(self):
        return "High-capacity Bike" if self.engine_cc >= self.HIGH_CC else "Bike"

    def extras_for(self, days):
        """The helmet is charged once, however long the hire is."""
        return self.HELMET_CHARGE

    def calculate_rent(self, days):
        """The base rent, plus one helmet charge."""
        return round(super().calculate_rent(days) + self.extras_for(days), 2)

    def display_details(self):
        super().display_details()
        print(f"      engine     : {self.engine_cc} cc")
        print(f"      helmet     : {self.CURRENCY} {self.HELMET_CHARGE:>9,.2f}"
              f" once")


if __name__ == "__main__":
    swift = Car("KA01AB1234", "Maruti", "Swift", 1_800, seats=5)
    classic = Bike("KA05CD5678", "Royal Enfield", "Classic 350", 700, engine_cc=349)
    swift.display_details()
    print()
    classic.display_details()
    print()
    print("total vehicles:", Vehicle.get_total_vehicles())
