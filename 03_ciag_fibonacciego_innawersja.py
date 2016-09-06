
#Funkcje Fibonnacci


#n = int(input("Podaj liczbe"))
def fib(n):
    a = 0
    b = 1
    temp = 0
    wynik = [0, 1]
    for i in range(n):
            wynik.append(a+b)
            temp = a
            a = b
            b = b+temp
    print(wynik)

fib(12)

