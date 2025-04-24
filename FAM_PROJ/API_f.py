import fastapi
from fastapi import FastAPI, Query, Depends 
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from FAM_PROJ.DBService_f import DBService
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="FAM_PROJ/templates_f")

@app.get("/", response_class=HTMLResponse)
def root(request: fastapi.Request):
    return templates.TemplateResponse("fam.html", {"request": request})

@app.get("/family")
def family_info(info: DBService = Depends(lambda: DBService())):
    return info.get_all()

@app.get("/family/f_name")
def family_info_filter(first_name: str, info: DBService = Depends(lambda: DBService())):
    return info.get_f_name(first_name)

@app.get("/family/l_name")
def family_info_filter(last_name: str, info: DBService = Depends(lambda: DBService())):
    return info.get_l_name(last_name)
