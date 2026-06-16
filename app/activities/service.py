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

def get_all_activities():
    return fake_activities

def get_activity_by_id(activity_id: int):
    for acitivity in fake_activities:
        if acitivity["id"] == activity_id:
            return acitivity
    return None