
#PIRAMIDA
literyList=[]
n = int(input('Podaj losc pieter: '))
for i in range (27):
    literyList.append(chr(97+i))
for i in range(n):
    print((n-1-i)*" "+''.join(literyList[:(i+1)]),end='')
    print(''.join(reversed(literyList[:i])))

