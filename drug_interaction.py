import streamlit as st
import pandas as pd
from groq import Groq


# ---------- GROQ CLIENT ----------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])


# ---------- LLM FUNCTION ----------
def ask_llm(med1, med2):

    prompt = f"""
You are a medical information assistant.

Check if there is a known interaction between:

{med1} and {med2}

Rules:
- If interaction exists, explain briefly.
- If unsure, say "No reliable interaction information found".
- Do not invent medical facts.

Format:

Interaction: Yes / No / Unknown
Risk:
Advice:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# ---------- STREAMLIT MODULE ----------
def run(agent_input=None):

    st.header("💊 Drug Interaction Checker")

    if agent_input:
        st.info(f"Detected medicine query: {agent_input}")

    med1 = st.text_input("Enter first medicine")
    med2 = st.text_input("Enter second medicine")

    if st.button("Check Interaction") or agent_input:

        if med1.strip() == "" or med2.strip() == "":
            st.warning("Please enter both medicines")
            return

        med1_input = med1
        med2_input = med2

        med1 = med1.lower().strip()
        med2 = med2.lower().strip()

        try:

            df = pd.read_csv("data/drug_interactions.csv")

            # normalize dataset
            df["drug1"] = df["drug1"].astype(str).str.lower().str.strip()
            df["drug2"] = df["drug2"].astype(str).str.lower().str.strip()

            result = df[
                ((df["drug1"] == med1) & (df["drug2"] == med2)) |
                ((df["drug1"] == med2) & (df["drug2"] == med1))
            ]

            if not result.empty:

                st.error("⚠ Interaction Found (Dataset)")
                st.write(result.iloc[0]["interaction"])

            else:

                st.info("No interaction found in dataset. Checking with AI...")

                with st.spinner("Analyzing..."):
                    answer = ask_llm(med1_input, med2_input)

                st.subheader("🧠 AI Insight")
                st.write(answer)

        except:

            st.warning("Dataset not available. Using AI.")

            answer = ask_llm(med1_input, med2_input)

            st.write(answer)

    st.caption("⚠ This tool provides general information and is not medical advice.")