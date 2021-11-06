def fibonacci(n):
    a = 1
    b = 0
    for i in range(0,n,1):

        print(b)
        b += a
        a = b-a


print("Podaj pierwsza cyfrę z zakresu")
x = input()
xcyfra = int(x)
fibonacci(xcyfra)