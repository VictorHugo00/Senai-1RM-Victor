listanum = []
mai = 0
men = 0
for c in range(0, 3):
    listanum.append(int(input(f'Digite um valor para a Posicao {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'O maior valor digitado foi {mai}')
print(f'O menor valor digitado foi {men}')