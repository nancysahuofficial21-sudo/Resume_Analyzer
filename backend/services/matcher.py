import re

def extract_keywords(text):
    # Remove symbols
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text.lower())

    # Common tech keywords (you can expand this)
    skill_keywords = [
        "python", "java", "c++", "sql", "machine learning",
        "deep learning", "nlp", "django", "flask", "react",
        "node", "api", "aws", "docker", "kubernetes",
        "pandas", "numpy", "data analysis"
    ]

    found = []

    for skill in skill_keywords:
        if skill in text:
            found.append(skill)

    return list(set(found))


def match_resume(text, job_desc):

    resume_skills = extract_keywords(text)
    job_skills = extract_keywords(job_desc)

    matched = []
    missing = []

    for skill in job_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    # Score calculation
    if len(job_skills) == 0:
        score = 0
    else:
        score = int((len(matched) / len(job_skills)) * 100)

    return {
        "match_percentage": score,
        "matched_skills": matched,
        "missing_skills": missing
    }