import asyncio
from functools import wraps
from typing import Callable
from fastapi import HTTPException


def exception_handler(func: Callable):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:

            return asyncio.run(func(*args, **kwargs))

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return wrapper
