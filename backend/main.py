from fastapi import FastAPI
from api.routes import api_router  # Import the router from your routes.py file

app = FastAPI()

app.include_router(api_router, prefix="/api")