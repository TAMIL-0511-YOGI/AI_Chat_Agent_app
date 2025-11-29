# 🤖 AI Question-Answer Helper

A beginner-friendly agentic AI chatbot built with **Python** and **Streamlit**. This project demonstrates how a simple AI agent can answer user questions, use a search tool for factual queries, and maintain short-term conversational memory — all wrapped in a playful robot interface.

---

## 🚀 Features

- 🧠 Agent logic to distinguish factual vs conversational questions  
- 📚 Dictionary-based search tool for quick factual answers  
- 🤖 Cute robot replies with randomized emoji responses  
- 💬 Streamlit web interface with robot greeting and image  
- 🧪 Easy to test and extend with new tools or memory modules

---

## 🛠️ Technologies Used

- Python 3.9  
- Streamlit  
- Basic HTML/CSS (for styling)  
- Optional: Langchain or LlamaIndex (for future memory/tool upgrades)

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/ai-question-answer-helper.git
cd ai-question-answer-helper

# Install dependencies
pip install streamlit

💡 How It Works
User types a question in the Streamlit interface

Agent decides if it’s factual or conversational

Factual → uses search tool

Conversational → generates cute reply

Response is displayed with emojis and robot personality

🧪 Example Questions
“What is the capital of France?” → 📚 Paris

“Who wrote Hamlet?” → 📚 William Shakespeare

“I love Paris.” → 🤖 Beep boop! You said: 'I love Paris.'

🎯 Future Enhancements
Add chat history panel

Connect to Wikipedia or OpenAI API

Style chatbot with cartoon CSS

# Run the chatbot
streamlit run chat_app.py
