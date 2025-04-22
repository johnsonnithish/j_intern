from fastapi import FastAPI, Query
from typing import List, Dict
import mysql.connector
from mysql.connector import Error

query_all = """
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
        LEFT JOIN emp_register m ON e.reporting_to_id = m.id;
        """
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
app = FastAPI()

@app.get("/")
def read_root():
    return {"TSK028"} 

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='35.154.151.12',
            port=5501,
            database='portal_db_18_10_24',
            user='johnsonm',
            password='nQ*{i~1XeY1N0('
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

@app.get("/employees", response_model=List[Dict])
def get_employees():
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query_all)
        results = cursor.fetchall()
        return results 
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
@app.get("/employees/filter", response_model=List[Dict])
def get_employees_by_first_name(first_name: str = Query(..., description="First name to filter")):
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
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
