import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_gemini(prompt: str, model_name="gemini-2.5-flash-lite") -> str:
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text
