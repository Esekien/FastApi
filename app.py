from fastapi import FastAPI
from routes.users import user
from routes.problems import problems

app = FastAPI()
app.include_router(user)
app.include_router(problems)
