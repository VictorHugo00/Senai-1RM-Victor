while True: 
    valor = int(input('Informe um numero: '))
    if valor <0:
        break
    if valor & 2 == 0:
        print(f'{valor} é impar')
    else:
        print(f'{valor} é par')