import streamlit as st

from app.ui import render_page_title
from src.data.loaders import load_engineering_data


def render(
    fitting_evaluation,
    render_box_plot,
    render_scatter_plot,
):
    render_page_title("Box and Cylinder Analysis")
    st.header("Synthetic Dataset")
    main_df, _ = fitting_evaluation()
    main_df.drop(
        columns=[
            "fitting_distance",
            "Prediction",
            "Evaluation",
            "fitting_group",
        ],
        inplace=True,
    )
    st.dataframe(main_df, hide_index=True, width=1250)
    st.header("Box-Cylinder Model Range ")
    engineering_data = load_engineering_data()
    st.dataframe(engineering_data, hide_index=True)

    box_tab, scatter_tab = st.tabs(["Box-Plot", "Scatter-Plot"])
    with box_tab:
        st.header("Box-Plot")
        render_box_plot()
    with scatter_tab:
        st.header("Scatter-Plot")
        render_scatter_plot()
