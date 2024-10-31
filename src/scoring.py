# scoring.py

import re

def weighted_score(skills_score, experience_score, soft_skills_score, weights):
    # Calculate weighted score
    final_score = (
        skills_score * weights['skills'] +
        experience_score * weights['experience'] +
        soft_skills_score * weights['soft_skills']
    )
    return round(final_score, 2)

def extract_scores_from_analysis(analysis_text):
    # Extract numerical scores from analysis text (mockup extraction method)
    skills_score = int(re.search(r"Skills Score: (\d+)", analysis_text).group(1))
    experience_score = int(re.search(r"Experience Score: (\d+)", analysis_text).group(1))
    soft_skills_score = int(re.search(r"Soft Skills Score: (\d+)", analysis_text).group(1))

    return skills_score, experience_score, soft_skills_score