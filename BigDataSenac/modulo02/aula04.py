import pandas as pd
from sqlalchemy import create_engine

# =====================================
# 1️⃣ CONEXÃO COM O MYSQL
# =====================================
engine = create_engine(
    "mysql+mysqlconnector://root:leonardo10@127.0.0.1:3306/meu_database"
)

print("Conexão com MySQL criada com sucesso.\n")

# =====================================
# 2️⃣ CONSULTAS SQL (ETAPA 1 - CSV)
# =====================================

# 🔹 QUERY 1 — COUNT
query_1 = """
SELECT COUNT(*) AS total_filmes
FROM movie_metadata
"""
df_q1 = pd.read_sql(query_1, engine)
print("QUERY 1 - COUNT (quantidade total de filmes):")
print(df_q1, "\n")


# 🔹 QUERY 2 — AVG
query_2 = """
SELECT AVG(imdb_score) AS media_imdb
FROM movie_metadata
"""
df_q2 = pd.read_sql(query_2, engine)
print("QUERY 2 - AVG (média das notas IMDb):")
print(df_q2, "\n")


# 🔹 QUERY 3 — GROUP BY
query_3 = """
SELECT
    title_year,
    COUNT(*) AS qtd_filmes
FROM movie_metadata
WHERE title_year IS NOT NULL
GROUP BY title_year
ORDER BY title_year DESC
LIMIT 5
"""
df_q3 = pd.read_sql(query_3, engine)
print("QUERY 3 - GROUP BY (filmes por ano):")
print(df_q3, "\n")


# 🔹 QUERY 4 — ORDER BY
query_4 = """
SELECT
    movie_title,
    imdb_score
FROM movie_metadata
ORDER BY imdb_score DESC
LIMIT 5
"""
df_q4 = pd.read_sql(query_4, engine)
print("QUERY 4 - ORDER BY (top 5 filmes por nota):")
print(df_q4, "\n")


# 🔹 QUERY 5 — WHERE
query_5 = """
SELECT
    movie_title,
    title_year,
    imdb_score
FROM movie_metadata
WHERE imdb_score >= 8
ORDER BY imdb_score DESC
LIMIT 5
"""
df_q5 = pd.read_sql(query_5, engine)
print("QUERY 5 - WHERE (filmes com nota >= 8):")
print(df_q5)
