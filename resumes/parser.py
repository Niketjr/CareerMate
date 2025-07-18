import re

def parse_resume(file):
    """
    Placeholder function to parse a resume file and extract relevant data.
    This will return:
      - full text
      - list of skills
      - education section (as text)
      - experience section (as text)
    """
    # Step 1: Read the file content (assume it's a PDF or text for now)
    text = extract_text_from_file(file)

    # Step 2: Extract skills (dummy keywords for now)
    skills = extract_skills(text)

    # Step 3: Extract education and experience
    education = extract_section(text, "education")
    experience = extract_section(text, "experience")

    return text, skills, education, experience


def extract_text_from_file(file):
    """
    Extract raw text from the uploaded file.
    NOTE: This is a placeholder. You should later use pdfminer, PyMuPDF, docx2txt, etc.
    """
    try:
        content = file.read().decode('utf-8', errors='ignore')
    except Exception:
        content = "Unable to extract text. (You can plug in a real parser here.)"
    return content


def extract_skills(text):
    """
    Extract a list of predefined skills from the text.
    Replace with spaCy/ML-based extraction later.
    """
    predefined_skills = [
        "Python", "Django", "REST", "SQL", "Java", "JavaScript",
        "Machine Learning", "React", "Git", "AWS", "Docker"
    ]
    found_skills = [skill for skill in predefined_skills if re.search(rf'\b{re.escape(skill)}\b', text, re.IGNORECASE)]
    return found_skills


def extract_section(text, section_name):
    """
    Extracts a section from the resume using keyword-based heuristics.
    """
    pattern = rf"{section_name}\s*(?:\:)?(.*?)(?:\n\n|\Z)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return f"{section_name.capitalize()} section not found."
