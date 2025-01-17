# AI-Powered Resume Generator

A comprehensive web application designed to **analyze job descriptions**, **optimize resumes**, and **generate AI-enhanced resume content** using the OpenAI API, Flask (Python), React, and PostgreSQL. This project helps job seekers tailor their resumes to Applicant Tracking Systems (ATS) and streamline their job search process.

---

## Table of Contents
1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Getting Started](#getting-started)  
4. [Usage](#usage)  
5. [Roadmap](#roadmap)  
6. [Contributing](#contributing)  
7. [License](#license)  
8. [Contact](#contact)

---

## Features
- **Resume Analysis**: AI-driven suggestions for **ATS-friendly keywords** and improvements based on job descriptions.  
- **Automated Resume Content Generation**: Creates or updates bullet points, skills, and sections tailored to specific roles.  
- **Real-Time Feedback**: React frontend provides **instant** text improvements and analysis.  
- **Secure Data Storage**: PostgreSQL database stores and retrieves user resumes and job descriptions.  
- **Scalable Backend**: Flask (or Django) for processing resume data, calling AI models, and returning optimized content.

---

## Tech Stack
- **Backend**  
  - **Flask (or Django)** – Manages API requests, processes data, and integrates with the AI model.  
  - **OpenAI API** – Powers the NLP and language generation features.  
  - **Python** – Core backend language enabling quick data manipulation and AI interactions.  
  - **PostgreSQL** – Stores user data (resumes, job descriptions, generated content).

- **Frontend**  
  - **React** – Intuitive UI with real-time text updates and AI suggestions.  
  - **Axios** – Handles communication with the Flask backend.  
  - **Bootstrap (optional)** – For styling and responsive layouts.

- **Deployment**  
  - * Future deployment using AWS, GCP, or other cloud platforms.*

---

## Getting Started

### Prerequisites
1. **Python 3.8+**  
2. **Node.js & npm**  
3. **PostgreSQL** (Installed & running)  
4. **OpenAI API Key** (https://platform.openai.com/signup/) Get it here

### Installation

**1. Clone the Repository**
~~~
git clone https://github.com/Konsing/AI_Resume_Generator.git
cd AI-Resume-CoverLetter-Generator
~~~

**2. Backend Setup**
1. Create and activate a virtual environment:
   ~~~
   cd backend
   python -m venv venv
   venv\Scripts\activate  # Since I'm using Windows
   ~~~
2. Install dependencies:
   ~~~
   pip install -r requirements.txt
   ~~~
3. Create a `.env` file in the `backend` folder for your environment variables:
   ~~~
   OPENAI_API_KEY=your-openai-api-key
   ~~~
4. Configure PostgreSQL connection in `app.py` or `models.py`.

**3. Frontend Setup**
1. Install Node.js dependencies:
   ~~~
   cd ../frontend
   npm install
   ~~~

---

## Usage

1. **Launch the Backend**  
   - Make sure you’re in the `backend/` directory inside your virtual environment:
     ~~~
     python app.py
     ~~~
   - Flask server will start on **http://127.0.0.1:5000/**.

2. **Start the Frontend**  
   - In a separate terminal, navigate to the `frontend/` directory:
     ~~~
     npm start
     ~~~
   - React app will launch at **http://localhost:3000**.

3. **Optimize or Generate Resume Content**  
    - Paste your existing resume text and the relevant job description into the provided input fields.
    - Click Generate / Optimize Resume.
    - The backend uses the OpenAI API to enhance your resume content.

4. **View Enhanced Resume**  
   - See the updated resume in real-time.
   - Optionally, store or refine your resumes for future use (if database integration is fully configured).

---

## Roadmap
- **User Authentication**: Implement user login (e.g., Google OAuth) to store multiple resumes/cover letters per user.
- **Detailed ATS Optimization**: Expand AI prompts for more granular keyword suggestions.
- **Deployment**: Host backend on AWS/GCP and serve the React app with a CDN or custom domain.
- **Advanced Analytics**: Track user success metrics, measure improvements in job application responses.

---

## Contributing
1. **Fork** this repository.  
2. **Create** a new branch for your feature or bug fix:
   ~~~
   git checkout -b feature/amazing-feature
   ~~~
3. **Commit** your changes:
   ~~~
   git commit -m "Add amazing feature"
   ~~~
4. **Push** to your branch:
   ~~~
   git push origin feature/amazing-feature
   ~~~
5. **Open** a Pull Request.
