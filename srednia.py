
#Program oblicza średnie; arytmetyczną, geometrzyczną i harmoniczą


n = int(input('podaj ilość liczb: '))
liczby = []
sumaAr = 0
sumaGeo = 1
sumaHar = 0
for i in range(n):
    x = float(input('podaj liczbę: '))
    liczby.append(x)
    sumaAr = sumaAr + x
    sumaGeo = sumaGeo * x
    sumaHar = sumaHar + 1/x
print(liczby)
print('srednia arytmetyczna: ', sumaAr/n)
print('srednia geometryczna: ', sumaGeo ** (1/n))
print('srednia harmoniczna: ', n/sumaHar)
