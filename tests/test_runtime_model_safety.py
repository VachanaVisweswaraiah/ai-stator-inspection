import ast
import hashlib
import inspect

import joblib

from src.config.paths import DECISION_TREE_MODEL_PATH, PROJECT_ROOT
from src.models import (
    decision_tree,
    iris_tree,
    probabilistic_tree,
    steel_faults_tree,
    vw_sample_tree,
)
from src.models.persistence import save_model_artifact


TRAINING_FUNCTIONS = [
    decision_tree.Decision_Tress,
    probabilistic_tree.Probabilistic_Decision_Tree,
    iris_tree.Probabilistic_Decision_Tree_Iris,
    steel_faults_tree.Probabilistic_Decision_Tree_Steel_Faults,
    vw_sample_tree.Probabilistic_Decision_Tree_VW_Sample,
]


def _sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_training_workflows_default_to_in_memory_models():
    for training_function in TRAINING_FUNCTIONS:
        parameter = inspect.signature(training_function).parameters[
            "persist"
        ]
        assert parameter.default is False


def test_default_training_does_not_modify_committed_artifact(monkeypatch):
    saved_models = []
    monkeypatch.setattr(
        decision_tree,
        "save_model_artifact",
        lambda model, path: saved_models.append((model, path)),
    )
    checksum_before = _sha256(DECISION_TREE_MODEL_PATH)

    decision_tree.Decision_Tress(depth=2)

    assert saved_models == []
    assert _sha256(DECISION_TREE_MODEL_PATH) == checksum_before


def test_persistence_requires_explicit_opt_in(monkeypatch):
    saved_models = []
    monkeypatch.setattr(
        decision_tree,
        "save_model_artifact",
        lambda model, path: saved_models.append((model, path)),
    )

    result = decision_tree.Decision_Tress(depth=2, persist=True)

    assert len(saved_models) == 1
    assert saved_models[0][0] is result[5]
    assert saved_models[0][1] == DECISION_TREE_MODEL_PATH


def test_model_artifact_persistence_round_trip(tmp_path):
    artifact_path = tmp_path / "model.joblib"
    model = {"model": "test"}

    save_model_artifact(model, artifact_path)

    assert joblib.load(artifact_path) == model


def test_streamlit_workflows_use_one_in_memory_model_per_rerun():
    expectations = {
        "main.py": {
            "Decision_Tress": 1,
            "Probabilistic_Decision_Tree": 1,
        },
        "iris_viz.py": {
            "Probabilistic_Decision_Tree_Iris": 1,
        },
        "steel_faults_viz.py": {
            "Probabilistic_Decision_Tree_Steel_Faults": 1,
        },
        "vw_sample_data_viz.py": {
            "Probabilistic_Decision_Tree_VW_Sample": 1,
        },
    }

    for relative_path, expected_calls in expectations.items():
        tree = ast.parse((PROJECT_ROOT / relative_path).read_text())
        calls = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
        ]

        for function_name, expected_count in expected_calls.items():
            matching_calls = [
                call
                for call in calls
                if isinstance(call.func, ast.Name)
                and call.func.id == function_name
            ]
            assert len(matching_calls) == expected_count

        prediction_calls = [
            call
            for call in calls
            if isinstance(call.func, ast.Name)
            and call.func.id in {"predict_input", "predict_input_pdt"}
        ]
        assert prediction_calls
        assert all(len(call.args) == 2 for call in prediction_calls)
