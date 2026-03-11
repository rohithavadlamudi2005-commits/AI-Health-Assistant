def health_agent(user_query):

    query = user_query.lower()

    if "symptom" in query or "fever" in query or "pain" in query:
        return "symptom"

    elif "interaction" in query or "drug" in query:
        return "drug"

    elif "report" in query or "blood" in query:
        return "report"

    elif "risk" in query or "disease":
        return "disease"

    elif "alternative" in query:
        return "medicine"

    else:
        return "chat"