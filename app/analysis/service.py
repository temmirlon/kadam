def generate_fake_activity_analysis(activity: dict):
    return {
        "activity_id": activity["id"],
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