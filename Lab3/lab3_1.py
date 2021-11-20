

Dict = {'0': 'zero',
        '1':'jeden',
        '2':'dwa',
        '3': 'trzy',
        '4': 'cztery',
        '5': 'pięc',
        '6': 'sześć',
        '7': 'siedem',
        '8': 'osiem',
        '9': 'dziweięc',
        '10': 'dziesięć'









                    }







print("Podaj cyfre z zakresu 0 do 10 ")

while True:

    x = input()
    if(int(x)<=10):
        print(Dict[x])
    else:
        print("Nie jest w zakresie słownika")







