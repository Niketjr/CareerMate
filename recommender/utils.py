import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def recommend_based_on_skills(skills):
    if not skills:
        return []

    prompt = f"Skills: {', '.join(skills)}"

    payload = {
        "model": "job-recommender",  # your Modelfile model
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()

        data = response.json()
        raw_response = data.get("response", "")

        # Try to parse the JSON array from model response
        try:
            return json.loads(raw_response)
        except json.JSONDecodeError:
            # Fallback: extract JSON array using regex
            import re
            match = re.search(r'\[.*?\]', raw_response, re.DOTALL)
            if match:
                return json.loads(match.group())
            else:
                return ["No valid recommendations parsed."]
    except Exception as e:
        return [f"Error: {str(e)}"]
