import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo completo:
df_movies_metadata = pd.read_csv('BigDataSenac/modulo02/analiseDataImdb/movie_metadata.csv')

# Extrair a coluna de preços e remover NaN:
num_critic_for_reviews_array = df_movies_metadata['num_critic_for_reviews'].dropna().values
serie_num_reviews = pd.Series(num_critic_for_reviews_array)

# Exibir os primeiros dados carregados para confirmação:
print("DataFrame Carregado (Primeiros 5):")
print(df_movies_metadata.head())
print("\nArray de Número de Reviews Carregado (Primeiros 5):")
print(num_critic_for_reviews_array[:5])

# Calcular Q1 e Q3
Q1 = np.percentile(num_critic_for_reviews_array, 25)
Q3 = np.percentile(num_critic_for_reviews_array, 75)

# Calcular IQR
IQR = Q3 - Q1

# Calcular Limites
limite_superior = Q3 + (1.5 * IQR)
limite_inferior = Q1 - (1.5 * IQR)

print(f"\n--- Limites de Outliers (Nome e número de reviews) ---")
print(f"Q1 (25%): {Q1:.2f}")
print(f"Q3 (75%): {Q3:.2f}")
print(f"IQR: {IQR:.2f}")
print(f"Limite Superior (LS): {limite_superior:.2f}")
print(f"Limite Inferior (LI): {limite_inferior:.2f}")

# Identificação de Outliers Superiores e Inferiores
outliers_superiores = df_movies_metadata[df_movies_metadata['num_critic_for_reviews'] > limite_superior]
outliers_inferiores = df_movies_metadata[df_movies_metadata['num_critic_for_reviews'] < limite_inferior]

print("Qtd outliers inferiores:", len(outliers_inferiores))
print("Qtd outliers superiores:", len(outliers_superiores))

# Exibir Outliers Superiores Ordenados (Decrescente)
print(f"\n--- Outliers Superiores ({len(outliers_superiores)} reviews) ---")
print(outliers_superiores[['movie_title', 'num_critic_for_reviews']].sort_values(by='num_critic_for_reviews', ascending=False))

# Exibir Outliers Inferiores Ordenados (Crescente)
print(f"\n--- Outliers Inferiores ({len(outliers_inferiores)} reviews) ---")
print(outliers_inferiores[['movie_title', 'num_critic_for_reviews']].sort_values(by='num_critic_for_reviews', ascending=True))

# Garante que os DataFrames de outliers não estão vazios antes de plotar
if not outliers_inferiores.empty or not outliers_superiores.empty:
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))  # 1 linha, 2 colunas
    
    # 1ª Posição: Outliers Inferiores (Crescente)
    if not outliers_inferiores.empty:
        outliers_inferiores_plot = outliers_inferiores.sort_values(by='num_critic_for_reviews', ascending=True).head(999)
        axes[0].bar(range(len(outliers_inferiores_plot)), outliers_inferiores_plot['num_critic_for_reviews'])
        axes[0].axhline(y=limite_superior, color='red', linestyle='--', linewidth=2, label=f'Limite Superior: {limite_superior:.2f}')
        axes[0].set_xticks(range(len(outliers_inferiores_plot)))
        axes[0].set_xticklabels(outliers_inferiores_plot['movie_title'], rotation=90, ha='right', fontsize=9)
        axes[0].set_title('Outliers Inferiores (Menor Número de Reviews)')
        axes[0].set_ylabel('Número de Reviews')
        axes[0].grid(axis='y', linestyle='--')
    
    # 2ª Posição: Outliers Superiores (Decrescente)
    if not outliers_superiores.empty:
        outliers_superiores_plot = outliers_superiores.sort_values(by='num_critic_for_reviews', ascending=False).head(999)
        axes[1].bar(range(len(outliers_superiores_plot)), outliers_superiores_plot['num_critic_for_reviews'])
        axes[1].axhline(y=limite_superior, color='red', linestyle='--', linewidth=2, label=f'Limite Superior: {limite_superior:.2f}')
        axes[1].set_xticks(range(len(outliers_superiores_plot)))
        axes[1].set_xticklabels(outliers_superiores_plot['movie_title'], rotation=90, ha='right', fontsize=9)
        axes[1].set_title('Outliers Superiores (Maior Número de Reviews)')
        axes[1].set_ylabel('Número de Reviews')
        axes[1].grid(axis='y', linestyle='--')
    
    plt.tight_layout()
    plt.show()

else:
    print("\nNão houve outliers superiores ou inferiores para plotar.")