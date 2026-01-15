# 1. Cálculo de Lâmpadas:
# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
# iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
# lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
# cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
# 3m² existe um bocal para uma lâmpada.
import math
potenciaLamp= int(input('\nQuantos watts tem a lâmpada: '))
largura= float(input('Qual a largura do cômodo(em metros): '))
comprimento= float(input('qual o comprimento do cômodo(em metros): '))

# 3 watts por m².
# a cada 3m² existe um bocal para uma lâmpada.

area=largura*comprimento
potenciaNecessaria=area*3
bocaisDisponiveis=area/3
lampNecessarias=potenciaNecessaria/potenciaLamp

print('\n================================================INFORMAÇÕES========================================================')
print(f'A área do cômodo é de: {area:.2f}m².')
print(f'A potência necessária pra iluminar ele é de: {potenciaNecessaria:.2f} watts.')
print(f'O número de bocais disponiveis neste cômodo é de: {math.ceil(bocaisDisponiveis)}.')
print(f'Seguindo a potência por lâmpada inserida, o número necessário para iluminar o comodo é de: {math.ceil(lampNecessarias)} lâmpadas no total.')
print('===================================================================================================================\n')

if bocaisDisponiveis<lampNecessarias:
    print(f'\n----------------------------------------------------------------------------------------------------------\n ATENÇÃO!!! O número de lâmpadas necessárias ultrapassou o limite de bocais no comodo(1 bocal a cada 3m²)\n----------------------------------------------------------------------------------------------------------\n')

# lembrando que importei a bibliotéca math no início do código para poder arredondar o número em 2 variaveis. 