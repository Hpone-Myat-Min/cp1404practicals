for i in range(1, 21, 2):
    print(i, end=" ")
print()

for i in range(10, 101, 10):
    print(i, end=" ")
print()

number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1):
    print("*", end="")

for i in range(number_of_stars + 1):
    print("*" * i)
