# src/llm_handler.py

import os
from groq import Groq

# Initialize the Groq client with the API key
api_key = ''
client = Groq(
    api_key=api_key)

def call_groq_api(messages, model="llama3-8b-8192"):
    """Calls Groq API to generate a response based on input messages."""
    response = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return response.choices[0].message.content