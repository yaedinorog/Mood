from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow these origins to access the API
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get('/api/sign_up')
async def