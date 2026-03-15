from langgraph.graph import StateGraph
from state import MedicalState

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

graph.add_edge("classifier","extractor")
graph.add_edge("extractor","patient")
graph.add_edge("patient","analysis")
graph.add_edge("analysis","response")

app = graph.compile()