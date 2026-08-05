from langchain_huggingface import HuggingFaceEmbeddings
from backend.config import EMBEDDING_MODEL


def get_embeddings():
    """
    Return HuggingFace embedding model.
    """
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )