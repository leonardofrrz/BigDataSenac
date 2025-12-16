# Tansformando tsv/csv em parquet com POLARS

import polars as pl
import os

# --- 1. Configuração ---
BASE_PATH = r"C:/Users/leonardo.ferraz/Documents/Leonardo Ferraz/BigDataSenac/projetofinal"

FILES = [
    "title.basics.tsv",
    "title.ratings.tsv",
    "title.principals.tsv",
    "name.basics.tsv",
    "title.crew.tsv",
    "title.episode.tsv",
    "title.akas.tsv"
]

# --- 2. Loop por arquivo ---
for file_name in FILES:
    arquivo_tsv = os.path.join(BASE_PATH, file_name)
    arquivo_parquet = os.path.join(BASE_PATH, file_name.replace(".tsv", "_POLARS.parquet"))

    if not os.path.exists(arquivo_tsv):
        print(f"Arquivo não encontrado: {arquivo_tsv}. Pulando...")
        continue

    print(f"\nConvertendo {arquivo_tsv} para {arquivo_parquet}...")

    try:
        # --- 3. Criar LazyFrame com tolerância a erros ---
        lazy_df = pl.scan_csv(
            arquivo_tsv,
            separator="\t",
            null_values="\\N",
            encoding="utf8-lossy",
            quote_char=None,        # ignora aspas internas problemáticas
            ignore_errors=True      # pula linhas com problemas de parsing
        )

        # --- 4. Salvar como Parquet ---
        lazy_df.sink_parquet(
            arquivo_parquet,
            compression="snappy"
        )

        print(f"Arquivo convertido com sucesso: {arquivo_parquet}")

    except Exception as e:
        print(f"Erro durante a conversão do arquivo {file_name}: {e}")


# 1️⃣ O que é um LazyFrame?

# Um LazyFrame é uma representação preguiçosa de um dataframe.
# Diferente de um DataFrame normal, que carrega e processa os dados imediatamente, o LazyFrame só guarda as instruções que você quer aplicar nos dados.
# Nenhum dado é realmente carregado ou processado até que você execute uma ação de “sink” ou “collect”.
# Em outras palavras: você descreve o que quer fazer, e só no final o Polars executa tudo de uma vez, de forma otimizada.

# 2️⃣ Diferença entre DataFrame e LazyFrame

# Recurso	DataFrame	LazyFrame
# Carregamento	        Imediato	  Preguiçoso (adiado)
# Execução de operações	Imediata	  Executada somente no final
# Otimização	        Limitada	  Polars reorganiza e otimiza
# Uso típico	   Pequenos datasets, testes    Grandes datasets, ETL, pipelines

# 3️⃣ Exemplo simples

# import polars as pl

# # LazyFrame: apenas descreve operações, nada é carregado ainda
# lf = pl.scan_csv("title.basics.tsv", separator="\t", null_values="\\N")

# # Adiciona uma operação de filtro
# lf = lf.filter(pl.col("startYear") > 2000)

# # Adiciona uma operação de seleção de colunas
# lf = lf.select(["tconst", "primaryTitle", "startYear"])

# # Nessa etapa, ainda não foi feito nada no arquivo real
# # Polars só armazenou as instruções

# # Só aqui os dados são carregados e processados de verdade
# df = lf.collect()  # df é um DataFrame normal agora
# print(df.head())

# 4️⃣ Por que usar LazyFrame?

# Eficiência em grandes arquivos: Polars consegue otimizar múltiplas operações de uma vez (filtragem, agregações, joins) sem precisar passar pelos dados várias vezes.
# Menos memória: como os dados só são carregados quando necessário, você não precisa armazenar tudo na memória imediatamente.
# Bom para ETL: se você tiver pipelines de transformação de dados complexos, LazyFrame permite que tudo seja planejado antes de executar.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1️⃣ collect()

# O que faz:
# Executa todas as operações que você definiu no LazyFrame e retorna um DataFrame normal (eager) com os resultados.

# Até você chamar collect(), nenhuma leitura ou cálculo real ocorre.

# Exemplo:

# import polars as pl

# # LazyFrame: carregamento preguiçoso
# lf = pl.scan_csv("title.basics.tsv", sep="\t", null_values="\\N")

# # Adicionando algumas operações
# lf = lf.filter(pl.col("startYear") > 2000).select(["tconst", "primaryTitle", "startYear"])

# # Nada foi processado ainda
# print(type(lf))  # <class 'polars.internals.lazyframe.LazyFrame'>

# # Aqui sim: os dados são processados e retornados
# df = lf.collect()
# print(df.head())
# print(type(df))  # <class 'polars.internals.dataframe.DataFrame'>


# ✅ collect() = executar tudo e retornar os dados reais.

# 2️⃣ explain()

# O que faz:
# Mostra o plano de execução interno do LazyFrame, ou seja, como o Polars pretende executar suas operações.

# Muito útil para debug, otimização e entender como Polars reordena operações.

# Não carrega os dados reais, apenas mostra a lógica.

# Exemplo:

# # Exibe o plano lógico e físico
# lf.explain()


# Saída típica (simplificada):

# Logical Plan:
#   Scan CSV: title.basics.tsv
#   Filter: startYear > 2000
#   Projection: ["tconst", "primaryTitle", "startYear"]

# Physical Plan:
#   CSV Scan (optimized)
#   Filter pushdown applied
#   Projection pushdown applied


# 💡 Aqui você vê que:

# O Polars otimiza a leitura, aplicando filtros e projeções antes de carregar os dados.

# Para arquivos grandes, isso economiza muita memória e tempo.

# 3️⃣ Fluxo resumido

# Criação do LazyFrame → define o pipeline preguiçosamente

# Definição de transformações → filtros, seleções, joins, agregações

# explain() → ver como o Polars vai executar tudo

# collect() → realmente executa o pipeline e retorna o DataFrame

# 💡 Dica prática:

# Se você estiver processando arquivos gigantes (como os da IMDb), use scan_csv() + LazyFrame,
#  defina todos os filtros e seleções, rode explain() para conferir o plano e só depois chame collect() ou sink_parquet(). Isso garante máxima eficiência