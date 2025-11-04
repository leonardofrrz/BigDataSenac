# ==============================================================================
# DESAFIOS DE LÓGICA DE PROGRAMAÇÃO
#
# Comandos Permitidos: Variáveis, If/Else, Match/Case, For, While, Try/Except.
# 
# ==============================================================================

# DICA GERAL: Utilize try/except para proteger todas as entradas de usuário (input)!

# ------------------------------------------------------------------------------
# 1. VALIDADOR DE UM TRIÂNGULO
# TEMA PRINCIPAL: Decisão (If/elif/else)
# LÓGICA: A soma do comprimento de dois lados deve ser sempre maior que o terceiro. Isso define o que é um triângulo.
# ------------------------------------------------------------------------------
'''print("\n--- 1. VALIDADOR DE TRIÂNGULO ---")
# 1. Leia 3 lados (A, B, C)
# 2. Use IF/ELSE para verificar a condição de existência do triângulo.
# 3. Imprima se é ou não um triângulo válido.


# [ESPAÇO PARA O CÓDIGO]

lado01=input('Insira o valor do primeiro lado do triângulo: ')
lado02=input('Insira o valor do segundo lado do triângulo: ')
lado03=input('Insira o valor do terceiro lado do triângulo: ')

try:
    if (lado01 < lado02+lado03) and (lado02 < lado01+lado03) and (lado03 < lado01+lado02):
        print('É um triângulo válido.')
    elif (lado03 | lado02 | lado01) <= 0:
        print('Não é um triângulo válido.')
    else:
        print('Não é um triângulo válido.')
except ValueError:
    print('Por favor, insra um número.')
'''
# ------------------------------------------------------------------------------
# 2. ADIVINHE O NÚMERO
# TEMA PRINCIPAL: Repetição (FOR) e Decisão (BREAK)
# LÓGICA: O jogador tem um número fixo de tentativas para acertar o valor.
# ------------------------------------------------------------------------------
print("\n--- 2. ADIVINHE O NÚMERO ---")
NUMERO_SECRETO = 42
TENTATIVAS_MAX = 5
# 1. Use um laço FOR para limitar as TENTATIVAS_MAX.
# 2. Dentro do loop, leia o palpite.
# 3. Use IF/ELIF/ELSE para dar dicas (MAIOR ou MENOR).
# 4. Se acertar, use o comando 'break' e imprima sucesso.


# [ESPAÇO PARA O CÓDIGO]


