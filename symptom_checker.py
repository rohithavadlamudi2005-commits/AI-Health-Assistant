import streamlit as st
from groq import Groq
from utils import translate_text, speak

# GROQ CLIENT
client = Groq(api_key=st.secrets["GROQ_API_KEY"])


# AI FUNCTION
def analyze_symptoms(symptoms):

    prompt = f"""
You are a helpful medical assistant.

A user reports these symptoms:

{symptoms}

Tasks:
1. Suggest possible health conditions related to these symptoms.
2. Give a short explanation for each condition.
3. Provide general advice.

Rules:
- Do NOT diagnose.
- Keep explanations simple.
- Recommend consulting a doctor if symptoms are severe.

Format:

Possible Conditions:
1.
2.
3.

Advice:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# STREAMLIT MODULE
def run():

    st.header("🤒 Symptom Checker")

    st.write("Enter symptoms to see possible health conditions.")

    symptoms = st.text_area(
        "Enter symptoms (comma separated)",
        placeholder="fever, cough, headache"
    )

    if st.button("Analyze Symptoms"):

        if symptoms.strip() == "":
            st.warning("Please enter symptoms.")
            return

        with st.spinner("Analyzing symptoms..."):

            result = analyze_symptoms(symptoms)

        st.subheader("🧠 AI Health Insight")

        language = st.session_state.get("language", "English")

        translated = translate_text(result, language)

        st.write(translated)

        speak(translated, language)

        st.caption("⚠ This tool provides general health information and is not a medical diagnosis.")