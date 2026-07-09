import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create Gemini model
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="""
    You are Anand, a personal AI assistant.
    Your purpose is to help users solve problems,
    answer questions, explain concepts, write content,
    and provide useful guidance.

    Always introduce yourself as Anand.
    Be friendly, professional, and helpful.
    """
)
print("=" * 50)
print("🤖 Anand AI")
print("=" * 50)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        print("\nAnand AI: Goodbye! 👋")
        break

    try:
        response = model.generate_content(user_input)
        print(f"\nAnand AI: {response.text}")
    except Exception as e:
        print(f"\nError: {e}")