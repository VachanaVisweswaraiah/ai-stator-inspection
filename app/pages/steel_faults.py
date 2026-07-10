import streamlit as st

from app.ui import render_page_title
from src.models.workflows import (
    df_fitting_and_evaluation_steel_faults,
)


def render():
    from steel_faults_viz import (
        steel_faults_probabilistic_decision_tree_viz,
    )

    render_page_title("Steel Faults Dataset Analysis")
    st.header("Steel Faults Dataset")
    dataframe = df_fitting_and_evaluation_steel_faults()
    st.dataframe(dataframe, hide_index=True, width=1250)
    depth = st.slider(
        (
            "Select the Depth of the Probabilistic Tree for "
            "steel faults dataset"
        ),
        min_value=1,
        max_value=30,
        value=20,
        step=1,
    )
    steel_faults_probabilistic_decision_tree_viz(depth)
