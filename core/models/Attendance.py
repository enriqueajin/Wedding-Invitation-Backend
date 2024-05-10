from pydantic import BaseModel, Field
from typing import List, Optional

class Attendance(BaseModel):
    id: Optional[str] = None
    name: str 
    attendees_quantity: int 
    message: str | str = ""

class AttendanceCollection(BaseModel):
    attendance_list: List[Attendance]