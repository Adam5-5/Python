#
#Daniel Matkowski i Adrian Kiełczewski
#podnosimy do kwadratu kolejne elmenty tablicy za pomoca petli while

tablica=[13,5,7,9,16,25]
i=0
while i <len(tablica):
    zmienna= tablica[i]
    tablica[i]=zmienna*zmienna
    print(tablica[i])
    i=+1
