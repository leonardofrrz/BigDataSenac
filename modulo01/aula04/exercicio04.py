# 4. Código de Origem do Produto:
# Escreva um programa que leia o código de origem de um produto e imprima na tela a região
# de sua procedência, conforme a tabela abaixo:
#
#                                    /==========================================\
#                                    |código 1 sul     código 5 ou 6 nordeste   |
#                                    |código 2 norte   código 7, 8 ou 9 sudeste |
#                                    |código 3 leste   código 10 centro-oeste   |
#                                    |código 4 oeste   código 11 noroeste       |
#                                    \==========================================/
#
#Observação: caso o código não seja nenhum dos especificados, o produto deve ser
#encarado como “Importado”.
try:
    codigoOrigem=int(input('\nQual o código de origem do produto(de 1 á 11)?\n:'))

    match codigoOrigem:
        case 1:
            print('=====\n|Sul|\n=====')
        case 2:
            print('=======\n|Norte|\n=======')
        case 3:
            print('=======\n|Leste|\n=======')
        case 4:
            print('=======\n|Oeste|\n=======')
        case 5 | 6:
            print('==========\n|Nordeste|\n==========')
        case 7 | 8 | 9:
            print('=========\n|Sudeste|\n=========')
        case 10:
            print('==============\n|Centro-Oeste|\n==============')
        case 11:
            print('==========\n|Noroeste|\n==========')
        case _:
            print('=======================================\n|Por favor, insira um número de 1 á 11|\n=======================================')
except ValueError:
    print('=====================================\nPor favor, insira um número inteiro.\n=====================================')