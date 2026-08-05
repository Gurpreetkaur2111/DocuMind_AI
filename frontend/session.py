import streamlit as st


def initialize_session():

    if "chain" not in st.session_state:
        st.session_state.chain = None

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "pdfs_processed" not in st.session_state:
        st.session_state.pdfs_processed = False

    if "uploaded_files_count" not in st.session_state:
        st.session_state.uploaded_files_count = 0