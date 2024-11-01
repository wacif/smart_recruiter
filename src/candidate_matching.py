# candidate_matching.py

import os
from groq import Groq
import streamlit as st
import re

# Initialize the Groq client
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

def analyze_candidate_skills(profile_text, job_spec):
    # Prepare a dynamic prompt tailored to each resume
    prompt = (
        f"Analyze the following resume text and assess how well it matches these job specifications: {job_spec}\n"
        f"Resume:\n{profile_text}\n"
        "Identify relevant skills, years of experience, and any mention of soft skills. Provide a summary and an evaluation score for skills, experience, and soft skills.\n"
        "Output format: 'Skills Score: X, Experience Score: Y, Soft Skills Score: Z'"
    )

    # Create the chat completion using Groq
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.2-90b-vision-preview", 
    )

    # Extract response
    analysis = chat_completion.choices[0].message.content

    # Debugging: Print the analysis to verify its content
    print("LLM Analysis Output:", analysis)

    return analysis

def extract_scores_from_analysis(analysis_text):
    # Initialize scores to 0 in case of failures
    skills_score = 0
    experience_score = 0
    soft_skills_score = 0

    # Debugging: Log the analysis text to verify if it contains scores
    print("Analysis Text for Scoring:", analysis_text)

    # Extract scores using regex
    try:
        skills_score = int(re.search(r"Skills Score:\s*(\d+)", analysis_text).group(1))
    except AttributeError:
        print("Skills Score not found in analysis text.")

    try:
        experience_score = int(re.search(r"Experience Score:\s*(\d+)", analysis_text).group(1))
    except AttributeError:
        print("Experience Score not found in analysis text.")

    try:
        soft_skills_score = int(re.search(r"Soft Skills Score:\s*(\d+)", analysis_text).group(1))
    except AttributeError:
        print("Soft Skills Score not found in analysis text.")

    return skills_score, experience_score, soft_skills_score

def get_improvement_recommendations(resume_data):
    # Placeholder function
    return "Recommendations will be implemented later."