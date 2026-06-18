from app.activities.fake_data import fake_activities
from app.analysis.service import generate_fake_activity_analysis

def get_all_activities():
    return fake_activities

def get_activity_by_id(activity_id: int):
    for acitivity in fake_activities:
        if acitivity["id"] == activity_id:
            return acitivity
    return None

def get_activity_analysis(activity_id: int):
    activity = get_activity_by_id(activity_id)

    if activity is None:
        return None

    return generate_fake_activity_analysis(activity)