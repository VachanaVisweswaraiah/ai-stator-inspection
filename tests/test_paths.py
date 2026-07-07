from pathlib import Path

from src.config import paths


def test_project_root_points_to_repository_root():
    assert paths.PROJECT_ROOT.is_absolute()
    assert (paths.PROJECT_ROOT / "README.md").is_file()
    assert (paths.PROJECT_ROOT / "app" / "streamlit_app.py").is_file()


def test_project_path_resolves_inside_repository():
    resolved_path = paths.project_path("fake_data.xlsx")

    assert isinstance(resolved_path, Path)
    assert resolved_path == paths.FAKE_DATA_PATH
    assert resolved_path.is_file()


def test_core_data_and_model_paths_are_absolute():
    core_paths = [
        paths.FAKE_DATA_PATH,
        paths.IRIS_DATA_PATH,
        paths.STEEL_FAULTS_DATA_PATH,
        paths.VW_SAMPLE_DATA_PATH,
        paths.DECISION_TREE_MODEL_PATH,
        paths.PROBABILISTIC_DECISION_TREE_MODEL_PATH,
        paths.IRIS_PROBABILISTIC_MODEL_PATH,
        paths.STEEL_FAULTS_PROBABILISTIC_MODEL_PATH,
    ]

    assert all(path.is_absolute() for path in core_paths)
