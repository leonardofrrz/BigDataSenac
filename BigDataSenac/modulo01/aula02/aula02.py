dinheiro= int(input('Quanto você tem na carteira? '))
if dinheiro>100:
    print("Pode comprar, manda bala!")
elif dinheiro<=100 and dinheiro>70:
    print('Junta mais um pouco bb...')
elif not dinheiro >0:
    print('Ta falido?')
else:
    print('Esquece.')