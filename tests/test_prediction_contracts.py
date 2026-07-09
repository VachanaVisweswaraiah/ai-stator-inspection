import warnings

import joblib
import numpy as np
import pytest

from src.data.loaders import (
    load_fake_data,
    load_iris_data,
    load_steel_faults_data,
)
from src.models.registry import MODEL_ARTIFACTS


MANUFACTURING_FEATURES = [
    "box_hole_diameter",
    "box_hole_depth",
    "cylinder_diameter",
    "cylinder_height",
    "wire_diameter",
    "bed_distance",
]
IRIS_FEATURES = [
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm",
]
STEEL_FAULT_FEATURES = [
    "X_Minimum",
    "X_Maximum",
    "Y_Minimum",
    "Y_Maximum",
    "Pixels_Areas",
    "X_Perimeter",
    "Y_Perimeter",
    "Sum_of_Luminosity",
    "Minimum_of_Luminosity",
    "Maximum_of_Luminosity",
    "Length_of_Conveyer",
    "TypeOfSteel_A300",
    "TypeOfSteel_A400",
    "Steel_Plate_Thickness",
    "Edges_Index",
    "Empty_Index",
    "Square_Index",
    "Outside_X_Index",
    "Edges_X_Index",
    "Edges_Y_Index",
    "Outside_Global_Index",
    "LogOfAreas",
    "Log_X_Index",
    "Log_Y_Index",
    "Orientation_Index",
    "Luminosity_Index",
    "SigmoidOfAreas",
]


def _artifact(name):
    return next(artifact for artifact in MODEL_ARTIFACTS if artifact.name == name)


PREDICTION_CASES = [
    pytest.param(
        "decision_tree_model.joblib",
        load_fake_data,
        MANUFACTURING_FEATURES,
        {0, 1},
        id="manufacturing-decision-tree",
    ),
    pytest.param(
        "probabilistic_decision_tree_model.joblib",
        load_fake_data,
        MANUFACTURING_FEATURES,
        {0, 1},
        id="manufacturing-probabilistic-tree",
    ),
    pytest.param(
        "probabilistic_decision_tree_model_Iris.joblib",
        load_iris_data,
        IRIS_FEATURES,
        {0, 1, 2},
        id="iris-probabilistic-tree",
    ),
    pytest.param(
        "probabilistic_decision_tree_model_Steel_Faults.joblib",
        load_steel_faults_data,
        STEEL_FAULT_FEATURES,
        set(range(7)),
        id="steel-faults-probabilistic-tree",
    ),
]


@pytest.mark.parametrize(
    ("artifact_name", "dataset_loader", "feature_names", "expected_classes"),
    PREDICTION_CASES,
)
def test_committed_models_preserve_prediction_contracts(
    artifact_name,
    dataset_loader,
    feature_names,
    expected_classes,
):
    artifact = _artifact(artifact_name)
    sample = dataset_loader().loc[:, feature_names].head(5)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = joblib.load(artifact.path)

    assert list(model.feature_names_in_) == feature_names
    assert model.n_features_in_ == len(feature_names)
    assert set(model.classes_) == expected_classes

    predictions = model.predict(sample)
    probabilities = model.predict_proba(sample)

    assert predictions.shape == (len(sample),)
    assert set(predictions).issubset(expected_classes)
    assert probabilities.shape == (len(sample), len(expected_classes))
    np.testing.assert_allclose(probabilities.sum(axis=1), 1.0)
