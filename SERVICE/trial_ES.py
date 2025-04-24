import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from SERVICE.DBService import DBService ,Error

query = """ SELECT
            e.first_name AS "First Name",
            e.last_name AS "Last Name",
            e.date_of_birth AS "DOB",
            e.date_of_joining AS "DOJ",
            d.name AS "Department Name",
            p.name AS "Project Name",
            des.name AS "Designation",
            CONCAT(m.first_name, ' ' , m.last_name) AS "Reporting Manager Name"
            FROM emp_register e
            LEFT JOIN dept_master d ON e.department_id=d.id
            LEFT JOIN project_master p ON e.project_id=p.id
            LEFT JOIN designation_master des ON e.designation_id=des.id
            LEFT JOIN emp_register m ON e.reporting_to_id=m.id
            """
class trial_ES(DBService):
    def __init__(self):
        super().__init__()
    def get_employees(self,query=query):
        try:
            connection = self.create_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query) 
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_employees_by_first_name(self,first_name: str):
        try:
            connection = self.create_connection()
            cursor = connection.cursor(dictionary=True)
            query_filter = query + " WHERE e.first_name = %s"
            cursor.execute(query_filter, (first_name,)) 
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()