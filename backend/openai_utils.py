import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_resume(resume_text, job_description):
    prompt = f"""
    You are an ATS optimization expert. Analyze the following resume against the given job description and suggest improvements:

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Provide:
    1. An ATS match score (0-100%)
    2. Missing keywords to improve the resume
    3. Bullet points to enhance work experience
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
