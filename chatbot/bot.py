def get_bot_response(message):
    message = message.lower()

    # Rule-based logic (you can later replace with OpenAI or Hugging Face model)
    if "career" in message:
        return "Tell me more about your skills and interests so I can guide you."
    elif "resume" in message:
        return "You can upload your resume on the 'Resume Upload' page to get personalized help."
    elif "recommend" in message:
        return "I can suggest jobs or courses based on your resume. Type 'recommend' to get started."
    elif "hello" in message or "hi" in message:
        return "Hello! I'm CareerBot. How can I assist you today?"
    else:
        return "Sorry, I didn't quite get that. Try asking about resumes, careers, or recommendations."
