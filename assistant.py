import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompts import ASSISTANT_PROMPT

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create Gemini model
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction=ASSISTANT_PROMPT
)

# Start chat session
chat = model.start_chat(history=[])


def get_response(user_message):
    """
    Send a message to Gemini and return the response.
    """

    try:
        response = chat.send_message(user_message)
        return response.text

    except Exception as e:
        return f"Error: {e}"