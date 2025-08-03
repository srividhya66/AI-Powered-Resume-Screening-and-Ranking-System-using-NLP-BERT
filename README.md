# 🤖 AI-Powered Resume Screening and Ranking System using NLP & BERT

This project helps HR teams automatically screen, score, and rank resumes based on a provided Job Description (JD). It uses modern NLP techniques (SpaCy or BERT) and provides a simple, interactive interface via Streamlit.

---

## 🔍 Features

- 📄 Upload multiple resumes (PDF format)
- 🧠 NLP-based similarity scoring (Spacy or BERT-based)
- ✅ Skill keyword matcher (JD vs. resume)
- 📊 Ranked output with match scores
- 🧾 Export PDF report of top candidates
- 🗂️ Resume management (optional MongoDB support)

---

## 📁 Project Structure

```bash
resume-screening-ai/
│
├── app.py                 # Streamlit frontend
├── utils.py               # Core NLP and PDF extraction functions
├── requirements.txt       # Python dependencies
├── resumes/               # Folder for uploaded resumes
│   └── .gitkeep
└── README.md              # Project overview (this file)

💻 How to Run the App Locally
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/srividhya66/AI-Powered-Resume-Screening-and-Ranking-System-using-NLP-BERT.git
cd AI-Powered-Resume-Screening-and-Ranking-System-using-NLP-BERT
2. Set Up Virtual Environment
bash
Copy
Edit
python -m venv env
source env/bin/activate         # On Linux/Mac
env\Scripts\activate            # On Windows
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
python -m spacy download en_core_web_sm
4. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
🧠 Technology Stack
Frontend: Streamlit

Backend (NLP): SpaCy, Transformers (BERT)

PDF Parsing: PyPDF2

Similarity: Cosine similarity, TF-IDF, Sentence Transformers

Optional DB: MongoDB (for storing resumes/data)

📊 Sample Output
Match Score: 0.82 (Highly relevant)

Top Skills Matched: Python, NLP, TensorFlow, Communication

PDF Report: Automatically generated with top-ranked candidates

🚀 Future Improvements
Integrate full MongoDB resume storage and search

Add email alerts to HR for top matches

Support DOCX format parsing

Add resume feedback summary using LLMs
