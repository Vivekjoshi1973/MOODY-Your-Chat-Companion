# 🐉 Moody Bot

A Streamlit chatbot powered by Mistral AI with mood-based personalities — Angry, Funny, or Sad. Inspired by Dragon Ball aesthetics.

## Features

- **3 Mood Modes + Custom** — Angry, Funny, Sad, or write your own personality prompt
- **Streaming Responses** — See replies appear token-by-token in real time
- **Chat Memory** — Conversation persists across sessions (saved locally)
- **Export Chat** — Download your conversation as a `.txt` file
- **Dragon Ball Themed UI** — Dark space gradient with gold/orange accents
- **Reset / End Controls** — Switch moods or stop anytime

## Setup

1. Clone the repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file:
   ```
   MISTRAL_API_KEY=your_api_key_here
   ```
4. Run the app:
   ```
   streamlit run chatmodels/chatbot_ui.py
   ```

## Deploy

Deploy for free on [Streamlit Community Cloud](https://streamlit.io/cloud) — connect your GitHub repo, set the main file to `chatmodels/chatbot_ui.py`, and add `MISTRAL_API_KEY` in Secrets.
