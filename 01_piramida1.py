
#PIRAMIDA

n = int(input('Podaj ilosc pieter: '))
literyString = 'abcdefghijklmnopqrstuvwxyz'
literyList = []

for l in literyString:
    literyList.append(l)

odstep=n-1
for i in range(n):
    print((odstep-i)*" ",end='')
    for j in range(i+1):
        print(literyList[j],end='')
    for j in range(i):
        print(literyList[-j+i-1],end='')
    print()

