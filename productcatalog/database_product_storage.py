import sqlite3
from productcatalog.product_storage import ProductStorage
from productcatalog.product import Product


class SQLiteProductStorage(ProductStorage):
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                uuid TEXT PRIMARY KEY,
                name TEXT,
                description TEXT,
                price REAL,
                online BOOLEAN
            )
        ''')
        self.conn.commit()

    def add_product(self, product):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO products (uuid, name, description, price, online)
            VALUES (?, ?, ?, ?, ?)
        ''', (
        product.get_uuid(), product.get_name(), product.get_desc(), product.get_price(), product.get_online()))
        self.conn.commit()

    def get_all_products(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM products')
        rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append(row[1:])
        return products

    def get_product_by_uuid(self, uuid):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM products WHERE uuid = ?', (uuid,))
        row = cursor.fetchone()
        if row:
            uuid, name, description, price, online = row
            return Product(uuid, name, description, price, online)
        else:
            return None

    def delete_product_by_uuid(self, uuid):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM products WHERE uuid = ?', (uuid,))
        self.conn.commit()

    def update_product(self, product):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE products
            SET name = ?, description = ?, price = ?, online = ?
            WHERE uuid = ?
        ''', (
        product.get_name(), product.get_desc(), product.get_price(), product.get_online(), product.get_uuid()))
        self.conn.commit()

    def get_all_published_products(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM products WHERE online = 1')
        rows = cursor.fetchall()
        products = []
        for row in rows:
            uuid, name, description, price, online = row
            products.append(Product(uuid, name, description, price, online))
        return products

    def close(self):
        self.conn.close()
