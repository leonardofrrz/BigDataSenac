# 2. Quantidade de Caixas de Azulejos:
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
# todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m².

import math

comprimento=float(input('\nQual o comprimento do cômodo em metros? '))
largura=float(input('Qual a largura do cômodo em metros? '))
altura=float(input('Qual a altura do cômodo em metros? '))

# cálculo da área das paredes
# uma cozinha retangular tem 4 paredes:
# 2 paredes com dimensões: comprimento × altura
# 2 paredes com dimensões: largura × altura

parede1=comprimento*altura
parede2=comprimento*altura
parede3=largura*altura
parede4=largura*altura

areaTotal=parede1+parede2+parede3+parede4

# ou de forma simplificada: areaTotal=2*(comprimento*altura)+2*(largura*altura)
# cada caixa tem 1,5 m²

areaPorCaixa=1.5
caixasNecessarias = math.ceil(areaTotal / areaPorCaixa)
print('\n===========================================================')
print(f'Área total das paredes: {areaTotal:.2f}m²')
print(f'Quantidade de caixas de azulejos necessárias: {caixasNecessarias} caixas')
print('===========================================================\n')