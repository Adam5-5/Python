

#plansza

def rysujplansze(x=6,y=4):
      
    for i in range(x):
        print('   ',i+1,end='')
    print()
   
    for i in range(y):
          print(' ',(2*x+3)*'* ', end='')
          print()
          print(i+1,(x+2)*'*   ')

    print(' ',(2*x+3)*'* ', end='')
    print() 


rysujplansze()
