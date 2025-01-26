
---

# 📄 **AI-Powered Resume Generator**  

🚀 **Optimize your resume with AI-powered insights!** This web application **analyzes job descriptions**, **enhances resumes for ATS systems**, and **generates AI-driven feedback** to improve job application success. Built using **OpenAI API, Flask, React, and PostgreSQL**, this tool streamlines the resume optimization process for job seekers.

---

## **✨ Features**  
✔ **ATS Optimization** – Tailors resumes to pass Applicant Tracking Systems.  
✔ **AI-Driven Insights** – Provides keyword suggestions and formatting improvements.  
✔ **Real-Time Feedback** – Instantly refines resume content based on job descriptions.  
✔ **User-Friendly Interface** – Simple and interactive design for seamless usage.  

---

## **📌 Preview of the Application**  
🔹 **Homepage:** The intuitive UI allows users to input their resume and job description effortlessly.  

<img src="images/Webpage.png" alt="Website Home Page" width="650"/>

🔹 **Resume Analysis:** The AI processes the resume and job description, providing **ATS match scores, missing keywords, and detailed recommendations**.  

<img src="images/Output.png" alt="Website with sample inputs and outputs" width="650"/>

---

## 📌 Table of Contents
1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Getting Started](#getting-started)  
4. [Usage](#usage)  
5. [Roadmap](#roadmap)  
6. [Contributing](#contributing)  
7. [License](#license)  
8. [Contact](#contact)  

---

## 🚀 Features
- **Resume Analysis**: AI-driven suggestions for **ATS-friendly keywords** and improvements.  
- **Automated Resume Content Generation**: AI enhances bullet points, skills, and sections tailored to job descriptions.  
- **Real-Time AI Feedback**: React frontend provides **instant resume optimization** based on user input.  
- **Secure Data Storage**: PostgreSQL database stores resumes and job descriptions.  
- **User Authentication**: Login using Google OAuth (Upcoming Feature).  
- **Export to PDF**: Generate and download optimized resumes.  

---

## 🛠️ Tech Stack
| **Category**  | **Technology**  |
|--------------|----------------|
| **Frontend** | React, Axios, Bootstrap/Tailwind |
| **Backend**  | Flask (Python), FastAPI (optional) |
| **AI API**   | OpenAI GPT-4 |
| **Database** | PostgreSQL, SQLAlchemy |
| **Authentication** | OAuth2 (Google, LinkedIn) |
| **Deployment** | Docker, Render, Vercel |

---

## 🔧 Getting Started

### **🔑 Prerequisites**
Before setting up the project, ensure you have:
- **Python 3.8+**
- **Node.js & npm**  
- **PostgreSQL** (Installed & running)  
- **OpenAI API Key** (Sign up at [OpenAI](https://platform.openai.com/signup/))  

### **📂 Installation Guide**
#### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Konsing/AI_Resume_Generator.git
cd AI-Resume-Generator
```

#### **2️⃣ Backend Setup (Flask)**
```sh
cd backend
python -m venv venv
source venv/bin/activate  # (Windows users: venv\Scripts\activate)
pip install -r requirements.txt
```

- Create a `.env` file inside the `backend` folder:
```sh
OPENAI_API_KEY=your-openai-api-key
DATABASE_URL=postgresql://yourusername:yourpassword@localhost/ai_resume_db
```

- Initialize the database:
```sh
python setup_db.py
```

- Run the backend:
```sh
python app.py
```
Your Flask API should now be running at **http://127.0.0.1:5000/**.

---

#### **3️⃣ Frontend Setup (React)**
```sh
cd ../frontend
npm install
npm start
```
The frontend should now be running at **http://localhost:3000**.

---

## 🎯 Usage

### **1️⃣ Launch the Backend**
```sh
cd backend
source venv/bin/activate
python app.py
```
- Flask API starts at **http://127.0.0.1:5000/**.

### **2️⃣ Start the Frontend**
```sh
cd frontend
npm start
```
- React app opens at **http://localhost:3000**.

### **3️⃣ AI Resume Optimization**
- Paste your **resume text** and the **job description**.
- Click **Analyze Resume** to get AI suggestions.
- Download the **optimized ATS-friendly resume**.

---

## 📅 Roadmap
- ✅ **Basic AI Resume Analysis**  
- ✅ **Job-Resume Match Score**  
- 🔜 **User Authentication (Google OAuth)**  
- 🔜 **Export to PDF**  
- 🔜 **Deployment on AWS/GCP**  

---

## 🤝 Contributing
We welcome contributions! To contribute:  
1. **Fork** this repository.  
2. **Create a new branch** for your feature:
   ```sh
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**:
   ```sh
   git commit -m "Add amazing feature"
   ```
4. **Push to your branch**:
   ```sh
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**.

---

## 📜 License
This project is licensed under the **MIT License**.

---