import streamlit as st
from groq import Groq

st.write("DEBUG: Symptom checker loaded")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def analyze_symptoms(symptoms):

    st.write("DEBUG: Calling Groq API")

    prompt = f"User symptoms: {symptoms}. Suggest possible conditions."

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write("DEBUG: Response received")

    return response.choices[0].message.content


def run(agent_input=None):

    st.header("🤒 Symptom Checker")

    # ---------- AGENT MODE ----------
    if agent_input:

        st.info(f"Detected symptoms: {agent_input}")

        with st.spinner("Analyzing symptoms..."):

            result = analyze_symptoms(agent_input)

        st.subheader("🧠 AI Health Insight")
        st.write(result)

        st.caption(
            "⚠ This tool provides general health information and is not a medical diagnosis."
        )

        return


    # ---------- MANUAL MODE ----------
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
        st.write(result)

        st.caption(
            "⚠ This tool provides general health information and is not a medical diagnosis."
        )