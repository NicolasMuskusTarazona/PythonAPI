from fastapi import FastAPI
from routes.user import user


app = FastAPI(
    title="FastAPI and Mongodb",
    description="Nicolas Muskus",
    version="0.0.1",
)

app.include_router(user)