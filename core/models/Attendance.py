from pydantic import BaseModel
from typing import List

class Attendance(BaseModel):
    is_attending: bool
    name: str 
    attendees_quantity: int 
    message: str | str = ""

class AttendanceCollection(BaseModel):
    attendance_list: List[Attendance]