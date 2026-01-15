# 2. Cadastro de Candidatos
# Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar
# candidatos menores de 18 anos.
# ● O programa deve pedir o Ano de Nascimento do candidato.
# ● Se for menor de 18, o programa deve informar que ele não pode participar e pular
# a coleta dos demais dados (telefone, email etc) para esse candidato.
# ● Se for maior de 18, o programa prossegue com o input() para os demais dados.
#
# Cadastro Seletivo de Candidatos
# Use um for loop para iterar 5 vezes. Dentro do loop, use um if/else para checar se o
# candidato é menor de 18 anos (rejeição). Crie uma lista principal: candidatos_validos = [].
# Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}).
# Adicione este Dicionário à lista: candidatos_validos.append(candidato)

import datetime
candidatos_validos = []

for i in range(5):
    try:
        print(f'\n=== Candidato {i + 1} ===')
        anoNascimento = int(input('Qual ano você nasceu?\nResposta: '))
        anoCalendario = datetime.datetime.now().year
        idade = anoCalendario - anoNascimento
        
        if idade < 18:
            print('\nCandidato menor de idade.\n')
        elif idade >= 18:
            nome = input('Digite seu nome: ')
            email = input('Digite seu E-Mail: ')
            cep = input('Digite seu CEP: ')
            candidato = {'Nome': nome,'Idade': idade, 'E-mail': email, 'Cep': cep} # fazendo um dicionario
            candidatos_validos.append(candidato) # implementando ele na lista
        
            print(f'\n--- Dados do Candidato {i + 1} ---')
            print(candidatos_validos[-1])
    except ValueError:
        print('Por favor, insira algo válido.\n')