COLOR_NAMES_TO_CODES = {"Amber": '#ffbf00', "Aqua": '#ffbf00', "Beaver": '#ffbf00',
                        "Black": '#ffbf00', "Blond": '#ffbf00', 'Boysenberry': '#ffbf00',
                        "Bronze": '#ffbf00', "Burgundy": '#ffbf00', "Camel": '#ffbf00',
                        "Cardinal": '#ffbf00'}

color_name = input("Enter a color name: ").title()
while color_name != "":
    if color_name in COLOR_NAMES_TO_CODES:
        print(f"Color code of {color_name} is {COLOR_NAMES_TO_CODES[color_name]}")
    else:
        print("Invalid color name")
    color_name = input("Enter a color name: ").title()
