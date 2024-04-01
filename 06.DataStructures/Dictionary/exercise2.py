'''
Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un
número; el programa debe imprimir el jugador al que hace referencia ese número

{

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}

'''

players = {
    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa" }

enteredNumber = int(input("Enter a number to know the player name: "))
if ( enteredNumber in players ):
    print("The player number {} is {}".format(enteredNumber, players[enteredNumber]))
else:
    sorted_players_by_number = sorted(players.keys())
    #sorted_players_by_number = sorted(players.items(), key=lambda x: x[0])
    #sorted_players_by_name = sorted(players.items(), key=lambda x: x[1])
    print("There's no player with the number {}. \nThe current ones are: {}"
          .format(enteredNumber, sorted_players_by_number ))