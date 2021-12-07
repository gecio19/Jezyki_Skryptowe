import math






class Punkt(object):

    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y
    def odleglosc(self):
        return math.hypot(self.x, self.y)

    def dystans(self,other):
        odleglosc = math.sqrt( (self.x - other.x)**2 + ( self.y - other.y)**2)
        return odleglosc
    def __repr__(self):
        return ("Punkt(%g,%g)" % (self.x,self.y))





class Kolo(Punkt):

    def __init__(self, x= 0,y=0, r = 1):
        super().__init__(x,y)
        self.r =r
        
    def obwod(self):
        obw = 2* math.pi * self.r
        return obw
    def pole(self):
        pole = math.pi* (self.r)**2
        return pole

    def przesun(self, wektor ):
        self.x = self.x + wektor[0]
        self.y = self.y +wektor[1]
    def czy_wsp(self, other):

        odleglość = math.sqrt( (self.x - other.x)**2 + ( self.y - other.y)**2)
        Spromieni = self.r + other.r
        if( odleglość < Spromieni):
            return False
        else:
            return True

    def __repr__(self):
        return ("Okrąg o środku (%g,%g)  i promieniu (%g)" % (self.x, self.y, self.r))

    def __str__(self):
        return ("Okrąg o środku (%g,%g)  i promieniu (%g)" % (self.x,self.y,self.r))




kolo = Kolo(0,0,2)
print(kolo.obwod())
print(kolo.pole())


print(kolo)
kolo2 = Kolo(15,0,2)


'''
kolo.przesun((1,2))

print(kolo)
kolo.przesun([-1,-1])
print(kolo)
'''

if(kolo.czy_wsp(kolo2) == True):
    print("Nie nachodzą na siebie")
else:
    print("Nachodzą na siebie")