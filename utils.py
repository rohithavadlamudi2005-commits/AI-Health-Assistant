import streamlit as st
from groq import Groq
from gtts import gTTS
import tempfile

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def translate_text(text, language):

    if language == "English":
        return text

    prompt = f"""
Translate the following health information into {language}.
Keep it simple so common people can understand.

Text:
{text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def speak(text, language):

    lang_code = {
        "English": "en",
        "Hindi": "hi",
        "Telugu": "te"
    }

    tts = gTTS(text=text, lang=lang_code.get(language, "en"))

    tmp = tempfile.NamedTemporaryFile(delete=False)

    tts.save(tmp.name)

    st.audio(tmp.name)