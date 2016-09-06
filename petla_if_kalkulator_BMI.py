#Piotr i Pawel
#Petla if sprawdzajaca BMI
wzrost=float(input("Podaj wzrost "))
waga=float(input("Podaj wagę "))


BMI=waga/(wzrost**2)

if BMI<18.5:
    print("niedowaga")
elif BMI<24.9:
    print("waga prawidłowa")
elif BMI<29.9:
    print("nadwaga")
else:
    print("otylosc")
