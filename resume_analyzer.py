import pdfplumber
import re

SKILLS = [
    "python", "sql", "machine learning", "deep learning",
    "flask", "numpy", "pandas", "git", "c++", "data analysis"
]

def extract_text(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t
    except:
        pass
    return text.lower()

def detect_skills(text):
    return [s for s in SKILLS if re.search(rf"\b{s}\b", text)]

def get_suggestions(skills):
    suggestions = []
    if "python" not in skills:
        suggestions.append("Improve Python programming")
    if "sql" not in skills:
        suggestions.append("Learn SQL for database handling")
    if "machine learning" not in skills:
        suggestions.append("Start Machine Learning basics")
    if "flask" not in skills:
        suggestions.append("Build web apps using Flask")
    return suggestions
