import re

def extract_scores_from_analysis(analysis_text):
    # Initialize scores to 0 in case of failures
    skills_score = 0
    experience_score = 0
    soft_skills_score = 0

    # Try to extract scores using regex
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