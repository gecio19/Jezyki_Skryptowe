
import math
import  cmath




def funckjaK(a,b,c):

    delta = complex( b*b - (4*a*c))

    if((delta.real + delta.imag) < 0):
        print("Brak miejsc zerowych")
    elif((delta.real + delta.imag) == 0 ):
        wynik = (-1)*b / 2*a
        print("Fynkcja ma tylko 1 miejsce zerowe:",wynik)
    elif((delta.real + delta.imag) > 0):
        print("Pierwiastek ma dwa miejsca zerowe:")

        Pierwszy = (((-1)*b) - cmath.sqrt(delta))/2*a
        Drugi = (((-1) * b) + cmath.sqrt(delta)) /2*a
        print("Pierwszy : ", Pierwszy)
        print("Pierwszy : ", Drugi)








A = complex(input("Współczynnik A"))
B = complex(input("Współczynnik B"))
C = complex(input("Współczynnik C"))

funckjaK(A,B,C)






