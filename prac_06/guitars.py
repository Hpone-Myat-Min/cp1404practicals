from guitar import Guitar

print("My guitars!")
guitars = []

blank_name = False
while not blank_name:
    name = input("Name: ")
    if name == "":
        blank_name = True
    else:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        print(f"{name} ({year}) : ${cost:.2f} added.\n")

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)


