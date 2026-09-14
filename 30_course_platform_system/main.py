"""
main.py - the learning platform demonstration
==============================================
Six courses - four self-paced, two premium - and the same two method names
answering differently on each.

    python main.py

All of the logic lives in course.py.
"""

from course import Course, PremiumCourse

LINE = "=" * 62


def title(number, text):
    print()
    print(LINE)
    print(f"  {number}. {text}")
    print(LINE)


def catalogue(courses):
    print(f"    {'course':<24}{'type':<16}{'weeks':>6}{'price':>11}{'pay':>11}")
    print(f"    {'-' * 68}")
    for course in courses:
        print(f"    {course.name:<24}{course.course_type():<16}"
              f"{course.duration_weeks:>6}{course.price:>11,.2f}"
              f"{course.final_price():>11,.2f}")


# ---------------------------------------------------------------- 1

def demo_1_catalogue():
    title(1, "Two classes, six courses")

    print(f"    Course.get_course_count()  -> {Course.get_course_count()}")
    print()

    courses = [
        Course("Python Basics", "V. Krishnan", 6, 4_999),
        Course("SQL Foundations", "R. Banerjee", 4, 3_499),
        Course("Data Structures", "V. Krishnan", 10, 6_999),
        Course("Git and GitHub", "S. Fernandes", 2, 1_499),
        PremiumCourse("Python Pro", "V. Krishnan", 12, 14_999,
                      mentor_support=True, live_sessions=16),
        PremiumCourse("Analytics Career Track", "R. Banerjee", 16, 24_999,
                      mentor_support=True, live_sessions=24),
    ]

    catalogue(courses)
    print()
    print(f"    Course.get_course_count()  -> {Course.get_course_count()}")
    print()
    print("    Six, not four. PremiumCourse.__init__ calls super().__init__,")
    print("    and the counter lives there - so the class method that counts")
    print("    courses never had to learn that premium courses exist.")
    return courses


# ---------------------------------------------------------------- 2

def demo_2_overriding(courses):
    title(2, "calculate_discount() - overridden, then extended")

    print("    Course.calculate_discount():")
    print(f"      base {Course.BASE_DISCOUNT}%, plus {Course.LONG_COURSE_BONUS}% "
          f"for {Course.LONG_COURSE_WEEKS} weeks or more")
    print()
    print("    PremiumCourse.calculate_discount():")
    print("      super().calculate_discount(), plus "
          f"{PremiumCourse.MENTOR_BONUS}% for a mentor")
    print(f"      and {PremiumCourse.LIVE_SESSION_BONUS}% per live session, "
          f"capped at {Course.MAX_DISCOUNT}%")
    print()

    print(f"    {'course':<24}{'weeks':>6}{'base':>7}{'total':>8}{'saves':>12}")
    print(f"    {'-' * 57}")
    for course in courses:
        print(f"    {course.name:<24}{course.duration_weeks:>6}"
              f"{course.BASE_DISCOUNT:>6}%{course.calculate_discount():>7}%"
              f"{course.discount_amount():>12,.2f}")

    print()
    print("    BASE_DISCOUNT is a class variable defined in both classes, so")
    print("    the same super() call returns a different number depending on")
    print("    which class the object belongs to:")
    print()
    print(f"      Course.BASE_DISCOUNT         -> {Course.BASE_DISCOUNT}")
    print(f"      PremiumCourse.BASE_DISCOUNT  -> {PremiumCourse.BASE_DISCOUNT}")


# ---------------------------------------------------------------- 3

def demo_3_super_arithmetic(courses):
    title(3, "What super() actually returned")

    pro = courses[4]

    print(f"    {pro.name}: {pro.duration_weeks} weeks, mentor "
          f"{pro.mentor_support}, {pro.live_sessions} live sessions")
    print()
    print(f"      super().calculate_discount()   "
          f"= {super(PremiumCourse, pro).calculate_discount():>5}%"
          f"   (base {pro.BASE_DISCOUNT} + long-course {Course.LONG_COURSE_BONUS})")
    print(f"      + mentor                       "
          f"= {PremiumCourse.MENTOR_BONUS:>5}%")
    sessions_line = (f"      + {pro.live_sessions} live sessions x "
                     f"{PremiumCourse.LIVE_SESSION_BONUS}%")
    print(f"{sessions_line:<37}"
          f"= {pro.live_sessions * PremiumCourse.LIVE_SESSION_BONUS:>5}%")
    print(f"      {'-' * 44}")
    print(f"      pro.calculate_discount()       "
          f"= {pro.calculate_discount():>5}%")
    print()
    print("    PremiumCourse did not re-implement the long-course bonus. It")
    print("    asked the parent for a number and added to it, so a change to")
    print("    the platform-wide rule reaches premium courses for free.")

    print()
    print("    The cap is real, not decorative:")
    print(f"      before  {pro.name}: {pro.calculate_discount()}%")
    pro.add_live_sessions(60)
    print(f"      pro.add_live_sessions(60)")
    print(f"      after   {pro.name}: {pro.calculate_discount()}%"
          f"   (capped at {Course.MAX_DISCOUNT}%)")


