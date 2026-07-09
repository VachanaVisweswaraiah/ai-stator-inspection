import streamlit as st
from streamlit_option_menu import option_menu


SECTIONS = {
    "Data Understanding": "Data Understanding",
    "K-Means": "k-means",
    "Decision Tree": "Decision Tree",
    "Probabilistic Decision Tree": "Probabilistic Decision Tree",
    "Iris PDT": "Iris PDT",
    "Steel Faults PDT": "Steel Faults PDT",
    "Volkswagen PDT": "Volkswagen PDT",
}


def select_section():
    with st.sidebar:
        selected_navigation = option_menu(
            "PMV4 Analytics",
            list(SECTIONS),
            default_index=0,
        )

    return SECTIONS.get(selected_navigation)


__all__ = ["SECTIONS", "select_section"]
