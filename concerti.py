import sqlite3
import csv

# Создание и подключение к БД
connection = sqlite3.connect('libre.db')
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Удаление старых таблиц
cursor.execute("DROP TABLE IF EXISTS concert")
cursor.execute("DROP TABLE IF EXISTS musician")
cursor.execute("DROP TABLE IF EXISTS tickets")

# Таблица групп
cursor.execute("""
CREATE TABLE musician (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    genre TEXT NOT NULL
)
""")
# Таблица продажи билетов
cursor.execute("""
CREATE TABLE tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_of_the_site TEXT NOT NULL,
    capacity TEXT NOT NULL,
    address TEXT NOT NULL,
    tickets_sold TEXT NOT NULL
)
""")
# Таблица концертов
cursor.execute("""
CREATE TABLE concert (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    musician_id INTEGER NOT NULL,
    tickets_id INTEGER NOT NULL,
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    FOREIGN KEY (musician_id) REFERENCES musician(id),
    FOREIGN KEY (tickets_id) REFERENCES tickets(id)
)
""")
# 2.1 Ручной ввод
cursor.execute("""
INSERT INTO musician (name, genre) VALUES (?, ?)
""", ('Руки Вверх', 'Поп'))

cursor.execute("""
INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
""", ('Крокус Сити Холл', 6200, 'Москва, ул. Международная, 20', 5000))

cursor.execute(""" 
    INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
    """, ('Стадион Спартак', 45000, 'Москва, Волгоградский пр-т, 47', 38000))

cursor.execute(""" 
    INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
    """, ('Газпром Арена', 68000, 'Санкт-Петербург, пр. Добролюбова, 16', 60000))

cursor.execute(""" 
    INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
    """, ('Ростов Арена', 45000, 'Ростов-на-Дону, пр. Левобережный, 1', 42000))

cursor.execute(""" 
    INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
    """, ('Казань Арена', 45000, 'Казань, ул. Чистопольская, 50', 43000))

cursor.execute(""" 
    INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
    """, ('Дворец Спорта', 3500, 'Екатеринбург, ул. Большакова, 90', 3300))

cursor.execute(""" 
    INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
    """, ('Клуб 16 Тонн', 800, 'Москва, ул. Пресненский Вал, 6', 750))

cursor.execute(""" 
    INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
    """, ('Arena Hall', 1200, 'Краснодар, ул. Конгрессная, 1', 1100))

cursor.execute(""" 
    INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
    """, ('Театр Эстрады', 1000, 'Новосибирск, ул. Депутатская, 45', 980))

cursor.execute(""" 
    INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
    """, ('Минск-Арена', 15000, 'Минск, пр. Победителей, 111', 14000))

cursor.execute(""" 
    INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
    """, ('Баскет Холл', 7000, 'Краснодар, ул. Пригородная, 24', 6500))





cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (?,?)
    """ , ('The Hatters', 'Фолк-панк'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (?,?)
    """, ('ЛСП', 'Хип-хоп / Альтернатива'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (? , ?)
    """ ,('Кис-кис', 'Поп-панк'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (?,?)
    """ ,('Miyagi & Эндшпиль', 'Хип-хоп / Регги'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (?,?)
    """ ,('Пошлая Молли', 'Поп-панк / Инди'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (?,?)
    """ ,('Кравц', 'Хип-хоп'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (? , ?)
    """ ,('Нервы', 'Альтернативный рок'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (? , ?)
    """ ,('Красные Звёзды', 'Рок'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (? , ?)
    """ ,('SLAVA MARLOW', 'Поп'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (? , ?)
    """ ,('Папин Олимпос', 'Поп-рок'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (? , ?)
    """ , ('Остап Парфёнов', 'Инди-фолк'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (? , ?)
    """ ,('Инстасамка', 'Поп / Хип-хоп'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (?,?)
    """ ,('Wildways', 'Металкор'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (?,?)
    """ ,('MORGENSHTERN', 'Поп / Хип-хоп'))

cursor.execute(""" 
    INSERT INTO musician (name, genre) VALUES (?,?)
    """ ,('zhanulka', 'Инди-поп'))

cursor.execute(""" 
    INSERT INTO concert (musician_id, tickets_id, start_time, end_time) VALUES (? , ? , ? , ?)
    """ , (1, 1, '2025-06-15 19:00:00', '2025-06-15 22:00:00'))

cursor.execute(""" 
    INSERT INTO concert (musician_id, tickets_id, start_time, end_time) VALUES (? , ? , ? , ?)
    """ , (10, 8, '2025-09-05 20:00:00', '2025-09-05 23:00:00'))

cursor.execute(""" 
    INSERT INTO concert (musician_id, tickets_id, start_time, end_time) VALUES (? , ? , ? , ?)
    """ , (11, 3, '2025-09-15 19:00:00', '2025-09-15 22:00:00'))

cursor.execute(""" 
    INSERT INTO concert (musician_id, tickets_id, start_time, end_time) VALUES (? , ? , ? , ?)
    """ , (12, 9, '2025-09-20 18:30:00', '2025-09-20 21:00:00'))

cursor.execute(""" 
    INSERT INTO concert (musician_id, tickets_id, start_time, end_time) VALUES (? , ? , ? , ?)
    """ , (13, 5, '2025-10-01 20:00:00', '2025-10-01 23:30:00'))

cursor.execute(""" 
    INSERT INTO concert (musician_id, tickets_id, start_time, end_time) VALUES (? , ? , ? , ?)
    """ , (14, 10, '2025-10-10 19:00:00', '2025-10-10 22:00:00'))

cursor.execute(""" 
    INSERT INTO concert (musician_id, tickets_id, start_time, end_time) VALUES (? , ? , ? , ?)
    """ , (15, 4, '2025-10-20 18:00:00', '2025-10-20 21:30:00'))




# 2.2 Пользовательский ввод
print("Введите имя музыканта: ")
musician_name = input()
print("Введите жанр: ")
genre = input()

cursor.execute("""
INSERT INTO musician (name, genre) VALUES (?, ?)
""", (musician_name, genre))

print("Введите название площадки: ")
site_name = input()
print("Введите вместимость: ")
capacity = int(input())
print("Введите адрес: ")
address = input()
print("Введите количество проданных билетов: ")
tickets_sold = int(input())

cursor.execute("""
INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
""", (site_name, capacity, address, tickets_sold))

# 2.3 Через случайные комбинации (музыканты)
musicians_array = [
    ("Король и Шут", "Панк-рок"),
    ("Земфира", "Рок"),
    ("Баста", "Хип-хоп"),
    ("Сплин", "Рок"),
    ("Би-2", "Рок"),
    ("Ленинград", "Ска-панк"),
    ("Монеточка", "Поп"),
    ("Face", "Хип-хоп"),
    ("Noize MC", "Хип-хоп"),
    ("Макс Корж", "Поп"),
    ("Оксимирон", "Хип-хоп"),
    ("Скриптонит", "Хип-хоп"),
    ("Дима Билан", "Поп"),
    ("Полина Гагарина", "Поп"),
    ("Мот", "Хип-хоп")
]

cursor.executemany("""
INSERT INTO musician (name, genre) VALUES (?, ?)
""", musicians_array)

connection.commit()
connection.close()