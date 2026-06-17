from fastapi import APIRouter, HTTPException

from app.activities.schemas import ActivityDetail, ActivitySummary
from app.activities.service import get_activity_by_id, get_all_activities

router = APIRouter(prefix="/activities", tags=["activities"])


@router.get("/", response_model=list[ActivitySummary])
def get_activities():
    return get_all_activities()

@router.get("/{activity_id}", response_model=ActivityDetail)
def get_activity(activity_id: int):
    activity = get_activity_by_id(activity_id)

    if activity == None:
        raise HTTPException(status_code=404, detail="Activity not found..")
    
    return activity