import json
from llm_model import llm

def extractor_agent(state):
    text = state["text"]
    
    prompt = f"""
Extract ALL medical test values as numbers ONLY.

Report: {text}

Return STRICT JSON:

{{
  "hemoglobin": 13.5,
  "blood_sugar": 131,
  "platelets": 235000,
  "cholesterol": 218,
  "wbc": 7500
}}

Numbers only. If not found, omit key. JSON ONLY.
"""
    
    result = llm.invoke(prompt)
    
    # Robust JSON parsing
    try:
        # Clean response
        cleaned = result.content.strip()
        start = cleaned.find('{')
        end = cleaned.rfind('}') + 1
        json_str = cleaned[start:end]
        values = json.loads(json_str)
    except:
        values = {}
    
    print("EXTRACTED VALUES:", values)
    state["medical_values"] = values
    return state

