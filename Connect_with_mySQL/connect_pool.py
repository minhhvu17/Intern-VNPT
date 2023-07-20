import mysql.connector.pooling

class ConnectorPooling:
    def __init__(self):
        pass
    
    def connection_pool(self):
        connector = mysql.connector.pooling.MySQLConnectionPool(
            pool_name = "my_pool",
            host = 'localhost',
            user = 'root',
            password = 'minhhvu11',
            database = 'mydatabase',
            pool_size = 5
        )
        return connector
    
    def insert(self, connection_pool, name, address):
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        connection = connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (name, address))
        connection.commit()
        cursor.close()
        connection.close()
        
    def delete(self, connection_pool, name, address):
        sql = "DELETE FROM customers WHERE name = %s AND address = %s"
        connection = connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (name, address))
        connection.commit()
        cursor.close()
        connection.close()
    
    def update(self, connection_pool, name, address, new_name, new_address):
        sql = "UPDATE customers SET name = %s, address = %s WHERE name = %s AND address = %s"
        connection = connection_pool.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (new_name, new_address, name, address))
        connection.commit()
        cursor.close()
        connection.close()
        

def main():
    db = ConnectorPooling()
    connection_pooling = db.connection_pool()
    db.delete(connection_pooling, "Minh", "Xuan Thuy")
    
    # db.delete(connection_pooling, 'A', 'B')
    

if __name__ == "__main__":
    main()