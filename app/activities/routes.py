from fastapi import APIRouter

from app.activities.schemas import Activity

router = APIRouter(prefix="/activities", tags=["activities"])

@router.get("/", response_model=list[Activity])
def get_activities():
    return [
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