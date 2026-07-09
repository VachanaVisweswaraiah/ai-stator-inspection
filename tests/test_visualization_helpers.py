from base64 import b64decode
from io import BytesIO

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

from src.config.paths import PROJECT_ROOT
from src.visualization import (
    dataframe_to_excel_download_link,
    serialize_decision_tree,
)


def test_excel_download_link_preserves_dataframe_contents():
    dataframe = pd.DataFrame(
        {
            "feature": [1.5, 2.5],
            "label": ["OK", "NOK"],
        }
    )

    link = dataframe_to_excel_download_link(dataframe)
    encoded_workbook = link.split("base64,", 1)[1].split('"', 1)[0]
    restored = pd.read_excel(BytesIO(b64decode(encoded_workbook)))

    pd.testing.assert_frame_equal(restored, dataframe)
    assert 'download="data.xlsx"' in link
    assert "Download Sample Excel file" in link


def test_tree_serializer_preserves_split_and_leaf_contract():
    features = pd.DataFrame(
        {"measurement": [0.0, 0.1, 0.9, 1.0]}
    )
    labels = [0, 0, 1, 1]
    model = DecisionTreeClassifier(
        max_depth=1,
        random_state=0,
    ).fit(features, labels)

    result = serialize_decision_tree(
        model,
        features.columns,
        {0: "NOK", 1: "OK"},
    )

    assert result["id"] == 0
    assert result["type"] == "split"
    assert result["feature"] == "measurement"
    assert result["left"]["prediction"] == "NOK"
    assert result["right"]["prediction"] == "OK"
    assert result["left"]["samples"] == 1
    assert result["right"]["samples"] == 1
    assert result["left"]["class_distribution"] == [1.0, 0.0]
    assert result["right"]["class_distribution"] == [0.0, 1.0]


def test_streamlit_modules_use_shared_visualization_helpers():
    for relative_path in [
        "main.py",
        "iris_viz.py",
        "steel_faults_viz.py",
        "vw_sample_data_viz.py",
    ]:
        source = (PROJECT_ROOT / relative_path).read_text()

        assert "dataframe_to_excel_download_link" in source
        assert "serialize_decision_tree" in source
        assert "def extract_tree_json" not in source
        assert "b64encode" not in source
