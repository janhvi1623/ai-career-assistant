from flask import Flask, request, render_template
from resume_analyzer import extract_text, detect_skills, get_suggestions
from chatbot import ai_chat

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    chat_response = None

    if request.method == "POST":

        if "chat" in request.form:
            chat_response = ai_chat(request.form["chat"])

        elif "resume" in request.files:
            file = request.files["resume"]
            text = extract_text(file)

            skills = detect_skills(text)
            suggestions = get_suggestions(skills)

            result = {
                "skills": skills,
                "suggestions": suggestions
            }

    return render_template("index.html", result=result, chat_response=chat_response)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
