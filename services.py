import asyncio
from functools import wraps
from typing import Callable
from fastapi import HTTPException


def exception_handler(func: Callable) -> Callable:
    """
    Handle exceptions and return an HTTP error response.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> dict | HTTPException:
        try:

            return asyncio.run(func(*args, **kwargs))

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return wrapper
