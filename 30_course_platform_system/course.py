"""
course.py - Course, and PremiumCourse(Course)
==============================================
How a small online learning platform can model its catalogue with two classes
instead of one class and a pile of if-statements.

    Course
       |
    PremiumCourse

    from course import Course, PremiumCourse

    basics = Course("Python Basics", "V. Krishnan", 6, 4_999)
    pro    = PremiumCourse("Python Pro", "V. Krishnan", 12, 14_999,
                           mentor_support=True, live_sessions=16)

    basics.calculate_discount()   # 10  (%)
    pro.calculate_discount()      # 30  (%)  - super() + its own
    pro.show_course_details()     # the parent's block, plus three lines

Both classes define `calculate_discount()` and `show_course_details()`. In both
cases the child calls `super()` first and then adds to the answer, rather than
rewriting it.
"""


class Course:
    """A self-paced course in the catalogue."""

    # ---------------------------------------------------------------- class
    total_courses = 0                 # every course, premium or not
    platform = "Nova Learn"
    CURRENCY = "INR"
    BASE_DISCOUNT = 10                # percent, before any duration bonus
    LONG_COURSE_WEEKS = 8
    LONG_COURSE_BONUS = 5             # percent, for a course of 8 weeks or more
    MAX_DISCOUNT = 60                 # nothing may be cheaper than this

    # ------------------------------------------------------------ construct

    def __init__(self, name, instructor, duration_weeks, price):
        if not self.is_valid_price(price):
            raise ValueError(f"price must be greater than zero, got {price!r}")
        if isinstance(duration_weeks, bool) or not isinstance(duration_weeks, int):
            raise ValueError(f"duration must be a whole number of weeks, got {duration_weeks!r}")
        if duration_weeks <= 0:
            raise ValueError(f"duration must be at least 1 week, got {duration_weeks}")

        self.name = name
        self.instructor = instructor
        self.duration_weeks = duration_weeks
        self.price = float(price)
        self.enrolled = 0

        Course.total_courses += 1     # the class, so subclasses count here too

    # --------------------------------------------------------------- static

    @staticmethod
    def is_valid_price(price):
        """True when price is a number above zero. Needs no course."""
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            return False
        return price > 0

    # ------------------------------------------------------------- instance

    def course_type(self):
        """Overridden by PremiumCourse."""
        return "Course"

    def calculate_discount(self):
        """The discount percentage this course earns.

        A flat base, plus a bonus for anything eight weeks or longer. Returns a
        percentage rather than a price, so the child class can add to it.
        """
        discount = self.BASE_DISCOUNT
        if self.duration_weeks >= self.LONG_COURSE_WEEKS:
            discount += self.LONG_COURSE_BONUS
        return min(discount, self.MAX_DISCOUNT)

    def discount_amount(self):
        return round(self.price * self.calculate_discount() / 100, 2)

    def final_price(self):
        return round(self.price - self.discount_amount(), 2)

    def price_per_week(self):
        return round(self.final_price() / self.duration_weeks, 2)

    def enrol(self, count=1):
        """Add learners. Returns the new total."""
        if isinstance(count, bool) or not isinstance(count, int) or count <= 0:
            raise ValueError(f"enrolment must be a whole number above zero, got {count!r}")
        self.enrolled += count
        return self.enrolled

    def revenue(self):
        return round(self.final_price() * self.enrolled, 2)

    def show_course_details(self):
        """Print the course. PremiumCourse extends this rather than replacing it."""
        print(f"    {self.name}")
        print(f"      type       : {self.course_type()}")
        print(f"      instructor : {self.instructor}")
        print(f"      platform   : {self.platform}")
        print(f"      duration   : {self.duration_weeks} weeks")
        print(f"      price      : {self.CURRENCY} {self.price:>10,.2f}")
        print(f"      discount   : {self.calculate_discount()}%"
              f"   (-{self.CURRENCY} {self.discount_amount():,.2f})")
        print(f"      you pay    : {self.CURRENCY} {self.final_price():>10,.2f}")
        print(f"      per week   : {self.CURRENCY} {self.price_per_week():>10,.2f}")
        print(f"      enrolled   : {self.enrolled}")

    # ---------------------------------------------------------------- class

    @classmethod
    def get_course_count(cls):
        """How many courses exist, of any kind."""
        return cls.total_courses

    @classmethod
    def set_platform(cls, name):
        """Rename the platform for every course at once."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("platform name must be a non-empty string")
        Course.platform = name.strip()
        return Course.platform

    # -------------------------------------------------------------- dunders

    def __repr__(self):
        return (f"{type(self).__name__}({self.name!r}, {self.instructor!r}, "
                f"{self.duration_weeks!r}, {self.price!r})")


class PremiumCourse(Course):
    """A course with a mentor and live sessions. Costs more, discounts harder."""

    # its own values for two inherited class variables
    BASE_DISCOUNT = 20
    LIVE_SESSION_BONUS = 0.5          # percent per live session
    MENTOR_BONUS = 5                  # percent, when mentor support is included

    def __init__(self, name, instructor, duration_weeks, price,
                 mentor_support=True, live_sessions=0):
        # the child's own checks run FIRST, before super().__init__ - because
        # super().__init__ increments the counter, and a course that is about
        # to be refused must not be counted on its way out
        if not isinstance(mentor_support, bool):
            raise ValueError(f"mentor_support must be True or False, got {mentor_support!r}")
        if isinstance(live_sessions, bool) or not isinstance(live_sessions, int):
            raise ValueError(f"live_sessions must be a whole number, got {live_sessions!r}")
        if live_sessions < 0:
            raise ValueError(f"live_sessions must not be negative, got {live_sessions}")

        # the parent validates, stores the four common fields and counts
        super().__init__(name, instructor, duration_weeks, price)

        self.mentor_support = mentor_support
        self.live_sessions = live_sessions

    # ------------------------------------------------------------ overrides

    def course_type(self):
        return "Premium Course"

    def calculate_discount(self):
        """The parent's discount, plus what being premium adds."""
        discount = super().calculate_discount()        # not a rewrite - a base
        if self.mentor_support:
            discount += self.MENTOR_BONUS
        discount += self.live_sessions * self.LIVE_SESSION_BONUS
        return round(min(discount, self.MAX_DISCOUNT), 2)

    def show_course_details(self):
        """The parent's nine lines, plus the three only a premium course has."""
        super().show_course_details()
        print(f"      mentor     : {'included' if self.mentor_support else 'not included'}")
        print(f"      live        : {self.live_sessions} sessions")
        print(f"      per session: {self.CURRENCY} {self.cost_per_session():>10,.2f}")

    # ------------------------------------------------------------- its own

    def cost_per_session(self):
        """What one live session works out at. 0 when there are none."""
        if self.live_sessions == 0:
            return 0.0
        return round(self.final_price() / self.live_sessions, 2)

    def add_live_sessions(self, count):
        """Schedule more live sessions - which also moves the discount."""
        if isinstance(count, bool) or not isinstance(count, int) or count <= 0:
            raise ValueError(f"count must be a whole number above zero, got {count!r}")
        self.live_sessions += count
        return self.live_sessions


if __name__ == "__main__":
    basics = Course("Python Basics", "V. Krishnan", 6, 4_999)
    pro = PremiumCourse("Python Pro", "V. Krishnan", 12, 14_999,
                        mentor_support=True, live_sessions=16)
    basics.show_course_details()
    print()
    pro.show_course_details()
    print()
    print("courses:", Course.get_course_count())
