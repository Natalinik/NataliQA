import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r"D:\PrometheusQA\NataliQA" + r"\become_qa_auto.db")
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        return records
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record
    
    def get_tables(self):
        query = "SELECT name FROM sqlite_schema WHERE type ='table'"
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        return records

    def insert_user(self, customer_id: int, name: str, address: str, city: str, postalCode: str, country: str):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
            VALUES ({customer_id}, '{name}', '{address}', '{city}', '{postalCode}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def select_user_by_id(self, customer_id: int):
        query = f"SELECT id, name, address, city, postalCode, country FROM customers WHERE id = {customer_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchone()

        return record
    
    def update_user_name_by_id(self, customer_id: int, name: str):
        query = f"UPDATE customers SET name = '{name}' WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_user_by_id(self, customer_id):
        query = f"DELETE FROM customers WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_user_addresses_by_postalCode(self, postalCode: str):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE postalCode = '{postalCode}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        
        return record
