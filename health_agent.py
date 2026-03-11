from symptom_checker import analyze_symptoms
from drug_interaction import check_interaction
from report_analyzer import analyze_report
from medicine_alternative import find_alternative

def health_agent(user_query):
    query = user_query.lower()

    if "fever" in query or "pain" in query or "symptom" in query:
        return analyze_symptoms(user_query)

    elif "interaction" in query or "drug" in query:
        return check_interaction(user_query)

    elif "report" in query or "blood" in query:
        return analyze_report(user_query)

    elif "alternative" in query:
        return find_alternative(user_query)

    else:
        return "Please provide more details about your health concern."