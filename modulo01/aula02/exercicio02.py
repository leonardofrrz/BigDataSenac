'''
nota01= 1
nota02= 10
nota03= 10
nota04= 10
'''
nota01=float(input('Digite sua nota do primeiro bimestre: '))
nota02=float(input('Digite sua nota do segundo bimestre: '))
nota03=float(input('Digite sua nota do terceiro bimestre: '))
nota04=float(input('Digite sua nota do quarto bimestre: '))
media=(nota01+nota02+nota03+nota04)/4

if media<5:
    print('REPROVAÇÃO: Média estritamente abaixo de 5!')
elif media>7:
    print('APROVADO: Média estritamente maior que 7.')
else:
    print('RECUPERAÇÃO: Média entre 5 e 7.')