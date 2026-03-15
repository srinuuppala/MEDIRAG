from langchain_core.tools import tool
from rag.vector_store import get_report

@tool
def retrieve_medical_report(report_id: str) -> dict:
    """Retrieve stored medical report analysis by report ID."""
    report = get_report(report_id)
    if report:
        return {
            "report_id": report_id,
            "content": report["content"],
            "metadata": report["metadata"],
            "status": "success"
        }
    return {
        "report_id": report_id,
        "status": "not_found",
        "message": "Report not found in vector store."
    }

retrieval_agent = retrieve_medical_report

