import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="JamesChatGPT")
st.title("🤖 JamesChatGPT – Free LLM Edition")
st.write("Ask anything — I'm here to help you!")

# Load model once
if "chatbot" not in st.session_state:
    st.session_state.chatbot = pipeline("text2text-generation", model="google/flan-t5-base")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_question" not in st.session_state:
    st.session_state.last_question = ""

# Chat input with arrow mark
user_input = st.chat_input("Type your question here...")

if user_input:
    if user_input.strip().lower() == st.session_state.last_question.strip().lower():
        st.warning("You already asked this question. Try something new!")
    else:
        st.session_state.last_question = user_input
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner("Thinking..."):
            response = st.session_state.chatbot(user_input, max_length=200)
            reply = response[0]['generated_text']
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.success("JamesGPT: " + reply)

# Display chat history
st.subheader("Chat History")
for msg in st.session_state.messages:
    role = "You" if msg["role"] == "user" else "JamesGPT"
    st.markdown(f"**{role}:** {msg['content']}")
