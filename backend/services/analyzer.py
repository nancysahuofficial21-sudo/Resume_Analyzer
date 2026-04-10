def analyze_resume(text):

    text_lower = text.lower()

    # ATS SCORE (based on length)
    ats_score = min(len(text) / 1000, 1) * 100

    # KEYWORD SCORE
    keywords = [
        "python", "java", "sql", "machine learning",
        "project", "experience", "team", "leadership"
    ]

    found = 0
    for k in keywords:
        if k in text_lower:
            found += 1

    keyword_score = (found / len(keywords)) * 100

    # OVERALL SCORE
    overall = (ats_score + keyword_score) / 2

    return {
        "ats_score": int(ats_score),
        "keyword_match_score": int(keyword_score),
        "overall_score": int(overall),
        "strengths": ["Good content length"],
        "weaknesses": ["Add more measurable achievements"],
        "missing_keywords": [k for k in keywords if k not in text_lower]
    }