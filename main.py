from fastapi import FastAPI
from v1.routers import attendees
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Routers
app.include_router(attendees.router)

origins = [
    "http://localhost:8080"
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