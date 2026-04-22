"""
TASK 1: Streamlit + Ollama LLM Interface
Author: Intern
Description: A simple chatbot app using Streamlit and Ollama local LLM
"""

import streamlit as st
import requests
import json

# ─── PAGE SETUP ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Local AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ─── TITLE ────────────────────────────────────────────────────────────────────
st.title("🤖 Local AI Chatbot")
st.markdown("Powered by **Ollama** running on your computer")
st.divider()

# ─── SIDEBAR SETTINGS ─────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Choose which model to use
    model_name = st.selectbox(
        "Select Model",
        ["llama3", "mistral", "phi3", "gemma"],
        index=0,
        help="Make sure this model is downloaded in Ollama"
    )
    
    # Ollama server address
    ollama_url = st.text_input(
        "Ollama URL",
        value="http://localhost:11434",
        help="Default Ollama address"
    )
    
    st.markdown("---")
    st.markdown("**How to start Ollama:**")
    st.code("ollama serve", language="bash")
    st.markdown("**Download a model:**")
    st.code("ollama pull llama3", language="bash")

# ─── SESSION STATE: store chat history ────────────────────────────────────────
# This keeps the conversation in memory while app is running
if "messages" not in st.session_state:
    st.session_state.messages = []

# ─── RESET BUTTON ─────────────────────────────────────────────────────────────
col1, col2 = st.columns([4, 1])
with col2:
    if st.button("🗑️ Reset", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

with col1:
    st.markdown(f"**Chat History** ({len(st.session_state.messages)} messages)")

# ─── DISPLAY PAST MESSAGES ────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ─── FUNCTION: Send message to Ollama ─────────────────────────────────────────
def ask_ollama(user_message, model, url, history):
    """
    Sends user message to Ollama API and gets a response.
    
    Parameters:
        user_message: what the user typed
        model: which AI model to use
        url: where Ollama is running
        history: past messages for context
    
    Returns:
        The AI's response as a string
    """
    
    # Build message list (include history for context)
    messages_payload = []
    
    # Add past messages so the AI remembers the conversation
    for past_msg in history:
        messages_payload.append({
            "role": past_msg["role"],
            "content": past_msg["content"]
        })
    
    # Add current user message
    messages_payload.append({
        "role": "user",
        "content": user_message
    })
    
    # Prepare the API request
    payload = {
        "model": model,
        "messages": messages_payload,
        "stream": False  # Get full response at once (not word by word)
    }
    
    try:
        # Send request to Ollama
        response = requests.post(
            f"{url}/api/chat",
            json=payload,
            timeout=120  # Wait up to 2 minutes
        )
        
        # Check if request was successful
        response.raise_for_status()
        
        # Extract the AI's message from the response
        data = response.json()
        return data["message"]["content"]
    
    except requests.exceptions.ConnectionError:
        return "❌ Error: Cannot connect to Ollama. Make sure Ollama is running!\nRun: `ollama serve`"
    
    except requests.exceptions.Timeout:
        return "❌ Error: Request timed out. The model might be too slow."
    
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ─── CHAT INPUT BOX ───────────────────────────────────────────────────────────
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Show user message immediately
    with st.chat_message("user"):
        st.write(user_input)
    
    # Save user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Show loading spinner while waiting for AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Get response from Ollama
            response = ask_ollama(
                user_message=user_input,
                model=model_name,
                url=ollama_url,
                history=st.session_state.messages[:-1]  # Exclude the current message
            )
        
        # Display the AI response
        st.write(response)
    
    # Save AI response to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.divider()
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 12px;'>"
    "Running locally on your machine • No data sent to cloud"
    "</div>",
    unsafe_allow_html=True
)
