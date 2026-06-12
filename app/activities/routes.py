from fastapi import APIRouter, HTTPException

from app.activities.schemas import Activity

router = APIRouter(prefix="/activities", tags=["activities"])

fake_activities = [
    {
        "id": 1,
        "name": "Morning Run",
        "sport_type": "Run",
        "distance_km": 8.2,
        "moving_time_minutes": 45,
    },
    {
        "id": 2,
        "name": "Evening Ride",
        "sport_type": "Ride",
        "distance_km": 32.5,
        "moving_time_minutes": 78,
    },
]

@router.get("/", response_model=list[Activity])
def get_activities():
    return fake_activities

@router.get("/{activity_id}", response_model=Activity)
def get_activity(activity_id: int):
    for activity in fake_activities:
        if activity["id"] == activity_id:
            return activity
        
    raise HTTPException(status_code=404, detail="Activity not found..")