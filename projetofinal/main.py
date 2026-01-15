import pandas as pd
import mysql.connector

######################

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="test"
        )
        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

# Usando a função

##########Filtrando fimes por genero e ordenando por nota############

query_01 = """
SELECT
    movies.title,
    movies.title_year,
    movies.imdb_score,
    movies.duration
FROM test.movies
JOIN movie_genres ON movies.movie_id = movie_genres.movie_id
JOIN genres ON movie_genres.genre_id = genres.genre_id
WHERE genres.name = 'Drama'
ORDER BY movies.imdb_score DESC
LIMIT 10;
"""
dados_filtrados = obter_dados_do_banco(query_01)
if dados_filtrados:
    print('\nResultado da Query 1\n')
    for results in dados_filtrados:
        print(results)

#########Filtrando filmes por idioma e ordenando por ordem alfabetica#############

query_02 = """
SELECT 
    title,
    title_year,
    imdb_score
FROM movies
WHERE language_id IN (
    SELECT language_id 
    FROM languages 
    WHERE name IN ('English', 'Spanish', 'French')
)
ORDER BY title ASC
LIMIT 10;
"""
dados_filtrados = obter_dados_do_banco(query_02)
if dados_filtrados:
    print('\nResultado da Query 2\n')
    for results in dados_filtrados:
        print(results)

##########Filtrando filmes que tem duracao definida(IS NOT NULL) e ordenando por maior duracao############

query_03 = """
SELECT 
    title AS nome_do_filme,
    duration AS duracao_em_minutos,
    title_year AS ano_de_lancamento
FROM movies
WHERE duration IS NOT NULL
ORDER BY duration DESC
LIMIT 10;
"""
dados_filtrados = obter_dados_do_banco(query_03)
if dados_filtrados:
    print('\nResultado da Query 3\n')
    for results in dados_filtrados:
        print(results)

##########Filtrando filmes que deram lucro e ordenando por percentual de lucro############

query_04 = """
SELECT 
    title AS filme,
    budget AS orcamento,
    gross AS receita,
    (gross - budget) AS lucro,
    ROUND(((gross - budget) / budget) * 100, 2) AS percentual_lucro -- round é usado igual um :.2f do pyton pra selecionar o número de casas decimais que quer
FROM movies
WHERE budget > 0 
  AND gross > 0
  AND gross > budget
ORDER BY percentual_lucro DESC
LIMIT 15;
"""
dados_filtrados = obter_dados_do_banco(query_04)
if dados_filtrados:
    print('\nResultado da Query 4\n')
    for results in dados_filtrados:
        print(results)

##########Filtrando filmes por diretor e ordenando por nota############

query_05 = """
SELECT
	title AS filme,
    title_year AS ano,
    imdb_score AS nota
FROM movies
JOIN people ON movies.director_id = people.person_id
WHERE people.name = 'James Cameron'
ORDER BY movies.imdb_score DESC
LIMIT 10;
"""
dados_filtrados = obter_dados_do_banco(query_05)
if dados_filtrados:
    print('\nResultado da Query 5\n')
    for results in dados_filtrados:
        print(results)

##########Filtrando fimes por cor e ordenando por nota############

query_06 = """
SELECT 
    title AS filme,
    imdb_score AS nota,
    title_year AS ano_de_lancamento
FROM movies
WHERE color = 'Black and White'
ORDER BY imdb_score DESC
LIMIT 10;
"""
dados_filtrados = obter_dados_do_banco(query_06)
if dados_filtrados:
    print('\nResultado da Query 6\n')
    for results in dados_filtrados:
        print(results)