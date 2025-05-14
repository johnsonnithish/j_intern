from fastapi import FastAPI, Depends
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TSK031.emp import Employees

app = FastAPI()

def get_employees():
    return Employees()

@app.get("/")
def read_root(info: Employees = Depends(get_employees)):
    return info.emp_info()

@app.get("/genderdiv")
def gender_div(info: Employees = Depends(get_employees)):
    return info.gender_div()