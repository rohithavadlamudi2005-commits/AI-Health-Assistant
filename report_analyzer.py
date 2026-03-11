import streamlit as st
from pypdf import PdfReader
import easyocr
import re
import pandas as pd
from groq import Groq


# ---------- GROQ CLIENT ----------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])


# ---------- TEXT EXTRACTION ----------
def extract_text(uploaded_file):

    file_type = uploaded_file.name.split(".")[-1].lower()
    text = ""

    if file_type == "pdf":

        reader = PdfReader(uploaded_file)

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

    elif file_type == "txt":

        text = uploaded_file.read().decode("utf-8")

    elif file_type in ["png", "jpg", "jpeg"]:

        reader = easyocr.Reader(['en'])
        result = reader.readtext(uploaded_file)

        for r in result:
            text += r[1] + " "

    return text


# ---------- PARAMETER EXTRACTION ----------
def extract_parameters(text):

    results = []

    patterns = [

        r'([A-Za-z ()]+)\s+(\d+\.?\d*)\s+(High|Low)\s+(\d+\.?\d*)\s*-\s*(\d+\.?\d*)',

        r'([A-Za-z ()]+)\s+(\d+\.?\d*)\s+(\d+\.?\d*)\s*-\s*(\d+\.?\d*)'
    ]

    for pattern in patterns:

        matches = re.findall(pattern, text)

        for m in matches:

            try:

                if len(m) == 5:
                    test, value, status, low, high = m
                else:
                    test, value, low, high = m
                    status = None

                value = float(value)
                low = float(low)
                high = float(high)

                if status is None:

                    if value < low:
                        status = "Low"
                    elif value > high:
                        status = "High"
                    else:
                        status = "Normal"

                results.append({
                    "Test": test.strip(),
                    "Value": value,
                    "Range": f"{low}-{high}",
                    "Status": status
                })

            except:
                pass

    return results


# ---------- AI EXPLANATION ----------
def explain_results(results):

    summary = ""

    for r in results:
        summary += f"{r['Test']} = {r['Value']} ({r['Status']})\n"

    prompt = f"""
You are a helpful medical assistant.

Explain the following blood test results in simple language.

Highlight abnormal parameters and possible health implications.
If values are normal, say they are within the normal range.

Always remind the user that this is not a medical diagnosis.

Results:
{summary}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# ---------- STREAMLIT MODULE ----------
def run(agent_input=None):

    st.header("📄 Medical Report Analyzer")

    st.write("Upload a medical report to analyze health parameters.")

    uploaded_file = st.file_uploader(
        "Upload Medical Report",
        type=["pdf", "png", "jpg", "jpeg", "txt"]
    )

    if uploaded_file:

        with st.spinner("Analyzing report..."):

            text = extract_text(uploaded_file)

            parameters = extract_parameters(text)

            if parameters:

                df = pd.DataFrame(parameters)

                st.subheader("🩺 Report Summary")
                st.dataframe(df, use_container_width=True)

                abnormal = df[df["Status"] != "Normal"]

                if not abnormal.empty:

                    st.subheader("⚠ Abnormal Results")
                    st.dataframe(abnormal, use_container_width=True)

                explanation = explain_results(parameters)

                st.subheader("🧠 AI Health Explanation")
                st.write(explanation)

            else:

                st.warning("Could not detect medical parameters from the report.")