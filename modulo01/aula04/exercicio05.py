# 5. Média do Aluno com Optativa:
# Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
# optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
# ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
# substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
# mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
# recuperação, de acordo com as informações abaixo:
# Aprovado: média >= 6.0
# Reprovado: média < 3.0
# Recuperação: média >= 3.0 e < 6.0
# Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o
# resultado final

nota1=float(input("Digite a nota da 1ª avaliação: "))
nota2=float(input("Digite a nota da 2ª avaliação: "))
nota_optativa=float(input("Digite a nota da avaliação optativa (-1 se não fez): "))

if nota_optativa== -1:
    media = (nota1 + nota2) / 2
    print(f"\nO aluno não realizou a prova optativa.")
else:
    nota_menor = min(nota1, nota2)
    nota_maior = max(nota1, nota2)
    media = (nota_maior + nota_optativa) / 2 
    print(f"\nA nota optativa ({nota_optativa:.1f}) substituiu a menor nota ({nota_menor:.1f}).")

print(f"Média final: {media:.2f}")
print("\n--- SITUAÇÃO DO ALUNO ---")
if media>=6.0:
    print("Status: APROVADO!")
elif media>=3.0:
    print("Status: EM RECUPERAÇÃO")
else:
    print("Status: REPROVADO")