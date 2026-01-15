# 3. Rendimento do Taxista:
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
# média do consumo em km/L e o lucro (líquido) do dia.

precoCombustivel=6.15

kmInicio=float(input('\nMarcação do odômetro no início do dia (km): '))
kmFinal=float(input('Marcação do odômetro no final do dia (km): '))
litrosGastos=float(input('Quantidade de litros de combustível gasto: '))
valorRecebido=float(input('Valor total recebido dos passageiros (R$): '))

kmPercorridos=kmFinal-kmInicio
mediaConsumo=kmPercorridos/litrosGastos
gastoCombustivel=litrosGastos*precoCombustivel
lucroLiquido=valorRecebido-gastoCombustivel

print(f'\n========== RELATÓRIO DO DIA ==========')
print(f'Quilômetros percorridos: {kmPercorridos:.2f} km')
print(f'Média de consumo: {mediaConsumo:.2f} km/L')
print(f'Gasto com combustível: R${gastoCombustivel:.2f}')
print(f'Valor recebido: R${valorRecebido:.2f}')
print(f'Lucro líquido do dia: R${lucroLiquido:.2f}')
print(f'======================================')


print(f'\n--- ANÁLISE DO CONSUMO ---')
if mediaConsumo>=12:
    print('Consumo EXCELENTE! O carro está muito econômico.')
elif mediaConsumo>=9:
    print('Consumo BOM. O carro está dentro da média.')
elif mediaConsumo>=7:
    print('Consumo REGULAR. Considere uma revisão.')
else:
    print('Consumo RUIM! O carro precisa de manutenção urgente.')


print(f'\n--- ANÁLISE DO LUCRO ---')
if lucroLiquido>300:
    print('Dia EXCELENTE! Lucro muito bom!')
elif lucroLiquido>150:
    print('Dia BOM! Lucro satisfatório.')
elif lucroLiquido>0:
    print('Dia FRACO. Lucro baixo.')
else:
    print('Dia com PREJUÍZO! Você gastou mais do que ganhou.\n')