import pandas as pd
import streamlit as st

from app.ui import render_page_title
from src.data.loaders import load_vw_sample_data
from src.models.workflows import (
    df_fitting_and_evaluation_vw_sample,
)


UNNECESSARY_COLUMNS = [
    "pin_position",
    "stator_id",
    "ProduktID",
    "Pinbezeichnung",
    "left_pin_id",
    "right_pin_id",
    "Drahtprüfung_Ergebnis_x",
    "Pin_ID_x",
    "Dachbiegen_Ergebnis_x",
    "Pin_Type_x",
    "3D_Biegen_Ergebnis_x",
    "Abisolieren_eval_x",
    "Drahtprüfung_Ergebnis_y",
    "Pin_ID_y",
    "Dachbiegen_Ergebnis_y",
    "Pin_Type_y",
    "3D_Biegen_Ergebnis_y",
    "Ergebnis",
]
DEFAULT_DROPPED_FEATURES = ["Abstand_Pins_vertikal"]


def render():
    from vw_sample_data_viz import (
        vw_sample_probabilistic_decision_tree_viz,
    )

    available_features = load_vw_sample_data().drop(
        columns=UNNECESSARY_COLUMNS
    )
    render_page_title("Volkswagen Dataset Analysis")
    st.header("Volkswagen Dataset")
    dataframe = df_fitting_and_evaluation_vw_sample()
    st.dataframe(dataframe, hide_index=True, width=1250)
    depth = st.slider(
        (
            "Select the Depth of the Probabilistic Tree for "
            "VW Sample dataset"
        ),
        min_value=1,
        max_value=10,
        value=5,
        step=1,
    )

    if "vw_applied_drop" not in st.session_state:
        st.session_state.vw_applied_drop = DEFAULT_DROPPED_FEATURES.copy()
    if "vw_drop" not in st.session_state:
        st.session_state.vw_drop = DEFAULT_DROPPED_FEATURES.copy()

    st.multiselect(
        "Choose the features to be dropped (Optional)",
        available_features.columns.tolist(),
        default=st.session_state.vw_drop,
        key="vw_drop",
    )

    pending_drop = st.session_state.vw_drop
    applied_drop = st.session_state.vw_applied_drop
    show_body = pending_drop == applied_drop

    if not show_body and len(pending_drop) == 0:
        st.session_state.vw_applied_drop = []
        applied_drop = []
        show_body = True
    elif not show_body:
        st.write("You have selected following features to be dropped:")
        selected_features = pd.DataFrame(
            pending_drop,
            columns=["Features Dropped"],
        )
        st.dataframe(selected_features, width=200, hide_index=True)
        if st.button("Update"):
            st.session_state.vw_applied_drop = pending_drop
            applied_drop = pending_drop
            show_body = True

    if show_body:
        vw_sample_probabilistic_decision_tree_viz(
            depth,
            applied_drop,
        )
