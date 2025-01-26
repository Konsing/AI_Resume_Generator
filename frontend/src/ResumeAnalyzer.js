import React, { useState } from "react";
import { analyzeResume } from "./api";
import "bootstrap/dist/css/bootstrap.min.css";
import "./ResumeAnalyzer.css"; // Import the CSS file

function ResumeAnalyzer() {
  const [resume, setResume] = useState("");
  const [job, setJob] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!resume || !job) {
      alert("❌ Please enter both resume and job description.");
      return;
    }

    setLoading(true);
    try {
      const result = await analyzeResume(resume, job);
      setResponse(result.feedback || result.error);
    } catch (error) {
      setResponse("⚠️ Error: Could not fetch analysis. Please try again.");
    }
    setLoading(false);
  };

  return (
    <div className="container mt-5">
      <div className="card shadow-lg p-4">
        <h1>🚀 AI Resume Optimizer</h1>
        <p>Optimize your resume with AI for better job matching</p>

        <form onSubmit={handleSubmit}>
          <div className="input-container">
            <div className="input-box">
              <label className="form-label">📄 Resume</label>
              <textarea
                className="form-control"
                rows="10"
                placeholder="Paste your resume here..."
                value={resume}
                onChange={(e) => setResume(e.target.value)}
              />
            </div>

            <div className="input-box">
              <label className="form-label">📝 Job Description</label>
              <textarea
                className="form-control"
                rows="10"
                placeholder="Paste job description here..."
                value={job}
                onChange={(e) => setJob(e.target.value)}
              />
            </div>
          </div>

          <button type="submit" className="btn btn-primary" disabled={loading}>
            {loading ? "Generating..." : "Generate"}
          </button>
        </form>

        {response && (
          <div className="response-box">
            <h3 className="text-success">💡 AI Feedback:</h3>
            <p>{response}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default ResumeAnalyzer;
