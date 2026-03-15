from sentence_transformers import SentenceTransformer

# Load the embedding model once globally
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding_model():
    """Get the global embedding model instance."""
    return model

def encode(text: str):
    """Encode text to embedding vector."""
    return model.encode(text).tolist()

