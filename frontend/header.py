import streamlit as st


def render_header():
    """Display the application header."""

    st.markdown(
        """
        <div class="main-header">
            📚 DocuMind AI
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sub-header">
            Ask questions about your uploaded ordinance documents
        </div>
        """,
        unsafe_allow_html=True
    )