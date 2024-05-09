def individual_serial(attendance) -> dict:
    return {
        "id": str(attendance["_id"]),
        "name": attendance["name"],
        "attendees_quantity": int(attendance["attendees_quantity"]),
        "message": attendance["message"]
    }

def list_serial(attendance_entries) -> list:
    return[individual_serial(attendance) for attendance in attendance_entries]