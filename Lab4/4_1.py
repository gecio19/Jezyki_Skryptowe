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
    def __str__(self):
        return ("Punkt(%g,%g)" % (self.x, self.y))





PunktA = Punkt(-3,4)
PunktB = Punkt(3,9)

print("Odległość od początku układ: :" , PunktA.odleglosc())
print("Dystans pomiędzy dwoma punktami :", PunktA.dystans(PunktB))

print("cos:",PunktA)






