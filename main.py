from fastapi import FastAPI
from v1.routers import attendees

app = FastAPI()

# Routers
app.include_router(attendees.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}