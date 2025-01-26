from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import psycopg2
import traceback  # For error debugging

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# PostgreSQL Connection
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route("/")
def home():
    return jsonify({"message": "AI Resume Generator API is running!"})

@app.route("/api/analyze", methods=["POST"])
def analyze_resume():
    try:
        data = request.get_json()
        resume_text = data.get("resume", "").strip()
        job_description = data.get("job", "").strip()

        if not resume_text or not job_description:
            return jsonify({"error": "❌ Both resume and job description must be provided."}), 400

        # OpenAI API Request (NEW FORMAT)
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Use an available model
            messages=[
                {"role": "system", "content": "You are an ATS optimization expert."},
                {"role": "user", "content": f"Analyze this resume against the given job description:\n\nResume:\n{resume_text}\n\nJob Description:\n{job_description}\n\nProvide:\n1. ATS match score (0-100%)\n2. Missing keywords\n3. Bullet points to improve experience."}
            ]
        )

        feedback = response.choices[0].message.content  # New format for extracting response

        return jsonify({"feedback": feedback})

    except Exception as e:
        print("❌ ERROR LOG:")
        traceback.print_exc()
        return jsonify({"error": f"❌ Internal Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
