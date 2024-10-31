# scoring.py

import re

def extract_scores_from_analysis(analysis_text):
    # Initialize scores to 0 in case of failures
    skills_score = 0
    experience_score = 0
    soft_skills_score = 0

    # Extract scores using regex
    try:
        skills_score = int(re.search(r"Skills Score: (\d+)", analysis_text).group(1))
    except AttributeError:
        print("Skills Score not found in analysis text.")

    try:
        experience_score = int(re.search(r"Experience Score: (\d+)", analysis_text).group(1))
    except AttributeError:
        print("Experience Score not found in analysis text.")

    try:
        soft_skills_score = int(re.search(r"Soft Skills Score: (\d+)", analysis_text).group(1))
    except AttributeError:
        print("Soft Skills Score not found in analysis text.")

    return skills_score, experience_score, soft_skills_score

def weighted_score(skills_score, experience_score, soft_skills_score, weights):
    # Calculate weighted score based on provided weights
    total_weight = weights['skills'] + weights['experience'] + weights['soft_skills']
    weighted_total = (
        skills_score * weights['skills'] +
        experience_score * weights['experience'] +
        soft_skills_score * weights['soft_skills']
    )
    
    return weighted_total / total_weight if total_weight > 0 else 0