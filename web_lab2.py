import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу admin
cursor.execute('''
CREATE TABLE IF NOT EXISTS admin (
    admin_id INT PRIMARY KEY,
    admin_name VARCHAR(255),
    login VARCHAR(50),
    password VARCHAR(50)
)
''')

print(cursor.fetchall())

cursor.execute('''
CREATE TABLE IF NOT EXISTS client (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(255),
    login VARCHAR(50),
    password VARCHAR(50)
)
''')

print(cursor.fetchall())

cursor.execute('''
CREATE TABLE IF NOT EXISTS photostudio (
    photostudio_id INT PRIMARY KEY,
    studio_name VARCHAR(255)
)
''')
print(cursor.fetchall())
connection.commit()

cursor.execute(''' CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    admin_id INT,
    photostudio_id INT,
    date DATE,
    time_begin TIME,
    time_end TIME,
    price INT,
    client_id INT,
    FOREIGN KEY (admin_id) REFERENCES admin (admin_id) ON DELETE CASCADE,
    FOREIGN KEY (photostudio_id) REFERENCES photostudio (photostudio_id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES client (client_id) ON DELETE CASCADE
)
''')
print(cursor.fetchall())

cursor.execute('''
CREATE TABLE IF NOT EXISTS service_order (
    service_id INT PRIMARY KEY,
    service_name VARCHAR(255),
    order_id INT,
    price INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
)
''')
print(cursor.fetchall())

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
