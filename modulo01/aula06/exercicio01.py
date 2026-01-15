# 1. Cálculo de Média Escolar para Vários Alunos
# Use o laço for para repetir a lógica de cálculo de média e status
# (Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes.
#
# Média Escolar para 5 Estudantes
# Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão
# (if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma
# string (ex: "Aluno 1 - Aprovado") a esta lista usando .append().

resultados = []
for i in range(5):

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
        resultados.append(f'Aluno {i+1} - Aprovado')
        print(resultados[i])
    elif media>=3.0:
        resultados.append(f'Aluno {i+1} - Recuperação')
        print(resultados[i])
    else:
        resultados.append(f'Aluno {i+1} - Reprovado')
        print(resultados[i])