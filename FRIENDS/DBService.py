import mysql.connector
from mysql.connector import Error

class DBService:
    def __init__(self):
        self.host="localhost",
        self.port=3306,
        self.user="root",
        self.password="root"
        self.database="friends"
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
    def get_all(self):
        try:
            connection = self.create_connection()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT F_Name as 'FIRST NAME', L_Name as 'LAST NAME', Alias as 'NICK NAME', About as 'ABOUT' from frnds_info"
            cursor.execute(query)   
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    def get_f_name(self,first_name: str):
        try:
            connection = self.create_connection()
            cursor = connection.cursor(dictionary=True)
            query_filter = "SELECT F_Name as 'FIRST NAME', L_Name as 'LAST NAME', Alias as 'NICK NAME', About as 'ABOUT' from frnds_info WHERE F_Name = %s"
            cursor.execute(query_filter, (first_name,)) 
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    def get_l_name(self,last_name: str):
        try:
            connection = self.create_connection()
            cursor = connection.cursor(dictionary=True)
            query_filter = "SELECT F_Name as 'FIRST NAME', L_Name as 'LAST NAME', Alias as 'NICK NAME', About as 'ABOUT' from frnds_info WHERE L_Name = %s"
            cursor.execute(query_filter, (last_name,)) 
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    def get_alias(self,alias: str):
        try:
            connection = self.create_connection()
            cursor = connection.cursor(dictionary=True)
            query_filter = "SELECT F_Name as 'FIRST NAME', L_Name as 'LAST NAME', Alias as 'NICK NAME', About as 'ABOUT' from frnds_info WHERE Alias = %s"
            cursor.execute(query_filter, (alias,)) 
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()  