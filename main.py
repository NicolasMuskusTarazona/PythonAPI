from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
import os
import uvicorn

from routes.user import user
from routes.character import character
from routes.auth import auth

from Handler.CustomErrorHandler import (
    custom_http_exception_handler,
    validation_exception_handler,
    generic_exception_handler
)

from utils.create_admin import create_admin

app = FastAPI(
    title="CodeGeass API",
    description="API desarrollada por Nicolas Muskus con FastAPI y MongoDB",
    version="1.0.0",
)

# Endpoint 
@app.get("/")
def root():
    return {"message": "CodeGeass API running"}

# Custom Error Handlers
app.add_exception_handler(HTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# Crear admin si no existe
create_admin()

# ROUTERS
app.include_router(auth)
app.include_router(user)
app.include_router(character)

# Run local
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)