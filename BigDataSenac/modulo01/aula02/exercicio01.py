'''
num01=1
num02=9421
num03=-31
'''

num01=int(input('Digite o primeiro número: '))
num02=int(input('Digite o segundo número: '))
num03=int(input('Digite o terceiro número: '))

if num01<num02 and num02<num03:
    print(num01, num02, num03) #123
elif num01>num02 and num01<num03:
    print(num02, num01, num03) #213
elif num01<num02 and num01>num03:
    print(num03, num01, num02) #312
elif num01<num02 and num02>num03:
    print(num01, num03, num02) #132
elif num02<num03 and num03<num01:
    print(num02, num03, num01) #231
elif num03<num02 and num02<num01:
    print(num03, num02, num01) #321
else:
    print('Por favor, escreva 3 números DIFERENTES.')