from fastapi import FastAPI ,Depends
from typing import List, Dict
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from SERVICE.EmployeeService import EmployeeService
app = FastAPI()
@app.get("/")
def read_root():
    return "TSK026 REST API"

def get_info():
    return EmployeeService()
@app.get("/employees")
def emp_info(info: EmployeeService=Depends(get_info)):
    return info.get_employees()