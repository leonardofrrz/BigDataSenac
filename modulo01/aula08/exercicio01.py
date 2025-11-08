# 1. Controle de Pesca
# Crie um programa que ajude um pescador a controlar sua produtividade. Toda vez que ele
# traz um peso de peixes maior que o estabelecido pelo regulamento (100 quilos), ele deve
# pagar uma multa de R$ 4,00 por quilo excedente.
# ● O programa deve ler o peso de peixes (em quilos) pescado no dia.
# ● Você deve criar uma função (ex: calcular_multa(peso_total)) que recebe o peso e
# retorna o valor da multa (que pode ser 0.0 se estiver dentro do limite).
# ● Se o valor da multa retornado for maior que zero, mostre a multa.
# ● Caso contrário, mostre a mensagem "Peso dentro do limite. Nenhuma multa a
# pagar."
# ● Pergunte o peso de várias pescarias feitas ao longo da semana. O loop para quando
# o usuário digitar 0. Ao final, mostre o total de multa acumulado no dia.

def calcular_multa(pesoTotal):
    """
    Calcula a multa baseada no peso de peixes pescados.
    """
    LIMITE_PESO = 100  # quilos
    VALOR_MULTA_POR_QUILO = 4.00  # reais
    
    if pesoTotal > LIMITE_PESO:
        excedente = pesoTotal - LIMITE_PESO
        multa = excedente * VALOR_MULTA_POR_QUILO
        return multa
    else:
        return 0.0


def main():
    """Função principal do programa de controle de pesca."""
    print("=" * 50)
    print("SISTEMA DE CONTROLE DE PESCA")
    print("=" * 50)
    print(f"Limite permitido: 100 kg")
    print(f"Multa por excedente: R$ 4,00/kg")
    print("=" * 50)
    print()
    
    total_multas = 0.0
    numero_pescaria = 0
    
    while True:
        try:
            peso = float(input("Digite o peso de peixes pescados (0 para sair): "))
            
            # Condição de parada
            if peso == 0:
                break
            
            # Validação de peso negativo
            if peso < 0:
                print("Erro: O peso não pode ser negativo!\n")
                continue
            
            numero_pescaria += 1
            print(f"\n--- Pescaria #{numero_pescaria} ---")
            
            # Calcula a multa
            multa = calcular_multa(peso)
            
            # Exibe o resultado
            if multa > 0:
                excedente = peso - 100
                print(f"Peso pescado: {peso:.2f} kg")
                print(f"Excedente: {excedente:.2f} kg")
                print(f"Multa a pagar: R$ {multa:.2f}")
                total_multas += multa
            else:
                print(f"Peso pescado: {peso:.2f} kg")
                print("Peso dentro do limite. Nenhuma multa a pagar.")
            
            print()
            
        except ValueError:
            print("❌ Erro: Digite um número válido!\n")
    
    # Exibe o resumo final
    print("=" * 50)
    print("RESUMO DA SEMANA")
    print("=" * 50)
    print(f"Total de pescarias registradas: {numero_pescaria}")
    print(f"Total de multas acumuladas: R$ {total_multas:.2f}")
    print("=" * 50)
    
    if total_multas > 0:
        print(f"\nVocê deve pagar R$ {total_multas:.2f} em multas.")
    else:
        print("\nParabéns! Nenhuma multa foi aplicada.")


# Executa o programa
if __name__ == "__main__":
    main()