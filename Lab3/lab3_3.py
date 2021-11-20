
imiona=list()


filepath = "imiona.txt"
def zapis(imiona):
    f = open(filepath,"w", encoding="utf-8")
    for i in range(0, len(imiona)):

        f.write(imiona[i] + "\n")
    f.close()









while True:

    imie = input("Podaj imie")
    if(imie.lower() == "koniec"):     #lower zamienia wszystkie duże litery na małe
        imiona.sort()
        print('Zawartość listy imion:', imiona)
        zapis(imiona)

        break


    if(imie.isalpha() == True):                                              #sprawdzić czy ciąg znaków składa się z samych liter (metoda isaplha)



        if(str(imie.capitalize()) in imiona):      # capitalize() zmiana na duża litere pierwszego znaku
            print("już jest")


        else:
            imiona += [imie.capitalize()]


    else:
        print("Błąd w zapisie")







