from langgraph.graph import StateGraph
from typing_extensions import TypedDict, Annotated
import operator

# Define state schema (replaces state.py)
class MedicalState(TypedDict):
    text: str
    classification: str
    entities: dict
    patient_info: dict
    medical_values: dict
    analysis: dict
    explanation: str
    recommendations: str
    prescriptions: list
    urgency: str

from agents.classifier_agent import classify_agent
from agents.entity_extractor_agent import extractor_agent
from agents.patient_info_agent import patient_agent
from agents.analysis_agent import analysis_agent
from agents.response_agent import response_agent

graph = StateGraph(MedicalState)

graph.add_node("classifier", classify_agent)
graph.add_node("extractor", extractor_agent)
graph.add_node("patient", patient_agent)
graph.add_node("analysis", analysis_agent)
graph.add_node("response", response_agent)

graph.set_entry_point("classifier")

graph.add_edge("classifier", "extractor")
graph.add_edge("extractor", "patient")
graph.add_edge("patient", "analysis")
graph.add_edge("analysis", "response")

app = graph.compile()

