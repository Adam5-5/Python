
# funkcje

def board(x = 5, y = 5):
    print ("  ", end = " ")
    for i in range(1, x + 1):
        print(i, end = " ")
    print("\n ", (2*x+1) * "*")
    for z in range(1, y + 1):
        print(z, x * "* " + "*\n ", (2*x+1) * "*" )
        
board()

