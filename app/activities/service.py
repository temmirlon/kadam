from app.activities.fake_data import fake_activities

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

    return {
        "activity_id": activity_id,
        "summary": f"Analysis for {activity['name']}. This is a fake AI analysis for now.",
        "positives": [
            "Good consistency during the session.",
            "Solid aerobic effort.",
        ],
        "improvements": [
            "Try to keep the effort more controlled in the second half.",
            "Add more context later: sleep, fatigue and weather.",
        ],
        "recommendation": "For the next similar session, start slightly easier and focus on stable pacing.",
    }