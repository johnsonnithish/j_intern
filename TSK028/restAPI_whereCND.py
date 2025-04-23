from fastapi import FastAPI, Query ,Depends
from typing import List, Dict
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from SERVICE.EmployeeService import  EmployeeServiceFilter

app = FastAPI()
@app.get("/")
def read_root():
    return {"TSK028"} 

def get_info_filter():
    return EmployeeServiceFilter()


@app.get("/employees/filter", response_model=List[Dict])
def emp_info_filter(first_name: str, info: EmployeeServiceFilter=Depends(get_info_filter)):
    return info.get_employees_by_first_name(first_name)