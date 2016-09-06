
# wczytujemy 2 nazwiska od uzytkownikow
# wyswietlenie informacji

x=input('podaj imie i nazwisko 1: ')
y=input('podaj imie i nazwisko 2: ')

a1=x.split()
a2=y.split()


max=max(len(x),len(y))

print('Witajcie'.center(max,'*'))
print(x)
print(str(len(a1[0])).rjust(len(a1[0])),str(len(a1[1])).rjust(len(a1[1])))
print(y)
print(str(len(a2[0])).rjust(len(a2[0])),str(len(a2[1])).rjust(len(a2[1])))



      

