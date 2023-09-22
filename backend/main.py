import sys
import os

# Add the path to your project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from fastapi import FastAPI
from api.routes import api_router  # Import the router from your routes.py file
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(api_router, prefix="/api")

# Define a list of allowed origins (replace with your frontend's origin)
origins = ["http://localhost:3000"]  # Add your frontend's URL here

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[
        "*"
    ],  # You can specify specific HTTP methods (e.g., ["GET", "POST"]) if needed
    allow_headers=["*"],  # You can specify specific headers if needed
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
