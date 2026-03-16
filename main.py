from fastapi import FastAPI
from routes.user import user
from routes.character import character
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException
from Handler.CustomErrorHandler import (
    custom_http_exception_handler,
    validation_exception_handler,
    generic_exception_handler
)
from utils.create_admin import create_admin
from routes.auth import auth
import os
import uvicorn

app = FastAPI(
    title="FastAPI and Mongodb",
    description="Nicolas Muskus",
    version="0.0.1",
)

# CustomErrorHandler
app.add_exception_handler(HTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# Crear admin
create_admin()

# ROUTERS
app.include_router(user)
app.include_router(character)
app.include_router(auth)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)