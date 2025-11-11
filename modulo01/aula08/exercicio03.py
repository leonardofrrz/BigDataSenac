# 3. Conversor de Temperatura
# Crie um programa que permita ao usuário converter temperaturas entre Celsius e
# Fahrenheit.
# ● Função 1: Crie uma função celsius_para_fahrenheit(temp_c) que recebe a
# temperatura em Celsius e retorna o valor em Fahrenheit.
# ○ Fórmula: F = (C * 9/5) + 32
# ● Função 2: Crie uma função fahrenheit_para_celsius(temp_f) que recebe a
# temperatura em Fahrenheit e retorna o valor em Celsius.
# ○ Fórmula: C = (F - 32) * 5/9
# ● O programa principal deve perguntar ao usuário qual conversão ele quer fazer (ex:
# "1 para C->F" ou "2 para F->C"), pedir o valor, chamar a função correta e mostrar o
# resultado.
# Desafio: Criar uma única função que faça qualquer uma das conversões,
# sempre perguntando ao usuário qual é desejada.
'''
# funcao01: celsius pra fahrenheit
def celsiusToFahrenheit(tempC):
    tempF=(tempC * 9/5) + 32
    return(tempF)

# funcao02: fahrenheit pra celsius
def fahrenheitToCelsius(tempF):
    tempC=(tempF - 32) * 5/9
    return(tempC)

# programa principal
try:
    tipoConversao = int(input('Digite 1 para C->F e 2 para F->C: '))
    
    if tipoConversao == 1:
        tempC = float(input('Quantos graus Celsius são? '))
        tempF = celsiusToFahrenheit(tempC)
        print(f'{tempC}°C são {tempF:.2f}°F')

    elif tipoConversao == 2:
        tempF = float(input('Quantos graus Fahrenheit são? '))
        tempC = fahrenheitToCelsius(tempF)
        print(f'{tempF}°F são {tempC:.2f}°C')
    
    else:
        print('Por favor, digite 1 ou 2.')
        
except ValueError:
    print('Por favor, digite números válidos.')
'''

# desafio:
def converter_temperatura(valor, tipo):
    """
    Converte temperatura entre Celsius e Fahrenheit
    tipo: 1 para C->F, 2 para F->C
    """
    if tipo == 1:
        # Celsius para Fahrenheit
        resultado = (valor * 9/5) + 32
        return resultado
    elif tipo == 2:
        # Fahrenheit para Celsius
        resultado = (valor - 32) * 5/9
        return resultado
    else:
        return None  # Retorna None se o tipo for inválido

# programa principal
try:
    tipoConversao = int(input('Digite 1 para C->F e 2 para F->C: '))
    
    if tipoConversao == 1:
        tempC = float(input('Quantos graus Celsius são? '))
        resultado = converter_temperatura(tempC, tipoConversao)
        print(f'{tempC}°C são {resultado:.2f}°F')
    
    elif tipoConversao == 2:
        tempF = float(input('Quantos graus Fahrenheit são? '))
        resultado = converter_temperatura(tempF, tipoConversao)
        print(f'{tempF}°F são {resultado:.2f}°C')
    
    else:
        print('Por favor, digite 1 ou 2.')

except ValueError:
    print('Por favor, digite números válidos.')