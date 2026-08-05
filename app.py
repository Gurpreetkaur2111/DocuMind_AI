
from frontend.config import configure_page
from frontend.session import initialize_session
from frontend.styles import load_css
from frontend.sidebar import render_sidebar
from frontend.header import render_header
from frontend.chat import render_chat


def main():
    # Configure Streamlit page
    configure_page()

    # Initialize session variables
    initialize_session()

    # Load custom CSS
    load_css()

    # Render sidebar
    render_sidebar()

    # Render main page
    render_header()
    render_chat()


if __name__ == "__main__":
    main()