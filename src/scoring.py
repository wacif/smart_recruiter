# src/scoring.py

def weighted_score(skills_score, experience_score, soft_skills_score, weights):
    """Calculates weighted score based on specified weights."""
    return (skills_score * weights['skills'] +
            experience_score * weights['experience'] +
            soft_skills_score * weights['soft_skills'])
