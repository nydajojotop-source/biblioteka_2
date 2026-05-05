# Проект базы данных
## Описание
**Проект базы данных концертов в разных клубах**
## Структура
**Таблица musician (музыканты)**

| Поле | Тип     | Описание                   |
|------|---------|----------------------------|
| id   | INTEGER | Идентификатор исполнителя  |
| name | TEXT    | Имя исполнителя            |
| genre| TEXT    | жанр исполнителя           |

**Таблица tickets (билеты)**

| Поле                |   Тип   |         Описание           |
|---------------------|---------|----------------------------|
| id                  | INTEGER | Идентификатор кассеты      |
| name_of_the_site    | TEXT    | Название площадки          |
| capacity            | TEXT    | Вместимость                |
| address             | TEXT    | адресс площадки            |
| tickets_sold        | TEXT    | продано билетов            |

**Таблица concert(концерты)**

| Поле           | Тип     | Описание                             |
|----------------|---------|--------------------------------------|
| id             | INTEGER | Идентификатор операции               |
| musician_id    | INTEGER | Идентификатор исполнителя из musican |
| tickets_id     | INTEGER | Идентификатор билета из tickets      |
| start_time     | TEXT    | Дата начала выступления              |
| end_time       | TEXT    | Дата конца выступления               |



# Скриншоты работы таблицы

>Таблица musician
<img width="1271" height="608" alt="{C2F93991-F2B7-4276-A38C-0DC64E54AD06}" src="https://github.com/user-attachments/assets/1d01a0df-3de4-457f-9649-fe23f8376b3c" />

>Таблица tickets
<img width="1263" height="443" alt="{E37132B2-B20A-4D72-87FE-7187EBAF081D}" src="https://github.com/user-attachments/assets/34f335fb-d60a-4c1f-9b5a-2c173625b3f2" />

>Таблица concert
<img width="1230" height="285" alt="{C0207907-A1E9-4A34-9125-01970834C450}" src="https://github.com/user-attachments/assets/9ff03b3a-399d-430a-8d8a-5932abd09c7a" />
