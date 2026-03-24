def ai_chat(msg):
    msg = msg.lower()

    if "resume" in msg:
        return "Add strong projects, measurable achievements, and technical skills to improve your resume."

    elif "python" in msg:
        return "Build projects using Flask, automation scripts, and data analysis to improve Python."

    elif "internship" in msg or "job" in msg:
        return "Apply daily on LinkedIn and Internshala. Focus on strong projects and GitHub."

    elif "skills" in msg:
        return "Focus on Python, SQL, Machine Learning, and Data Structures."

    elif "project" in msg:
        return "Build real-world projects like AI Resume Analyzer, Chatbot, and deploy them."

    else:
        return "Keep learning, building projects, and applying consistently 🚀"
