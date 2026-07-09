import streamlit as st


APP_TITLE = "PMV4 Analytics"


def configure_page():
    st.set_page_config(
        page_title=APP_TITLE,
        layout="wide",
    )


def render_page_title(title):
    st.title(title)


__all__ = ["APP_TITLE", "configure_page", "render_page_title"]
