import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

OLLAMA_URL = "http://localhost:11434/api/generate"  # Or your Cloudflare proxy if hosted externally

def query_ollama(prompt):
    payload = {
        "model": "career_chatbot",  # Your custom model name
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": 512
        }
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"Error: {str(e)}"

class ChatBotView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_input = request.data.get("message", "")
        if not user_input:
            return Response({"error": "No message provided."}, status=400)

        prompt = f"You are a helpful career guidance chatbot.\nUser: {user_input}\nAI:"
        answer = query_ollama(prompt)
        return Response({"response": answer})
