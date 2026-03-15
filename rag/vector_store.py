import chromadb
from rag.embedding_model import get_embedding_model, encode

client = chromadb.PersistentClient(path="./chroma_db", settings=chromadb.Settings(allow_reset=True))
collection = client.get_or_create_collection("medical_reports")

def store_report(report_id: str, content: str, metadata: dict = None):
    """Store medical report embedding in ChromaDB."""
    if metadata is None:
        metadata = {}
    embedding = encode(content)
    collection.add(
        documents=[content],
        ids=[report_id],
        metadatas=[{"type": "medical_report", **metadata}],
        embeddings=[embedding]
    )

def get_report(report_id: str):
    """Retrieve report from ChromaDB by ID."""
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

