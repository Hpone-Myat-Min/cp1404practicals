"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# TODO: Fix this!
MIN_EXCELLENT_SCORE = 90
MIN_PASSING_SCORE = 50
score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))
if score >= MIN_EXCELLENT_SCORE:
    print("Excellent")
elif score >= MIN_PASSING_SCORE:
    print("Passable")
else:
    print("Bad")
