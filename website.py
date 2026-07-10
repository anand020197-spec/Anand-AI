import streamlit as st
from assistant import get_response, clear_chat

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Anand AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------

st.markdown(
    """
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:1.5rem;
padding-bottom:1rem;
max-width:1100px;
}

.hero{
padding:25px;
border-radius:18px;
background:linear-gradient(90deg,#2563eb,#4f46e5);
color:white;
margin-bottom:20px;
}

.hero h1{
font-size:42px;
margin-bottom:5px;
}

.hero p{
font-size:18px;
opacity:.95;
}

.status{
padding:12px;
border-radius:12px;
background:#e8f5e9;
color:#2e7d32;
font-weight:600;
text-align:center;
margin-bottom:15px;
}

.feature-box{
padding:12px;
border-radius:10px;
background:#f5f7fb;
margin-bottom:10px;
}

.footer{
text-align:center;
padding:20px;
color:gray;
font-size:14px;
}

.stChatMessage{
border-radius:14px;
padding:10px;
}

@media (max-width:768px){

.hero h1{
font-size:30px;
}

.hero p{
font-size:15px;
}

.block-container{
padding-top:10px;
}

}

</style>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------
# SESSION
# -------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

with st.sidebar:

    st.title("🤖 Anand AI")

    st.markdown(
        """
<div class="status">
🟢 Online
</div>
""",
        unsafe_allow_html=True,
    )

    if st.button("🆕 New Chat", use_container_width=True):

        st.session_state.messages = []

        clear_chat()

        st.rerun()

    st.markdown("---")

    st.subheader("✨ Features")

    st.markdown(
        """
<div class="feature-box">
💬 AI Chat
</div>

<div class="feature-box">
📚 Learning Assistant
</div>

<div class="feature-box">
💻 Coding Help
</div>

<div class="feature-box">
📝 Resume Guidance
</div>

<div class="feature-box">
📖 Content Writing
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.success("Version 1.1 Stable")

    st.caption("Developed by Anand")

# -------------------------------------------------------
# HERO SECTION
# -------------------------------------------------------

st.markdown(
    """
<div class="hero">

<h1>🤖 Anand AI</h1>

<p>
Smarter conversations.<br>
Faster answers.<br>
Powered by Google Gemini.
</p>

</div>
""",
    unsafe_allow_html=True,
)

st.write(
    "Welcome! I'm **Anand AI**, your intelligent assistant for learning, coding, writing, career guidance and much more."
)

st.divider()

# -------------------------------------------------------
# DISPLAY CHAT HISTORY
# -------------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])
        # -------------------------------------------------------
# CHAT INPUT
# -------------------------------------------------------

prompt = st.chat_input("💬 Ask Anand AI anything...")

if prompt:

    # Store & display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):

        placeholder = st.empty()

        placeholder.markdown(
            """
🧠 **Anand AI is analyzing your request...**

Please wait a moment.
"""
        )

        with st.spinner("Generating response..."):

            response = get_response(prompt)

        placeholder.empty()

        st.markdown(response)

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------

st.divider()

st.markdown(
    """
<div class="footer">

<b>🤖 Anand AI v1.1 Stable</b><br><br>

Powered by <b>Google Gemini</b><br>

Developed with ❤️ by <b>Anand Nadiya</b>

</div>
""",
    unsafe_allow_html=True,
)