import sqlite3
import csv

# Создание и подключение к БД
connection = sqlite3.connect('conciki.py')
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
    genre TEXT NOT NULL,
    age limit TEXT NOT NULL
)
""")
# Таблица продажи билетов
cursor.execute("""
CREATE TABLE tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name of the site TEXT NOT NULL,
    capacity TEXT NOT NULL,
    address TEXT NOT NULL,
    tickets sold TEXT NOT NULL
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

cursor.execute("""
INSERT INTO musician (name, genre, age) VALUES (?, ?, ?)
""", ('Руки Вверх', 'Поп', 50))

cursor.execute("""
INSERT INTO tickets (name_of_the_site, capacity, address, tickets_sold) VALUES (?, ?, ?, ?)
""", ('Крокус Сити Холл', 6200, 'Москва, ул. Международная, 20', 5000))

# 2.2 Пользовательский ввод
print("Введите имя музыканта: ")
musician_name = input()
print("Введите жанр: ")
genre = input()
print("Введите возраст: ")
age = int(input())

cursor.execute("""
INSERT INTO musician (name, genre, age) VALUES (?, ?, ?)
""", (musician_name, genre, age))

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
    ("Король и Шут", "Панк-рок", 45),
    ("Земфира", "Рок", 48),
    ("Баста", "Хип-хоп", 44),
    ("Сплин", "Рок", 55),
    ("Би-2", "Рок", 54),
    ("Ленинград", "Ска-панк", 60),
    ("Монеточка", "Поп", 26),
    ("Face", "Хип-хоп", 27),
    ("Noize MC", "Хип-хоп", 39),
    ("Макс Корж", "Поп", 36),
    ("Оксимирон", "Хип-хоп", 39),
    ("Скриптонит", "Хип-хоп", 34),
    ("Дима Билан", "Поп", 43),
    ("Полина Гагарина", "Поп", 38),
    ("Мот", "Хип-хоп", 35)
]

cursor.executemany("""
INSERT INTO musician (name, genre, age) VALUES (?, ?, ?)
""", musicians_array)
