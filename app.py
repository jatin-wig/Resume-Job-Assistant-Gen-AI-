import re
import streamlit as st
from dotenv import load_dotenv

from utils.pdf_parser import extract_text_from_pdf
from utils.gemini_llm import ask_gemini
from utils.prompts import (
    resume_review_prompt,
    ats_score_prompt,
    jd_match_prompt,
    cover_letter_prompt
)

load_dotenv()

st.set_page_config(page_title="Resume + Job Assistant)", layout="wide")

st.title("Resume + Job Assistant")
st.caption("Upload Resume -> Match Job Description> Improve ATS -> Generate Cover Letter")

st.markdown(
    """
<div style="
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:16px;
    padding:16px 18px;
    border:1px solid rgba(255,255,255,0.12);
    border-radius:14px;
    background:rgba(255,255,255,0.03);
    margin-top:8px;
    margin-bottom:8px;
">
    <div>
        <div style="font-size:16px; font-weight:700; margin-bottom:4px;">
            GitHub Repository
        </div>
        <div style="font-size:13px; opacity:0.8;">
            Resume-Job-Assistant-Gen-AI
        </div>
    </div>
    <div style="display:flex; gap:10px; flex-wrap:wrap;">
        <a href="https://github.com/jatin-wig/Resume-Job-Assistant-Gen-AI-" target="_blank"
           style="
                text-decoration:none;
                padding:8px 12px;
                border-radius:10px;
                border:1px solid rgba(255,255,255,0.18);
                font-size:13px;
                font-weight:600;
            ">
            View on GitHub
        </a>
    </div>
</div>
""",
    unsafe_allow_html=True
)

model = "gemini-2.5-flash-lite"
min_chars = 900

resume_pdf = st.file_uploader("Upload Resume PDF", type=["pdf"])
jd_text = st.text_area("Paste Job Description (JD)", height=220)

def normalize_text(t: str) -> str:
    if not t:
        return ""
    t = t.replace("\x00", " ")
    t = re.sub(r"\n{3,}", "\n\n", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    return t.strip()

resume_text = ""
resume_ok = False

if resume_pdf:
    try:
        resume_text = extract_text_from_pdf(resume_pdf)
        resume_text = normalize_text(resume_text)
    except Exception:
        resume_text = ""
    resume_ok = len(resume_text) >= min_chars

tabs = st.tabs(["Input", "Resume Review", "ATS Score", "Job Description Match", "Cover Letter"])

with tabs[0]:
    left, right = st.columns(2)

    with left:
        st.subheader("Resume")
        if resume_pdf and resume_text:
            st.text_area("Extracted Resume Text", resume_text[:12000], height=380)
        elif resume_pdf and not resume_text:
            st.error("Resume text extraction failed.")
        else:
            st.info("Upload a resume PDF to start.")

    with right:
        st.subheader("Job Description")
        st.text_area("JD Text", jd_text[:12000], height=380)

    if resume_pdf:
        st.subheader("Extraction Status")
        c1, c2 = st.columns(2)
        c1.metric("Extracted length", str(len(resume_text)))
        c2.metric("Ready", "Yes" if resume_ok else "No")

def guard():
    if not resume_pdf:
        st.warning("Upload a resume PDF first.")
        return False
    if not resume_ok:
        return False
    if not jd_text.strip():
        st.warning("Paste a job description first.")
        return False
    return True

with tabs[1]:
    st.subheader("Resume Review")
    if not resume_ok and resume_pdf:
        st.error("Resume text extraction is too weak. Nothing will be generated.")
    if st.button("Generate Resume Review", use_container_width=True, disabled=not guard()):
        with st.spinner("Generating..."):
            prompt = resume_review_prompt(resume_text, jd_text)
            output = ask_gemini(prompt, model)
        st.write(output)

with tabs[2]:
    st.subheader("ATS Score")
    if not resume_ok and resume_pdf:
        st.error("Resume text extraction is too weak. Nothing will be generated.")
    if st.button("Generate ATS Score", use_container_width=True, disabled=not guard()):
        with st.spinner("Generating..."):
            prompt = ats_score_prompt(resume_text, jd_text)
            output = ask_gemini(prompt, model)
        st.write(output)

with tabs[3]:
    st.subheader("JD Match")
    if not resume_ok and resume_pdf:
        st.error("Resume text extraction is too weak. Nothing will be generated.")
    if st.button("Generate JD Match", use_container_width=True, disabled=not guard()):
        with st.spinner("Generating..."):
            prompt = jd_match_prompt(resume_text, jd_text)
            output = ask_gemini(prompt, model)
        st.write(output)

with tabs[4]:
    st.subheader("Cover Letter")
    if not resume_ok and resume_pdf:
        st.error("Resume text extraction is too weak. Nothing will be generated.")

    name = st.text_input("Your Name", "")
    company = st.text_input("Company Name", "")
    role = st.text_input("Role Title", "")

    if st.button("Generate Cover Letter", use_container_width=True, disabled=not guard()):
        with st.spinner("Generating..."):
            prompt = cover_letter_prompt(resume_text, jd_text, name, company, role)
            output = ask_gemini(prompt, model)
        st.write(output)
