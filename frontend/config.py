import streamlit as st


def configure_page():
    """Configure the Streamlit page settings."""

    st.set_page_config(
        page_title="DMPC Ordinance Chatbot",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )