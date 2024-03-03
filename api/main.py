from fastapi import FastAPI
from .routes import users

app = FastAPI()

print(app)

app.include_router(users.router)