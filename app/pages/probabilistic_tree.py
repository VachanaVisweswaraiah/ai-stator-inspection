import streamlit as st

from app.ui import render_page_title


def render(fitting_evaluation, render_visualization):
    render_page_title("Box and Cylinder Analysis")
    st.header("Predictions for Synthetic Dataset")
    _, evaluated_data = fitting_evaluation()
    st.dataframe(evaluated_data, hide_index=True, width=1250)
    depth = st.slider(
        "Select the Depth of the Probabilistic Tree",
        min_value=1,
        max_value=6,
        value=4,
        step=1,
    )
    render_visualization(depth)
