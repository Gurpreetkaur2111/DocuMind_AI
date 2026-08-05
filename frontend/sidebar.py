import streamlit as st

from frontend.upload import process_uploaded_pdfs
from frontend.chat import clear_conversation, reset_all


def render_sidebar():
    """Render the application sidebar."""

    with st.sidebar:

        st.markdown("### 📁 Document Upload")

        uploaded_files = st.file_uploader(
            "Upload DMPC Ordinance PDFs",
            type=["pdf"],
            accept_multiple_files=True,
            help="Select one or more PDF files to analyze",
            key="pdf_uploader"
        )

        if uploaded_files:

            if len(uploaded_files) != st.session_state.uploaded_files_count:

                if st.button("🚀 Process PDFs", type="primary"):
                    process_uploaded_pdfs(uploaded_files)

        st.markdown("---")

        # Status
        if st.session_state.pdfs_processed:
            st.success(
                f"✓ {st.session_state.uploaded_files_count} PDF(s) loaded"
            )
        else:
            st.info("📤 Please upload PDF files to begin")

        st.markdown("---")

        # Actions
        st.markdown("### ⚙️ Actions")

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                "🗑️ Clear Chat",
                disabled=not st.session_state.messages
            ):
                clear_conversation()

        with col2:
            if st.button(
                "🔄 Reset All",
                disabled=not st.session_state.pdfs_processed
            ):
                reset_all()

        st.markdown("---")

        # Instructions
        st.markdown("### 📖 How to Use")

        st.markdown("""
        1. **Upload** one or more PDF files
        2. Click **Process PDFs**
        3. **Ask questions**
        4. View AI-generated answers
        """)

        st.markdown("---")

        # About
        st.markdown("### ℹ️ About")

        st.markdown("""
        This chatbot uses **RAG (Retrieval-Augmented Generation)** to answer questions from uploaded DMPC ordinance PDFs.

        - **Model:** Llama 3.3 70B
        - **Embeddings:** HuggingFace MiniLM
        - **Vector Store:** FAISS
        """)