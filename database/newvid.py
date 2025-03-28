# Все команды в cmd должны оканчиваться на ;
# Команда для подключения: cd "C:\Program Files\PostgreSQL\17\bin" и потом  psql -U postgres
# \dt - список всех таблиц, \d superheroes - посмотреть конкретную
# Если забыл ; и видишь 1 палку: postgres-#, то пиши или ; для подтверждения или \r для отмены действия

"""Типы баз данных
1)Сетевые и иерархические – данные в виде графов и деревьев, подходят для жесткой структуры.
2)Реляционные – данные в таблицах, SQL, связи и транзакции (как раз то, что учим).
3)Big Data, NoSQL – масштабируемость, работа с неструктурированными и большими данными.
"""

"""
| ID  | Name                               | Align               | Eye Color  | Hair Color             | Gender            | Appearances | Year | Universe |
|-----|------------------------------------|---------------------|------------|------------------------|-------------------|-------------|------|----------|
|   1 | Spider-Man (Peter Parker)         | Good Characters     | Hazel Eyes | Brown Hair            | Male Characters   |        4043 | 1962 | Marvel   |
|   2 | Captain America (Steven Rogers)   | Good Characters     | Blue Eyes  | White Hair            | Male Characters   |        3360 | 1941 | Marvel   |
|   3 | Wolverine (James "Logan" Howlett) | Neutral Characters  | Blue Eyes  | Black Hair            | Male Characters   |        3061 | 1974 | Marvel   |
|   4 | Iron Man (Anthony "Tony" Stark)   | Good Characters     | Blue Eyes  | Black Hair            | Male Characters   |        2961 | 1963 | Marvel   |
|   5 | Thor (Thor Odinson)               | Good Characters     | Blue Eyes  | Blonde Hair           | Male Characters   |        2258 | 1950 | Marvel   |
|   6 | Benjamin Grimm (Earth-616)        | Good Characters     | Blue Eyes  | No Hair               | Male Characters   |        2255 | 1961 | Marvel   |
|   7 | Reed Richards (Earth-616)         | Good Characters     | Brown Eyes | Brown Hair            | Male Characters   |        2072 | 1961 | Marvel   |
|   8 | Hulk (Robert Bruce Banner)        | Good Characters     | Brown Eyes | Brown Hair            | Male Characters   |        2017 | 1962 | Marvel   |
|   9 | Black Widow (Natasha Romanoff)    | Good Characters     | Green Eyes | Red Hair              | Female Characters |        2093 | 1964 | Marvel   |
|  10 | Jean Grey (Phoenix)               | Good Characters     | Green Eyes | Red Hair              | Female Characters |        1501 | 1963 | Marvel   |
|  11 | Mary Jane Watson                  | Good Characters     | Green Eyes | Red Hair              | Female Characters |        1356 | 1965 | Marvel   |
|  12 | Batwoman (Katherine Kane)         | Good Characters     | Green Eyes | Auburn Hair           | Female Characters |        1203 | 2006 | DC       |
|  13 | Barbara Gordon (Batgirl)          | Good Characters     | Green Eyes | Auburn Hair           | Female Characters |        1752 | 1967 | DC       |
|  14 | Starfire (Koriand'r)              | Good Characters     | Green Eyes | Strawberry Blond Hair | Female Characters |         987 | 1980 | DC       |
|  15 | Jessica Jones                     | Neutral Characters  | Brown Eyes | Black Hair            | Female Characters |        1105 | 2001 | Marvel   |
|  16 | X-23 (Laura Kinney)               | Good Characters     | Blue Eyes  | Black Hair            | Female Characters |        1420 | 2004 | Marvel   |
"""
#
#
#
"""SELECT
SELECT * FROM superheroes - получение всех столбцов из таблицы superheroes


SELECT name, appearances - выбрать стобцы name, appearances
FROM superheroes           из таблицы superheroes


SELECT name AS hero_name, - выбрать столбец name, как hero_name
appearances                 выбрать столбец appearances
FROM superheroes            из таблицы superheroes


SELECT DISTINCT(align) - получить только уникальные значения из столбца align
FROM superheroes         из таблицы superheroes


SELECT DISTINCT(hair) - получить только уникальные значения из столбца hair
FROM superheroes        из таблицы superheroes
LIMIT 10                ограничиваем результат первыми 10тью элементами
"""
#
#
#
"""WHERE
SELECT *                           - Выбрать все
FROM superheroes                     из таблицы superheroes
WHERE gender = 'Female Characters'   где значение столбца gender равняется Female Characters


Операторы сравнения:
=, !=(<>), ><, >=  равно, неравно, больше/меньше, больше или равно
between            значение находится в указанном диапазоне
in                 значение входит в список
like               проверка строки на соответствие шаблону


SELECT *                            - Выбрать все
FROM superheroes                      из таблицы superheroes
WHERE year BETWEEN 2000 AND 2005      где значение столбца year находится в промежутке между 2000 и 2005


SELECT *                                                              - Выбрать все
FROM superheroes                                                        из таблицы superheroes
WHERE hair IN ('Strawberry Blond Hair', 'Red Hair', 'Auburn Hair')      где значение столбца hair находится в списке ('Strawberry Blond Hair', 'Red Hair', 'Auburn Hair')  


LIKE:
% - любое количество любых символов
_ - только один символ


Select *                  - Выбрать все
FROM superheroes            из таблицы superheroes
WHERE hair LIKE '%Blond%'   где значение столбца hair содержит Blond с любым количеством символов до Blond и после Blond
с _Blond_ это бы смотрелось только как (1Blond2), (fdsadf 1Blond2) уже не подошел бы


Логические операции в WHERE:
AND - и, OR - или, NOT - не


SELECT *                            - Выбрать все
FROM superheroes                      из таблицы superheroes
WHERE gender = 'Female Characters'    где значение столбца gender равно Female Characters
AND                                   и
align = 'Bad Characters'              значение столбца align равно Bad Characters


SELECT *                            - Выбрать все
FROM superheroes                      из таблицы superheroes
WHERE hair = 'Red Hair'               где значение столбца hair равно Red Hair
OR hair = 'Strawberry Blond Hair'     или значение столбца hair равно Strawberry Blond Hair
OR hair = 'Auburn Hair'               или значение столбца hair равно Auburn Hair


SELECT *                                                                  - Выбрать все строки             
FROM superheroes                                                            из таблицы superheroes 
WHERE hair NOT IN ('Blond Hair', 'Black Hair', 'Brown Hair', 'Red Hair')    где значение столбца hair не соответствует значения в списке ('Blond Hair', 'Black Hair', 'Brown Hair', 'Red Hair')
"""
# 
# 
#
"""Сортировка
SELECT *            - Выбрать все строки
FROM superheroes      из таблицы superheroes
ORDER BY year         отсортировать по столбцу year


Порядок сортировки:
ASC (ascending) - сортировка по возрастанию(применяется по умолчанию)
DESK (descending) - сортировка по убыванию


SELECT *                   - Выбрать все строки
FROM superheroes             из таблицы superheroes
ORDER BY appearances DESC    отсортировать по столбцу appearances по убыванию
"""
#
"""Сортировка и фильтры в SELECT
SELECT *                           - Выбрать все строки
FROM superheroes                     из таблицы superheroes
WHERE align = 'Bad Characters'       где значение столбцы align равно Bad Characters
ORDER BY appearances DESC            отсортировать по столбцу appearances по убыванию
"""
#
"""Сортировка и ограничение количества строк
SELECT *                                      - Выбрать все строки
FROM superheroes                                из таблицы superheroes
WHERE align = 'Bad Characters'                  где значение столбца align равно Bad Characters
AND                                             и
gender = 'Female Characters'                    значение столбца gender равно Female Characters
ORDER BY appearances DESC                       отсортировать по столбцу appearances по убыванию
LIMIT 5                                         вывести только 5 строк
"""
#
"""Сортировка по нескольким столбцам 
SELECT *                              - Выбрать все строки
FROM superheroes                        из таблицы superheroes
ORDER BY year, appearances              отсортировать по столбцу years, appearances
сначала сортируются по years в порядке возрастания, а затем по appearances в порядке возрастания
"""
#
#
#
"""Типы данных в SQL
CHARACTER(n) - CHAR(n)                Строка фиксированной длины последовательность
CHARACTER VARYING(n) - VARCHAR(n)     Строка переменной длины, максимальная длина n
BOOLEAN                               Логический тип данных
INTEGER - INT                         Целое число
NUMERIC(p,s)                          Действительное число (р - количество значащих цифр, s - количество цифр после запятой). Хранится точно.
REAL                                  Действительное число одинарной точности, формат IEEE 754
DOUBLE PRECISION                      Действительное число двойной точности, формат IEEE 754
DATE                                  Дата
TIMESTAMP                             Дата и время
"""
#
"""Создание таблиц в SQL
CREATE TABLE superheroes(   - Создать таблицу superheroes
    id INT,                   создать в таблице столбец id с типом данных int
    name VARCHAR(100),        создать в таблице столбец name с типом данных str с ограничением в 100 символов
    align VARCHAR(30),        создать в таблице столбец align с типом данных str с ограничением в 30 символов
    eye VARCHAR(30),          создать в таблице столбец eye с типом данных str с ограничением в 30 символов
    hair VARCHAR(30),         создать в таблице столбец hair с типом данных str с ограничением в 30 символов
    gender VARCHAR(30),       создать в таблице столбец gender с типом данных str с ограничением в 30 символов
    appearances INT,          создать в таблице столбец appearances с типо данных int
    year INT,                 создать в таблице столбец year с типо данных int
    universe VARCHAR(10)      создать в таблице столбец universe с типом данных str с ограничением в 10 символов
)
"""
#
"""Первчиный ключ
CREATE TABLE superheroes(
    id INT PRIMARY KEY,     - Первичный ключ, гарантирует уникальность строки в столбце id, два одинаковых id не будет
    name VARCHAR(100)           
)
"""
#
"""Автоматическое заполнение первичного ключа в PostgreSQL
CREATE TABLE superheroes(   
    id SERIAL PRIMARY KEY,   - для создания поля id будет использовано int, будет высчитываться автоматически(неиспользованное + 1)    
    name VARCHAR(100),        
    align VARCHAR(30),        
    eye VARCHAR(30),          
    hair VARCHAR(30),         
    gender VARCHAR(30),       
    appearances INT,          
    year INT,                 
    universe VARCHAR(10)      
)
"""
#
"""Удаление таблицы в SQL
DROP TABLE superheroes     - Удалить таблицу superheroes
"""
#
"""Безопасный скрипт создания таблицы
-- Создаем таблицу супергероев
DROP TABLE IF EXISTS superheroes;    - Удалить таблицу superheroes, если она существует
CREATE TABLE superheroes(   
    id SERIAL PRIMARY KEY,       
    name VARCHAR(100),        
    align VARCHAR(30),        
    eye VARCHAR(30),          
    hair VARCHAR(30),         
    gender VARCHAR(30),       
    appearances INT,          
    year INT,                 
    universe VARCHAR(10)
);
"""
#
#
#
"""Изменение таблиц в SQL
ALTER TABLE superheroes                                    - Изменить таблицу superheroes
ADD COLUMN alive BOOLEAN;                                    добавить столбец alive с типом BOOLEAN 

ALTER TABLE superheroes                                    - Изменить таблицу superheroes
ADD COLUMN first_appearance TIMESTAMP;                       добавить столбец first_apperance с типом TIMESTAMP

ALTER TABLE superheroes                                    - Изменить таблицу superheroes
DROP COLUMN year;                                            удалить столбец year

ALTER TABLE superheroes                                    - Изменить таблицу superheroes
RENAME COLUMN name TO hero_name;                             переименовать столбец name в hero_name 

ALTER TABLE superheroes                                    - Изменить таблицу superheroes
RENAME TO comic_characters;                                  переименовать таблицу в comic_characters
"""
#
#
#
"""Вставка данных в таблицу
INSERT INTO superheroes(name, appearances, universe)  - Вставить в таблицу superheroes в поля (name, appearances, universe)
VALUES ('Spider-Man', 4043, 'marvel')                   значения ('Spider-Man', 4043, 'marvel') 
"""
#
#
#
"""Изменение данных в таблице
UPDATE superheroes               - Обновить таблицу superheroes
SET name='Batman',                 установить в столбце name значение Batman
universe ='dc'                     в столбце universe значение dc    
WHERE id=1                         у строки, где id равно 1
"""
#
"""Изменение нескольких строк
UPDATE superheroes               - Обновить таблицу superheroes
SET gender='Man',                  установить в столбце gender значение Man
WHERE gender='Male Characters'     в строках, где в столбце gender установлено значение Male Characters
"""
#
"""Удаление данных из таблицы
DELETE FROM superheroes          - Удалить из таблицы superheroes
WHERE id=2                         строку, в которой в столбце id установлено значение 2
"""
# 
"""Удаление нескольких строк
DELETE FROM superheroes          - Удалить из таблицы superheroes
WHERE gender='Male Characters'     строки, в которых в столбце gender установлено значение Male Characters
"""
#
"""Удалить все данные
DELETE FROM superheroes
"""
#
#
# COUNT(*) - считает кол-во строк в каждой группе, если не группировать он подсчитает кол-во всех элементов, т.к будет ток 1 группа
"""Группировка данных
SELECT gernder, COUNT(*)  - Выбрать gender и кол-во строк в текущей группе
FROM superheroes            в таблице superheroes
GROUP BY gender             группировать по столбцу gender
"""
# Вот сверху будет 2 строки male-20, female-50, но если добавить группировку еще по universe, будет dc-male-12, dm-female-30, marvel-male-8, marvel-female-20
"""Несколько значение в группировке
SELECT universe, align, COUNT(*)      - Выбрать universe, align, кол во строк в текущей группе
FROM superheroes                        из таблицы superheroes
GROUP BY universe, align                группировать по universe, align
"""
#
"""Фильтрация + группировка + сортировка + ограничение по кол-ву строк
SELECT hair, COUNT(*)               - Выбрать hair, количество строк в текущей группе
FROM superheroes                      из таблицы superheroes
WHERE gender='Female Characters'      где значение столбца gender равно Female Characters
GROUP BY hair                         группировать по значение hair
ORDER BY count(*) DESC                сортировать по столбцу count(*) по убыванию
LIMIT 5                               показать только первые 5 строк
"""
#
#
#
"""Агрегатные функции в SQL
AVG - среднее значение 
COUNT - количество значений
MAX - максимальное значение 
MIN - минимальное значение
SUM - сумма 
"""
#
"""Кол-во хороших/плохих/еще каких то и сумма их появлений
SELECT align, COUNT(*), SUM(apperances) - Выбрать align, кол-во строк в текущей группе, сумму всех apperances в текущей группе
FROM superheroes                          из таблицы superheroes
GROUP BY align                            группировать по столбцу align
"""
#Снизу будет выведено good characters - 65.4324534 - 65, neureal character - 36.4324534 - 36 и тд
"""Тут SUM(appearances)/COUNT(*) AS average - почти то же самое, что AVG(appearances), ток округленное до целого
SELECT align, AVG(appearances),        - Выбрать align, среднее значение в столбце appearances
SUM(appearances)/COUNT(*) AS average     сумму значений в столбце appearances, поделенную на кол-во строк в текущей группе, вывести в столбце average
FROM superheroes                         из таблицы superheroes 
GROUP BY align                           грпуппировать по столбцу align
"""
# 
"""
SELECT year, MIN(appearances), MAX(appearances) - Выбрать year, минимальное значение appearances в текущей группе, максимальное значение appearances в текущей группе
FROM superheroes                                  из таблицы superheroes
GROUP BY year                                     группировать по столбцу year
ORDER BY MAX(appearances) DESC                    сортировать по максимальному значению appearances в порядке убывания
"""
#
"""Сокращение
SELECT year, MIN(appearances),
MAX(appearances) AS max_ap         - альяс, так же теперь столбец будет так называться
FROM superheroes
GROUP BY year
ORDER BY max_ap DESC
"""
#
"""В этом случае вся таблица - 1 большая группа => 1 строка 
SELECT COUNT(*),
MIN(appearances),
MAX(appearances),
SUM(appearances),
AVG(appearances)
FROM superheroes
"""
#
#
#
"""
SELECT hair, COUNT(*)               
FROM superheroes                      
WHERE gender='Female Characters'        
GROUP BY hair
HAVING COUNT(*) > 10       -       Вывести только те строки, где COUNT(*) > 10, в WHERE это записать нельзя, 
т.к там группы еще не созданы, а HAVING запускается после создания групп
"""
#
"""
SELECT hair, COUNT(*)               
FROM superheroes                      
WHERE gender='Female Characters'        
GROUP BY hair
HAVING COUNT(*) BETWEEN 50 AND 300  - Вывести строки, где COUNT(*) больше 50 и меньше 300
"""
#
#
#
"""Новая таблица movies
 id |                title                | year | superhero_id
----+-------------------------------------+------+--------------
  1 | Spider-Man                          | 2002 |            1
  2 | The Amazing Spider-Man              | 2012 |            1  
  3 | Captain America: The First Avenger  | 2011 |            2
  4 | Captain America: The Winter Soldier | 2014 |            2
  8 | Logan                               | 2017 |          4854
  5 | Batman                              | 1989 |          4854
  6 | Batman Returns                      | 1992 |          4854
  7 | The Dark Knight Rises               | 2012 |            3

superhero_id - FOREIGN KEY(внешний ключ) - можнет содержать только значение,
которое находится в столбце, на который он ссылается, а ссылается она на id в таблице superheroes

В таблице superheroes лучше хранить align в виде align_id, т.к если удалить персонажа, который единственный
представлял какой то тип, то этот тип удалится вместе с ним
"""
#
"""На помощь приходит создание новой таблицы alignment с ссылкой на align_id:
 id |       align
----+-------------------
  1 | Good
  2 | Bad
  3 | Neutral
  4 | Reformed Criminal


  id  |                name                 | align_id |    eye     |    hair    |     gender      | appearances | year | universe
------+-------------------------------------+----------+------------+------------+-----------------+-------------+------+----------
    1 | Spider-Man (Peter Parker)           |        1 | Hazel Eyes | Brown Hair | Male Characters |        4043 | 1962 | Marvel
    2 | Captain America (Steven Rogers)     |        2 | Blue Eyes  | White Hair | Male Characters |        3360 | 1941 | Marvel
 4854 | Batman (Bruce Wayne)                |        3 | Blue Eyes  | Black Hair | Male Characters |        3093 | 1939 | DC
    3 | Wolverine (James \"Logan\" Howlett) |        4 | Blue Eyes  | Black Hair | Male Characters |        3061 | 1974 | Marvel
    4 | Iron Man (Anthony \"Tony\" Stark)   |        5 | Blue Eyes  | Black Hair | Male Characters |        2961 | 1963 | Marvel

Таким образом впринципе заменять данные почти все, но это минус для понятности
"""
#
#
#
"""
products
 id |                             name                              | type_id | price
----+---------------------------------------------------------------+---------+-------
  1 | Основы искусственного интеллекта                              |       1 | 15000
  2 | Технологии обработки больших данных                           |       1 | 50000
  3 | Программирование глубоких нейронных сетей                     |       1 | 30000
  4 | Нейронные сети для анализа текстов                            |       1 | 50000
  5 | Нейронные сети для анализа изображений                        |       1 | 50000
  6 | Инженерия искусственного интеллекта                           |       1 | 60000
  7 | Как стать DataScientist'ом                                    |       2 |   0
  8 | Планирование карьеры в Data Science                           |       2 |  2000
  9 | Области применения нейросетей: в какой развивать экспертность |       2 |  4000
 10 | Программирование глубоких нейронных сетей на Python           |       3 |  1000
 11 | Математика для Data Science                                   |       3 |  2000
 12 | Основы визуализации данных                                    |       3 |   500

 type_id ссылается на столбец id в product_types

 product_types
 id |  type_name
----+--------------
  1 | Онлайн-курс
  2 | Вебинар
  3 | Книга
  4 | Консультация
"""
#
"""Объединение данных из нескольких таблиц
SELECT products.name, product_types.type_name - Выбрать столбец name из таблицы products и столбец type_name из таблицы product_types 
FROM products INNER JOIN product_types                из таблицы product, объединенной с таблицей product_types
ON products.type_id = product_types.id          при условии, что  значение столбца type_id из таблицы products равно значению столбца id из таблицы product_types
"""
#
"""Сокращение верхнего запроса
SELECT p.name, t.type_name 
FROM products AS p JOIN product_types AS t              
ON p.type_id = t.id          
"""
#
"""Фильтрация данных из нескольких таблиц + сокращение
SELECT p.name AS product_name,
       t.type_name AS product_type,
       p.price AS product price
FROM products AS p JOIN product_types AS t
ON p.type_id = t.id
WHERE t.type_name='Вебинар'
AND p.price = 0
"""

