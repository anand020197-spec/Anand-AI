import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from prompts import ASSISTANT_PROMPT

# Load local .env (for local development)
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# If running on Streamlit Cloud, read from Secrets
if not api_key:
    api_key = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=api_key)

# Create model
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction=ASSISTANT_PROMPT
)

# Start chat session
chat = model.start_chat(history=[])


def get_response(user_message):
    try:
        response = chat.send_message(user_message)
        return response.text

    except Exception as e:
        return f"Error: {e}"