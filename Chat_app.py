# chat_app.py

import streamlit as st
import random

# --- Robot Greeting Section ---
st.markdown(
    """
    <div style='text-align:center;'>
        <h1>🤖 Hi, I'm RoboHelper!</h1>
        <p style='font-size:20px;'>I'm here to answer your questions and chat with you 💬</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Optional: Add a cute robot image
st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=150)

# --- Simple facts database ---
facts_db = {
    "capital of france": "Paris",
    "largest planet": "Jupiter",
    "speed of light": "299,792 km/s",
    "who wrote hamlet": "William Shakespeare",
    "current year": "2025",
    "python creator": "Guido van Rossum",
    "meaning of ai": "Artificial Intelligence is the simulation of human intelligence by machines."
}

# --- Search tool with keyword matching ---
def search_tool(query):
    query = query.lower()
    for key in facts_db:
        if key in query:
            return facts_db[key]
    return "Sorry, I don't know that."

# --- Check if question is factual ---
def is_factual(question):
    keywords = ["what", "when", "where", "who", "how many", "which", "give me"]
    return any(question.lower().startswith(k) for k in keywords)

# --- Agent response logic with cute replies ---
def agent_response(user_input):
    cute_replies = [
        "🤖 Beep boop! I heard you say: '{}'",
        "✨ Robo says: '{}'",
        "💡 That's interesting! Tell me more about '{}'",
        "👋 Hi friend! You said: '{}'"
    ]
    
    if is_factual(user_input):
        answer = search_tool(user_input)
        if "Sorry" not in answer:
            return f"📚 Here's what I found: {answer}"
        else:
            return "🤔 Hmm, I don't know that yet!"
    else:
        return random.choice(cute_replies).format(user_input)

# --- Streamlit UI ---
st.title("🧠 AI Question-Answer Helper")
st.write("Ask me anything!")

user_input = st.text_input("Your question:")

if user_input:
    response = agent_response(user_input)
    st.write("🤖", response)