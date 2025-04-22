import mysql.connector
from mysql.connector import Error
from fastapi import FastAPI
from typing import List, Dict

def create_connection():
    """Create a database connection."""
    try:
        connection = mysql.connector.connect(
            host='35.154.151.12',
            database='portal_db_18_10_24',
            user='johnsonm',
            port=5501,
            password='nQ*{i~1XeY1N0('
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None
    
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to the TSK025 Employee API!"}
@app.get("/employees", response_model=List[Dict])
def get_employees():
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
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
        LEFT JOIN emp_register m ON e.reporting_to_id=m.id;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        return results 
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
