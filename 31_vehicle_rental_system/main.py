"""
main.py - the vehicle rental demonstration
===========================================
Two cars, two bikes, one parent class, and a static method that validates a
rental duration before a single vehicle is built.

    python main.py

All of the logic lives in vehicle.py.
"""

from vehicle import Bike, Car, Vehicle

LINE = "=" * 62


def title(number, text):
    print()
    print(LINE)
    print(f"  {number}. {text}")
    print(LINE)


def forecourt(fleet):
    print(f"    {'number':<13}{'vehicle':<26}{'type':<20}{'per day':>10}")
    print(f"    {'-' * 69}")
    for v in fleet:
        print(f"    {v.vehicle_number:<13}{v.brand + ' ' + v.model:<26}"
              f"{v.vehicle_type():<20}{v.rent_per_day:>10,.2f}")


# ---------------------------------------------------------------- 1

def demo_1_static_first():
    title(1, "is_valid_duration() - a static method, called first")

    print(f"    Vehicle.get_total_vehicles()  -> {Vehicle.get_total_vehicles()}")
    print("    No vehicle exists yet. The duration check does not need one:")
    print()
    for days in [1, 3, 7, 90, 0, -2, 91, 2.5, True, "3"]:
        print(f"      Vehicle.is_valid_duration({days!r:<6}) -> "
              f"{Vehicle.is_valid_duration(days)}")
    print()
    print(f"    The agency rents for {Vehicle.MIN_DAYS} to {Vehicle.MAX_DAYS} "
          f"whole days. 2.5 is refused")
    print("    because half a day is not a rental day, and True is refused")
    print("    because bool subclasses int - a hire of True would otherwise")
    print("    be a hire of one day.")
    print()
    print("    All three classes share it. There is one rule about durations:")
    print(f"      Car.is_valid_duration(7)   -> {Car.is_valid_duration(7)}")
    print(f"      Bike.is_valid_duration(7)  -> {Bike.is_valid_duration(7)}")


# ---------------------------------------------------------------- 2

def demo_2_fleet():
    title(2, "One parent, two children, four vehicles")

    fleet = [
        Car("KA01AB1234", "Maruti", "Swift", 1_800, seats=5),
        Car("KA02XY7788", "Toyota", "Innova", 3_200, seats=7),
        Bike("KA05CD5678", "Royal Enfield", "Classic 350", 700, engine_cc=349),
        Bike("KA09EF4321", "Honda", "Activa", 350, engine_cc=110),
    ]

    forecourt(fleet)
    print()
    print(f"    Vehicle.get_total_vehicles()  -> {Vehicle.get_total_vehicles()}")
    print()
    print("    Four, from a counter that lives in Vehicle. Car and Bike both")
    print("    call super().__init__, so neither had to know a counter exists.")
    print()
    print("    Car and Bike are siblings. Neither imports, mentions or inherits")
    print("    from the other:")
    print(f"      issubclass(Car, Vehicle)  -> {issubclass(Car, Vehicle)}")
    print(f"      issubclass(Bike, Vehicle) -> {issubclass(Bike, Vehicle)}")
    print(f"      issubclass(Car, Bike)     -> {issubclass(Car, Bike)}")
    return fleet


# ---------------------------------------------------------------- 3

def demo_3_rent(fleet):
    title(3, "calculate_rent(days) - defined three times, shared once")

    print(f"    Weekly discount: {Vehicle.WEEKLY_DISCOUNT}% from "
          f"{Vehicle.WEEKLY_DAYS} days, written once in Vehicle")
    print(f"    Car adds insurance of {Car.INSURANCE_PER_DAY:,.2f} per day")
    print(f"    Bike adds a helmet charge of {Bike.HELMET_CHARGE:,.2f}, once")
    print()

    print(f"    {'vehicle':<26}{'1 day':>11}{'3 days':>11}{'7 days':>11}"
          f"{'14 days':>11}")
    print(f"    {'-' * 70}")
    for v in fleet:
        row = "".join(f"{v.calculate_rent(d):>11,.2f}" for d in (1, 3, 7, 14))
        print(f"    {v.brand + ' ' + v.model:<26}{row}")

    print()
    swift, classic = fleet[0], fleet[2]
    print("    Where a 7-day Swift hire comes from:")
    print(f"      super().calculate_rent(7)  = {Vehicle.calculate_rent(swift, 7):>10,.2f}"
          f"   (7 x {swift.rent_per_day:,.2f}, less {Vehicle.WEEKLY_DISCOUNT}%)")
    print(f"      + insurance 7 x {Car.INSURANCE_PER_DAY:,.2f}   = "
          f"{swift.extras_for(7):>10,.2f}")
    print(f"      {'-' * 40}")
    print(f"      swift.calculate_rent(7)    = {swift.calculate_rent(7):>10,.2f}")
    print()
    print("    And a 7-day Classic hire:")
    print(f"      super().calculate_rent(7)  = "
          f"{Vehicle.calculate_rent(classic, 7):>10,.2f}")
    print(f"      + helmet, once             = {classic.extras_for(7):>10,.2f}")
    print(f"      {'-' * 40}")
    print(f"      classic.calculate_rent(7)  = {classic.calculate_rent(7):>10,.2f}")
    print()
    print("    Neither child re-implemented the weekly discount. Change it in")
    print("    Vehicle and all four rows above move together.")


