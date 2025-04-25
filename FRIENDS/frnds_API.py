import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from FRIENDS.DBService import DBService
from fastapi import FastAPI, Query, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="FRIENDS/templates")
app.mount("/static", StaticFiles(directory="FRIENDS/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("frnds.html", {"request": request})

@app.get("/friends")
def friends_info(info: DBService = Depends(lambda: DBService())):
    return info.get_all()

@app.get("/friends/first_name")
def get_friends_by_first_name(first_name: str, info: DBService = Depends(lambda: DBService())):
    return info.get_f_name(first_name)

@app.get("/friends/last_name")
def get_friends_by_last_name(last_name: str, info: DBService = Depends(lambda: DBService())):
    return info.get_l_name(last_name)

@app.get("/friends/alias")
def get_friends_by_alias(alias: str, info: DBService = Depends(lambda: DBService())):
    return info.get_alias(alias)