import random
MIN_NUMBER = 1
MAX_NUMBER = 45
number_of_quick_picks = int(input("How many quick picks? "))
for each_line in range(number_of_quick_picks):
    quick_picks = []
    for i in range(6):
        pick = (random.randint(MIN_NUMBER, MAX_NUMBER))
        while pick in quick_picks:
            pick = (random.randint(MIN_NUMBER, MAX_NUMBER))
        quick_picks.append(pick)
        print(f"{pick:2d}", end=" ")
    print()
