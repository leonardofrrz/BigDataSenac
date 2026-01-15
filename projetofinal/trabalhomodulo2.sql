-- ============================================
-- MODELO LÓGICO - DDL COMPLETO
-- Sistema de Gerenciamento de Filmes
-- Normalizado até 3FN
-- ============================================

-- Tabela de Países
CREATE TABLE countries (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Idiomas
CREATE TABLE languages (
    language_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Pessoas (Diretores e Atores)
CREATE TABLE people (
    person_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    facebook_likes INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uk_person_name (name)
);

-- Tabela de Gêneros
CREATE TABLE genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Palavras-chave
CREATE TABLE keywords (
    keyword_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela Principal de Filmes
CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(300) NOT NULL,
    title_year INT,
    duration INT,
    color VARCHAR(20),
    imdb_link VARCHAR(500),
    imdb_score DECIMAL(3,1),
    num_voted_users INT DEFAULT 0,
    num_critic_for_reviews INT,
    num_user_for_reviews INT,
    gross BIGINT,
    budget BIGINT,
    aspect_ratio DECIMAL(4,2),
    facenumber_in_poster INT,
    movie_facebook_likes INT DEFAULT 0,
    content_rating VARCHAR(20),
    director_id INT,
    country_id INT,
    language_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_movie_director FOREIGN KEY (director_id) 
        REFERENCES people(person_id) ON DELETE SET NULL,
    CONSTRAINT fk_movie_country FOREIGN KEY (country_id) 
        REFERENCES countries(country_id) ON DELETE SET NULL,
    CONSTRAINT fk_movie_language FOREIGN KEY (language_id) 
        REFERENCES languages(language_id) ON DELETE SET NULL,
        
    CONSTRAINT chk_imdb_score CHECK (imdb_score BETWEEN 0 AND 10),
    CONSTRAINT chk_title_year CHECK (title_year >= 1888 AND title_year <= 2100),
    CONSTRAINT chk_duration CHECK (duration > 0),
    
    INDEX idx_title (title),
    INDEX idx_year (title_year),
    INDEX idx_imdb_score (imdb_score),
    INDEX idx_director (director_id)
);

-- Tabela de Relacionamento: Filme-Elenco
CREATE TABLE movie_cast (
    movie_cast_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    person_id INT NOT NULL,
    cast_order TINYINT NOT NULL,
    actor_facebook_likes INT DEFAULT 0,
    
    CONSTRAINT fk_cast_movie FOREIGN KEY (movie_id) 
        REFERENCES movies(movie_id) ON DELETE CASCADE,
    CONSTRAINT fk_cast_person FOREIGN KEY (person_id) 
        REFERENCES people(person_id) ON DELETE CASCADE,
        
    CONSTRAINT chk_cast_order CHECK (cast_order IN (1, 2, 3)),
    UNIQUE KEY uk_movie_cast_order (movie_id, cast_order),
    INDEX idx_cast_person (person_id)
);

-- Tabela de Relacionamento: Filme-Gênero
CREATE TABLE movie_genres (
    movie_genre_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    genre_id INT NOT NULL,
    
    CONSTRAINT fk_mg_movie FOREIGN KEY (movie_id) 
        REFERENCES movies(movie_id) ON DELETE CASCADE,
    CONSTRAINT fk_mg_genre FOREIGN KEY (genre_id) 
        REFERENCES genres(genre_id) ON DELETE CASCADE,
        
    UNIQUE KEY uk_movie_genre (movie_id, genre_id),
    INDEX idx_mg_genre (genre_id)
);

-- Tabela de Relacionamento: Filme-Palavra-chave
CREATE TABLE movie_keywords (
    movie_keyword_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    keyword_id INT NOT NULL,
    
    CONSTRAINT fk_mk_movie FOREIGN KEY (movie_id) 
        REFERENCES movies(movie_id) ON DELETE CASCADE,
    CONSTRAINT fk_mk_keyword FOREIGN KEY (keyword_id) 
        REFERENCES keywords(keyword_id) ON DELETE CASCADE,
        
    UNIQUE KEY uk_movie_keyword (movie_id, keyword_id),
    INDEX idx_mk_keyword (keyword_id)
);


SELECT 
    CONCAT(
        'CREATE TABLE movie_database.', 
        table_name, 
        ' LIKE ', 
        table_schema, 
        '.', 
        table_name, 
        '; ',
        'INSERT INTO movie_database.', 
        table_name, 
        ' SELECT * FROM ', 
        table_schema, 
        '.', 
        table_name, 
        ';'
    ) AS comandos
FROM information_schema.tables 
WHERE table_type = 'BASE TABLE' 
    AND table_schema = 'nome_do_banco_original';
    
-- testando keys
USE test;

-- Ver todas as PKs
SELECT 
    TABLE_NAME as 'Tabela',
    COLUMN_NAME as 'Coluna PK'
FROM information_schema.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'test'
  AND CONSTRAINT_NAME = 'PRIMARY'
ORDER BY TABLE_NAME;



USE test;
-- Ver todas as FKs
SELECT 
    TABLE_NAME as 'Tabela',
    COLUMN_NAME as 'Coluna FK',
    REFERENCED_TABLE_NAME as 'Referencia Tabela',
    REFERENCED_COLUMN_NAME as 'Referencia Coluna'
FROM information_schema.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'test'
  AND REFERENCED_TABLE_NAME IS NOT NULL
ORDER BY TABLE_NAME;


ALTER TABLE movie_cast
DROP FOREIGN KEY fk_cast_person;

ALTER TABLE movie_cast
DROP INDEX idx_cast_person;

ALTER TABLE movie_cast
DROP COLUMN person_id;

-- 5 CONSULTAS DO TRABALHO (FASE 1)
-- -------------Filtrando fimes por genero e ordenando por nota---------------------------------------------------
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
-- -----------------Filtrando filmes por idioma e ordenando por ordem alfabetica----------------------------------
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
LIMIT 100;
-- --------------Filtrando filmes que tem duracao definida(IS NOT NULL) e ordenando por maior duracao-------------
SELECT 
    title AS nome_do_filme,
    duration AS duracao_em_minutos,
    title_year AS ano_de_lancamento
FROM movies
WHERE duration IS NOT NULL
ORDER BY duration DESC
LIMIT 10;
-- ----------------Filtrando filmes que deram lucro e ordenando por percentual de lucro---------------------------
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
-- -----------------Filtrando filmes por diretor e ordenando por nota--------------------------------------------
SELECT
	title AS filme,
    title_year AS ano,
    imdb_score AS nota
FROM movies
JOIN people ON movies.director_id = people.person_id
WHERE people.name = 'James Cameron'
ORDER BY movies.imdb_score DESC
LIMIT 10;
-- -----------------Filtrando fimes por cor e ordenando por nota-------------------------------------------------
SELECT 
    title AS filme,
    imdb_score AS nota,
    title_year AS ano_de_lancamento
FROM movies
WHERE color = 'Black and White'
ORDER BY imdb_score DESC
LIMIT 10;

    