import sqlite3

def create_countries_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE countries(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    ''')
    conn.commit()


def insert_countries_data(conn):
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO countries (title) VALUES (?)', [('Япония',), ('Корея',), ('Китай',)])
    conn.commit()

def create_cities_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            area FLOAT DEFAULT 0,
            country_id INTEGER,
            FOREIGN KEY (country_id) REFERENCES countries (id)
        )
    ''')
    conn.commit()

def insert_cities_data(conn):
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO cities (title, country_id) VALUES (?, ?)',
                       [('Токио', 1), ('Сеул', 2), ('Пекин', 3),
                        ('Киото', 1), ('Пусан', 2), ('Шангхаи', 3), ('Осака', 1)])
    conn.commit()

def update_city_area(conn, city_id, new_area):
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE cities
        SET area = ?
        WHERE id = ?
''', (new_area, city_id))
    conn.commit()

def create_students_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city_id INTEGER,
            FOREIGN KEY (city_id) REFERENCES cities (id)
        )
    ''')
    conn.commit()


def insert_students_data(conn):
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)',
                       [('John', 'Doe', 1), ('Jane', 'Smith', 2), ('Bob', 'Johnson', 3),
                        ('Alice', 'Williams', 4), ('Charlie', 'Brown', 5), ('Eva', 'Davis', 6),
                        ('David', 'Clark', 7), ('Emma', 'Lee', 2), ('Frank', 'Taylor', 3),
                        ('Grace', 'Moore', 4), ('Henry', 'Adams', 5), ('Ivy', 'Evans', 6),
                        ('Jack', 'Ford', 7), ('Kate', 'Martin', 1), ('Leo', 'Miller', 2)])
    conn.commit()


def display_students_by_city_id(conn):
    cursor = conn.cursor()

    while True:
        cursor.execute('SELECT id, title FROM cities')
        cities = cursor.fetchall()

        print("\nСписок городов:")
        for city in cities:
            print(f"{city[0]}. {city[1]}")

        city_id = int(input(
            "Вы можете отобразить список учеников по выбранному id города из перечня городов выше, для выхода из программы введите 0: "))
        if city_id == 0:
            break


        cursor.execute('''
            SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
            FROM students
            JOIN cities ON students.city_id = cities.id
            JOIN countries ON cities.country_id = countries.id
            WHERE cities.id = ?
        ''', (city_id,))
        students_info = cursor.fetchall()


        print(f"\nУченики в городе {cities[city_id - 1][1]}:")
        for student in students_info:
            print(
                f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")



connection = sqlite3.connect('hw8.db')

# create_countries_table(connection)
# insert_countries_data(connection)
#
# create_cities_table(connection)
# insert_cities_data(connection)
#
# create_students_table(connection)
# insert_students_data(connection)
# update_city_area(connection, 1, 2194)
# update_city_area(connection, 2, 605)
# update_city_area(connection, 3, 16410)
# update_city_area(connection, 4, 827)
# update_city_area(connection, 5, 767)
# update_city_area(connection, 6, 6341)
# update_city_area(connection, 7, 223)
display_students_by_city_id(connection)

connection.close()
