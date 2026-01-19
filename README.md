# Resume + Job Assistant (Gen AI)

A Streamlit + Gemini-powered Resume Assistant that helps you improve your resume and apply faster.

Upload your resume (PDF), paste a Job Description, and instantly generate:
- Resume Review (actionable improvements)
- ATS Score + Optimization Tips
- JD Matching (missing keywords + alignment)
- Job-Specific Cover Letter

## Demo Video

[![Watch the video](https://img.youtube.com/vi/I67IT8pcW9A/hqdefault.jpg)](https://www.youtube.com/watch?v=I67IT8pcW9A)

## Features

- Resume PDF upload and text extraction
- Resume review with ATS-focused improvements
- ATS score + clear optimization suggestions
- Job Description matching with missing keyword detection
- Job-specific cover letter generation (resume + JD based)
- Clean Streamlit UI with separate tabs for each feature
- Gemini API powered results

## Tech Stack

- Streamlit (Frontend/UI)
- Gemini API (LLM)
- Python
- PDF Parsing (via `pypdf` / `pdfplumber` depending on your setup)

## Project Structure

```bash
Resume-Job-Assistant-Gen-AI-/
├── app.py
├── .env
├── requirements.txt
├── utils/
│   ├── pdf_parser.py
│   ├── gemini_llm.py
│   └── prompts.py
└── README.md

```

# Setup Instructions

## 1) Clone the Repository
```bash

git clone https://github.com/jatin-wig/Resume-Job-Assistant-Gen-AI-.git
```
```bash

cd Resume-Job-Assistant-Gen-AI-
```

## 2) Install Dependencies
```bash
pip install -r requirements.txt
```
## 3) Add Gemini API Key (Required)

Create a .env file in the project root directory:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

## Important:

Do not upload .env to GitHub

Keep your Gemini API key private

## 4) Run the App
```bash
streamlit run app.py
 ```
or 
```bash
python -m streamlit run app.py 
```

