import mysql.connector
from mysql.connector import Error

class DB_Tables:
    def __init__(self,host,user,pwd,database):
        self.host=host
        self.user=user
        self.pwd=pwd
        self.database=database
        self.connection=None

    def connect(self):
        try:
            self.connection=mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.pwd,
                database=self.database
                )
            if self.connection.is_connected():
                print("DATABASE IS CONNECTED")

        except Error as e:
            print(f"Error occured while attempting to connect : {e}")

    def disconnect(self):
        if self.connection or self.connection.is_connected():
            self.connection.close()
            print("DATABASE IS DISCONNECTED")
    def disp_tables(self,query):
        if not self.connection or not self.connection.is_connected():
            print("NO ACTIVE CONNECTION")
            return None

        try:
            cursor= self.connection.cursor()
            cursor.execute(query)
            results= cursor.fetchall()
            return results

        except Error as e:
            print(f"ERROR OCCURED DURING QUERY : {e}")



if __name__ == "__main__":

    j=DB_Tables("localhost", "root", "CarpeDiem0903", "book_shop")

    j.connect()
    output=j.disp_tables("DESC books")
    if output:
        for n,i in enumerate(output,start=1):
            print(f"{n} {i}")
    j.disconnect()
