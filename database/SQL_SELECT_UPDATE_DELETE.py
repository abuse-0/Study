import sqlite3

# Подключение к бд + ее создание в папке
base = sqlite3.connect('new.db')
cur = base.cursor()

# Создание 2х таблиц(login, password), PRIMARY KEY означает, что 2 таких значения в столбце быть не может
base.execute('CREATE TABLE IF NOT EXISTS {}(login PRIMARY KEY, password)'.format('data'))
base.commit()

# Вставка в бд 
cur.execute('INSERT INTO data VALUES(?, ?)', ('jonny123', '123456789'))
base.commit()

# Еще одна вставка в бд
cur.execute('INSERT INTO data VALUES(?, ?)', ('billy123', 'password'))
base.commit()

# Вставка в бд значений из списка
cur.executemany('INSERT INTO data VALUES(?, ?)', ([['user1', '123'], ['user2', '1234'], ['user3', '12345']]))
base.commit()

# Получение логинов из бд
r = cur.execute('SELECT login FROM data').fetchall()

# Получение пароля по логину
r = cur.execute('SELECT password FROM data WHERE login == ?', ('jonny123',)).fetchone()

# UPDATE
cur.execute('UPDATE data SET password == ? WHERE password == ?', ('123456789', 'password'))
base.commit()

# DELETE
cur.execute('DELETE FROM data WHERE login == ?', ('jonny123',))
base.commit()

# Удаление бд
base.execute('DROP TABLE IF EXISTS data')
base.commit()

# Закрытие бд
base.close()