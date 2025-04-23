import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from SERVICE.DBService import DBService ,Error
from fastapi import Query
class EmployeeService(DBService):
    def __init__(self,query):
        super().__init__()
        self.query=query
    def get_employees(self):
        try:
            connection = self.create_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(self.query)
            results = cursor.fetchall()
            return results 
        except Error as e:
            print(f"Error: {e}")
            
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


class EmployeeServiceFilter(DBService):
    def __init__(self,query):
        super().__init__()
        self.query=query
    def get_employees_by_first_name(self,first_name: str):
        try:
            connection = self.create_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(self.query, (first_name,))
            results = cursor.fetchall()
            return results

        except Error as e:
            print(f"Error: {e}")
            return {"error": str(e)}

        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")