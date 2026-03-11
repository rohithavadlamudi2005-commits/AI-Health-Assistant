import streamlit as st
from groq import Groq
from utils import translate_text, speak

# Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])


# AI function
def get_alternatives(medicine):

    prompt = f"""
You are a medical assistant.

A user wants alternatives for the medicine: {medicine}

Tasks:
1. Identify the active ingredient.
2. Suggest 3 to 5 alternative medicines that contain the same ingredient.
3. Keep explanation short.

Format:

Active Ingredient:
Alternatives:
1.
2.
3.

Note:
Remind user to consult a doctor before switching medicines.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# Streamlit module
def run(agent_input=None):

    st.header("🔎 Medicine Alternative Finder")

    st.write("Find alternative medicines with the same active ingredient.")

    # If called by agent
    if agent_input:
        medicine = agent_input
        st.info(f"Detected medicine query: {medicine}")
    else:
        medicine = st.text_input(
            "Enter medicine name",
            placeholder="e.g., Paracetamol"
        )

    if st.button("Find Alternatives") or agent_input:

        if medicine.strip() == "":
            st.warning("Please enter a medicine name.")
            return

        with st.spinner("Finding alternatives..."):

            result = get_alternatives(medicine)

        st.subheader("💊 Possible Alternatives")

        language = st.session_state.get("language", "English")

        translated = translate_text(result, language)

        st.write(translated)

        speak(translated, language)

        st.caption(
            "⚠ This information is for educational purposes only and not medical advice."
        )