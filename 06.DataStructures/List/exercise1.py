'''
Ejercicio 1
En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez,
debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo
lugar:
[20, 50, "Curso", 'Python', 3.14]
'''

list = [20, 50, "Curso", 'Python', 3.14]
print("Current list: {}".format(list))
list[0] = input("Enter a value to overwrite the first value of the list: ")
list[1] = input("Enter a value to overwrite the second value of the list: ")
print("New list: {}".format(list))