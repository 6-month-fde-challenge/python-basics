"""
Exercise 04 - Quiz Application
==============================
Asks five Python questions one at a time, checks each answer, keeps score,
and shows a final percentage with a grade.

DATA STRUCTURE
Each question is a dictionary holding the question text, four options, the
correct letter and a short explanation. All five live in one list, so the
quiz is driven by a single for loop.

FUNCTIONS
    ask_question()      - display one question and return the user's answer
    check_answer()      - compare the answer with the correct option
    show_final_result() - percentage, grade and a review of any mistakes
    main()              - runs the quiz

LOOPS USED
    for   - over the five questions (the count is known)
    while - to re-ask until a valid option letter is entered (count unknown)

SAMPLE INPUT / OUTPUT
    Question 1 of 5 ... Your answer: b   -> CORRECT   (score 1/1)
    Question 2 of 5 ... Your answer: a   -> WRONG, the answer was c
    ...
    FINAL SCORE : 4 / 5      PERCENTAGE : 80.00%      GRADE : B
"""

QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {"a": "func", "b": "def", "c": "function", "d": "define"},
        "answer": "b",
        "explanation": "Functions are declared with the `def` keyword.",
    },
    {
        "question": "What is the data type of the value  5 / 2  in Python 3?",
        "options": {"a": "int", "b": "str", "c": "float", "d": "bool"},
        "answer": "c",
        "explanation": "A single slash always returns a float: 5 / 2 is 2.5.",
    },
    {
        "question": "Which of these collections does NOT allow duplicate values?",
        "options": {"a": "list", "b": "tuple", "c": "set", "d": "string"},
        "answer": "c",
        "explanation": "A set stores only unique values; duplicates are dropped.",
    },
    {
        "question": "What does the `break` statement do inside a loop?",
        "options": {
            "a": "Skips the current pass only",
            "b": "Ends the entire loop immediately",
            "c": "Restarts the loop from the beginning",
            "d": "Pauses the loop",
        },
        "answer": "b",
        "explanation": "`break` exits the whole loop. `continue` skips one pass.",
    },
    {
        "question": "What will  len('Python')  return?",
        "options": {"a": "5", "b": "6", "c": "7", "d": "Error"},
        "answer": "b",
        "explanation": "P-y-t-h-o-n is six characters, so len() returns 6.",
    },
]

VALID_OPTIONS = ["a", "b", "c", "d"]


def ask_question(number, total, item):
    """
    Display one question and return the user's chosen option letter.

    Keeps asking until one of a, b, c or d is entered.
    """
    print()
    print("=" * 56)
    print(f"   QUESTION {number} OF {total}")
    print("=" * 56)
    print(f"   {item['question']}")
    print()

    for letter in VALID_OPTIONS:
        print(f"      {letter}) {item['options'][letter]}")

    print()

    # while: the user may mistype any number of times before answering validly
    answer = ""
    while answer not in VALID_OPTIONS:
        answer = input("   Your answer (a/b/c/d) : ").strip().lower()
        if answer not in VALID_OPTIONS:
            print(f"      '{answer}' is not a valid option. Please enter a, b, c or d.")

    return answer


def check_answer(item, given):
    """Return True if the given answer matches the correct option."""
    return given == item["answer"]


def calculate_percentage(score, total):
    """Return the score as a percentage of the total questions."""
    if total == 0:
        return 0.0
    return (score / total) * 100


def assign_grade(percentage):
    """Return a letter grade for a quiz percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    return "F"


def show_final_result(score, total, mistakes):
    """Display the final score, percentage, grade and any wrong answers."""
    percentage = calculate_percentage(score, total)

    print()
    print("=" * 56)
    print("                  QUIZ COMPLETE")
    print("=" * 56)
    print(f"   Questions answered : {total}")
    print(f"   Correct answers    : {score}")
    print(f"   Wrong answers      : {total - score}")
    print("   " + "-" * 50)
    print(f"   FINAL SCORE  : {score} / {total}")
    print(f"   PERCENTAGE   : {percentage:.2f}%")
    print(f"   GRADE        : {assign_grade(percentage)}")
    print("   " + "-" * 50)

    if percentage == 100:
        print("   Perfect score. Every answer correct.")
    elif percentage >= 60:
        print("   A solid pass.")
    else:
        print("   Below 60% - worth revising these topics.")

    if len(mistakes) > 0:
        print()
        print("   REVIEW OF WRONG ANSWERS")
        print("   " + "-" * 50)
        for item in mistakes:
            correct_letter = item["answer"]
            print(f"   Q: {item['question']}")
            print(f"      Correct answer: {correct_letter}) "
                  f"{item['options'][correct_letter]}")
            print(f"      {item['explanation']}")
            print()

    print("=" * 56)


def main():
    """Run the quiz from the first question to the final result."""
    print("=" * 56)
    print("              PYTHON QUIZ APPLICATION")
    print("=" * 56)
    print(f"   {len(QUESTIONS)} questions. One mark each. Answer with a, b, c or d.")

    # INITIALIZATION : the score and the list of mistakes, before the loop
    score = 0
    mistakes = []

    # for: the number of questions is known in advance
    for number, item in enumerate(QUESTIONS, start=1):
        answer = ask_question(number, len(QUESTIONS), item)

        if check_answer(item, answer):
            score += 1
            print(f"   CORRECT. Score is now {score}/{number}.")
        else:
            mistakes.append(item)
            correct_letter = item["answer"]
            print(f"   WRONG. The answer was {correct_letter}) "
                  f"{item['options'][correct_letter]}")
            print(f"   Score is still {score}/{number}.")

    show_final_result(score, len(QUESTIONS), mistakes)


if __name__ == "__main__":
    main()
