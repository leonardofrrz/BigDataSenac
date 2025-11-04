# 3. Tentativa de Login e Senha
# Simule um sistema de login simples onde o usuário tem um número limitado de tentativas
# para digitar a senha correta.
# ● Defina um nome de usuário e uma senha corretos (ex: admin e 123456).
# ● Dê ao usuário 3 tentativas para acertar a combinação.
# ● Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando
# break para sair do loop.
# ● Se a senha estiver errada, informe o erro e diminua o número de tentativas
# restantes.
# ● Se as tentativas acabarem, imprima uma mensagem de bloqueio

tentativas=3
limite=0
usuario='admin'
senha='admin'

try:
    while tentativas > limite:
        insertUser=input('Usuario: ')
        insertPass=input('Senha: ')
        if insertUser == usuario and insertPass == senha:
                print('Sucesso')
                break
        else:
            tentativas = tentativas-1
            print(f'Incorreto. {tentativas}/3 tentativas restantes.')
        if tentativas==limite:
            print('\nBLOQUADO PELO SISTEMA!!! TENTE NOVAMENTE MAIS TARDE!!!\n')
except:
    print('Insira algo Valido.')
