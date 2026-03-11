import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def analyze_symptoms(symptoms):

    prompt = f"""
User symptoms: {symptoms}

Suggest possible conditions and advice.
Do not diagnose.
Keep explanation simple.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def run(agent_input=None):

    st.header("🤒 Symptom Checker")

    symptoms = st.text_area(
        "Enter symptoms",
        value=agent_input if agent_input else ""
    )

    if st.button("Analyze Symptoms"):

        if symptoms.strip() == "":
            st.warning("Please enter symptoms")
            return

        with st.spinner("Analyzing..."):

            result = analyze_symptoms(symptoms)

        st.subheader("AI Result")

        st.write(result)