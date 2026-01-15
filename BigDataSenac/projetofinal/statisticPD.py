import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

# ==============================================================================
# 1. FUNÇÃO DE CÁLCULO
# ==============================================================================

def calcular_medidas_descritivas(dados_array):
    """
    Calcula e retorna um dicionário com as principais medidas estatísticas
    de tendência central, posição e dispersão para um array NumPy.
    """
    if dados_array is None or len(dados_array) == 0:
        return None

    # Medidas de Tendência Central
    media = np.mean(dados_array)
    mediana = np.median(dados_array)

    # Medidas de Posição (Quartis e IQR)
    Q1 = np.percentile(dados_array, 25)
    Q3 = np.percentile(dados_array, 75)
    IQR = Q3 - Q1

    # Limites de Outliers
    limite_superior = Q3 + (1.5 * IQR)
    limite_inferior = Q1 - (1.5 * IQR)

    # Valores Extremos
    min_valor = np.min(dados_array)
    max_valor = np.max(dados_array)

    return {
        'media': media,
        'mediana': mediana,
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'limite_superior': limite_superior,
        'limite_inferior': limite_inferior,
        'min_valor': min_valor,
        'max_valor': max_valor,
    }

# ==============================================================================
# 2. FUNÇÃO DE VISUALIZAÇÃO
# ==============================================================================

def gerar_painel_boxplot(dados_array, medidas, titulo_boxplot='Boxplot da Distribuição de Dados', caminho_salvar=None):
    """
    Gera e exibe um painel com um Boxplot e um resumo das medidas estatísticas.
    
    Args:
        dados_array (np.ndarray): O array NumPy com os dados.
        medidas (dict): O dicionário retornado por calcular_medidas_descritivas().
        titulo_boxplot (str): Título para o boxplot.
        caminho_salvar (str, optional): Caminho para salvar a imagem.
    """
    if medidas is None:
        print("Erro: Medidas estatísticas não fornecidas ou inválidas.")
        return

    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    # --- POSIÇÃO 1: BOXPLOT ---
    sns.boxplot(y=dados_array, ax=axes[0])
    axes[0].set_title(titulo_boxplot)
    axes[0].set_ylabel(dados_array.name if hasattr(dados_array, 'name') else 'Valores')

    # --- POSIÇÃO 2: CENÁRIO DE MEDIDAS (plt.text) ---
    axes[1].axis('off')
    axes[1].set_title('Medidas Estatísticas Calculadas')

    # Preparando o texto formatado (usando as chaves do dicionário 'medidas')
    resumo = (
        f"Medidas de Tendência Central:\n"
        f"  Média: R$ {medidas['media']:.2f}\n"
        f"  Mediana (Q2): R$ {medidas['mediana']:.2f}\n"
        f"\n"
        f"Medidas de Posição/Dispersão:\n"
        f"  Q1: R$ {medidas['Q1']:.2f}\n"
        f"  Q3: R$ {medidas['Q3']:.2f}\n"
        f"  IQR: R$ {medidas['IQR']:.2f}\n"
        f"\n"
        f"Limites e Extremos:\n"
        f"  Limite Superior (LS): R$ {medidas['limite_superior']:.2f}\n"
        f"  Limite Inferior (LI): R$ {medidas['limite_inferior']:.2f}\n"
        f"  Valor Máximo: R$ {medidas['max_valor']:.2f}\n"
        f"  Valor Mínimo: R$ {medidas['min_valor']:.2f}\n"
    )

    # Adicionando o texto
    axes[1].text(0.1, 0.95, resumo,
                 transform=axes[1].transAxes,
                 fontsize=12,
                 verticalalignment='top',
                 bbox=dict(boxstyle="round,pad=0.5", alpha=0.1, color='lightgray'))

    plt.tight_layout()
    
    if caminho_salvar:
        plt.savefig(caminho_salvar)
        print(f"Painel salvo em: {caminho_salvar}")
    
    plt.show()

############################################

# Conjunto de dados
dados = [2, 4, 6, 8, 10]

# Passo 1: Calcular a média
media = sum(dados) / len(dados)
print(f"Dados: {dados}")
print(f"Média: {media}")

print("-" * 100)
# Passo 2: Calcular as diferenças entre cada valor e a média
diferencas = [x - media for x in dados]
print(f"Diferenças em relação à média: {diferencas}")

# Passo 3: Elevar as diferenças ao quadrado
quadrados_diferencas = [x ** 2 for x in diferencas]
print(f"Quadrados das diferenças: {quadrados_diferencas}")

