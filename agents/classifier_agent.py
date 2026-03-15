from llm_model import llm

def classify_agent(state):

    text = state["text"]

    prompt = f"""
Classify this document.

Return:
medical_report
prescription
not_medical

Document:
{text}
"""

    result = llm.invoke(prompt)

    state["report_type"] = result.content

    return state