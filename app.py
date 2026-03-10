import streamlit as st

import report_analyzer
import drug_interaction
import symptom_checker
import disease_predictor
import medicine_alternative
import health_chatbot


st.set_page_config(
    page_title="AI Health Assistant",
    layout="wide"
)


# ---------- TITLE ----------
st.title("🩺 AI Health Assistant")

st.write(
"""
AI-powered tools to help understand medical reports, symptoms,
drug interactions, disease risks, and general health questions.
"""
)


# ---------- SIDEBAR ----------
st.sidebar.title("Health Tools")


# Language selection
language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "Hindi", "Telugu"]
)

# store language globally
st.session_state["language"] = language


# Tool navigation
page = st.sidebar.radio(
    "Choose a tool",
    [
        "📄 Medical Report Analyzer",
        "💊 Drug Interaction Checker",
        "🤒 Symptom Checker",
        "📊 Disease Risk Predictor",
        "🔎 Medicine Alternative Finder",
        "🧠 AI Health Chat Assistant"
    ]
)


# ---------- MODULE ROUTING ----------
if page == "📄 Medical Report Analyzer":
    report_analyzer.run()

elif page == "💊 Drug Interaction Checker":
    drug_interaction.run()

elif page == "🤒 Symptom Checker":
    symptom_checker.run()

elif page == "📊 Disease Risk Predictor":
    disease_predictor.run()

elif page == "🔎 Medicine Alternative Finder":
    medicine_alternative.run()

elif page == "🧠 AI Health Chat Assistant":
    health_chatbot.run()


# ---------- DISCLAIMER ----------
st.markdown("---")

st.caption(
    "⚠ **Disclaimer:** This AI Health Assistant provides general health information "
    "for educational purposes only. It is not intended to replace professional medical "
    "advice, diagnosis, or treatment. Always consult a qualified healthcare provider "
    "for medical concerns."
)