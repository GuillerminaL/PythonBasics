character = input("Enter a character: ")

if character.lower() in "\.[]{}()<>*+-=!?^$|":
    print("{} is a special character".format(character))
else:
    print("{} is not a special character".format(character))
