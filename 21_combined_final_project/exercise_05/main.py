"""
Exercise 05 - Number Analysis Tool
==================================
Analyses a list of numbers and reports eight statistics at once.

    largest    smallest    total    average
    even count    odd count    positive count    negative count

CONSTRAINT: min(), max() and sum() are NOT used. Every statistic is
calculated with a loop written by hand.

THE KEY DESIGN DECISION - ONE PASS, NOT EIGHT
A naive version would loop eight separate times. This version collects
everything in a SINGLE pass, because each statistic only needs to look at
one number at a time. The results are returned as a dictionary, so the
caller gets all eight together.

WHY largest STARTS AT numbers[0] AND NOT 0
If every value were negative, nothing would beat 0 and the answer would be
0 - a number not even in the list. Starting from the first real element is
always safe. The same reasoning applies to smallest.

SAMPLE INPUT / OUTPUT
    Input : [12, -5, 8, 0, 33, -17, 4, 25, -8, 41]
    Largest 41   Smallest -17   Total 93   Average 9.30
    Even 5   Odd 5   Positive 6   Negative 3   Zeros 1
"""


def analyse_numbers(numbers):
    """
    Return a dictionary of statistics for a list of numbers.

    Calculates largest, smallest, total, average, and counts of even, odd,
    positive, negative and zero values - all in a single pass, and without
    using min(), max() or sum().

    Returns None if the list is empty.
    """
    if len(numbers) == 0:
        return None

    # INITIALIZATION : seed the champions with the FIRST real element,
    # and start every counter and accumulator at zero.
    largest = numbers[0]
    smallest = numbers[0]
    total = 0
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0
    zero_count = 0

    # One pass over the data collects every statistic
    for number in numbers:
        # running total, replacing sum()
        total += number

        # champion comparisons, replacing max() and min()
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

        # even or odd
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        # sign - zero is neither positive nor negative, so it needs its own branch
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1

    average = total / len(numbers)

    return {
        "count": len(numbers),
        "largest": largest,
        "smallest": smallest,
        "total": total,
        "average": average,
        "even_count": even_count,
        "odd_count": odd_count,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "zero_count": zero_count,
        "range": largest - smallest,
    }


def display_analysis(numbers, results):
    """Print the analysis results as a formatted report."""
    print()
    print("=" * 52)
    print("              NUMBER ANALYSIS REPORT")
    print("=" * 52)
    print(f"   Input : {numbers}")

    if results is None:
        print("   The list is empty - there is nothing to analyse.")
        print("=" * 52)
        return

    print(f"   Count : {results['count']} numbers")
    print("   " + "-" * 46)
    print(f"   {'Largest number':<24}: {results['largest']}")
    print(f"   {'Smallest number':<24}: {results['smallest']}")
    print(f"   {'Range (largest-smallest)':<24}: {results['range']}")
    print(f"   {'Total':<24}: {results['total']}")
    print(f"   {'Average':<24}: {results['average']:.2f}")
    print("   " + "-" * 46)
    print(f"   {'Even numbers':<24}: {results['even_count']}")
    print(f"   {'Odd numbers':<24}: {results['odd_count']}")
    print("   " + "-" * 46)
    print(f"   {'Positive numbers':<24}: {results['positive_count']}")
    print(f"   {'Negative numbers':<24}: {results['negative_count']}")
    print(f"   {'Zeros':<24}: {results['zero_count']}")
    print("   " + "-" * 46)

    # The two groupings must each account for every number
    even_odd = results["even_count"] + results["odd_count"]
    signs = results["positive_count"] + results["negative_count"] + results["zero_count"]
    print(f"   Check: even + odd = {even_odd}, "
          f"positive + negative + zero = {signs}, count = {results['count']}")
    print("=" * 52)


def read_numbers_from_user():
    """
    Ask the user for numbers separated by spaces and return them as a list.

    Returns an empty list if the user enters nothing. Invalid entries are
    reported and skipped rather than crashing the program.
    """
    entry = input("   Enter numbers separated by spaces (or press Enter to skip) : ")

    if entry.strip() == "":
        return []

    numbers = []
    for piece in entry.split():
        try:
            numbers.append(int(piece))
        except ValueError:
            print(f"      Skipping '{piece}' - it is not a whole number.")

    return numbers


def main():
    """Analyse a built-in sample list, then anything the user supplies."""
    print("=" * 52)
    print("              NUMBER ANALYSIS TOOL")
    print("=" * 52)
    print("   min(), max() and sum() are not used - every value is")
    print("   calculated with a loop, in a single pass over the data.")

    # --- Built-in examples, so the program demonstrates itself -------------
    samples = [
        [12, -5, 8, 0, 33, -17, 4, 25, -8, 41],
        [10, 20, 30, 40, 50],
        [-5, -12, -3, -40, -8],
        [7],
        [],
    ]

    for numbers in samples:
        display_analysis(numbers, analyse_numbers(numbers))

    # --- Then let the user try their own -----------------------------------
    print()
    print("=" * 52)
    print("              ANALYSE YOUR OWN NUMBERS")
    print("=" * 52)
    user_numbers = read_numbers_from_user()
    display_analysis(user_numbers, analyse_numbers(user_numbers))


if __name__ == "__main__":
    main()
