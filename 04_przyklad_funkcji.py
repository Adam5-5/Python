# przykladowy program ilustrujacy dzialanie funkcji

def przywitanie(imie, plec="m"):
    print("Witaj")
    if plec == "m":
        print("Drogi " + imie + " !")
    elif plec == "k":
        print("Droga " + imie + " !")
    elif plec == 't':
        print('pa')


przywitanie("Jaceku")
przywitanie("Pawle", 't')
przywitanie("Malgosiu", 'k')
