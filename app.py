import streamlit as st

import report_analyzer
import drug_interaction
import symptom_checker
import disease_predictor
import medicine_alternative
import health_chatbot
from health_agent import health_agent


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

language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "Hindi", "Telugu"]
)

st.session_state["language"] = language


page = st.sidebar.radio(
    "Choose a tool",
    [
        "🤖 Agentic Health Assistant",
        "📄 Medical Report Analyzer",
        "💊 Drug Interaction Checker",
        "🤒 Symptom Checker",
        "📊 Disease Risk Predictor",
        "🔎 Medicine Alternative Finder",
        "🧠 AI Health Chat Assistant"
    ]
)

# ---------- AGENTIC AI MODE ----------

if page == "🤖 Agentic Health Assistant":

    st.header("🤖 Agentic AI Health Assistant")

    st.write(
        "Ask any health-related question. The AI agent will decide which tool to use."
    )

    user_query = st.text_input("Enter your health question")

    if st.button("Analyze"):

        decision = health_agent(user_query)

        if decision == "symptom":
            st.success("Agent selected: Symptom Checker")
            symptom_checker.run(user_query)

        elif decision == "drug":
            st.success("Agent selected: Drug Interaction Checker")
            drug_interaction.run(user_query)

        elif decision == "report":
            st.success("Agent selected: Medical Report Analyzer")
            report_analyzer.run()

        elif decision == "disease":
            st.success("Agent selected: Disease Risk Predictor")
            disease_predictor.run()

        elif decision == "medicine":
            st.success("Agent selected: Medicine Alternative Finder")
            medicine_alternative.run(user_query)

        else:
            st.success("Agent selected: AI Health Chat Assistant")
            health_chatbot.run()


# ---------- MANUAL TOOL ROUTING ----------

elif page == "📄 Medical Report Analyzer":
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
    "⚠ Disclaimer: This AI Health Assistant provides general health information "
    "for educational purposes only. It is not intended to replace professional "
    "medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider."
)