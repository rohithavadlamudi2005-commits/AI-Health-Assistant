from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def health_agent(user_query):

    prompt = f"""
You are an AI routing agent.

Your job is to decide which healthcare tool should handle the user query.

Available tools:

symptom → for symptoms like fever, headache, pain
drug → for drug interactions
report → for medical report analysis
disease → for disease risk prediction
medicine → for medicine alternatives
chat → general health questions

User Query:
{user_query}

Respond with ONLY one word:

symptom
drug
report
disease
medicine
chat
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    decision = response.choices[0].message.content.strip().lower()

    return decision