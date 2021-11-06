

def oblicz(liczba):
    if (liczba < 0):
        print("-1000")
    elif (liczba == 0):
        print("ZEROOO")
    elif (liczba > 0 and liczba < 10):
        print(liczba)
    elif (liczba >= 10 and liczba <= 100):
        print("dużo")
    elif (liczba > 100):
        print("bardzo dużo")
    print("Podana cyfra:", liczba)




print("Podaj cyfre")
x = input()
liczba = int(x)

oblicz(liczba)




