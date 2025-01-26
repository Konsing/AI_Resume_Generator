import openai
import os

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_resume(resume_text, job_description):
    prompt = f"""
    Analyze this resume against the job description for ATS optimization:
    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Provide:
    1. ATS match score (0-100%).
    2. Missing keywords.
    3. Bullet points for improvement.
    """

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Use gpt-4-turbo for cost-efficiency
            messages=[{"role": "system", "content": prompt}]
        )
        return response.choices[0].message.content

    except openai.OpenAIError as e:
        print(f"❌ OpenAI API Error: {e}")
        return f"Error: {e}"
