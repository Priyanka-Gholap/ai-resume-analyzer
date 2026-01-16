SKILLS_DB = [
    "python", "java", "c", "c++", "javascript",
    "react", "node", "express", "mongodb", "sql",
    "html", "css", "flask", "django",
    "machine learning", "deep learning",
    "nlp", "data science", "pandas", "numpy",
    "git", "github", "docker", "aws",
    "linux", "tensorflow", "keras", "pytorch"
]

def extract_skills(text):
    text = text.lower()
    found_skills = set()

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    return sorted(found_skills)
