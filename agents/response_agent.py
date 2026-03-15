from llm_model import llm

def response_agent(state):
    patient = state.get("patient_info", {})
    values = state.get("medical_values", {})
    analysis = state.get("analysis", {})

    prompt = f"""
Based on this medical data, write BEAUTIFUL structured explanation EXACTLY like this format:

📝 **Full Report Analysis for {patient.get('name', 'Patient')}**

**1. Patient Information**  
{patient.get('name', 'Unknown')} is a {patient.get('age', '?')} year old {patient.get('gender', 'patient')}.  
**Doctor**: {patient.get('doctor', 'TBD')} | **Date**: {patient.get('report_date', 'TBD')}

**2. Test Results**  
{chr(10).join([f"- **{{k.title()}}**: {{v}}" for k,v in values.items()])}

**3. Health Assessment**  
{analysis.get('risk_explanation', 'Consult doctor for detailed analysis')}

**🔴 Health Recommendations**  
• Monitor diet and exercise  
• Schedule follow-up with doctor  
• {{analysis.get('top_recommendation', 'Regular checkups recommended')}}

**Next Steps:** Book appointment with your doctor to discuss these results.

Keep exactly this markdown format with emojis and structure. Make it professional and caring.
"""

    result = llm.invoke(prompt)
    state["explanation"] = result.content
    return state

