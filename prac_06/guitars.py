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

""" Testing """
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("\nThese are my guitars:")
for i, guitar in enumerate(guitars, 1):
    if guitar.is_vintage():
        vintage_string = " (vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}")
