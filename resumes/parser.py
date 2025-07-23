import requests
from .utils import extract_text_from_file

OLLAMA_API_URL = "http://localhost:11434/api/generate"  # or your Cloudflare tunnel URL

def parse_resume(uploaded_file):
    text = extract_text_from_file(uploaded_file)

    # Send to Ollama model via HTTP
    payload = {
        "model": "resume-parser",  # your Modelfile name
        "prompt": f"{text}",
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        result = response.json()

        # Parse JSON from model output
        import json
        parsed_data = json.loads(result["response"])  # model returns stringified JSON

        skills = parsed_data.get("skills", [])
        education = parsed_data.get("education", "")
        experience = parsed_data.get("experience", "")

        return text, skills, education, experience

    except Exception as e:
        print("Error calling Ollama model:", e)
        return text, [], "Education parsing failed", "Experience parsing failed"
