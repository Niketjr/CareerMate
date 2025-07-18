def recommend_based_on_skills(skills):
    """
    Very basic rule-based recommendation system.
    You can replace this with ML later.
    """
    recommendations = []

    job_map = {
        "Python": ["Backend Developer", "Data Analyst", "Automation Engineer"],
        "Django": ["Backend Developer"],
        "REST": ["API Developer", "Full-Stack Developer"],
        "React": ["Frontend Developer", "Full-Stack Developer"],
        "Machine Learning": ["ML Engineer", "Data Scientist"],
        "AWS": ["Cloud Engineer", "DevOps Engineer"],
        "SQL": ["Database Admin", "BI Analyst"]
    }

    for skill in skills:
        matched_jobs = job_map.get(skill, [])
        for job in matched_jobs:
            if job not in recommendations:
                recommendations.append(job)

    return recommendations
