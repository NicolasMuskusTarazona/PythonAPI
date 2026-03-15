from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException

async def custom_http_exception_handler(request: Request, exc: HTTPException):

    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):

    return JSONResponse(
        status_code=422,
        content={
            "error": "All input fields are required (name, geass, affiliation, image, etc...)."
        }
    )


async def generic_exception_handler(request: Request, exc: Exception):

    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
        # watch the mistake 
        # content={"error": "Internal server error","details": str(exc)}
    )