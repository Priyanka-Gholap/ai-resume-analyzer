# 🤖 AI Resume Analyzer & Job Matcher

A full-stack Machine Learning web application that analyzes resumes, compares them with job descriptions, and provides actionable insights such as match score, matched skills, and missing skills.

🌐 **Live Demo:** https://ai-resume-analyzer-bxmz.onrender.com
---

## 📌 Features

* Upload resume (PDF)
* Paste job description for comparison
* Extracts key technical skills automatically
* Calculates resume–job match score using ML (TF-IDF + cosine similarity)
* Shows matched and missing skills (skill gap analysis)
* Clean, modern UI using pure HTML + CSS
* Fully deployed on Render

---

## 🧠 Technologies Used

**Backend & ML**

* Python
* Flask
* scikit-learn (TF-IDF, cosine similarity)
* pdfplumber (PDF text extraction)
* NumPy, Pandas

**Frontend**

* HTML
* CSS (no frameworks used)

**Deployment & Tools**

* Git & GitHub
* Render (cloud deployment)

---

## ⚙️ How It Works

1. User uploads a resume (PDF)
2. Resume text is extracted using `pdfplumber`
3. Skills are extracted using a custom keyword-matching engine
4. Resume and Job Description are vectorized using **TF-IDF**
5. Similarity score is calculated using **Cosine Similarity**
6. App displays:

   * Match Score (%)
   * Matched Skills
   * Missing Skills
   * Resume Preview

---

## 📂 Project Structure

```
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── uploads/
│
├── utils/
│   ├── parser.py      # PDF text extraction
│   ├── matcher.py     # Skill extraction logic
│   └── scorer.py      # ML similarity + skill gap
│
├── templates/
│   ├── index.html     # Upload page
│   └── result.html    # Result dashboard
```

---

## 🚀 Run Locally

1. Clone the repository

```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
```

2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the app

```bash
python app.py
```

5. Open in browser

```
http://127.0.0.1:5000
```

---

## 📈 Example Output

* Match Score: `72.45%`
* Matched Skills: Python, React, MongoDB
* Missing Skills: Docker, AWS

---

## 📚 What I Learned

* Building end-to-end ML projects
* Resume parsing and text processing
* TF-IDF and cosine similarity
* Flask backend development
* HTML/CSS UI design
* GitHub version control
* Deploying real projects to cloud (Render)

---

## 👩‍💻 Author

**Priyanka Gholap**
Computer Engineering Student

* LinkedIn: https://www.linkedin.com/in/priyankagholap-in
* GitHub: 
