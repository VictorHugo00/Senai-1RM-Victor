print('Qual o valor do salario?')
salario = float(input())

print('Qual sera o aumento salarial?')
porcentagem = float(input())

aumento = salario*porcentagem/100
salariooficial = salario + aumento

print('salario atual: R$',salario)
print('\nO valor do aumento sera: R$' ,aumento)
print('o valor do salario com reajuste sera: R$' ,salariooficial)