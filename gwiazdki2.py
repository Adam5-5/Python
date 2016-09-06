
# GWIAZDKI
max = int(input('Maksymalna ilosc gwiazek w linii: '))
for i in range(max):
    print(i*" "+(max-i)*'*');
for i in range(max):
    print((max-i-1)*' '+(i+1)*'*')
