

print("Podaj Rok")
x = input()
rok = int(x)

if(rok% 4 == 0 and rok% 100 != 0 or rok %400 == 0):
    print("Rok jest przestępny")
else:
    print("Rok jest nieprzestępny")