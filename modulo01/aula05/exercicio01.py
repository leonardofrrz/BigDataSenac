# 1. Cálculo de Média Escolar para Vários Alunos
# Use o laço for para repetir a lógica de cálculo de média e status
# (Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes.

for i in range(10):

    print(f'\nEstudante {i+1}.')
    nota1=float(input("\nDigite a nota da 1ª avaliação: "))
    nota2=float(input("Digite a nota da 2ª avaliação: "))
    nota_optativa=float(input("Digite a nota da avaliação optativa (-1 se não fez): "))

    print(f'\nSituação do estudante {i+1}.')
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