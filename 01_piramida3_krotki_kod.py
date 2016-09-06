
# wczytujemy liczbe i na podstawie liczby kształt z liter
n= int (input('Podaj liczbę' ))
tab = 'abcdefghijklmnoprstuwxyz'
 for y in range (n+1):
    print ( (n-y)*(' ') + tab[0:y+1], end="")
    for i in range(y-1, -1, -1):
        print(tab[i], end="")
    print ("") 
        
