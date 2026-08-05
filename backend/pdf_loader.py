"""
pdf_loader.py

Handles loading PDF documents and splitting them into
smaller chunks for the RAG pipeline.
"""

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.config import CHUNK_SIZE, CHUNK_OVERLAP


def load_and_split_pdfs(file_paths: list):
    """
    Load one or more PDF files and split them into
    smaller overlapping text chunks.

    Args:
        file_paths (list):
            List of PDF file paths.

    Returns:
        list:
            List of LangChain Document chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    all_chunks = []

    for path in file_paths:

        loader = PyPDFLoader(path)

        chunks = splitter.split_documents(
            loader.lazy_load()
        )

        all_chunks.extend(chunks)

    return all_chunks