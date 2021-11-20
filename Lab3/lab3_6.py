import  pickle

Idamskie = list()
Imeskie = list()




fM = open('Imeskie.pickle','rb')
Imeskie = pickle.load(fM)
fM.close()

fD = open('Idamskie.pickle','rb')
Idamskie = pickle.load(fD)
fD.close()



print("Imiona Meskie po deserializacji: ",Imeskie)
print("Imiona Damskie po deserializacji: ",Idamskie)
