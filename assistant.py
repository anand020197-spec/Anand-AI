import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from prompts import ASSISTANT_PROMPT

# Load .env file
load_dotenv()

# Get API Key
api_key = os.getenv("GEMINI_API_KEY")

# If running on Streamlit Cloud
if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY")

# Create Gemini Client
client = genai.Client(api_key=api_key)

# Store conversation history
history = []


def get_response(user_message):
    global history

    try:
        # Add user message
        history.append({
            "role": "user",
            "parts": [{"text": user_message}]
        })

        # Generate response
        response = client.models.generate_content(
            model="gemini-3.5-flash"
            contents=history,
            config={
                "system_instruction": ASSISTANT_PROMPT,
                "temperature": 0.7,
                "max_output_tokens": 1024,
            },
        )

        ai_text = response.text

        # Save AI response
        history.append({
            "role": "model",
            "parts": [{"text": ai_text}]
        })

        return ai_text

    except Exception as e:
        return f"❌ Error: {str(e)}"