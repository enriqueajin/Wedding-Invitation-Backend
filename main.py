from fastapi import FastAPI
from v1.routers import attendees
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
handler = Mangum(app)

# Routers
app.include_router(attendees.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}