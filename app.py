from fastapi import FastAPI
from routes.users import user
from routes.problems import problems

app = FastAPI(
    openapi_tags=[{
        "name": "users",
        "description": "users routes"
    },
    {
        "name": "problems",
        "description": "problems routes"
    }]
)
app.include_router(user)
app.include_router(problems)
