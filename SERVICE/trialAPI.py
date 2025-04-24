from fastapi import FastAPI, Query ,Depends
from typing import List, Dict
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from SERVICE.trial_ES import trial_ES

app = FastAPI()
@app.get("/")
def read_root():
    return "trial" 


@app.get("/employees")
def emp_info(info: trial_ES=Depends(lambda: trial_ES())):
    return info.get_employees()

@app.get("/employees/filter")
def emp_info_filter(first_name: str, info: trial_ES=Depends(lambda: trial_ES())):
    return info.get_employees_by_first_name(first_name)