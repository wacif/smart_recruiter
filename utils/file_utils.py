# utils/file_utils.py

def is_pdf(file_path):
    """Checks if the file is a PDF based on extension."""
    return file_path.lower().endswith(".pdf")
