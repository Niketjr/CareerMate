# 💼 CareerMate

CareerMate is a full-stack AI-powered web application designed to guide users through their career development journey. It leverages advanced technologies like natural language processing and machine learning to analyze resumes, provide personalized career suggestions, and offer real-time chatbot support.

---

## 🌟 Features

### 📄 Resume Parsing and Analysis
- Upload PDF/DOCX resumes.
- Extract structured data: **Skills**, **Education**, and **Work Experience**.
- Parsed data is stored and displayed in the user dashboard.

### 🤖 AI-Powered Chatbot (via Ollama)
- Provides **career guidance** through natural conversations.
- Uses **Ollama-hosted LLM** with a custom Modelfile (`career_chatbot`) for personalized advice.
- Supports questions like:
  - “What jobs can I apply for with these skills?”
  - “Suggest ways to improve my resume.”
  - “What certifications should I pursue?”

### 📌 Career Suggestions
- Based on parsed resume and user input.
- Recommends:
  - Career paths
  - Courses
  - Skill upgrades

### 📡 Upcoming Features
- ✅ Job Matching (via external APIs)
- ✅ PDF Resume Enhancement Tool
- ✅ Leaderboard and Rewards (Gamification)

---

## 🛠 Tech Stack

### ⚙ Backend
- **Framework**: Django (REST Framework)
- **Language**: Python
- **AI Integration**: Ollama (local or via Cloudflare Tunnel)
- **Parsing Libraries**: PyMuPDF, python-docx, Spacy / Regex
- **Database**: SQLite (default), PostgreSQL (for production)

### 💻 Frontend
- **Framework**: React.js (Vite)
- **Styling**: Tailwind CSS
- **State Management**: Context API
- **API Integration**: Axios, REST API

---

## 🧪 Getting Started

### 📦 Prerequisites
- [Node.js](https://nodejs.org/) and npm
- [Python 3.11+](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Ollama](https://ollama.com/) (installed and running locally)
- Git

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Niketjr/CareerMate.git
cd CareerMate
````

---

### 2. Backend Setup (Django)

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Migrate and run server
python manage.py migrate
python manage.py runserver
```

---

### 3. Ollama Setup (LLM)

```bash
# Run Ollama model locally
ollama run career_chatbot  # Custom Modelfile for chatbot

# OR to pull the model first
ollama pull career_chatbot
ollama run career_chatbot
```

> 📌 If hosted behind Cloudflare Tunnel, configure `OLLAMA_URL` in Django accordingly.

---

### 4. Frontend Setup (React)

```bash
# Navigate to frontend folder
cd ../frontend

# Install dependencies
npm install

# Start frontend
npm run dev
```

---

## 📂 Project Structure

```
CareerMate/
│
├── backend/           # Django backend
│   ├── resumes/       # App for resume parsing
│   ├── chatbot/       # Chatbot integration with Ollama
│   ├── media/         # Uploaded resumes
│   └── manage.py
│
├── frontend/          # React.js frontend
│   ├── src/
│   ├── public/
│   └── ...
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📡 API Endpoints

### Resume Upload/Parse

* `POST /api/resumes/` – Upload a resume
* `GET /api/resumes/{id}/` – Get parsed resume data

### Chatbot

* `POST /api/chatbot/`
  **Body:**

  ```json
  {
    "message": "Suggest job roles for someone with Python and Django experience"
  }
  ```

---

## 🔐 Environment Variables

Create a `.env` file in the backend folder for configuration (optional):

```env
OLLAMA_URL=http://localhost:11434/api/generate
DEBUG=True
SECRET_KEY=your-secret-key
```

---

## 🧠 Modelfile (career\_chatbot)

```txt
FROM mistral:7b-instruct

SYSTEM """
You are an expert resume assistant. Extract structured data like:
- Name
- Skills
- Education
- Experience

Also respond to career-related questions clearly and in JSON format if extraction is requested.
"""
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Niket Dugar**
[GitHub](https://github.com/Niketjr)
Open to collaboration and suggestions!

---

## 📣 Contributions

PRs, issues, and feedback are welcome!
Please raise a GitHub issue or open a pull request.

---

```

