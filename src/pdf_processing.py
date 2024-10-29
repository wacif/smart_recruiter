# src/pdf_processing.py

import fitz  # PyMuPDF
from io import BytesIO

def extract_text_from_pdf(uploaded_file):
    """Extracts text from an uploaded PDF file."""
    text = ""
    # Use BytesIO to handle in-memory file
    pdf_data = BytesIO(uploaded_file.read())
    with fitz.open(stream=pdf_data, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text
