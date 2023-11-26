import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_products(conn, products):
    sql = '''INSERT INTO products 
    (product_title, price, quantity)
    VALUES (?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)



sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT NOT NULL DEFAULT 0.0 CHECK(price >= 0 AND price <= 999999999.99),
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def update_products_by_id(conn, products):
    sql = '''UPDATE products SET quantity = ? 
    WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_products_price_by_id(conn, products):
    sql = '''UPDATE products SET price = ? 
    WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_products(conn, id):
    sql = '''DELETE from products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_products_by_price(conn, price_limit, quantity):
    sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (price_limit, quantity))
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_name(conn, product_title):
    sql = '''SELECT * FROM products WHERE product_title LIKE ? '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + product_title + '%',))
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

connection = create_connection('hw.db')
if connection is not None:
    print('Successfully connected to DB!')
    # create_table(connection, sql_to_create_products_table)
    # insert_products(connection, ('Футбольный мяч', 1000, 20))
    # insert_products(connection, ('Баскетбольный мяч', 1500, 15))
    # insert_products(connection, ('Теннисная ракетка', 2000, 10))
    # insert_products(connection, ('Беговая дорожка', 10000, 5))
    # insert_products(connection, ('Велосипед', 8000, 12))
    # insert_products(connection, ('Гантели ', 500, 30))
    # insert_products(connection, ('Йогамат', 1000, 25))
    # insert_products(connection, ('Боксерские перчатки ', 2000, 8))
    # insert_products(connection, ('Плавки', 800, 18))
    # insert_products(connection, ('Волейбольный мяч', 1200, 15))
    # insert_products(connection, ('Лыжи', 5000, 7))
    # insert_products(connection, ('Боксерская груша', 1500, 10))
    # insert_products(connection, ('Бадминтонный комплект', 1500, 20))
    # insert_products(connection, ('Фитнес-груша', 2500, 5))
    # insert_products(connection, ('Гимнастический коврик', 800, 30))
    # select_all_products(connection)
    # update_products_by_id(connection, (6, 4))
    # update_products_price_by_id(connection, (6000, 5))
    # delete_products(connection, 9)
    # select_products_by_price(connection,3000, 10)
    # select_products_by_name(connection, 'мяч')

    connection.close()