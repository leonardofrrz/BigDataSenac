# 2. Cadastro de Candidatos
# Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar
# candidatos menores de 18 anos.
# ● O programa deve pedir o Ano de Nascimento do candidato.
# ● Se for menor de 18, o programa deve informar que ele não pode participar e pular
# a coleta dos demais dados (telefone, email etc) para esse candidato.
# ● Se for maior de 18, o programa prossegue com o input() para os demais dados.


contador = 0
limite = 12

while contador < limite:
    try:
        print(f'\n=== Candidato {contador + 1} ===')
        anoNascimento = int(input('Qual ano você nasceu?\nResposta: '))
        anoCalendario = 2025
        idade = anoCalendario - anoNascimento
        
        if idade < 18:
            print('\nCandidato menor de idade.\n')
            contador = contador+1
            continue
        
        nome = str(input('Digite seu nome: '))
        email = input('Digite seu E-Mail: ')
        telefone = int(input('Digite seu telefone(ex.:DDD123456789): '))
        cep = input('Digite seu CEP: ')
        
        print(f'\n--- Dados do Candidato {contador + 1} ---')
        print(f'Idade: {idade}')
        print(f'Nome: {nome}')
        print(f'E-mail: {email}')
        print(f'Telefone: {telefone}')
        print(f'CEP: {cep}\n')
        
        contador = contador + 1
        
    except ValueError:
        print('Por favor, insira algo válido.\n')