# Passo 4: Calcular a média dos quadrados das diferenças
variancia = sum(quadrados_diferencas) / len(quadrados_diferencas)
print(f"Variância: {variancia:.2f}")

# Passo 5: Calcular a raiz quadrada da variância
desvio_padrao = math.sqrt(variancia)
print(f"Desvio Padrão: {desvio_padrao:.2f}")

print("-" * 100)

dados_serie = pd.Series([2, 4, 6, 8, 10])

print("--- Usando Pandas e NumPy ---")
print(f"\nMédia (usando Pandas .mean()): {dados_serie.mean():.2f}")

# NumPy por padrão usa N no denominador (população)
print(f"Variância (usando NumPy np.var()): {np.var(dados_serie):.2f}")

# Pandas por padrão usa N-1 (amostra), mas podemos forçar o cálculo da população:
# print(f"- Variância (usando Pandas .var(ddof=0)): {dados_serie.var(ddof=0):.2f}")

# NumPy por padrão usa N no denominador (população)
print(f"Desvio Padrão (usando NumPy np.std()): {np.std(dados_serie):.2f}")

# Pandas por padrão usa N-1 (amostra)
print(f"Desvio Padrão (usando Pandas .std(ddof=0)): {dados_serie.std(ddof=0):.2f}")

print("-" * 100)

# Coeficiente de Variação (CV)
cv = (desvio_padrao / media) * 100
print(f"Coeficiente de Variação (CV): {cv:.2f}%")

# Distância da Variância em relação à Média
distancia = variancia / (media ** 2)
print(f"Distância da Variância em relação à Média: {distancia:.2f}")

# Análise de Dispersão
if distancia <= 0.10:
    analise = "Baixa dispersão dos dados em relação à média."
elif distancia < 0.25:
    analise = "Dispersão moderada dos dados em relação à média."
else:
    analise = "Alta dispersão dos dados em relação à média."
    
print(f"Análise de Dispersão: {analise}")

print("-" * 100)

###################################################################

# Carregar o DataFrame
pedidos_df = pd.read_csv("../Aula04/vendas_pedidos.csv")

# Selecionar os dados de interesse
dados_valor_total = pedidos_df['valor_total']

# Cálculo das medidas
media_vendas = dados_valor_total.mean()
# Usando np.var com ddof=0 para calcular a variância populacional
variancia_vendas = np.var(dados_valor_total, ddof=0)
# Usando np.std com ddof=0 para calcular o desvio padrão populacional
desvio_padrao_vendas = np.std(dados_valor_total, ddof=0)

# Coeficiente de Variação (CV)
cv_vendas = (desvio_padrao_vendas / media_vendas) * 100

# Distância da Variância em relação à Média
distancia_vendas = variancia_vendas / (media_vendas ** 2)

print(f"--- Análise dos Valores Totais dos Pedidos ---")
print(f"\nMédia dos Valores Totais: R$ {media_vendas:.2f}")
print(f"Variância dos Valores Totais: {variancia_vendas:.2f}")
print(f"Desvio Padrão dos Valores Totais: R$ {desvio_padrao_vendas:.2f}")
print("-" * 100)
print(f"Coeficiente de Variação (CV): {cv_vendas:.2f}%")
print(f"Distância da Variância / Média²: {distancia_vendas:.2f}")

# Análise de Dispersão
if distancia_vendas <= 0.10:
    analise_vendas = "Baixa dispersão dos dados em relação à média."
elif distancia_vendas < 0.25:
    analise_vendas = "Dispersão moderada dos dados em relação à média."
else:
    analise_vendas = "Alta dispersão dos dados em relação à média."
    
print(f"Conclusão da Dispersão: {analise_vendas}")

##############################################################

### ASSIMETRIA ###

# Carregar o DataFrame
pedidos_df = pd.read_csv("../Aula04/vendas_pedidos.csv")
dados_valor_total = pedidos_df['valor_total']

# 1. Calcular Assimetria
assimetria = dados_valor_total.skew()
print(f"Assimetria dos Valores Totais: {assimetria:.4f}")

# 2. Relembrar Média e Mediana para contextualizar
media = dados_valor_total.mean()
mediana = dados_valor_total.median()
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")

# 3. Análise da Assimetria
if assimetria >= -0.5 and assimetria <= 0.5:
    analise_assimetria = "Simétrica (ou Quase Simétrica). Média e Mediana são próximas."
elif assimetria > 0.5:
    analise_assimetria = "Positiva. A cauda se estende para a direita (valores maiores). Média > Mediana."
else:
    analise_assimetria = "Negativa. A cauda se estende para a esquerda (valores menores). Média < Mediana."

