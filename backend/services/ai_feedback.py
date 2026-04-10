def generate_feedback(text):

    improvements = []
    suggestions = []

    if "project" not in text.lower():
        improvements.append("Add more project details")

    if len(text) < 300:
        improvements.append("Resume too short")

    suggestions.append("Built scalable application using modern tools")

    return {
        "improvements": improvements,
        "suggested_bullet_points": suggestions,
        "formatting_tips": ["Use action verbs"]
    }