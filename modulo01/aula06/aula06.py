lista01=['abc', 2134124, {2.1, True, '...'}, [1,2,[3,2,1,4,[1,2,35,6,5]]]]
print(lista01[-1][2][4][2])
print(lista01[2])
print(lista01.index('abc'))
#
# lista []
# ----dentro da lista----
# dicionario {'nome' : 'maria'}
# set {}
# tupla ()
#
# --------- parte da aula07 ----------
lista02=[
    'Lavar louça',
    'Ir ao Mercado',
    'Lavar Banheiro',
    'Tirar Poeira',
    'Lavar o Quintal'
    ]

novosItens=input('Novo itens da lista: ')
lista02.append(novosItens) # .append adiciona algo na ultima posição da lista(-1).
print(lista02)             # .pop tira (pop nao tirar por nome, e sim por indice. ex.: 0, 1, 2...),
print(lista02[1][6 : 13], lista02[4][6:])  # para imprimir uma "palavra", no caso, selecionando o indice da primeira letra do elemento e da ultima. 
# é preciso inicar o indice do elemento desejado primeiro.(ex.: [1])
# se tiver só 6: ou :6 tambem da, no primeiro caso é do indice 6 em diante, e o segundo caso é tudo antes do 6
print('=' * 100)
lista03=lista02.copy()
novosItens=input('Novo itens da lista: ')
lista03.append(novosItens)
print(lista03)