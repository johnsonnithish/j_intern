import mysql.connector
from mysql.connector import Error
class DBService:
    def __init__(self):
        self.host='35.154.151.12'
        self.database="portal_db_18_10_24"
        self.user="johnsonm"
        self.port=5501
        self.password="nQ*{i~1XeY1N0("
        self.connection = None
    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                port=self.port,
                password=self.password
            )
            if connection.is_connected():
                print("Connection to MySQL DB successful")
                return connection
        except Error as e:
            print(f"Error: {e}")
            return None
        
