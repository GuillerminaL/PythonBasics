'''
Ejercicio 2
Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están
en las posiciones 4, 7 y 9 sean multiplicados por 2; por último, mostrar la lista nueva con los
nuevos datos
'''

list = [1,2,3,4,5,6,7,8,9,10]
print("Current list: {}".format(list))
list[3] *= 2
list[6] *= 2
list[8] *= 2
print("Modified list (numbers in positions 4, 7, and 9 have been multiplied by 2): {}".format(list))