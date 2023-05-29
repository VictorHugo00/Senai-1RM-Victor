km = int(input('Informe quantos você ira percorrer km: '))

kms = km * 0.50

kmss = km * 0.45

if kms <=200:
    print('voce ira pagar: {:.2f}'.format(kms))

else:
    if kmss >=200:
        print('voce ira pagar: {:.2f}'.format(kmss))



