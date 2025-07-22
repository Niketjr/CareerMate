import re
from .utils import extract_text_from_file

def parse_resume(uploaded_file):
    """
    Parses the uploaded resume and returns:
      - full extracted text
      - list of skills
      - education section
      - experience section
    """
    text = extract_text_from_file(uploaded_file)
    skills = extract_skills(text)
    education = extract_section(text, "education")
    experience = extract_section(text, "experience")
    return text, skills, education, experience

def extract_skills(text):
    """
    Extract a list of predefined skills from the text.
    """
    predefined_skills = [
        "Python", "Django", "REST", "SQL", "Java", "JavaScript",
        "Machine Learning", "React", "Git", "AWS", "Docker"
    ]
    found_skills = [
        skill for skill in predefined_skills
        if re.search(rf'\b{re.escape(skill)}\b', text, re.IGNORECASE)
    ]
    return found_skills

def extract_section(text, section_name):
    """
    Extract a section like Education or Experience based on heading heuristics.
    """
    pattern = rf"{section_name}\s*(?:\:)?(.*?)(?:\n\n|\Z)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return f"{section_name.capitalize()} section not found."
