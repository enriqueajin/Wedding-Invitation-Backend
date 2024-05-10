from fastapi import APIRouter, HTTPException
from pymongo import ReturnDocument
from core.database import attendance_collection
from core.models.Attendance import Attendance, AttendanceCollection
from fastapi.responses import Response
from core.schemas.Attendance import list_serial, individual_serial
from bson.objectid import ObjectId

router = APIRouter(
    prefix="/attendees",
    tags=["attendees"]
)

@router.get(
    "/",
    status_code=200,
    response_model=AttendanceCollection,
    response_model_by_alias=False
)
async def get_attendance():
    """ Get the attendance list
    
    Returns: AttendanceCollection object (list of Attendance)
    """
    attendance_list = list_serial(attendance_collection.find())
    return AttendanceCollection(attendance_list=attendance_list)

@router.get(
    "/{id}",
    status_code=200,
    response_model=Attendance,
    response_model_by_alias=False
)
async def get_attendance_entry_by_id(id: str):
    """ Get a single entry of the attendance list
    
    Returns: Attendance object
    """
    if ObjectId.is_valid(id):
        attendance_entry = individual_serial(attendance_collection.find_one({"_id": ObjectId(id)}))

        if attendance_entry is not None:
            return attendance_entry

    raise HTTPException(status_code=404, detail=f"Attendance entry with ID: {id} not found")


@router.post(
    "/",
    status_code=201,
    response_model=Attendance,
    response_model_by_alias=False
)
async def post_attendance_entry(attendance: Attendance):
    """ Insert an attendance entry into the database
    
    Returns: Attendance object
    """
    # Insert the attendance entry
    new_entry = attendance_collection.insert_one(dict(attendance))

    # Get the document just inserted
    inserted_document = await get_attendance_entry_by_id(new_entry.inserted_id)

    if inserted_document is not None:
        return inserted_document
    
    raise HTTPException(status_code=404, detail=f"Attendance entry with ID: {id} not inserted.")



@router.put(
    "/{id}",
    status_code=200,
    response_model=Attendance,
    response_model_by_alias=False
)
async def update_attendance_entry(id: str, attendance: Attendance):
    """ Update an existant attendance entry
    
    Returns: Attendance object
    """
    if ObjectId.is_valid(id):
        updated_entry = individual_serial(attendance_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(attendance)}, return_document=ReturnDocument.AFTER))

        if updated_entry is not None:
            return updated_entry
        
    raise HTTPException(status_code=404, detail=f"Attendance entry with ID: {id} not updated.")

@router.delete(
    "/{id}",
    status_code=200,
)
async def delete_attendance_entry(id: str):
    """ Delete an attendance entry
    
    Returns: message (string)
    """
    if ObjectId.is_valid(id):
        doc_deleted = attendance_collection.delete_one({"_id": ObjectId(id)})

        if doc_deleted.deleted_count == 1:
            return Response(status_code=200)

    raise HTTPException(status_code=404, detail=f"Attendance entry with ID: {id} not deleted.")