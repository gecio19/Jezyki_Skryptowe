





imiona=list()











for i in range(4):
    imie = input("Podaj imie")


    if(imie.isalpha() == True):                                              #sprawdzić czy ciąg znaków składa się z samych liter (metoda isaplha)



        if(str(imie.capitalize()) in imiona):      # capitalize() zmiana na duża litere pierwszego znaku
            print("już jest")


        else:
            imiona += [imie.capitalize()]









    else:
        print("Błąd w zapisie")






print('Zawartość listy imion:',imiona)