# ---------------------------------------------------------------- 4

def demo_4_hiring(fleet):
    title(4, "Renting the fleet out")

    bookings = [(fleet[0], 4), (fleet[2], 10), (fleet[3], 2), (fleet[1], 7)]
    takings = 0

    for vehicle, days in bookings:
        owed = vehicle.rent_out(days)
        takings += owed
        print(f"      {vehicle.vehicle_number}  "
              f"{vehicle.brand + ' ' + vehicle.model:<28}"
              f"{days:>3} days {owed:>12,.2f}")

    print(f"      {'-' * 60}")
    print(f"      {'takings':<44}{takings:>12,.2f}")

    print()
    print("    Nothing can be hired out twice:")
    try:
        fleet[0].rent_out(2)
    except ValueError as error:
        print(f"      swift.rent_out(2) -> ValueError: {error}")

    print()
    print(f"      swift.return_vehicle() -> {fleet[0].return_vehicle()}")
    print(f"      swift.rent_out(2)      -> {fleet[0].rent_out(2):,.2f}")
    print(f"      swift.days_hired       -> {fleet[0].days_hired}")


# ---------------------------------------------------------------- 5

def demo_5_refusals(fleet):
    title(5, "What the agency refuses")

    swift = fleet[0]
    cases = [
        ("zero days", lambda: swift.calculate_rent(0)),
        ("negative days", lambda: swift.calculate_rent(-3)),
        ("half a day", lambda: swift.calculate_rent(2.5)),
        ("a string", lambda: swift.calculate_rent("7")),
        ("True", lambda: swift.calculate_rent(True)),
        ("longer than the maximum", lambda: swift.calculate_rent(120)),
        ("a car with 1 seat",
         lambda: Car("KA00ZZ0000", "Odd", "Monocycle", 500, seats=1)),
        ("a bike with 30cc",
         lambda: Bike("KA00ZZ0001", "Odd", "Toy", 100, engine_cc=30)),
        ("a rent of zero",
         lambda: Bike("KA00ZZ0002", "Free", "Ride", 0, engine_cc=110)),
    ]

    for label, call in cases:
        try:
            call()
        except ValueError as error:
            print(f"      {label:<26} ValueError: {error}")

    print()
    print(f"    Vehicle.get_total_vehicles()  -> {Vehicle.get_total_vehicles()}"
          f"   (still 4)")
    print("    Car and Bike check their own argument before calling")
    print("    super().__init__, so a vehicle that is refused is never counted.")

    print()
    print("    And the boundaries that are allowed:")
    print(f"      swift.calculate_rent(1)   -> {swift.calculate_rent(1):>10,.2f}")
    print(f"      swift.calculate_rent(90)  -> {swift.calculate_rent(90):>10,.2f}")


# ---------------------------------------------------------------- 6

def demo_6_details_and_class(fleet):
    title(6, "display_details(), and what the three classes share")

    fleet[1].display_details()
    print()
    fleet[2].display_details()
    print()
    print("    The first seven lines of both blocks are Vehicle's method.")
    print("    Car adds two, Bike adds two, and neither repeats the seven.")

    print()
    print(f"    Vehicle.agency  -> {Vehicle.agency}")
    Vehicle.set_agency("Nova Rentals India")
    print("    Vehicle.set_agency('Nova Rentals India')")
    print(f"      Vehicle.agency -> {Vehicle.agency}")
    print(f"      Car.agency     -> {Car.agency}")
    print(f"      Bike.agency    -> {Bike.agency}")
    print()
    for v in fleet[:3]:
        print(f"      {v.vehicle_number:<13}{v.agency}")

    print()
    print("    One loop over the whole fleet, whatever is in it:")
    print()
    # the accumulator and champion patterns from exercise 18, over objects
    total, busiest = 0, fleet[0]
    for v in fleet:
        total += v.days_hired
        if v.days_hired > busiest.days_hired:
            busiest = v
        print(f"      {v.vehicle_type():<20}{v.brand + ' ' + v.model:<26}"
              f"{v.days_hired:>3} days")
    print(f"      {'-' * 52}")
    print(f"      {'total days hired':<46}{total:>3}")
    print(f"      {'busiest':<46}{busiest.model}")


def main():
    print()
    print(LINE)
    print("  EXERCISE 31 - Vehicle Rental System")
    print("  One parent, two children, and a shared static validator")
    print(LINE)

    demo_1_static_first()
    fleet = demo_2_fleet()
    demo_3_rent(fleet)
    demo_4_hiring(fleet)
    demo_5_refusals(fleet)
    demo_6_details_and_class(fleet)

    print()
    print(LINE)
    print("  calculate_rent() exists three times and the weekly discount once.")
    print("  Car and Bike never mention each other.")
    print(LINE)
    print()


if __name__ == "__main__":
    main()
