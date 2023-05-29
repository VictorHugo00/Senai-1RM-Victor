nota1 = float( input('Informe a nota: '))
nota2 = float( input('Informe a note: '))
nota3 = float( input('Informe a nota: '))

media = (nota1 + nota2 + nota3)/3

if media >=  6:
    print('Aprovado')
else:
    if media >= 5:
        print('Conselho de classe!')
    else:
        print('Reprovado')

print('Sua nota final foi:', media)