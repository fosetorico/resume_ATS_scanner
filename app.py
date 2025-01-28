import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader
from docx import Document
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract text from a PDF file
def input_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from a Word file
def input_docx_text(uploaded_file):
    doc = Document(uploaded_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Function to fetch response from Gemini Pro
def get_gemini_response(resume_text, job_description):
    input_prompt = f"""
    Hey Act Like a skilled or very experienced ATS (Application Tracking System)
    with a deep understanding of the tech field, software engineering, data science, data analytics,
    and big data engineering. Your task is to evaluate the resume based on the given job description.
    You must consider the job market is very competitive, and you should provide 
    the best assistance for improving the resumes. Assign the percentage Matching based 
    on Job Description (JD) and list the missing keywords with high accuracy.

    resume: {resume_text}
    description: {job_description}

    I want the response in one single string having the structure:
    {{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
    """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input_prompt)
    return response.text

# Function to format and display the output
def format_response(response_text):
    try:
        # Parse response string to JSON
        response_data = json.loads(response_text)

        # Format the output
        st.subheader("Evaluation Results")
        st.write(f"**Job Description Match:** {response_data['JD Match']}")
        st.write(f"**Missing Keywords:** {', '.join(response_data['MissingKeywords']) if response_data['MissingKeywords'] else 'None'}")
        st.write(f"**Evaluation Summary:** {response_data['Profile Summary']}")
        return response_data
    except json.JSONDecodeError:
        st.error("Unable to parse the response. Please try again.")
        return None

# Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf", "docx"], help="Upload a PDF or Word document")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        # Process the uploaded file
        if uploaded_file.name.endswith(".pdf"):
            resume_text = input_pdf_text(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            resume_text = input_docx_text(uploaded_file)
        else:
            st.error("Unsupported file format.")
            resume_text = ""

        if resume_text and jd.strip():
            with st.spinner("Evaluating your resume..."):
                response = get_gemini_response(resume_text, jd)
                result = format_response(response)

                # Add to history if result is successfully parsed
                if result:
                    st.session_state.history.append({
                        "job_description": jd,
                        "resume_name": uploaded_file.name,
                        "results": result
                    })
        else:
            st.error("Please ensure both the resume and job description are provided.")
    else:
        st.error("Please upload a valid resume file.")

# Display conversation history
with st.expander("Conversation History"):
    if st.session_state.history:
        for i, entry in enumerate(st.session_state.history):
            st.write(f"### Submission {i + 1}")
            st.write(f"**Job Description:**\n{entry['job_description']}")
            st.write(f"**Resume Name:** {entry['resume_name']}")
            st.write(f"**Job Description Match:** {entry['results']['JD Match']}")
            st.write(f"**Missing Keywords:** {', '.join(entry['results']['MissingKeywords']) if entry['results']['MissingKeywords'] else 'None'}")
            st.write(f"**Evaluation Summary:** {entry['results']['Profile Summary']}")
            st.divider()
    else:
        st.info("No history available yet. Submit your first resume and job description!")

