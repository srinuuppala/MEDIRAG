import json
from llm_model import llm

def analysis_agent(state):
    values = state.get("medical_values", {})
    patient = state.get("patient_info", {})
    
    prompt = f"""
Analyze for patient {patient.get('name', 'Patient')}:

Values: {json.dumps(values)}

For each value:
1. Status: normal/monitor/high/low
2. Risk explanation (1 sentence)
3. Reference range

Return STRICT JSON:
{{
  "overall_status": "normal|monitor|high risk",
  "values_analysis": [
    {{
      "test": "hemoglobin",
      "status": "normal",
      "risk": "Low risk - normal range",
      "range": "13.5-17.5 g/dL"
    }}
  ],
  "urgent": false
}}

JSON ONLY.
"""
    
    result = llm.invoke(prompt)
    
    try:
        cleaned = result.content.strip()
        start = cleaned.find('{')
        end = cleaned.rfind('}') + 1
        json_str = cleaned[start:end]
        analysis = json.loads(json_str)
    except:
        analysis = {"error": "Consult doctor"}
    
    state["analysis"] = analysis
    return state

