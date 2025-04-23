import mysql.connector
from mysql.connector import Error
class DBService:
    def __init__(self,host,database,user,port,password):
        self.host=host
        self.database=database
        self.user=user
        self.port=port
        self.password=password
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
        
