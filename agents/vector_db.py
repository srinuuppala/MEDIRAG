import chromadb
from sentence_transformers import SentenceTransformer
import uuid

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("medical_reports")

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_report_id():
    return str(uuid.uuid4()).replace('-', '').upper()[:8]

def store_report(report_id, content, metadata=None):
    if metadata is None:
        metadata = {}
    embedding = model.encode(content).tolist()
    collection.add(
        documents=[content],
        ids=[report_id],
        metadatas=[{"type": "medical_report", **metadata}],
        embeddings=[embedding]
    )

def get_report(report_id):
    results = collection.get(
        ids=[report_id],
        include=["documents", "metadatas"]
    )
    if results and results['documents']:
        return {
            "content": results['documents'][0],
            "metadata": results['metadatas'][0] if results['metadatas'] else {}
        }
    return None
