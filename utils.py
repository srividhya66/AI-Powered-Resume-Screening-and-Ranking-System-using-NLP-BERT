import io
import re
import PyPDF2
import spacy
import torch
from fpdf import FPDF
from sentence_transformers import SentenceTransformer, util

# Load spaCy and BERT model
nlp = spacy.load("en_core_web_sm")
bert_model = SentenceTransformer('all-MiniLM-L6-v2')

# List of predefined skills (you can expand this)
SKILL_KEYWORDS = [
    "python", "machine learning", "deep learning", "data analysis", "tensorflow",
    "pytorch", "nlp", "computer vision", "sql", "excel", "communication", "teamwork",
    "problem solving", "flask", "streamlit", "react", "git", "mongodb", "rest api"
]

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip().lower()

def compute_similarity(resume_text, job_description):
    resume_embedding = bert_model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = bert_model.encode(job_description, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(resume_embedding, jd_embedding).item()
    return round(similarity * 100, 2)  # percentage

def extract_skills(resume_text, job_description):
    matched = []
    for skill in SKILL_KEYWORDS:
        if skill.lower() in resume_text and skill.lower() in job_description.lower():
            matched.append(skill)
    score = round(len(matched) / len(SKILL_KEYWORDS) * 100, 2)
    return matched, score

def generate_pdf_report(filename, results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_title("AI Resume Match Report")

    pdf.cell(200, 10, txt="AI Resume Screening Report", ln=True, align='C')
    pdf.ln(10)

    for i, result in enumerate(results, 1):
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=f"{i}. {result['name']}")
        pdf.cell(0, 10, txt=f"   Match Score: {result['score']}%", ln=True)
        skills_text = ', '.join(result['skills']) if result['skills'] else 'No matched skills'
        pdf.multi_cell(0, 10, txt=f"   Matched Skills: {skills_text}")
        pdf.ln(5)

    pdf.output(filename)
