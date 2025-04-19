import mysql.connector
from mysql.connector import Error

class DB_Tables:
    def __init__(self,host,user,pwd,port):
        self.host=host
        self.user=user
        self.pwd=pwd
        self.port=port
        self.connection=None

    def connect(self):
        try:
            self.connection=mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.pwd,
                port=self.port
                )
            if self.connection.is_connected():
                print("MySQL CONTAINER IS CONNECTED")

        except Error as e:
            print(f"Error Occured while attempting to connect : {e}")

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL CONTAINER IS DISCONNECTED")
    def disp_tables(self,query):
        if not self.connection or not self.connection.is_connected():
            print("NO ACTIVE CONNECTION")
            return None
        
j=DB_Tables("localhost", "j_intern", "internpass", 3305)

j.connect()
j.disconnect()
