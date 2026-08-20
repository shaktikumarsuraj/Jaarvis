<div align="center">

# 🤖 J.A.R.V.I.S.
### 🎙️ Your Gemini-Powered Voice & Text Assistant

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_API-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-4CAF50?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-00C853?style=for-the-badge)

</div>

---

Jarvis is a voice and text assistant built with **Streamlit** and **Google Gemini**. It supports typed chat as well as microphone input, and replies both on-screen and out loud via text-to-speech. 🌟

The repo includes two ways to run Jarvis:

| Mode | File | Description |
|------|------|-------------|
| 🖥️ **Web App** | `app.py` | Streamlit chat UI, sidebar, and mic input |
| 📓 **Notebook / CLI** | `assistant.ipynb` | Continuous voice-loop assistant |

---

## ✨ Features

| | |
|---|---|
| 💬 | Text chat powered by the Gemini API (`gemini-3.6-flash`) |
| 🎙️ | Voice input via `SpeechRecognition` (Google Speech-to-Text) |
| 🔊 | Spoken responses via `pyttsx3` (offline text-to-speech) |
| 🖥️ | Clean, dark-themed chat UI (Streamlit app) |
| 🔁 | "New chat" button to reset the conversation |
| ⚡ | Fast, minimal setup — just add your API key and go |

---

## 🧰 Requirements

- 🐍 Python 3.9+
- 🎤 A microphone (for voice input)
- 🔑 A Gemini API key ([Google AI Studio](https://aistudio.google.com/))

---

## 🚀 Installation

1. Clone the repository and move into it:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   > ⚠️ **Note:** `PyAudio` can be tricky to install on some systems.
   > - 🍎 macOS: `brew install portaudio` before `pip install pyaudio`
   > - 🐧 Linux: `sudo apt-get install python3-pyaudio` or `sudo apt-get install portaudio19-dev` first
   > - 🪟 Windows: usually installs fine via pip, or use a prebuilt wheel if it fails

4. Set up your environment variables. Create a `.env` file in the project root (this file is git-ignored) with:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

---

## ▶️ Usage

### 🖥️ Streamlit app

```bash
streamlit run app.py
```

This opens Jarvis in your browser. Type a message in the input box, or click the microphone widget to speak — Jarvis will transcribe your speech, send it to Gemini, and both display and speak the response. 💬🔊

### 📓 Notebook / CLI version

Open `assistant.ipynb` and run the single cell, or convert it to a script and run it directly. This version:
- 🎚️ Calibrates the microphone for ambient noise on startup
- 🔁 Listens continuously and responds to each spoken command
- 🛑 Say **"stop"**, **"exit"**, **"quit"**, or **"goodbye"** to end the session

---

## 📁 Project Structure

```
.
├── app.py              # 🖥️ Streamlit web app
├── assistant.ipynb     # 📓 Notebook/CLI voice assistant
├── requirements.txt    # 📦 Python dependencies
├── .gitignore
└── .env                # 🔑 Your API key (not committed)
```

---

## ⚙️ Configuration Notes

- 🤖 The model used is `gemini-3.6-flash`. Change the `MODEL` variable in `app.py` (or the model name in `assistant.ipynb`) to use a different Gemini model.
- 🌐 Speech recognition uses `en-IN` (English – India) by default. Update the `language` parameter in `transcribe_audio()` / `listen()` to change this.
- 🔌 Text-to-speech runs offline via `pyttsx3`, so no extra API calls or internet connection are needed for the spoken output itself (speech recognition still requires internet).

---

## 🩹 Troubleshooting

| Issue | Fix |
|---|---|
| ❌ `"GEMINI_API_KEY not found in .env"` | Make sure your `.env` file exists in the project root and contains a valid key |
| 🤷 `"I couldn't understand the audio."` | Speak more clearly or closer to the microphone; background noise can affect accuracy |
| 📡 `"Speech recognition service is unavailable."` | Check your internet connection — Google's speech recognition requires network access |
| 🔧 PyAudio install errors | See the installation note above for platform-specific fixes |

---

## 📜 License

Add your preferred license here (e.g., MIT).

<div align="center">

Made with 🤖 and a bit of Gemini magic

</div>