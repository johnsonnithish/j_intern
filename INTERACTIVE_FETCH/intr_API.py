from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from SERVICE.trial_ES import trial_ES

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/employees")
def emp_info(info: trial_ES = Depends(lambda: trial_ES())):
    return info.get_employees()

@app.get("/employees/filter")
def emp_info_filter(first_name: str, info: trial_ES = Depends(lambda: trial_ES())):
    return info.get_employees_by_first_name(first_name)
