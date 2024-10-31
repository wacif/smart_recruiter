# src/llm_handler.py

import os
from groq import Groq
import streamlit as st

# Initialize the Groq client with the API key
api_key = st.secrets["GROQ_API_KEY"]
client = Groq(
    api_key=api_key)

def call_groq_api(messages, model="llama-3.2-90b-vision-preview"):
    """Calls Groq API to generate a response based on input messages."""
    response = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return response.choices[0].message.content