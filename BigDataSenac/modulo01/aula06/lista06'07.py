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

#---------------------------------FUNÇÕES----------------------------------------------
def origem_produtos():
    print("--- 4. CÓDIGO DE ORIGEM (MATCH/CASE) ---")
    try:
        codigo = int(input("Digite o código de origem (inteiro, ex: 7, 15 ou 90): "))
        
        # ESTRUTURA MATCH/CASE
        match codigo:
            case 1:
                procedencia = "Sul"
            case 2:
                procedencia = "Norte"
            case 3:
                procedencia = "Leste"
            case 4:
                procedencia = "Oeste"
            case 5 | 6:
                procedencia = "Nordeste"
            # Faixa com Condição (Guard: 'if')
            case n if 7 <= n <= 9:
                procedencia = "Sudeste"
            case 10:
                procedencia = "Centro-Oeste"
            case 11:
                procedencia = "Nordeste"
            # Caso Padrão (Default)
            case _:
                procedencia = "Importado"

        print(f"Resultado:\n  Código {codigo} -> Procedência: {procedencia}\n")
        
    except ValueError:
        print("ERRO: Digite um número inteiro válido.")

print(origem_produtos)