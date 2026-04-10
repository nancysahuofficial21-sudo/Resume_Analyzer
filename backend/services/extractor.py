def extract_info(text):

    import re

    # EMAIL
    email = re.findall(r'\S+@\S+', text)

    # PHONE
    phone = re.findall(r'\+?\d[\d -]{8,}\d', text)

    # NAME (simple guess: first line)
    lines = text.split("\n")
    name = lines[0] if lines else ""

    # SKILLS
    skill_keywords = [
        "python", "java", "c++", "sql", "machine learning",
        "deep learning", "react", "node", "django", "flask"
    ]

    skills = []
    for word in text.lower().split():
        if word in skill_keywords:
            skills.append(word)

    return {
        "name": name,
        "email": email[0] if email else "",
        "phone": phone[0] if phone else "",
        "skills": list(set(skills)),
        "education": [],
        "experience": [],
        "projects": []
    }