from fastapi import FastAPI ,Depends
from typing import List, Dict
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from SERVICE.EmployeeService import EmployeeService

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
app = FastAPI()
@app.get("/")
def read_root():
    return "TSK026 REST API"

def get_info():
    return EmployeeService(query)
@app.get("/employees")
def emp_info(info: EmployeeService=Depends(get_info)):
    return info.get_employees()