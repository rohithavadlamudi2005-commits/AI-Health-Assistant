import streamlit as st
from groq import Groq
from utils import translate_text, speak


client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def ask_health_ai(question):

    prompt = f"""
You are a helpful AI health assistant.

Answer the following health question clearly and simply.

Rules:
- Provide general health information only
- Do not diagnose diseases
- Encourage consulting a healthcare professional

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def run():

    st.header("🧠 AI Health Chat Assistant")

    question = st.text_input(
        "Ask a health question",
        placeholder="What causes high blood pressure?"
    )

    if st.button("Ask AI"):

        if question.strip() == "":
            st.warning("Please enter a question.")
            return

        with st.spinner("Thinking..."):
            result = ask_health_ai(question)

        language = st.session_state.get("language", "English")

        translated = translate_text(result, language)

        st.subheader("AI Response")

        st.write(translated)

        speak(translated, language)

        st.caption(
            "⚠ This AI assistant provides general health information and is not medical advice."
        )