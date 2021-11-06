import math


def funckjaK(a,b,c):
    delta = math.pow(b,2) - 4*a*c
    if(delta<0):
        print("Brak miejsc zerowych")
    elif(delta == 0 ):
        wynik = (-1)*b / 2*a
        print("Fynkcja ma tylko 1 miejsce zerowe:",wynik)
    elif(delta>0):
        print("Pierwiastek ma dwa miejsca zerowe:")

        Pierwszy = (((-1)*b) - math.sqrt(delta))/2*a
        Drugi = (((-1) * b) + math.sqrt(delta)) /2*a
        print("Pierwszy : ", Pierwszy)
        print("Pierwszy : ", Drugi)










print("Funcka kwadratowa : Ax^2 + Bx + C")

print("Podaj wyznaczik A")
A = input()
a = float(A)

print("Podaj wyznaczik B")
B = input()
b = float(B)

print("Podaj wyznaczik C")
C = input()
c = float(C)

funckjaK(a,b,c)