"""Сортировка с join + сокращение
SELECT p.name AS product_name,
       t.type_name AS product_type,
       p.price AS product price
FROM products AS p JOIN product_types AS t
ON p.type_id = t.id
WHERE t.type_name='Онлайн-курс'
ORDER BY p.price DESC
"""
#
#
#
"""Левое внешнее объединение(всё с левой таблицы выведется)
SELECT products.name, product_types.type_name 
FROM products LEFT OUTER JOIN product_types                
ON products.type_id = product_types.id        
"""

"""Правое внешнее объединение(всё с правой таблицы выведется)
SELECT products.name, product_types.type_name 
FROM products RIGHT OUTER JOIN product_types                
ON products.type_id = product_types.id        
"""

"""Полное внешнее объединение(всё с обеих таблиц выведется)
SELECT products.name, product_types.type_name 
FROM products FULL OUTER JOIN product_types                
ON products.type_id = product_types.id        
"""

"""Внутреннее объединение(если слева или справа нет значения - строка не выводится)
SELECT products.name, product_types.type_name 
FROM products INNER JOIN product_types             
ON products.type_id = product_types.id        
"""
#https://drawsql.app/teams/ural-federal-university/diagrams/online-school
#https://drawsql.app/teams/ural-federal-university/diagrams/online-school
#https://drawsql.app/teams/ural-federal-university/diagrams/online-school
"""Продукты в заказе
SELECT p.id,
       p.price,
       s.quantity,
       p.price * s.quantity AS total -- умножаем стоимость на кол-во
FROM products AS p JOIN sales As s
    ON p.id = s.product_id
WHERE s.order_id=2
"""
#
"""Все покупки заказчика
SELECT p.id,
       p.name,
       p.price,
       s.quantity,
       p.price * s.quantity AS total
FROM products AS p JOIN sales As s 
    ON p.id = s.product_id
    JOIN orders AS o
    ON o.id = s.order_id
WHERE o.customer_id=1 -- айди заказчика
"""
#
#
#
"""Подзапросы в SQL
SELECT id, name, price -- Получить id, name, price
FROM products -- из таблицы products
WHERE price = (SELECT MAX(price) -- где значение в столбце price = выбрать максимум из столбца price
               FROM products) -- в таблице products
"""
#
"""Инфа о продуктах, проданных хотя бы 1 раз
SELECT id, name, price -- Выбрать id, name, price
FROM products -- из таблицы products
WHERE id IN -- где id входит в список значений в 
(SELECT product_id FROM sales) -- столбце product_id в таблице sales(ну проданы типо)
"""
#
"""Подзапрос с update
UPDATE products -- обновить таблицу products
SET price = price + 500 -- установить в столбцах price значения price + 500
WHERE type_id = (SELECT id
                 FROM product_types
                 WHERE type_name='Книга')
--Где type_id равно значению (Выбрать id из таблицы product_types, где значение type_name это 'Книга')
"""
#
#
#
"""Выполнение транзации
START TRANSACTION;

UPDATE accounts SET balance = balance - 15000
WHERE account_number = 123456

-- Важно, чтобы обе команды выполнились успешно

UPDATE accounts SET balance = balance + 15000
WHERE account_number = 9876543

COMMIT; -- чтобы применить
-- Выбери чето одно
ROLLBACK; -- чтобы откатить
"""
# В Postgre по умолчанию после каждой команды автофиксация транзации есть, из за этого нельзя откатиться
# Но опять же это только по умолчанию, ничего не мешает не юзать это
#
"""Создание индекса
CREATE INDEX superheroes_name_idx
ON superheroes(name)
"""
#
"""Теперь поиск ускорен автоматически
SELECT name, appearances, eye, hair
FROM superheroes
WHERE name = ' Iron Man (Anthony\"Tony\" Stark)'
"""
#
"""индекс для сортировки
CREATE INDEX superheroes_ppearances_idx
ON superheroes(appearances DESC)
"""
#
"""индекс по нескольким столбцам
CREATE INDEX person_name_idx
ON person(last_name, first_name)
"""
# Индексы хранятся в базе и замедляют приколы, для всех столбцов юзать их не надо
#
#
