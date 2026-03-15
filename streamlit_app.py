import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
from utils.pdf_reader import load_pdf
# from utils.ocr_reader import read_image  # Skip OCR for now to avoid Tesseract
from utils.report_id_generator import generate_report_id
from rag.vector_store import store_report
from workflows.medical_workflow import app as workflow_app
import json

def format_analysis_value(value):
    """Format value for markdown display"""
    if isinstance(value, dict):
        return json.dumps(value, indent=2, ensure_ascii=False)
    elif isinstance(value, list):
        return "\n".join([f"- {format_analysis_value(item)}" for item in value])
    else:
        return str(value)

load_dotenv()

st.set_page_config(page_title="MediRAG - Streamlit", layout="wide", initial_sidebar_state="expanded")

st.title("🩺 MediRAG - AI Medical Report Analyzer")
st.markdown("**Upload file or enter text manually for AI-powered medical analysis & recommendations**")

# Sidebar for input options
with st.sidebar:
    st.header("📤 Input Method")
    input_method = st.radio("Choose input:", ["Upload File", "Manual Text"])
    
    if input_method == "Upload File":
        uploaded_file = st.file_uploader("Choose PDF or image", type=['pdf', 'png', 'jpg', 'jpeg', 'tiff'])
    else:
        manual_text = st.text_area("Enter medical report text:", height=200, placeholder="Paste your medical report, lab results, or prescription text here...")
    
    if st.button("🔬 Analyze Report", type="primary"):
        pass  # Trigger below

# Main content
if 'result' not in st.session_state:
    st.session_state.result = None
    st.session_state.report_id = None

col1, col2 = st.columns([1, 3])

if input_method == "Upload File" and uploaded_file is not None:
    # Save uploaded file
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        file_path = tmp_file.name
    
    try:
        if uploaded_file.name.lower().endswith('.pdf'):
            text = load_pdf(file_path)
        else:
            st.warning("OCR not available. Use PDF or manual text.")
            text = ""
        
        os.unlink(file_path)
        
        with col1:
            st.info(f"✅ Text extracted: {len(text)} chars")
        
        # Process
        report_id = generate_report_id()
        state = {"text": text}
        result = workflow_app.invoke(state)
        
        full_content = f"Text: {text} | Analysis: {json.dumps(result)}"
        store_report(report_id, full_content)
        
        st.session_state.result = result
        st.session_state.report_id = report_id
        
        st.success(f"Analysis complete! Report ID: **{report_id}** 🎉")
        st.balloons()
        
    except Exception as e:
        st.error(f"Error: {str(e)}")

elif input_method == "Manual Text" and manual_text:
    if st.button("🔬 Analyze Report", type="primary"):
        # Process manual text
        report_id = generate_report_id()
        state = {"text": manual_text.strip()}
        result = workflow_app.invoke(state)
        
        full_content = f"Text: {manual_text} | Analysis: {json.dumps(result)}"
        store_report(report_id, full_content)
        
        st.session_state.result = result
        st.session_state.report_id = report_id
        
        st.success(f"Analysis complete! Report ID: **{report_id}** 🎉")
        st.balloons()

# Display results
if st.session_state.result:
    result = st.session_state.result
    report_id = st.session_state.report_id
    
    st.markdown("---")
    st.header("📋 Results")
    
    col_id, col_copy = st.columns(2)
    with col_id:
        st.metric("Report ID", report_id)
    with col_copy:
        st.button("📋 Copy ID", on_click=lambda: st.write(report_id))
    
    # Medical Values
    medical_values = result.get("medical_values", {})
    if medical_values:
        st.subheader("💉 Medical Values")
        for key, value in medical_values.items():
            st.metric(key.replace("_", " ").title(), value)
    
    # Analysis
    analysis = result.get("analysis", {})
    if analysis:
        with st.expander("📊 Detailed Analysis", expanded=True):
            for key, value in analysis.items():
                st.markdown(f"**{key.replace('_', ' ').title()}**")
                st.markdown(format_analysis_value(value))
    
    # Explanation
    explanation = result.get("explanation", "")
    if explanation:
        st.subheader("📝 Full Explanation")
        st.markdown(explanation)
    
    # Recommendations
    recommendations = result.get("recommendations", "")
    if recommendations:
        st.subheader("💡 Recommendations")
        st.info(recommendations)

# Retrieve section
st.markdown("---")
st.header("🔍 Retrieve Past Report")
retrieve_id = st.text_input("Enter Report ID:")
if st.button("Retrieve") and retrieve_id:
    from rag.vector_store import get_report
    report = get_report(retrieve_id)
    if report:
        st.success("Report found!")
        st.json(report)
    else:
        st.warning("Report not found.")

def format_analysis_value(value):
    """Format value for markdown display"""
    if isinstance(value, dict):
        return json.dumps(value, indent=2, ensure_ascii=False)
    elif isinstance(value, list):
        return "\n".join([f"- {format_analysis_value(item)}" for item in value])
    else:
        return str(value)

# Footer
st.markdown("---")
st.caption("Powered by LangGraph + Groq + Streamlit")