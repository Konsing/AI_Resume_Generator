
---

# **📝 AI-Powered Resume Optimizer**

A **React + Flask** web application that helps job seekers **optimize their resumes** using **AI-driven analysis**. The app compares resumes to job descriptions and provides **real-time feedback, keyword suggestions, and improvement tips** to improve ATS (Applicant Tracking System) compatibility.

---

## **📌 Features**
✅ **AI-Powered Resume Analysis** – Uses OpenAI to analyze resumes and suggest improvements.  
✅ **Real-Time Feedback** – Get ATS optimization scores, missing keywords, and enhanced bullet points.  
✅ **Full-Stack Implementation** – Built with **React (Frontend), Flask (Backend), and PostgreSQL (Database)**.  
✅ **Seamless API Integration** – Connects React with Flask via **Axios** for smooth requests.  
✅ **Secure & Scalable** – Uses **dotenv for environment variables** and **Flask CORS** for secure connections.  

---

## **🛠️ Tech Stack**
**Frontend:** React, Axios, Bootstrap  
**Backend:** Flask, OpenAI API, psycopg2  
**Database:** PostgreSQL  
**Deployment:** Node.js, Python  

---

## **🚀 Getting Started**

### **🔹 Prerequisites**
1️⃣ **Install Node.js & npm** (for frontend)  
2️⃣ **Install Python 3.x** & create a virtual environment (for backend)  
3️⃣ **Install PostgreSQL** & set up the database  
4️⃣ **Get an OpenAI API Key** ([Sign up here](https://platform.openai.com/signup/))  

---

### **🖥️ 1️⃣ Backend Setup (Flask + PostgreSQL)**
1️⃣ **Navigate to the backend directory**  
```sh
cd backend
```
2️⃣ **Create a virtual environment**  
```sh
python -m venv venv
```
3️⃣ **Activate the virtual environment**  
```sh
venv\Scripts\activate  # Windows
```
4️⃣ **Install required dependencies**  
```sh
pip install -r requirements.txt
```
5️⃣ **Set up PostgreSQL database** (Make sure PostgreSQL is running)
```sh
psql -U postgres
```
Then run (only needed during creation):
```sql
CREATE DATABASE ai_resume_db;
\c ai_resume_db;

CREATE TABLE resumes (
    id SERIAL PRIMARY KEY,
    resume_text TEXT NOT NULL,
    job_description TEXT NOT NULL,
    ai_feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
6️⃣ **Create and configure a `.env` file**
```ini
OPENAI_API_KEY=your-openai-api-key
DATABASE_URL=postgresql://youruser:yourpassword@localhost/ai_resume_db
SECRET_KEY=your-generated-secret-key
```
7️⃣ **Run the Flask server**
```sh
python app.py
```
📌 Flask API should now run on **http://127.0.0.1:5000/**

---

### **🌐 2️⃣ Frontend Setup (React)**
1️⃣ **Navigate to the frontend directory**  
```sh
cd ../frontend
```
2️⃣ **Install dependencies**  
```sh
npm install
```
3️⃣ **Install required packages**  
```sh
npm install axios react-bootstrap web-vitals
```
4️⃣ **Start the React app**  
```sh
npm start
```
📌 The app should open in your browser at **http://localhost:3000/**

---

## **📡 API Endpoints**
### **🔹 Analyze Resume (`/api/analyze`)**
**Request (POST):**
```json
{
  "resume": "Your resume text here...",
  "job": "Job description here..."
}
```
**Response (JSON):**
```json
{
  "feedback": "Your resume matches 85% with the job description. Consider adding the following keywords: Python, Flask, Machine Learning."
}
```

---

## **🎨 UI Overview**
📌 **Home Page (Resume Input)**
```jsx
<ResumeAnalyzer />
```
📌 **API Request to Flask**
```javascript
const analyzeResume = async () => {
    const response = await axios.post("http://127.0.0.1:5000/api/analyze", { resume, job });
    setFeedback(response.data.feedback);
};
```
---

## **📝 Essential PostgreSQL Commands for This Project**
✅ **1️⃣ Connecting to PostgreSQL**
```sh
psql -U postgres
```
📌 **This logs into PostgreSQL as the default postgres user.**

✅ **2️⃣ Creating the Database**

```sh
CREATE DATABASE ai_resume_db;
```
📌 **This creates a database called ai_resume_db where we store resumes.**

✅ **3️⃣ Connecting to the Database**
```sh
\c ai_resume_db;
```
📌 **This switches to the ai_resume_db database.**

✅ **4️⃣ Creating the resumes Table**
```sh
CREATE TABLE resumes (
    id SERIAL PRIMARY KEY,
    resume_text TEXT NOT NULL,
    job_description TEXT NOT NULL,
    ai_feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
📌 **What this does:**
```
    id SERIAL PRIMARY KEY → Creates a unique ID for each resume.
    resume_text TEXT NOT NULL → Stores the raw resume text.
    job_description TEXT NOT NULL → Stores the job description.
    ai_feedback TEXT → Stores the AI-generated improvements.
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP → Records when the resume was analyzed.
```
✅ **5️⃣ Viewing All Tables**
```sh
\d
```
📌 **This lists all tables inside the database.**

✅ **6️⃣ Viewing Table Structure**
```sh
\d resumes;
```
📌 **This shows the columns and types inside resumes.**

✅ **7️⃣ Inserting Sample Data**
```sh
INSERT INTO resumes (resume_text, job_description, ai_feedback)
VALUES ('Software Engineer with 5 years experience', 'Looking for Python Developer', 'Add Python, Flask skills');
```
📌 **This manually adds a test resume.**

✅ **8️⃣ Viewing All Records**
```sh
SELECT * FROM resumes;
```
📌 **This retrieves all stored resumes.**

✅ **9️⃣ Deleting a Specific Resume**
```sh
DELETE FROM resumes WHERE id=1;
```
📌 **This deletes a resume with id=1.**

---

## **🎯 Future Enhancements**
🔹 **User Authentication** – Save & track multiple resumes  
🔹 **AI-Powered Cover Letter Generator**  
🔹 **Cloud Deployment (AWS/GCP)** for scalability  
🔹 **Enhanced ATS Optimization Algorithm**  

---

## **📜 License**
This project is licensed under the **MIT License**.

🚀 **Enjoy optimizing your resumes with AI!** 🎯🔥

---