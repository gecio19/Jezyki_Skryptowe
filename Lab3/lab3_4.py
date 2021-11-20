
imiona = list()

filepath = "imiona.txt"


f = open(filepath, "r")


imiona = f.read().splitlines()



print('Zawartość listy imion:',imiona)
