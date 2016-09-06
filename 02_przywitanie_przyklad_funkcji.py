#Przykladowy program, ktory ilustruje użycie funkcji
#

def przywitanie(imie, plec):
    print("Witaj")
    if plec == "m":
        print("Drogi " + imie + " !")
    elif plec == "k":
        print("Droga " + imie + " !")
    elif plec == 't':
        print('pa')

przywitanie("Pawle", 't')
przywitanie("Jaceku", 'm')
przywitanie("Malgosiu", 'k')
