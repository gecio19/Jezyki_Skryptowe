print("Podaj pierwsza cyfrę z zakresu")

x = input()
xcyfra = int(x)


print("Podaj ostatnią cyfrę z zakresu")

y = input()
ycyfra = int(y)


for i in range(xcyfra,ycyfra+1):
    if(i%2 == 0 and i%17 == 0):
        print(i)



