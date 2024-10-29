# src/candidate_matching.py

from src.llm_handler import call_groq_api

def analyze_candidate_skills(profile_text, job_spec):
    """Analyzes candidate skills based on job specs using Groq API."""
    messages = [
        {"role": "user", "content": f"Analyze and list the skills relevant to this job specification:\n{job_spec}\n\nCandidate profile:\n{profile_text}"}
    ]
    return call_groq_api(messages)

def get_improvement_recommendations(profile_text):
    """Suggests improvements to enhance candidate profile score using Groq API."""
    messages = [
        {"role": "user", "content": f"Suggest ways for this candidate to improve their score:\n{profile_text}"}
    ]
    return call_groq_api(messages)
