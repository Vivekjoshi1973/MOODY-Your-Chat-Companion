# 🐉 Moody Bot — Your Chat Companion

A Streamlit chatbot powered by **Mistral AI** with mood-based AI personalities. Choose from **Angry 😠**, **Funny 😂**, **Sad 😢**, or write your **own custom mood**. Features a Dragon Ball inspired theme with streaming responses, chat memory, and conversation export.

## ✨ Features

| Feature | Description |
|---|---|
| 🎭 **4 Mood Modes** | Angry, Funny, Sad, or Custom — you control the personality |
| ⚡ **Streaming** | Replies appear token-by-token in real time |
| 💾 **Chat Memory** | Conversations auto-save and persist across sessions |
| 📥 **Export Chat** | Download your chat as a `.txt` file anytime |
| 🎨 **Dragon Ball UI** | Dark space gradient with gold/orange accents |
| 🔄 **Reset / End** | Switch moods or stop the conversation cleanly |

## 🛠️ Setup

```bash
# Clone the repo
git clone https://github.com/Vivekjoshi1973/MOODY-Your-Chat-Companion.git
cd MOODY-Your-Chat-Companion

# Install dependencies
pip install -r requirements.txt

# Add your Mistral API key
echo "MISTRAL_API_KEY=your_api_key_here" > .env

# Run the app
streamlit run chatmodels/chatbot_ui.py
```

## 🚀 Deploy

**Streamlit Community Cloud (free):**
1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **New app** → select this repo
4. Set main file to `chatmodels/chatbot_ui.py`
5. Add `MISTRAL_API_KEY` in **Advanced → Secrets**
6. Click **Deploy**

Your app will be live at `https://moody-bot.streamlit.app` 🎉

## 📦 Tech Stack

- **Python** — Core logic
- **Streamlit** — UI framework
- **LangChain + Mistral AI** — LLM integration
- **JSON** — Local chat persistence
