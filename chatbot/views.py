import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Replace with your Hugging Face API key
HF_API_TOKEN = "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"
HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

def query_huggingface(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 512, "temperature": 0.7}
    }
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    return response.json()

class ResumeChatbotAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_input = request.data.get("message", "")
        if not user_input:
            return Response({"error": "No message provided."}, status=400)

        prompt = f"You are a career guidance expert.\n\nUser: {user_input}\n\nAI:"
        hf_response = query_huggingface(prompt)

        try:
            answer = hf_response[0]["generated_text"].split("AI:")[-1].strip()
        except Exception:
            answer = "Sorry, I couldn't process that. Please try again."

        return Response({"response": answer})
