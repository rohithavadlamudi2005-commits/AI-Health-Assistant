import streamlit as st


def run():

    st.header("📊 Disease Risk Predictor")

    st.write("Estimate your risk for diabetes or heart disease based on health indicators.")

    age = st.number_input("Age", min_value=1, max_value=120)

    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0)

    blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=60, max_value=200)

    glucose = st.number_input("Glucose Level (mg/dL)", min_value=50, max_value=300)

    cholesterol = st.number_input("Cholesterol Level (mg/dL)", min_value=100, max_value=400)

    smoking = st.selectbox("Do you smoke?", ["No", "Yes"])

    exercise = st.selectbox("Do you exercise regularly?", ["Yes", "No"])

    family_history = st.selectbox("Family history of diabetes/heart disease?", ["No", "Yes"])

    if st.button("Predict Risk"):

        risk_score = 0

        if age > 45:
            risk_score += 1

        if bmi > 30:
            risk_score += 1

        if blood_pressure > 140:
            risk_score += 1

        if glucose > 140:
            risk_score += 2

        if cholesterol > 240:
            risk_score += 1

        if smoking == "Yes":
            risk_score += 1

        if exercise == "No":
            risk_score += 1

        if family_history == "Yes":
            risk_score += 1


        st.subheader("Risk Assessment Result")

        if risk_score >= 5:
            st.error("⚠ High Risk of Diabetes or Heart Disease")

        elif risk_score >= 3:
            st.warning("⚠ Moderate Risk")

        else:
            st.success("✅ Low Risk")


        st.caption("⚠ This tool provides an estimate and is not a medical diagnosis.")