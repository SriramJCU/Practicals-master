COLOUR_TO_HEX = {"Alice Blue": "#f0f8ff", "Acid Green": "#b0bf1a", "Amethyst": "#9966cc", "Aqua": "#00ffff", "Army Green": "#4b5320",
                 "Arylide Yellow": "#e9d66b", "Baby Pink": "#f4c2c2", "Barn Red": "#7c0a02", "Bistre": "#3d2b1f", "Black Shadows": "#bfafb2"}


colour = input("Enter colour name: ").title()
while colour != "":
    if colour in COLOUR_TO_HEX:
        print(f"{colour} is {COLOUR_TO_HEX[colour]}")
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ").title()
