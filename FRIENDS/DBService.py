import mysql.connector
from mysql.connector import Error

class DBService:
    def __init__(self):
        self.host = "mysql-db"
        self.port = 3306
        self.user = "john"
        self.password = "johnspassword"
        self.database = "friends"
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
        connection = self.create_connection()
        if not connection:
            return {"error": "Database connection failed"}
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT F_Name AS 'FIRST NAME',
                       L_Name AS 'LAST NAME',
                       Alias AS 'NICK NAME',
                       About AS 'ABOUT',
                       image
                FROM frnds_info
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
            return {"error": str(e)}
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_f_name(self, first_name: str):
        connection = self.create_connection()
        if not connection:
            return {"error": "Database connection failed"}
        try:
            cursor = connection.cursor(dictionary=True)
            query_filter = """
                SELECT F_Name AS 'FIRST NAME', 
                       L_Name AS 'LAST NAME', 
                       Alias AS 'NICK NAME', 
                       About AS 'ABOUT', 
                       image 
                FROM frnds_info 
                WHERE F_Name = %s
            """
            cursor.execute(query_filter, (first_name,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
            return {"error": str(e)}
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_l_name(self, last_name: str):
        connection = self.create_connection()
        if not connection:
            return {"error": "Database connection failed"}
        try:
            cursor = connection.cursor(dictionary=True)
            query_filter = """
                SELECT F_Name AS 'FIRST NAME', 
                       L_Name AS 'LAST NAME', 
                       Alias AS 'NICK NAME', 
                       About AS 'ABOUT', 
                       image 
                FROM frnds_info 
                WHERE L_Name = %s
            """
            cursor.execute(query_filter, (last_name,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
            return {"error": str(e)}
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_alias(self, alias: str):
        connection = self.create_connection()
        if not connection:
            return {"error": "Database connection failed"}
        try:
            cursor = connection.cursor(dictionary=True)
            query_filter = """
                SELECT F_Name AS 'FIRST NAME', 
                       L_Name AS 'LAST NAME', 
                       Alias AS 'NICK NAME', 
                       About AS 'ABOUT', 
                       image 
                FROM frnds_info 
                WHERE Alias = %s
            """
            cursor.execute(query_filter, (alias,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
            return {"error": str(e)}
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
