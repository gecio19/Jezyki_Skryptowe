print("Podaj cyfre")
x = input()
cyfra = int(x)

if(cyfra < 0 ):
    print("-1000")
elif(cyfra==0):
    print("ZEROOO")
elif(cyfra>0 and cyfra <10):
    print(cyfra)
elif(cyfra >= 10 and cyfra <= 100):
    print("dużo")
elif(cyfra>100):
    print("bardzo dużo")




