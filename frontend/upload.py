import os
import tempfile
import streamlit as st

from backend.service import process_pdfs

def save_uploaded_files(uploaded_files):
    """
    Save uploaded PDF files into a temporary directory
    and return their file paths.
    """

    temp_dir = tempfile.mkdtemp()
    file_paths = []

    for uploaded_file in uploaded_files:
        file_path = os.path.join(temp_dir, uploaded_file.name)

        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

        file_paths.append(file_path)

    return file_paths


def process_uploaded_pdfs(uploaded_files):
    """
    Process uploaded PDFs and initialize the RAG pipeline.
    """

    with st.spinner("🔄 Processing PDFs... This may take a moment."):

        file_paths = save_uploaded_files(uploaded_files)

        st.session_state.chain = process_pdfs(file_paths)

        st.session_state.pdfs_processed = True
        st.session_state.uploaded_files_count = len(uploaded_files)

    st.success(
        f"✅ Successfully processed {len(uploaded_files)} PDF(s)!"
    )