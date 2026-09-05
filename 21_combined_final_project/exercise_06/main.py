"""
Exercise 06 - Employee Salary Analyzer
======================================
Analyses a payroll and reports:

    total payroll        average salary
    highest salary       lowest salary
    employees earning above the average

DATA STRUCTURE
A list of dictionaries, one per employee, each holding a name, department
and salary. This is the same shape a database query or a CSV file would
give you.

FUNCTIONS
    total_payroll()          - add every salary, without sum()
    average_salary()         - total divided by headcount
    highest_paid()           - the champion pattern, without max()
    lowest_paid()            - the champion pattern, without min()
    above_average_earners()  - filter using the calculated average
    display_report()         - print the full analysis

NOTE ON THE AVERAGE
The average is usually NOT the midpoint of the list. A few large salaries
pull it upward, so fewer than half the staff may be above it. The report
prints the count so this is visible rather than assumed.

SAMPLE INPUT / OUTPUT
    Employees        : 8
    Total payroll    : Rs.4,120,000
    Average salary   : Rs.515,000.00
    Highest          : Kavya (Rs.980000) - Management
    Lowest           : Rohit (Rs.240000) - Support
    Above average    : 3 of 8 employees
"""

employees = [
    {"name": "Rahul", "department": "Engineering", "salary": 620000},
    {"name": "Priya", "department": "Engineering", "salary": 750000},
    {"name": "Aman", "department": "Marketing", "salary": 410000},
    {"name": "Sneha", "department": "Design", "salary": 380000},
    {"name": "Kavya", "department": "Management", "salary": 980000},
    {"name": "Rohit", "department": "Support", "salary": 240000},
    {"name": "Meera", "department": "Engineering", "salary": 540000},
    {"name": "Arjun", "department": "Marketing", "salary": 200000},
]


def total_payroll(staff):
    """Return the sum of every salary, calculated without sum()."""
    total = 0
    for employee in staff:
        total += employee["salary"]
    return total


def average_salary(staff):
    """Return the mean salary, or 0 if there are no employees."""
    if len(staff) == 0:
        return 0
    return total_payroll(staff) / len(staff)


def highest_paid(staff):
    """
    Return the employee with the highest salary, without using max().

    Returns None if the staff list is empty.
    """
    if len(staff) == 0:
        return None

    # Start with the first real employee, not an assumed value of 0
    top = staff[0]
    for employee in staff:
        if employee["salary"] > top["salary"]:
            top = employee
    return top


def lowest_paid(staff):
    """
    Return the employee with the lowest salary, without using min().

    Returns None if the staff list is empty.
    """
    if len(staff) == 0:
        return None

    bottom = staff[0]
    for employee in staff:
        if employee["salary"] < bottom["salary"]:
            bottom = employee
    return bottom


def above_average_earners(staff):
    """Return a list of employees earning strictly more than the average."""
    average = average_salary(staff)
    earners = []
    for employee in staff:
        if employee["salary"] > average:
            earners.append(employee)
    return earners


def below_average_earners(staff):
    """Return a list of employees earning at or below the average."""
    average = average_salary(staff)
    earners = []
    for employee in staff:
        if employee["salary"] <= average:
            earners.append(employee)
    return earners


def salary_by_department(staff):
    """Return a dictionary mapping each department to its total salary bill."""
    totals = {}
    for employee in staff:
        department = employee["department"]
        if department in totals:
            totals[department] += employee["salary"]
        else:
            totals[department] = employee["salary"]
    return totals


def display_report(staff):
    """Print the complete salary analysis report."""
    print()
    print("=" * 58)
    print("               EMPLOYEE SALARY ANALYZER")
    print("=" * 58)

    if len(staff) == 0:
        print("   No employees on record - nothing to analyse.")
        print("=" * 58)
        return

    # --- The payroll itself -------------------------------------------------
    print(f"   {'NAME':<10}{'DEPARTMENT':<16}{'SALARY':>14}")
    print("   " + "-" * 44)
    for employee in staff:
        print(f"   {employee['name']:<10}{employee['department']:<16}"
              f"{employee['salary']:>14,}")
    print("   " + "-" * 44)

    # --- The headline figures ----------------------------------------------
    total = total_payroll(staff)
    average = average_salary(staff)
    top = highest_paid(staff)
    bottom = lowest_paid(staff)

    print()
    print("   SUMMARY")
    print("   " + "-" * 50)
    print(f"   {'Employees':<22}: {len(staff)}")
    print(f"   {'Total payroll':<22}: Rs.{total:,}")
    print(f"   {'Average salary':<22}: Rs.{average:,.2f}")
    print(f"   {'Highest salary':<22}: Rs.{top['salary']:,}  "
          f"({top['name']}, {top['department']})")
    print(f"   {'Lowest salary':<22}: Rs.{bottom['salary']:,}  "
          f"({bottom['name']}, {bottom['department']})")
    print(f"   {'Salary range':<22}: Rs.{top['salary'] - bottom['salary']:,}")

    # --- Above and below the average ---------------------------------------
    above = above_average_earners(staff)
    below = below_average_earners(staff)

    print()
    print(f"   EMPLOYEES EARNING ABOVE THE AVERAGE (Rs.{average:,.2f})")
    print("   " + "-" * 50)
    for employee in above:
        difference = employee["salary"] - average
        print(f"   {employee['name']:<10}Rs.{employee['salary']:>10,}"
              f"   (Rs.{difference:,.2f} above average)")

    print(f"   {len(above)} of {len(staff)} employees are above the average.")
    print(f"   {len(below)} of {len(staff)} are at or below it.")
    print()
    print("   Note: the average is not the midpoint. A few large salaries pull")
    print("   it upward, so fewer than half the staff can be above it.")

    # --- Department breakdown ----------------------------------------------
    print()
    print("   SALARY BILL BY DEPARTMENT")
    print("   " + "-" * 50)
    departments = salary_by_department(staff)
    for department, amount in departments.items():
        share = (amount / total) * 100
        print(f"   {department:<16}Rs.{amount:>12,}   ({share:5.1f}% of payroll)")

    print("=" * 58)


def main():
    """Run the employee salary analyzer."""
    display_report(employees)

    # Demonstrate that the empty case is handled rather than crashing
    print()
    print("   Edge case - an empty payroll:")
    display_report([])


if __name__ == "__main__":
    main()
