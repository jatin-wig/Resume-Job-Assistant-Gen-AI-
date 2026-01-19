def resume_review_prompt(resume_text, jd_text):
    return f"""
You are a professional Resume Reviewer and ATS Optimization expert.

TASK:
1. Review the resume for clarity, impact, formatting, weak points.
2. Suggest improvements in bullet points.
3. Suggest rewritten bullet examples for at least 5 lines.

RESUME:
{resume_text}

JOB DESCRIPTION:
{jd_text}
"""

def ats_score_prompt(resume_text, jd_text):
    return f"""
You are an ATS (Applicant Tracking System) scoring system.

Give:
- ATS Score out of 100
- Breakdown: Formatting, Keywords, Experience, Projects, Skills
- HIGH / MEDIUM / LOW priority fixes
- Missing sections if any

RESUME:
{resume_text}

JOB DESCRIPTION:
{jd_text}
"""

def jd_match_prompt(resume_text, jd_text):
    return f"""
You are a Job Description matching assistant.

Extract:
1. Top required skills/tools/keywords from JD (max 25)
2. Which ones exist in resume
3. Which ones are missing
4. Give match percentage estimate

RESUME:
{resume_text}

JOB DESCRIPTION:
{jd_text}
"""

def cover_letter_prompt(resume_text, jd_text, name="", company="", role=""):
    return f"""
Write a job-specific cover letter.

Rules:
- Short and strong (max 200-250 words)
- Very relevant to JD
- No generic filler lines like "I am passionate"
- 3 paragraphs format
- ATS-friendly

Candidate Name: {name}
Company: {company}
Role: {role}

RESUME:
{resume_text}

JOB DESCRIPTION:
{jd_text}
"""
