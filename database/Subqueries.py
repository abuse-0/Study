import sqlite3

base = sqlite3.connect("example_subqueries.db")
cur = base.cursor()

base.execute("CREATE TABLE IF NOT EXISTS products (id PRIMARY KEY, name, price)")
base.commit()

# Числа обязательно писать как числа
cur.executemany(
    "INSERT INTO products VALUES (?, ?, ?)",
    [
        (1, "Телефон", 1000),
        (2, "Ноутбук", 1599),
        (3, "Телевизор", 700),
        (4, "ИИ кукла", 3000),
    ],
)
base.commit()

cur.execute(
    """
    SELECT id, name, price 
    FROM products 
    WHERE price = (SELECT MAX(price) FROM products)
    """
)

print(cur.fetchone())  # (4, 'ИИ кукла', 3000)


base.close()
