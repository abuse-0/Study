import sqlite3

# Подключение к бд + её создание
base = sqlite3.connect('example.db')
cur = base.cursor()

# Создание таблицы users
base.execute('CREATE TABLE IF NOT EXISTS users (id PRIMARY KEY, name)')
base.commit()

# Создание таблицы orders
base.execute('CREATE TABLE IF NOT EXISTS orders (id PRIMARY KEY, user_id, product)')
base.commit()

# Вставка данных в users
cur.executemany('INSERT INTO users VALUES (?, ?)', [(1, "Алиса"),(2, "Боб"),(3, "Чарли"),(4, "Давид")])
base.commit()

# Вставка данных в orders
cur.executemany('INSERT INTO orders VALUES (?, ?, ?)', [(1, 1, "Ноутбук"), (2, 1, "Телефон"), (3, 2, "Книга"), (4, 6, "Палетка")])
base.commit()

# Выполняем INNER JOIN (Показывает только те записи, для которых нашлись пары)
cur.execute("SELECT users.name, orders.product FROM users JOIN orders ON users.id = orders.user_id;")
'''
+--------+----+        +---------+------------+         +--------+-----------+  
| name   | id |        | user_id |  product   |         |  name  | product   |  
+--------+----+        +---------+------------+         +--------+-----------+  
|  Алиса | 1  |        |    1    | Ноутбук    |   =>    | Алиса  | Ноутбук   |  
|  Боб   | 2  |        |    1    | Телефон    |         | Алиса  | Телефон   |  
|  Чарли | 3  |        |    2    | Книга      |         | Боб    | Книга     |  
|  Давид | 4  |        |    6    | Палетка    |         +--------+-----------+  
+--------+----+       +---------+-------------+  
'''

# Выполняем LEFT JOIN (Показывает все записи из первой таблицы, для не найденных пар из второй проставит NONE)
cur.execute("SELECT users.name, orders.product FROM users LEFT JOIN orders ON users.id = orders.user_id;")

'''
+--------+----+        +---------+------------+         +--------+-----------+  
| name   | id |        | user_id |  product   |         |  name  | product   |  
+--------+----+        +---------+------------+         +--------+-----------+  
|  Алиса | 1  |        |    1    | Ноутбук    |   =>    | Алиса  | Ноутбук   |  
|  Боб   | 2  |        |    1    | Телефон    |         | Алиса  | Телефон   |  
|  Чарли | 3  |        |    2    | Книга      |         | Боб    | Книга     |  
|  Давид | 4  |        |    6    | Палетка    |         | Чарли  | NULL      |  
+--------+----+        +---------+------------+         | Давид  | NULL      |  
                                                        +--------+-----------+  
'''

# RIGHT JOIN можно симулировать, поменяв местами таблицы в LEFT JOIN и поменяв порядок вывода колонок
cur.execute("SELECT users.name, orders.product FROM orders LEFT JOIN users ON orders.user_id = users.id;")

'''

+--------+----+        +---------+------------+         +--------+-----------+  
| name   | id |        | user_id |  product  |          |  name  | product   |   
+--------+----+       +---------+------------+         +--------+-----------+  
|  Алиса | 1  |        |    1    | Ноутбук    |   =>    | Алиса  | Ноутбук   |  
|  Боб   | 2  |        |    1    | Телефон    |         | Алиса  | Телефон   |  
|  Чарли | 3  |        |    2    | Книга      |         | Боб    | Книга     |   
|  Давид | 4  |        |    6    | Палетка    |         | NULL   | Палетка   |
+--------+----+        +---------+------------+         +--------+-----------+

'''

# симуляция FULL JOIN (объединяем LEFT JOIN и RIGHT JOIN через UNION)

cur.execute("""
SELECT users.name, orders.product 
FROM users 
LEFT JOIN orders ON users.id = orders.user_id
UNION
SELECT users.name, orders.product 
FROM orders 
LEFT JOIN users ON orders.user_id = users.id;
""")

'''

+--------+----+        +---------+------------+         +--------+-----------+  
| name   | id |        | user_id |  product   |         |  name  | product   |   
+--------+----+        +---------+------------+         +--------+-----------+  
|  Алиса | 1  |        |    1    | Ноутбук    |   =>    | Алиса  | Ноутбук   |  
|  Боб   | 2  |        |    1    | Телефон    |         | Алиса  | Телефон   |  
|  Чарли | 3  |        |    2    | Книга      |         | Боб    | Книга     |   
|  Давид | 4  |        |    6    | Палетка    |         | Чарли  | NULL      |
+--------+----+        +---------+------------+         | Давид  | NULL      |
                                                        | NULL   | Палетка   | 
                                                        +--------+-----------+
'''

# Вывод результатов
for row in cur.fetchall():
    print(row)

# Закрытие бд
base.close()
