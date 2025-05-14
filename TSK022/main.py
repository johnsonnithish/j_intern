from fastapi import FastAPI
from TSK22.routers import users, items

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
