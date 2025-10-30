# 6. Positivo ou Negativo:
# Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o
# valor zero como positivo.

valor=float(input('\nDigite um número para saber se é negativo ou positivo(0 é considerado positivo): '))

if valor<0:
    print('\nNegativo\n')
elif valor>=0:
    print('\nPositivo\n')
else:
    print('\nInsira um número por favor.\n')