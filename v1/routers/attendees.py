from fastapi import APIRouter
from core.database import client

router = APIRouter(
    prefix="/attendees",
    tags=["attendees"]
)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)