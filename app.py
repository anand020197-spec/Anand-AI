import os
from dotenv import load_dotenv
import google.generativeai as genai
from memory import save_memory, get_memory

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

# Create conversation history
chat = model.start_chat(history=[])

while True:
    user_input = input("\nYou: ")
    # Save user's name
    if user_input.lower().startswith("my name is"):
        name = user_input[11:].strip()
        save_memory("name", name)
        print(f"\nAnand: Nice to meet you {name}! I will remember your name.")
        continue

    # Recall user's name
    if "what is my name" in user_input.lower():
        name = get_memory("name")

        if name:
            print(f"\nAnand: Your name is {name}.")
        else:
            print("\nAnand: I don't know your name yet.")

        continue

    if user_input.lower() in ["exit", "quit"]:
        print("\nAnand AI: Goodbye! 👋")
        break

    try:
        response = chat.send_message(user_input)
        print(f"\nAnand AI: {response.text}")
    except Exception as e:
        print(f"\nError: {e}")