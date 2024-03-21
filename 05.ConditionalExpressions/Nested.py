name = input("What's your name? ")
color = input("Which is your favourite color? ")

if name.upper() == "JOHN":
    if color.upper() == "RED":
        print("Red is di lovely color!")
    else:
        print("That is not red!")
else:
    print("Nice choice, {}!".format(name.capitalize()))


