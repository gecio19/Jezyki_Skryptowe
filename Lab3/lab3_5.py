import pickle
imiona = list()



Idamskie = list()
Imeskie = list()
filepath = "imiona.txt"


f = open(filepath, "r")








imiona = f.read().splitlines()


for i in range(0,len(imiona)):



    if(imiona[i] == " Kosma" or imiona[i] == "Barnaba" or  imiona[i] == "Bonawentura" or imiona[i] == "Jarema" or imiona[i] == "Kuba"):
        Imeskie += [imiona[i]]

    else:
        if (imiona[i][len(imiona[i]) - 1] == "a"):
            Idamskie += [imiona[i]]


        else:
            Imeskie += [imiona[i]]












Idamskie.sort()
Imeskie.sort()

print('Zawartość listy imion Damskich:',Idamskie)
print('Zawartość listy imion Meskich:', Imeskie)




fD = open('Idamskie.pickle', 'wb')
pickle.dump(Idamskie,fD)
fD.close()

fM = open('Imeskie.pickle', 'wb')
pickle.dump(Imeskie,fM)
fM.close()





