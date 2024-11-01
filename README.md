# Smart Recruiter - AI-Powered Candidate Screening

Welcome to **Smart Recruiter**, an AI-powered candidate screening application designed to assist recruiters in efficiently analyzing and evaluating candidate resumes against job specifications. This application leverages the power of AI to extract insights from resumes, deduce scores based on tailored job requirements, and provide improvement recommendations for candidates.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Modules Explored](#modules-explored)
6. [Configuration](#configuration)
7. [Contributing](#contributing)
8. [License](#license)

## Features

- **PDF Resume Processing**: Upload multiple candidate resumes in PDF format.
- **Job Specification Input**: Define job specifications directly in the web interface.
- **Scoring Weights Adjustments**: Dynamically adjust weights for skills, experience, and soft skills.
- **Candidate Analysis**: Automatically evaluate candidates based on the job specifications.
- **Improvement Recommendations**: Get insights into areas of improvement for candidates.
- **Interactive Web App**: Built with Streamlit, providing an easy-to-use interface.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/wacif/smart-recruiter.git
   cd smart-recruiter
   ```

2. **Install the required packages**:
   Make sure you have Python installed. You can create a virtual environment and install packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure API Keys and Secrets**:
   Store your confidential keys (e.g., `GROQ_API_KEY`) safely. You can use Streamlit secrets management:
   ```bash
   streamlit secrets set "GROQ_API_KEY" "your_groq_api_key"
   ```

## Usage

To run the application, execute the following command:

```bash
streamlit run main.py
```

Upon running, the application launches a Streamlit web interface where you can input job specifications, upload candidate resumes, and receive scoring results and improvement suggestions.

## Project Structure

The project is organized as follows:

```plaintext
smart-recruiter/
│
├── main.py               # Entry point for the application
├── requirements.txt      # Python dependencies
├── src/                  # Source modules
│   ├── candidate_matching.py
│   ├── pdf_processing.py
│   ├── llm_handler.py
│   ├── scheduling.py
│
├── utils/                # Utility functions
│   ├── table_utils.py
│   ├── security_utils.py
│   ├── file_utils.py
│
└── scoring.py            # Scoring related functions
```

## Modules Explored

### Main Application - `main.py`

It serves as the starting point of the application. Major components include:

- **Streamlit Interface**: Designed with sections for job specification input, resume uploads, score weight configuration, candidate analysis, and improvement recommendation output.
- **Session Management**: Utilizes Streamlit's session state to manage application state across interactions.

### Source Modules - `src`

- **`candidate_matching.py`**: Handles candidate analysis using a language model, extracting skills, experiences, scores, and providing improvement suggestions.
- **`pdf_processing.py`**: Manages the extraction of text data from uploaded PDF resumes.
- **`llm_handler.py`**: Interacts with the Groq API for processing language model tasks.
- **`scheduling.py`**: A placeholder for potential integration with scheduling APIs like Google Calendar.

### Utility Functions - `utils`

- **`table_utils.py`**: Provides utilities for generating DataFrame tables.
- **`security_utils.py`**: Contains functions for encryption and decryption using the Fernet module.
- **`file_utils.py`**: Offers utility to verify if a file type is PDF.

### Scoring - `scoring.py`

This module includes functions for extracting scores from text analysis and calculating weighted scores based on user-defined preferences.

## Configuration

- **Groq API Key**: Essential for processing analysis and recommendations. Secure it using Streamlit's secrets management.

- **Default Scoring Weights**: Preset weights for different evaluation criteria can be modified in the configuration files if needed.

## Contributing

Contributions are welcome! Please follow these guidelines:

- Fork the repository.
- Create a feature branch (`git checkout -b feature-branch`).
- Commit your changes (`git commit -m 'Add new feature'`).
- Push to your branch (`git push origin feature-branch`).
- Open a Pull Request.

## License
