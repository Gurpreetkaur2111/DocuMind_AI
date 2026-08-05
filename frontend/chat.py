import streamlit as st
from backend.service import ask


def clear_conversation():
    st.session_state.messages = []
    st.rerun()


def reset_all():
    st.session_state.chain = None
    st.session_state.messages = []
    st.session_state.pdfs_processed = False
    st.session_state.uploaded_files_count = 0
    st.rerun()


def display_chat_history():
    """Display conversation."""

    if not st.session_state.messages:
        st.info("👇 Type your question below to get started!")
        return

    st.markdown("### 💬 Conversation")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def handle_chat():

    question = st.chat_input("Ask a question about your documents...")

    if not question:
        return

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.spinner("🤔 Thinking..."):

        try:

            history = st.session_state.messages[:-1]

            response = ask(
                chain=st.session_state.chain,
                question=question,
                messages=history
            )

            if isinstance(response, str):
                answer = response
            elif hasattr(response, "content"):
                answer = response.content
            elif hasattr(response, "text"):
                answer = response.text
            else:
                answer = str(response)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()

        except Exception as e:
            st.error(f"❌ {str(e)}")


def render_chat():

    if not st.session_state.pdfs_processed:
        st.info("👈 Please upload and process PDFs first.")
        return

    display_chat_history()
    handle_chat()