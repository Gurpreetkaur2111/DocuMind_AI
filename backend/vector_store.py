from langchain_community.vectorstores import FAISS
from backend.embeddings import get_embeddings
from backend.config import RETRIEVER_K


def build_vector_store(chunks):
    embeddings = get_embeddings()
    return FAISS.from_documents(chunks, embeddings)


def build_retriever(vector_store):
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": RETRIEVER_K},
    )