# ---------------------------------------------------------------- 4

def demo_4_details(courses):
    title(4, "show_course_details() - nine lines, then twelve")

    courses[0].show_course_details()
    print()
    courses[5].show_course_details()
    print()
    print("    The first nine lines of both blocks are the same method.")
    print("    PremiumCourse.show_course_details() is four lines long:")
    print()
    print("        def show_course_details(self):")
    print("            super().show_course_details()")
    print("            print(... mentor ...)")
    print("            print(... live ...)")
    print("            print(... per session ...)")


# ---------------------------------------------------------------- 5

def demo_5_one_loop(courses):
    title(5, "One loop over both classes")

    for course in courses:
        course.enrol(40 if isinstance(course, PremiumCourse) else 180)

    print(f"    {'course':<24}{'enrolled':>9}{'pay':>11}{'revenue':>14}")
    print(f"    {'-' * 58}")

    # the accumulator and champion patterns from exercise 18, over objects
    total, best = 0, courses[0]
    for course in courses:
        total += course.revenue()
        if course.revenue() > best.revenue():
            best = course
        print(f"    {course.name:<24}{course.enrolled:>9}"
              f"{course.final_price():>11,.2f}{course.revenue():>14,.2f}")

    print(f"    {'-' * 58}")
    print(f"    {'total':<24}{'':>9}{'':>11}{total:>14,.2f}")
    print(f"    {'top earner':<24}{best.name}")
    print()
    print("    revenue(), final_price() and enrol() are written once, in")
    print("    Course, and run on both classes. isinstance() appears once, to")
    print("    choose a different number of learners for a premium course.")


# ---------------------------------------------------------------- 6

def demo_6_class_members(courses):
    title(6, "The class variable and the class method")

    print(f"    Course.platform         -> {Course.platform}")
    print(f"    PremiumCourse.platform  -> {PremiumCourse.platform}"
          f"   <- inherited, not copied")
    print()
    Course.set_platform("Nova Learn Academy")
    print("    Course.set_platform('Nova Learn Academy')")
    print(f"    Course.platform         -> {Course.platform}")
    print(f"    PremiumCourse.platform  -> {PremiumCourse.platform}")
    print()
    for course in (courses[0], courses[4]):
        print(f"      {course.name:<24}{course.platform}")

    print()
    print(f"    Course.total_courses          -> {Course.total_courses}")
    print(f"    PremiumCourse.total_courses   -> {PremiumCourse.total_courses}")
    print(f"    Course.get_course_count()     -> {Course.get_course_count()}")
    print(f"    PremiumCourse.get_course_count() -> "
          f"{PremiumCourse.get_course_count()}")
    print()
    print("    One counter, held by Course, read through inheritance by both.")

    print()
    print("    The validation both classes share, and the one only the child has:")
    cases = [
        ("price of zero", lambda: Course("Free", "X", 4, 0)),
        ("duration of 0 weeks", lambda: Course("Instant", "X", 0, 999)),
        ("duration 2.5 weeks", lambda: Course("Odd", "X", 2.5, 999)),
        ("live_sessions = -3",
         lambda: PremiumCourse("Bad", "X", 8, 9_999, live_sessions=-3)),
        ("mentor_support = 'yes'",
         lambda: PremiumCourse("Bad", "X", 8, 9_999, mentor_support="yes")),
    ]
    for label, call in cases:
        try:
            call()
        except ValueError as error:
            print(f"      {label:<24} ValueError: {error}")

    print()
    print("    PremiumCourse never wrote the price or duration check - it")
    print("    inherited both. The two checks it did write run BEFORE")
    print("    super().__init__, so a course that is about to be refused is")
    print("    not counted on its way out:")
    print(f"      Course.get_course_count()  -> {Course.get_course_count()}"
          f"   (still {len(courses)}, after 5 refusals)")


def main():
    print()
    print(LINE)
    print("  EXERCISE 30 - Course and PremiumCourse")
    print("  Method overriding, super(), and a counter across two classes")
    print(LINE)

    courses = demo_1_catalogue()
    demo_2_overriding(courses)
    demo_3_super_arithmetic(courses)
    demo_4_details(courses)
    demo_5_one_loop(courses)
    demo_6_class_members(courses)

    print()
    print(LINE)
    print("  calculate_discount() is defined twice and duplicated nowhere:")
    print("  the child asks the parent for a number and adds to it.")
    print(LINE)
    print()


if __name__ == "__main__":
    main()
