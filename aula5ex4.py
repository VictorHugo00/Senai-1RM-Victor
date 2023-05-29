num = int(input('Digite o numero: '))
def verificar_par (num): 
    if (num%2) == 0:
        print('False',verificar_par(num))
    else:
        print('True',verificar_par(num))