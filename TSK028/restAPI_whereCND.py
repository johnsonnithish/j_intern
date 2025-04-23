from fastapi import FastAPI, Query ,Depends
from typing import List, Dict
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DBService import DBService ,Error
from TSK026.restAPI_JSPL import EmployeeService

conn_details= {
    'host':'35.154.151.12',
    'database':'portal_db_18_10_24',
    'user':'johnsonm',
    'port':5501,
    'password':'nQ*{i~1XeY1N0('
}

ge=EmployeeService(*conn_details.values())
app = FastAPI()
@app.get("/")
def read_root():
    return {"TSK028"} 

class EmployeeServiceFilter(DBService):
    def __init__(self,host,database,user,port,password):
        super().__init__(host,database,user,port,password)
    def get_employees(self):
        return ge.get_employees()
    def get_employees_by_first_name(self,first_name: str = Query(...,)):
        try:
            connection = self.create_connection()
            cursor = connection.cursor(dictionary=True)
            query_filter= """
            SELECT
                e.first_name AS "First Name",
                e.last_name AS "Last Name",
                e.date_of_birth AS "DOB",
                e.date_of_joining AS "DOJ",
                d.name AS "Department Name",
                p.name AS "Project Name",
                des.name AS "Designation",
                CONCAT(m.first_name, ' ', m.last_name) AS "Reporting Manager Name"
            FROM emp_register e
            LEFT JOIN dept_master d ON e.department_id = d.id
            LEFT JOIN project_master p ON e.project_id = p.id
            LEFT JOIN designation_master des ON e.designation_id = des.id
            LEFT JOIN emp_register m ON e.reporting_to_id = m.id
            WHERE e.first_name = %s;
            """
            cursor.execute(query_filter, (first_name,))
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


def get_info():
    return EmployeeServiceFilter(*conn_details.values())

        
@app.get("/employees", response_model=List[Dict])
def emp_info(info: EmployeeServiceFilter=Depends(get_info)):
    return info.get_employees()
@app.get("/employees/filter", response_model=List[Dict])
def emp_info_filter(first_name: str, info: EmployeeServiceFilter=Depends(get_info)):
    return info.get_employees_by_first_name(first_name)