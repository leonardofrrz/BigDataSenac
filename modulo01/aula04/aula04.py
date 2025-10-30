# diaDaSemana= int(input('\nQual dia da semana você quer saber? '))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# if diaDaSemana==1:
#     print('Domingo')
# elif diaDaSemana==2:
#     print('Segunda')                            /-----------------------\
# elif diaDaSemana==3:                            |  Maneira mais longa   |
#     print('Terça')                              |  e massante de fazer. |
# elif diaDaSemana==4:                            \-----------------------/
#     print('Quarta')
# elif diaDaSemana==5:
#     print('Quinta')
# elif diaDaSemana==6:
#     print('Sexta')
# elif diaDaSemana==7:
#     print('Sabado')
# else:
#     print('Número invalido')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
try: # no try/except É PRECISO INICIAR O PENSAMENTO JÁ DENTRO DELE. ex.: declarar a variavel dentro e não fora. (mas não é muito usado, só usamos de exemplo.)
    diaDaSemana= int(input('\nQual dia da semana você quer saber? '))

    match diaDaSemana:
        case 1:
            print('Domingo')
        case 2:
            print('Segunda')
        case 3:
            print('Terça')
        case 4:
            print('Quarta')
        case 5:
            print('Quinta')
        case 6:
            print('Sexta')
        case 7:
            print('Sabado')
        case _: #funciona parecido com o else, sendo ativado se nenhum caso for encontrado no match.
            print('Por favor, informe um número de 1 á 7.')
except ValueError: # prestar atenção no tipo de erro que o terminal pede. Nesse caso era ValueError, então usei ele, mas podem ser outros erros.
    print('Por favor, informe um número inteiro.')

# o match/case funciona de maneira diferente do if/elif/else...
# o match/case procura exatamente o valor pedido. ex.: pediu o número 2, ele vai direto no caso 2(segunda).
# já o if/elif/else compara o primeiro, dps o segundo, dps o terceiro.... até achar o valor. Se ele não achar, cai no else. (SE e SENÃO).
# em suma, Quantidade: match/case. Qualidade:if/elif/else.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------