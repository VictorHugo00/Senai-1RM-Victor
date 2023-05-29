salario = float(input('Informe seu salario: '))

reajuste1 = salario * 1.10
reajuste2 = salario * 1.15

if salario >= 8250:
    print('Seu salario sera: ',reajuste1)
else:
    print('Seu salario sera: ',reajuste2)