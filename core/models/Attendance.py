from pydantic import BaseModel

class Attendance(BaseModel):
    name: str
    attendees_number: int
    message: str | str = ""