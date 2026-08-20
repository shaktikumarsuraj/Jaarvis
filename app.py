import os
import streamlit as st
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found in .env")
    st.stop()

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.6-flash"

st.set_page_config(
    page_title="Nova",
    page_icon="✦",
    layout="wide"
)

st.markdown("""
<style>
#MainMenu, footer, header {
    visibility: hidden;
}

.stApp {
    background: #131314;
    color: #e3e3e3;
}

.block-container {
    max-width: 1000px;
    padding-top: 2rem;
    padding-bottom: 7rem;
}

[data-testid="stSidebar"] {
    background: #1e1f20;
    border-right: 1px solid #2c2d2f;
}

.brand {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 2rem;
}

.brand span {
    color: #8ab4f8;
}

.hero {
    text-align: center;
    padding: 10vh 0 5vh;
}

.hero h1 {
    font-size: 3.2rem;
    letter-spacing: -0.05em;
    margin-bottom: .5rem;
}

.hero p {
    color: #a8aaad;
    font-size: 1.05rem;
}

.message {
    padding: 1rem 1.2rem;
    border-radius: 20px;
    margin: .8rem 0;
    line-height: 1.6;
    max-width: 80%;
}

.user {
    background: #2b2c2f;
    margin-left: auto;
}

.assistant {
    background: transparent;
}

.status {
    color: #8ab4f8;
    font-size: .85rem;
    margin-top: 1rem;
}

div[data-testid="stChatInput"] {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: min(900px, 88%);
    z-index: 999;
}

div[data-testid="stChatInput"] textarea {
    background: #1e1f20;
    border: 1px solid #3c4043;
    border-radius: 28px;
    color: #e3e3e3;
}
</style>
""", unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(
        model=MODEL
    )

if "engine" not in st.session_state:
    st.session_state.engine = pyttsx3.init()


def ask_gemini(text):
    try:
        response = st.session_state.chat.send_message(
            message=text
        )

        return response.text

    except Exception as e:
        print("Gemini error:", e)
        return "Sorry, I couldn't process that."


def speak(text):
    try:
        st.session_state.engine.say(text)
        st.session_state.engine.runAndWait()
    except Exception as e:
        print("TTS error:", e)


def transcribe_audio(audio):
    recognizer = sr.Recognizer()

    try:
        audio_bytes = audio.getvalue()

        audio_data = sr.AudioData(
            audio_bytes,
            16000,
            2
        )

        text = recognizer.recognize_google(
            audio_data,
            language="en-IN"
        )

        return text

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return None

    except Exception as e:
        print("Speech error:", e)
        return None


with st.sidebar:

    st.markdown(
        '<div class="brand">✦ <span>Nova</span></div>',
        unsafe_allow_html=True
    )

    st.caption("Gemini-powered voice assistant")

    if st.button(
        "＋ New chat",
        use_container_width=True
    ):
        st.session_state.messages = []

        st.session_state.chat = client.chats.create(
            model=MODEL
        )

        st.rerun()

    st.divider()

    st.caption("Status")

    st.success("Gemini connected")

    st.divider()

    st.caption("Nova")

    st.write(
        "A voice and text assistant built with "
        "Streamlit and Gemini."
    )


if not st.session_state.messages:

    st.markdown("""
    <div class="hero">
        <h1>What can I help with?</h1>
        <p>Ask anything. Type it or use your microphone.</p>
    </div>
    """, unsafe_allow_html=True)


for message in st.session_state.messages:

    if message["role"] == "user":
        css = "user"
    else:
        css = "assistant"

    st.markdown(
        f"""
        <div class="message {css}">
            {message["content"]}
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown(
    '<div class="status">🎙️ Voice input</div>',
    unsafe_allow_html=True
)


audio = st.audio_input(
    "Speak to Nova"
)


if audio is not None:

    audio_id = str(audio.size)

    if st.session_state.get("last_audio") != audio_id:

        st.session_state.last_audio = audio_id

        text = transcribe_audio(audio)

        if text:

            st.session_state.messages.append({
                "role": "user",
                "content": text
            })

            with st.spinner("Thinking..."):

                answer = ask_gemini(text)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

            speak(answer)

            st.rerun()

        elif text == "":

            st.warning(
                "I couldn't understand the audio."
            )

        else:

            st.error(
                "Speech recognition service is unavailable."
            )


prompt = st.chat_input(
    "Message Nova..."
)


if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.spinner("Thinking..."):

        answer = ask_gemini(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    speak(answer)

    st.rerun()