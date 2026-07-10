import streamlit as st
from assistant import get_response

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Anand AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("🤖 Anand AI")

    st.markdown("---")

    st.write("### Navigation")

    st.button("🏠 Home", use_container_width=True)

    if st.button("🆕 New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.button("ℹ️ About", use_container_width=True)

    st.markdown("---")

    st.success("Version 1.0")

# -----------------------------
# Main Header
# -----------------------------
st.title("🤖 Anand AI")

st.caption("Your Personal AI Assistant")

st.markdown(
    """
Hello! I am **Anand**.

I'm here to help you with your daily tasks, questions, writing, learning and much more.
"""
)

st.divider()

# -----------------------------
# Chat Messages
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Anand is thinking..."):

            response = get_response(prompt)

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

st.divider()

st.caption("Powered by Google Gemini | Created by Anand")