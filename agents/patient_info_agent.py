import json
from llm_model import llm

def patient_agent(state):
    text = state["text"]
    
    prompt = f"""
Extract patient info ONLY.

Report: {text}

Return STRICT JSON:
{{
  "name": "Vikram Joshi",
  "age": 48,
  "gender": "Male",
  "doctor": "Dr. Rakesh Mehta",
  "report_date": "2026-03-15"
}}

JSON ONLY.
"""
    
    result = llm.invoke(prompt)
    
    try:
        cleaned = result.content.strip()
        start = cleaned.find('{')
        end = cleaned.rfind('}') + 1
        json_str = cleaned[start:end]
        info = json.loads(json_str)
    except:
        info = {"name": "Unknown", "age": "?", "gender": "?"}
    
    state["patient_info"] = info
    return state

