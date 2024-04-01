'''
En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un
programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no
este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
'''

capitals = {"Guatemala": "Ciudad de Guatemala", "El_salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa_rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
enteredCountry = (input("Enter a country name in spanish: "))
enteredCountry = enteredCountry.lower().capitalize()
if ( " " in enteredCountry):
    enteredCountry = enteredCountry.replace(" ", "_")

if ( enteredCountry in capitals ):
    capital = capitals[enteredCountry]
    if ("_" in enteredCountry):
        enteredCountry = enteredCountry.replace("_", " ")
        words = enteredCountry.split()
        enteredCountry = words[0] + " " + words[1].capitalize()
    print("The capital city of {} is {}".format(enteredCountry, capital))
else:
    print("The capital city of {} is not in the dictionary. \nCurrent dictionary entries: {}".format(enteredCountry, (capitals.keys())))