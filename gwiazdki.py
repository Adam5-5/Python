
#gwiazdki


i = int(input('liczba gwiazdek: '))
for j in range(i):
    for k in range(i-j):
        print("*",end="")
    print("")
for j in range(i):
    for k in range(j+1):
        print("*",end="")
    print("")
