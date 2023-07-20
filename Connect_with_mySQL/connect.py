import mysql.connector

class Connector:
    def __init__ (self):
        self.database = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'minhhvu11',
            database = 'mydatabase'
        )
        self.cursor = self.database.cursor()
        
    def insert(self, name, address):
        self.cursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", (name, address))
        self.database.commit()
        return True
    
    def update(self, name, address, new_name, new_address):
        self.cursor.execute(
            "UPDATE customers SET name = %s, address = %s WHERE name = %s AND address = %s", (new_name, new_address, name, address)
        )
        self.database.commit()
        return True
    
    def delete(self, name, address):
        self.cursor.execute(
            "DELETE FROM customers WHERE name = %s AND address = %s", (name, address)
        )
        self.database.commit()
        return True
    
def main():
    db = Connector()
    # db.insert('Vu', 'Dai Mo')
    # db.insert('Tung', 'Duc Dien')
    
    # db.update('Vu', 'Dai Mo', 'Vu', 'NTL')
    
    db.delete('Tung', 'Duc Dien')
    
if __name__ == '__main__':
    main()
