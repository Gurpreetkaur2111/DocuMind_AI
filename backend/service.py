from langchain_core.messages import AIMessage

from backend.pdf_loader import load_and_split_pdfs
from backend.vector_store import build_vector_store, build_retriever
from backend.rag_pipeline import build_rag_chain


def process_pdfs(file_paths):
    chunks = load_and_split_pdfs(file_paths)
    vector_store = build_vector_store(chunks)
    retriever = build_retriever(vector_store)
    return build_rag_chain(retriever)


def ask(chain, question, messages=None):

    response = chain.invoke(
        {
            "question": question,
            "history": messages or [],
        }
    )

    print(type(response))
    print(repr(response))

    # AIMessage
    if isinstance(response, AIMessage):
        return response.content

    # LangChain TextAccessor
    if hasattr(response, "text"):
        return response.text

    # Normal string
    if isinstance(response, str):
        return response

    return str(response)