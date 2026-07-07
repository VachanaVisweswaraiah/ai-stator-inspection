import warnings

import joblib

from src.config.paths import PROJECT_ROOT
from src.models.registry import MODEL_ARTIFACTS


def test_model_artifact_registry_points_to_existing_files():
    assert MODEL_ARTIFACTS

    for artifact in MODEL_ARTIFACTS:
        assert artifact.path.is_file(), f"Missing model artifact: {artifact.name}"
        assert artifact.path.name == artifact.name
        assert artifact.depth > 0
        assert artifact.training_module
        assert artifact.training_function
        assert artifact.prediction_context


def test_registered_model_depths_match_committed_artifacts():
    for artifact in MODEL_ARTIFACTS:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model = joblib.load(artifact.path)

        assert model.get_params()["max_depth"] == artifact.depth


def test_model_artifact_documentation_matches_registry():
    documentation = (PROJECT_ROOT / "docs" / "model_artifacts.md").read_text()
    reproducibility = (PROJECT_ROOT / "docs" / "reproducibility.md").read_text()

    for artifact in MODEL_ARTIFACTS:
        assert artifact.name in documentation
        assert artifact.training_module in documentation
        assert artifact.training_function in documentation

    assert "docs/model_artifacts.md" in reproducibility
