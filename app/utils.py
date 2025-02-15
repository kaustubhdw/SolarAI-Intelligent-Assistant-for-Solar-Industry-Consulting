import openai
from app.config import OPENAI_API_KEY

def get_ai_response(question):
    if not OPENAI_API_KEY:
        return "Error: OpenAI API key is missing. Set it in environment variables."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=150
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return "Error retrieving response from OpenAI API."
