import os
import time
import logging

import streamlit as st
from dotenv import load_dotenv
from google import genai

from prompts import ASSISTANT_PROMPT

# --------------------------------------------------
# Logging
# --------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# --------------------------------------------------
# Load Environment
# --------------------------------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY not found.")

# --------------------------------------------------
# Gemini Client
# --------------------------------------------------
client = genai.Client(api_key=api_key)

# --------------------------------------------------
# Chat History (Per User)
# --------------------------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# --------------------------------------------------
# Build Conversation
# --------------------------------------------------
def build_contents(user_message: str):
    """
    Convert Streamlit session history into Gemini contents.
    """

    contents = []

    for msg in st.session_state.chat_history:

        role = "user" if msg["role"] == "user" else "model"

        contents.append(
            {
                "role": role,
                "parts": [
                    {
                        "text": msg["content"]
                    }
                ]
            }
        )

    contents.append(
        {
            "role": "user",
            "parts": [
                {
                    "text": user_message
                }
            ]
        }
    )

    return contents


# --------------------------------------------------
# Friendly Error Messages
# --------------------------------------------------
def friendly_error(error_text: str):

    error = error_text.lower()

    if "503" in error or "unavailable" in error:
        return (
            "⚠️ Anand AI is currently experiencing high demand.\n\n"
            "Please wait a few seconds and try again."
        )

    if "429" in error:
        return (
            "⚠️ Too many requests.\n\n"
            "Please wait a moment before sending another message."
        )

    if "401" in error:
        return (
            "⚠️ Authentication failed.\n\n"
            "Please contact the administrator."
        )

    if "timeout" in error:
        return (
            "⚠️ Request timed out.\n\n"
            "Please try again."
        )

    return (
        "⚠️ Something went wrong while generating the response.\n\n"
        "Please try again."
    )


# --------------------------------------------------
# Generate Response
# --------------------------------------------------
def get_response(user_message: str):

    contents = build_contents(user_message)

    retries = 3

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=contents,
                config={
                    "system_instruction": ASSISTANT_PROMPT,
                    "temperature": 0.7,
                    "max_output_tokens": 1024,
                },
            )

            answer = response.text.strip()

            st.session_state.chat_history.append(
                {
                    "role": "user",
                    "content": user_message,
                }
            )

            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": answer,
                }
            )

            return answer

        except Exception as e:

            logging.exception(e)

            message = str(e)

            # Retry temporary server errors
            if (
                "503" in message
                or "UNAVAILABLE" in message
                or "429" in message
            ):

                wait_time = 2 ** attempt

                logging.info(
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

                continue

            return friendly_error(message)

    return (
        "⚠️ Anand AI is temporarily unavailable.\n\n"
        "Please try again in a few moments."
    )


# --------------------------------------------------
# Clear Chat
# --------------------------------------------------
def clear_chat():

    st.session_state.chat_history = []