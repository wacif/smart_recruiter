# candidate_matching.py

import openai

def analyze_candidate_skills(profile_text, job_spec):
    # Prepare a dynamic prompt tailored to each resume
    prompt = (
        f"Analyze the following resume text and assess how well it matches these job specifications: {job_spec}\n\n"
        f"Resume:\n{profile_text}\n\n"
        "Identify relevant skills, years of experience, and any mention of soft skills. Provide a summary and an evaluation score."
    )

    response = openai.chat.completion.create(
        model="llama-3.2-90b-vision-preview",  # Use the desired LLM model
        messages=[
            {"role": "system", "content": "You are a helpful AI model skilled at evaluating resumes based on job requirements."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract response
    analysis = response.choices[0].message['content']
    return analysis