from fastapi import FastAPI
from fastapi.routing import APIRouter

app = FastAPI()
@app.get("/")
def read_root():
    return {"WORKS"}
# this is one module that contains all the routes regd users
user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get("/")
def read_user():
    return [{"user": "John Doe", "age": 30}, {"user": "Jane Doe", "age": 25}]

@user_router.get("/{user_id}")
def read_user_by_id(user_id: int):
    return {"user": f"User {user_id}", "age": 30 + user_id}



# this is another module that contains all the routes regd info
info_router = APIRouter(prefix="/info", tags=["info"])

@info_router.get("/")
def read_info():
    return {"info": "INFORMATION"}

@info_router.get("/{info_id}")
def read_info_by_id(info_id: int):
    return {"info": f"Info {info_id}", "details": "Details about info"}

app.include_router(user_router)
app.include_router(info_router)
# these lines are used to include the routers in the main app

# this can also be done by having multiple files and importing them in the main file