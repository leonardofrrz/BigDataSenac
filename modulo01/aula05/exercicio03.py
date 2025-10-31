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

contador=3
limite=0
usuario='admin'
senha='admin'

try:
    while contador > limite:
        insertUser=input('Usuario: ')
        if insertUser == usuario:
            insertPass=input('Senha: ')
            if insertPass == senha:
                print('Sucesso')
                break
            else:
                contador = contador-1
                print(f'Senha incorreta. {contador}/3 tentativas restantes.')
        else:
            contador = contador-1
            print(f'Usuario incorreto. {contador}/3 tentativas restantes.')
            if contador==limite:
                print('\nBLOQUADO PELO SISTEMA!!! TENTE NOVAMENTE MAIS TARDE!!!\n')
except:
    print('Insira algo Valido.')