from app.analysis.ai.fake import FakeAIProvider
from app.analysis.prompts import build_training_analysis_prompt


def build_activity_summary(activity: dict) -> str:
    return (
        f"Activity: {activity['name']}\n"
        f"Sport type: {activity['sport_type']}\n"
        f"Distance: {activity['distance_km']} km\n"
        f"Moving time: {activity['moving_time_minutes']} min\n"
        f"Average pace: {activity['average_pace']}\n"
        f"Average heart rate: {activity.get('average_heartrate', 'N/A')} bpm\n"
        f"Max heart rate: {activity.get('max_heartrate', 'N/A')} bpm\n"
        f"Elevation gain: {activity.get('total_elevation_gain', 'N/A')} m\n"
    )


def generate_fake_activity_analysis(activity: dict):
    activity_summary = build_activity_summary(activity)
    prompt = build_training_analysis_prompt(activity_summary)

    ai_provider = FakeAIProvider()
    ai_response = ai_provider.generate_text(prompt)

    return {
        "activity_id": activity["id"],
        "summary": ai_response,
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