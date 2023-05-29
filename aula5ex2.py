from time import sleep

def contagem_regressiva (conta):
    for i in range (conta, -1, -1):
        print(i)
        sleep(0.5)
conta = int(input('insira um numero: '))

print('Sua contagem',contagem_regressiva(conta))