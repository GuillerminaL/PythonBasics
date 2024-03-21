from math import sqrt
x1 = 0
x2 = 0

a = int(input("Enter the value of 'a': "))
b = int(input("Enter the value of 'b': "))
c = int(input("Enter the value of 'c': "))

fst = b*-1
snd = b**2 - 4*a*c  # --> sqrt = (b**2 - 4*a*c)**0.5
trd = 2*a

if (snd < 0):
    print("Can't find the square root of a negative number")
else:
    snd = sqrt(snd)
    x1 = (fst + snd) / trd
    x2 = (fst - snd) / trd
    print("La solución es:   \nx1=", x1, "\nx2=", x2)

'''
Enter the value of 'a': 3
Enter the value of 'b': 5
Enter the value of 'c': 2
La solución es:   
x1= -0.6666666666666666 
x2= -1.0
'''