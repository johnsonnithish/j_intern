import mysql.connector
from mysql.connector import Error

class DBService:
    def __init__(self):
        self.host='localhost'
        self.database='family'
        self.user='root'
        self.port=3306
        self.password='CarpeDiem0903'
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
            query = "SELECT f_name AS 'FIRST NAME', l_name AS 'LAST NAME', age AS Age, D_O_B as 'Date of Birth' FROM fam_deet"
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
            query_filter = "SELECT f_name AS 'FIRST NAME', l_name AS 'LAST NAME', age AS Age, D_O_B as 'Date of Birth' FROM fam_deet WHERE f_name = %s"
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
            query_filter = "SELECT f_name AS 'FIRST NAME', l_name AS 'LAST NAME', age AS Age, D_O_B as 'Date of Birth' FROM fam_deet WHERE l_name = %s"
            cursor.execute(query_filter, (last_name,)) 
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()