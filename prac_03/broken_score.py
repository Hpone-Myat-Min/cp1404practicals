"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# TODO: Fix this!
import random
MIN_EXCELLENT_SCORE = 90
MIN_PASSING_SCORE = 50


def main():
    """Determine score status."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    score_status = determine_score_status(score)
    print(score_status)
    random_score = random.randint(0, 100)
    print(determine_score_status(random_score))


def determine_score_status(score):
    """Check which category score falls in."""
    if score >= MIN_EXCELLENT_SCORE:
        return "Excellent"
    elif score >= MIN_PASSING_SCORE:
        return "Passable"
    else:
        return "Bad"


main()
