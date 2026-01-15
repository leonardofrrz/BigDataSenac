# 2. Calculadora de IMC
# Crie um programa que leia a altura e o peso de N pessoas (pergunte ao usuário quantas
# pessoas são). Para cada pessoa, mostre seu IMC e a classificação.
# ● Fórmula: IMC = PESO / (ALTURA * ALTURA)
# ● Obrigatório (Função 1): Crie uma função calcular_imc(peso, altura) que receberá
# os valores e retornará o IMC calculado.
# ● Obrigatório (Função 2): Crie outra função obter_classificacao(imc) que recebe o
# valor do IMC (calculado pela função 1) e retorna uma string com a classificação.
# ○ Valores de Referência:
# ■ Menor que 18.5: "Abaixo do peso"
# ■ 18.5 a 24.9: "Peso normal"
# ■ 25.0 a 29.9: "Sobrepeso"
# ■ 30.0 ou mais: "Obesidade"
# ● O programa principal deve pedir N, fazer um loop N vezes, pedir peso e altura,
# chamar as duas funções e imprimir o resultado formatado.

# funcao01: caucula o imc
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

# funcao02: retorna a classificação
def obter_classificacao(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25.0:
        return 'Peso normal'
    elif imc < 30.0:
        return 'Sobrepeso'
    else:
        return 'Obesidade'

# programa principal
try:
    pessoas = int(input('Quantas pessoas medirão o IMC no total? '))
    
    if pessoas <= 0:
        print('Ok, até a proxima.')
    else:
        for i in range(pessoas):
            print(f'\n--- Pessoa {i+1} ---')
            altura = float(input('Qual a altura?(em metros) '))
            peso = float(input('Qual o peso?(em quilos) '))
            
            # Chama as funções
            imc = calcular_imc(peso, altura)            
            
            if imc > 0.1:
                classificacao = obter_classificacao(imc)
                # Mostra o resultado
                print(f'IMC: {imc:.2f}')
                print(f'Classificação: {classificacao}')
            else:
                print('Valor descrepante, informe corretamente.')
        
except ValueError:
    print('Por favor, digite um número válido.')