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
appearances                 выбрать столбец apperances
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
#
#
"""Сортировка и фильтры в SELECT
SELECT *                           - Выбрать все строки
FROM superheroes                     из таблицы superheroes
WHERE align = 'Bad Characters'       где значение столбцы align равно Bad Characters
ORDER BY appearances DESC            отсортировать по столбцу apperances по убыванию
"""
