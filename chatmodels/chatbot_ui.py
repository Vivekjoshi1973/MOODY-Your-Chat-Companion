import json, os, time
import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

MEMORY_FILE = "chat_memory.json"

st.set_page_config(page_title="Your Moody Bot", page_icon="🐉")

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
    .main > div {
        background: transparent;
    }
    .stChatMessage {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px !important;
        padding: 10px !important;
        margin: 5px 0 !important;
        border: 1px solid rgba(255, 215, 0, 0.1) !important;
    }
    .stChatInput textarea {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 215, 0, 0.2) !important;
        color: #fff !important;
        border-radius: 12px !important;
    }
    .stChatInput textarea:focus {
        border-color: #ff6b00 !important;
        box-shadow: 0 0 15px rgba(255, 107, 0, 0.2) !important;
    }
    .stButton button {
        background: linear-gradient(145deg, #ff6b00, #ff4500) !important;
        color: #fff !important;
        border: 2px solid #ffd700 !important;
        border-radius: 12px !important;
        font-weight: bold !important;
        transition: all 0.3s !important;
    }
    .stButton button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 0 20px rgba(255, 107, 0, 0.5) !important;
    }
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 215, 0, 0.2) !important;
        color: #fff !important;
        border-radius: 12px !important;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a3e, #0f0c29) !important;
        border-right: 1px solid rgba(255, 215, 0, 0.1) !important;
    }
    [data-testid="stSidebar"] .stButton button {
        width: 100% !important;
    }
    h1, h2, h3, p, label {
        color: #fff !important;
    }
    .stInfo {
        background: rgba(255, 107, 0, 0.15) !important;
        border: 1px solid #ff6b00 !important;
        color: #ffd700 !important;
    }
    div[data-testid="stDownloadButton"] button {
        background: linear-gradient(145deg, #ffd700, #ffaa00) !important;
        color: #1a1a3e !important;
        border: none !important;
    }
    div[data-testid="stDownloadButton"] button:hover {
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; padding: 5px;'>
        <div style='display: inline-block; width: 110px; height: 110px; background: linear-gradient(145deg, #ff6b00, #ff4500); border-radius: 50%; box-shadow: 0 0 30px rgba(255, 107, 0, 0.6), inset 0 0 15px rgba(255, 215, 0, 0.3); border: 3px solid #ffd700; text-align: center; padding-top: 8px;'>
            <span style='font-size: 38px; filter: drop-shadow(0 0 8px rgba(255, 215, 0, 0.8));'>🐉</span>
            <div style='margin-top: -2px;'>
                <span style='color: #ffd700; font-size: 10px;'>⭐</span>
                <span style='color: #ff6b00; font-size: 14px;'>🔮</span>
                <span style='color: #ffd700; font-size: 10px;'>⭐</span>
            </div>
            <div style='color: #ffd700; font-size: 11px; font-weight: 900; text-shadow: 1px 1px 0 #cc3300; letter-spacing: 1px; font-family: Arial Black, sans-serif; margin-top: -2px;'>MOODY</div>
        </div>
        <p style='color: #ffd700; font-size: 11px; margin: 5px 0; opacity: 0.8; letter-spacing: 4px; text-transform: uppercase;'>⚡ Your Chat Companion ⚡</p>
    </div>
""", unsafe_allow_html=True)

mode_map = {
    "Angry": "you are an angry ai agent .reply aggressively and in a bad tone",
    "Funny": "you are a funny ai agent",
    "Sad": "you are a sad ai agent",
}

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"mode": None, "chat_history": []}

def save_memory(mode, chat_history):
    with open(MEMORY_FILE, "w") as f:
        json.dump({"mode": mode, "chat_history": chat_history}, f)

if "mode_selected" not in st.session_state:
    memory = load_memory()
    if memory["mode"] and memory["chat_history"]:
        st.session_state.mode = memory["mode"]
        st.session_state.mode_selected = True
        st.session_state.messages = [SystemMessage(content=memory["mode"])]
        st.session_state.chat_history = memory["chat_history"]
    else:
        st.session_state.mode_selected = False
        st.session_state.messages = []
        st.session_state.chat_history = []
    st.session_state.ended = False

if not st.session_state.mode_selected:
    st.markdown("<h3 style='text-align: center; color: #ffd700;'>Choose Your AI Mood</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("😠 Angry"):
            st.session_state.mode = mode_map["Angry"]
            st.session_state.mode_selected = True
            st.rerun()
    with col2:
        if st.button("😂 Funny"):
            st.session_state.mode = mode_map["Funny"]
            st.session_state.mode_selected = True
            st.rerun()
    with col3:
        if st.button("😢 Sad"):
            st.session_state.mode = mode_map["Sad"]
            st.session_state.mode_selected = True
            st.rerun()

    st.markdown("<p style='text-align: center; color: #ffd700; margin-top: 15px;'>— or write your own —</p>", unsafe_allow_html=True)
    custom = st.text_area("Custom mood prompt", placeholder="e.g. you are a sarcastic ai agent...", label_visibility="collapsed")
    if st.button("✨ Use Custom Mood") and custom.strip():
        st.session_state.mode = custom.strip()
        st.session_state.mode_selected = True
        st.rerun()
else:
    if not st.session_state.messages:
        st.session_state.messages = [SystemMessage(content=st.session_state.mode)]
        save_memory(st.session_state.mode, st.session_state.chat_history)

    model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

    with st.sidebar:
        st.markdown("<h3 style='color: #ffd700; text-align: center;'>⚙️ Controls</h3>", unsafe_allow_html=True)
        if st.button("🔄 Reset Chat"):
            st.session_state.mode_selected = False
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.session_state.ended = False
            if os.path.exists(MEMORY_FILE):
                os.remove(MEMORY_FILE)
            st.rerun()
        if st.button("⏹ End Conversation"):
            st.session_state.ended = True
        if st.session_state.chat_history:
            chat_text = "\n\n".join(f"{c['role'].upper()}: {c['content']}" for c in st.session_state.chat_history)
            st.download_button("📥 Export Chat", data=chat_text, file_name="moody_chat.txt", mime="text/plain")

    if st.session_state.ended:
        st.info("Conversation ended. Click **Reset Chat** to start a new one.")
        save_memory(st.session_state.mode, st.session_state.chat_history)
        st.stop()

    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])

    if prompt := st.chat_input("You:"):
        st.session_state.messages.append(HumanMessage(content=prompt))
        st.session_state.chat_history.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            placeholder = st.empty()
            full = ""
            for chunk in model.stream(st.session_state.messages):
                full += chunk.content
                placeholder.markdown(full + "▌")
            placeholder.markdown(full)

        st.session_state.messages.append(AIMessage(content=full))
        st.session_state.chat_history.append({"role": "assistant", "content": full})
        save_memory(st.session_state.mode, st.session_state.chat_history)
