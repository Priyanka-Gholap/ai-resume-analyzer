import os
from flask import Flask, render_template, request
from utils.parser import extract_text_from_pdf
from utils.matcher import extract_skills
from utils.scorer import calculate_match_score, get_skill_gap

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_resume():
    file = request.files["resume"]
    job_desc = request.form["job_desc"]

    if file.filename == "":
        return "No file selected"

    # Save file
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    # Extract resume text
    resume_text = extract_text_from_pdf(file_path)

    # Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    # Calculate match score
    match_score = calculate_match_score(resume_text, job_desc)

    # Skill gap analysis
    matched, missing = get_skill_gap(resume_skills, job_skills)

    # Send data to result.html
    return render_template(
        "result.html",
        match_score=match_score,
        matched=matched,
        missing=missing,
        resume_text=resume_text[:1500]
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