'''# ------------------------------------------------------------------------------
# 3. MENU DE OPÇÕES SIMPLES
# TEMA PRINCIPAL: Decisão (MATCH/CASE)
# LÓGICA: Mapear a escolha numérica do usuário para uma ação específica.
# ------------------------------------------------------------------------------
print("\n--- 3. MENU DE OPÇÕES SIMPLES ---")
print("1 - Iniciar | 2 - Configurações | 3 - Ajuda | 4 - Sair")
# 1. Leia a escolha do usuário.
# 2. Use o comando 'match' na variável de escolha.
# 3. Implemente os 'case' 1, 2, 3 e 4.
# 4. Use o 'case _' para tratar opções inválidas.


# [ESPAÇO PARA O CÓDIGO]


# ------------------------------------------------------------------------------
# 4. CONTADOR DE VOGAIS
# TEMA PRINCIPAL: Repetição (FOR em String) e Variáveis
# LÓGICA: Percorrer cada caractere de uma string e contar quantos se encaixam na condição (ser uma vogal).
# ------------------------------------------------------------------------------
print("\n--- 4. CONTADOR DE VOGAIS ---")
# 1. Leia a palavra ou frase. Converta tudo para minúsculas (.lower()) ou maiúsculas (.upper()).
# 2. Inicialize uma variável 'contador_vogais = 0'.
# 3. Use um laço FOR: 'for letra in palavra:'.
# 4. Dentro do loop, use um IF com o operador 'or' para checar se a letra é 'a', 'e', 'i', 'o' ou 'u'.
# 5. Se for, incremente o contador.


# [ESPAÇO PARA O CÓDIGO]


# ------------------------------------------------------------------------------
# 5. LOGIN COM TENTATIVAS
# TEMA PRINCIPAL: Repetição (WHILE) e Decisão (Controle de fluxo)
# LÓGICA: Repetir a checagem de senha enquanto a condição (tentativas < max) for verdadeira.
# Aqui, você começa pedindo para o usuário criar um login e a senha; depois, testa o login.
# ------------------------------------------------------------------------------
print("\n--- 5. LOGIN COM TENTATIVAS ---")
USUARIO = None
SENHA = None
TENTATIVAS_MAX = 4
# 1. Inicialize 'tentativas_atuais' e use 'while tentativas_atuais < TENTATIVAS_MAX:'.
# 2. Dentro do WHILE, leia Usuário e Senha.
# 3. Use IF para checar se a combinação está correta. Se sim, imprima sucesso e use 'break'.
# 4. Fora do loop (ou no ELSE), cheque se o acesso foi bloqueado (se tentativas_atuais alcançou o máximo).


# [ESPAÇO PARA O CÓDIGO]


# ------------------------------------------------------------------------------
# 6. CALCULADORA SIMPLES
# TEMA PRINCIPAL: Decisão (MATCH/CASE)
# LÓGICA: Mapear o símbolo da operação (+, -, *, /) para o cálculo correto.
# ------------------------------------------------------------------------------
print("\n--- 6. CALCULADORA SIMPLES ---")
# 1. Leia o primeiro número, o símbolo da operação e o segundo número. Todos são fornecidos pelo usuário.
# 2. Use MATCH/CASE na variável do símbolo da operação.
# 3. Trate o caso de divisão por zero dentro do 'case /'.
# 4. Use o 'case _' para tratar símbolos inválidos.


# [ESPAÇO PARA O CÓDIGO]


# ------------------------------------------------------------------------------
# 7. CONTAGEM REGRESSIVA
# TEMA PRINCIPAL: Repetição (WHILE) com Decremento
# LÓGICA: Iniciar um contador em N e subtrair 1 a cada repetição até chegar em 1.
# ------------------------------------------------------------------------------
print("\n--- 7. CONTAGEM REGRESSIVA ---")
# 1. Leia o número inicial (N).
# 2. Use um laço WHILE com a condição 'while contador >= 1:'.
# 3. Dentro do loop, imprima o valor e use o decremento 'contador = contador - 1'.


# [ESPAÇO PARA O CÓDIGO]


# ------------------------------------------------------------------------------
# 8. CÁLCULO DE UM FATORIAL
# TEMA PRINCIPAL: Repetição (FOR) e Variável (Multiplicação)
# LÓGICA: Acumular a multiplicação dos números de 1 até N.
# ------------------------------------------------------------------------------
print("\n--- 8. CÁLCULO DE FATORIAL ---")
# 1. Leia o número N.
# 2. Inicialize a variável 'resultado_fatorial = 1'. Essa será sua variável acumuladora.
# 3. Use um laço FOR que percorra os números de 1 até N.
# 4. Dentro do loop, atualize a acumuladora: 'resultado_fatorial = resultado_fatorial * i'.
# 5. Use IF/ELSE para tratar N=0 e N negativo.


# [ESPAÇO PARA O CÓDIGO]


# ------------------------------------------------------------------------------
# 9. SISTEMA DE REPETIÇÃO FORÇADA
# TEMA PRINCIPAL: Simulação DO-WHILE (WHILE TRUE e BREAK)
# LÓGICA: Garantir que a ação (pedir input) ocorra pelo menos uma vez, e só parar se a condição de saída for atendida.
# ------------------------------------------------------------------------------
print("\n--- 9. SIMULAÇÃO DO-WHILE ---")
# 1. Crie um loop infinito: 'while True:'.
# 2. Dentro do loop, peça a entrada (input). Ou seja, deixe o usuário responder QUALQUER coisa.
# 3. Use um IF para verificar se a entrada é válida (se não está VAZIA: 'if entrada != "":').
# 4. Se for válida, use o comando 'break' para sair do loop.


# [ESPAÇO PARA O CÓDIGO]


# ------------------------------------------------------------------------------
# 10. VALIDAR CATEGORIA POR IDADE
# TEMA PRINCIPAL: Decisão (IF/ELIF/ELSE) com cálculo
# LÓGICA: Calcular a idade e classificá-la em faixas etárias usando IF/ELIF/ELSE.
# ------------------------------------------------------------------------------
print("\n--- 10. VALIDAR CATEGORIA POR IDADE ---")
ANO_ATUAL = 2025 # Use este valor para o cálculo
# 1. Leia o ano de nascimento.
# 2. Calcule a idade.
# 3. Use IF/ELIF/ELSE para verificar as faixas: <= 12 (Criança), <= 17 (Adolescente), Adulto (outros).


# [ESPAÇO PARA O CÓDIGO]


print("\n--- FIM DOS DESAFIOS ---")'''