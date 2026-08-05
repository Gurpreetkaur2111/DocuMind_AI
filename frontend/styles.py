import streamlit as st


def load_css():
    """Load custom CSS for the application."""

    st.markdown("""
        <style>
        .stApp {
            background-color: #1a1a1a;
        }

        .main-header {
            font-size: 2.5rem;
            font-weight: 700;
            color: #64b5f6;
            text-align: center;
            margin-bottom: 0.5rem;
        }

        .sub-header {
            font-size: 1.1rem;
            color: #b0b0b0;
            text-align: center;
            margin-bottom: 2rem;
        }

        .chat-message {
            padding: 1.5rem;
            border-radius: 0.8rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }

        .user-message {
            background-color: #1e3a5f;
            border-left: 4px solid #4a9eff;
        }

        .assistant-message {
            background-color: #2d2d2d;
            border-left: 4px solid #66bb6a;
        }

        .message-role {
            font-weight: 600;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .message-content {
            line-height: 1.6;
            color: #e0e0e0;
        }

        .stButton > button {
            width: 100%;
            border-radius: 0.5rem;
            font-weight: 600;
        }

        .upload-section {
            background-color: #2d2d2d;
            padding: 1.5rem;
            border-radius: 0.8rem;
            border: 2px dashed #444;
            margin-bottom: 1rem;
        }

        section[data-testid="stSidebar"] {
            background-color: #242424;
        }

        section[data-testid="stSidebar"] .stMarkdown {
            color: #e0e0e0;
        }

        .stTextInput > div > div > input {
            background-color: #2d2d2d;
            color: #e0e0e0;
        }

        .stAlert {
            background-color: #2d2d2d;
            color: #e0e0e0;
        }

        </style>
    """, unsafe_allow_html=True)
    