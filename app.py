import streamlit as st
from utils import extract_text_from_pdf, compute_similarity, extract_skills, generate_pdf_report

st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("🤖 AI-Powered Resume Screening")
st.write("Upload resumes and enter job description to rank candidates using AI (BERT) and skill matching.")

# Upload resumes
uploaded_files = st.file_uploader("📄 Upload Resumes (PDFs only)", accept_multiple_files=True, type=["pdf"])

# Input Job Description
job_desc = st.text_area("📝 Paste Job Description Here")

results = []

if st.button("🔍 Rank Resumes"):
    if not uploaded_files or not job_desc:
        st.warning("Please upload at least one resume and paste the job description.")
    else:
        with st.spinner("Analyzing resumes with BERT & skill matcher..."):
            for uploaded_file in uploaded_files:
                resume_text = extract_text_from_pdf(uploaded_file)
                sim_score = compute_similarity(resume_text, job_desc)
                matched_skills, skill_count = extract_skills(resume_text, job_desc)
                results.append({
                    'name': uploaded_file.name,
                    'score': sim_score,
                    'skills': matched_skills,
                    'skill_count': skill_count
                })

        # Sort by similarity score
        results.sort(key=lambda x: x['score'], reverse=True)

        st.subheader("📊 Ranked Resumes:")
        for idx, res in enumerate(results, 1):
            st.markdown(f"**{idx}. {res['name']}**")
            st.markdown(f"🔹 **Match Score**: `{res['score']:.2f}`")
            st.markdown(f"✅ **Matched Skills**: {', '.join(res['skills']) if res['skills'] else 'None'}")
            st.markdown("---")

        # Generate PDF Report
        if st.button("📥 Download PDF Report"):
            pdf_filename = "resume_report.pdf"
            generate_pdf_report(pdf_filename, results)
            with open(pdf_filename, "rb") as file:
                st.download_button("Download Report", file, file_name=pdf_filename)
