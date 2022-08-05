def Calculadora(num1, num2, op):
    print('Calculadora')
    print('\n1 - soma', '\n2 - subtraçao', '\n3 - multiplicaçao', '\n4 - divisão')

    if op==1: 
          print('a soma é:', num1 + num2)
    elif op==2: 
          print('a subtraçao é:', num1 - num2)
    elif op==3:
          print('a multiplicaçao é:', num1 * num2)
    elif op==4:
          print('a divisão é:', num1 / num2)

     
    

Calculadora(20, 5, 3)

