# AI-Powered ATS Resume Scanner
#### Link: https://huggingface.co/spaces/valleeneutral/resume_ATS_tracker

This project is an AI-driven ATS Resume Scanner designed to evaluate resumes against job descriptions. By utilizing advanced text processing, keyword extraction, and Gemini AI, the tool provides job match scores, identifies missing keywords, and optimizes resumes to enhance visibility in Applicant Tracking Systems (ATS).

## Features
#### Job Description Match Score – Calculates the percentage match between the resume and job description.
#### Keyword Analysis – Identifies missing and essential keywords to improve resume ranking.
#### Profile Summary Optimization – Generates ATS-friendly resume summaries using AI.
#### Multi-Format Support – Accepts both PDF and DOCX resumes for analysis.

## Steps to run this Project?

#### Clone the repository
```
git clone https://github.com/yourusername/ats_resume_scanner.git
```

#### Create a conda environment after opening the repository
```
conda create -n your-chosen-name python=3.10 -y
```

```
conda activate your-chosen-name
```

#### Install the requirements
```
pip install -r requirements.txt
```

#### Finally run the Application
```
streamlit run app.py
```