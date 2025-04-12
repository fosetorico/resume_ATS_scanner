# AI-Powered ATS Resume Scanner
#### Link: https://huggingface.co/spaces/valleeneutral/resume_ATS_tracker

This project is an AI-driven ATS Resume Scanner designed to evaluate resumes against job descriptions. By utilizing advanced text processing, keyword extraction, and Gemini AI, the tool provides job match scores, identifies missing keywords, and optimizes resumes to enhance visibility in Applicant Tracking Systems (ATS).

## Features
1. Job Description Match Score – Calculates the percentage match between the resume and job description.
2. Keyword Analysis – Identifies missing and essential keywords to improve resume ranking.
3. Profile Summary Optimization – Generates ATS-friendly resume summaries using AI.
4. Multi-Format Support – Accepts both PDF and DOCX resumes for analysis.

## Steps to run this Project?

#### 1. Clone the repository
```
https://github.com/fosetorico/resume_ATS_scanner.git
```

#### 2. Create a conda environment after opening the repository
```
conda create -n your-chosen-name python=3.10 -y
```

```
conda activate your-chosen-name
```

#### 3. Rename the '.env.example' file to '.env' and insert your Google API key

#### 4. Install the requirements
```
pip install -r requirements.txt
```

#### 5. Finally run the following command
```
streamlit run app.py