print(f"\nConclusão da Assimetria: {analise_assimetria}")

### CURTOSE ###

# 1. Calcular Curtose
curtose_excesso = dados_valor_total.kurtosis()

# 2. Calcular a Curtose Real
curtose_real = curtose_excesso + 3
print(f"Curtose em Excesso (Pandas): {curtose_excesso:.4f}")
print(f"Curtose Real (Referência 3.0): {curtose_real:.4f}")

# 3. Análise da Curtose
if curtose_real >= 2.5 and curtose_real <= 3.5:
    analise_curtose = "Mesocúrtica. Distribuição próxima da normal (dados uniformes no entorno da média)."
elif curtose_real < 2.5:
    analise_curtose = "Platicúrtica. Dados mais dispersos em relação à média. Caudas finas e Outliers comuns."
else: # curtose_real > 3.5
    analise_curtose = "Leptocúrtica. Dados extremamente concentrados no centro e caudas pesadas. Outliers muito comuns."

print(f"\nConclusão da Curtose: {analise_curtose}")

# 1. Carregar os dados de produtos
produtos_df = pd.read_csv("../Aula03/vendas_produtos.csv")
dados_preco = produtos_df['preco']

# 2. Calcular Medidas
media_preco = dados_preco.mean()
mediana_preco = dados_preco.median()
std_preco = dados_preco.std(ddof=0) # Desvio padrão populacional

assimetria_preco = dados_preco.skew()
curtose_excesso_preco = dados_preco.kurtosis()
curtose_real_preco = curtose_excesso_preco + 3 # Para a nossa referência de 3.0

# 3. Painel de Resultados

print("-" * 50)
print("PAINEL: DISTRIBUIÇÃO DOS PREÇOS DOS PRODUTOS")
print("-" * 50)
print(f"Média do Preço: R$ {media_preco:.2f}")
print(f"Mediana do Preço: R$ {mediana_preco:.2f}")
print(f"Desvio Padrão: R$ {std_preco:.2f}")
print("-" * 50)
print(f"Assimetria: {assimetria_preco:.4f}")
# Interpretação da Assimetria
if assimetria_preco > 0.5:
    print(" -> Assimétrica Positiva (Cauda à Direita). Média > Mediana. Produtos mais caros 'puxam' a cauda.")
elif assimetria_preco < -0.5:
    print(" -> Assimétrica Negativa (Cauda à Esquerda). Média < Mediana. Produtos mais baratos 'puxam' a cauda.")
else:
    print(" -> Simétrica. Média ≈ Mediana. Distribuição equilibrada.")

print(f"Curtose (Real, Ref. 3.0): {curtose_real_preco:.4f}")
# Interpretação da Curtose
if curtose_real_preco > 3.5:
    print(" -> Leptocúrtica. Pico alto e caudas pesadas. Preços extremamente concentrados no centro (muitos outliers de preço).")
elif curtose_real_preco < 2.5:
    print(" -> Platicúrtica. Pico baixo. Preços mais dispersos em relação à média.")
else:
    print(" -> Mesocúrtica. Próximo à Normal. Distribuição uniforme dos preços.")
print("-" * 50)

# 4. Geração do Boxplot para visualização de Outliers
plt.figure(figsize=(8, 4))
sns.boxplot(x=dados_preco)
plt.title('Boxplot da Distribuição dos Preços dos Produtos')
plt.xlabel('Preço (R$)')
plt.show()

# 5. Geração do Histograma com KDE
plt.figure(figsize=(10, 6))
sns.histplot(dados_preco, kde=True, bins=30, color='skyblue', edgecolor='black', stat='density')

# Adicionar a Média e Mediana para referência
plt.axvline(media_preco, color='red', linestyle='--', label=f'Média: {media_preco:.2f}')
plt.axvline(mediana_preco, color='green', linestyle=':', label=f'Mediana: {mediana_preco:.2f}')

# Adicionar textos para Assimetria e Curtose (apenas para referência visual, não desenha uma linha específica)
plt.text(0.95, 0.95, f'Assimetria: {assimetria_preco:.2f}', transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5))
plt.text(0.95, 0.88, f'Curtose (Real): {curtose_real_preco:.2f}', transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round,pad=0.5', fc='lightgreen', alpha=0.5))

plt.title('Distribuição dos Preços dos Produtos (Histograma com KDE)', fontsize=14)
plt.xlabel('Preço (R$)', fontsize=12)
plt.ylabel('Densidade', fontsize=12)
plt.legend()
plt.grid(axis='y', alpha=0.75)
plt.show()