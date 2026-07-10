import streamlit as st

from app.ui import render_page_title
from src.models.workflows import df_fitting_and_evaluation_iris


def render():
    from iris_viz import iris_probabilistic_decision_tree_viz

    render_page_title("IRIS Dataset Analysis")
    st.header("Iris Dataset")
    dataframe = df_fitting_and_evaluation_iris()
    st.dataframe(dataframe, hide_index=True, width=1250)
    depth = st.slider(
        "Select the Depth of the Probabilistic Tree for Iris dataset",
        min_value=1,
        max_value=6,
        value=4,
        step=1,
    )
    iris_probabilistic_decision_tree_viz(depth)
