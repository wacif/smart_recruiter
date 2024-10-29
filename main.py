# main.py

import streamlit as st
from src.pdf_processing import extract_text_from_pdf
from src.scoring import weighted_score
from src.candidate_matching import analyze_candidate_skills, get_improvement_recommendations
from utils.table_utils import generate_results_table
from config import DEFAULT_WEIGHTS
import pandas as pd

# Initialize the Streamlit App
st.title("Smart Recruiter - AI-Powered Candidate Screening")

# 1. **Input Job Specifications**
st.header("Job Specifications")
job_spec = st.text_area("Enter the job specifications for the role", placeholder="List required skills, experience, and qualifications...")

# 2. **Upload Candidate Resumes**
st.header("Upload Candidate CVs")
uploaded_files = st.file_uploader("Upload candidate CVs (PDF only)", accept_multiple_files=True, type="pdf")

# 3. **Define Scoring Weights**
st.header("Adjust Scoring Weights")
weights = {
    'skills': st.slider("Skills Weight", 0.0, 1.0, DEFAULT_WEIGHTS['skills']),
    'experience': st.slider("Experience Weight", 0.0, 1.0, DEFAULT_WEIGHTS['experience']),
    'soft_skills': st.slider("Soft Skills Weight", 0.0, 1.0, DEFAULT_WEIGHTS['soft_skills'])
}

# 4. **Process Candidates**
if st.button("Analyze Candidates"):
    results = []
    for uploaded_file in uploaded_files:
        # Extract text from PDF
        profile_text = extract_text_from_pdf(uploaded_file)

        # Analyze candidate skills and job match
        skill_analysis = analyze_candidate_skills(profile_text, job_spec)

        # Example placeholder scores; replace with scoring logic
        candidate_scores = {
            'skills_score': 7,  # Static example score; replace with actual logic
            'experience_score': 6,
            'soft_skills_score': 8
        }

        # Calculate final weighted score
        final_score = weighted_score(
            candidate_scores['skills_score'],
            candidate_scores['experience_score'],
            candidate_scores['soft_skills_score'],
            weights
        )

        # Append candidate results to the list
        results.append({
            "Candidate": uploaded_file.name,
            "Skills Analysis": skill_analysis,
            "Final Score": final_score
        })

    # Display results in a table
    results_df = pd.DataFrame(results)
    st.subheader("Candidate Analysis Results")
    st.write(results_df)

    # Option for improvement recommendations
    if st.button("Get Improvement Recommendations"):
        improvement_recs = []
        for result in results:
            recommendation = get_improvement_recommendations(result["Skills Analysis"])
            improvement_recs.append({
                "Candidate": result["Candidate"],
                "Recommendation": recommendation
            })
        
        recs_df = pd.DataFrame(improvement_recs)
        st.subheader("Improvement Recommendations")
        st.write(recs_df)
