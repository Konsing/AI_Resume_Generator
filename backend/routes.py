from flask import Blueprint, request, jsonify
from openai_utils import analyze_resume
from models import SessionLocal, Resume

api = Blueprint('api', __name__)

@api.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    resume_text = data.get("resume")
    job_description = data.get("job")

    if not resume_text or not job_description:
        return jsonify({"error": "Missing input"}), 400

    feedback = analyze_resume(resume_text, job_description)

    db = SessionLocal()
    new_entry = Resume(
        user_email="test@example.com",
        resume_text=resume_text,
        job_description=job_description,
        ai_feedback=feedback
    )
    db.add(new_entry)
    db.commit()
    db.close()

    return jsonify({"feedback": feedback})
