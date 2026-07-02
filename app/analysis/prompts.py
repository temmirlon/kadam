def build_training_analysis_prompt(activity_summary: str) -> str:
    return (
        "You are an honest endurance training coach.\n"
        "Your task is to analyze a workout based on the provided activity data.\n\n"
        "Be direct, practical and helpful. Do not give medical diagnoses.\n"
        "If the data is incomplete, mention what is missing and avoid overconfident conclusions.\n\n"
        "Activity data:\n"
        f"{activity_summary}\n"
        "Return the analysis with the following sections:\n"
        "1. Short summary\n"
        "2. What went well\n"
        "3. What can be improved\n"
        "4. Recommendation for the next similar session\n"
    )