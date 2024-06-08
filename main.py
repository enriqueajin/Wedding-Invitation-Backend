from fastapi import FastAPI
from v1.routers import attendees
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Routers
app.include_router(attendees.router)

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:8081",
    "https://enriqueajin.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}