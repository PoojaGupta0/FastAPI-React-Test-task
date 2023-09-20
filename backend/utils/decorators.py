from typing import Callable
from fastapi import FastAPI, HTTPException
from pydantic import ValidationError

# Define a function to handle errors
def handle_errors(handler: Callable):
    async def wrapper(*args, **kwargs):
        try:
            return await handler(*args, **kwargs)
        except SyntaxError as e:
            raise HTTPException(status_code=400, detail=f"Syntax Error: {e}")
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Value Error: {e}")
        except ValidationError as e:
            raise HTTPException(status_code=404, detail=f"Validation Error: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")

    return wrapper