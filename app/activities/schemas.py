from pydantic import BaseModel

# short version of activity
class ActivitySummary(BaseModel):
    id: int
    name: str
    sport_type: str
    distance_km: float
    moving_time_minutes: int

# detailed version of activity
class ActivityDetail(ActivitySummary):
    average_pace: str
    average_heartrate: int | None = None
    max_heartrate: int | None = None
    total_elevation_gain: float | None = None
    strava_url: str | None = None
