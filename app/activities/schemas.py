from pydantic import BaseModel

class Activity(BaseModel):
    id: int
    name: str
    sport_type: str
    distance_km: float
    moving_time_minutes: int