from fastapi import FastAPI
from routes.user import user
from routes.character import character
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException
from Handler.CustomErrorHandler import (custom_http_exception_handler,validation_exception_handler,generic_exception_handler)

app = FastAPI(
    title="FastAPI and Mongodb",
    description="Nicolas Muskus",
    version="0.0.1",
)

app.add_exception_handler(HTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(user)
app.include_router(character)